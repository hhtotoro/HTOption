from tornado.web import RequestHandler
from tornado.escape import json_decode, json_encode
from db.Mysql import mysql_db
# 解决js跨域请求问题
class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


# 删除用户
class DelHandler(BaseHandler):
    def post(self):
        name = self.get_argument('name', None)
        result = {}
        conn = db.connect(host='127.0.0.1', port=5432, user='leo', password='king', database='testdb')
        cursor = conn.cursor()
        try:
            sqlstr = "delete from  user_tbl where name='%s'" % name
            cursor.execute(sqlstr)
        except(psycopg2.Warning, psycopg2.Error) as error:
            result["result"] = "DB Error:" + error.message
            result["status"] = "false"
            result["code"] = 300
            self.write(json_encode(result))
            conn.rollback()
            cursor.close()
            conn.close()
            return
        result["result"] = "success"
        result["status"] = "true"
        result["code"] = 200
        if (result["status"] == "true"):
            conn.commit()
        cursor.close()
        conn.close()
        self.write(json_encode(result))


# 修改用户
class EditHandler(BaseHandler):
    def post(self):
        o_name = self.get_argument('o_name', None)
        name = self.get_argument('name', None)
        time = self.get_argument('time', None)
        result = {}
        conn = psycopg2.connect(host='127.0.0.1', port=5432, user='leo', password='king', database='testdb')
        cursor = conn.cursor()
        try:
            sqlstr = "update user_tbl set name='%s',signup_date='%s' where name='%s'" % (name, time, o_name)
            cursor.execute(sqlstr)
        except(psycopg2.Warning, psycopg2.Error) as error:
            result["result"] = "DB Error:" + error.message
            result["status"] = "false"
            result["code"] = 300
            self.write(json_encode(result))
            conn.rollback()
            cursor.close()
            conn.close()
            return
        result["result"] = "success"
        result["status"] = "true"
        result["code"] = 200
        if (result["status"] == "true"):
            conn.commit()
        cursor.close()
        conn.close()
        self.write(json_encode(result))


# 新增用户
class AddHandler(BaseHandler):
    def post(self):
        time = self.get_argument('time', None)
        result = {}
        conn = psycopg2.connect(host='127.0.0.1', port=5432, user='leo', password='king', database='testdb')
        cursor = conn.cursor()
        try:
            sqlstr = "insert into user_tbl(name,signup_date) values('%s','%s')" % (name, time)
            cursor.execute(sqlstr)
        except(psycopg2.Warning, psycopg2.Error) as error:
            result["result"] = "DB Error:" + error.message
            result["status"] = "false"
            result["code"] = 300
            self.write(json_encode(result))
            conn.rollback()
            cursor.close()
            conn.close()
            return
        result["result"] = "success"
        result["status"] = "true"
        result["code"] = 200
        if (result["status"] == "true"):
            conn.commit()
        cursor.close()
        conn.close()
        self.write(json_encode(result))


class IndexHandler(BaseHandler):
    def get(self):
        conn = psycopg2.connect(host='127.0.0.1', port=5432, user='leo', password='king', database='testdb')
        cursor = conn.cursor()
        result = {}
        try:
            sqlstr = "select name,signup_date from user_tbl"
            cursor.execute(sqlstr)
            if (cursor.rowcount == 0):
                result["total"] = 0
                result["rows"] = "no data."
                result["status"] = "false"
                result["code"] = 300
                self.write(json_encode(result))
                conn.close()
                return
            else:
                res = cursor.fetchall()
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
        except(psycopg2.Warning, psycopg2.Error) as error:
            result["result"] = "DB error:" + error.message
            result["status"] = "false"
            result["code"] = 300
            self.write(json_encode(result))
            conn.rollback()
            conn.close()
            return
        if (result["status"] == "true"):
            conn.commit()
        conn.close()
        print json_encode(result)
        self.write(json_encode(result))