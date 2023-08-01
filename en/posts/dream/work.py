import os
import re

path = "./"

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        # 对于 Markdown 文件进行处理
        if name.endswith(".md") or name.endswith(".markdown"):
            with open(os.path.join(root, name), "r+", encoding='UTF-8') as f:
                # 读取文件内容
                content = f.read()
                # 替换内容
                content = re.sub(r'', r'dream', content)
                # 将指针移动到文件开头
                f.seek(0)
                # 清空文件
                f.truncate()
                # 将修改后的内容写入文件
                f.write(content)
                # 关闭文件
                f.close()
