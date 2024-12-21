def copy_jsonl_file(input_file_path, output_file_path, copy_count):
    """
    复制jsonl文件并根据倍数重复内容

    :param input_file_path: 输入的jsonl文件路径
    :param output_file_path: 输出的jsonl文件路径
    :param copy_count: 复制的倍数
    """
    try:
        # 打开输入文件和输出文件
        with open(input_file_path, 'r', encoding='utf-8') as infile, \
                open(output_file_path, 'w', encoding='utf-8') as outfile:

            # 逐行读取输入文件
            for line in infile:
                # 每行内容根据倍数重复写入输出文件
                for _ in range(copy_count):
                    outfile.write(line.strip() + '\n')  # 写入一行内容并加上换行符
                    # outfile.write(line)  # 写入一行内容
    except FileNotFoundError:
        print(f"输入文件 {input_file_path} 不存在.")
    except Exception as e:
        print(f"文件操作出错: {e}")


if __name__ == "__main__":
    # input_file = "clean.jsonl"  # 输入文件路径
    # output_file = "train_v2_0_1.jsonl"  # 输出文件路径
    input_file = "zengqiang.jsonl"  # 输入文件路径
    output_file = "train_v2_0_2.jsonl"  # 输出文件路径

    copy_count = 500  # 复制倍数

    copy_jsonl_file(input_file, output_file, copy_count)
    print("文件复制完成，已根据倍数进行重复！")
