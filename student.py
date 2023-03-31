import os.path
import time


def menu():
    print("""---------------------学生管理系统------------------
             选择要进行的指令：
             （1）录入学生信息模块

             （2）查找学生信息模块

              （3）删除学生信息模块

              （4）修改学生信息模块

              （5）学生成绩排名模块

               （6）统计学生总人数模块
 
               （7）显示全部学生信息模块
               
               退出系统 选择 请输入y""")


# 用字典来查询
def insert():
    while 1 == 1:
        message = []
        name = input("请输入学生姓名")
        while not name:
            print('输入错误，请重新输入')
            name = input("请输入学生姓名")
        id = input("输入学生学号")
        while not id:
            print('输入错误请从新输入')
            id = input("输入学生学号")
        while True:
            try:
                chinese = int(input('输入语文成绩'))
                math = int(input('输入数学成绩'))
                break
            except:
                print('输入错误，请重新输入')
        d = {'id': id, 'name': name, 'chinese': chinese, 'math': math}
        message.append(d)
        print(d)
        x = input("是否继续插入（y/n）")
        if (x == 'y' or x == 'Y'):
            save(message)
            continue
        if (x == 'n' or x == 'N'):
            save(message)
        break


def save(lst):
    fp = open('D:\project\student\student_message.txt', 'a+')
    for item in lst:
        fp.write(str(item) + '\n')
    fp.close()


# 全局变量
def seek():
    while 1 == 1:
        name = ''
        id = 0
        result = []
        if os.path.exists('D:\project\student\student_message.txt'):

            mode = input('选择使用名字或id查询（1，2)')
            while not mode:
                print('输入错误，请重新输入')
                mode = input('选择使用名字或id查询（1，2)')
            if mode == '1':
                name = input('输入要查询的姓名')
                while not name:
                    name = input('输入要查询的姓名')
            elif mode == '2':
                id = input('请输入要查询的id')
                while not id:
                    id = input('请输入要查询的id')
            else:
                print('输入错误，请重新输入')
        with open('D:\project\student\student_message.txt', 'r+') as fp:
            lst = fp.readlines()
            for item in lst:
                d = dict(eval(item))
                if d['id'] == id:
                    result.append(d)
                elif d['name'] == name:
                    result.append(d)
        if len(result) == 0:
            print('没有查询到数据')
        for item in result:
            print(item)
        result.clear()
        x = input('是否继续查询(y/n)')
        while not x:
            print('输入错误，请重新输入')
            x = input('是否继续查询(y/n)')
        if (x == 'y' or x == 'Y'):
            continue
        elif (x == 'n' or x == 'N'):
                break
        else:
            print('输入错误，请重新输入')
        fp.close()


# 文件指针的处理：通过开关文件来重置指针位置，文件的打开方式,    把没有被删的写进去就相当于把要删的删掉了
def delete():
    while True:
        show()
        with open("D:\project\student\student_message.txt", 'r+') as fp:
            message = fp.readlines()
            id = input("输入要删除的学生id")
            while not id:
                id = input("输入要删除的学生id")
            flag = False
            with open('D:\project\student\student_message.txt', 'w+') as wp:
                for item in message:
                    d = dict(eval(item))
                    if d['id'] != id:
                        wp.write(str(d) + '\n')
                    else:
                        flag = True
                if flag == True:
                    print('删除成功')
                else:
                    print('该生未录入该系统')
            show()
            x = input("是否继续删除（y/n）")
            if (x == 'y' or x == 'Y'):
                continue
            if (x == 'n' or x == 'N'):
                break


# 文件操作,输入原来的数据
def modify():
    while True:
        show()
        d = {}
        lst = []
        id = input('请输入要修改学生的id')
        with open('D:\project\student\student_message.txt', 'r') as fp:
            lst = fp.readlines()
            with open('D:\project\student\student_message.txt', 'w') as wp:
                for item in lst:
                    d = dict(eval(str(item)))
                    if d['id'] == id:
                        print('找到该学生')
                        while True:
                            choice = input('请输入要修改的项目：id（1），chinese(2),math(3)')
                            if choice == '1':
                                d[id] = input('请输入id')
                            if choice == '2':
                                d['chinese'] = input('请输入chinese成绩')
                            if choice == '3':
                                d['math'] = input('请输入math成绩')

                            wp.write(str(d) + '\n')
                            id=None

                            x = input('是否继续修改该同学其他信息（y/n）')
                            if x == 'y' or x == 'Y':
                                continue
                            elif x == 'n' or x == 'N':
                                break
                    else:
                        wp.write(str(d) + '\n')
        show()
        a = input('是否继续修改其他同学信息（y/n）')
        if a == 'y' and a == 'Y':
            continue
        else:
            break


# sort 函数 排序需要考虑 1.升序降序，2排序方式
def sort():
    lst = []
    d = {}

    if os.path.exists('D:\project\student\student_message.txt'):
        with open('D:\project\student\student_message.txt', 'r') as fp:
            message = []
            lst = fp.readlines()
            for item in lst:
                d = dict(eval(item))
                message.append(d)
    else:
        return
    while True:

        while True:

            choice = input('请选择升序/降序（1/2）')

            if choice == '1':
                b = False
                break
            elif choice == '2':
                b = True
                break
            else:
                print('请输入正确的选择')
        while True:
            mode = input('选择排序方式（按学号排名1，按chinese排名2，按math排名3）')
            if mode == '1':
                message.sort(key=lambda x: (int(x['id'])), reverse=b)
                print(message)
                break
            elif mode == '2':
                message.sort(key=lambda x: (int(x['chinese'])), reverse=b)
                print(message)
                break
            elif mode == '3':
                message.sort(key=lambda x: (int(x['math'])), reverse=b)
                print(message)
                break
            else:
                print('请选择正确的排序方式')
        idea = input('是否继续查看（y/n）')
        if idea == 'Y' or idea == 'y':
            continue
        elif idea == 'N' or idea == 'n':
            break


# print
def total():
    list = []
    if os.path.exists('D:\project\student\student_message.txt'):
        with open('D:\project\student\student_message.txt', 'r') as fp:
            list = fp.readlines()
            if not list:
                print('暂未输入学生信息')
            else:
                print('共有人数%d' % (len(list)))
    else:
        print('暂无数据信息')

#return 还可以用来结束函数
def show():
    lst = []
    message = []
    d = {}
    if os.path.exists('D:\project\student\student_message.txt'):
        with open('D:\project\student\student_message.txt', 'r') as fp:
            lst = fp.readlines()
            for item in lst:
                d=dict(eval(item))
                message.append(d)

        for item in message:
            print(item)
        time.sleep(1)
    else:
        print('没有储存数据')


if __name__ == '__main__':
    while 1 == 1:
        menu()
        choice = input("请输入要进行的指令")
        if (choice == 'Y' or choice == 'y'):
            print("退出成功")
            break
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if (choice == '1'):
                insert()
            if (choice == '2'):
                seek()
            if (choice == '3'):
                delete()
            if (choice == '4'):
                modify()
            if (choice == '5'):
                sort()
            if (choice == '6'):
                total()
            if (choice == '7'):
                show()
        else:
            print("请重新输入")
