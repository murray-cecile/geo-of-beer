##===================================================================##
# CRAFT BREWERY LOCATIONS: BREWER DB API
#
# Cecile Murray
# Date: October 2017
##===================================================================##

import csv
import sys
import requests
import json
import time
import pandas as pd
import numpy as np
import keys

# globals
API_KEY = keys.key_dict["BREWERYDB"]

BASE_URL = "http://api.brewerydb.com/v2"


# collates parameters with key, makes request, returns response as JSON
def get_from_bdb(endpt, options):

	options.update({'key': API_KEY})
	response = requests.get(BASE_URL + "/" + endpt, params=options)
	
	response.raise_for_status()

	return response.json()

# parse JSON dict and return nump array?
def parse_dict(json_dict):

	df = pd.DataFrame(json_dict)

	return df


if __name__ == '__main__':
	print("glory to AMR")