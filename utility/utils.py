SHOPIFY_BASE = 'http://shopicruit.myshopify.com/'
PARSE_TYPE = ['xml', 'json', 'html']
GST = 0.05
PROVINCES = [
    "Manitoba",
    "British Columbia",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Nova Scotia",
    "Nunavut",
    "Ontario",
    "Prince Edward Island",
    "Quebec",
    "Saskatchewan",
    "Yukon"
]
PRODUCTS = [
    "Time",
    "Apparel",
    "Accessory",
    "Furniture",
    "Kitchen",
    "Electronic",
    "Automobile"
]


def get_provincial_tax(province):
    provinces = [
        {"province":"Alberta", "sales_tax":0},
        {"province":"British Columbia", "sales_tax":0.07},
        {"province":"Manitoba", "sales_tax": 0.08},
        {"province":"New Brunwsick", "sales_tax":0.10},
        {"province":"Newfoundland and Labrador", "sales_tax":0.08},
        {"province":"Northwest Territories", "sales_tax":0},
        {"province":"Nova Scotia", "sales_tax":0.10},
        {"province":"Nunavut", "sales_tax":0},
        {"province":"Ontario", "sales_tax":0.08},
        {"province":"Prince Edward Island", "sales_tax":0.09},
        {"province":"Quebec", "sales_tax":0.9975},
        {"province":"Saskatchewan", "sales_tax":0.05},
        {"province":"Yukon", "sales_tax":0}
    ]

    for prov in provinces:
        if prov["province"] == province:
            tax = prov["sales_tax"]
            break

    return tax

def get_product_type(ptype):
    products = [
        {"type":"time", "products":["Watch", "Clock"]},
        {"type":"apparel", "products":["Coat", "Pants", "Hat", "Gloves", "Shoes", "Shirt"]},
        {"type":"accessory", "products":["Hat", "Bag", "Watch"]},
        {"type":"furniture", "products":["Desk", "Table", "Lamp"]},
        {"type":"kitchen", "products":["Knife", "Plate", "Cup"]},
        {"type":"electronic", "products":["Computer"]},
        {"type":"automobile", "products":["Car"]}
    ]

    for product in products:
        if product["type"] == ptype:
            options = product["products"]
            break

    return options
