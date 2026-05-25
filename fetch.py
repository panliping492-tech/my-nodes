import urllib.request
import base64

urls = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/colatiger/v2ray-nodes/master/v2ray.md"
]

all_nodes = []
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8').strip()
            try:
                # 尝试解密 Base64 格式
                decoded = base64.b64decode(content + '=' * (-len(content) % 4)).decode('utf-8')
                all_nodes.extend(decoded.strip().split('\n'))
            except:
                # 若是明文，直接添加
                all_nodes.extend(content.split('\n'))
    except: pass

valid_nodes = [node.strip() for node in all_nodes if node.strip()]
with open("nodes.txt", "w", encoding="utf-8") as f:
    for node in valid_nodes:
        f.write(node + "\n")
