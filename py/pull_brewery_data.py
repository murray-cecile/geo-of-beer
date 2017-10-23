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

STATE_LIST = [Alabama, Connecticut, Georgia, Illinois, Indiana, Iowa,
			  Kentucky, Maryland, Massachusetts, Michigan, Minnesota,
			  Missouri, New Jersey, New York, Ohio, Pennsylvania,
			  Rhode Island, Texas, Virginia, Wisconsin
			  ]

# collates parameters with key, makes request, returns response as JSON
def get_from_bdb(endpt, options):

	options.update({'key': API_KEY})
	response = requests.get(BASE_URL + "/" + endpt, params=options)
	
	response.raise_for_status()

	return response.json()

# extract latitude longitude tuples from JSON response
def extract_lat_lon(response):

	rv = []

	for i in 1:len(response['data']):
		rv.append((response['data'][i]['latitude'], response['data'][i]['longitude']))

	return rv

# loop through state lists, make API requests
def pull_multiple_states(STATE_LIST, endpt, options):

	# initialize RV here

	for s in STATE_LIST:

		options['region'] = s
		r = get_from_bdb(endpt, options)

		# extract relevant info
		lat_lon = extract_lat_lon(r)
		brand_class = r['brewery']


	return #data structure

if __name__ == '__main__':
	print("glory to AMR")