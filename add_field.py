import json


def add_system_field_to_jsonl(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w',
                                                                      encoding='utf-8') as outfile:
        for line in infile:
            try:
                # 解析每一行的 JSON 对象
                json_object = json.loads(line.strip())

                # 为每个 JSON 对象添加 "system" 字段
                json_object["system"] = "You are a helpful assistant."

                # 将修改后的 JSON 对象写入输出文件
                outfile.write(json.dumps(json_object, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                # print(f"Error decoding JSON line: {line}")
                print(e)


if __name__ == "__main__":
    input_file_path = 'merged_output.jsonl'  # 输入文件路径
    output_file_path = 'merged_output_system.jsonl'  # 输出文件路径
    add_system_field_to_jsonl(input_file_path, output_file_path)
    print("Finished modifying the JSONL file.")
