from typing import List

import xlsxwriter
from xlsxwriter import Workbook

from models import product as p


class XlsxExport:
    company_name: str
    products: List[p.Product]
    product_overview='Products Overview'
    def __init__(self, company_name: str, products: List[p.Product]):
        self.company_name = company_name
        self.products = products

    def write_to_xlsx(self):
        file_name = self.company_name + '.xlsx'
        workbook = xlsxwriter.Workbook(file_name)
        self.init_worksheets(workbook)
        self.write_products_list(workbook)
        self.write_to_sheet(workbook)

        workbook.close()

    def init_worksheets(self, book: Workbook):
        book.add_worksheet(self.product_overview)
        for p in self.products:
            book.add_worksheet(f'{p.name.strip()}', None)

    def write_to_sheet(self, book: Workbook):
        row = 0
        col = 0
        arr = ['Year','Beginning Book Value ($)','Annual Depreciation ($)','Accumulated Depreciation ($)','Ending Book Value ($)']
        for p in self.products:
            worksheet = book.get_worksheet_by_name(p.name)

            for i in arr:
                worksheet.write(row,col,i)
                col+=1
            col=0
            row+=1
            product_price = p.price
            for i in range(1,p.get_asset_lifetime()+1):
                worksheet.write(row,col,i)
                worksheet.write(row,col+1,product_price)
                worksheet.write(row,col+2,p.depreciation_amount)
                worksheet.write(row,col+3,p.depreciation_amount*i)
                worksheet.write(row,col+4,p.price-p.depreciation_amount*i)
                row+=1
                product_price = p.price - (p.depreciation_amount * i)
            row=0

    def write_products_list(self, book: Workbook):
        row = 0
        col = 0
        worksheet = book.get_worksheet_by_name(self.product_overview)
        worksheet.write(row, col, self.product_overview)
        for product in self.products:
            row += 1
            worksheet.write(row, col, product.name)
