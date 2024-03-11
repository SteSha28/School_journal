from abc import ABC, abstractmethod
import python.Utils_for_classes as u
import datetime
import python.Registers as r
import python.Exceptions_for_classes as ec
import python.Reports_for_school as rep


class User(ABC):
    # общая модель пользователя
    def __init__(self, id_user, first_name, second_name, dob, address, phone, password):
        # try:
        #     id = u.get_id()
        #     if type(id) is not int:
        #         raise ec.UserExc("Wrong ID")
        #     else:
        #         self.id_user = id
        # except ec.UserExc as e:
        #     print(f"{e}")
        self.id_user = id_user
        try:
            if any(d.isdigit() for d in first_name) or any(d.isdigit() for d in second_name):
                raise ec.UserExc("Wrong name")
            else:
                self.first_name = first_name.title()
                self.second_name = second_name.title()
        except ec.UserExc as e:
            print(f"{e}")
        try:
            self.dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            print("Uncorrected date")
        self.address = address
        try:
            if phone.isnumeric:
                self.phone = phone
            else:
                raise ec.UserExc("Wrong phone")
        except ec.UserExc as e:
            print(f"{e}")
        try:
            if u.check_new_password(password):
                self.password = password
            else:
                raise ec.UserExc("Uncorrected password")
        except ec.UserExc as e:
            print(f"{e}")

    # функция смены пароля
    @abstractmethod
    def change_password(self, password):
        try:
            if u.check_new_password(password):
                self.password = password
            else:
                raise ec.UserExc("Uncorrected password")
        except ec.UserExc as e:
            print(f"{e}")


class Student(User):
    # модель пользователя "ученик"
    def __init__(self, id_user, first_name, second_name, dob, address, phone, password):
        super().__init__(id_user, first_name, second_name, dob, address, phone, password)
        self.parents = set()  # set

    def change_password(self, password):
        super().change_password(password)

    def view_marks(self):
        pass

    def view_attendance(self):
        pass

    def view_homework(self):
        pass


class Parent(Student):
    # модель пользователя "родитель"
    def __init__(self, id_user, first_name, second_name, dob, address, phone, password):
        super().__init__(id_user, first_name, second_name, dob, address, phone, password)

    def change_password(self, password):
        super().change_password(password)

    @staticmethod
    def get_notice(massage):
        print(f"{massage}")


class Teacher(User):
    # модель пользователя "учитель"
    def __init__(self,id_user, first_name, second_name, dob, address, phone, password):
        super().__init__(id_user, first_name, second_name, dob, address, phone, password)
        self.access_group = []
        self.specialization = set()
        self.curator = []

    def change_password(self, password):
        super().change_password(password)

    # функция добавления специальности учителю
    def add_specialization(self, specialization):
        self.specialization.add(specialization.number)

    def show_report(self, group, specialization, time):
        if group in self.access_group:
            if time == 'year':
                report = rep.CreatorReportsYear()
            elif time == 'quarter':
                report = rep.CreatorReportsQuarter()
            reportm = report.create_report_marks(group, specialization)
            reporta = report.create_report_attendance(group, specialization)
            return reportm, reporta

    # def edit_marks
    # def edit_attendance
    # def edit_homework


class Admin(Teacher):
    # модель пользователя "администратор"
    def __init__(self, id_user, first_name, second_name, dob, address, phone, password):
        super().__init__(id_user, first_name, second_name, dob, address, phone, password)

    def change_password(self, password):
        super().change_password(password)

    # функция назначения классу(группе) учителя по дисциплине
    def teacher_assignment(self, teacher, group, specialization):
        if specialization in teacher.specialization:
            teacher.access_group[specialization] = group.number

    # def create_user(self):
    # def delete_user
    # def correction_user
    # def create_group
    # def edit_group
    # def create_specialization_list
    # def edit_specialization_list


class Group:
    # модель класса учеников
    def __init__(self, id_group, number):
        self.number = number
        self.id = id_group
        self.students = []
        self.specializations = []
        self.registers_mark = []
        self.registers_homework = []

    # функция добавления ученика в класс
    def add_student(self, student: Student):
        self.students.append(student.id_user)

    # функция удаления ученика из класса
    def delete_student(self, student):
        self.students.remove(student.id_user)

    # функция добавления дисциплины классу
    def add_specialization(self, specialization):
        self.specializations.append(specialization)


# класс для тестирования шаблона "Одиночка"
class SuperUser(u.Singleton):
    login = ''
    password = ''

