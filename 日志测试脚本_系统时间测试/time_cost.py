def hex_to_decimal(hex_string):
    decimal_value = int(hex_string, 16)
    return decimal_value

def calculate_result(hex_string):
    try:
        decimal_value = hex_to_decimal(hex_string)
        result = (decimal_value / 24) / 1000
        print(f"Hexadecimal: {hex_string}")
        print(f"Decimal: {decimal_value}")
        print(f"Result: {result} ms")
    except ValueError:
        print("无效的十六进制字符串，请确保输入正确。")

def main():
    while True:
        hex_string = input("请输入十六进制字符串 (输入 'exit' 退出): ").strip().upper()
        if hex_string == 'EXIT':
            break

        calculate_result(hex_string)

if __name__ == "__main__":
    main()
