# Implementing Student Class
class Students:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.courses_list=[] # [ [101,Math,Marks], [102,Eng,Marks] ]
        self.grade=None

class Courses:
    def __init__(self,course_code,course_name):
        self.course_code=course_code
        self.course_name=course_name
        self.course_students=[]


class School:
    def __init__(self):
        self.students=[]    # contains instances of 'Students' class
        self.courses=[]    # contains instances of 'Courses' class
        self.course_students={} # to get list of students enrolled in a particular course
        self.ch=False       # to use if/else statements

    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            self.course_students[course.course_code]=[]
            print(f"'{course.course_name}' course added successfully.")
        else:
            print("Course already exists")


    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student '{student.name}' added successfully.")
        else:
            print("Student already exists.")

    def enroll_in_course(self,student,course):
        if student in self.students:
            if course in self.courses:
                student.courses_list.append([course.course_code,course.course_name])
                self.course_students[course.course_code].append(student.name)
            else:
                print("No such course exists.")
                return
        else:
            print("No such student exists.")

    def update_marks(self,student,course_code,marks):
        if student in self.students:
            for sub in student.courses_list:
                if sub[0]==course_code:
                    self.ch=True
                    sub.append(marks)
            if self.ch:
                print(f"Marks Updated of {student.name} for the course code :{course_code}")
            else:
                print("Student is not enrolled in the mentioned subject code.")
        else:
            print("No such student exists, please add student first")


    def course_details(self):
        print("\n---COURSE details with the students enrolled in it, are as follow---\n")
        for cou in self.course_students:
            print("code : ",cou, " students: ",self.course_students[cou])
        
    def student_details(self):
        print("\n---Detail of all the students with the courses enrolled in---\n")
        for index,stu in enumerate(self.students):
            print("Student ID: ",stu.id)
            print("Stdent Name: ",stu.name)
            print("Courses enrolled in: ")
            for sub in stu.courses_list:
                print(sub[1]," ",end='')
            print()
            print()

    def print_marks_of_student(self,student):
        if student in self.students:
            print(f"\n{student.name}'s marks are as follow : ")
            for nl in student.courses_list:
                    print(f"{nl[1]} : {nl[2]}")
        else:
            print("Students data is not in the database.")

    def result_of_student(self,student):
        if student in self.students:
            print(f"\n\n--**--RESULT of the 'Mr.{student.name}'--**--\n")
            self.print_marks_of_student(student)
            self.marks_list = [nl[2] for nl in student.courses_list]
            self.avg = sum(self.marks_list) / len(self.marks_list)
            print(f"Average Marks : {self.avg}")
            if 90<=self.avg and self.avg<100:
                print("Grade : A+")
            elif 80<=self.avg and self.avg<90:
                print("Grade : A")
            elif 70<=self.avg and self.avg<80:
                print("Grade : B")
            elif 60<=self.avg and self.avg<70:
                print("Grade : C")
            elif 50<=self.avg and self.avg<60:
                print("Grade : D")
            elif 10<self.avg and self.avg<50:
                print("Grade : E")





# Creating instance of the class school to operate
school = School()


# Creating Courses
c1=Courses(101,"Mathematics")
c2=Courses(102,"English")
c3=Courses(103,"Computer_Science")
c4=Courses(104,"Hindi")
c5=Courses(105,"Social_Science")

print()

# Adding courses to the db
school.add_course(c1)
school.add_course(c2)
school.add_course(c3)
school.add_course(c4)
school.add_course(c5)


# Creating Students
s1=Students(90010,"Avinash")
s2=Students(90020,"Devendra")

# Adding students in db
school.add_student(s1)
school.add_student(s2)

# Enrolling student in Courses
school.enroll_in_course(s1,c1)
school.enroll_in_course(s1,c2)
school.enroll_in_course(s1,c3)
school.enroll_in_course(s1,c4)

school.enroll_in_course(s2,c4)
school.enroll_in_course(s2,c5)


# Updating Marks for student 1
school.update_marks(s1,101,70)
school.update_marks(s1,102,80)
school.update_marks(s1,103,90)
school.update_marks(s1,104,60)
# Updating Marks for student 2
school.update_marks(s2,104,50)
school.update_marks(s2,105,75)

# Printing Course Details       # Prints course code and students enrolled in it.
school.course_details()

# Printing Student Details
school.student_details()        # Prints name,id and subjects enrolle in 

# Printing Marks of Student 
# school.print_marks_of_student(s1)

# Printing result of student1
school.result_of_student(s1)

# Printing result of student2
school.result_of_student(s2)






