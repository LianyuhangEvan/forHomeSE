def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # 将每行分割成(数字, 单词)的元组，并按数字排序
    lines = [line.strip().split(' ') for line in lines]
    lines.sort(key=lambda x: int(x[0]))
    
    # 根据金字塔结构确定要挑选的行
    pick_lines = [1]  # 总是挑选第一行
    next_pick = 2
    counter = 1
    for i in range(2, len(lines) + 1):
        counter -= 1
        if counter == 0:
            pick_lines.append(i)
            next_pick += 1
            counter = next_pick
    
    # 从选中的行中提取单词
    message = [lines[i-1][1] for i in pick_lines]
    
    return ' '.join(message)

# 使用示例，假设你有一个名为'message.txt'的文件在同一目录下
print(decode('coding_qual_input.txt'))

