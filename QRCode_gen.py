#import dependencies
import pyqrcode
import png

#text which you want to convert in QRCode
QRtext = input(print('Enter text to generate QR: '))

#filename that will be saved
QRimg = input(print('Enter image name to save: '))

#image extension
QRimg = QRimg + '.png'


#Generating Final QRCOODE
FinalQR = pyqrcode.create(QRtext)

FinalQR.show()
FinalQR.png(QRimg, scale=6)
