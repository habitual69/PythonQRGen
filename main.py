import pyqrcode
import png
from pyqrcode import QRCode
import time
import os


def menu():
    name=input("Enter Your Name: ")
    phoneno=input("Enter Your Phone No.")
    url=input("Enter Your website ulr (www.example.com)")
    genqr(name,phoneno,url)
    

def genqr(name,phoneno,url):
    os.makedirs(os.path.join("out", f"{name}"))
    os.chdir(f"out\{name}")
    data=name+"\n"+phoneno+"\n"+url
    qrout = pyqrcode.create(data)
    print("Getting Your QRCode Ready")
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("....")
    time.sleep(0.5)
    print(".....")
    qrout.svg(f"{name}.svg", scale = 8)
    qrout=qrout.png(f"{name}.png", scale = 6)

menu()