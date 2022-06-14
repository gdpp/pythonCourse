class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0
        
    def get_os_version(self):
        return self._firmware
    
    def update_os_version(self):
        print("Reaching out to the server for the next version")
        self.firmware += 1

iphone = SmartPhone()

print(iphone._company)
print(iphone._firmware)