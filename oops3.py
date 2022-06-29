# inheritance - inherits, extends, override
class Kiet:

    def __init__(self, sname, sadmno, spercentage):
        self.name = sname
        self.admno = sadmno
        self.percentage = spercentage

    def greet_student(self):
        return f"Hello, {self.name} welcome to the College"

    def fee(self):
        return f"The fee is 1.6 lakh per year"

    def __str__(self):
        return f"The name is {self.name} and the ADM no is {self.admno}"


class Akgec(Kiet):

    def __init__(self, sname, sadmno, spercentage, icard_ribbon):
        # extends of instance attribute
        super().__init__(sname, sadmno, spercentage)
        self.icard_ribbon = icard_ribbon

    # method overriding
    def greet_student(self):
        return f"Hello, {self.name} welcome to AKGEC"

    # instance methods extending
    def fossc(self):
        print(f"Welcome {self.name} to Fossc club of Akgec")


class Jss(Kiet):

    def __init__(self, sname, sadmno, spercentage, campus):
        super().__init__(sname, sadmno, spercentage)
        self.campus = campus

    # method overriding
    def greet_student(self):
        return f"Hello, {self.name} welcome to JSS {self.campus} campus"

    # instance method extending
    def dsc_jss(self):
        print(f"Welcome {self.name} to DSC JSS")


Student_kiet = Kiet(sname="Kanishk", sadmno=2626, spercentage=44)
Student_akg = Akgec(sname="Akshat", sadmno=2627, spercentage=77, icard_ribbon="Red")
Student_jss = Jss(sname="Pavittar", sadmno=2628, spercentage=45, campus="Noida")
print(Student_kiet)
print(Student_jss)
print(Student_akg)

# Polymorphism

students_ghzb = Kiet(sname="Kanishk", sadmno=2626, spercentage=44), Akgec(sname="Akshat", sadmno=2627, spercentage=77,
                                                                          icard_ribbon="Red"), Jss(sname="Pavittar",
                                                                                                   sadmno=2628,
                                                                                                   spercentage=45,
                                                                                                   campus="Noida")


def say_hello_to_students(students):
    for student in students:
        print(student.greet_student())

say_hello_to_students(students_ghzb)
