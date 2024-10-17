import unittest
from models import product, asset_classes


class MyTestCase(unittest.TestCase):

    def test_product_creation(self):
        new_product = product.Product("RTX 3050", product.dep.Decimal('1_500.00'),product.dep.Decimal('500.00'), asset_classes.AssetClass.CLASS_II)
        self.assertEqual(product.dep.Decimal('200'),new_product.get_depreciation_amount())
        self.assertEqual(5,new_product.get_asset_lifetime())

if __name__ == '__main__':
    unittest.main()
