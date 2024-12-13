import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog


def analyze_file(content):
    # 初始化一个Counter对象来跟踪频率
    data_counter = Counter()

    # 逐行读取内容
    lines = content.split('\n')
    for line in lines:
        # 使用正则表达式查找匹配的字符串
        match = re.search(r'\|\s+\d+\|(.*?)\]', line)
        if match:
            # 提取匹配的字符串
            data = match.group(1).strip()
            # 更新计数器
            data_counter[data] += 1

    return data_counter


def show_file_content(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 清空文本框
    content_text.delete('1.0', tk.END)

    # 在文本框中显示文件内容
    content_text.insert(tk.END, content)


def show_results():
    content = content_text.get('1.0', tk.END)
    if not content.strip():
        return

    # 分析内容
    data_counter = analyze_file(content)

    # 清空结果文本框
    result_text.delete('1.0', tk.END)

    # 打印每个数据及其出现的频率
    for data, count in data_counter.items():
        result_text.insert(tk.END, f'日志编号：{data}     出现频率：{count}次\n')


def choose_file():
    # 打开文件对话框，让用户选择要分析的文件
    file_path = filedialog.askopenfilename()
    if file_path:
        show_file_content(file_path)


def count_data():
    show_results()


# 创建Tkinter窗口
root = tk.Tk()
root.title("日志编号分析工具_lswei")
root.geometry("1920x1080")
root.configure(bg="black")  # 设置窗口背景颜色为蓝色

# 创建选择文件按钮
select_file_button = tk.Button(root, text="选择文件", command=choose_file)
select_file_button.pack(pady=10)

# 创建文本框，用于显示文件内容
content_text = tk.Text(root, height=45, width=500, bg="black", fg="white")  # 设置文本框背景为黑色，文本颜色为白色
content_text.pack()


# 创建统计按钮
count_button = tk.Button(root, text="统计", command=count_data)
count_button.pack(pady=10)

# 创建文本框，用于显示结果
result_text = tk.Text(root, height=20, width=100, bg="black", fg="white")  # 设置结果文本框背景为黑色，文本颜色为白色
result_text.pack()

# 创建滚动条，用于滚动文本框中的内容
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
