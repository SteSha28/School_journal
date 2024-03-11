import Users as u
import Registers as reg
import SchoolDataBase as sdb
import pandas as pd
import CreatingUsers as cr

#firstp = u.Parent("jon", "galt", '1991-08-28', "lenina strit 1", "9056321215", "GFoige56")
# firstst = u.Student("jon", "galt", '28-08-1991', "lenina strit 1", "9056321215", "GFoige56")
# user = u.User("jon", "galt", '28-08-1991', "lenina strit 1", "9056321215", "GFoige56")

# firstp.change_password('12345')
# print(user.first_name)

admin1 = u.SuperUser
admin1.login = 'admin1'
admin2 = u.SuperUser
print(admin2.login)

# 10
# roditel = u.Parent("Richard", "galt", '1991-08-28', "lenina strit 1", "9056321215", "GFoige56")
# uchenik = u.Student("jon", "galt", '2008-08-08', "lenina strit 1", "9056321215", "GFoige56")
# uchenik.parents.add(roditel)
# klass = u.Group('8a')
# klass.add_student(uchenik)
#
# subject = reg.Specialization(1, 'русский язык')
#
# str_l = reg.StructList(uchenik)
# str_l.mark = 3
# date = reg.DateRating('2023-11-11')
# date.add_marks(str_l)
#
# jurnal = reg.RegisterMA(klass, subject)
# jurnal.edit_register_mark(date)


# 11
# klass = u.Group('8a')
# subject1 = reg.Specialization(1, 'русский язык')
# subject2 = reg.Specialization(2, 'математика')
# subject3 = reg.Specialization(3, 'физическая культура')
# klass.add_specialization(subject1)
# klass.add_specialization(subject2)
# klass.add_specialization(subject3)
# r_creator = reg.RegisterCreator()
# r_creator.create_register(klass, subject1)
# r_creator.create_register(klass, subject2)
# r_creator.create_register(klass, subject3)
#
# print(klass.registers_mark)
# print(klass.registers_homework)
#
# creator = u.CreateStudent()
# uchenik = creator.create("jon", "galt", '2008-08-08', "lenina strit 1", "9056321215", "GFoige56")
# print(uchenik.first_name)

# 12
# creator = u.CreateTeacher()
# teacher1 = creator.create('Юлия Петровна', 'Иванова', '1991-08-28', 'lenina strit 1',
#                           '9023216547', 'Hlbf89dhs')
# klass = u.Group('8a')
# subject1 = reg.Specialization(1, 'русский язык')
# teacher1.access_group.append(klass)
# teacher1.show_report(klass, subject1, 'quarter')

# 13
# db = sdb.SchDataBase()
# # db._create_all_tables()
# creator = u.CreateTeacher()
# teacher1 = creator.create('Юлия Петровна', 'Иванова', '1991-08-28', 'lenina strit 1',
#                        '9023216547', 'Hlbf89dhs')
# db_access = sdb.ProxyDBAccessPoint(teacher1)
# db_access.create_specialization(4, 'геометрия')
# df = pd.read_sql_query("""select * from Specialization;""", db.connection)
# print(df)

# 14
# db = sdb.SchDataBase()
# point = sdb.ProxyDBAccessPoint('us')
# data = point.get_user_info(111)
# data = list(data[0])
# admin = u.Admin(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
# # point2 = sdb.ProxyDBAccessPoint(admin)
# # point2.create_group(1, '1A')
# pros = cr.CreatingProcess(admin)
# data = ['Елизавета Николаевна', 'Степанова', '2015-06-06', 'Иркутский тр. 42-1', '9023035485', 'Parol123', 1]
# pros.request1(data)
# pros.request2('Qwerty')
# pros.request3('Student')

#15
# klass = u.Group(111, '8a')
# uchenik1 = u.Student(112, 'Анна', 'Николаева', '2015-02-03', 'dsjhjs',
#                      '9056321475', 'HFGIU45r')
# uchenik2 = u.Student(113, 'Алина', 'Николаева', '2015-03-02', 'dsjhjs',
#                      '9056321475', 'HFGIU45r')
# klass.add_student(uchenik1)
# klass.add_student(uchenik2)
#
# subject1 = reg.Specialization(1, 'русский язык')
# subject2 = reg.Specialization(2, 'литература')
#
# type_mark1 = reg.TypeMark(1, 'контрольная работа')
# type_mark2 = reg.TypeMark(2, 'дз')
#
# jurnal = reg.RegisterMA(klass)
#
# jurnal.edit_register_mark(uchenik1, '2023-11-25', subject1, type_mark1, 5, True)
# jurnal.edit_register_mark(uchenik2, '2023-11-25', subject1, type_mark1, 5, True)
# jurnal.edit_register_mark(uchenik2, '2023-11-25', subject2, type_mark1, 5, True)
# print(jurnal.flyweight_factory.total)

#16
# uchenik1 = u.Student(112, 'Анна', 'Николаева', '2015-02-03', 'dsjhjs',
#                      '9056321475', 'HFGIU45r')
# teacher1 = u.Teacher(113, 'Анна', 'Петрова', '1999-02-03', 'dsjhjs',
#                      '9056321475', 'HFGIU45r')
#
# view = sdb.UserRegisterViewing(sdb.TeacherViewerRegister())
# view.view()
# view.set_viewer_strategy(sdb.StudentViewerRegister())
# view.view()

