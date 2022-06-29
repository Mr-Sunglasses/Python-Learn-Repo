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

    # instance Method
    def tell_branch(self):
        return f"The branch of {self.name} is {self.branch}"

    # instance Method with arguments
    def calculate_total_fee(self, year_of_course: int) -> int:
        return f"Your total fee of {year_of_course} will be {1.27 * year_of_course} lakhs"


# instance or object of class Student_kiet
Student1 = Students_kiet(name="Prabhakar", branch="CSIT", session="2021-2025", roll_no=2132211233,
                         mobile_no="9436000032")

Student2 = Students_kiet(name="Moshin", branch="CS", session="2021-2025", roll_no=2132211233,
                         mobile_no="94126000032")

# Working of self keyword
print(Student1.tell_branch())

print(Students_kiet.calculate_total_fee(Student2,6))

print(Students_kiet.tell_branch(Student2))