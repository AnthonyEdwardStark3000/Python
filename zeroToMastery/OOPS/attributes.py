class Example:
    isStudent = True  # Class Object Attribute - Static in nature

    def __init__(self, college, department):
        self.college = college  # attributes - Dynamic in nature
        self.department = department
        self.examination()

    def examination(self):
        if self.isStudent:
            print(
                f"Examination starts on 22nd of this month for {self.department} Department")
        print(f"Enjoy you'r study time.")


suresh = Example("TCE", "MCA")
rajesh = Example("KMU", "Bsc.cs")
