import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 50, 680, 1200)
        self.setStyleSheet("background: black;")
        self.setWindowTitle("Calculator")
        self.initUI()
        self.temp_numbers = []
        self.numbers = None
        self.printed_nums = ""
        self.decimal = False
        self.negative = False
        self.operator_pressed = False
        self.last_operator_pressed = None

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setGeometry(50, 250, 580, 150)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet("""
            color: 'white';
            font-size: 120px;
            """)

        self.ac_button = QPushButton(self)
        self.ac_button.setText("AC")
        self.ac_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ac_button.setGeometry(50, 400, 120, 120)
        self.ac_button.setStyleSheet("""
            color: 'black';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid grey;
            background-color: grey;
            """)

        self.plus_minus_button = QPushButton(self)
        self.plus_minus_button.setText("+/–")
        self.plus_minus_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus_minus_button.setGeometry(200, 400, 120, 120)
        self.plus_minus_button.clicked.connect(self.clicked_plus_minus)
        self.plus_minus_button.setStyleSheet("""
            QPushButton
            {
            color: 'black';
            font-size: 40px;
            border-radius: 60;
            border: 2px solid grey;
            background-color: grey;
            }"""
            """QPushButton:pressed
            {
            border: 2px solid white;
            background-color: white;
            }""")

        self.percentage_button = QPushButton(self)
        self.percentage_button.setText("%")
        self.percentage_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.percentage_button.setGeometry(350, 400, 120, 120)
        self.percentage_button.setStyleSheet("""
            color: 'black';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid grey;
            background-color: grey;
            """)

        self.divide_button = QPushButton(self)
        self.divide_button.setText("÷")
        self.divide_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.divide_button.setGeometry(500, 400, 120, 120)
        self.divide_button.clicked.connect(self.clicked_divide)
        self.divide_button.setStyleSheet("""
            color: 'white';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            """)
        
        self.seven_button = QPushButton(self)
        self.seven_button.setText("7")
        self.seven_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.seven_button.setGeometry(50, 550, 120, 120)
        self.seven_button.clicked.connect(self.clicked_num)
        self.seven_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")


        self.eight_button = QPushButton(self)
        self.eight_button.setText("8")
        self.eight_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.eight_button.setGeometry(200, 550, 120, 120)
        self.eight_button.clicked.connect(self.clicked_num)
        self.eight_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.nine_button = QPushButton(self)
        self.nine_button.setText("9")
        self.nine_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.nine_button.setGeometry(350, 550, 120, 120)
        self.nine_button.clicked.connect(self.clicked_num)
        self.nine_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")
        
        self.multiply_button = QPushButton(self)
        self.multiply_button.setText("×")
        self.multiply_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.multiply_button.setGeometry(500, 550, 120, 120)
        self.multiply_button.clicked.connect(self.clicked_multiply)
        self.multiply_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)

        self.four_button = QPushButton(self)
        self.four_button.setText("4")
        self.four_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.four_button.setGeometry(50, 700, 120, 120)
        self.four_button.clicked.connect(self.clicked_num)
        self.four_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.five_button = QPushButton(self)
        self.five_button.setText("5")
        self.five_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.five_button.setGeometry(200, 700, 120, 120)
        self.five_button.clicked.connect(self.clicked_num)
        self.five_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.six_button = QPushButton(self)
        self.six_button.setText("6")
        self.six_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.six_button.setGeometry(350, 700, 120, 120)
        self.six_button.clicked.connect(self.clicked_num)
        self.six_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")
        
        self.minus_button = QPushButton(self)
        self.minus_button.setText("–")
        self.minus_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minus_button.setGeometry(500, 700, 120, 120)
        self.minus_button.clicked.connect(self.clicked_minus)
        self.minus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)

        self.one_button = QPushButton(self)
        self.one_button.setText("1")
        self.one_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_button.setGeometry(50, 850, 120, 120)
        self.one_button.clicked.connect(self.clicked_num)
        self.one_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.two_button = QPushButton(self)
        self.two_button.setText("2")
        self.two_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.two_button.setGeometry(200, 850, 120, 120)
        self.two_button.clicked.connect(self.clicked_num)
        self.two_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.three_button = QPushButton(self)
        self.three_button.setText("3")
        self.three_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.three_button.setGeometry(350, 850, 120, 120)
        self.three_button.clicked.connect(self.clicked_num)
        self.three_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")
        
        self.plus_button = QPushButton(self)
        self.plus_button.setText("+")
        self.plus_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus_button.setGeometry(500, 850, 120, 120)
        self.plus_button.clicked.connect(self.clicked_plus)
        self.plus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)

        self.zero_button = QPushButton(self)
        self.zero_button.setText("0")
        self.zero_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.zero_button.setGeometry(50, 1000, 270, 120)
        self.zero_button.clicked.connect(self.clicked_num)
        self.zero_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")

        self.decimal_button = QPushButton(self)
        self.decimal_button.setText(".")
        self.decimal_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decimal_button.setGeometry(350, 1000, 120, 120)
        self.decimal_button.clicked.connect(self.clicked_decimal)
        self.decimal_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid #6B695E;
            background-color: #6B695E;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid #a7a69d;
            background-color: #a7a69d;
            }""")
        
        self.equals_button = QPushButton(self)
        self.equals_button.setText("=")
        self.equals_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.equals_button.setGeometry(500, 1000, 120, 120)
        self.equals_button.clicked.connect(self.clicked_equals)
        self.equals_button.setStyleSheet("""
            QPushButton
            {
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            }"""
            """QPushButton:pressed
            {
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            }""")

    def clicked_num(self):
        button = self.sender()    

        if self.operator_pressed:
            self.numbers = float(self.printed_nums.replace(",", ""))
            self.temp_numbers = []
            self.reset_operator_button_colour()
            self.operator_pressed = False
            self.decimal = False

        if len(self.temp_numbers) == 0 and button.text() == "0":
            return None

        self.resize_label(self.temp_numbers)

        if len(self.temp_numbers) < 9 and self.decimal == False:
            self.temp_numbers += button.text()         
        
        if self.decimal:
            nums, decimals = self.split_decimal_num(self.temp_numbers)
            if len(nums) + len(decimals) < 9:
                self.temp_numbers += button.text()
                decimals += button.text()                
            nums_with_commas = self.add_commas(nums)
            self.printed_nums = "".join(nums_with_commas) + "." + "".join(decimals)
        else:
            temp_numbers_with_commas = copy.deepcopy(self.temp_numbers)
            nums_with_commas = self.add_commas(temp_numbers_with_commas)
            self.printed_nums = "".join(nums_with_commas)
        
        if self.negative:
            self.label.setText("–" + self.printed_nums)
        else:
            self.label.setText(self.printed_nums)

    def clicked_decimal(self):
        if "." not in self.temp_numbers:
            if len(self.temp_numbers) == 0:
                self.temp_numbers += "0"
            self.temp_numbers += "."
            self.decimal = True
            temp_numbers_with_commas = copy.deepcopy(self.temp_numbers[:-1])
            nums_with_commas = self.add_commas(temp_numbers_with_commas)
            self.printed_nums = "".join(nums_with_commas) + "."
            self.label.setText(self.printed_nums)

    def clicked_plus_minus(self):
        if not self.negative:
            self.negative = True
            if len(self.printed_nums) > 0:
                self.label.setText("–" + self.printed_nums)
            else:
                self.label.setText("–0")
        else:
            self.negative = False
            if len(self.printed_nums) > 0:
                self.label.setText(self.printed_nums)
            else:
                self.label.setText("0")

    def clicked_divide(self):
        self.operator_pressed = True
        if self.last_operator_pressed:
            self.clicked_equals()
        self.last_operator_pressed = "divide"
        self.active_operator_button_colour()

    def clicked_multiply(self):
        self.operator_pressed = True
        if self.last_operator_pressed:
            self.clicked_equals()
        self.last_operator_pressed = "multiply"
        self.active_operator_button_colour()

    def clicked_minus(self):
        self.operator_pressed = True
        if self.last_operator_pressed:
            self.clicked_equals()
        self.last_operator_pressed = "subtract"
        self.active_operator_button_colour()

    def clicked_plus(self):
        self.operator_pressed = True
        if self.last_operator_pressed:
            self.clicked_equals()
        self.last_operator_pressed = "add"
        self.active_operator_button_colour()

    def clicked_equals(self):
        if not self.numbers:
            return None

        self.reset_operator_button_colour()

        divide_answer = multiply_answer = addition_answer = subtraction_answer = False

        if self.last_operator_pressed == "divide":
            divide_answer = self.numbers / float("".join(self.temp_numbers))
        elif self.last_operator_pressed == "multiply":
            multiply_answer = self.numbers * float("".join(self.temp_numbers))
        elif self.last_operator_pressed == "subtract":
            subtraction_answer = self.numbers - float("".join(self.temp_numbers))
        elif self.last_operator_pressed == "add":
            addition_answer = self.numbers + float("".join(self.temp_numbers))

        for answer in [divide_answer, multiply_answer, subtraction_answer, addition_answer]:
            if answer != False:
                if answer < 0.00000001 or answer > 999999999:
                    self.printed_nums = str("{:e}".format(answer))
                else:
                    nums_before_rounding, _ = self.split_decimal_num(list(str(answer)))
                    nums, decimals = self.split_decimal_num(list(str(round(answer, (9 - len(nums_before_rounding))))))
                    if len(decimals) == 0 or "".join(decimals) == "0":
                        self.printed_nums = "".join(self.add_commas(nums))
                    else:
                        self.printed_nums = "".join(self.add_commas(nums)) + "." + "".join(decimals)
                self.resize_label(self.printed_nums)
                self.label.setText(self.printed_nums)
                self.last_operator_pressed = False

    def split_decimal_num(self, num):
        decimal_index = num.index(".")
        nums = num[:decimal_index]
        decimals = num[decimal_index + 1:]
        return nums, decimals  

    def add_commas(self, nums):
        if len(nums) > 3 and nums.count(",") == 0:
            nums.insert(len(nums) - 3, ",")
        elif len(nums) > 3 and nums.count(",") > 0:
            index_pos_first = nums.index(",", (len(nums) - 5))
            first_comma = nums.pop(index_pos_first)
            nums.insert(len(nums) - 3, first_comma)
        if len(nums) > 7 and nums.count(",") == 1:
            nums.insert(len(nums) - 7, ",")
        elif len(nums) > 7 and nums.count(",") > 1:
            index_pos_second = nums.index(",", 0, (len(nums) - 6))
            second_comma = nums.pop(index_pos_second)
            nums.insert(len(nums) - 7, second_comma)
        return nums

    def resize_label(self, nums):
        if len(nums) < 5:
            self.label.setStyleSheet("""
            font-size: 120px;
            color: 'white';
            """)
        if len(nums) > 5:
            self.label.setStyleSheet("""
            font-size: 110px;
            color: 'white';
            """)
        if len(nums) > 6:
            self.label.setStyleSheet("""
            font-size: 100px;
            color: 'white';
            """)
        if len(nums) > 7:
            self.label.setStyleSheet("""
            font-size: 90px;
            color: 'white';
            """)
        if len(nums) > 10:
            self.label.setStyleSheet("""
            font-size: 80px;
            color: 'white';
            """)    

    def active_operator_button_colour(self):
        if self.last_operator_pressed == "divide":
            self.divide_button.setStyleSheet("""
            color: 'orange';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            """)
        elif self.last_operator_pressed == "multiply":
            self.multiply_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)
        elif self.last_operator_pressed == "subtract":
            self.minus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)
        elif self.last_operator_pressed == "add":
            self.plus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)

    def reset_operator_button_colour(self):
        if self.last_operator_pressed == "divide":
            self.divide_button.setStyleSheet("""
            color: 'white';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            """)
        elif self.last_operator_pressed == "multiply":
            self.multiply_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)
        elif self.last_operator_pressed == "subtract":
            self.minus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)
        elif self.last_operator_pressed == "add":
            self.plus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    print(window.temp_numbers)
    sys.exit(app.exec())