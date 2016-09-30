# shopicruit_vs

This code requires the following libraries
    
    json

    requests
    
    argparse
    
    sys

I created this code for my Shopify intern application.

It allows you to compute the cost of buying all products of a certain type (the default is time telling devices.)

Modify the product type with the argument
    --product [PRODUCT]

If the product is taxable, it will use the tax rate from a specified province (the default is Yukon, i.e., no tax.)

Modify the province with the argument
    --province [PROVINCE]

You may also specify the type of file that you are parsing. For now, only JSON files are permitted.

Modify the filetype with the argument
    --filetype [FILETYPE]

To see a list of all possible provinces and all possible products, look under
    
    utility/utils.py
