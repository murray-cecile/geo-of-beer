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

STATE_LIST = ['Alabama', 'Connecticut', 'Georgia', 'Illinois', 'Indiana', 'Iowa',
			  'Kentucky', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
			  'Missouri', 'New Jersey', 'New York', 'Ohio', 'Pennsylvania',
			  'Rhode Island', 'Texas', 'Virginia', 'Wisconsin'
			  ]

# collates parameters with key, makes request, returns response as JSON
def get_from_bdb(endpt, options):

	options.update({'key': API_KEY})
	response = requests.get(BASE_URL + "/" + endpt, params = options)
	
	response.raise_for_status()

	return response.json()

# extract relevant data from JSON response as pandas data.frame
def extract_data(response):

	# extract relevant info from first level
	st_data = pd.DataFrame(response['data'])
	st_data = st_data.drop(['brewery', 'country'], axis = 1)

	# extract data from brewery subdict
	detail = []
	for i in range(0, len(response['data'])):
		detail.append(pd.DataFrame(response['data'][i]['brewery'],
			index = response['data'][i]['brewery'].keys()))
	brew_detail = pd.concat(detail, keys = detail[1].index)

	# concatenate data frames
	rv = pd.concat([st_data, brew_detail], axis = 0, ignore_index = True)
	
	return rv

# loop through state lists, make API requests
def pull_all_states(endpt, num_pages, options):

	df_list = []
	options = {}

	for p in range(1, num_pages):

		options.update({'p':p})
		r = get_from_bdb(endpt, options)
		
		st_df = extract_data(r)
		df_list.append(st_df)

	return df_list

if __name__ == '__main__':

	num_pages = get_from_bdb("locations", {})['numberOfPages']
	oic_data = pull_all_states("locations", num_pages, {})

	master = oic_data[0]
	master.append(oic_Data[1:len(oic_data)], ignore_index=True)

	print("glory to AMR")