from app.api import api
from app.api import browser_call
import socket
import qrcode
import time
import os

if __name__ == '__main__':
    
    time.sleep(10)
    
    # get my ip adress
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    hostip =  s.getsockname()[0]
    print(hostip)
    
    # make qr code for smartphone
    img = qrcode.make('http://' + hostip + ':8000')
    img.save("app/static/img/qr.png")
    
    # launch browser
    #browser_call.call_selenium_browser('file://' + os.getcwd() + '/app/templates/black.html')
    browser_call.call_selenium_browser('file:///home/takosuke/kitchenProject/app/templates/black.html')
    
    # launch flask server
    api.run(host='0.0.0.0', port=8000) 
