# класс-шаблон паттерна "одиночка"
class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super.__new__(cls)
        return Singleton.instance


# функция генерации id для пользователей
def get_id() -> int:
    try:
        with open('D:\\school\\python\\Utils_for_classes\\sequence.txt', 'r+') as sequence:
            id_number = int(sequence.read())
            id_number += 1
            sequence.seek(0)
            sequence.write(str(id_number))
        return id_number
    except FileNotFoundError:
        return 'File not found'


# функция проверки пароля
def check_new_password(paswd: str):
    good_password = True
    if not any(d.isdigit() for d in paswd):
        good_password = False
    if not any(ch.isalpha() for ch in paswd):
        good_password = False
    if not any(ch.islower() for ch in paswd):
        good_password = False
    if not any(ch.isupper() for ch in paswd):
        good_password = False
    return good_password


# класс-медиатор для получения родителем уведомления о плохой оценке
class Notification:
    def __init__(self, student):
        self.student = student

    def notify_bad_mark(self, subject, mark):
        if self.student:
            massage = f"{self.student.first_name} получил оценку {mark} по предмету {subject.subject_name}"

        for parents in self.student.parents:
            parents.get_notice(massage)