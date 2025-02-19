#we are going to create a QR code for a youtube link using the qrcode library
#we are going to create a QR code for a youtube link using the qrcode library

import qrcode
website_link = "https://youtu.be/hT94urc-MVw?si=ImUjOduZDfnqJn9i"

#this is to create a qrcode image
#after importing the qrcode library we assign to qr an instance of the QRCode class

qr = qrcode.QRCode(version=1, box_size=5, border=5)

# version is controlling the size of the QR Code
# box_size is how many pixels each “box” of the QR code is
# border is how many boxes thick the border should be
#then we add data to the qr code by using add.data(link)

qr.add_data(website_link)
#then we call make() to generate the QR code

qr.make()
#then we create an image of the QR code

img = qr.make_image(fill_color="black", back_color="white")

#then we save the image to a file

img.save("youtube_qr.png")
