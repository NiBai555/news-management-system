
from db.mysql_file import pool


class Role_info:

    def search_role(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT id,role FROM t_role"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


# if __name__ == "__main__":
#     a = Role_info().search_role()
#     print(a)