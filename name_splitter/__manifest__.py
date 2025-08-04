{
    'name': 'Name Splitter',
    'version': '0.1.0',
    'category': 'Tools',
    'summary': 'Split partner names into first, middle, and last name fields',
    'description': """
Name Splitter Module
====================

This module extends the res.partner model to automatically split names into 
separate first_name, middle_name, and last_name fields while keeping them 
synchronized with the main name field.

Features:
* Adds first_name, middle_name, and last_name fields to partners
* Automatically splits the name field when modified into individual components
* Automatically combines first_name, middle_name, and last_name into the name field
* Handles various naming scenarios:
  - Single names (only first_name is populated)
  - Two names (first_name and last_name)
  - Three names (first_name, middle_name, and last_name)
  - Multiple middle names (combines all middle parts into middle_name field)
* Smart name parsing with proper handling of edge cases and empty fields
* Bidirectional synchronization between full name and individual name components
    """,
    'author': 'SDA SE',
    'website': 'https://sda.se',
    'depends': ['base', 'contacts'],
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
