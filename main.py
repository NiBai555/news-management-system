from colorama import Fore,Style
from service.user_service import User_service
from service.news_service import News_service
from service.role_service import Role_service
import os
import sys
import time
from getpass import getpass







__user_service = User_service()
__news_service = News_service()
__role_service = Role_service()

while True:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX,'\n\t================================')
    print(Fore.LIGHTCYAN_EX,'\n\t欢迎来到新闻信息管理系统')
    print(Fore.LIGHTBLUE_EX,'\n\t================================')
    print(Fore.LIGHTBLUE_EX,'\n\t1.登录系统')
    print(Fore.LIGHTBLUE_EX, '\n\t2.退出系统')
    print(Style.RESET_ALL)

    opt = input('\n\t请输入操作编号:')
    if opt == '1':
        username = input('\n\t用户名:')
        password = getpass('\n\t密码:')
        result = __user_service.user_login(username,password)

        #登录成功
        if result == True:
            role = __user_service.user_role(username)
            while True:
                os.system('cls')
                if role == '新闻编辑':
                    # 审批新闻
                    print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                    print(Style.RESET_ALL)

                    opt = input('\n\t请输入操作编号:')
                    if opt == '1':
                        page = 1
                        while True:
                            os.system('cls')
                            count_page = __news_service.count_unreview_page()
                            result = __news_service.search_news_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTWHITE_EX,
                                      '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))
                            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                            print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                            print(Style.RESET_ALL)

                            opt = input('请输入操作编号:')
                            if opt == 'back':
                                break
                            elif opt == 'prev' and page > 1:
                                page -= 1
                            elif opt == 'next' and page < count_page:
                                page += 1
                            elif int(opt) >= 1 and int(opt) <= 10:
                                new_id = result[int(opt) - 1][0]
                                __news_service.review_news(new_id)
                    elif opt == '2':
                        page = 1
                        while True:
                            os.system('cls')
                            count_page = __news_service.count_news_page()
                            result = __news_service.search_news_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTWHITE_EX,
                                      '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))

                            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                            print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                            print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                            print(Style.RESET_ALL)

                            opt = input('请输入操作编号:')
                            if opt == 'back':
                                break
                            elif opt == 'prev' and page > 1:
                                page -= 1
                            elif opt == 'next' and page < count_page:
                                page += 1
                            elif int(opt) >= 1 and int(opt) <= 10:
                                new_id = result[int(opt) - 1][0]
                                __news_service.delete_news(new_id)
                    elif opt == 'back':
                        break





                elif role == '管理员':
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登陆")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input('请输入操作编号:')
                    if opt == '1':
                        while True:
                            os.system('cls')
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)

                            opt = input('\n\t请输入操作编号:')
                            if opt == '1':
                                # page=1
                                # while True:
                                #     os.system('cls')
                                #     count_page = __news_service.count_unreview_page()
                                #     result = __news_service.search_unreview_list(page)
                                #     for index in range(len(result)):
                                #         one = result[index]
                                #         print(Fore.LIGHTWHITE_EX,'\n\t%d\t%s\t%s\t%s'%(index+1,one[1],one[2],one[3]))
                                #
                                #     print(Fore.LIGHTBLUE_EX,'\n\t-------------------------')
                                #     print(Fore.LIGHTRED_EX,'\n\t%s/%s'%(page,count_page))
                                #
                                #     print(Fore.LIGHTBLUE_EX,'\n\t-------------------------')
                                #     print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                #     print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                #     print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                #     print(Style.RESET_ALL)
                                #
                                #     opt = input("\n\t输入操作编号:")
                                #
                                #     if opt == 'back':
                                #         break
                                #     elif opt == 'prev' and page>1:
                                #         page-=1
                                #     elif opt == 'next' and page<count_page:
                                #         page+=1
                                #     elif int(opt) >= 1 and int(opt) <= 10:
                                #         new_id = result[int(opt)-1][0]
                                #         __news_service.review_news(new_id)
                                page = 1
                                while True:
                                    os.system('cls')
                                    # 待审批新闻总页数
                                    count_page = __news_service.count_unreview_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTWHITE_EX,
                                              '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)

                                    opt = input('请输入操作编号:')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10:
                                        new_id = result[int(opt) - 1][0]
                                        __news_service.review_news(new_id)


                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __news_service.count_news_page()
                                    result = __news_service.search_news_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTWHITE_EX,
                                              '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)

                                    opt = input('请输入操作编号:')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10:
                                        new_id = result[int(opt) - 1][0]
                                        __news_service.delete_news(new_id)
                            elif opt == 'back':
                                break



                    # 用户管理
                    elif opt == '2':
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)

                            opt = input("请输入操作编号:")
                            if opt == "back":
                                break
                            # 添加用户
                            elif opt == '1':
                                os.system('cls')
                                username = input("\n\t用户名:")
                                password = getpass("\n\t密码:")
                                repassword = getpass("\n\t请再次输入密码:")
                                if password != repassword:
                                    print("\n\t密码输入不一致，3秒后返回")
                                    time.sleep(3)
                                    continue
                                email = input("\n\temail:")
                                result = __role_service.search_role()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTMAGENTA_EX,'\n\t%d.%s'%(index+1,one[1]))
                                    print(Style.RESET_ALL)


                                opt = input("\n\t请输入选择的角色:")
                                role_id = result[int(opt)-1][0]
                                __user_service.insert_user(username,password,email,role_id)
                            # 修改用户
                            elif opt == '2':

                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __user_service.count_user_page()
                                    result = __user_service.search_user_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTWHITE_EX,
                                              '\n\t%d\t%s\t%s' % (index + 1, one[1],one[2]))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)

                                    opt = input("\n\t输入操作编号:")

                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1

                                    elif 1 <= int(opt) <= 10:
                                        os.system('cls')
                                        id = result[int(opt) - 1][0]
                                        username = input("\n\t新用户名:")
                                        password = getpass("\n\t新密码:")
                                        repassword = getpass("\n\t重新输入密码:")
                                        if password != repassword:
                                            print('两次输入不一致,3秒后自动返回')
                                            time.sleep(3)
                                            continue

                                        email = input("\n\t新邮箱:")

                                        result_role = __role_service.search_role()
                                        for index in range(len(result_role)):
                                            one = result_role[index]
                                            print(Fore.LIGHTCYAN_EX,'\n\t%d\t%s'%(index+1,one[1]))
                                        print(Style.RESET_ALL)

                                        opt = input("\n\t请输入编号:")
                                        role_id = result_role[int(opt)-1][0]

                                        opt = input("\n\t是否保存（y/n）")
                                        if opt == 'Y' or opt == 'y':
                                            __user_service.update_user(id,username,password,email,role_id)
                                            print('\n\t保存成功,3秒返回')
                                            time.sleep(3)

                            # 删除用户
                            if opt == '3':
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __user_service.count_user_page()
                                    result = __user_service.search_user_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTWHITE_EX,'\n\t%d\t%s' % (index + 1, one[1]))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, '\n\t%s/%s' % (page, count_page))

                                    print(Fore.LIGHTBLUE_EX, '\n\t-------------------------')
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)

                                    opt = input("\n\t输入操作编号:")

                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif int(opt) > 0 and int(opt) <= 10:
                                        new_id = result[int(opt) - 1][0]
                                        print('-------')
                                        print(new_id)
                                        __user_service.delete_user(new_id)
                                        print("\n\t删除成功(3秒自动返回)")








                    # 退出登录
                    elif opt == 'back':
                        break

                    # 退出系统

                    elif opt == 'exit':
                        sys.exit(0)






    elif opt == '2':
        sys.exit(0)
