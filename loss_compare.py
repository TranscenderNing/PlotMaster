import matplotlib.pyplot as plt
import json
import os

def plot_loss_from_files(file_paths, output_file):
    # 定义线条样式和灰度
    linestyles = ['-', '--', '-.', ':']
    grayscale = [0.1, 0.3, 0.5, 0.7, 0.9]  # 从浅到深的灰度值
    fig, ax = plt.subplots()
    
    # 存储图例标签
    labels = []
    
    for i, file_path in enumerate(file_paths):
        # 读取 JSON 文件内容
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # 提取 'epoch' 和 'loss' 数据
        epochs = [entry['epoch'] for entry in data]
        loss_values = [entry['loss'] for entry in data]
        
        # 选择线条样式和灰度
        linestyle = linestyles[i % len(linestyles)]
        color = (grayscale[i % len(grayscale)],) * 3  # RGB 色值 (灰度)
        
        # 生成图例标签
        label = os.path.basename(file_path)  # 使用文件名作为图例标签
        labels.append(label)
        
        # 绘制 loss 曲线，并设置图例标签
        ax.plot(epochs, loss_values, linestyle=linestyle, color=color, label=label)
    
    # 设置坐标轴标签和标题
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title('Loss vs Epoch for Multiple Files')
    
    # 添加图例
    ax.legend(loc='best')
    
    # 保存图像到文件
    plt.savefig(output_file, format='png')  # 你可以选择其他格式，如 'jpg', 'pdf', 'svg' 等
    plt.savefig(output_file.replace('.png','pdf'), format='pdf')
    # 显示图像
    plt.show()

# 示例文件路径列表
file_paths = [
    '/home/ldn/baidu/reft-pytorch-codes/PlotMaster/data/loss_n2.json',  # 替换为实际文件路径
    '/home/ldn/baidu/reft-pytorch-codes/PlotMaster/data/loss_n4.json',  # 替换为实际文件路径
    '/home/ldn/baidu/reft-pytorch-codes/PlotMaster/data/loss_n8.json',
    '/home/ldn/baidu/reft-pytorch-codes/PlotMaster/data/loss_n16.json',# 替换为实际文件路径
]

# 输出文件路径，保存为 'loss_comparison.png'
output_file = 'loss_comparison.png'

plot_loss_from_files(file_paths, output_file)
