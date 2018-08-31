import pymysql


class database:
    def __init__(self):
        self.db = pymysql.connect("localhost","root","root","library",charset="utf8",cursorclass= pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def insert(self,sql,args):
        # self.sql=sql
        # print(self.sql)

        self.cursor.execute(sql,args)
        id = self.db.insert_id()
        self.db.commit()
        # self.close()
        return id

    def selectAll(self,sql,args=[]):
        self.sql=sql
        self.cursor.execute(self.sql,args)
        self.result  = self.cursor.fetchall()
        # self.close()
        return self.result

    def selectOne(self,sql,args=[]):
        self.sql = sql
        self.cursor.execute(self.sql,args)
        self.result  = self.cursor.fetchone()
        # self.close()
        return self.result

    # def selectMany(self,sql,args):
    #     self.cursor.execute(sql,args)
    #     result = self.cursor.fetchall()
    #     # self.result  = self.cursor.fetchone()
    #     print("12",result)
    #     self.close()
    #     return result
    def insertMany(self,sql,args):
        self.cursor.executemany(sql,args)
        self.db.commit()
        # self.result  = self.cursor.fetchone()
        # self.close()
        # return self.result

    def updata(self,sql,args=[]):
        print("sql",sql)
        self.cursor.execute(sql,args)
        self.db.commit()
        # self.result  = self.cursor.fetchone()
        # self.close()

    def close(self):
        self.cursor.close()
        self.db.close()

