import json

def copy_json_with_multiplication(input_file, output_file, multiplier):
    # 读取源 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # 将数据复制指定倍数
    expanded_data = data * multiplier

    # 将扩展后的数据写入新 JSON 文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(expanded_data, outfile, ensure_ascii=False, indent=4)

# 示例调用
input_file = 'zengqiang.jsonl'  # 输入源 JSON 文件路径
output_file = 'train_v2_0_0.jsonl'  # 输出目标 JSON 文件路径
multiplier = 50000  # 复制倍数

copy_json_with_multiplication(input_file, output_file, multiplier)
