# -*- coding: utf-8 -*-
from odoo import api, models, fields, _


class CustomBlog(models.Model):
    _description = 'Blogs'
    _inherit = ['blog.blog']

    company_id = fields.Many2one('res.company', string="Company",required=True)