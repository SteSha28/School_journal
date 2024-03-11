import python.Registers as reg
import python.Users as us
from abc import ABC, abstractmethod


# классы шаблона "Абстрактная фабрика"
class ReportMarks(ABC):

    @abstractmethod
    def release_report_marks(self, group: us.Group, specialization: reg.Specialization):
        pass


class ReportMarksQuarter(ReportMarks):
    def release_report_marks(self, group: us.Group, specialization: reg.Specialization):
        print(f"Отчёт по успеваемости за четверть")


class ReportMarksYear(ReportMarks):
    def release_report_marks(self, group: us.Group, specialization: reg.Specialization):
        print(f"Отчёт по успеваемости за год")


class ReportAttendance(ABC):

    @abstractmethod
    def release_report_attendance(self, group: us.Group, specialization: reg.Specialization):
        pass


class ReportAttendanceQuarter(ReportAttendance):
    def release_report_attendance(self, group: us.Group, specialization: reg.Specialization):
        print(f"Отчёт по посещаемости за четверть")


class ReportAttendanceYear(ReportAttendance):
    def release_report_attendance(self, group: us.Group, specialization: reg.Specialization):
        print(f"Отчёт по посещаемости за год")


class CreatorReports(ABC):

    @abstractmethod
    def create_report_marks(self, group: us.Group, specialization: reg.Specialization) -> ReportMarks:
        pass

    def create_report_attendance(self, group: us.Group, specialization: reg.Specialization) -> ReportAttendance:
        pass


class CreatorReportsQuarter(CreatorReports):
    def create_report_marks(self, group: us.Group, specialization: reg.Specialization):
        return ReportMarksQuarter().release_report_marks(group, specialization)

    def create_report_attendance(self, group: us.Group, specialization: reg.Specialization):
        return ReportAttendanceQuarter().release_report_attendance(group, specialization)


class CreatorReportsYear(CreatorReports):
    def create_report_marks(self, group: us.Group, specialization: reg.Specialization):
        return ReportMarksYear().release_report_marks(group, specialization)

    def create_report_attendance(self, group: us.Group, specialization: reg.Specialization):
        return ReportAttendanceYear().release_report_attendance(group, specialization)
