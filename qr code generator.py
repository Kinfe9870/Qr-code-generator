import pyqrcode

data = input("Enter a text to generate code: ")

code = pyqrcode.create(data)

code.svg("qr_code.svg", scale=15)
