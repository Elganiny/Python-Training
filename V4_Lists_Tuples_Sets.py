Courses_1 = ['History', 'Math','Physics', 'Computer Science']
Courses = Courses_1
print(Courses[-1]) #last item
print(Courses)
print(Courses[0:2])
print(Courses[:2])
print(Courses[2:])

Courses.append('Art')
print(Courses)

Courses.insert(0,'Programming')
print(Courses)

Courses_2 = []
#Courses.extend()