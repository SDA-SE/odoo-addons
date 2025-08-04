{
    'name': 'Name Splitter',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Split partner names into first and last name fields',
    'description': """
Name Splitter Module
====================

This module extends the res.partner model to automatically split names into 
separate first_name and last_name fields while keeping them synchronized 
with the main name field.

Features:
* Adds first_name and last_name fields to partners
* Automatically splits the name field when modified
* Automatically combines first_name and last_name into the name field
* Handles edge cases for single names and empty fields
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
