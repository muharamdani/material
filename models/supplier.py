# -*- coding: utf-8 -*-

from odoo import fields, models

class Supplier(models.Model):
    _name = 'supplier'
    _description = 'supplier'
    name = fields.Char(
        string='Supplier Name',
        required=True,
    )
