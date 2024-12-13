import os
import pandas as pd
from tabulate import tabulate

def excel_to_rst(input_file, output_file):
    """
    将 Excel 文件中所有工作表的内容合并为 RST 格式并保存到指定文件中。

    参数:
    - input_file: 输入的 Excel 文件路径。
    - output_file: 输出的 RST 文件路径。
    """
    # 读取 Excel 文件
    sheets = pd.read_excel(input_file, sheet_name=None)  # 读取所有工作表

    with open(output_file, 'w', encoding='utf-8') as f:
        for sheet_name, df in sheets.items():
            # 添加工作表标题
            f.write(f"\n工作表: {sheet_name}\n")
            f.write("=" * (len(sheet_name) * 3) + "\n\n")

            # 转换为 RST 表格格式
            rst_table = tabulate(df, headers='keys', tablefmt='grid')
            f.write(rst_table + "\n")

    print(f"文件 {input_file} 已转换为 RST 文件: {output_file}")

if __name__ == "__main__":
    # 获取当前文件夹内所有 .xlsx 文件
    current_dir = os.getcwd()
    excel_files = [f for f in os.listdir(current_dir) if f.endswith('.xlsx')]

    if not excel_files:
        print("当前文件夹内未找到 .xlsx 文件。")
    else:
        for excel_file in excel_files:
            # 生成对应的 .rst 文件名
            rst_file = os.path.splitext(excel_file)[0] + ".rst"

            # 调用转换函数
            excel_to_rst(excel_file, rst_file)
