#!/usr/bin/env python
"""watchscu

Used for registering AE's with UPS Watch
to subscribe for UPS Events
"""

import argparse
import os
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import Optional, Tuple

from pydicom import Dataset, dcmread
from pydicom.errors import InvalidDicomError
from pydicom.uid import UID
from pynetdicom import AE, Association, UnifiedProcedurePresentationContexts
from pynetdicom._globals import DEFAULT_MAX_LENGTH
from pynetdicom.apps.common import setup_logging
from pynetdicom.sop_class import UnifiedProcedureStepPush, UPSGlobalSubscriptionInstance

__version__ = "0.1.0"


def send_action(
    assoc: Association,
    class_uid: UID,
    instance_uid: UID,
    action_type=3,
    action_info=None,
) -> Tuple[Dataset, Optional[Dataset]]:
    """Send an N-ACTION request via `assoc`

    Parameters
    ----------
    assoc : association.Association
        The association sending the request.
    class_uid : pydicom.uid.UID
        The *Requested SOP Class UID* to use.
    instance_uid: pydicom.uid.UID
        The *Requested SOP Instance UID* to use.
    action_type : int, optional
        The *Action Type ID* to use.  default 3, global subscription
    action_info : None or pydicom.dataset.Dataset, optional
        The *Action Information* to use.
    """
    return assoc.send_n_action(action_info, action_type, class_uid, instance_uid)


def send_global_watch_registration(args: argparse.Namespace, assoc: Association, action_info: Dataset = None):
    """_summary_

    Args:
        args (argparse.Namespace): _description_
        assoc (Assocation): _description_
        action_info (Dataset, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    print(f"args: {args}")
    ds = action_info
    if ds is None:
        ds = Dataset()
        ds.DeletionLock = "FALSE"
        ds.RequestingAE = args.calling_aet
        ds.ReceivingAE = args.receiver_aet
        ds.RequestedSOPInstanceUID = UPSGlobalSubscriptionInstance
        ds.RequestedSOPClassUID = UnifiedProcedureStepPush
        # ds.RequestedSOPClassUID = UnifiedProcedureStepWatch
    return send_action(
        assoc=assoc,
        class_uid=ds.RequestedSOPClassUID,
        instance_uid=ds.RequestedSOPInstanceUID,
        action_type=3,
        action_info=ds,
    )


def _setup_argparser():
    """Setup the command line arguments"""
    # Description
    parser = argparse.ArgumentParser(
        description=("The watchscu application implements a Service Class User " "(SCU) for the UPS Watch Class. "),
        usage="watchscu [options] addr port",
    )

    # Parameters
    req_opts = parser.add_argument_group("Parameters")
    req_opts.add_argument("addr", help="TCP/IP address or hostname of DICOM peer", type=str)
    req_opts.add_argument("port", help="TCP/IP port number of peer", type=int)

    # General Options
    gen_opts = parser.add_argument_group("General Options")
    gen_opts.add_argument("--version", help="print version information and exit", action="store_true")
    output = gen_opts.add_mutually_exclusive_group()
    output.add_argument(
        "-q",
        "--quiet",
        help="quiet mode, print no warnings and errors",
        action="store_const",
        dest="log_type",
        const="q",
    )
    output.add_argument(
        "-v",
        "--verbose",
        help="verbose mode, print processing details",
        action="store_const",
        dest="log_type",
        const="v",
    )
    output.add_argument(
        "-d",
        "--debug",
        help="debug mode, print debug information",
        action="store_const",
        dest="log_type",
        const="d",
    )
    gen_opts.add_argument(
        "-ll",
        "--log-level",
        metavar="[l]",
        help=("use level l for the logger (critical, error, warn, info, debug)"),
        type=str,
        choices=["critical", "error", "warn", "info", "debug"],
    )

    # Configuration file Options
    fdir = os.path.abspath(os.path.dirname(__file__))
    fpath = os.path.join(fdir, "../config/default.ini")
    fabspath = os.path.abspath(fpath)
    gen_opts.add_argument(
        "-c",
        "--config",
        metavar="[f]ilename",
        help="use configuration file f",
        default=fabspath,
    )

    # Network Options
    net_opts = parser.add_argument_group("Network Options")
    net_opts.add_argument(
        "-aet",
        "--calling-aet",
        metavar="[a]etitle",
        help="set my calling AE title (default: WATCH_SCU)",
        type=str,
        default="WATCH_SCU",
    )
    net_opts.add_argument(
        "-aec",
        "--called-aet",
        metavar="[a]etitle",
        help="set called AE title of peer (default: UPSSCP)",
        type=str,
        default="UPSSCP",
    )
    net_opts.add_argument(
        "-aer",
        "--receiver-aet",
        metavar="[a]etitle",
        help="set receiver AE title of peer (default: NEVENT_RECEIVER)",
        type=str,
        default="NEVENT_RECEIVER",
    )
    net_opts.add_argument(
        "-ta",
        "--acse-timeout",
        metavar="[s]econds",
        help="timeout for ACSE messages (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-td",
        "--dimse-timeout",
        metavar="[s]econds",
        help="timeout for DIMSE messages (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-tn",
        "--network-timeout",
        metavar="[s]econds",
        help="timeout for the network (default: 30 s)",
        type=float,
        default=30,
    )
    net_opts.add_argument(
        "-pdu",
        "--max-pdu",
        metavar="[n]umber of bytes",
        help=(f"set max receive pdu to n bytes (0 for unlimited, " f"default: {DEFAULT_MAX_LENGTH})"),
        type=int,
        default=DEFAULT_MAX_LENGTH,
    )

    # Transfer Syntaxes
    ts_opts = parser.add_argument_group("Transfer Syntax Options")
    syntax = ts_opts.add_mutually_exclusive_group()
    syntax.add_argument(
        "-xe",
        "--request-little",
        help="request explicit VR little endian TS only",
        action="store_true",
    )
    syntax.add_argument(
        "-xb",
        "--request-big",
        help="request explicit VR big endian TS only",
        action="store_true",
    )
    syntax.add_argument(
        "-xi",
        "--request-implicit",
        help="request implicit VR little endian TS only",
        action="store_true",
    )

    # Misc Options
    # misc_opts = parser.add_argument_group("Miscellaneous Options")

    return parser.parse_args()


def get_contexts(fpaths, app_logger):
    """Return the valid DICOM files and their context values.

    Parameters
    ----------
    fpaths : list of str
        A list of paths to the files to try and get data from.

    Returns
    -------
    list of str, dict
        A list of paths to valid DICOM files and the {SOP Class UID :
        [Transfer Syntax UIDs]} that can be used to create the required
        presentation contexts.
    """
    good, bad = [], []
    contexts = {}
    for fpath in fpaths:
        path = os.fspath(Path(fpath).resolve())
        try:
            ds = dcmread(path)
        except Exception:
            bad.append(("Bad DICOM file", path))
            continue

        try:
            sop_class = ds.SOPClassUID
            tsyntax = ds.file_meta.TransferSyntaxUID
        except Exception:
            bad.append(("Unknown SOP Class or Transfer Syntax UID", path))
            continue

        tsyntaxes = contexts.setdefault(sop_class, [])
        if tsyntax not in tsyntaxes:
            tsyntaxes.append(tsyntax)

        good.append(path)

    for reason, path in bad:
        app_logger.error(f"{reason}: {path}")

    return good, contexts


def main(args=None):
    """Run the application."""
    if args is not None:
        sys.argv = args

    args = _setup_argparser()

    if args.version:
        print(f"watchscu.py v{__version__}")
        sys.exit()

    APP_LOGGER = setup_logging(args, "watchscu")
    APP_LOGGER.debug(f"watchscu.py v{__version__}")
    APP_LOGGER.debug("")

    APP_LOGGER.debug("Using configuration from:")
    APP_LOGGER.debug(f"  {args.config}")
    APP_LOGGER.debug("")
    config = ConfigParser()
    config.read(args.config)

    ae = AE(ae_title=args.calling_aet)
    ae.acse_timeout = args.acse_timeout
    ae.dimse_timeout = args.dimse_timeout
    ae.network_timeout = args.network_timeout

    # Propose the default presentation contexts
    # if args.request_little:
    #     transfer_syntax = [ExplicitVRLittleEndian]
    # elif args.request_big:
    #     transfer_syntax = [ExplicitVRBigEndian]
    # elif args.request_implicit:
    #     transfer_syntax = [ImplicitVRLittleEndian]
    # else:
    #     transfer_syntax = [
    #         ExplicitVRLittleEndian,
    #         ImplicitVRLittleEndian,
    #         ExplicitVRBigEndian,
    #     ]

    # Request association with remote
    assoc = ae.associate(
        args.addr,
        args.port,
        contexts=UnifiedProcedurePresentationContexts,
        ae_title=args.called_aet,
        max_pdu=args.max_pdu,
    )
    if assoc.is_established:
        try:
            status, response = send_global_watch_registration(args, assoc=assoc)
            print(f"Status: {status}  response {response}")
        except InvalidDicomError:
            APP_LOGGER.error("Bad DICOM: ")
        except Exception as exc:
            APP_LOGGER.error("Watch Registration (N-ACTION-RQ) failed")
            APP_LOGGER.exception(exc)

        assoc.release()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
