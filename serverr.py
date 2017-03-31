# *-* coding: utf8 *-**

import SocketServer
import datetime
import cPickle



bagli_clientlar = []
mesajlar = []

class MyHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "geldi"
        print self.client_address
        data = self.request.recv(1024)
        self.request.sendall("#hg")
        username = self.request.recv(1024)
        bagli_clientlar.append({'client': self.client_address,
                                'name': username, 'date': datetime.datetime.now()})
        self.request.sendall("#gir")
        while True:
            msg = self.request.recv(1024)
            mesajlar.append({'client': (self.client_address[0], username),
                             'date': datetime.datetime.now(), 'message': msg})
            self.request.sendall(cPickle.dumps(mesajlar))






def baglanti_kur(host, port, classname):
    server = SocketServer.ThreadingTCPServer((host, port), classname)
    server.serve_forever()

if __name__ == "__main__":
    baglanti_kur("0.0.0.0", 21, MyHandler)
