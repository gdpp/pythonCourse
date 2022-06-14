class Nonsense():
    def __init__(self):
        self.__some_attr = "Hello"
        
    def __some_method(self):
        print("SOME METHOD")
        

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

# print(n.some_attr)
# print(sn.some_attr)
print(n._Nonsense__some_attr)
print(sn._Nonsense__some_attr)