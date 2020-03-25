from datetime import datetime

db_data = [
    {'name': 'jason',
     'sex': '男',
     'brithday': '19900101'
     },
    {'name': 'ahsliy',
     'sex': '女',
     'brithday': '19830102'
     },
    {'name': 'tommy',
     'sex': '男',
     'brithday': '19800908'
     },
    {'name': 'luchy',
     'sex': '女',
     'brithday': '19920909'
     }
]

"""
******************************
欢迎使用【】
    1、显示所有学生信息-同时计算学生年龄
    2、新增学生信息
    3、查询学生信息
    4、修改学生信息
    5、删除学生信息
    0、退出系统
******************************
"""


# 西方思维//精确逻辑
# 每天300行代码

# 哈哈哈短发


# 学生类
class Student:

    # 学生初始化
    def __init__(self, name, sex, brithday):
        self.name = name
        self.sex = sex
        self.brithday = brithday

    # 计算年龄
    def get_age(self):
        if self.brithday:
            this_year = datetime.now().year
            age = this_year - int(self.brithday[:4])
            return age
        else:
            print('年龄未知')


# 学生管理系统类
class StudentSys:
    def __init__(self, name):
        self.name = name
        self.data = []

    # 美化输出
    def beauty(self, data_list):
        # 增加index 索引序号
        for index, student in enumerate(data_list):
            print(f'序号：{index}', end='\t')
            print(f'名字：{student.name}', end='\t')
            print(f'性别：{student.sex:3}', end='\t')  # 固定宽度
            print(f'生日：{student.brithday}', end='\t')
            print(f'年龄：{student.get_age()}')

    # 加载数据
    def load_data(self):
        for student_data in db_data:
            student = Student(student_data['name'], student_data['sex'],
                              student_data['brithday'])
            self.data.append(student)

    def start(self):
        self.load_data()
        while True:
            self.show_menu()
            op = input('选择操作：')
            if op == '1':
                self.show_all_studeng()
            elif op == '2':
                self.create_student()
            elif op == '3':
                self.find_student()
            elif op == '4':
                self.modify_student()
            elif op == '5':
                self.remove_student()
            elif op == '0':
                print('退出程序')
                break
            else:
                print('请输入正常的操作序号')

    # 选择性别
    def choose_sex(self):
        sex = input('选择性别：（1 男| 2 女）').strip()  # 去除空格
        while True:
            if sex == '1':
                return '男'
            elif sex == '2':
                return '女'
            elif not sex:
                return '未知'
            else:
                continue

    # 根据名字查找学生
    def find_student_by_name(self):
        name = self.input_name()
        find_list = []
        for student in self.data:
            if name.lower() in student.name.lower():
                find_list.append(student)
        if find_list:
            return find_list
        else:
            print(f'没有找到学生：{name}')

    # 强制输入名字
    def input_name(self):
        while True:
            name = input('输入名字：').strip()
            if name:
                return name
            else:
                continue

    # 显示菜单
    def show_menu(self):
        print(f"""
        ************************************
        欢迎使用【{self.name}】
            1、显示所有学生信息-同时计算学生年龄
            2、新增学生信息
            3、查询学生信息
            4、修改学生信息
            5、删除学生信息
            0、退出系统
        ************************************
        """)

    # 显示所有学生信息
    def show_all_studeng(self):
        self.beauty(self.data)

    # 新建学生信息
    def create_student(self):
        name = self.input_name()
        sex = self.choose_sex()
        brithday = input('输入生日：')
        student = Student(name, sex, brithday)
        self.data.append(student)

    # 3、查询学生信息
    def find_student(self):
        find_list = self.find_student_by_name()
        self.beauty(find_list)

    # 修改学生信息
    def modify_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty(find_list)
            index_s = int(input('选择需要修改到序号：'))
            student = find_list[index_s]
            print('当前修改到是：')
            self.beauty([student])
            name = input('新名字：').strip()
            sex = self.choose_sex()
            brithdday = input('输入生日：')
            if name:
                student.name == name
            student.sex = sex
            student.brithday = brithdday

    # 删除学生信息
    def remove_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty(find_list)
            index_s = int(input('选择需要删除到序号：'))
            print('当前要删除的是：')
            student = find_list[index_s]
            self.beauty([student])
            self.data.remove(student)


if __name__ == '__main__':
    student_sys = StudentSys("python面向对象编程管理系统DEMO")
    student_sys.start()
