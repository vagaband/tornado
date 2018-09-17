# coding:utf-8

# coding:utf-8

import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("hello Itcase!")

if __name__ == '__main__':
    app = tornado.web.Application([(r"/", IndexHandler)])
    #app.listen(8888)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8888)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()
