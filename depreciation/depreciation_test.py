import unittest
from models import asset_classes as ac
from depreciation import depreciation as dep
from decimal import Decimal


class MyTestCase(unittest.TestCase):

    def test_straight_line(self):
        number = dep.straight_line_depreciation(Decimal('10_000.00'), Decimal('500.00'),
                                                ac.ASSET_CLASS_YEARS.get(ac.AssetClass.CLASS_FOUR))
        self.assertEqual(Decimal('950.00'), number)

    def test_straight_line_fail(self):
        number = dep.straight_line_depreciation(Decimal('10_000.00'), Decimal('500.00'),
                                                ac.ASSET_CLASS_YEARS.get(ac.AssetClass.CLASS_ONE))
        self.assertNotEqual(Decimal('950.00'), number)


if __name__ == '__main__':
    unittest.main()
