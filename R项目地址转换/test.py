def option(data, length):
    rtn = 0
    for i in range(length - 1, -1, -1):
        rtn *= 100
        uc = ((data[i] & 0xf0) >> 4) * 10
        uc += data[i] & 0x0f
        rtn += uc & 0xff
    return rtn

def main():
    while True:
        # 循环输入十六进制地址字符串
        hex_address = input("输入十六进制地址（输入 q 退出程序）: ")

        # 如果输入为 'q'，则退出程序
        if hex_address.lower() == 'q':
            print("程序已退出。")
            break

        # 将十六进制字符串转换为字节数组
        data = bytes.fromhex(hex_address)

        # 反转字节数组
        reversed_data = data[::-1]

        # 执行地址转换操作
        result = option(reversed_data, len(reversed_data))

        # 将结果转换回十六进制字符串并转换为大写
        hex_result = hex(result)[2:].upper()  # 移除开头的 '0x' 前缀并转换为大写

        # 如果十六进制字符串的长度为奇数，则补零确保长度为偶数
        if len(hex_result) % 2 != 0:
            hex_result = '0' + hex_result

        # 将结果补齐到与输入地址相同的长度
        if len(hex_result) < len(hex_address):
            hex_result = '0' * (len(hex_address) - len(hex_result)) + hex_result

        # 反转字节，但不分割成一对一对的字符
        reversed_hex_result = ''.join(reversed([hex_result[i:i+2] for i in range(0, len(hex_result), 2)]))

        # 输出反转后的十六进制结果
        print("转换后的地址:", reversed_hex_result)

if __name__ == "__main__":
    main()
