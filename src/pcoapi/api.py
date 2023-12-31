"""
This implements all required endpoints for the PCO API
"""
from __future__ import annotations

from pcoapi.checkins import CheckIns
from pcoapi.groups import TopLevelGroups
from pcoapi.people import TopLevelPeople
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
        self.people = TopLevelPeople(self.api)
        self.checkins = CheckIns(self.api)
        self.groups = TopLevelGroups(self.api)
