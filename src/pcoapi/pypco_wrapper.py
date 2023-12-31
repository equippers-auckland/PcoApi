"""
Wrapper for the pypco library
"""
from __future__ import annotations

from typing import Any, Iterator

import pypco
import requests

from pcoapi.helpers import PcoParamsType, PcoResponseType


# noinspection Mypy
class OverloadedPco(pypco.PCO):  # type: ignore
    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        super().__init__(*args, **kwargs)

    def get(self, url: str, **params) -> PcoResponseType:  # type: ignore
        if params is None:
            params = {}
        if "per_page" not in params:
            params["per_page"] = 100
        response: PcoResponseType = super().get(url, **params)
        if "links" not in response:
            return response
        if "next" in response["links"]:
            next_url = response["links"]["next"]
            next_response = self.get(next_url, **params)
            response["data"] = response["data"].__add__(next_response["data"])  # type: ignore
        return response

    def limited_get(self, url: str, **params: PcoParamsType) -> PcoResponseType:
        response: PcoResponseType = super().get(url, **params)
        return response


# noinspection Mypy
class PyPcoWrapper:
    """
    Wrapper Class for the pypco library
    """

    def __init__(
        self,
        application_id: str | None = None,  # pylint: disable=unsubscriptable-object
        secret: str | None = None,  # pylint: disable=unsubscriptable-object
        token: str | None = None,  # pylint: disable=unsubscriptable-object
    ):
        api_base: str = "https://api.planningcenteronline.com"
        timeout: int = 60
        upload_url: str = "https://upload.planningcenteronline.com/v2/files"
        upload_timeout: int = 300
        timeout_retries: int = 3
        self.pco = OverloadedPco(
            application_id=application_id,
            secret=secret,
            token=token,
            api_base=api_base,
            timeout=timeout,
            upload_url=upload_url,
            upload_timeout=upload_timeout,
            timeout_retries=timeout_retries,
        )

    def request_response(
        self,
        method: str,
        url: str,
        payload: Any | None | None = None,  # pylint: disable=unsubscriptable-object
        upload: str | None = None,  # pylint: disable=unsubscriptable-object
        **params: PcoParamsType,
    ) -> requests.Response:
        """A generic entry point for making a managed request against PCO.

        This function will return a Requests response object, allowing access to
        all request data and metadata. Executed request could be one of the standard
        HTTP verbs or a file upload. If you're just looking for your data (json), use
        the request_json() function or get(), post(), etc.

        Args:
            method (str): The HTTP method to use for this request.
            url (str): The URL against which this request will be executed.
            payload (obj): A json-serializable Python object to be sent as the post/put payload.
            upload (str): The path to a file to upload.
            params (obj): A dictionary or list of tuples or bytes to send in the query string.

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            requests.Response: The response to this request.
        """

        return self.pco.request_response(  # type: ignore
            method=method, url=url, payload=payload, upload=upload, **params
        )

    def request_json(
        self,
        method: str,
        url: str,
        payload: Any | None = None,  # pylint: disable=unsubscriptable-object
        upload: str | None = None,  # pylint: disable=unsubscriptable-object
        **params: PcoParamsType,
    ) -> dict[Any, Any] | None:  # pylint: disable=unsubscriptable-object
        """A generic entry point for making a managed request against PCO.

        This function will return the payload from the PCO response (a dict).

        Args:
            method (str): The HTTP method to use for this request.
            url (str): The URL against which this request will be executed.
            payload (obj): A json-serializable Python object to be sent as the post/put payload.
            upload (str): The path to a file to upload.
            params (obj): A dictionary or list of tuples or bytes to send in the query string.

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            dict: The payload from the response to this request.
        """

        return self.pco.request_json(  # type: ignore
            method=method, url=url, payload=payload, upload=upload, **params
        )

    def get(
        self, url: str, **params: PcoParamsType
    ) -> PcoResponseType:  # pylint: disable=unsubscriptable-object
        """Perform a GET request against the PCO API.

        Performs a fully managed GET request (handles ratelimiting, timeouts, etc.).

        Args:
            url (str): The URL against which to perform the request. Can include
                what's been set as api_base, which will be ignored if this value is also
                present in your URL.
            params: Any named arguments will be passed as query parameters.

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            dict: The payload returned by the API for this request.
        """
        return self.pco.get(url=url, **params)

    def limited_get(self, url: str, **params: PcoParamsType) -> PcoResponseType:
        return self.pco.limited_get(url=url, **params)

    def post(
        self,
        url: str,
        payload: dict | None = None,  # type: ignore
        **params: PcoParamsType,  # pylint: disable=unsubscriptable-object
    ) -> dict | None:  # type: ignore  # pylint: disable=unsubscriptable-object
        """Perform a POST request against the PCO API.

        Performs a fully managed POST request (handles ratelimiting, timeouts, etc.).

        Args:
            url (str): The URL against which to perform the request. Can include
                what's been set as api_base, which will be ignored if this value is also
                present in your URL.
            payload (dict): The payload for the POST request. Must be serializable to JSON!
            params: Any named arguments will be passed as query parameters. Values must
                be of type str!

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            dict: The payload returned by the API for this request.
        """

        return self.pco.post(url=url, payload=payload, **params)  # type: ignore

    def patch(
        self,
        url: str,
        payload: dict | None = None,  # type: ignore
        **params: PcoParamsType,  # pylint: disable=unsubscriptable-object
    ) -> dict | None:  # type: ignore  # pylint: disable=unsubscriptable-object
        """Perform a PATCH request against the PCO API.

        Performs a fully managed PATCH request (handles ratelimiting, timeouts, etc.).

        Args:
            url (str): The URL against which to perform the request. Can include
                what's been set as api_base, which will be ignored if this value is also
                present in your URL.
            payload (dict): The payload for the PUT request. Must be serializable to JSON!
            params: Any named arguments will be passed as query parameters. Values must
                be of type str!

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            dict: The payload returned by the API for this request.
        """

        return self.pco.patch(url=url, payload=payload, **params)  # type: ignore

    def delete(self, url: str, **params: PcoParamsType) -> requests.Response:
        """Perform a DELETE request against the PCO API.

        Performs a fully managed DELETE request (handles ratelimiting, timeouts, etc.).

        Args:
            url (str): The URL against which to perform the request. Can include
                what's been set as api_base, which will be ignored if this value is also
                present in your URL.
            params: Any named arguments will be passed as query parameters. Values must
                be of type str!

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            requests.Response: The response object returned by the API for this request.
            A successful delete request will return a response with an empty payload,
            so we return the response object here instead.
        """

        return self.pco.delete(url=url, **params)  # type: ignore

    def iterate(
        self, url: str, offset: int = 0, per_page: int = 25, **params: str
    ) -> Iterator[dict[str, object]]:  # pylint: disable=too-many-branches
        """Iterate a list of objects in a response, handling pagination.

        Basically, this function wraps get in a generator function designed for
        processing requests that will return multiple objects. Pagination is
        transparently handled.

        Objects specified as includes will be injected into their associated
        object and returned.

        Args:
            url (str): The URL against which to perform the request. Can include
                what's been set as api_base, which will be ignored if this value is also
                present in your URL.
            offset (int): The offset at which to start. Usually going to be 0 (the default).
            per_page (int): The number of results that should be requested in a single page.
                Valid values are 1 - 100, defaults to the PCO default of 25.
            params: Any additional named arguments will be passed as query parameters. Values must
                be of type str!

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Yields:
            dict: Each object returned by the API for this request. Returns "data",
                "included", and "meta" nodes for each response. Note that data is processed
                somewhat before being returned from the API. Namely, includes are injected into
                the object(s) with which they are associated.
                This makes it easier to process includes associated with specific objects
                since they are accessible directly from each returned object.
        """

        return self.pco.iterate(  # type: ignore
            url=url, offset=offset, per_page=per_page, **params
        )

    def upload(
        self, file_path: str, **params: PcoParamsType
    ) -> dict | None:  # type: ignore # pylint: disable=unsubscriptable-object
        """Upload the file at the specified path to PCO.

        Args:
            file_path (str): The path to the file to be uploaded to PCO.
            params : Any named arguments will be passed as query parameters. Values must
                be of type str!

        Raises:
            PCORequestTimeoutException: The request to PCO timed out the maximum number of
                times.
            PCOUnexpectedRequestException: An unexpected error occurred when making your
                request.
            PCORequestException: The response from the PCO API indicated an error with your
                request.

        Returns:
            dict: The PCO response from the file upload.
        """

        return self.pco.upload(file_path=file_path, **params)  # type: ignore

    def template(
        self, object_type: str, attributes: dict | None = None  # type: ignore
    ) -> dict:  # type: ignore # pylint: disable=unsubscriptable-object
        """Get template JSON for creating a new object.

        Args:
            object_type (str): The type of object to be created.
            attributes (dict): The new objects attributes. Defaults to empty.

        Returns:
            dict: A template from which to set the new object's attributes.
        """
        return self.pco.template(object_type=object_type, attributes=attributes)  # type: ignore
