{
    'name': 'Mallz',
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    'data':[
        'security/ir.model.access.csv',

        'views/all_malls_views.xml',
        'views/mall_menus.xml'
    ],
    'application': True,
    'installable': True,
}
