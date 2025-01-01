import pyqrcode 

s = "https://www.google.com"
url = pyqrcode.create(s)
url.svg("google.svg", scale = 8) 