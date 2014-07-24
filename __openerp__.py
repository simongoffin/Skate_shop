# __openerp__.py
{
    'name': "Skate shop",
    'description': "Do you want to buy a skate?",
    'author' : "Simon",
    'data': [
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/skate_view.xml',
        'data/skate_records.xml',
        'views/proprietaire_view.xml',
        'data/proprietaire_records.xml',
        'views/inherit_view.xml',
        'views/shop_assets.xml',
    ],
    'depends': ['base'],
    'qweb':['static/src/xml/*.xml'],
}