import odoo
from odoo.exceptions import UserError
import odoo.tests
class TestMaterial(odoo.tests.TransactionCase):
    def test_create(self):
        # create supplier first
        supplier = self.env['supplier'].create([
            {'name': 'admin'},
            {'name': 'ramdani'},
            {'name': 'Anon'},
        ])
        # get supplier id
        supplier_id = supplier.mapped('id')
        # get material type
        material_type = self.env['material'].material_type
        # create material typr
        material = self.env['material'].create([
            {
                'name': 'MaterialX',
                'code': 'material_x',
                'type': 'Fabric',
                'price': 120,
                'supplier_id': supplier_id[0],
            }, {
                'name': 'MaterialY',
                'code': 'material_y',
                'type': 'Jeans',
                'price': 120,
                'supplier_id': supplier_id[1],
            }, {
                'name': 'MaterialZ',
                'code': 'material_z',
                'type': 'Cotton',
                'price': 120,
                'supplier_id': supplier_id[2],
            },
        ])
        # assertEqual type => material_type
        self.assertEqual(
            material.mapped('type'),
            material_type,
        )

    # Validation buy price test
    def test_constraints(self):
        supplier = self.env['supplier'].create([
            {'name': 'admin'},
        ])
        with self.assertRaises(UserError):
            self.env['material'].create({
                'name': 'MaterialX',
                'code': 'material_x',
                'type': 'Fabric',
                'price': 20,
                'supplier_id': supplier[0]['id'],
            })
