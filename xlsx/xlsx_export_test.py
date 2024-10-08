import unittest

import xlsx_export as x


class MyTestCase(unittest.TestCase):

    def test_init_workbook(self):
        products: x.List[x.p.Product]
        products = [x.p.Product('Hello', x.p.dep.Decimal('1500'), x.p.dep.Decimal('80'), x.p.dep.ac.AssetClass.CLASS_II),
                    x.p.Product('Hello1', x.p.dep.Decimal('1000'), x.p.dep.Decimal('120'), x.p.dep.ac.AssetClass.CLASS_VI)]
        export = x.XlsxExport('name',products)
        x.XlsxExport.write_to_xlsx(export)

if __name__ == '__main__':
    unittest.main()
