"""
Author : Ryan Downey <ryandowney64@yahoo.com>
Date   : 2022-09-27
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedWidth(680)
        self.setFixedHeight(1200)
        self.setStyleSheet("background: black;")
        self.setWindowTitle("Calculator")
        self.initUI()
        self.temp_numbers = []
        self.numbers = None
        self.previous_numbers = None
        self.printed_nums = ""
        self.old_printed_nums = ""
        self.decimal = False
        self.negative = False
        self.answer = None
        self.operator_pressed = None
        self.previous_operator_pressed = None
        self.equals_button_clicked = False
        self.operator_button_active = False
        self.percentage_pressed = False
        self.number_overwritten = False
        self.pressed_c_before_equation = False
        self.pressed_c_after_equation = False
        self.add_or_subtract_pressed = False

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
        self.ac_button.clicked.connect(self.clicked_ac_button)
        self.ac_button.setStyleSheet("""
            QPushButton
            {
            color: 'black';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid grey;
            background-color: grey;
            }"""
            """QPushButton:pressed
            {
            border: 2px solid white;
            background-color: white;
            }""")

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
        self.percentage_button.clicked.connect(self.clicked_percentage)
        self.percentage_button.setStyleSheet("""
            QPushButton
            {
            color: 'black';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid grey;
            background-color: grey;
            }"""
            """QPushButton:pressed
            {
            border: 2px solid white;
            background-color: white;
            }""")

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
        self.reset_operator_button_colour()
        self.resize_label(self.temp_numbers)
        self.ac_button.setText("C")
        self.pressed_c_before_equation = False

        if self.answer and self.equals_button_clicked and not self.operator_button_active and not self.pressed_c_after_equation:
            self.number_overwritten = True

        print(f"self.number_overwritten: {self.number_overwritten}")

        if self.percentage_pressed:
            self.percentage_pressed = False
            self.temp_numbers = []

        if len(self.temp_numbers) == 0 and button.text() == "0":
            return

        # each time number is clicked, add a new number to self.temp_numbers whilst the length of the number is below the max length of 9 digits
        if len(self.temp_numbers) < 9 and self.decimal == False:
            self.temp_numbers += button.text()         
        
        # handle the 9 digit number length when decimals are present
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
            self.printed_nums = "-" + self.printed_nums
            self.label.setText(self.printed_nums)
        else:
            self.label.setText(self.printed_nums)

        if self.pressed_c_after_equation and not self.answer:
            self.numbers = self.clean_printed_nums(self.printed_nums)
            self.answer = self.numbers
            self.printed_nums = self.old_printed_nums

        print("CLICKED NUM")
        print(f"self.temp_numbers: {self.temp_numbers}")
        print(f"self.numbers: {self.numbers}")
        print(f"self.printed_nums: {self.printed_nums}")
        print(f"self.answer: {self.answer}\n\n")

    def clicked_ac_button(self):
        # reset all variable if "AC" is clicked
        if self.ac_button.text() == "AC":
            self.reset_operator_button_colour()
            self.temp_numbers = []
            self.numbers = None
            self.previous_numbers = None
            self.printed_nums = ""
            self.old_printed_nums = ""
            self.decimal = False
            self.negative = False
            self.answer = None
            self.operator_pressed = None
            self.previous_operator_pressed = None
            self.equals_button_clicked = False
            self.operator_button_active = False
            self.percentage_pressed = False
            self.number_overwritten = False
            self.pressed_c_before_equation = False
            self.pressed_c_after_equation = False
            self.add_or_subtract_pressed = False
            self.resize_label("0")
            self.label.setText("0")
        # if "C" is clicked, change button text to "AC" 
        elif self.ac_button.text() == "C":
            self.ac_button.setText("AC")
            if self.numbers is None:
                # if a number hasn't been passed to self.numbers yet, clear screen and reset variables
                self.printed_nums = ""
                self.resize_label("0")
                self.label.setText("0")
                self.temp_numbers = []
                return
            self.temp_numbers = list(str(self.numbers))
            self.convert_float_to_printed_nums(self.numbers)
            self.temp_numbers = []
            # if no equation has been calculated, 
            if self.pressed_c_after_equation or self.answer is None:
                self.active_operator_button_colour()
                self.pressed_c_before_equation = True
                self.pressed_c_after_equation = False
            # if equation has been calculated, reset self.numbers to 0 but retain number previously used as operation number
            elif self.operator_button_active or not self.equals_button_clicked:
                self.reset_operator_button_colour()
                self.numbers = 0
                self.pressed_c_after_equation = True
            else:
                self.numbers = 0
                self.printed_nums = self.old_printed_nums
                self.pressed_c_after_equation = True
            self.resize_label("0")
            self.label.setText("0")
            self.answer = None

            print("CLICKED C")
            print(f"self.temp_numbers: {self.temp_numbers}")
            print(f"self.numbers: {self.numbers}")
            print(f"self.printed_nums: {self.printed_nums}")
            print(f"self.last_operator_pressed: {self.operator_pressed}")
            print(f"self.old_printed_nums: {self.old_printed_nums}")
            print(f"self.answer: {self.answer}\n\n")

    def clicked_decimal(self):
        # add a decimal point when clicked if there isn't already a decimal
        if "." not in self.temp_numbers:
            if len(self.temp_numbers) == 0:
                self.temp_numbers += "0"
            self.temp_numbers += "."
            self.decimal = True
            temp_numbers_with_commas = copy.deepcopy(self.temp_numbers[:-1])
            nums_with_commas = self.add_commas(temp_numbers_with_commas)
            self.printed_nums = "".join(nums_with_commas) + "."
            self.label.setText(self.printed_nums)

            print("CLICKED DECIMAL")
            print(f"self.temp_numbers: {self.temp_numbers}")
            print(f"self.numbers: {self.numbers}")
            print(f"self.printed_nums: {self.printed_nums}")
            print(f"self.answer: {self.answer}\n\n")

    def clicked_plus_minus(self):
        # if user presses plus/minus button before typing a second number following an operator button, display "-0" which will change to "-{user entered number}" once the user enters a number
        if self.operator_button_active == True:
            self.negative = True
            self.label.setText("-0")
            return
        # if number is already negative, make it positive
        if "-" in self.label.text():
            self.negative = False
            self.label.setText(self.label.text().replace("-", ""))
            if self.answer:
                self.answer = self.numbers = self.clean_printed_nums(self.label.text())
            else:
                self.printed_nums = self.label.text()
        else:
            # is number is positive, make it negative
            self.negative = True
            if len(self.temp_numbers) != 0 or self.answer:
                self.label.setText("-" + self.label.text())
            else:
                self.label.setText("-0")
            if self.answer:
                self.answer = self.numbers = -self.numbers
            else:
                self.printed_nums = self.label.text()

        print("CLICKED PLUS/MINUS")
        print(f"self.temp_numbers: {self.temp_numbers}")
        print(f"self.numbers: {self.numbers}")
        print(f"self.printed_nums: {self.printed_nums}")
        print(f"self.answer: {self.answer}\n\n")

    def clicked_percentage(self):
        self.percentage_pressed = True
        # if a sum has just been calculated, divide the answer of that sum by 100
        if self.equals_button_clicked and not self.operator_button_active:
            self.convert_float_to_printed_nums(self.answer / 100)
            self.resize_label(self.printed_nums)
            self.label.setText(self.printed_nums)
            self.numbers = self.clean_printed_nums(self.printed_nums)
            self.answer = self.numbers
            self.printed_nums = self.old_printed_nums

            print("CLICKED PERCENTAGE No1")
            print(f"self.temp_numbers: {self.temp_numbers}")
            print(f"self.numbers: {self.numbers}")
            print(f"self.printed_nums: {self.printed_nums}")
            print(f"self.answer: {self.answer}\n\n")

            return

        # return number if number is 0 as it can't be divided
        if self.printed_nums in ["", "0", "0.", "0.0"]:
            return
        float_nums = self.clean_printed_nums(self.printed_nums)
        # last button clicked was a number, divide this number by 100
        if (self.operator_button_active == False and (self.temp_numbers != [] and self.temp_numbers != ["0", "."])):
            if "e" in self.printed_nums:
                float_nums = float(self.printed_nums) / 100
            else:
                float_nums = float_nums / 100
            if (float_nums > 0 and (float_nums < 0.00000001 or float_nums > 999999999)) or (float_nums < 0 and (float_nums > -0.00000001 or float_nums < -999999999)):
                self.printed_nums = str("{:e}".format(float_nums))
            else:
                self.convert_float_to_printed_nums(float_nums)
                if "e" in self.printed_nums:
                    """as Python automatically converts numbers to scientific notation a lot sooner than this calculator should, convert any numbers in scientific notation that aren't outside 
                    the 9 digit number length when in normal notation back to a float"""
                    self.printed_nums = "{:.8f}".format(float(self.printed_nums))
                    # remove any trailing zero's
                    self.printed_nums = self.printed_nums.rstrip("0")
        # if the last button pressed was an operator button
        elif self.operator_button_active == True:
            if self.numbers:
                float_nums = self.numbers
            if self.operator_pressed == "divide" or self.operator_pressed == "multiply":
                float_nums = float_nums / 100
            if self.operator_pressed == "add" or self.operator_pressed == "subtract":
                if "e" in self.printed_nums:
                    float_nums = float(self.printed_nums) * (float(self.printed_nums) / 100)
                else:
                    float_nums = float_nums * (float_nums / 100)
            if (float_nums > 0 and (float_nums < 0.00000001 or float_nums > 999999999)) or (float_nums < 0 and (float_nums > -0.00000001 or float_nums < -999999999)):
                self.printed_nums = str("{:e}".format(float_nums))
            else:
                self.convert_float_to_printed_nums(float_nums)
                if "e" in self.printed_nums:
                    self.printed_nums = "{:.8f}".format(float(self.printed_nums))
                    # remove any trailing zero's
                    self.printed_nums = self.printed_nums.rstrip("0")
        self.resize_label(self.printed_nums)
        self.label.setText(self.printed_nums)

        print("CLICKED PERCENTAGE No2")
        print(f"self.temp_numbers: {self.temp_numbers}")
        print(f"self.numbers: {self.numbers}")
        print(f"self.printed_nums: {self.printed_nums}")
        print(f"self.answer: {self.answer}\n\n")

    def clicked_divide(self):
        if self.operator_pressed == "add" or self.operator_pressed == "subtract":
            self.previous_operator_pressed = self.operator_pressed
            self.previous_numbers = self.numbers
            self.numbers = self.clean_printed_nums(self.printed_nums)
            if self.answer:
                self.answer = self.numbers
        # calculate answer without having to click equals button after one of the operator buttons has been clicked atleast once
        if self.equals_button_clicked == False and self.operator_button_active == False and self.operator_pressed not in ["add", "subtract"]:
            self.calculate_answer()
        self.reset_operator_button_colour()
        self.operator_pressed = "divide"
        self.active_operator_button_colour()
        self.operator_button_active = True
        self.reset_temp_numbers()
        self.equals_button_clicked = False

    def clicked_multiply(self):
        if self.operator_pressed == "add" or self.operator_pressed == "subtract":
            self.previous_operator_pressed = self.operator_pressed
            self.previous_numbers = self.numbers
            self.numbers = self.clean_printed_nums(self.printed_nums)
            if self.answer:
                self.answer = self.numbers
        if self.equals_button_clicked == False and self.operator_button_active == False and self.operator_pressed not in ["add", "subtract"]:
            self.calculate_answer()
        self.reset_operator_button_colour()
        self.operator_pressed = "multiply"
        self.active_operator_button_colour()
        self.operator_button_active = True
        self.reset_temp_numbers()
        self.equals_button_clicked = False

    def clicked_minus(self):
        self.add_or_subtract_pressed = True
        if self.equals_button_clicked == False and self.operator_button_active == False:
            self.calculate_answer()
        self.reset_operator_button_colour()
        self.operator_pressed = "subtract"
        self.active_operator_button_colour()
        self.operator_button_active = True
        self.reset_temp_numbers()
        self.equals_button_clicked = False
        self.add_or_subtract_pressed = False

    def clicked_plus(self):
        self.add_or_subtract_pressed = True
        if self.equals_button_clicked == False and self.operator_button_active == False:
            self.calculate_answer()
        self.reset_operator_button_colour()
        self.operator_pressed = "add"
        self.active_operator_button_colour()
        self.operator_button_active = True
        self.reset_temp_numbers()
        self.equals_button_clicked = False
        self.add_or_subtract_pressed = False

    def clicked_equals(self):
        self.equals_button_clicked = True
        self.calculate_answer()

    def calculate_answer(self):
        # if no second number had been entered, don't carry out function
        if self.numbers is None:
            return

        self.reset_operator_button_colour()
        divide_answer = multiply_answer = addition_answer = subtraction_answer = None

        """if number has been overwritten, retrieve the number last used in the previous equation as the current operation number, therefore if 
        the number is overwritten but no new operator or operation number is clicked in, you can apply the previous operation to the new number
         - for instance if a new number is typed but the previous operation added 5 each time equals was clicked, then 5 would still be added to this
         newly overwritten number each time the equals button is clicked"""
        if self.number_overwritten:
            operation_number = self.clean_printed_nums(self.old_printed_nums)
            self.numbers = self.clean_printed_nums(self.printed_nums)
            self.number_overwritten = False
        else:
            self.old_printed_nums = self.printed_nums
            operation_number = self.clean_printed_nums(self.printed_nums)

        # handle if "C" button is pressed before any value is passed to self.answer
        if self.pressed_c_before_equation:
            self.numbers = 0

            print("CLICKED EQUALS AFTER C IS PRESSED WITH NO ANSWER TO EQUATION PASSED")
            print(f"self.temp_numbers: {self.temp_numbers}")
            print(f"self.numbers: {self.numbers}")
            print(f"self.printed_nums: {self.printed_nums}")
            print(f"self.answer: {self.answer}\n\n")

        # carry out operation depending on which operator was clicked
        if self.operator_pressed == "divide":
            divide_answer = self.numbers / operation_number
        elif self.operator_pressed == "multiply":
            multiply_answer = self.numbers * operation_number
        elif self.operator_pressed == "subtract":
            subtraction_answer = self.numbers - operation_number
        elif self.operator_pressed == "add":
            addition_answer = self.numbers + operation_number

        for answer in [divide_answer, multiply_answer, subtraction_answer, addition_answer]:
            # if not the correct operator, go to next iteration
            if answer is None:
                pass
            else:
                if (self.equals_button_clicked and self.previous_numbers) or (self.add_or_subtract_pressed and self.previous_numbers):

                    print(f"self.equals_button_clicked: {self.equals_button_clicked}")
                    print(f"self.previous numbers: {self.previous_numbers}")
                    print(f"self.operator_pressed: {self.operator_pressed}\n\n")

                    if self.previous_operator_pressed == "add":
                        answer = self.previous_numbers + answer
                    elif self.previous_operator_pressed == "subtract":
                        answer = self.previous_numbers - answer
                    self.previous_numbers = None
                    self.previous_operator_pressed = None
                    self.add_or_subtract_pressed = False
                if answer == 0.0:
                    self.printed_nums = "0"
                # if number is outside of the 9 digits boundary, convert the number to scientific notation
                elif (answer > 0 and (answer < 0.00000001 or answer > 999999999)) or (answer < 0 and (answer > -0.00000001 or answer < -999999999)):
                    self.printed_nums = str("{:e}".format(answer))
                    self.answer = float(self.printed_nums)
                else:
                    self.convert_float_to_printed_nums(answer)
                    self.answer = self.clean_printed_nums(self.printed_nums)
                    if "e" in self.printed_nums:
                        """as Python automatically converts numbers to scientific notation a lot sooner than this calculator should, convert any numbers in scientific notation that aren't outside 
                        the 9 digit number length when in normal notation back to a float"""
                        self.printed_nums = "{:.8f}".format(float(self.printed_nums))
                        # remove any trailing zero's
                        self.printed_nums = self.printed_nums.rstrip("0")
                # reset various variables once answer has been calculated and printed to the screen
                self.resize_label(self.printed_nums)
                self.label.setText(self.printed_nums)
                self.numbers = self.answer
                self.printed_nums = self.old_printed_nums
                self.temp_numbers = []
                self.negative = False
                self.operator_button_active = False
                if self.pressed_c_after_equation:
                    self.operator_pressed = None
                    self.pressed_c_after_equation = False

                print("CLICKED EQUALS")
                print(f"self.temp_numbers: {self.temp_numbers}")
                print(f"self.numbers: {self.numbers}")
                print(f"self.printed_nums: {self.printed_nums}")
                print(f"self.old_printed_nums: {self.old_printed_nums}")
                print(f"self.operator_pressed: {self.operator_pressed}")
                print(f"self.answer: {self.answer}\n\n")
    
    def reset_temp_numbers(self):
        # if user types over a number that's given as an answer to their previous equation, store the overwritten number in self.numbers to be used for the next equation
        if self.number_overwritten:
            self.numbers = self.clean_printed_nums(self.printed_nums)
            self.answer = self.numbers
            self.number_overwritten = False
        # if no equation has been solved yet but a second number has been entered after use of an operator for instance, store the first number in self.numbers so that it can be used in the equation
        if self.answer is None:
            if len(self.temp_numbers) > 0:
                self.numbers = self.clean_printed_nums(self.printed_nums)
            else:
                self.numbers = 0
        # reset variables used for next number typed
        self.temp_numbers = []
        self.decimal = False
        self.negative = False

        print("RESET TEMP NUMBERS")
        print(f"self.temp_numbers: {self.temp_numbers}")
        print(f"self.numbers: {self.numbers}")
        print(f"self.operator pressed: {self.operator_pressed}")
        print(f"self.printed_nums: {self.printed_nums}")
        print(f"self.answer: {self.answer}\n\n")

    def convert_float_to_printed_nums(self, float_nums):

        print("CONVERT FLOAT TO PRINTED NUMS")
        print(f"float_nums: {float_nums}\n\n")

        if (float_nums > 0 and (float_nums < 0.00000001 or float_nums > 999999999)) or (float_nums < 0 and (float_nums > -0.00000001 or float_nums < -999999999)):
            self.printed_nums = "{:e}".format(float_nums)
            return
        elif "e" in str(float_nums):
            self.printed_nums = "{:e}".format(float_nums)
            return
        else:
            float_nums = "{:.8f}".format(float_nums)

        print(f"float nums after conversion: {float_nums}\n\n")

        nums_before_rounding, _ = self.split_decimal_num(list(float_nums))
        if "-" in nums_before_rounding:
            # remove minus element so that it's not included in the length of the list figure used to round float_nums
            nums_before_rounding.remove("-")
        # split the number once it's been rounded so that there's a maximum of 9 digits present in the number  
        nums, decimals = self.split_decimal_num(list(str(round(float(float_nums), (9 - len(nums_before_rounding))))))
        # if no decimal number is present, just add commas to the number converted into a string, otherwise join with the string of the decimal number
        if len(decimals) == 0 or "".join(decimals) == "0":
            self.printed_nums = "".join(self.add_commas(nums))
        else:
            self.printed_nums = "".join(self.add_commas(nums)) + "." + "".join(decimals)

    def clean_printed_nums(self, nums):
        # if string shows number in scientific notation, keep the same
        if "e" in nums:

            print("CLEAN PRINTED NUMS")
            print(f"float(nums): {float(nums)}\n\n")

            return float(nums)
        # remove all added commas so that the number can be converted into float
        amended_nums = nums.replace(",", "")
        # if the string represents a negative number, convert it to a negative float
        if "-" in nums[0]:
            return -float(amended_nums.replace("-", ""))
        else:
            return float(amended_nums)

    def split_decimal_num(self, num):
        # split number into two lists based on the index of the decimal if it exists
        if "." in num:
            decimal_index = num.index(".")
            nums = num[:decimal_index]
            decimals = num[decimal_index + 1:]
        else:
            nums = num
            decimals = ["0"]
        return nums, decimals  

    def add_commas(self, nums):
        minus = False
        # if number is in scientific notation, don't add commas
        if "e" in nums:
            return nums
        if "-" in nums:
            minus = True
            nums.remove("-")
        # add comma 4 elements from the end of the list
        if len(nums) > 3 and nums.count(",") == 0:
            nums.insert(len(nums) - 3, ",")
        # if comma already exists but list had grown, get the index of the initial comma, remove said comma and replace with new comma at 4th element from the end of the list
        elif len(nums) > 3 and nums.count(",") > 0:
            index_pos_first = nums.index(",", (len(nums) - 5))
            first_comma = nums.pop(index_pos_first)
            nums.insert(len(nums) - 3, first_comma)
        # add second comma 8 elements from the end of the list if length of numbers above 7 
        if len(nums) > 7 and nums.count(",") == 1:
            nums.insert(len(nums) - 7, ",")
        # if second comma already exists but list had grown, get the index of the second comma, remove said comma and replace with new comma at 8th element from the end of the list
        elif len(nums) > 7 and nums.count(",") > 1:
            index_pos_second = nums.index(",", 0, (len(nums) - 6))
            second_comma = nums.pop(index_pos_second)
            nums.insert(len(nums) - 7, second_comma)
        if minus:
            nums = ["-"] + nums
        return nums

    def resize_label(self, nums):
        # resize the labels font size based on the number of characters present
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
        # change operator button colour to show that the operator is now active
        if self.operator_pressed == "divide":
            self.divide_button.setStyleSheet("""
            color: 'orange';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            """)
        elif self.operator_pressed == "multiply":
            self.multiply_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)
        elif self.operator_pressed == "subtract":
            self.minus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)
        elif self.operator_pressed == "add":
            self.plus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid white;
            background-color: white;
            color: 'orange';
            """)

    def reset_operator_button_colour(self):
        # return operator button colour to default to show that the operator is no longer active
        self.operator_button_active = False

        if self.operator_pressed == "divide":
            self.divide_button.setStyleSheet("""
            color: 'white';
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            """)
        elif self.operator_pressed == "multiply":
            self.multiply_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)
        elif self.operator_pressed == "subtract":
            self.minus_button.setStyleSheet("""
            font-size: 50px;
            border-radius: 60;
            border: 2px solid orange;
            background-color: orange;
            color: 'white';
            """)
        elif self.operator_pressed == "add":
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
    sys.exit(app.exec())