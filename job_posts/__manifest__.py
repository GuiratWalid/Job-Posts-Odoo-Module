{
    'name' : 'Job Posts',
    'version' : '17.0',
    'summary': 'Job Posts Management Module',
    'sequence': 10,
    'description': """
    Job Posts Management Module
    ====================
    This Odoo Module allows you to:
    * scrape and add job posts to your Odoo system from a job listing site.
    * assign the scraped job posts to users.
    """,
    'category': 'Human Resources/Jobs',
    'website': 'https://smarte-conseil.fr/fr/',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/ir_sequence_data.xml',

        'views/job_posts_views.xml',
        'views/job_configurations_views.xml',
        'views/job_posts_menus.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
    'images': [
        'static/description/icon.png'
    ]
}
