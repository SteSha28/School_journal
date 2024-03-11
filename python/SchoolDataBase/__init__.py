import sqlite3
from abc import ABC, abstractmethod
import python.Utils_for_classes as u
from python.Users import *


# класс, реализующий базу данных
class SchDataBase:
    connection = sqlite3.connect('db_file.db')
    cursor = connection.cursor()

    def _create_all_tables(self):
        self.cursor.execute("""
        create table User
        ( id_user int not null,
        first_name char(20),
        second_name char(40),
        dob DATE,
        address char(250),
        phone char(10),
        password char(20),
        primary key (id_user)
        );""")

        self.cursor.execute("""
        create table TypeMark(
        id_type int not null,
        name char(25),
        primary key (id_type)
        );""")

        self.cursor.execute("""
        create table Specialization(
        id_spec int not null,
        name char(25),
        primary key (id_spec)
        );""")

        self.cursor.execute("""
        create table SCHGroup(
        id_group int not null ,
        number char(3),
        primary key (id_group)
        );""")

        self.cursor.execute("""
        create table Teacher(
        id_user int not null,
        id_group char(7),
        primary key (id_user),
        constraint FK_CURATOR_NUMBER foreign key (id_group)
        references SCHGroup(id_group),
        constraint FK_TEACHER_ID foreign key (id_user)
        references User(id_user)
        );""")

        self.cursor.execute("""
        create table TeacherGroup(
        id_user int not null,
        id_group char(7) not null,
        primary key (id_user, id_group),
        constraint FK_TEACHER_NUMBER foreign key (id_group)
        references SCHGroup(id_group),
        constraint FK_TEACHER_NUMBERID foreign key (id_user)
        references Teacher(id_user)
        );""")

        self.cursor.execute("""
        create table TeacherSpecialization(
        id_user int not null,
        id_spec int not null,
        primary key (id_user, id_spec),
        constraint FK_TEACHER_SPEC foreign key (id_spec)
        references Specialization(id_spec),
        constraint FK_TEACHER_SPECID foreign key (id_user)
        references Teacher(id_user)
        );""")

        self.cursor.execute("""
        create table Parent(
        id_user int not null,
        work char(250),
        primary key (id_user),
        constraint FK_PARENT_ID foreign key (id_user)
        references User(id_user)
        );""")

        self.cursor.execute("""
        create table Student(
        id_user int not null,
        id_group char(7),
        primary key (id_user),
        constraint FK_STUDENT_ID foreign key (id_user)
        references User(id_user),
        constraint FK_STUDENT_GROUP foreign key (id_group)
        references SCHGroup(id_group)
        );""")

        self.cursor.execute("""
        create table StudentParents(
        id_user int not null,
        id_parent int not null,
        primary key (id_user, id_parent),
        constraint FK_STUDENT_ID foreign key (id_user)
        references User(id_user),
        constraint FK_STUDENT_GROUP foreign key (id_parent)
        references User(id_user)
        );""")

        self.cursor.execute("""
        create table RegisterMA(
        id_user int not null,
        id_spec int not null,
        date DATE not null,
        id_type int not null,
        mark int,
        attendance char(1),
        primary key (id_user, id_spec, date, id_type),
        constraint FK_STUDENT_REG foreign key (id_user)
        references User(id_user),
        constraint FK_SPEC_REG foreign key (id_spec)
        references Specialization(id_spec),
        constraint FK_TYPE_REG foreign key (id_type)
        references TypeMark(id_type)
        );""")

        self.cursor.execute("""
        create table RegisterH(
        id_group int not null,
        id_spec int not null,
        date DATE not null,
        homework char(500),
        primary key (id_group, id_spec, date),
        constraint FK_GROUP_REG foreign key (id_group)
        references SCHGroup(id_group),
        constraint FK_SPEC_REG2 foreign key (id_spec)
        references Specialization(id_spec)
        );""")


# класс - точка доступа к базе данных, шаблон "Прокси"
class ProxyDBAccessPoint:
    def __init__(self, user):
        db = SchDataBase()
        self.cursor = db.cursor
        self.connection = db.connection
        self.user = user

    def create_user(self, data):
        if str(type(self.user)) == "<class 'Users.Admin'>":
            params = data
            insert = """insert into User values
                        ( ?, ?, ?, ?, ?, ?, ?);"""
            self.cursor.execute(insert, params)
            self.connection.commit()
        else:
            print(f"Ошибка доступа")

    def create_specialization(self, number, subject_name):
        if str(type(self.user)) == "<class 'Users.Admin'>":
            params = (number, subject_name)
            insert = """insert into Specialization values
            ( ?, ?);"""
            self.cursor.execute(insert, params)
            self.connection.commit()
        else:
            print(f"Ошибка доступа")

    def create_group(self, id_group, number):
        if str(type(self.user)) == "<class 'Users.Admin'>":
            params = (id_group, number)
            insert = """insert into SCHGroup values
            ( ?, ?);"""
            self.cursor.execute(insert, params)
            self.connection.commit()
        else:
            print(f"Ошибка доступа")

    def create_student(self, id_user, id_group):
        if str(type(self.user)) == "<class 'Users.Admin'>":
            params = (id_user, id_group)
            insert = """insert into Student values
            ( ?, ?);"""
            self.cursor.execute(insert, params)
            self.connection.commit()
        else:
            print(f"Ошибка доступа")

    def edit_marks(self, *args):
        print(f"На доработке")

    def get_user_info(self, id):
        u_id = (id, )
        request = """SELECT * FROM User WHERE id_user = (?);"""
        self.cursor.execute(request, u_id)
        data = self.cursor.fetchall()
        return data


# класс-создатель для реализации фабричного метода
class CreateUser:
    def __init__(self, user):
        self.user = user

    def create(self) -> User:
        pass


# 1-4 классы фабричного метода
# 1
class CreateStudent(CreateUser):

    def __int__(self, user):
        super().__int__(user)

    def create(self, first_name, second_name, dob, address, phone, password, id_group):
        db_access = ProxyDBAccessPoint(self.user)
        student = Student(u.get_id(), first_name, second_name, dob, address, phone, password)
        data = (student.id_user, student.first_name, student.second_name, student.dob, student.address, student.phone,
                student.password)
        db_access.create_user(data)
        db_access.create_student(student.id_user, id_group)


# 2
class CreateParent(CreateUser):
    def create(self, first_name, second_name, dob, address, phone, password):
        return Parent(first_name, second_name, dob, address, phone, password)


# 3
class CreateTeacher(CreateUser):
    def create(self, first_name, second_name, dob, address, phone, password):
        return Teacher(first_name, second_name, dob, address, phone, password)


# 4
class CreateAdmin(CreateUser):
    def create(self, first_name, second_name, dob, address, phone, password):
        return Admin(first_name, second_name, dob, address, phone, password)


# реализация шаблона "Стратегия"
class ViewerRegister(ABC):
    @abstractmethod
    def view_mode(self):
        pass


class UserRegisterViewing:
    def __init__(self, viewer: ViewerRegister):
        self.__viewer = viewer

    def set_viewer_strategy(self, viewer: ViewerRegister):
        self.__viewer = viewer

    def view(self):
        self.__viewer.view_mode()


class TeacherViewerRegister(ViewerRegister):
    def view_mode(self):
        print(f'Промотр успеваемости всего класса')


class StudentViewerRegister(ViewerRegister):
    def view_mode(self):
        print(f'Просмотр успеваемости учащегося')