class Hospital:
    def __init__(self):
        self.hospital_name=input("Enter hospital name:")
        self.location=input("Enter location:")
        self.hos_phone=int(input("Enter phone number:"))
    def display_hospital(self):
        print("Hospital name:",self.hospital_name,"Location:",self.location,"Phone no:",self.hos_phone)
class Department:
    def __init__(self):
        self.dept_name=input("Enter department name:")
        self.doctor_name=input("Enter doctor name:")
    def display_department(self):
        print("Department name:",self.dept_name,"Doctor name:",self.doctor_name)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("enter patient name:")
        self.age=int(input("enter age:"))
        self.gender=input('enter gender:')
        self.phone=int(input("enter phone number:"))
        self.admission_date=input("enter admission date:")
        self.bed_no=int(input("enter the bed number:"))
        self.discharge_date=""
    def set_discharge(self):
        self.discharge_date=input("enter discharge date:")
    def full_summary(self):
        print("Patient summary")
        self.display_hospital()
        self.display_department()
        print("Patient name:",self.patient_name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Phone no:",self.phone)
        print("Admission date:",self.admission_date)
        print("Bed no:",self.bed_no)
        if (self.discharge_date==""):
            print("not yet discharged")
        else:
            print("Discharge date:",self.discharge_date)
p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()

class A:
    def f(self):
        print("In first function f")
    def f(self,a):
        print("In second function f")
    def f(self,a,b):
        print("In third function f")
a=A()
# a.f()
# a.f(10)
a.f(20,30)