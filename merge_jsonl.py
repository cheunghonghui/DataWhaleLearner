import json


def merge_jsonl_files(input_file_path1, input_file_path2, output_file_path):
    with open(input_file_path1, 'r', encoding='utf-8') as infile1, \
            open(input_file_path2, 'r', encoding='utf-8') as infile2, \
            open(output_file_path, 'w', encoding='utf-8') as outfile:

        # 处理第一个 JSONL 文件
        for line in infile1:
            try:
                # 直接将每行写入输出文件
                outfile.write(line)
            except Exception as e:
                print(f"Error writing line from {input_file_path1}: {line}")
                print(e)

        # 处理第二个 JSONL 文件
        for line in infile2:
            try:
                # 直接将每行写入输出文件
                outfile.write(line)
            except Exception as e:
                print(f"Error writing line from {input_file_path2}: {line}")
                print(e)


if __name__ == "__main__":
    input_file_path1 = 'train_v2_0_2.jsonl'  # 第一个输入文件路径
    input_file_path2 = 'train_v2_0_1.jsonl'  # 第二个输入文件路径
    output_file_path = 'merged_output.jsonl'  # 输出文件路径

    merge_jsonl_files(input_file_path1, input_file_path2, output_file_path)
    print(f"Finished merging the files into {output_file_path}.")
