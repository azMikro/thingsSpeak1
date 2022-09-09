#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("api.thingspeak.com" , 80))
    s.send(b"POST /update HTTP/1.1\r\nHost: api.thingspeak.com\r\nContent-Length: 42\r\n\r\napi_key=PHDI7FCOYDX178PO&field1=5&field2=6\r\n\r\n")
    print(str(s.recv(4096), 'utf-8'))


 ###GET / HTTP/1.1\r\nHost: api.thingspeak.com/update?api_key=PHDI7FCOYDX178PO&field1=0


###POST /update HTTP/1.1\r\nHost: api.thingspeak.com\r\n\r\napi_key=PHDI7FCOYDX178PO&field1=0\r\n\r\n
