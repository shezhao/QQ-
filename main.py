import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5 import uic

# API接口
url_qq_to_phone = 'https://zy.xywlapi.cc/qqapi'
url_phone_to_qq = "https://zy.xywlapi.cc/qqphone"
url_id_to_phone = "https://zy.xywlapi.cc/wbapi"


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.menu()

    # 打开QQ-Phone界面
    def menu(self):
        self.ui_menu = uic.loadUi("menu.ui")
        self.qq_button = self.ui_menu.pushButton
        self.phone_button = self.ui_menu.pushButton_2
        self.id_button = self.ui_menu.pushButton_3
        # print(self.qq_button)
        # print(self.phone_button)
        self.qq_button.clicked.connect(self.open_qq)
        self.phone_button.clicked.connect(self.open_phone)
        self.id_button.clicked.connect(self.open_id)


    def open_qq(self):
        self.qq_window = Qqwindow()
        self.qq_window.ui_qq.show()

    def open_phone(self):
        self.phone_window = Phwindow()
        self.phone_window.ui_phone.show()

    def open_id(self):
        self.id_window = Idwindow()
        self.id_window.ui_id.show()


class Qqwindow(QWidget):
    global url_qq_to_phone

    def __init__(self):
        super().__init__()
        self.qq_find()

    def qq_find(self):
        self.ui_qq = uic.loadUi("qq.ui")

        self.qq_number = self.ui_qq.lineEdit
        self.qq_number.textChanged.connect(self.update_qq_number)

        self.qq_start_button = self.ui_qq.pushButton
        self.qq_start_button.clicked.connect(self.find_phone)

        self.qq_display = self.ui_qq.textBrowser

    def update_qq_number(self, text):
        # print(f'QQ Number: {text}')
        self.qq_number_text = text

    def find_phone(self):
        # print(f'QQ Number: {self.qq_number_text}')
        self.qq_find_phone(str(self.qq_number_text))

    # qq查找电话
    def qq_find_phone(self, qq_number):
        qq_str = qq_number
        params_qq = {
            'qq': qq_str
        }
        try:
            response = requests.get(url_qq_to_phone, params=params_qq)
            if not response:
                self.qq_display.setText("请检查网络与vpn")
            elif response.status_code == 200:
                data = response.json()
                self.qq_display.setText(str_in(data))
                # 处理返回的数据
            else:
                self.qq_display.setText('请求失败:', response.status_code)
        except Exception as e:
            self.qq_display.setText(e)


class Phwindow(QWidget):
    global url_phone_to_qq

    def __init__(self):
        super().__init__()
        self.phone_find()

    def phone_find(self):
        self.ui_phone = uic.loadUi("phone.ui")

        self.phone_number = self.ui_phone.lineEdit
        self.phone_number.textChanged.connect(self.update_phone_number)

        self.phone_start_button = self.ui_phone.pushButton
        self.phone_start_button.clicked.connect(self.find_phone)

        self.phone_display = self.ui_phone.textBrowser

    def update_phone_number(self, text):
        # print(f'phone Number: {text}')
        self.phone_number_text = text

    def find_phone(self):
        # print(f'phone Number: {self.phone_number_text}')
        self.phone_find_phone(str(self.phone_number_text))

    # phone查找电话
    def phone_find_phone(self, phone_number):
        phone_str = phone_number
        params_phone = {
            'phone': phone_str
        }
        try:
            response = requests.get(url_phone_to_qq, params=params_phone)
            if not response:
                self.phone_display.setText("请检查网络与vpn")
            elif response.status_code == 200:
                data = response.json()
                self.phone_display.setText(str_in(data))
                # 处理返回的数据
            else:
                self.phone_display.setText('请求失败:', response.status_code)
        except Exception as e:
            self.phone_display.setText(e)


class Idwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.id_find()

    def id_find(self):
        self.ui_id = uic.loadUi("web.ui")

        self.id_number = self.ui_id.lineEdit
        self.id_number.textChanged.connect(self.update_id_number)

        self.id_start_button = self.ui_id.pushButton
        self.id_start_button.clicked.connect(self.find_phone)

        self.id_display = self.ui_id.textBrowser

    def update_id_number(self, text):
        # print(f'id Number: {text}')
        self.id_number_text = text

    def find_phone(self):
        # print(f'id Number: {self.id_number_text}')
        self.id_find_phone(str(self.id_number_text))

    # id查找电话
    def id_find_phone(self, id_number):
        id_str = id_number
        params_id = {
            'id': id_str
        }
        try:
            response = requests.get(url_id_to_phone, params=params_id)
            if not response:
                self.id_display.setText("请检查网络与vpn")
            elif response.status_code == 200:
                data = response.json()
                self.id_display.setText(str_in(data))
                # 处理返回的数据
            else:
                self.id_display.setText('请求失败:', response.status_code)
        except Exception as e:
            self.id_display.setText(e)


def str_in(dir_x):
    key_value_pair_string = '\n'.join(f'{k}={v}' for k, v in dir_x.items())
    return key_value_pair_string


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MenuWindow()
    w.ui_menu.show()
    sys.exit(app.exec_())
