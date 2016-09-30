#!/usr/bin/env python

import requests
import argparse
import sys
import json
from utility.utils import *

# Use argparse library to parse optional arguments
# Default settings
#   Product: searches for time telling products (Watch and Clock)
#   Province: Yukon (no tax)
#   Filetype: json
# Only json parsing is available.
# This code could be built on to include XML and HTML parsing.

class Products:
    def __init__(self, product_type):
        self.product_type = product_type
        self.total_cost = 0
        self.subtotal = 0

    def json_calc_costs(self, province):
        page = 1
        catalogue_base = SHOPIFY_BASE + 'products.json?page='
        catalogue_url = catalogue_base + str(page)
        clock_sum = 0
        valid_page = True
        tax = get_provincial_tax(province) + GST

        while valid_page:
            catalogue = requests.get(catalogue_url, timeout=15.000)
            if catalogue.status_code == requests.codes.ok:
                json_c = catalogue.json()
                if type(json_c) == dict:
                    products = json_c['products']
                    if len(products) > 0:
                        for cat_product in products:
                            if str(cat_product['product_type']) in self.product_type:
                                print(str(cat_product['title']))
                                variants = cat_product['variants']
                                self.total_cost += self.__get_total_cost(variants, tax)
                                print('')
                    else:
                        valid_page = False
                        break
            page += 1
            catalogue_url = catalogue_base + str(page)

    def print_total(self):
        print("Total cost: $%.2f" % (self.total_cost))

    def print_subtotal(self):
        print("Subtotal: $%.2f" % (self.subtotal))
    
    # Considers the tax as a function of the product, not as a function of subtotal.
    def __get_total_cost(self, variants, tax):
        cost = 0
        cost_sum = 0

        for variant in variants:
            available = bool(variant['available'])
            taxable = bool(variant['taxable'])
            if available:
                subtotal = float(variant['price'])
                self.subtotal += subtotal
                if taxable:
                    cost = subtotal + (subtotal * tax)
                else:
                    cost = subtotal
            print("%-10s%5s%.2f" % (str(variant['title']), '$', cost))
            cost_sum += round(cost, 2)
        return cost_sum

def parse_args():
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Calculate the cost of products from a Shopify store.')
    store_params = arg_parser.add_argument_group(
        title='Store parsing configuration.')
    store_params.add_argument('--product', '-pd', default='Time',
        nargs='+', help='Type of product to parse.')
    # Could be a province containing multiple words, put in list.
    store_params.add_argument('--province', '-pr', default=['Yukon'],
        nargs='+', help='Province you are purchasing from.')
    store_params.add_argument('--filetype', '-f', default='json',
        help='File type to parse')
    args = arg_parser.parse_args()
    return args

# Format a list into a string with spaces between each entry
def list_to_string(l):
    result = ''
    for word in l:
        if len(result) == 0:
            result += word
        else:
            result += ' ' + word
    return result

# Creates a Products object and gets the costs by examining a json file.
def json_process(product, province):
    product_catalogue = Products(product)
    product_catalogue.json_calc_costs(province)

    product_catalogue.print_subtotal()
    product_catalogue.print_total()

def main():
    config = parse_args()
    if config.province:
        province = list_to_string(config.province)
        if province not in PROVINCES:
            sys.exit("Sorry, you have specified an undefined province.")
    if config.product not in PRODUCTS:
        sys.exit("Sorry, you have specified an undefined product type.")

    if config.filetype == 'json':
        print("Parsing JSON with product type %s" % (config.product))
        product = get_product_type((config.product).lower())
        json_process(product, province)
    elif config.filetype == 'html':
        sys.exit("Sorry, html parsing has not yet been implemented.")
    elif config.filetype == 'xml':
        sys.exit("Sorry, xml parsing has not yet been implemented.")
    else:
        sys.exit("Sorry, you have specified an undefined filetype.")

if __name__ == '__main__':
    main()
