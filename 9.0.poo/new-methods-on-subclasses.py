class Employee():
    def do_work(self):
        print("I'm working!")
            
class Manager(Employee):
    def waste_time(self):
        print("Wow, this youtube video looks fun!")
        
class Director(Manager):
    def fire_employee(self):
        print("You're fired!")

e = Employee()
m = Manager()
d = Director()

e.do_work()
m.do_work()
m.waste_time()
d.do_work()
d.waste_time()
d.fire_employee()