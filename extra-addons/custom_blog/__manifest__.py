# -*- coding: utf-8 -*-
{
    'name': 'Custom Blogs',
    'category': 'Website',
    'summary': 'Adds custom blogging functionality to Odoo.',
    'version': '1.0',
    'description': "",
    'depends': ['website_blog','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_blog_views.xml',
        'views/custom_blog_post_views.xml',
    ],
    'demo': [
        ],
    'test': [
        ],
    'qweb': [
        ],
    'installable': True,
    'application': True,
}
