import json
from os import environ
from pathlib import Path

from dotenv import load_dotenv
from faker import Faker
import requests

from pcoapi.api import PcoApi

fake = Faker()


def main() -> None:
    load_dotenv()
    api = PcoApi(application_id=environ["PCO_USER"], secret=environ["PCO_PASSWD"])
    endpoint = "/check-ins/v2/event_times/32690292/headcounts"
    target_file = "get_eventtime_headcounts.json"
    response = api.api.get(endpoint)
    randomized_response = randomize_data(response)
    write_test_data_to_file(target_file, randomized_response)


def randomize_data(response: requests.Request) -> requests.Request:
    return response
    data_path = response["data"]
    for field in data_path:
        field["relationships"]["event"]["data"]["id"] = str(1234)
    return response


def write_test_data_to_file(filename: str, data: requests.Request) -> None:
    path = "../tests/test_data/"
    with Path(path + filename).open() as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
