import sqlite3

class DB():

    def __init__(self):
        # self.query = query
        self.con = sqlite3.connect("contributors.db")
        self.cur = self.con.cursor()


    def insert(self,tb_name,col_1,col_2,col_3,col_4,data1,data2,data3,data4):
        self.cur.execute("INSERT INTO {}({},{},{},{})VALUES(?,?,?,?)".format(tb_name,col_1,col_2,col_3,col_4),(data1,data2,data3,data4))
        self.con.commit()
        return True
    
    def select_where(self,tb_name,col_name,data):
        self.cur.execute("SELECT * FROM {} WHERE {}=?".format(tb_name, col_name), (data,))
        data = self.cur.fetchall()
        return data

    def select(self,tb_name,name,email):
        self.cur.execute("SELECT * FROM {} WHERE intern_name=? AND intern_email=?".format(tb_name), (name,email))
        data = self.cur.fetchall()
        return data[0][1]

    def authentication(self,tb_name,col_name1,data1,col_name2,data2):
        self.cur.execute("SELECT * FROM {} WHERE {}=? AND {}=?".format(tb_name,col_name1,col_name2), (data1,data2))
        data = self.cur.fetchall()
        if len(data) > 0:
            return True
        return False
    

    def select_all(self,tb_name):
        self.cur.execute("SELECT * FROM {}".format(tb_name))
        data = self.cur.fetchall()
        return data


    
    def update(self,tb_name,col2_change,value, col_id, data_id):
        self.cur.execute("UPDATE {} SET {}=? WHERE {}=?".format(tb_name,col2_change,col_id), (value,data_id))
        self.con.commit()
        return True

    def delete_one(self,tb_name,data_id):
        self.cur.execute("DELETE FROM {} WHERE activity_id=?".format(tb_name), (data_id,))
        self.con.commit()
        return True
        
    def delete_rows(self,tb_name):
        self.cur.execute("DELETE FROM {}".format(tb_name))
        self.con.commit()
        return True
    
   

if __name__ =="__main__":
    db = DB()
    