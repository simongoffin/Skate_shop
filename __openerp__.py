# __openerp__.py
{
    'name': "Skate shop",
    'description': "Do you want to buy a skate?",
    'author' : "Simon",
    'data': [
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/skate_view.xml',
    ],
    'depends': ['base'],
}