# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Office_automation:
    def __init__(self, model, serial_number):
        self.model = model
        self.serial_number = serial_number

    @staticmethod
    def mode(mode=0):
        if mode == 0:
            print('Turned off')
        elif mode == 1:
            print('Turned on')
        else:
            print('Incorrect mode')

    def information(self):
        return f'Model: {self.model}'

    def information2(self):
        return f'Serial number: {self.serial_number}'


class Printer(Office_automation):
    @staticmethod
    def to_print(colour):
        if colour == 1:
            print('Item was printed with black and white color')
        elif colour == 2:
            print('Item was printed with color')
        elif colour == 3:
            print('Item printed as high quality needed for photos')
        else:
            print('Wrong input')


class Scanner(Office_automation):
    def __init__(self, model, serial_number,max_res_height,max_res_width):
        # res_height and res_width are maximum resolution signs of that scanner
        self.model = model
        self.serial_number = serial_number
        self.max_res_height = max_res_height
        self.max_res_width = max_res_width

    def to_scan(self, res_height, res_width, mode):
        if 100 < res_height <= self.max_res_height and 100 < res_width <= self.max_res_width:
            if mode == 1:
                print(f'Black and white scan with resolution {res_height}x{res_width}')
            elif mode ==2:
                print(f'Colour scan with resolution {res_height}x{res_width}')
            else:
                print('Wrong mode')
        else:
            print('Incorrect resolution. You can scan higher than 100 dpi and lower than max resolution')

# FOR TESTING
#Office_automation.mode(1)
#Office_automation.mode()
#ffice_automation.mode('s')
#Printer('Xerox a25','a123-1').information()
#Printer.to_print(2)
#Scanner('Canon','p42',1100,1200).to_scan(1000,1300,1)



