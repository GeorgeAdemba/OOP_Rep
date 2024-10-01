class Student_details:
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name

    def display_details(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Student Name: {self.name}")

student1 = Student_details("S21213", "Roboske Yayo")
student1.display_details()