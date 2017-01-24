import MySQLdb as db
import ConfigParser
class mysql_db():
    def db_connect(self):
        cp = ConfigParser.SafeConfigParser()
        cp.read('./conf/db.conf')
        host = cp.get('db', 'host')
        port = cp.get('db', 'port')
        user = cp.get('db', 'user')
        passwd = cp.get('db', 'passwd')
        database = cp.get('db', 'ht_option')
        try:
            conn = db.connect(host=host, user=user, passwd=passwd, db=database, charset="utf8")
            cursor = conn.cursor()
            return conn,cursor
        except db.Error, e:
            try:
                print "Error %d:%s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error:%s" % str(e)
    def db_disconnect(self,cursor,conn):
        cursor.close()
        conn.close()

    def execute(self,statement):
       conn, cursor = self.db_connect()
       try:
           cursor.execute(statement)
           self.db_disconnect(cursor,conn)
           return "success"
       except db.Error, e:
           try:
               return "Error %d:%s" % (e.args[0], e.args[1])
           except IndexError:
               return "MySQL Error:%s" % str(e)

    def query(self,statement):
        conn, cursor = self.db_connect()
        try:
            n = cursor.execute(statement)
            return_info = cursor.fetchall()
            self.db_disconnect(cursor, conn)
            return n,return_info
        except db.Error, e:
            try:
                return "Error %d:%s" % (e.args[0], e.args[1])
            except IndexError:
                return "MySQL Error:%s" % str(e)
