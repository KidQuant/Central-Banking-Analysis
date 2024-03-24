import os
import pickle
import re
import sys
import threading

import numpy as np
import pandas as pd
import requests
import textract
from bs4 import BeautifulSoup
from datatime import datetime

from .FomcBase import FomcBase


class FomcMeetingScript(FomcBase):
    """
    A convenient class for extracting meeting scripts from the FOMC website.
    FOMC publishes the meeting scripts after 5 years, so this cannot be used
    for the prediction of the monetary policy in real-time.

    Example Usage:
        fomc = FomcMeetingScript()
        df = fomc.get_contents()
    """

    def __init__(self, verbose=True, max_threads=10, base_dir="../data/FOMC/"):
        super().__init__("meeting_script", verbose, max_threads, base_dir)

    def _get_links(self, from_year):
        """
        Override private function
        """
