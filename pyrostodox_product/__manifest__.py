# -*- coding: utf-8 -*-
{
    'name': "Pyrostodox: product_template",

    'summary': """
        Pyrostodox: new fields on product_template model""",

    'description': """
        
    """,

    'author': "Odoo sa",
    'website': "http://www.odoo.com",

    'category': 'user',
    'version': '1.0',

    'depends': [
        'product',
        'sale_management',
        'account_accountant',
        'stock',
        'purchase'
    ],

    'data': [
        # views
        'views/product.xml',
    ],
}
