import re
import json


def extract_loss_data(log_file_path):
    # 正则表达式匹配日志中包含 loss, grad_norm, learning_rate 和 epoch 的行
    pattern = r"\{'loss':\s*([\d\.e\+-]+),\s*'grad_norm':\s*([\d\.e\+-]+),\s*'learning_rate':\s*([\d\.e\+-]+),\s*'epoch':\s*([\d\.e\+-]+)\}"

    extracted_data = []

    # 打开日志文件并读取内容
    with open(log_file_path, "r") as file:
        log_content = file.read()

        # 使用正则表达式查找所有匹配的内容
        matches = re.findall(pattern, log_content)

        # 将匹配结果转换为字典并存储
        for match in matches:
            data = {
                "loss": float(match[0]),
                "grad_norm": float(match[1]),
                "learning_rate": float(match[2]),
                "epoch": float(match[3]),
            }
            extracted_data.append(data)

    return extracted_data


# 使用脚本
log_file_paths = [
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/train_melora_n2.log",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/train_melora.log",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/train_melora_n8.log",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/train_melora_n16.log",
]
output_json_paths = [
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/loss_n2.json",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/loss_n4.json",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/loss_n8.json",
    "/data/ldn/gsm8k-eval-with-multi-peft-methods/loss_n16.json",
]

for log_file_path, output_json_path in zip(log_file_paths, output_json_paths):
    print(log_file_path)
    print(output_json_path)
    loss_data = extract_loss_data(log_file_path)

    # 将 loss_data 写入 JSON 文件
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(loss_data, json_file, ensure_ascii=False, indent=4)

    print(f"Loss data has been written to {output_json_path}")
