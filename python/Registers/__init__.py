from abc import ABC
from datetime import date
import python.Utils_for_classes as u


class Specialization:
    # предсталяет номер и название дисциплины
    def __init__(self, number, subject_name):
        self.number = number
        self.subject_name = subject_name


class TypeMark:
    def __init__(self, id_type, name_type):
        self.id_type = id_type
        self.name_type = name_type


# реализация шаблона "Легковес"
class SharedRegisterValues:
    def __init__(self, specialization: Specialization, type_mark: TypeMark, mark: int, attendance: bool):
        self.__specialization = specialization
        self.__type_mark = type_mark
        self.__mark = mark
        self.__attendance = attendance
        self.__shared_obj = [self.__specialization, self.__type_mark, self.__mark, self.__attendance]

    @property
    def shared_obj(self):
        return self.__shared_obj


class RegisterFlyweight:
    def __init__(self, shared_register_values: SharedRegisterValues):
        self.__shared_register_values = shared_register_values

    def get_data(self):
        return self.__shared_register_values.shared_obj


class RegisterContext:
    def __init__(self, student, date, flyweight: RegisterFlyweight):
        self.student = student
        self.date = date
        self.flyweight = flyweight

    def get_record(self):
        print(f'уникальные: {self.student}, {self.date}, разделяемые: {self.flyweight}')
        self.flyweight.append(self.student, self.date)
        return self.flyweight


class RegisterFlyweightFactory:
    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_values: SharedRegisterValues) -> RegisterFlyweight:
        temp = next((x for x in self.flyweights if x._RegisterFlyweight__shared_register_values == shared_values), None)
        #temp = filter(lambda x: x == shared_values, self.flyweights)

        if temp:
            return temp
        else:
            temp = RegisterFlyweight(shared_values)
            self.flyweights.append(temp)
            return temp

    @property
    def total(self):
        return len(self.flyweights)


class RegisterRecord:
    def __init__(self, factory: RegisterFlyweightFactory):
        self.reg_factory = factory

    def make_register_record(self, student, date, shared_state) -> RegisterContext:
        flyweight = self.reg_factory.get_flyweight(shared_state)
        record = RegisterContext(student, date, flyweight)
        return record


class DateHomework:
    # структура для хранения дз
    def __init__(self, lesson_date):
        self.lesson_date = date.fromisoformat(lesson_date)
        self.homework = ''


class Register(ABC):
    # модель классного журнала
    def __init__(self, group):
        self.group = group.number
        # self.specialization = specialization


class RegisterMA(Register):
    # модель классного журнала оценок и посещаемости
    def __init__(self, group):
        super().__init__(group)
        self.register = []
        self.flyweight_factory = RegisterFlyweightFactory()
        self.reg_record = RegisterRecord(self.flyweight_factory)

    def edit_register_mark(self, student, date, spec: Specialization, type: TypeMark, mark, atten):
        values = [spec, type, mark, atten]
        date_r = self.reg_record.make_register_record(student, date, values)
        self.register.append(date_r)
        if mark < 4:
            notice = u.Notification(student)
            notice.notify_bad_mark(spec, mark)
    # def show_register_mark
    # def show_register_attendance
    # def edit_register_attendance
    # def show_mark_for_student
    # def show_attendance_for_student


class RegisterHW(Register):
    # модель журнала домашнего задания
    def __init__(self, group, specialization):
        super().__init__(group, specialization)
        self.register = []

    def add_homework(self, date_homework: DateHomework):
        self.register.append(date_homework)



