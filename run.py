from app.api import api
import socket

if __name__ == '__main__':
    host = socket.gethostname()
    print(host)
    ip = socket.gethostbyname(host)
    print(ip) 
    api.run(host='0.0.0.0', port=8000) 