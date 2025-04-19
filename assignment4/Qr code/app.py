import qrcode
data = "QR Code using make() function"
img = qrcode.make(data)
img.save("qr code project 7.png")