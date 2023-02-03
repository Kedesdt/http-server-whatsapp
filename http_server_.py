from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import cgi
import whatsapp

# ip and port of server
HOST_NAME = '127.0.0.1'

# by default http server port is 8085
PORT_NUMBER = '5678'


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """ Create custom HTTPRequestHandler class """

    def _set_headers(self):
        """ set HTTP headers """

        # send code 200 response
        self.send_response(200)
        # send header first
        self.send_header('Content-type', 'text/html')
        self.send_header('Last-Modified',
                         self.date_time_string(time.time()))
        # send file content to client
        self.end_headers()

    def do_HEAD(self):
        """ do the HTTP HEAD """

        # set HTTP headers
        self._set_headers()

    def do_GET(self):
        """ handle GET command """
        """
        http: // 127.0
        .0
        .1: 5678 /?arquivo = C: % 2
        FUsers % 2
        Fkdtorres % 2
        FPictures % 2
        Fteste.png
        """
        rootdir = os.path.dirname(__file__)  # file location

        form = cgi.FieldStorage()
        arquivo = str(form['arquivo'].value)
        numero = str(form['numero'].value)
        if whatsapp.envia(numero, arquivo):
            self._set_headers()
        else:
            self.send_error(404, 'file not found')

    def do_POST(self):
        """ handle POST command """

        # set HTTP headers
        self._set_headers()

        # Create instance of FieldStorage
        # for parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        # Begin the response
        self._set_headers()

        # Get data from fields
        message = form.getvalue('message')

        html_response = """
<html>
  <body>
    <h1>POST verb demo</h1>
    <p>The message is '%s'.</p>
    <br />
    <p>This is a POST verb!</p>
  </body>
</html>
        """ % (message)

        self.wfile.write(bytes(html_response, "utf-8"))


def run():
    try:
        print('HTTP Server is starting...')
        server_address = (HOST_NAME, int(PORT_NUMBER))
        server = HTTPServer(server_address, MyHTTPRequestHandler)
        print("HTTP Server running on http://{0}:{1}/ use <Ctrl-C> to stop.".format(HOST_NAME, PORT_NUMBER))
        server.serve_forever()
    except KeyboardInterrupt:
        print(" o <Ctrl-C> entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    """ Starting Python program """
    run()
