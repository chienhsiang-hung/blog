import logging
import requests
from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.DEBUG)

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

session.get('http://httpstat.us/503')