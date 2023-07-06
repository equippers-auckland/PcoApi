"""
This implements all required endpoints for the PCO API
"""
from __future__ import annotations

from pcoapi.checkins import CheckIns
from pcoapi.people import People
from pcoapi.pypco_wrapper import PyPcoWrapper


class PcoApi:
    """
    This class implements all required endpoints for the PCO API
    """

    def __init__(
        self,
        application_id: str | None = None,  # pylint: disable=unsubscriptable-object
        secret: str | None = None,  # pylint: disable=unsubscriptable-object
        token: str | None = None,  # pylint: disable=unsubscriptable-object
    ):
        self.api = PyPcoWrapper(application_id=application_id, secret=secret, token=token)
        self.people = People(self.api)
        self.checkins = CheckIns(self.api)
