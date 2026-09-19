# MVCLOSE01 审查交接与Stage A
元信息：批次 MVCLOSE01 | 卷版本 v1 | 更新 2026-09-17 | 状态 independent_validation_pending | 可见性 审查（先独立审查并封存） | 学生卷 `../../题库/MVCLOSE01_多元微积分收尾混合复习/学生卷.md`

仅含题包与允许前置；按根目录Validation协议由外部审查方独立执行。本地未解题验收。先封存Stage A，再读取解析目录的目标声明；不得预先加载学情或设计目的。

## 前置声明
P-MATH1-CALC-v1范围依据为根目录01_高等数学_总入口.md §4.1第5—6项及直接代数前置。下列P01—P08为本批显式允许工具，不是对学习者能力的断言。

### P01
参数偏导与叉乘；无向面积及定向；参数交换。

### P02
曲线积分参数化；Green公式及定义域条件；分片边界与环域。

### P03
一元Taylor余项；局部极值定义；多元统一不等式估计。

### P04
第二类曲面积分；隐式或参数法向；有向投影和普通平面面积；矩形二重积分。

### P05
空间球面与平面交线；曲线积分；Stokes公式条件及方向；圆盘曲面积分与对称性。

### P06
通量、散度、Gauss公式条件；封闭边界方向；柱体与圆盘积分。

### P07
一元Taylor及复合总次数；齐次多项式；O/o余项；多元极限与路径反证。

### P08
Jacobian矩阵；转置、对称分解；叉乘与旋度；C2函数混合偏导相等。

## MVCLOSE01-01
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "曲面 $S$ 是 $z=1+x^2+y^2$ 在 $x^2+y^2\\le1$ 上方的部分，始终取向上的方向。\n\n甲用 $r(u,v)=(u,v,1+u^2+v^2)$，乙用 $\\widetilde r(s,t)=(t,s,1+s^2+t^2)$；各自的参数都在单位圆盘内，映射输出均为曲面上的点。\n\n两人分别写出向量面积元 $r_u\\times r_v\\,du\\,dv$ 和 $\\widetilde r_s\\times\\widetilde r_t\\,ds\\,dt$。这两种写法是否都符合题目的方向？如有不符，改正，并说明换参数后 $\\iint_S dS$ 与 $\\iint_S n_z\\,dS$ 的数值是否应改变；不要求算出这两个积分。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "参数偏导与叉乘；无向面积及定向；参数交换。",
      "source_ref": "本文件P01；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-02
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "圆周 $L:(x-1)^2+y^2=4$ 按逆时针方向行进。计算\n\\[\n\\oint_L\\left(-\\frac{y}{x^2+y^2}-y\\right)dx\n+\\left(\\frac{x}{x^2+y^2}+x\\right)dy.\n\\]\n先说明所用方法及其适用范围，再计算。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "曲线积分参数化；Green公式及定义域条件；分片边界与环域。",
      "source_ref": "本文件P02；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-03
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "设\n\\[\nf(x,y)=\\sin(x^2+y^2)-(x^2+y^2)+x^4+y^4.\n\\]\n判断原点是否为局部极值点；若是，说明类型及是否严格。须给出对整个充分小邻域成立的依据，不能只检查几条路径。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "一元Taylor余项；局部极值定义；多元统一不等式估计。",
      "source_ref": "本文件P03；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-04
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "曲面 $S$ 为\n\\[\nx=yz,\\qquad 0\\le y\\le1,\\quad 0\\le z\\le2,\n\\]\n取法向量 $x$ 分量为负的方向。计算\n\\[\n\\iint_S x\\,dy\\,dz+z\\,dz\\,dx+y\\,dx\\,dy.\n\\]\n写清采用的投影或参数区域，明确普通平面面积元与题目方向如何对应，再完成计算。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "第二类曲面积分；隐式或参数法向；有向投影和普通平面面积；矩形二重积分。",
      "source_ref": "本文件P04；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-05
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "闭曲线 $L$ 是球面 $x^2+y^2+z^2=1$ 与平面 $x+y+z=1$ 的交线。从 $z$ 轴正向朝原点看，$L$ 沿逆时针方向行进。计算\n\\[\n\\oint_L -yz\\,dx+xz\\,dy+y\\,dz.\n\\]\n给出方法选择和方向依据；若使用辅助曲面，写清该曲面的范围及方向。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "空间球面与平面交线；曲线积分；Stokes公式条件及方向；圆盘曲面积分与对称性。",
      "source_ref": "本文件P05；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-06
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-06",
    "package_version": 1,
    "title": "第6题",
    "stem": "立体 $V$ 为 $x^2+y^2\\le1,\\ 0\\le z\\le2$。曲面 $S$ 由它的圆柱侧面与上底面 $z=2$ 组成，不包含下底面，方向均向 $V$ 外。\n\n计算向量场\n\\[\nF=(x+\\sin(yz),\\ y+\\sin(xz),\\ z+1)\n\\]\n通过 $S$ 的通量。说明方法选择；如果增减了边界，写清该部分的有向贡献。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "通量、散度、Gauss公式条件；封闭边界方向；柱体与圆盘积分。",
      "source_ref": "本文件P06；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-07
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-07",
    "package_version": 1,
    "title": "第7题",
    "stem": "令\n\\[\nf(x,y)=\\cos(x^2+y^2+xy^2)-\\cos(x^2+y^2),\n\\qquad \\rho=\\sqrt{x^2+y^2}.\n\\]\n写出最低次非零齐次多项式 $P_m$、次数 $m$，并把函数写成 $f=P_m+R$，给出对所有趋近方式成立的余项阶估计。\n\n再判断 $f/\\rho^m$ 在原点的极限是否存在，给出依据。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "一元Taylor及复合总次数；齐次多项式；O/o余项；多元极限与路径反证。",
      "source_ref": "本文件P07；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MVCLOSE01-08
```json
{
  "item_package": {
    "item_id": "MVCLOSE01-08",
    "package_version": 1,
    "title": "第8题",
    "stem": "设 $F(x,y,z)=(2x-y,\\ 3x+z,\\ -y+z)$，$J=DF$，其中 $J$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$。令\n\\[\nK=\\frac{J-J^T}{2}.\n\\]\n求满足 $Kh=\\omega\\times h$ 对每个三维向量 $h$ 都成立的向量 $\\omega$，并写出它与 $\\nabla\\times F$ 的关系，说明依据。\n\n若把 $F$ 换成 $F+\\nabla\\phi$，其中 $\\phi$ 是 $\\mathbb R^3$ 上任意 $C^2$ 标量函数，$K$ 是否改变？不要求重写一般曲面积分公式的完整证明。",
    "options": [],
    "instructions": "所有变量取实数，三维空间采用右手直角坐标系。独立纸笔作答，每题写结论、关键理由和必要计算；可以采用不同合法路线。遇到遗忘，保留已经完成的步骤，不必硬猜。记录作答顺序及中途查阅或提示。\n\n$dS$ 表示曲面无向面积元，$n$ 表示题目指定的单位法向；第二类曲面积分按该方向解释。普通平面正面积元可统一写为 $dA$，与有向投影面积元分开标注。",
    "response_requirement": "完成公开各问，结论、关键理由和必要计算齐全。",
    "scoring_rule": {
      "fully_acceptable": [
        "条件、方向、推理与计算成立；接受所有满足题意的合法路线。"
      ],
      "partially_acceptable": [
        "保留正确子问与步骤，不由最终答案反推未展示过程。"
      ],
      "unacceptable": [
        "关键条件或方向错误；无依据结论；使用待证命题代替证明。"
      ]
    },
    "source_refs": [
      "原创，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "Jacobian矩阵；转置、对称分解；叉乘与旋度；C2函数混合偏导相等。",
      "source_ref": "本文件P08；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及显式允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
