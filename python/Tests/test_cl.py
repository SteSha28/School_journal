import unittest
import python.Registers as r
import python.Exceptions_for_classes as ec
import python.Users as u


class Tests(unittest.TestCase):

    def setUp(self):
        # создание объектов для всех тестовых методов
        self.admin = u.Admin("admin", "admin", '1999-03-03', "admin", "9035468796", "123qwertY")
        self.student = u.Student("Jon", "Smit", '1991-08-28', "Lenina street, 1", "9059902882", "89Hnvf45")
        self.student2 = u.Student("Jon", "Smit", '1991-08-28', "Lenina street, 1", "9059902882", "89Hnvf45")
        self.student3 = u.Student("Jon", "Smit", '1991-08-28', "Lenina street, 1", "9059902882", "89Hnvf45")
        self.group = u.Group('1A')
        self.specialization = r.Specialization(101, 'русский язык')
        self.teacher = u.Teacher("Sara", "Smit", '1975-09-21', "Lenina street, 2", "9354687525", "96IpHr")

    def test_change_password(self):
        # тест функции смены пароля
        self.student.change_password("123IOpas")
        self.assertEqual("123IOpas", self.student.password)

    def test_add_group(self):
        # тест создания класса(группы) учеников
        self.group.add_student(self.student2)
        self.group.add_student(self.student)
        self.group.add_student(self.student3)
        m = [self.student2.id_user, self.student.id_user, self.student3.id_user]
        self.assertEqual(m, self.group.students)

    def test_delete_group(self):
        # тест функции удаления ученика из класса
        self.group.add_student(self.student)
        self.group.delete_student(self.student)
        self.assertNotIn(self.student.id_user, self.group.students)

    def test_teacher_specialization(self):
        # тест функции добавления специализации преподавателю
        self.teacher.add_specialization(self.specialization)
        self.assertIn(self.specialization.number, self.teacher.specialization)

    def test_teacher_assignment(self):
        # тест функции назначения классу(группе) преподавателя по предмету
        self.teacher.add_specialization(self.specialization)
        self.admin.teacher_assignment(self.teacher, self.group, self.specialization.number)
        rezult = any(key for key in self.teacher.access_group if self.teacher.access_group[key] == self.group.number)
        self.assertTrue(rezult)

    def test_wrong_password(self):
        # тест на выбрасывание исключения функции смены пароля
        self.student.change_password("12345")
        self.assertRaises(ec.UserExc)


if __name__ == '__main__':
    unittest.main()


