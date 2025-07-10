import qrcode

website = input("Enter the text or URL for QR code: ")
filename = input("Enter the filename you want to save it to: ")
img = qrcode.make(website)
type(img)
img.save(filename)