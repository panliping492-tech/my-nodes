import os

print("🚀 开始运行节点获取脚本...")

# 这里是你的核心代码逻辑，我们先让它模拟生成一个节点文件
try:
    with open("nodes.txt", "w", encoding="utf-8") as f:
        f.write("# 这是一个测试节点文件\n")
        f.write("ss://Y2F0bm9kZXM=@127.0.0.1:8888\n")
    print("✅ 脚本运行结束，数据已成功保存到 nodes.txt")
except Exception as e:
    print(f"❌ 运行出错了: {e}")
