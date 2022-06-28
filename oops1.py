# class
class Students_kiet:
    # class attribute
    type_kiet = "Kiet is an Engineering College"

    # instance Attributes
    def __init__(self, name, branch, session, roll_no, mobile_no):
        self.name = name
        self.branch = branch
        self.session = session
        self.roll_no = roll_no
        self.mobile_no = mobile_no


# instance or object of class Student_kiet
Student1 = Students_kiet(name="Prabhakar", branch="CSIT", session="2021-2025", roll_no=2132211233,
                         mobile_no="9436000032")

# this is how we call instance Attributes
print(Student1.name, Student1.session)

# this is how we call class Attributes
print(f"This is class Attribute called on class instance or object{Student1.type_kiet}, This is the class attribute "
      f"called on Class{Students_kiet.type_kiet}")
