
from db.user_file import User_Dao


class User_service:
    __User_info = User_Dao()

    # 读取用户登录信息
    def user_login(self,username,password):

        result = self.__User_info.user_login(username,password)
        return result


    # 读取用户角色

    def user_role(self,username):
        result = self.__User_info.user_role(username)
        return result
    # 查询用户总页数

    def count_user_page(self):
        result = self.__User_info.count_user_page()
        return result

    # 查询用户列表
    def search_user_list(self,page):
        result = self.__User_info.search_user_list(page)
        return result

    # 添加用户
    def insert_user(self,username,password,email,role_id):
        self.__User_info.insert_user(username,password,email,role_id)

    # 修改用户
    def update_user(self,id,username,password,email,role_id):
        self.__User_info.update_user(id,username,password,email,role_id)

    # 删除用户
    def delete_user(self,id):
        self.__User_info.delete_user(id)