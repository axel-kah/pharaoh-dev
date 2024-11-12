from __future__ import annotations

import contextlib
import io
import traceback

import pharaoh.log
from pharaoh.assetlib.generation import register_asset

log = pharaoh.log.log


@contextlib.contextmanager
def catch_exceptions(
    catch: tuple[type[Exception], ...] = (Exception,),
    reraise: tuple[type[Exception], ...] = (),
    msg_prefix: str = "",
    log_exc: bool = True,
    render_exc: bool = True,
):
    """
    Catch exceptions of given types.

    :param catch: The exception types to catch
    :param msg_prefix: The message prefix to log before the exception message
    :param log_exc: Whether to log the exception message
    :param render_exc: Whether to render the exception traceback as an asset in the report
    """
    try:
        yield
    except reraise:
        raise
    except catch as e:
        if log_exc:
            log.error(f"{msg_prefix}{e}")
        if render_exc:
            register_asset(
                file="error.txt",
                template="error_traceback",
                data=io.BytesIO(traceback.format_exc(limit=-1).encode("utf-8")),
                metadata={"error_message": f"{msg_prefix}{e}", "asset_type": "error_traceback"},
            )
