"""
This implements all required enpdoints for the PCO API
"""
from typing import Optional
from PcoApi.pypco_wrapper import PyPcoWrapper


class PcoApi(PyPcoWrapper):
    """
    This class implements all required endpoints for the PCO API
    """

    def __init__(
        self,
        application_id: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        secret: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        token: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        cc_name: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        api_base: str = "https://api.planningcenteronline.com",
        timeout: int = 60,
        upload_url: str = "https://upload.planningcenteronline.com/v2/files",
        upload_timeout: int = 300,
        timeout_retries: int = 3,
    ):
        super().__init__(
            application_id, secret, token, cc_name, api_base, timeout, upload_url, upload_timeout, timeout_retries
        )

    def get_people(self, **kwargs) -> dict:
        return self.get("/people/v2/people", **kwargs)
