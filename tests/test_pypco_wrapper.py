#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

import logging
from typing import Generator
from unittest.mock import Mock, patch

from pypco import PCO, PCOCredentialsException
import pytest
from pytest import fixture

from pcoapi.pypco_wrapper import PyPcoWrapper

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


@fixture
def mock_pypco_pco() -> Generator[Mock, None, None]:
    yield Mock(spec=PCO)


@fixture
def pypco_wrapper_instance() -> Generator[PyPcoWrapper, None, None]:
    with patch("pcoapi.pypco_wrapper.pypco.PCO", autospec=True) as mock_pypco_pco:
        pypcowrapper_instance = PyPcoWrapper(application_id="1234", secret="5678")
        pypcowrapper_instance.api = mock_pypco_pco.return_value
    yield pypcowrapper_instance


class TestPyPcoWrapper:
    @pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
    def test_empty_init(self) -> None:
        with pytest.raises(PCOCredentialsException):
            PyPcoWrapper()

    @patch("pcoapi.pypco_wrapper.pypco.PCO", autospec=True)
    def test_init_with_api_key_and_secret(self, mock_pypco_pco: Mock) -> None:
        PyPcoWrapper(application_id="1234", secret="5678")
        args, kwargs = mock_pypco_pco.call_args
        assert kwargs["application_id"] == "1234"
        assert kwargs["secret"] == "5678"

    @patch("pcoapi.pypco_wrapper.pypco.PCO", autospec=True)
    def test_init_with_token(self, mock_pypco_pco: Mock) -> None:
        PyPcoWrapper(token="1234")
        args, kwargs = mock_pypco_pco.call_args
        assert kwargs["token"] == "1234"

    def test_request_response(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        # check if all args are passed on to the pypco.PCO.request method
        assert (
                pypco_wrapper_instance.request_response(
                    method="GET",
                    url="/services/v2/event_times",
                    payload=None,
                    upload=None,
                    params=None,
                )
                == pypco_wrapper_instance.pco.request_response.return_value
        )
        pypco_wrapper_instance.pco.request_response(
            method="GET",
            url="/services/v2/event_times",
            payload=None,
            upload=None,
            params=None,
        )

    def test_get(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.get(
                    url="/services/v2/event_times",
                    params="Test",
                )
                == pypco_wrapper_instance.pco.get.return_value
        )
        pypco_wrapper_instance.pco.get.assert_called_once_with(
            url="/services/v2/event_times", params="Test"
        )

    def test_post(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.post(
                    url="/services/v2/event_times",
                    payload={"Test": "Test"},
                    params="Test",
                )
                == pypco_wrapper_instance.pco.post.return_value
        )
        pypco_wrapper_instance.pco.post.assert_called_once_with(
            url="/services/v2/event_times", payload="Test", params="Test"
        )

    def test_patch(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.patch(
                    url="/services/v2/event_times",
                    payload={"Test": "Test"},
                    params="Test",
                )
                == pypco_wrapper_instance.pco.patch.return_value
        )
        pypco_wrapper_instance.pco.patch.assert_called_once_with(
            url="/services/v2/event_times", payload="Test", params="Test"
        )

    def test_delete(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.delete(
                    url="/services/v2/event_times",
                    params="Test",
                )
                == pypco_wrapper_instance.pco.delete.return_value
        )
        pypco_wrapper_instance.pco.delete.assert_called_once_with(
            url="/services/v2/event_times", params="Test"
        )

    def test_iterate(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.iterate(
                    url="/services/v2/event_times",
                    offset=1,
                    per_page=26,
                    params="Test",
                )
                == pypco_wrapper_instance.pco.iterate.return_value
        )
        pypco_wrapper_instance.pco.iterate.assert_called_once_with(
            url="/services/v2/event_times", offset=1, per_page=26, params="Test"
        )

    def test_upload(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.upload(
                    file_path="Test",
                    params="Test",
                )
                == pypco_wrapper_instance.pco.upload.return_value
        )
        pypco_wrapper_instance.pco.upload.assert_called_once_with(file_path="Test", params="Test")

    def test_template(self, pypco_wrapper_instance: PyPcoWrapper) -> None:
        assert (
                pypco_wrapper_instance.template(object_type="Test", attributes={"a": "b"})
                == pypco_wrapper_instance.pco.template.return_value
        )
        pypco_wrapper_instance.pco.template.assert_called_once_with(
            object_type="Test", attributes={"a": "b"}
        )
