# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    source = fields.Selection([
        ('third_party', 'Third party'),
        ('social_media', 'Social media'),
        ('internet_search', 'Internet Search')
    ], string='Source', required=True)
    
    @api.constrains('email_from')
    def _check_email_from(self):
        for lead in self:
            if lead.email_from:
                #Comprueba que el mail introducido sea: (cualquier caracter menos @) (@) (cualquier caracter menos @) (punto) (cualqier caracter menos @)
                if not re.match(r"[^@]+@[^@]+\.[^@]+", lead.email_from):
                    raise ValidationError("Please enter a valid email address.")