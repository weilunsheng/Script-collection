import serial
import time

# 打开串口，设置偶校验位和8位数据位
ser = serial.Serial('COM9', baudrate=115200, timeout=1, parity=serial.PARITY_EVEN, bytesize=serial.EIGHTBITS)

# 初始的报文和待发送数据
initial_message = '8203009F8B8109017E015F000500A342000000FFFFFFFFFF7E'
send_data_base = bytes.fromhex(initial_message)
send_data = send_data_base

# 一个 KB 值对应的 num_iterations 数量
num_iterations_per_kb = 4
# 输入 KB 值
kb_value = float(input("请输入要读取的 KB 值："))
# 根据 KB 值计算 num_iterations
num_iterations = int(kb_value * num_iterations_per_kb)

# 接收数据并累加
with open('output.bin', 'wb') as file:
    for i in range(num_iterations):
        ser.write(send_data)

        # 等待串口接收数据
        while ser.in_waiting == 0:
            pass  # 等待直到串口接收到数据
        time.sleep(0.2)

        # 从串口读取接收到的数据 received_data
        received_data = ser.read_all()
        received_data = received_data[8:-5]

        # 将接收到的数据转换为十六进制字符串，方便处理
        hex_string = ' '.join(format(byte, '02x') for byte in received_data)
        # 检测并替换 0x7D5D 为 0x7D
        hex_string = hex_string.replace('7d 5d', '7d')
        # 检测并替换 0x7D5E 为 0x7E
        hex_string = hex_string.replace('7d 5e', '7e')
        # 将修改后的十六进制字符串转换回字节数据
        received_data = bytes.fromhex(hex_string)
        # 将接收到的数据存储
        file.write(received_data)
        res = ' '.join(format(byte, '02x') for byte in received_data)
        print(f"收到的数据：{res}")

        # 在每一轮发送之前检查递增的字节是否为0x7E，如果是，则转换为0x7D 0x5E
        data_to_change = bytearray(send_data_base)
        if data_to_change[16] == 0x7D and data_to_change[17] == 0x5E:
            data_to_change[16:18] = bytes([0x7E])  # 将0x7D 0x5E 转换为0x7E
        byte_to_update = data_to_change[16]

        byte_to_update = (byte_to_update + 1) % 256

        # 如果要递增的字节为0x7E，则转换为0x7D 0x5E64
        if byte_to_update == 0x7E:
            data_to_change[16:17] = bytes([0x7D, 0x5E])
        else:
            # 不是0x7E，直接更新字节
            data_to_change[16] = byte_to_update

        # 将更新后的字节数据转换为 bytes 类型，并设置为发送的数据
        send_data = bytes(data_to_change)
        send_data_base = send_data
        # res1 = ' '.join(format(byte, '02x') for byte in send_data)
        # print(f"发送数据（十六进制表示）：{res1}")

        #清空buff
        ser.flushInput()


print("所有数据已写入到 output.bin 文件中")

# 关闭串口
ser.close()
