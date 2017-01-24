#-*- coding:UTF-8 -*-
from tornado.web import RequestHandler
from tornado.escape import json_decode, json_encode
from db.Mysql import mysql_db
# 解决js跨域请求问题pycharm push 到github
class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


# 删除用户
class DelHandler(BaseHandler):
    db = mysql_db()
    def post(self):
        client_id = self.get_argument('client_id', None)
        result = {}
        self.db.db_connect()
        sqlstr = "delete from otc_client_info where client_id = '" + client_id + "'"
        result["result"] = self.db.execute(sqlstr)
        self.write(json_encode(result))


# 修改用户
class EditHandler(BaseHandler):
    db = mysql_db()
    def post(self):
        o_name = self.get_argument('o_name', None)
        name = self.get_argument('name', None)
        time = self.get_argument('time', None)
        result = {}
        self.db.db_connect()
        sqlstr = "update otc_client_info set  = '"
        result["result"] = self.db.execute(sqlstr)
        self.write(json_encode(result))


# 新增用户
class AddHandler(BaseHandler):
    db = mysql_db()
    def post(self):
        time = self.get_argument('time', None)
        result = {}
        self.db.db_connect()
        sqlstr = "update otc_client_info set  = '"
        result["result"] = self.db.execute(sqlstr)
        self.write(json_encode(result))


class IndexHandler(BaseHandler):
    db = mysql_db()
    def get(self):
        self.db.db_connect()
        sqlstr = "select * from otc_client_info"
        res = self.db.query(sqlstr)
        result = {}
        content = []
        t = 1
        for item in res:
            tempItem = {}
            tempItem["id"] = t
            tempItem["name"] = item[0]
            try:
                tempItem["signup_date"] = item[1].strftime("%Y-%m-%d %H:%M:%S")
            except:
                tempItem["signup_date"] = ''
            t += 1
            content.append(tempItem)
        result["total"] = 1000
        result["rows"] = content
        result["status"] = "true"
        result["code"] = 200
        self.write(json_encode(result))