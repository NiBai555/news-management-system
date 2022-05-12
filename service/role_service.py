from db.role_file import Role_info


class Role_service:

    __Role_service=Role_info()
    def search_role(self):
        result = self.__Role_service.search_role()
        return result

