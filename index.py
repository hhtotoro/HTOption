#-*- coding:UTF-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options
import t_url
app=tornado.web.Application(t_url.url)
define("port",default=8000,help="run on port",type=int)
if __name__=="__main__":
   tornado.options.parse_command_line()
   app.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()