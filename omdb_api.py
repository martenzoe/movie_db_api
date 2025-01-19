"""Module for interacting with the OMDb API."""

import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, Any

load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"

def get_movie_info(title: str) -> Optional[Dict[str, Any]]:
    """
    Fetch movie information from the OMDb API.

    Args:
        title (str): The title of the movie to search for.

    Returns:
        Optional[Dict[str, Any]]: A dictionary containing movie information,
                                  or None if an error occurred.
    """
    params = {
        "apikey": API_KEY,
        "t": title
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API access error: {e}")
        return None
