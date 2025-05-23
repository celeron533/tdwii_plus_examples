"""Unit tests for ncreatescu.py"""

import os
import subprocess
import sys
import time

import pytest
from pydicom import Dataset, dcmread
from pydicom.uid import (
    DeflatedExplicitVRLittleEndian,
    ExplicitVRBigEndian,
    ExplicitVRLittleEndian,
    ImplicitVRLittleEndian,
)
from pynetdicom import (
    AE,
    ALL_TRANSFER_SYNTAXES,
    UnifiedProcedurePresentationContexts,
    evt,
)
from pynetdicom.sop_class import UnifiedProcedureStepPush, Verification

# debug_logger()


APP_DIR = os.path.join(os.path.dirname(__file__), "../")
APP_FILE = os.path.join(APP_DIR, "./", "ncreatescu.py")
DATA_DIR = os.path.join(APP_DIR, "../", "responses", "dcm")
DATASET_FILE = os.path.join(DATA_DIR, "rsp000001.dcm")
LIB_DIR = os.path.join(APP_DIR, "../")


def start_ncreatescu(args):
    """Start the ncreatescu.py app and return the process."""
    pargs = [sys.executable, APP_FILE, "localhost", "11114"] + [*args]
    return subprocess.Popen(pargs)


# def start_ncreatescu_cli(args):
#     """Start the ncreatescu app using CLI and return the process."""
#     pargs = [sys.executable, "-m", "pynetdicom", "ncreatescu", "localhost", "11114"] + [
#         *args
#     ]
#     return subprocess.Popen(pargs)


def default_handle_ncreate(event):
    req = event.request
    # attr_list = event.attribute_list
    ds = Dataset()

    # Add the SOP Common module elements (Annex C.12.1)
    ds.AffectedSOPClassUID = UnifiedProcedureStepPush
    ds.AffectedSOPInstanceUID = req.AffectedSOPInstanceUID

    # Update with the requested attributes
    # ds.update(attr_list)
    ds.is_little_endian = True
    ds.is_implicit_VR = True
    ds.Status = 0x0000
    return ds, None


class ncreatescuBase:
    """Tests for ncreatescu.py"""

    def setup_method(self):
        """Run prior to each test"""
        self.ae = None
        self.func = None

    def teardown_method(self):
        """Clear any active threads"""
        if self.ae:
            self.ae.shutdown()

    def test_default(self):
        """Test default settings."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        # use attribute_list for N-CREATE vs  dataset for C-STORE
        assert events[0].attribute_list.PatientName == "head phantom^Hitachi"
        assert events[1].event == evt.EVT_RELEASED
        requestor = events[1].assoc.requestor
        assert "ncreatescu" == requestor.ae_title
        assert 16382 == requestor.maximum_length
        assert "ANY-SCP" == requestor.primitive.called_ae_title
        assert [] == requestor.extended_negotiation
        assert (1, 1) == requestor.asynchronous_operations
        assert {} == requestor.sop_class_common_extended
        assert {} == requestor.sop_class_extended
        assert requestor.user_identity is None
        cxs = requestor.primitive.presentation_context_definition_list
        assert len(cxs) == 5
        cxs = {cx.abstract_syntax: cx for cx in cxs}
        assert UnifiedProcedureStepPush in cxs
        assert cxs[UnifiedProcedureStepPush].transfer_syntax == [
            ExplicitVRLittleEndian,
            ImplicitVRLittleEndian,
            DeflatedExplicitVRLittleEndian,
            ExplicitVRBigEndian,
        ]

    def test_no_peer(self, capfd):
        """Test trying to connect to non-existent host."""
        p = self.func([DATASET_FILE])
        p.wait()
        out, err = capfd.readouterr()
        print(out)
        print(err)
        assert p.returncode == 1

        assert "Association request failed: unable to connect to remote" in err
        assert "TCP Initialisation Error" in err

    def test_flag_version(self, capfd):
        """Test --version flag."""
        p = self.func([DATASET_FILE, "--version"])
        p.wait()
        assert p.returncode == 0

        out, err = capfd.readouterr()
        assert "ncreatescu.py v" in out

    def test_flag_quiet(self, capfd):
        """Test --quiet flag."""
        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(Verification)
        scp = ae.start_server(("localhost", 11114), block=False)

        p = self.func([DATASET_FILE, "-q"])
        p.wait()
        assert p.returncode == 1

        out, err = capfd.readouterr()
        assert out == err == ""

        scp.shutdown()

    def test_flag_verbose(self, capfd):
        """Test --verbose flag."""

        def handle_create(event):
            return default_handle_ncreate(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-v"])
        p.wait()
        assert p.returncode == 0

        out, err = capfd.readouterr()
        assert "Requesting Association" in err
        assert "Association Accepted" in err
        assert "Sending Create Request" in err
        # assert "Received Store Response" in err
        assert "Releasing Association" in err
        assert "Accept Parameters" not in err

        scp.shutdown()

    def test_flag_debug(self, capfd):
        """Test --debug flag."""

        def handle_create(event):
            return default_handle_ncreate(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-d"])
        p.wait()
        assert p.returncode == 0

        out, err = capfd.readouterr()
        assert "Releasing Association" in err
        assert "Accept Parameters" in err

        scp.shutdown()

    def test_flag_log_collision(self):
        """Test error with -q -v and -d flag."""
        p = self.func([DATASET_FILE, "-v", "-d"])
        p.wait()
        assert p.returncode != 0

    @pytest.mark.skip("No way to test comprehensively")
    def test_flag_log_level(self):
        """Test --log-level flag."""
        pass

    def test_flag_aet(self):
        """Test --calling-aet flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-aet", "MYSCU"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        requestor = events[0].assoc.requestor
        assert "MYSCU" == requestor.ae_title

    def test_flag_aec(self):
        """Test --called-aet flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-aec", "YOURSCP"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        requestor = events[0].assoc.requestor
        assert "YOURSCP" == requestor.primitive.called_ae_title

    def test_flag_ta(self, capfd):
        """Test --acse-timeout flag."""
        events = []

        def handle_requested(event):
            events.append(event)
            time.sleep(0.1)

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_abort(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_ABORTED, handle_abort),
            (evt.EVT_REQUESTED, handle_requested),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-ta", "0.05", "-d"])
        p.wait()
        assert p.returncode == 1

        time.sleep(0.1)

        scp.shutdown()

        out, err = capfd.readouterr()
        assert "ACSE timeout reached while waiting for response" in err
        assert events[0].event == evt.EVT_REQUESTED
        assert events[1].event == evt.EVT_ABORTED

    def test_flag_td(self, capfd):
        """Test --dimse-timeout flag."""
        events = []

        def handle_create(event):
            events.append(event)
            time.sleep(0.1)
            return default_handle_ncreate(event)

        def handle_abort(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_ABORTED, handle_abort),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-td", "0.05", "-d"])
        p.wait()
        assert p.returncode == 0

        time.sleep(0.1)

        scp.shutdown()

        out, err = capfd.readouterr()
        assert "DIMSE timeout reached while waiting for message" in err
        assert events[0].event == evt.EVT_N_CREATE
        assert events[1].event == evt.EVT_ABORTED

    @pytest.mark.skip("Don't think this can be tested")
    def test_flag_tn(self, capfd):
        """Test --network-timeout flag."""
        pass

    def test_flag_max_pdu(self):
        """Test --max-pdu flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "--max-pdu", "123456"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        assert events[1].event == evt.EVT_RELEASED
        requestor = events[1].assoc.requestor
        assert 123456 == requestor.maximum_length

    def test_flag_xe(self):
        """Test --request-little flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-xe"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        assert events[0].attribute_list.PatientName == "head phantom^Hitachi"
        assert events[1].event == evt.EVT_RELEASED
        requestor = events[1].assoc.requestor
        cxs = requestor.primitive.presentation_context_definition_list
        assert len(cxs) == 5
        cxs = {cx.abstract_syntax: cx for cx in cxs}
        assert UnifiedProcedureStepPush in cxs
        assert cxs[UnifiedProcedureStepPush].transfer_syntax == [ExplicitVRLittleEndian]

    def test_flag_xi(self):
        """Test --request-implicit flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-xi"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert events[0].event == evt.EVT_N_CREATE
        assert events[0].attribute_list.PatientName == "head phantom^Hitachi"
        assert events[1].event == evt.EVT_RELEASED
        requestor = events[1].assoc.requestor
        cxs = requestor.primitive.presentation_context_definition_list
        cxs = requestor.primitive.presentation_context_definition_list
        assert len(cxs) == 5
        cxs = {cx.abstract_syntax: cx for cx in cxs}
        assert UnifiedProcedureStepPush in cxs
        assert cxs[UnifiedProcedureStepPush].transfer_syntax == [ImplicitVRLittleEndian]

    def test_flag_required_cx(self):
        """Test --required-contexts flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATASET_FILE, "-cx"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        ds = dcmread(DATASET_FILE)
        tsyntax = ds.file_meta.TransferSyntaxUID
        requestor = events[0].assoc.requestor
        cxs = requestor.primitive.presentation_context_definition_list
        assert len(cxs) == 1
        assert cxs[0].abstract_syntax == UnifiedProcedureStepPush
        assert cxs[0].transfer_syntax == [tsyntax]

    def test_bad_input(self, capfd):
        """Test being unable to read the input file."""
        p = self.func(["no-such-file.dcm", "-d"])
        p.wait()
        assert p.returncode == 0

        out, err = capfd.readouterr()
        assert "No suitable DICOM files found" in err
        assert "Cannot access path: no-such-file.dcm" in err

    def test_recurse(self, capfd):
        """Test the --recurse flag."""
        events = []

        def handle_create(event):
            events.append(event)
            return default_handle_ncreate(event)

        handlers = [
            (evt.EVT_N_CREATE, handle_create),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        for cx in UnifiedProcedurePresentationContexts:
            ae.add_supported_context(cx.abstract_syntax, ALL_TRANSFER_SYNTAXES)
        scp = ae.start_server(("localhost", 11114), block=False, evt_handlers=handlers)

        p = self.func([DATA_DIR, "--recurse", "-cx"])
        p.wait()
        assert p.returncode == 0

        scp.shutdown()

        assert len(events) == 1


class Testncreatescu(ncreatescuBase):
    """Tests for ncreatescu.py"""

    def setup_method(self):
        """Run prior to each test"""
        self.ae = None
        self.func = start_ncreatescu


# class TestncreatescuCLI(ncreatescuBase):
#     """Tests for ncreatescu using CLI"""

#     def setup_method(self):
#         """Run prior to each test"""
#         self.ae = None
#         self.func = start_ncreatescu_cli
