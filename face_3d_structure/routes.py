from flask import current_app as app
from flask import request, jsonify
from flask_api import status

from urllib.parse import urlparse as _urlparse
from re import match as _match


_check_referrer = True
_allowed_referrer_hosts = [
    r"^localhost.*$",
    r"^127\.0\.0\.1.*$",
]


def _validate_referrer(referrer):
    if referrer is not None:
        parsed = _urlparse(referrer)
        netloc = parsed.netloc
        for host_pattern in _allowed_referrer_hosts:
            if _match(host_pattern, netloc):
                return

    return jsonify(message="invalid access"), status.HTTP_403_FORBIDDEN


@app.before_request
def check_origin():
    if app.env == "development":
        return

    if _check_referrer:
        referrer = request.referrer
        return _validate_referrer(referrer)
