import matplotlib.pyplot as plt

# 数据
N_values = ["2", "4", "8", "16"]
acc_values = [70.12, 71.64, 72.25, 72.17]

# 创建柱状图，使用条纹区分，调整柱子宽度
patterns = ['/', '\\', '|', '-']  # 条纹样式
bars = plt.bar(N_values, acc_values, color='white', edgecolor='black', width=0.4)

# 为每个柱状图添加条纹样式
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# 在柱子上方显示数值
for bar, value in zip(bars, acc_values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{value:.2f}', 
             ha='center', va='bottom', fontsize=10)

# 添加标题和标签
# plt.title('Accuracy vs. Number of Segments', fontsize=14)
plt.xlabel('Number of Segments', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

# 设置横坐标刻度
plt.xticks(N_values)

# 设置 y 轴取值范围
plt.ylim(50, 75)

# 保存图表为PDF和PNG格式
plt.savefig('accuracy_vs_segments_bw.pdf', format='pdf')
plt.savefig('accuracy_vs_segments_bw.png', format='png')

# 显示图表
plt.show()