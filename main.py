from tornado.httpserver import HTTPServer
import tornado
from tornado.websocket import WebSocketHandler

class EchoWebSocket(WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("WebSocket received a message. real ip is " + self.request.remote_ip)
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True

    def on_pong(self, data):
        print("WebSocket on_pong. data is " + data)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/wq", EchoWebSocket),
    ])    #websocket_ping_timeout needs < websocket_ping_interval
    server = HTTPServer(app, xheaders=True)
    #server = HTTPServer(app)
    server.listen(4004)
    tornado.ioloop.IOLoop.current().start()