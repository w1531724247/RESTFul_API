#!/usr/bin/env python
from app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(host='0.0.0.0',ssl_context=('/Users/QMTV/PycharmProjects/RESTFul_API/certificate/server.crt', '/Users/QMTV/PycharmProjects/RESTFul_API/certificate/server.key'))
