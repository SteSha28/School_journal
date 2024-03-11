import python.Users as u
import python.SchoolDataBase as sdb
from abc import ABC, abstractmethod


# реализация паттерна "Состояние"
class ApplicationState(ABC):

    @abstractmethod
    def handle(self, *args):
        pass


class InputDataState(ApplicationState):
    def __init__(self):
        self.data = None

    def handle(self, data):
        self.data = data
        return self.data


class VerificationPasswordState(ApplicationState):

    def __init__(self, user: u.User):
        self.user = user
        self.verification = False

    def handle(self, password):
        db_access = sdb.ProxyDBAccessPoint(self.user)
        data = db_access.get_user_info(self.user.id_user)
        data = list(data[0])
        if data[6] == password:
            self.verification = True
        return self.verification


class SuccessVerificationState(ApplicationState):

    def __init__(self, user: u.User, data):
        self.data = data
        self.user = user

    def handle(self, type_user):
        if type_user == 'Student':
            creator = sdb.CreateStudent(self.user)
            creator.create(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5],
                           self.data[6])


class CreatingProcess:

    def __init__(self, user: u.User):
        self.state = 'InputDataState'
        self.user = user
        self.data = None
        self.user = user
        self.verification = False

    def request1(self, val):
        if self.state == 'InputDataState':
            first = InputDataState
            self.data = first.handle(self, val)
            self.state = 'VerificationPasswordState'

    def request2(self, val):
        if self.state == 'VerificationPasswordState':
            second = VerificationPasswordState(self.user)
            self.verification = second.handle(val)
            if self.verification:
                self.state = 'SuccessVerificationState'
            else:
                print(f'Ошибка доступа')

    def request3(self, val):
        if self.state == 'SuccessVerificationState':
            third = SuccessVerificationState(self.user, self.data)
            third.handle(val)
