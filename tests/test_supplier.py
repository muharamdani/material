import odoo
import odoo.tests

class TestSupplier(odoo.tests.TransactionCase):
    def test_create(self):
        supplier = self.env['supplier'].create([
            {'name': 'admin'},
            {'name': 'ramdani'},
        ])
        self.assertEqual(
            supplier.mapped('name'),
            ['admin', 'ramdani'],
        )
