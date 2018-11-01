# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Clear Shopping Carts',
    'version' : '1.1',
    'summary': 'Clear Shopping Carts',
    'sequence': 30,
    'description': """
Clear your shopping cart with a single click in Website Shop.
    """,
    'category': 'Website',
    'depends' : ['web','base_setup', 'sale', 'website_sale','website'],
    'data': [
        'views/website_sale_extends.xml',
        'views/templates.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
