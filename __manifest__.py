{
    'name' : 'Jokeen.id',
    'version' : '1.0',
    'summary': 'Jokeen.id Transactions Book',
    'sequence': 1,
    'description': """Jokeen.id Transactions Book""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/app/billing',
    'license': 'LGPL-3',
    'depends' : ['sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/categories_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
