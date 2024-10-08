from decimal import Decimal
from models import asset_classes as ac


def straight_line_depreciation(asset_price: Decimal, salvage_value: Decimal, useful_years: ac.ASSET_CLASS_YEARS):
    result = (asset_price - salvage_value) / useful_years
    return  result

