from typing import List

import xlsxwriter
from xlsxwriter import Workbook

from models import product as p


class XlsxExport:
    company_name: str
    products: List[p.Product]
    product_overview = 'Products Overview'

    def __init__(self, company_name: str, products: List[p.Product]):
        self.company_name = company_name
        self.products = products

    def write_to_xlsx(self):
        file_name = self.company_name + '.xlsx'
        workbook = xlsxwriter.Workbook(file_name)
        self.__init_worksheets(workbook)
        self.__write_products_list(workbook)
        self.__write_to_sheet(workbook)

        workbook.close()

    def __init_worksheets(self, book: Workbook):
        book.add_worksheet(self.product_overview)
        for p in self.products:
            book.add_worksheet(f'{p.get_name().strip()}', None)

    def __write_to_sheet(self, book: Workbook):
        row = 0
        col = 0
        arr = ['Year', 'Beginning Book Value ($)', 'Annual Depreciation ($)', 'Accumulated Depreciation ($)',
               'Ending Book Value ($)']
        for p in self.products:
            worksheet = book.get_worksheet_by_name(p.get_name())

            for i in arr:
                worksheet.write(row, col, i)
                col += 1
            col = 0
            row += 1
            product_price = p.get_price()
            for i in range(1, p.get_asset_lifetime() + 1):
                worksheet.write(row, col, i)
                beginning_book_value = '$' + f'{product_price:,}'
                worksheet.write(row, col + 1, beginning_book_value)
                annual_depreciation = '$' + f'{p.get_depreciation_amount():,}'
                worksheet.write(row, col + 2, annual_depreciation)
                accumulated_depreciation = '$' + f'{(p.get_depreciation_amount() * i):,}'
                worksheet.write(row, col + 3, accumulated_depreciation)
                ending_book_value = '$' + f'{(p.get_price() - (p.get_depreciation_amount() * i)):,}'
                worksheet.write(row, col + 4, ending_book_value)
                row += 1
                product_price = p.get_price() - (p.get_depreciation_amount() * i)
            row = 0

    def __write_products_list(self, book: Workbook):
        row = 0
        col = 0
        worksheet = book.get_worksheet_by_name(self.product_overview)
        worksheet.write(row, col, self.product_overview)
        for product in self.products:
            row += 1
            worksheet.write(row, col, product.get_name())
