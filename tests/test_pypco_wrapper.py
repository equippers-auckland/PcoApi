#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta
from unittest.mock import MagicMock, Mock, patch

import pytest
from pypco import PCO, PCOCredentialsException
from pytest import fixture

from PcoApi.pypco_wrapper import PyPcoWrapper

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


@fixture
def mock_pypco_pco():
    yield Mock(spec=PCO)


@fixture
def pcpco_wrapper_instance():
    with patch("PcoApi.pypco_wrapper.pypco.PCO", autospec=True) as mock_pypco_pco:
        pypcowrapper_instance = PyPcoWrapper(application_id="1234", secret="5678")
        pypcowrapper_instance.api = mock_pypco_pco.return_value
    yield pypcowrapper_instance


class TestPyPcoWrapper:
    def test_empty_init(self):
        with pytest.raises(PCOCredentialsException):
            PyPcoWrapper()

    @patch("PcoApi.pypco_wrapper.pypco.PCO", autospec=True)
    def test_init_with_api_key_and_secret(self, mock_pypco_pco: Mock):
        PyPcoWrapper(application_id="1234", secret="5678")
        args, kwargs = mock_pypco_pco.call_args
        assert kwargs["application_id"] == "1234"
        assert kwargs["secret"] == "5678"

    @patch("PcoApi.pypco_wrapper.pypco.PCO", autospec=True)
    def test_init_with_token(self, mock_pypco_pco: Mock):
        PyPcoWrapper(token="1234")
        args, kwargs = mock_pypco_pco.call_args
        assert kwargs["token"] == "1234"

    def test_request_response(self, pcpco_wrapper_instance: PyPcoWrapper):
        # check if all args are passed on to the pypco.PCO.request method
        assert (
            pcpco_wrapper_instance.request_response(
                method="GET",
                url="/services/v2/event_times",
                payload=None,
                upload=None,
                params=None,
            )
            == pcpco_wrapper_instance.api.request_response.return_value
        )
        pcpco_wrapper_instance.api.request_response(
            method="GET",
            url="/services/v2/event_times",
            payload=None,
            upload=None,
            params=None,
        )

    def test_get(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.get(
                url="/services/v2/event_times",
                params="Test",
            )
            == pcpco_wrapper_instance.api.get.return_value
        )
        pcpco_wrapper_instance.api.get.assert_called_once_with(url="/services/v2/event_times", params="Test")

    def test_post(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.post(
                url="/services/v2/event_times",
                payload="Test",
                params="Test",
            )
            == pcpco_wrapper_instance.api.post.return_value
        )
        pcpco_wrapper_instance.api.post.assert_called_once_with(
            url="/services/v2/event_times", payload="Test", params="Test"
        )

    def test_patch(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.patch(
                url="/services/v2/event_times",
                payload="Test",
                params="Test",
            )
            == pcpco_wrapper_instance.api.patch.return_value
        )
        pcpco_wrapper_instance.api.patch.assert_called_once_with(
            url="/services/v2/event_times", payload="Test", params="Test"
        )

    def test_delete(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.delete(
                url="/services/v2/event_times",
                params="Test",
            )
            == pcpco_wrapper_instance.api.delete.return_value
        )
        pcpco_wrapper_instance.api.delete.assert_called_once_with(url="/services/v2/event_times", params="Test")

    def test_iterate(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.iterate(
                url="/services/v2/event_times",
                offset=1,
                per_page=26,
                params="Test",
            )
            == pcpco_wrapper_instance.api.iterate.return_value
        )
        pcpco_wrapper_instance.api.iterate.assert_called_once_with(
            url="/services/v2/event_times", offset=1, per_page=26, params="Test"
        )

    def test_upload(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.upload(
                file_path="Test",
                params="Test",
            )
            == pcpco_wrapper_instance.api.upload.return_value
        )
        pcpco_wrapper_instance.api.upload.assert_called_once_with(file_path="Test", params="Test")

    def test_template(self, pcpco_wrapper_instance: PyPcoWrapper):
        assert (
            pcpco_wrapper_instance.template(object_type="Test", attributes={"a": "b"})
            == pcpco_wrapper_instance.api.template.return_value
        )
        pcpco_wrapper_instance.api.template.assert_called_once_with(object_type="Test", attributes={"a": "b"})
