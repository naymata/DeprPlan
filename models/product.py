from datetime import date
import models.asset_classes as ac
from depreciation import depreciation as dep
from depreciation.depreciation import Depreciation


class Product:
    # name of the asset
    __name: str
    # total price paid for asset
    __price: dep.Decimal
    # date of purchase
    __purchased_on = date.today().strftime("%m/%d/%Y")
    # expected useful life
    __asset_class: ac.AssetClass
    # salvage value (how much you can sell it after its useful life to a scrapyard)
    __salvage_value: dep.Decimal
    # depreciation amount
    __depreciation_amount: dep.Decimal

    def __init__(self, name: str, price: dep.Decimal, salvage_value : dep.Decimal,asset_class: ac.AssetClass):
        self.__name = name
        self.__price = price
        self.__asset_class = asset_class
        self.__salvage_value = salvage_value
        depre =dep.Depreciation = Depreciation(price,salvage_value,self.get_asset_lifetime())
        self.__depreciation_amount = depre.straight_line_depreciation()
        self.data = {"name": name, "price": str(price), "date": self.__purchased_on, "class": asset_class}

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_salvage_value(self):
        return self.__salvage_value
    def get_asset_class(self):
        return self.__asset_class.value
    def get_depreciation_amount(self):
        return self.__depreciation_amount
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value

    def get_asset_lifetime(self) -> int:
        return ac.ASSET_CLASS_YEARS.get(self.__asset_class, 0)

    def __repr__(self) -> str:
        return (
            f"Product(name={self.__name}, price={self.__price}, salvage_value={self.__salvage_value} "
            f" depreciation_amount= {self.__depreciation_amount}, asset_class = {self.__asset_class.value}, "
            f"asset_lifetime = {self.get_asset_lifetime()})"
        )
