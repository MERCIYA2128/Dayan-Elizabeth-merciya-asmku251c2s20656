***
implement a function sort_student that take a lost of students object as and sorts the 
list used on their CGPA(complative grade point average)in dis ending order each student object
has the following attributes name(string),roll number (string), and cgpa(float),tect the function 
with fiffrent input list of students
***

class student:
  
  del__init__(self,name,roll,cgpa):
  self,name=Name
  self.roll_number=roll_number
  self.cgpa=cgpa
  
  
def sort_student(student_list):
  #sort the list of students in descending order of CGPA
  sorted _student=sorted (student_list,
key=lambdastudents;students cgpa,
reverse=True)
return sorted_students


#example usage:
student=[
  student("hard","A123",7.8)
  student("srikant","A124",8.9)
  student("sowmiya","A125",9.1)
  student("mahthar","A126",9.9)
  ]

sorted_student=sort_student(student)

#print the sorted list of student
for_student in sorted_student:
  print("name:{},roll number:{},CGPA:{}",format(student.name,

                                                student.roll_number,
                                                