# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'material'
    material_type = ['Fabric', 'Jeans', 'Cotton']
    code = fields.Char(
        string='Material Code',
        required=True,
    )
    name = fields.Char(
        string='Material Name',
        required=True
    )
    type = fields.Selection(
        [
            (material_type[0], material_type[0]),
            (material_type[1], material_type[1]),
            (material_type[2], material_type[2]),
        ],
        string='Material Type',
        required=True
    )
    supplier_id = fields.Many2one(comodel_name='supplier', string='Related Supplier', required=True)
    price = fields.Float('Buy Price',
        required=True,
        digits='Product Unit of Measure',
        default=100,
    )
    # buy prive < 100 validation
    @api.constrains('price')
    def _check_something(self):
        for record in self:
            if record.price < 100.0:
                raise ValidationError("Price cannot below 100!")
    