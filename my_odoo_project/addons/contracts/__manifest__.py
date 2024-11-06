{
    'name': 'Contracts',
    'version': '11.0.1.0.0',
    'category': 'Sales',
    'summary': 'Manage contracts and payments',
    'description': """
        This module allows you to manage contracts, contract lines, and payments.
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_views.xml',
        'wizards/payment_wizard_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}