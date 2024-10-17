from decimal import Decimal
from models import asset_classes as ac

class Depreciation:
    __asset_price: Decimal
    __salvage_value :Decimal
    __useful_years:ac.ASSET_CLASS_YEARS
    def __init__(self,asset_price: Decimal, salvage_value:Decimal ,useful_years: ac.ASSET_CLASS_YEARS):
        self.__asset_price = asset_price
        self.__salvage_value = salvage_value
        self.__useful_years = useful_years

    def straight_line_depreciation(self):
        return  (self.__asset_price-self.__salvage_value) / self.__useful_years

