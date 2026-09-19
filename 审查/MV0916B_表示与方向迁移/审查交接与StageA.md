# MV0916B 审查交接与Stage A
元信息：批次 MV0916B | 卷版本 v1 | 更新 2026-09-16 | 状态 independent_validation_pending | 可见性 审查（仅供外部审查） | 学生卷 `../../题库/MV0916B_表示与方向迁移/学生卷.md`

本文件只含完整Q及允许前置，不含答案、目标或学情。先依据根目录Validation协议执行独立Stage A并封存记录，再读取解析目录的目标声明；本地未进行独立验收。

## 前置声明
允许profile为P-MATH1-CALC-v1，范围来源为根目录01_高等数学_总入口.md §4.1第5—6项及直接代数前置；P01—P10是本批显式允许的具体工具，不是教材引文或学习者能力记录。第3题矩阵分解是局部补充工具，不作为正式考研范围扩大。

### P01
可微映射的矩阵；二维行列式的有向面积；三维叉乘的面积；单位法向与参数换序。

### P02
复合求导；C2混合偏导相等；内积、叉乘、旋度的坐标定义。

### P03
矩阵转置与对称/反对称分解；叉乘坐标；DF与旋度定义；C2函数Hessian的对称性；沿曲线复合求导与闭曲线积分。

### P04
隐式曲面的梯度法向及单位化；第一类曲面积分和投影关系；圆域极坐标积分。

### P05
图形曲面参数化；向量面积元和有向投影；第二类曲面积分；圆域积分。

### P06
曲线参数化、Stokes条件及方向；三角形参数域与一次多项式二重积分；三角形重心与仿射函数平均关系（可选，非必需）。

### P07
曲线参数化、Stokes条件及方向；三角形面积；限制函数到平面。

### P08
Gauss条件及向外方向；开放面与辅助边界；奇点及穿孔区域；半球体积与通量。

### P09
Hessian和矩阵核；齐次多项式；局部极值与鞍点；统一不等式估计及路径反证。

### P10
一元指数Taylor展开及余项；复合展开的总次数；O/o的多元定义；统一估计及否定小o的路径证据。

## MV0916B-01
```json
{
  "item_package": {
    "item_id": "MV0916B-01",
    "package_version": 1,
    "title": "A组 第1题",
    "stem": "设 $D=(-1,1)\\times(1,2)$，\n\\[\nr(u,v)=(u,v,uv),\\qquad \\pi(x,y,z)=(y,z),\\qquad \\psi=\\pi\\circ r.\n\\]\n分别说明 $Dr$ 与 $D\\psi$ 的定义域、值域和矩阵大小，并求参数面积 $du\\,dv$ 对应的曲面无向面积密度，以及投影到有序坐标 $(y,z)$ 平面后的有向面积密度。这里曲面取向由有序参数 $(u,v)$ 诱导。\n\n解释两个密度为什么不能用同一个数直接替代，并写出它们与单位法向量 $x$ 分量的关系。若改用 $\\widetilde r(s,t)=r(t,s)$、$(s,t)\\in(1,2)\\times(-1,1)$，哪些无向量不变，哪些有向量改变？区分“更换参数但保持原曲面方向”和“按新有序参数重新定向”。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "可微映射的矩阵；二维行列式的有向面积；三维叉乘的面积；单位法向与参数换序。",
      "source_ref": "本文件P01；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-02
```json
{
  "item_package": {
    "item_id": "MV0916B-02",
    "package_version": 1,
    "title": "A组 第2题",
    "stem": "设 $r(u,v)$ 是开参数域上的 $C^2$ 正则参数化，$F$ 在曲面附近为 $C^1$，定义\n\\[\nA(u,v)=F(r(u,v))\\cdot r_u,\n\\qquad B(u,v)=F(r(u,v))\\cdot r_v.\n\\]\n证明\n\\[\nB_u-A_v=(\\nabla\\times F)(r(u,v))\\cdot(r_u\\times r_v).\n\\]\n写清复合求导中各对象的类型、哪些项相消及其依据；不能只引用所要证明的等式。证明路线自选。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "复合求导；C2混合偏导相等；内积、叉乘、旋度的坐标定义。",
      "source_ref": "本文件P02；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-03
```json
{
  "item_package": {
    "item_id": "MV0916B-03",
    "package_version": 1,
    "title": "A组 第3题",
    "stem": "某 $C^1$ 向量场在点 $P$ 的导数矩阵为\n\\[\nJ=DF(P)=\n\\begin{pmatrix}2&-3&1\\\\1&0&-4\\\\-1&2&5\\end{pmatrix}.\n\\]\n求满足 $J=S+K$、$S^T=S$、$K^T=-K$ 的分解，并求满足 $Kh=\\omega\\times h$ 对所有 $h\\in\\mathbb R^3$ 成立的向量 $\\omega$；说明其唯一性及与 $(\\nabla\\times F)(P)$ 的关系。\n\n对任意向量 $a,b$，解释为什么 $(Ja)\\cdot b-(Jb)\\cdot a$ 不受 $S$ 影响。这为何与有向曲面上的局部环流表达有关？最后判断：若将向量场换成 $F+\\nabla\\phi$，其中 $\\phi$ 是同一开域上单值的 $C^2$ 函数，该域内任意分段光滑闭曲线上的环流是否改变？给出依据。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "矩阵转置与对称/反对称分解；叉乘坐标；DF与旋度定义；C2函数Hessian的对称性；沿曲线复合求导与闭曲线积分。",
      "source_ref": "本文件P03；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-04
```json
{
  "item_package": {
    "item_id": "MV0916B-04",
    "package_version": 1,
    "title": "B组 第4题",
    "stem": "设\n\\[\nS=\\{(x,y,z):x^2+y^2+z^2=4,\\ x\\ge1\\}.\n\\]\n求 $\\iint_S x^2\\,dS$。本题要求以 $yz$ 平面组织积分，写出从隐式方程得到的单位法向量、投影区域以及面积因子；不要省略面积因子的来源。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "隐式曲面的梯度法向及单位化；第一类曲面积分和投影关系；圆域极坐标积分。",
      "source_ref": "本文件P04；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-05
```json
{
  "item_package": {
    "item_id": "MV0916B-05",
    "package_version": 1,
    "title": "B组 第5题",
    "stem": "设 $S$ 为曲面\n\\[\ny=1+x^2+z^2,\\qquad x\\ge0,\\quad z\\ge0,\\quad x^2+z^2\\le1,\n\\]\n取法向量 $y$ 分量为负的方向。计算\n\\[\n\\iint_S x\\,dy\\,dz+y\\,dz\\,dx+z\\,dx\\,dy.\n\\]\n写清参数或投影区域、向量面积元及三个有向投影面积元与所用无向参数面积的关系。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "图形曲面参数化；向量面积元和有向投影；第二类曲面积分；圆域积分。",
      "source_ref": "本文件P05；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-06
```json
{
  "item_package": {
    "item_id": "MV0916B-06",
    "package_version": 1,
    "title": "B组 第6题",
    "stem": "设 $L$ 为依次连接\n\\[\nP=(1,0,1),\\qquad Q=(0,2,1),\\qquad R=(0,0,3)\n\\]\n的闭折线，行进方向为 $P\\to Q\\to R\\to P$。计算\n\\[\n\\oint_L (xy+xz)\\,dz.\n\\]\n先说明方法选择及方向依据，再完成计算；若把曲线积分转到曲面上，须明确写出限制到该曲面后的被积表达式与面积元，不能只写转换公式。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "曲线参数化、Stokes条件及方向；三角形参数域与一次多项式二重积分；三角形重心与仿射函数平均关系（可选，非必需）。",
      "source_ref": "本文件P06；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-07
```json
{
  "item_package": {
    "item_id": "MV0916B-07",
    "package_version": 1,
    "title": "B组 第7题",
    "stem": "设 $L$ 是依次连接\n\\[\nA=(2,0,0),\\qquad B=(0,2,0),\\qquad C=(1,1,2)\n\\]\n的闭折线，方向为 $A\\to B\\to C\\to A$。计算\n\\[\n\\oint_L yz\\,dx-xz\\,dy.\n\\]\n先说明方法选择及方向依据，再完成计算；若在曲面上整理被积表达式，须写出每次使用曲面约束的等式。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "曲线参数化、Stokes条件及方向；三角形面积；限制函数到平面。",
      "source_ref": "本文件P07；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-08
```json
{
  "item_package": {
    "item_id": "MV0916B-08",
    "package_version": 1,
    "title": "B组 第8题",
    "stem": "设 $S$ 为球面\n\\[\n(x-1)^2+y^2+z^2=1,\\qquad x\\ge1\n\\]\n的半球面，取相对于球心 $(1,0,0)$ 向外的方向。\n\n（1）求 $F=(x-1,y,z+1)$ 通过 $S$ 的通量。若添加辅助边界，须写明其方向和有向通量。\n\n（2）将向量场换为\n\\[\nH=F+\\frac{(x-\\tfrac32,y,z)}{[(x-\\tfrac32)^2+y^2+z^2]^{3/2}}.\n\\]\n用 $x=1$ 平面的底面封闭 $S$ 后，能否直接在整个半球体上使用散度与边界通量的关系？若不能，说明怎样调整区域、哪些边界必须计入，以及新增边界的方向；不要求算出本问通量。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "Gauss条件及向外方向；开放面与辅助边界；奇点及穿孔区域；半球体积与通量。",
      "source_ref": "本文件P08；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-09
```json
{
  "item_package": {
    "item_id": "MV0916B-09",
    "package_version": 1,
    "title": "C组 第9题",
    "stem": "在 $\\mathbb R^2$ 上定义\n\\[\nf(x,y)=x^2y^2+x^6+y^6+4x^3y^3,\n\\]\n\\[\ng(x,y)=x^2y^2-x^6+y^6+4x^3y^3.\n\\]\n分别求原点处的 Hessian 及其核，给出最低次非零齐次项，并严格判断原点对两函数各是什么类型的点。若有局部极值，说明是否严格；正向结论须给整个邻域内有效的依据，不能只验证若干路径。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "Hessian和矩阵核；齐次多项式；局部极值与鞍点；统一不等式估计及路径反证。",
      "source_ref": "本文件P09；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916B-10
```json
{
  "item_package": {
    "item_id": "MV0916B-10",
    "package_version": 1,
    "title": "C组 第10题",
    "stem": "在 $|x|,|y|<1/4$ 内，令\n\\[\nq=x^2+2y^2,\n\\qquad f(x,y)=e^{q+xy^2}-e^q-xy^2,\n\\qquad \\rho=\\sqrt{x^2+y^2}.\n\\]\n求 $f$ 在原点的最低次非零齐次多项式 $P_m$ 及其次数 $m$，并写成\n\\[\nf=P_m+R.\n\\]\n要求给出尽可能高的整数 $k$，使 $R=O(\\rho^k)$，说明估计对所有趋近方式成立，并判断是否还有 $R=o(\\rho^k)$。解释所选展开阶数为何足够，不只报一个极限数值。",
    "options": [],
    "instructions": "所有变量与参数均为实数，空间采用右手直角坐标系。独立用纸笔完成，不查资料、不使用计算工具；不能完成时保留已有推理，注明中途查阅或提示。每题写“结论＋关键理由＋必要计算”，接受满足公开要求的不同合法路线。\n\n$dS$ 表示无向面积元，$n$ 是所指定方向的单位法向量；第二类曲面积分按该方向解释。$DF$ 的第 $i$ 行第 $j$ 列为 $\\partial F_i/\\partial x_j$，对列向量作用。局部极值相对于函数定义域的完整邻域判断；原点为鞍点指任意邻域都有函数值大于和小于原点值的点。可分组完成，记录实际顺序。",
    "response_requirement": "完成各问，写结论、关键理由及必要计算；证明题给数学链条。",
    "scoring_rule": {
      "fully_acceptable": [
        "完成所有公开要求，满足条件，方向及计算一致；接受不同合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效步骤正确；只评价实际展示的证据。"
      ],
      "unacceptable": [
        "关键推理、对象、条件或方向错误而未修正；仅给无依据结论。"
      ]
    },
    "source_refs": [
      "原创题面，无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "一元指数Taylor展开及余项；复合展开的总次数；O/o的多元定义；统一估计及否定小o的路径证据。",
      "source_ref": "本文件P10；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem及公共instructions"
    }
  ],
  "allowed_tools": [
    "纸笔和本题声明的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
