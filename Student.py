# extremely useful and help to make programs more organized and powerful

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    def type_of_student(self):
        if self.gpa >= 3.5:
            return "Honor Roll"
        elif self.gpa >= 3.0:
            return "Above Average"
        else:
            return "Below Average"


# init is a special function that is called when you create a new object based on this class