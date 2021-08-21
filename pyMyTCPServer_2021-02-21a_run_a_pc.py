"""
Material tomado de la libreria de referencia:
https://docs.python.org/3/library/socketserver.html
"""
import socketserver
import platform

print("sys info:")
for info in platform.uname():
    print(info)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.client_address[0].encode())
        self.request.sendall(self.data.upper())
        self.request.sendall(b'\r\n')

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    #with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    with socketserver.TCPServer(('', PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C

        server.serve_forever()
