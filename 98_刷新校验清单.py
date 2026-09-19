#!/usr/bin/env python3
"""刷新 校验清单.json：按当前磁盘内容重算所有 markdown 的字节数与 SHA-256，
新增文件自动登记，已删除文件自动移除。改完文件后在仓库根目录跑一次：

    python 98_刷新校验清单.py

只动 校验清单.json 的 files 段与 package_version 之外的内容，不改 layout、
sources、protocol_versions 等人工维护字段。哈希只证明传输完整性，不代表
数学内容或教学效果已验收。
"""
import glob, hashlib, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
MANIFEST = "校验清单.json"

if not os.path.exists(MANIFEST):
    sys.exit(f"找不到 {MANIFEST}，请在仓库根目录运行")

data = json.load(open(MANIFEST, encoding="utf-8"))
on_disk = sorted(p.replace("\\", "/") for p in glob.glob("**/*.md", recursive=True))
normalized = {}
for entry in data.get("files", []):
    entry["path"] = entry["path"].replace("\\", "/")
    normalized.setdefault(entry["path"], {}).update(entry)
data["files"] = list(normalized.values())
listed = {e["path"] for e in data.get("files", [])}

added = [p for p in on_disk if p not in listed]
removed = [p for p in sorted(listed) if not os.path.exists(p)]

entries = [e for e in data.get("files", []) if os.path.exists(e["path"])]
entries += [{"path": p} for p in added]
for e in entries:
    blob = open(e["path"], "rb").read()
    e["bytes"] = len(blob)
    e["sha256"] = hashlib.sha256(blob).hexdigest()
entries.sort(key=lambda e: e["path"])
data["files"] = entries

with open(MANIFEST, "w", encoding="utf-8") as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=2))

print(f"已登记 {len(entries)} 个文件")
for p in added:
    print("  新增：", p)
for p in removed:
    print("  移除：", p)
if not added and not removed:
    print("  文件集合未变，只刷新了哈希")
