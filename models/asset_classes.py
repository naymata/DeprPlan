from enum import Enum


class AssetClass(Enum):
    CLASS_I = "Class I"
    CLASS_II = "Class II"
    CLASS_III = "Class III"
    CLASS_IV = "Class IV"
    CLASS_V = "Class V"
    CLASS_VI = "Class VI"


ASSET_CLASS_YEARS = {
    AssetClass.CLASS_I: 3,  # Tractors, qualified rent-to-own property
    AssetClass.CLASS_II: 5,
    # Vehicles, computers, office equipment, research equipment, appliances for a rental property
    AssetClass.CLASS_III: 7,
    # Office furniture and fixtures, farm equipment, any assets that does not fit other classes
    AssetClass.CLASS_IV: 10,  # Boats, single purpose farm structures
    AssetClass.CLASS_V: 15,  # Land improvement (landscaping,roads, bridges)
    AssetClass.CLASS_VI: 20  # Multiple-purpose farm structures
}
