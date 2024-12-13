# 打开原始的二进制文件
with open('ht_log_20240129100520.bin', 'rb') as original_file:
    # 定位到地址 0x6F000
    original_file.seek(0x6F000)

    # 读取从地址 0x6F000 到文件末尾的内容
    content = original_file.read()

# 将截取的内容写入新的二进制文件
with open('new_file.bin', 'wb') as new_file:
    new_file.write(content)

print("从地址 6F000 开始到文件末尾的内容已写入到 new_file.bin 文件中")
