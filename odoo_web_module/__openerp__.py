#__openerp__.py
{
    'name': "Web Module Example",
    'description': "Basic example of a (future) web module",
    'category': 'web',
    'depends': ['website'],
    'data': [
        'data/data.xml',
        'views/main.xml',
        'views/content.xml',
        'views/config.xml'
         ]
}