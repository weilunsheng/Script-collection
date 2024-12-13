import os
import json
import shutil


def rename_folder_by_foldername(base_path):
    """
    遍历指定目录下的所有文件夹，读取 data.json 中的 folderName，将文件夹重命名为 folderName。
    :param base_path: 根目录路径
    """
    for root, dirs, files in os.walk(base_path, topdown=False):
        if 'data.json' in files:
            json_path = os.path.join(root, 'data.json')
            parent_path = os.path.dirname(root)

            try:
                # 使用 utf-8-sig 编码打开 JSON 文件
                with open(json_path, 'r', encoding='utf-8-sig') as f:
                    data = json.load(f)

                # 获取 JSON 中的 folderName
                if 'folderName' in data:
                    folder_name = data['folderName']
                    current_folder_name = os.path.basename(root)

                    if folder_name != current_folder_name:
                        # 计算新文件夹路径
                        new_folder_path = os.path.join(parent_path, folder_name)

                        if not os.path.exists(new_folder_path):
                            print(f"Renaming folder: {current_folder_name} -> {folder_name}")
                            shutil.move(root, new_folder_path)
                        else:
                            print(f"Conflict: Folder {folder_name} already exists, skipping...")
            except Exception as e:
                print(f"Error processing {json_path}: {e}")


if __name__ == "__main__":
    # 让用户输入路径
    base_directory = input("请输入根目录路径：").strip()

    if os.path.exists(base_directory) and os.path.isdir(base_directory):
        rename_folder_by_foldername(base_directory)
    else:
        print("输入的路径无效，请确保是有效的目录路径。")
