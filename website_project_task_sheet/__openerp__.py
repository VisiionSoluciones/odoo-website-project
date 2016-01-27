# -*- coding: utf-8 -*-


{
    'name': 'Timesheet on Website Project Task',
    'version': '1.0',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'website': 'https://hibou.io/',
    'license': 'AGPL-3',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
Add timesheet support on task in the frontend.
==============================================
    """,
    'depends': [
        'website_project_task',
        'project_timesheet',
    ],
    'data': [
        'views/project_task_templates.xml',
        'security/ir.model.access.csv',
        'security/portal_security.xml',
    ],
    'installable': True,
    'auto_install': False,
    'category': 'Hidden',
}
