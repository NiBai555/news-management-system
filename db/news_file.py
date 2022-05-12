
from db.mysql_file import pool

class News_dao:

    # 查询待审批新闻总页数

    def count_unrevuew_page(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s"
        cursor.execute(sql,['待审批'])
        count_page = cursor.fetchone()[0]
        return count_page

    # 查询待审批新闻列表
    def search_unreview_list(self,page):
        con = pool.get_connection()
        cursor = con.cursor()
        # sql = "SELECT n.id,n.title,t.type,u.username " \
        #       "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
        #       "JOIN t_user u ON n.editor_id=u.id " \
        #       "WHERE n.state=%s " \
        #       "ORDER BY n.create_time DESC " \
        #       "LIMIT %s,%s"

        sql = "SELECT n.id,n.title,t.type,u.username " \
              "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
              "JOIN t_user u ON n.editor_id=u.id " \
              "WHERE n.state=%s " \
              "ORDER BY n.create_time DESC " \
              "LIMIT %s,%s"
        cursor.execute(sql,('待审批',(page-1)*10,10))
        count_page = cursor.fetchall()
        return count_page

    # 审批新闻
    def review_news(self,id):
        # try:
        #     con = pool.get_connection()
        #     con.start_transcation()
        #     cursor = con.cursor()
        #     sql = "UPDATE t_news SET state=%s WHERE id=%s"
        #     cursor.execute(sql,('已审批',id))
        #     con.commit()
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="UPDATE t_news SET state=%s WHERE id=%s"
            cursor.execute(sql,("已审批",id))
            con.commit()

        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    # 查询新闻列表
    def search_news(self,page):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT n.id,n.title,t.type,u.username " \
              "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
              "JOIN t_user u ON n.editor_id=u.id " \
              "ORDER BY n.create_time " \
              "LIMIT %s,%s"
        cursor.execute(sql,((page-1)*10,10))
        count_page = cursor.fetchall()
        return count_page

    # 查询新闻总页数
    def search_news_page(self):
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
        cursor.execute(sql)
        count = cursor.fetchone()[0]

        return count








    # 删除新闻
    def delete_news(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'DELETE FROM t_news WHERE id=%s'
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()










# if __name__ == '__main__':
#     a = News_dao().search_news(1)
#     for index in range(len(a)):
#         one = a[index]
#
#
#         print(index+1,one[1],one[2],one[3])
#     opt = input('输入数字:')
#     print(a[int(opt)-1][0])


