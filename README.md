# Product Depreciation Calculator

This project is a desktop application that helps users manage a list of products, 
calculate their depreciation using the straight-line depreciation method, and export 
the data into Excel spreadsheets.

## Features

* **Add Products**: Users can add new products with details like name, price, salvage value, class, and depreciation
  amount.
* **Delete Products**: Easily remove products from the list.
* **Display Products**: View a detailed list of all added products in a table format.
* **Export to Excel**: Export the product list to an Excel file for easy sharing and analysis.
* **Depreciation Calculation**: Utilizes the straight-line depreciation strategy to calculate and display depreciation
  amounts.
* **Responsive UI**: User-friendly interface designed with PyQt5.
# Technologies used
* **Python**
* **PyQt5 for GUI**
* **XlsxWriter for writing to xlsx files**
* **unittest2**
## **Straight-line depreciation**

#### How it works ?

- You divide the cost of an asset, minus its salvage value, over its
  useful life. That determines how much depreciation can deduct each year.

##### Formula :

```
  (asset cost  - salvage value) / useful life = annual depreciation
```

##### Formula example:

```
($10,000 - $500) / 10 = $950
```
