import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QGridLayout, QWidget, QDesktopWidget, \
    QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sympy as sy
import math

stack = []

num_and_op = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']
tri_op = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt']


class Calculator(QMainWindow):

    def __init__(self):

        super().__init__()  # 调用父类的初始化方法
        # 初始化界面
        self.result_display = QLineEdit(self)
        self.result_display1 = QLineEdit(self)
        self.initUI()

    def initUI(self):

        # 设置窗口标题和大小
        self.setWindowTitle('简易计算器')
        self.setGeometry(300, 300, 420, 420)
        self.setWindowIcon(QIcon('calpic.png'))
        self.center()
        self.setObjectName('QMain')
        # 创建显示结果的文本框

        self.result_display.setReadOnly(True)  # 设置为只读
        self.result_display.move(10, 10)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.resize(400, 40)

        self.result_display1.setReadOnly(True)  # 设置为只读
        self.result_display1.move(10, 50)
        self.result_display1.setAlignment(Qt.AlignRight)
        self.result_display1.resize(400, 40)

        # 创建按钮并设置信号槽

        self.create_buttons()

        # 显示窗口

        self.show()

    def center(self):
        fw = self.frameGeometry()  # 获得主窗口的框架
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕分辨率的中点
        fw.moveCenter(cp)
        self.move(fw.topLeft())

    def create_buttons(self):

        # 创建数字按钮

        self.num_buttons = []

        for i in range(10):
            button = QPushButton(str(i), self)

            button.clicked.connect(self.on_number_click)

            self.num_buttons.append(button)
            self.setStyleSheet(
                "#QMain{background-color:rgb(253,253,253)}"
                "QPushButton{width:100%;height:100%;font-size:20px;font-family:KaiTi;border:none}"
                "QPushButton:hover{background-color:rgb(244,244,244);border-top:2px solid rgb(141,141,141);border-left:3px solid rgb(141,141,141);}"
                "QLineEdit{border:none;font-size:20px;font-family:KaiTi}"
                "#QMainWindow:{background-color:white}"

            )

        # 创建运算符按钮

        self.add_button = QPushButton('+', self)

        self.add_button.clicked.connect(self.on_operator_click)

        self.subtract_button = QPushButton('-', self)

        self.subtract_button.clicked.connect(self.on_operator_click)

        self.multiply_button = QPushButton('*', self)

        self.multiply_button.clicked.connect(self.on_operator_click)

        self.divide_button = QPushButton('/', self)

        self.divide_button.clicked.connect(self.on_operator_click)

        # 创建清除按钮

        self.clear_button = QPushButton('C', self)

        self.clear_button.clicked.connect(self.on_clear_click)

        # 创建小数点按钮

        self.point_button = QPushButton('.', self)

        self.point_button.clicked.connect(self.on_number_click)

        # 创建左括号按钮

        self.left_bracket_button = QPushButton('(', self)

        self.left_bracket_button.clicked.connect(self.on_number_click)

        # 创建右括号按钮

        self.right_bracket_button = QPushButton(')', self)

        self.right_bracket_button.clicked.connect(self.on_number_click)

        # 创建等号按钮

        self.equal_button = QPushButton('=', self)

        self.equal_button.clicked.connect(self.on_equal_click)

        # sin按钮
        self.sin_button = QPushButton('sin', self)

        self.sin_button.clicked.connect(self.on_tri_click)

        # sqrt按钮
        self.sqrt_button = QPushButton('sqrt', self)

        self.sqrt_button.clicked.connect(self.on_tri_click)

        # cos button
        self.cos_button = QPushButton('cos', self)
        self.cos_button.clicked.connect(self.on_tri_click)

        # cos button
        self.tan_button = QPushButton('tan', self)
        self.tan_button.clicked.connect(self.on_tri_click)

        # cos button
        self.asin_button = QPushButton('asin', self)
        self.asin_button.clicked.connect(self.on_tri_click)

        # cos button
        self.acos_button = QPushButton('acos', self)
        self.acos_button.clicked.connect(self.on_tri_click)

        # cos button
        self.atan_button = QPushButton('atan', self)
        self.atan_button.clicked.connect(self.on_tri_click)

        # 创建sqrt按钮
        self.pow_button = QPushButton('^', self)
        self.pow_button.clicked.connect(self.on_number_click)

        # 创建back按钮
        self.back_button = QPushButton('back', self)
        self.back_button.clicked.connect(self.on_back_click)

        # 使用网格布局排列按钮

        grid = QGridLayout()

        grid.setSpacing(0)

        positions = [(i, j) for i in range(7) for j in range(4)]
        print(type(self.num_buttons[7:9]))
        for pos, button in zip(positions, [self.cos_button, self.sin_button,
                                           self.tan_button, self.asin_button,
                                           self.acos_button,
                                           self.atan_button,
                                           self.left_bracket_button,
                                           self.right_bracket_button] + self.num_buttons[7:10] + [
                                              self.back_button] + self.num_buttons[4:7] + [
                                              self.clear_button] + self.num_buttons[1:4] + [self.add_button,
                                                                                            self.sqrt_button,
                                                                                            self.num_buttons[0],
                                                                                            self.point_button,
                                                                                            self.subtract_button] + [
                                              self.pow_button,
                                              self.multiply_button,
                                              self.divide_button,
                                              self.equal_button]):
            grid.addWidget(button, *pos)

        central_widget = QWidget(self)

        central_widget.setLayout(grid)

        central_widget.move(10, 100)

        central_widget.resize(400, 300)

    def on_tri_click(self):

        button = self.sender()
        self.result_display.setText(self.result_display.text() + button.text() + '(')

    def on_number_click(self):

        # 数字按钮点击事件处理
        button = self.sender()
        self.result_display.setText(self.result_display.text() + button.text())

    def on_operator_click(self):

        # 运算符按钮点击事件处理

        button = self.sender()

        self.result_display.setText(self.result_display.text() + button.text())

    def on_clear_click(self):

        # 清除按钮点击事件处理

        self.result_display.clear()

    def on_back_click(self):
        content = self.result_display.text()
        if content == '':
            return
        if content[len(content) - 1] == '(' and len(content) >= 5 and content[len(content) - 5] not in num_and_op:
            content = content[:len(content) - 5]
        elif content[len(content) - 1] == '(' and content[len(content) - 2] not in num_and_op:
            content = content[:len(content) - 4]
        else:
            content = content[:len(content) - 1]
        self.result_display.setText(content)


    def on_equal_click(self):

        # 等号按钮点击事件处理

        try:
            cal = self.result_display.text()

            result = self.calt_final(cal)

            self.result_display1.setText(str(result))

        except:

            self.result_display1.setText('错误')
    def calt_final(self, the_cal):
        final_cal = ''
        flag = 0
        i = 0
        flag1 = 0
        flag2 = 0
        while True:
            if the_cal[i] not in num_and_op:
                if the_cal[i] == '^':
                    p = 0
                    k = i
                    the_new = ''
                    while True:
                        k -= 1
                        if k == -1 or the_cal[k].isdigit() == False:
                            break
                        else:
                            the_new = the_cal[k] + the_new
                    p = k + 1
                    k = i
                    the_new1 = ''
                    while True:
                        k += 1
                        if k == len(the_cal) or the_cal[k].isdigit() == False:
                            break
                        else:
                            the_new1 = the_cal[k] + the_new1
                    t = pow(float(the_new), float(the_new1))
                    t = str(t)
                    final_cal += the_cal[flag:p] + t
                    i = k - 1
                    flag = k
                for j in range(i + 3, len(the_cal)):
                    if the_cal[j] == '(' and flag2 == 0:
                        flag1 = j
                        flag2 = 1
                        stack.append('(')
                    elif the_cal[j] == '(':
                        stack.append('(')
                    elif the_cal[j] == ')':
                        stack.pop()
                        if len(stack) == 0:
                            flag2 = 0
                            the_new_cal = the_cal[flag1 + 1:j]
                            t = self.calt_final(the_new_cal)
                            if the_cal[i] != 'a':
                                if the_cal[i + 1] != 'q':  # tri and sqrt\
                                    t = math.radians(t)
                                if the_cal[i:i + 3] == tri_op[0]:
                                    t = sy.sin(t)
                                elif the_cal[i:i + 3] == tri_op[1]:
                                    t = sy.cos(t)
                                elif the_cal[i:i + 3] == tri_op[2]:
                                    t = sy.tan(t)
                                elif the_cal[i:i + 4] == tri_op[6]:
                                    print(1)
                                    t = math.sqrt(t)
                            else:
                                if the_cal[i:i + 4] == tri_op[3]:
                                    t = sy.asin(t)
                                elif the_cal[i:i + 4] == tri_op[4]:
                                    t = sy.acos(t)
                                elif the_cal[i:i + 4] == tri_op[5]:
                                    t = sy.atan(t)
                                t = math.degrees(t)
                                t = math.radians(t)
                            t = str(t)
                            final_cal += the_cal[flag:i] + t
                            i = j
                            flag = j + 1
                            break
            i += 1
            if i >= len(the_cal):
                break
        try:
            final_cal += the_cal[flag:len(the_cal)]
            return eval(final_cal)
        except:
            self.result_display1.setText('None')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    calculator = Calculator()

    sys.exit(app.exec_())
