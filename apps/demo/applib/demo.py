import os
import shutil
from pathlib import Path


def copy_directory_contents(source: str, destination: str, overwrite: bool = True) -> None:
    """
    递归地将源目录的内容复制到已存在的目标目录中，可选择替换已存在的文件。

    参数:
        source (str): 源目录路径
        destination (str): 已存在的目标目录路径
        overwrite (bool): 是否覆盖已存在的文件（默认为 True）

    抛出:
        FileNotFoundError: 如果源目录不存在
        NotADirectoryError: 如果源路径或目标路径不是目录
        FileNotFoundError: 如果目标目录不存在
    """
    # 转换为 Path 对象以处理路径问题
    src_path = Path(source)
    dst_path = Path(destination)

    # 检查源目录是否存在且是一个目录
    if not src_path.exists():
        raise FileNotFoundError(f"源目录不存在: {source}")
    if not src_path.is_dir():
        raise NotADirectoryError(f"源路径不是一个目录: {source}")

    # 检查目标目录是否存在且是一个目录
    if not dst_path.exists():
        raise FileNotFoundError(f"目标目录不存在: {destination}")
    if not dst_path.is_dir():
        raise NotADirectoryError(f"目标路径不是一个目录: {destination}")

    try:
        # 遍历源目录中的所有内容
        for item in src_path.iterdir():
            src_item_path = src_path / item
            dst_item_path = dst_path / item.name

            if src_item_path.is_dir():
                # 如果是子目录，递归复制
                if not dst_item_path.exists():
                    os.makedirs(dst_item_path)
                copy_directory_contents(src_item_path, dst_item_path, overwrite)
            else:
                # 如果是文件，复制文件（如果 overwrite 为 True 则替换已存在的文件）
                if dst_item_path.exists() and overwrite:
                    print(f"替换已存在的文件: {dst_item_path}")
                    # 确保文件可写（处理只读文件）
                    if not dst_item_path.stat().st_mode & 0o200:  # 检查是否有写入权限
                        os.chmod(dst_item_path, dst_item_path.stat().st_mode | 0o200)  # 添加写入权限
                shutil.copy2(src_item_path, dst_item_path)
                print(f"复制文件: {src_item_path} -> {dst_item_path}")

        print(f"成功将目录 '{source}' 的内容复制到 '{destination}'")
    except Exception as e:
        print(f"复制目录内容时出错: {e}")


if __name__ == "__main__":
    # 使用示例
    try:
        # 替换为实际的源目录和目标目录路径
        source_dir = "/apps/demo"
        target_dir = "F:\copy_test"

        # 默认启用 overwrite=True，自动替换已存在的文件
        copy_directory_contents(source_dir, target_dir)
    except Exception as e:
        print(f"操作失败: {e}")
