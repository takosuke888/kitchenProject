from app.api import api
import socket
import qrcode

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    hostip =  s.getsockname()[0]
    print(hostip)
    img = qrcode.make('http://' + hostip + ':8000')
    img.save("qr.png")
    api.run(host='0.0.0.0', port=8000) 