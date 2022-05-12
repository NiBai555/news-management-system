from db.news_file import News_dao

class News_service:
    __news_service = News_dao()

    # 查询新闻总页数
    def count_unreview_page(self):
        result = self.__news_service.count_unrevuew_page()
        return result

    # 查询待审批新闻列表

    def search_unreview_list(self,page):
        result = self.__news_service.search_unreview_list(page)
        return result

    # 审批新闻
    def review_news(self,id):
        self.__news_service.review_news(id)

    # 删除新闻
    def delete_news(self,id):
        self.__news_service.delete_news(id)

    # 查询新闻总页数
    def count_news_page(self):
        result = self.__news_service.search_news_page()
        return result

    # 查询新闻列表
    def search_news_list(self,page):
        result = self.__news_service.search_news(page)
        return result