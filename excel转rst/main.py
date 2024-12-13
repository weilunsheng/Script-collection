import pandas as pd
from tabulate import tabulate
import argparse

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

    print(f"所有工作表已合并为 RST 文件: {output_file}")

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="将 Excel 文件的所有工作表内容转换为 RST 格式并合并输出。")
    parser.add_argument("-x", "--input_file", required=True, help="输入的 Excel 文件路径")
    parser.add_argument("-o", "--output_file", required=True, help="输出的 RST 文件路径")
    args = parser.parse_args()

    # 调用转换函数
    excel_to_rst(args.input_file, args.output_file)
