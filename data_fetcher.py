"""Data fetching utilities for Zootopia.

This module is responsible for loading API credentials from `.env` and
providing functions to fetch data from external services.
"""

import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=False)


API_KEY = os.getenv("NINJAS_API_KEY")

def call_api(name: str):
    """Call the API Ninjas animals endpoint with the given animal name.

    Parameters
    ----------
    name: str
        Animal name to search for.

    Returns
    -------
    list
        Parsed JSON list on success, or an empty list on error.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    try:
        response = requests.get(api_url, headers={"X-Api-Key": API_KEY}, timeout=15)
        if response.status_code == requests.codes.ok:
            return response.json()
        print("Error:", response.status_code, response.text)
    except requests.RequestException as exc:
        print("Network error:", exc)
    return []
