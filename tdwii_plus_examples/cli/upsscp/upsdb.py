"""Database interface for the upsscp application.

Unique Keys
-----------
* At each level one attribute is unique
* A unique key shall uniquely identify a single instance at a given level
* Unique keys **may** be in a C-FIND request's Identifier
* Unique keys **shall** be in a C-MOVE or C-GET request's Identifier
* C-FIND, C-GET and C-MOVE shall support existence and matching of all
* unique keys. All instances managed shall have specific non-zero length
  unique key values

Required Keys
-------------
* Multiple instances may have the same value for required keys.
* Required keys may be in a C-FIND request's Identifier
* Required keys shall not be in a C-GET or C-MOVE request's Identifier
"""

import sys
from collections import OrderedDict

try:
    from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
except ImportError:
    sys.exit("upsdb.py requires the sqlalchemy package")

from pydicom import dcmread
from pydicom.dataset import Dataset
from pynetdicom import build_context
from pynetdicom.sop_class import (
    PatientRootQueryRetrieveInformationModelFind,
    PatientRootQueryRetrieveInformationModelGet,
    PatientRootQueryRetrieveInformationModelMove,
    StudyRootQueryRetrieveInformationModelFind,
    StudyRootQueryRetrieveInformationModelGet,
    StudyRootQueryRetrieveInformationModelMove,
    UnifiedProcedureStepPull,
    UnifiedProcedureStepPush,
)
from sqlalchemy.orm import declarative_base


class InvalidIdentifier(Exception):
    pass


# C.2.2.2: The total length of the attribute may be larger than given in Part 5
# C.2.2.2: The VM may be larger than the VM from Part 6, depending
#   on the matching type

# VRs for supported elements - Part 5
# CS - 16 bytes maximum - str
# DA - 8 bytes fixed, format YYYYMMDD - str
# IS - 12 bytes maximum, range - int
# LO - 64 characters maximum - str
# PN - 64 characters maximum per component group (5 components per group) - str
# SH - 16 characters maximum - str
# TM - 14 bytes maximum, format HHMMSS.FFFFFF - str
# UI - 64 bytes maximum - str


# Translate from the element keyword to the db attribute
_TRANSLATION = {
    "PatientID": "patient_id",  # PATIENT | Unique | VM 1 | LO
    "PatientName": "patient_name",  # PATIENT | Required | VM 1 | PN
    "StudyInstanceUID": "study_instance_uid",  # STUDY | Unique | VM 1 | UI
    "StudyDate": "study_date",  # STUDY | Required | VM 1 | DA
    "StudyTime": "study_time",  # STUDY | Required | VM 1 | TM
    "AccessionNumber": "accession_number",  # STUDY | Required | VM 1 | SH
    "StudyID": "study_id",  # STUDY | Required | VM 1 | SH
    "SeriesInstanceUID": "series_instance_uid",  # SERIES | Unique | VM 1 | UI
    "Modality": "modality",  # SERIES | Required | VM 1 | CS
    "SeriesNumber": "series_number",  # SERIES | Required | VM 1 | IS
    "SOPInstanceUID": "sop_instance_uid",  # IMAGE | Unique | VM 1 | UI
    "InstanceNumber": "instance_number",  # IMAGE | Required | VM 1 | IS
    "ProcedureStepState": "procedure_step_state",  # Instance | VM 1 | CS
    "TransactionUID": "transaction_uid",  # Instance | Unique | VM 1 | UI
    "ScheduledProcedureStepStartDateTime": "start_date_time",  # Instance | Required | VM 1 | DT
    "ScheduledStationNameCodeSequence": "station_name",  # Instance | Required | VM 1 | SQ
    "ScheduledWorkitemCodeSequence": "work_item_code_value",  # Instance | Required | VM 1 | SQ
}

# Unique and required keys and their level, VR and VM for Patient Root
# Study Root is the same but includes the PATIENT attributes
_ATTRIBUTES = {
    "PatientID": ("PATIENT", "U", "LO", 1),
    "PatientName": ("PATIENT", "R", "PN", 1),
    "StudyInstanceUID": ("STUDY", "U", "UI", 1),
    "StudyDate": ("STUDY", "R", "DA", 1),
    "StudyTime": ("STUDY", "R", "TM", 1),
    "AccessionNumber": ("STUDY", "R", "SH", 1),
    "StudyID": ("STUDY", "R", "SH", 1),
    "SeriesInstanceUID": ("SERIES", "U", "UI", 1),
    "Modality": ("SERIES", "R", "VS", 1),
    "SeriesNumber": ("SERIES", "R", "IS", 1),
    "SOPInstanceUID": ("IMAGE", "U", "UI", 1),
    "InstanceNumber": ("IMAGE", "R", "UI", 1),
    "ProcedureStepState": ("INSTANCE", "U", "CS", 1),
    "TransactionUID": ("INSTANCE", "U", "UI", 1),
    "ScheduledProcedureStepStartDateTime": ("INSTANCE", "U", "DT", 1),
    "ScheduledStationNameCodeSequence": ("INSTANCE", "U", "SQ", 1),
    "ScheduledWorkitem​CodeSequence​": ("INSTANCE", "U", "SQ", 1),
}
_PATIENT_ROOT_ATTRIBUTES = OrderedDict(
    {
        "PATIENT": ["PatientID", "PatientName"],
        "STUDY": [
            "StudyInstanceUID",
            "StudyDate",
            "StudyTime",
            "AccessionNumber",
            "StudyID",
        ],
        "SERIES": ["SeriesInstanceUID", "Modality", "SeriesNumber"],
        "IMAGE": ["SOPInstanceUID", "InstanceNumber"],
    }
)
_STUDY_ROOT_ATTRIBUTES = OrderedDict(
    {
        "STUDY": [
            "StudyInstanceUID",
            "StudyDate",
            "StudyTime",
            "AccessionNumber",
            "StudyID",
            "PatientID",
            "PatientName",
        ],
        "SERIES": ["SeriesInstanceUID", "Modality", "SeriesNumber"],
        "IMAGE": ["SOPInstanceUID", "InstanceNumber"],
    }
)

_UPS_INSTANCE_KEYS = [
    "PatientID",
    "PatientName",
    "StudyInstanceUID",
    "ProcedureStepState",
    "TransactionUID",
    "ScheduledProcedureStepStartDateTime",
    "ScheduledStationNameCodeSequence",
    "ScheduledWorkitemCodeSequence",
    "SOPInstanceUID",
]

_UPS_ROOT_ATTRIBUTES = {
    "INSTANCE": _UPS_INSTANCE_KEYS,
}


# Supported Information Models
_C_FIND = [
    PatientRootQueryRetrieveInformationModelFind,
    StudyRootQueryRetrieveInformationModelFind,
]
_C_GET = [
    PatientRootQueryRetrieveInformationModelGet,
    StudyRootQueryRetrieveInformationModelGet,
]
_C_MOVE = [
    PatientRootQueryRetrieveInformationModelMove,
    StudyRootQueryRetrieveInformationModelMove,
]

_PATIENT_ROOT = {
    PatientRootQueryRetrieveInformationModelFind: _PATIENT_ROOT_ATTRIBUTES,
    PatientRootQueryRetrieveInformationModelGet: _PATIENT_ROOT_ATTRIBUTES,
    PatientRootQueryRetrieveInformationModelMove: _PATIENT_ROOT_ATTRIBUTES,
}
_STUDY_ROOT = {
    StudyRootQueryRetrieveInformationModelFind: _STUDY_ROOT_ATTRIBUTES,
    StudyRootQueryRetrieveInformationModelGet: _STUDY_ROOT_ATTRIBUTES,
    StudyRootQueryRetrieveInformationModelMove: _STUDY_ROOT_ATTRIBUTES,
}

_UPS_ROOT = {
    UnifiedProcedureStepPull: _UPS_ROOT_ATTRIBUTES,
}


def add_instance(ds, session, fpath=None):
    """Add a SOP Instance to the database or update existing instance.

    Parameters
    ----------
    ds : pydicom.dataset.Dataset
        The SOP Instance to be added to the database.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    fpath : str, optional
        The path to where the SOP Instance is stored, taken relative
        to the database file.
    """
    # Check if instance is already in the database
    result = session.query(Instance).filter(Instance.sop_instance_uid == ds.SOPInstanceUID).all()
    if result:
        instance = result[0]
    else:
        instance = Instance()

    # Unique or Required attributes
    required = [
        # (Instance attribute, DICOM keyword, max length, req'd)
        ("patient_id", "PatientID", 64, True),
        ("patient_name", "PatientName", 64, False),
        ("study_instance_uid", "StudyInstanceUID", 64, False),
        ("study_date", "StudyDate", 8, False),
        ("study_time", "StudyTime", 14, False),
        ("accession_number", "AccessionNumber", 16, False),
        ("study_id", "StudyID", 16, False),
        ("series_instance_uid", "SeriesInstanceUID", 64, False),
        ("modality", "Modality", 16, False),
        ("series_number", "SeriesNumber", None, False),
        ("sop_instance_uid", "SOPInstanceUID", 64, True),
        ("instance_number", "InstanceNumber", None, False),
        ("transaction_uid", "TransactionUID", 64, False),
        ("start_date_time", "ScheduledProcedureStepStartDateTime", 64, False),
        ("station_name", "ScheduledStationNameCodeSequence", 64, False),
        ("procedure_step_state", "ProcedureStepState", 16, False),
        ("work_item_code_value", "ScheduledWorkitemCodeSequence", 64, False),
    ]

    # Unique and Required attributes
    for attr, keyword, max_len, unique in required:
        if not unique and keyword not in ds:
            value = None
        else:
            elem = ds[keyword]
            if elem.VR == "SQ":
                value = elem[0].CodeValue
                if value is not None and attr in ["work_item_code_value"]:
                    designator = elem[0].CodingSchemeDesignator
                    addl_attr = "work_item_scheme_designator"
                    setattr(instance, addl_attr, designator)
                    meaning = elem[0].CodeMeaning
                    addl_attr = "work_item_meaning"
                    setattr(instance, addl_attr, meaning)
            else:
                value = elem.value
                if keyword == "ProcedureStepState":
                    if value is None:
                        value = "SCHEDULED"
                    elif value != "SCHEDULED":
                        raise InvalidIdentifier(f"ProcedureStepState via N-CREATE must be SCHEDULED, received {value}")

        if value is not None:
            # All supported attributes have VM 1
            # assert elem.VM == 1
            if max_len:
                if elem.VR == "PN":
                    value = str(value)

                assert len(value) <= max_len
            else:
                assert -(2**31) <= value <= 2**31 - 1

        setattr(instance, attr, value)

    instance.filename = fpath

    # Transfer Syntax UID
    try:
        tsyntax = ds.file_meta.TransferSyntaxUID
        if tsyntax:
            assert len(tsyntax) < 64
            instance.transfer_syntax_uid = tsyntax
    except (AttributeError, AssertionError):
        pass

    # SOP Class UID
    try:
        uid = ds.SOPClassUID
        if uid:
            assert len(uid) < 64
            instance.sop_class_uid = uid
    except (AttributeError, AssertionError):
        pass

    session.add(instance)
    session.commit()


def build_query(identifier, session, query=None):
    """Perform a query against the database.

    Parameters
    ----------
    identifier : pydicom.dataset.Dataset
        The request's *Identifier* dataset containing the query attributes.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        If not used then start a new query, otherwise extend the existing
        `query`.

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    # VRs for Single Value Matching and Wild Card Matching
    _text_vr = ["AE", "CS", "LO", "LT", "PN", "SH", "ST", "UC", "UR", "UT"]
    for elem in [e for e in identifier if e.keyword in _ATTRIBUTES]:
        vr = elem.VR
        val = elem.value
        # Convert PersonName3 to str
        if vr == "PN" and val:
            val = str(val)

        print(f"Searching based on element: {elem}")
        # Part 4, C.2.2.2.1 Single Value Matching
        if vr != "SQ" and val is not None:
            if vr in _text_vr and ("*" in val or "?" in val):
                pass
            elif vr in ["DA", "TM", "DT"] and "-" in val:
                pass
            else:
                print(f"Performing single value matching... {elem}")
                query = _search_single_value(elem, session, query)
                continue

        # Part 4, C.2.2.2.3 Universal Matching
        if val is None:
            print("Performing universal matching...")
            query = _search_universal(elem, session, query)
            continue

        # Part 4, C.2.2.2.2 List of UID Matching
        if vr == "UI":
            print("Performing list of UID matching...")
            query = _search_uid_list(elem, session, query)
            continue

        # Part 4, C.2.2.2.4 Wild Card Matching
        if vr in _text_vr and ("*" in val or "?" in val):
            print("Performing wildcard matching...")
            query = _search_wildcard(elem, session, query)
            continue

        # Part 4, C.2.2.2.5 Range Matching
        if vr in ["DT", "TM", "DA"] and "-" in val:
            query = _search_range(elem, session, query)
            continue

        # Part 4, C.2.2.2.6 Sequence Matching
        #   UPS has code sequences
        if vr == "SQ":
            print("Sequence Matching only partially supported")
            print(f"Sequence: {elem}")
            query = _search_sequence(elem, session, query)
            continue

    return query


def _check_identifier(identifier, model):
    """Check that the C-FIND, C-GET or C-MOVE `identifier` is valid.

    Parameters
    ----------
    identifier : pydicom.dataset.Dataset
        The *Identifier* dataset to check.
    model : pydicom.uid.UID
        The Query/Retrieve Information Model.

    Raises
    ------
    InvalidIdentifier
        If the Identifier is invalid.
    """
    # Part 4, C.4.1.1.3.1, C.4.2.1.4 and C.4.3.1.3.1:
    #   (0008,0052) Query Retrieve Level is required in the Identifier
    if "QueryRetrieveLevel" not in identifier:
        raise InvalidIdentifier("The Identifier contains no Query Retrieve Level element")

    if model in _PATIENT_ROOT:
        attr = _PATIENT_ROOT[model]
    else:
        attr = _STUDY_ROOT[model]

    levels = list(attr.keys())
    if identifier.QueryRetrieveLevel not in levels:
        raise InvalidIdentifier("The Identifier's Query Retrieve Level value is invalid")

    if len(identifier) == 1:
        raise InvalidIdentifier("The Identifier contains no keys")

    for ii, level in enumerate(levels):
        if level == identifier.QueryRetrieveLevel:
            # Check if identifier has elements below current level
            for sublevel in levels[ii + 1:]:
                if any([kw in identifier for kw in attr[sublevel]]):
                    raise InvalidIdentifier(
                        "The Identifier contains keys below the level " "specified by the Query Retrieve Level"
                    )

            # The level is the same as that in the identifier so we're OK
            return

        # The level is above that in the identifier so make sure the unique
        #   keyword is present
        if attr[level][0] not in identifier:
            raise InvalidIdentifier(f"The Identifier is missing a unique key for " f"the '{level}' level")


def clear(session):
    """Delete all entries from the database.

    Parameters
    ----------
    session : sqlalchemy.orm.session.Session
        The session we are using to clear the database.
    """
    for instance in session.query(Instance).all():
        session.delete(instance)

    session.commit()


def create(db_location, echo=False):
    """Create a new database at `db_location` if one doesn't already exist.

    Parameters
    ----------
    db_location : str
        The location of the database.
    echo : bool, optional
        Turn the sqlalchemy logging on (default ``False``).
    """
    engine = create_engine(db_location, echo=echo)

    # Create the tables (won't recreate tables already present)
    Base.metadata.create_all(engine)

    return engine


def remove_instance(instance_uid, session):
    """Remove a SOP Instance from the database.

    Parameters
    ----------
    instance_uid : pydicom.uid.UID
        The (0008,0018) *SOP Instance UID* of the SOP Instance to be removed
        from the database.
    session : sqlalchemy.orm.session.Session
        The session to use when querying the database for the instance.
    """
    matches = session.query(Instance).filter(Instance.sop_instance_uid == instance_uid).all()
    if matches:
        session.delete(matches[0])
        session.commit()


def search(model, identifier, session):
    """Search the database.

    Optional keys are not supported.

    Parameters
    ----------
    model : pydicom.uid.UID
        The Query/Retrieve Information Model. Supported models are:

        - *Patient Root Query Retrieve Information Model* for C-FIND, C-GET
          and C-MOVE
        - *Study Root Query Retrieve Information Model* for C-FIND, C-GET and
          C-MOVE
    identifier : pydicom.dataset.Dataset
        The Query/Retrieve request's *Identifier* dataset.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.

    Returns
    -------
    list of Instance
        The matching database Instances.

    Raises
    ------
    ValueError
        If the `identifier` is invalid.
    """
    if model not in [UnifiedProcedureStepPull, UnifiedProcedureStepPush]:
        raise ValueError(f"Unknown information model '{model}'")

    # Remove all optional keys, after this only unique/required will remain
    for elem in identifier:
        kw = elem.keyword
        if kw != "QueryRetrieveLevel" and kw not in _ATTRIBUTES:
            if elem.tag.element == 0:  # deletion by name fails for group length elements
                del identifier[elem.tag]
            else:
                delattr(identifier, kw)

    if model in _C_GET or model in _C_MOVE:
        # Part 4, C.2.2.1.2: remove required keys from C-GET/C-MOVE
        for kw, value in _ATTRIBUTES.items():
            if value[1] == "R" and kw in identifier:
                delattr(identifier, kw)

    return _search_qr(model, identifier, session)


def _search_qr(model, identifier, session):
    """Search the database using a Query/Retrieve *Identifier* query.

    Parameters
    ----------
    model : pydicom.uid.UID
        Either *Patient Root Query Retrieve Information Model* or *Study Root
        Query Retrieve Information Model* for C-FIND, C-GET or C-MOVE.
    identifier : pydicom.dataset.Dataset
        The request's *Identifier* dataset.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.

    Returns
    -------
    list of db.Instance
        The Instances that match the query.
    """
    # Will raise InvalidIdentifier if check failed
    # _check_identifier(identifier, model)

    # if model in _PATIENT_ROOT:
    #     attr = _PATIENT_ROOT[model]
    # else:
    #     attr = _STUDY_ROOT[model]
    attr = _UPS_ROOT[UnifiedProcedureStepPull]
    # Hierarchical search method: C.4.1.3.1.1
    query = None
    for level, keywords in attr.items():
        # Keywords at current level that are in the identifier
        keywords = [kw for kw in keywords if kw in identifier]
        # Create query dataset for only the current level and run it
        ds = Dataset()
        [setattr(ds, kw, getattr(identifier, kw)) for kw in keywords]
        query = build_query(ds, session, query)

        # if level == identifier.QueryRetrieveLevel:
        #    break

    return query.all()


def _search_range(elem, session, query=None):
    """Perform a range search for DA, DT and TM elements with '-' in them.

    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    # range matching
    #   <date1> - <date2>: matches any date within the range, inclusive
    #   - <date2>: match all dates prior to and including <date2>
    #   <date1> -: match all dates after and including <date1>
    #   <time>: if Timezone Offset From UTC included, values are in specified
    #   date: 20060705-20060707 + time: 1000-1800 matches July 5, 10 am to
    #       July 7, 6 pm.
    start, end = elem.value.split("-")
    attr = getattr(Instance, _TRANSLATION[elem.keyword])
    if not query:
        query = session.query(Instance)

    if start and end:
        return query.filter(attr >= start, attr <= end)
    elif start and not end:
        return query.filter(attr >= start)
    elif not start and end:
        return query.filter(attr <= end)

    raise ValueError("Invalid attribute value for range matching")


def _search_single_value(elem, session, query=None):
    """Perform a search using single value matching.

    Single value matching shall be performed if the value of an Attribute is
    non-zero length and the VR is not SQ and:

    * the VR is AE, CS, LO, LT, PN, SH, ST, UC, UR or UT and contains no wild
      card characters, or
    * the VR is DA, TM or DT and contains a single value with no "-", or
    * any other VR

    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    attr = getattr(Instance, _TRANSLATION[elem.keyword])
    if elem.VR == "PN":
        value = str(elem.value)
    else:
        value = elem.value

    if not query:
        query = session.query(Instance)

    return query.filter(attr == value)


def _search_uid_list(elem, session, query=None):
    """Search using an element containing a list of UIDs.

    A match against any of the UIDs is considered a positive result.

    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    if not elem.value:
        return _search_universal(elem, session, query)

    attr = getattr(Instance, _TRANSLATION[elem.keyword])
    if not query:
        query = session.query(Instance)

    if elem.VM == 1:
        return query.filter(attr == elem.value)

    return query.filter(attr.in_(elem.value))


def _search_universal(elem, session, query=None):
    """Perform a universal search for empty elements.

    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    # If the value is zero length then all entities shall match
    if not query:
        query = session.query(Instance)

    return query


def _search_wildcard(elem, session, query=None):
    """Perform a wildcard search.

    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    # Contains '*' or '?', case-sensitive if not PN
    #   '*' shall match any sequence of characters (incl. zero length)
    #   '?' shall match any single character
    attr = getattr(Instance, _TRANSLATION[elem.keyword])
    if elem.VR == "PN":
        value = str(elem.value)
    else:
        value = elem.value

    if value is None or value == "":
        value = "*"

    value = value.replace("*", "%")
    value = value.replace("?", "_")

    if not query:
        query = session.query(Instance)

    return query.filter(attr.like(value))


def _search_sequence(elem, session, query=None):
    """Perform a search using sequence matching.

    If a Key Attribute in the Identifier of a C-FIND request needs to be matched against an Attribute
    structured as a Sequence of Items (VR of SQ), the Key Attribute shall be structured as a Sequence of Items
    with a single Item. This Item may contain zero or more Item Key Attributes. Each Item Key Attribute matching
    shall be performed on an Item by Item basis.
    The types of matching defined in Section C.2.2.2 shall be used: Single Value Matching, List of UID Matching,
    Universal Matching, Wild Card Matching, Range Matching and Sequence Matching (recursive Sequence matching).
    If all the Item Key Attributes match, for at least one of the Items of the Attribute against which the match
    is performed, a successful match is generated. A sequence of matching Items containing only the requested
    Attributes is returned in the corresponding C-FIND responses.
    If the Key Attribute in the Identifier of a C-FIND request contains no Key Item Attribute (zero-length Item Tag),
    then all entities shall match this Attribute. This provides a Universal Matching like mechanism to request that the
    selected Key Attribute Value (the entire Sequence of Items) be returned in corresponding C-FIND responses.

    This search as initially implemented is currently woefully inadequate in meeting the expectations of the Standard.
    Single value matching is being performed on only a specific element in the Sequence, the CodeValue, and it is assuming
    the search sequence is a Code Sequence.


    Parameters
    ----------
    elem : pydicom.dataelem.DataElement
        The attribute to perform the search with.
    session : sqlalchemy.orm.session.Session
        The session we are using to query the database.
    query : sqlalchemy.orm.query.Query, optional
        An existing query within which this search should be performed. If
        not used then all the Instances in the database will be searched
        (default).

    Returns
    -------
    sqlalchemy.orm.query.Query
        The resulting query.
    """
    attr = getattr(Instance, _TRANSLATION[elem.keyword])
    value = None
    designator = None
    if elem.VR == "SQ":
        # this should always be VR of SQ for sequence matching
        print(f"Search sequence element: {elem}")
        print(f"{elem.keyword} maps to {attr}")
        if elem is not None:
            try:
                # for IHE-RO, only expect SEQUENCES in queries that are CodeSequence
                # namely Scheduled Station Name Code Sequence
                # Workitem Code Sequence
                value = elem[0].CodeValue
                print(f"Found code value: {value}")
            except Exception:
                pass

            try:
                # for IHE-RO, only expect SEQUENCES in queries that are CodeSequence
                # namely Scheduled Station Name Code Sequence should have 99IHERO2008 for the designator
                # and Workitem Code Sequence should have DCM for the designator
                # haven't figured out quite how to add the designator to the query yet.
                # maybe specify that attr as well and call query.filter(designator_attr == designator)?
                designator = elem[0].CodingSchemeDesignator  # noqa: F841
                print(f"Found coding scheme designator {designator}")

            except Exception:
                pass
    else:
        raise ValueError(elem.VR)

    if not query:
        query = session.query(Instance)
        print("Creating new Query")

    if value is None:
        print("value was none, not modifying query")
        return query

    print(f"Updating query to include {attr} == {value}")
    return query.filter(attr == value)


# Database table setup stuff
Base = declarative_base()


class Image(Base):
    __tablename__ = "image"
    # (0008,0018) SOP Instance UID | VR UI, VM 1, U
    sop_instance_uid = Column(String(64), primary_key=True)
    # (0020,0013) Instance Number | VR IS, VM 1, R
    instance_number = Column(Integer)


class Instance(Base):
    __tablename__ = "instance"

    # Absolute path to the stored SOP Instance
    filename = Column(String)
    # Transfer Syntax UID of the SOP Instance
    transfer_syntax_uid = Column(String(64))
    sop_class_uid = Column(String(64))
    transaction_uid = Column(String(64))

    station_name = Column(String(64))
    work_item_code_value = Column(String(64))  # needs to be matched in conjunction with the  scheme designator
    work_item_scheme_designator = Column(String(64))  # typically DCM, but could be 99IHERO2008 or other "private" schema
    work_item_meaning = Column(String(64))
    start_date_time = Column(String(64))
    procedure_step_state = Column(String(16))

    patient_id = Column(String, ForeignKey("patient.patient_id"))
    patient_name = Column(String, ForeignKey("patient.patient_name"))

    study_instance_uid = Column(String, ForeignKey("study.study_instance_uid"))
    # study_date = Column(String, ForeignKey("study.study_date"))
    # study_time = Column(String, ForeignKey("study.study_time"))
    # accession_number = Column(String, ForeignKey("study.accession_number"))
    # study_id = Column(String, ForeignKey("study.study_id"))

    # series_instance_uid = Column(String, ForeignKey("series.series_instance_uid"))
    # modality = Column(String, ForeignKey("series.modality"))
    # series_number = Column(String, ForeignKey("series.series_number"))

    sop_instance_uid = Column(
        String,
        ForeignKey("image.sop_instance_uid"),
        primary_key=True,
    )
    # instance_number = Column(String, ForeignKey("image.instance_number"))

    def as_identifier(self, identifier, model):
        """Return an Identifier dataset matching the elements from a query.

        Parameters
        ----------
        identifier : pydicom.dataset.Dataset
            The C-FIND, C-GET or C-MOVE request's *Identifier* dataset.
        model : pydicom.uid.UID
            The Query/Retrieve Information Model.

        Returns
        -------
        pydicom.dataset.Dataset
            The response *Identifier*.
        """
        ds = Dataset()
        ds = dcmread(self.sop_instance_uid, force=True)
        # ds.QueryRetrieveLevel = identifier.QueryRetrieveLevel

        # if model in _PATIENT_ROOT:
        #     attr = _PATIENT_ROOT[model]
        # else:
        #     attr = _STUDY_ROOT[model]
        attr = _UPS_ROOT[UnifiedProcedureStepPull]
        all_keywords = []
        for level, keywords in attr.items():
            all_keywords.extend(keywords)

        for kw in [kw for kw in all_keywords if kw in identifier]:
            try:
                attribute = _TRANSLATION[kw]
            except KeyError:
                continue

            setattr(ds, kw, getattr(self, attribute, None))

        return ds

    @property
    def context(self):
        """Return a presentation context for the Instance.

        Returns
        -------
        pynetdicom.presentation.PresentationContext

        Raises
        ------
        ValueError
            If either of the *SOP Class UID* or *Transfer Syntax UID* is not
            available for the Instance.
        """
        if None in [self.sop_class_uid, self.transfer_syntax_uid]:
            raise ValueError("Cannot determine which presentation context is required for " "for the SOP Instance")

        return build_context(self.sop_class_uid, self.transfer_syntax_uid)


class Patient(Base):
    __tablename__ = "patient"
    # (0010,0020) Patient ID | VR LO, VM 1, U
    patient_id = Column(String(64), primary_key=True)
    # (0010,0010) Patient's Name | VR PN, VM 1, R
    patient_name = Column(String(400))


class Series(Base):
    __tablename__ = "series"
    # (0020,000E) Series Instance UID | VR UI, VM 1, U
    series_instance_uid = Column(String(64), primary_key=True)
    # (0008,0060) Modality | VR CS, VM 1, R
    modality = Column(String(16))
    # (0020,0011) Series Number | VR IS, VM 1, R
    series_number = Column(Integer)


class Study(Base):
    __tablename__ = "study"
    # (0020,000D) Study Instance UID | VR UI, VM 1, U
    study_instance_uid = Column(String(64), primary_key=True)
    # (0008,0020) Study Date | VR DA, VM 1, R
    study_date = Column(String(8))
    # (0008,0030) Study Time | VR TM, VM 1, R
    study_time = Column(String(14))
    # (0008,0050) Accession Number | VR SH, VM 1, R
    accession_number = Column(String(16))
    # (0020,0010) Study ID | VR SH, VM 1, R
    study_id = Column(String(16))
