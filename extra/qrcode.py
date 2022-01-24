import qrcode

url = str(input("Enter url to make qr code with: "))
image = qrcode.make(url)
image.save(qrcode.png)
