#!/usr/bin/env python3
"""检查仓库是否符合摆放与交接约定。推送前在仓库根目录跑：

    python 97_检查摆放.py

检查项：批次三目录成对、文件头元信息的字段与取值、学生卷不含审查侧信息、
批次已在99登记、包内引用能解析、校验清单与磁盘一致。

只检查可机械判定的部分。标题文字、正文写法、数学内容与教学判断都不在检查范围，
那些按 AGENTS.md 与各协议执行。退出码非0表示有需要修的项。
"""
import glob, hashlib, json, os, re, sys

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ERR, WARN = [], []
def err(where, msg): ERR.append((where, msg))
def warn(where, msg): WARN.append((where, msg))

# 状态词表从 92 解析，保持单一出处
SPEC = "92_题库批次规范.md"
spec_text = open(SPEC, encoding="utf-8").read() if os.path.exists(SPEC) else ""
m = re.search(r"状态词固定用下列七个.*?：\n\s*(.+)", spec_text)
STATUS = set(re.findall(r"`([a-z_<>N0-9]+)`", m.group(1))) if m else set()
if not STATUS:
    err(SPEC, "没能从92解析出状态词表，后续状态检查跳过")
STATUS_RE = {re.sub(r"<N>", r"\\d+", s) for s in STATUS}

TREES = {"题库": "题库", "审查": "审查", "解析": "解析"}
batches = {k: set(os.path.basename(p) for p in glob.glob(f"{v}/*") if os.path.isdir(p))
           for k, v in TREES.items()}

# 1. 批次目录成对
all_batches = set().union(*batches.values())
for b in sorted(all_batches):
    missing = [k for k in TREES if b not in batches[k]]
    if missing:
        warn(f"批次 {b}", "缺少目录：" + "、".join(f"{k}/{b}" for k in missing) + "（按92可以暂缺，但请确认是有意的）")
    code = b.split("_")[0]
    if code != b and not re.fullmatch(r"[A-Za-z0-9]+", code):
        err(f"批次 {b}", "目录名首段应是代号，如 MV26_多元微积分水平检测")

# 2. 教师侧文件头元信息
META = re.compile(
    r"^元信息：批次 (?P<code>\S+) \| 卷版本 (?P<ver>v\d+) \| 更新 (?P<date>\d{4}-\d{2}-\d{2})"
    r" \| 状态 (?P<status>[^|]+?) \| 可见性 (?P<vis>审查|解析)[^|]*\| 学生卷 `(?P<paper>[^`]+)`\s*$")
for tree in ("审查", "解析"):
    for f in sorted(glob.glob(f"{tree}/*/*.md")):
        head = open(f, encoding="utf-8").read().split("\n")[:6]
        line = next((l for l in head if l.startswith("元信息：")), None)
        if line is None:
            err(f, "缺少元信息行；格式见 92_题库批次规范.md"); continue
        mm = META.match(line)
        if not mm:
            err(f, "元信息行字段或顺序不符：批次 | 卷版本 | 更新 | 状态 | 可见性 | 学生卷"); continue
        b = os.path.basename(os.path.dirname(f))
        if mm["code"] != b.split("_")[0]:
            err(f, f"元信息批次 {mm['code']} 与目录 {b} 的代号不一致")
        if mm["vis"] != tree:
            err(f, f"元信息可见性 {mm['vis']} 与所在目录 {tree}/ 不一致")
        if STATUS:
            for s in [x.strip() for x in mm["status"].split(",")]:
                if not any(re.fullmatch(r, s) for r in STATUS_RE):
                    err(f, f"状态词 {s} 未在92登记")
        tgt = os.path.normpath(os.path.join(os.path.dirname(f), mm["paper"]))
        if not os.path.exists(tgt):
            err(f, f"元信息里的学生卷路径不存在：{mm['paper']}")
        elif not tgt.startswith("题库" + os.sep):
            err(f, "元信息里的学生卷应指向 题库/ 下的文件")

# 3. 学生卷：只有三项，且不带审查侧信息
PAPER = re.compile(r"^批次 (?P<code>\S+) \| 版本 v\d+ \| \d+题")
BAN = ["状态 ", "验收", "教师稿", "教师用", "Stage A", "审查/", "解析/", "package_version", "评分", "target_claim"]
for f in sorted(glob.glob("题库/*/*.md")):
    text = open(f, encoding="utf-8").read()
    head = text.split("\n")[:8]
    if not any(PAPER.match(l) for l in head):
        err(f, "学生卷开头缺少 `批次 X | 版本 vN | M题` 一行")
    else:
        code = next(PAPER.match(l)["code"] for l in head if PAPER.match(l))
        b = os.path.basename(os.path.dirname(f))
        if code != b.split("_")[0]:
            err(f, f"卷头批次 {code} 与目录 {b} 的代号不一致")
    for bad in BAN:
        if bad in text:
            err(f, f"学生卷含审查侧信息「{bad}」，按AGENTS第13条不应出现在这一级")

# 4. 批次是否在99批次表登记
inv = open("99_工作包文件与版本清单.md", encoding="utf-8").read()
table = inv.split("## 题目审查批次")[1].split("\n##")[0] if "## 题目审查批次" in inv else ""
for b in sorted(all_batches):
    if b.split("_")[0] not in table:
        err("99_工作包文件与版本清单.md", f"批次 {b} 未出现在批次表")

# 5. 包内引用能否解析
files = glob.glob("**/*.md", recursive=True) + glob.glob("*.py") + ["校验清单.json"]
allp = {os.path.normpath(p) for p in files}
byname = {}
for p in files: byname.setdefault(os.path.basename(p), []).append(p)
REF = re.compile(r"(?<=[`\(\[《])([^`\(\)\[\]《》\s]+\.(?:md|json|py))(?=[`\)\]》])")
for f in [x for x in files if x.endswith(".md")]:
    d = os.path.dirname(f) or "."
    for mo in REF.finditer(open(f, encoding="utf-8").read()):
        ref = mo.group(1)
        if ref == "YYYY-MM.md": continue  # 月度记录格式示例，不是具体文件
        if ref.startswith(("http", "分析/", "练习/")): continue
        if any(c in ref for c in "<>*…") or "..." in ref: continue   # 占位与通配不检查
        if os.path.normpath(os.path.join(d, ref)) in allp: continue
        base = os.path.basename(ref)
        if base in byname:
            err(f, f"引用路径错了：{ref} 实际在 {byname[base][0]}")
        else:
            warn(f, f"引用的文件不在包里：{ref}（已知缺件可忽略）")

# 6. 校验清单与磁盘一致
man = json.load(open("校验清单.json", encoding="utf-8"))
hash_mode = man.get("hash_normalization", "raw-bytes")
if hash_mode not in ("raw-bytes", "crlf-to-lf-v1"):
    err("校验清单.json", f"未知哈希归一化方式：{hash_mode}")
listed = {e["path"].replace("\\", "/") for e in man["files"]}
disk = {p.replace("\\", "/") for p in glob.glob("**/*.md", recursive=True)}
for p in sorted(disk - listed): err("校验清单.json", f"未登记：{p}")
for p in sorted(listed - disk): err("校验清单.json", f"登记了不存在的文件：{p}")
for e in man["files"]:
    path = e["path"].replace("\\", "/")
    if path in disk:
        blob = open(path, "rb").read()
        if hash_mode == "crlf-to-lf-v1":
            blob = blob.replace(b"\r\n", b"\n")
        if hashlib.sha256(blob).hexdigest() != e["sha256"]:
            err("校验清单.json", f"哈希过期：{e['path']}")
        if e.get("bytes") != len(blob):
            err("校验清单.json", f"字节数过期：{e['path']}")
if any("校验清单" in w for w, _ in ERR):
    ERR.append(("校验清单.json", "跑 python 98_刷新校验清单.py 即可修好上面的清单项"))

# 提醒按文件归并，只报数量与两个例子，避免刷屏；要全部细节加 --verbose
if "--verbose" in sys.argv:
    for w, m_ in WARN: print("提醒 ", w, "：", m_)
else:
    grouped = {}
    for w, m_ in WARN: grouped.setdefault(w, []).append(m_)
    for w in sorted(grouped):
        msgs = grouped[w]
        head = "；".join(dict.fromkeys(msgs[:2]))
        more = f"，另有 {len(msgs)-2} 条同类" if len(msgs) > 2 else ""
        print(f"提醒  {w}：{head}{more}")
    if grouped: print("（以上多为上游未接入的已知缺件，加 --verbose 看全部）")
print()
if ERR:
    for w, m_ in ERR: print("要修 ", w, "：", m_)
    print(f"\n共 {len(ERR)} 项需要修，{len(WARN)} 项提醒")
    sys.exit(1)
print(f"摆放检查通过，{len(WARN)} 项提醒")
