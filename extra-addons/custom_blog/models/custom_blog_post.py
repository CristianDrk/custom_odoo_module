# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class CustomBlogPost(models.Model):
    _description = "Blog Post"
    _inherit = ['blog.post']
    
    company_id = fields.Many2one(related='blog_id.company_id', string="Company", store=True)