#!/usr/bin/env python

"""
ASIN Lookup on Amazon.com
"""

import sys
import urllib2
import copy
from bs4 import BeautifulSoup

# Query ASIN on Amazon


def asin_lookup(product_name):


    # Convert spaces to pluses
    query_product_name = product_name.replace(' ', '+')

    # Query the movie title on Amazon.com
    asin_query_url = "http://www.amazon.com/s/?url=search-alias%3Daps&field-keywords=" + query_product_name + "&rh=i%3Aaps%2Ck%3A" + query_product_name

    try:
        soup = BeautifulSoup(urllib2.urlopen(asin_query_url))
    except urllib2.HTTPError:
        print("URL could not be opened")
        return None
    else:
        # Look through first three results
        for i in range(0, 5):

            query_result = soup.find(id="result_" + str(i))

            # Get ASIN
            query_result_asin = copy.copy(query_result)
            matched_asin_string = query_result_asin.get('name')

            # Get Product Name
            query_result_title = copy.copy(query_result)
            matched_product_name = query_result_title.find("div", attrs={'class': 'productTitle'}).get_text()

            print(matched_asin_string + " - " + matched_product_name + "\n")

    return


def main(argv=None):
    if argv is None:
        argv = sys.argv

    #0 Parse options and user input
    if len(argv) < 2:
        print("Please enter product name to lookup")
        exit()

    product_name = argv[1]

    #1 Query for keywords
    asin_lookup(product_name)

if __name__ == "__main__":
    sys.exit(main())
