from datetime import date
import models.asset_classes as ac
from depreciation import depreciation as dep


class Product:
    # name of the asset
    name: str
    # total price paid for asset
    price: dep.Decimal
    # date of purchase
    purchased_on = date.today().strftime("%m/%d/%Y")
    # expected useful life
    asset_class: ac.AssetClass
    # salvage value (how much you can sell it after its useful life to a scrapyard)
    salvage_value: dep.Decimal
    # depreciation amount
    depreciation_amount: dep.Decimal

    def __init__(self, name: str, price: dep.Decimal, salvage_value : dep.Decimal,asset_class: ac.AssetClass):
        self.name = name
        self.price = price
        self.asset_class = asset_class
        self.salvage_value = salvage_value
        self.depreciation_amount = dep.straight_line_depreciation(dep.Decimal(price), dep.Decimal(self.salvage_value),
                                                                  self.get_asset_lifetime())
        self.data = {"name": name, "price": str(price), "date": self.purchased_on, "class": asset_class}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def get_asset_lifetime(self) -> int:
        return ac.ASSET_CLASS_YEARS.get(self.asset_class, 0)

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name}, price={self.price}, salvage_value={self.salvage_value} "
            f" depreciation_amount= {self.depreciation_amount}, asset_class = {self.asset_class.value}, "
            f"asset_lifetime = {self.get_asset_lifetime()})"
        )
