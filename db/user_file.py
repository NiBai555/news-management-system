
from db.mysql_file import pool


class User_Dao:

    # 验证登录信息
    def user_login(self,username,password):

        # 连接数据库
        con = pool.get_connection()
        cursor = con.cursor()
        sql = 'SELECT COUNT(*) FROM t_user WHERE username=%s AND ' \
              'AES_DECRYPT(UNHEX(password),"HelloWorld")=%s'
        cursor.execute(sql,(username,password))
        count = cursor.fetchone()[0]
        return True if count == 1 else False

    # 读取用户角色

    def user_role(self,username):

        con = pool.get_connection()
        cursor = con.cursor()
        sql = 'SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id WHERE username=%s'
        cursor.execute(sql,[username])
        role = cursor.fetchone()[0]
        return role

    # 查询用户总页数
    def count_user_page(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = 'SELECT CEIL(COUNT(*)/10) FROM t_user '
        cursor.execute(sql)
        count_page = cursor.fetchone()[0]
        return count_page
    # 查询用户表
    def search_user_list(self,page):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT u.id,u.username,r.role FROM t_user u JOIN t_role r ON u.role_id=r.id " \
              "LIMIT %s,%s"
        cursor.execute(sql,((page-1)*10,10))
        user_info = cursor.fetchall()
        return user_info


    # 添加用户
    def insert_user(self,username,password,email,role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user(username,password,email,role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            cursor.execute(sql,(username,password,email,role_id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 修改用户

    def update_user(self,id,username,password,email,role_id):

        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user " \
                  "SET username=%s,password=HEX(AES_ENCRYPT(%s,'HelloWorld')),email=%s,role_id=%s " \
                  "WHERE id=%s"
            cursor.execute(sql,(username,password,email,role_id,id))
            con.commit()

        except Exception as e:
            if 'con' in dir():
                con.rollback()
                print(e)
        finally:
            if 'con' in dir():
                con.close()

# 删除用户

    def delete_user(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id=%s"
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)

        finally:
            if 'con' in dir():
                con.close()




