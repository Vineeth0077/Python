from barcode import EAN13 #European Article Number' & 13-digit Global Trade Item Number (GTIN).
number = '1234567890'
code = EAN13(number)
code.save("BARCODE")
