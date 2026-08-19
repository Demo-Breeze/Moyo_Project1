class Student:
    count = 0
    total_gpa = 0
    def __init__(self,name, gpa):
        self.name = name
        self.gpa =  gpa
        Student.count =+1
        Student.total_gpa =+ gpa
    
    def get_info(self):
        return f"The Student's name is {self.name} and their gpa is {self.gpa}"
    @classmethod
    def get_count(cls):
        return f'Total Number of Students:{cls.count}' 
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average Gpa: {cls.total_gpa/cls.count}"
Student1= Student("Obama", 3.8)
print(Student1.get_info())