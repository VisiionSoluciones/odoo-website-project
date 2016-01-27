# -*- coding: utf-8 -*-


{
    'name': 'Website Project Tasks',
    'version': '1.0',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'website': 'https://hibou.io/',
    'license': 'AGPL-3',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds project tasks inside your account's page on website if project and website_portal are installed.
=================================================================================================================
    """,
    'depends': [
        'project',
        'website_portal',
    ],
    'data': [
        'views/project_task_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'category': 'Hidden',
}
