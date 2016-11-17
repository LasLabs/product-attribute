# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product Service Duration',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'resource',
        'product',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'views/product_template.xml',
    ],
    "application": False,
    'installable': True,
}
