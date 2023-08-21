import pyqrcode
from pyqrcode import QRCode

url_link = "andreiadam.pythonanywhere.com"

url = pyqrcode.create(url_link)

url.svg(".\\Porto.svg", scale=8)