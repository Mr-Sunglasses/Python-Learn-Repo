# class
class Students_kiet:
    # class attribute
    type_kiet = "Kiet is an Engineering College"

    # instance Attributes
    def __init__(self, name, branch, session, roll_no, mobile_no, attendence):
        self.name = name
        self.branch = branch
        self.session = session
        self.roll_no = roll_no
        self.mobile_no = mobile_no
        self.attendence = attendence

    # instance Method
    def tell_branch(self):
        return f"The branch of {self.name} is {self.branch}"

    # instance Method with arguments
    def calculate_total_fee(self, year_of_course: int) -> int:
        return f"Your total fee of {year_of_course} will be {1.27 * year_of_course} lakhs"

    # static methods
    '''
    if we write our function like this in the class then it only runs on the Class not on the instance of the class
    
    def pue_eligible(percentage):
        if percentage < 75:
            return f"You are Not Eligible for PUE"
        else:
            return f"You are Eligible for PUE"
    
    print(Student1.pue_elligible(75)) -> error -> 2 positonal arguments given only 1 required as it passes self
    print(Students_kiet.pue_elligible(75)) -> Runs successfully -> You are Eligible for PUE
    '''
    @staticmethod
    def pue_eligible(percentage):  # we can't able to use self.attribute here, or we can't able to use instance attributes here def pue_eligible(self, percentage) -> X
        if percentage < 75:
            return f"You are Not Eligible for PUE"
        else:
            return f"You are Eligible for PUE"

    # dunder methods
    # is used to print out string representation on production mode
    def __str__(self):
        return f"The Student name is {self.name} and there branch is {self.branch} and there session is {self.session} and there roolno is {self.roll_no} and there mobileno is {self.mobile_no}"

    # is used to print out string representation for Debug purposes
    def __repr__(self):
        return f"__repr__ is using for debug purposes"

    '''
        before defining __eq__ is our class
        s1 = (name = a, roll_no = b)
        s1 = (name = a, roll_no = b)
        print(s1 == s2)  -> False 
        
        After defining __eq__ is our class        
        s1 = (name = a, roll_no = b)
        s1 = (name = a, roll_no = b)
        print(s1 == s2)  -> True
        
    '''

    def __eq__(self, other):
        return self.name == other.name and self.branch == other.branch and self.session == other.session and self.roll_no == other.roll_no and self.mobile_no == other.mobile_no


# instance or object of class Student_kiet
Student1 = Students_kiet(name="Prabhakar", branch="CSIT", session="2021-2025", roll_no=2132211233,
                         mobile_no="9436000032", attendence=87)
Student2 = Students_kiet(name="Prabhakar", branch="CSIT", session="2021-2025", roll_no=2132211233,
                         mobile_no="9436000032", attendence=87)
Student3 = Students_kiet(name="Moshin", branch="CS", session="2021-2025", roll_no=2232211233,
                         mobile_no="9426000032", attendence=77)

# this is how we call instance Attributes
print(Student1.name, Student1.session)

# this is how we call class Attributes
print(f"This is class Attribute called on class instance or object{Student1.type_kiet}, This is the class attribute "
      f"called on Class{Students_kiet.type_kiet}")

# this is how we call instance Method
print(Student1.tell_branch())

# this is how we call instance Method with Arguments
print(Student1.calculate_total_fee(4))

# Use of __str__
print(Student1)
print("--------------")
print(str(Student1))
print("---------------")
print(Student1.__str__())

# Use of __repr__
print(Student1.__repr__())
print(repr(Student1))

# USE of __eq__
print(Student1 == Student2)
print(Student1 == Student3)

# Static methods
print(Student1.pue_eligible(75))
print(Students_kiet.pue_eligible(66))
print(Student1.pue_eligible(Student1.attendence))