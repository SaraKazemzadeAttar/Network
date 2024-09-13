from threading import Lock

# چون که هر کامپیوتر و مسیریاب در سه ویژگی داشتن اسم و ذوشن و خاموش شدن مشترکند از ارث بری استفاده می کنیم
# Device = کلاس مادر / Computer , Router = فرزند
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = True
        self.lock = Lock()

    def turn_on(self):
        with self.lock:
            self.is_on = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        with self.lock:
            self.is_on = False
            print(f"{self.name} is now OFF.")    



class Computer :
    
    
    
    
    
class Router :
    
    
    
    
    
    
class Wire:  # سیم‌ها ارتباط بین مسیریاب‌ها و کامپیوتر‌ها با یک دیگر را مشخص میکنن
    def __init__(self, device1, device2):
            self.device1 = device1
        self.device2 = device2

    def connects(self, device):
        return device in [self.device1, self.device2]
    
    
# هر کامپیوتر میتواند بسته‌ای را به کامپیوتر دیگری ارسال کند که این بسته از مسیریاب‌های مختلف عبور کرده و به کامپیوتر مقصد میرسد.
class Packet: 
    def __init__(self, source, destination, data): # روی هر بسته باید مبدا، مقصد، دیتا، مسیر و یک آیدی مشخص داشته باشد
        self.packet_id = id(self)
        self.source = source
        self.destination = destination
        self.data = data
        self.path = []

    def set_path(self, path):
        self.path = path
    
    