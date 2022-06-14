class Teacher():
    def teacher_class(self):
        print("Teaching stuff!")
        
    def grab_lunch(self):
        print("Yum yum yum")
        
    def grade_test(self):
        print("F! F! F!")
        
class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray, I'm an author")
        
    def grade_tests(self):
        print("A! A! A!")
        
t = Teacher()
p = CollegeProfessor()

t.teacher_class()
t.grab_lunch()
t.grade_test()

p.publish_book()
p.teacher_class()
p.grab_lunch()
p.grade_tests()