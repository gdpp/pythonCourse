def be_nice(fn):
    def inner():
        print("Nice to meet you!")
        fn()
        print("Have a nice day!")
        
    return inner

@be_nice
def complex_business_logic():
    print("something complex")
    
    
# result = be_nice(complex_business_logic)
# result()

complex_business_logic()