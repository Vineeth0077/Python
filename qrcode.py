import pyqrcode
import png
from pyqrcode import QRCode

s = "QR"

url = pyqrcode.create(s)

url.svg("qr.svg",scale=8)

url.png('myqr.png',scale=6)