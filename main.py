import pyqrcode
import png
from pyqrcode import QRCode
import time

  
def menu():
    name=input("Enter Your Name: ")
    phoneno=input("Enter Your Phone No.")
    url=input("Enter Your website ulr (www.example.com)")
    genqr(name,phoneno,url)
    

def genqr(name,phoneno,url):
    data=name+"\n"+phoneno+"\n"+url
    qrout = pyqrcode.create(data)
    print("Getting Your QRCode Ready")
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    qrout.svg(f"{name}.svg", scale = 8)
    qrout.png(f"{name}.png", scale = 6)
menu()