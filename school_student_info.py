'''class student:
    def __init__(self, name, course):
        self.course=tuple(course)
        self.name=tuple(name)
    def students(num):
        for i in range(num):
            #x=input("Enter the name of the student: ")'''
listnames=list()
listcourses=list()
class Students:
    info=dict()
    def __init__(self,num):
        self.num=num
        for i in range(num):
            name=input("Enter the name: ")
            listnames.append(name)
            course=input("Enter the Date of joining: ")
            listcourses.append(course)
            info=dict(zip(listnames,listcourses))
        print(info)
        print("END")
            
            
            
