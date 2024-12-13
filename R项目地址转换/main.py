import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

def option(data, length):
    rtn = 0
    for i in range(length - 1, -1, -1):
        rtn *= 100
        uc = ((data[i] & 0xf0) >> 4) * 10
        uc += data[i] & 0x0f
        rtn += uc & 0xff
    return rtn

class AddressConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('R项目地址转换器_wls')
        self.setGeometry(100, 100, 400, 200)

        # 创建地址输入框
        self.input_label = QLabel('输入地址:', self)
        self.input_address = QLineEdit(self)

        # 创建转换按钮
        self.convert_button = QPushButton('地址转换', self)
        self.convert_button.clicked.connect(self.convertAddress)

        # 创建地址输出框
        self.output_label = QLabel('转换后的地址:', self)
        self.output_address = QLineEdit(self)
        self.output_address.setReadOnly(True)

        # 设置布局
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_label)
        hbox1.addWidget(self.input_address)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.convert_button)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.output_label)
        hbox2.addWidget(self.output_address)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def convertAddress(self):
        # 获取输入的十六进制地址
        hex_address = self.input_address.text()

        # 将十六进制字符串转换为字节数组
        data = bytes.fromhex(hex_address)

        # 反转字节数组
        reversed_data = data[::-1]

        # 执行地址转换操作
        result = option(reversed_data, len(reversed_data))

        # 将结果转换回十六进制字符串并转换为大写
        hex_result = hex(result)[2:].upper()

        # 如果十六进制字符串的长度为奇数，则补零确保长度为偶数
        if len(hex_result) % 2 != 0:
            hex_result = '0' + hex_result

        # 将结果补齐到与输入地址相同的长度
        if len(hex_result) < len(hex_address):
            hex_result = '0' * (len(hex_address) - len(hex_result)) + hex_result

        # 反转字节，但不分割成一对一对的字符
        reversed_hex_result = ''.join(([hex_result[i:i + 2] for i in range(0, len(hex_result), 2)]))

        # 在输出框显示转换后的地址
        self.output_address.setText(reversed_hex_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddressConverter()
    ex.show()
    sys.exit(app.exec_())
