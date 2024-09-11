class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay =  pay
        self.email = fname + "." + lname + "@company.com"

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

emp_1 = Employee("George","Ademba","5000000")
emp_2 = Employee("John","Doe","2000000")

print("Name:",emp_1.fullname(),)
print("Pay: shs", emp_1.pay)
print("Email:", emp_1.email)

print("Name:",emp_2.fullname(),)
print("Pay: shs", emp_2.pay)
print("Email:", emp_2.email)
