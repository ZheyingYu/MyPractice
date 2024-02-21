#类继承练习：人力系统
# 员工分为两类：全职员工 FulltimeEmployee,兼职员工ParttimeEmployee
# 全职和兼职都有姓名name, 工号id 属性
# 都具备打印信息 print_info 打印姓名，工号方法
# 全职有月薪 monthly_salary 属性
# 兼职有日薪 daily_salary 属性，每月工作天数work_days 属性
# 全职和兼职都有计算月薪 calculate_monthly_pay 的方法，但具体计算过程不一样

class Employee():
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def print_info(self):
        print("Name:" + self.name, ", ID:" + str(self.id))

class FulltimeEmployee(Employee):
    def __init__(self,name, id,monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    def calculate_monthly_pay(self):
        return self.monthly_salary

class ParttimeEmployee(Employee):
    def __init__(self, name, id,daily_salary,work_days ):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_monthly_pay(self):
        monthly_pay = self.daily_salary * self.work_days
        return monthly_pay



Zhangsan = FulltimeEmployee("张三",'12138', monthly_salary=20000)
lisi = ParttimeEmployee("李四", "11113", daily_salary=500, work_days=10)
print(lisi.calculate_monthly_pay())
Zhangsan.print_info()