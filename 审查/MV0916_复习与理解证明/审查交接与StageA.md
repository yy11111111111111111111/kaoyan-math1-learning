# MV0916 审查交接与 Stage A
元信息：批次 MV0916 | 卷版本 v1 | 更新 2026-09-16 | 状态 independent_validation_pending | 可见性 审查（封存前只读本文件） | 学生卷 `../../题库/MV0916_复习与理解证明/学生卷.md`


外部审查方先按根目录Validation协议读取本文件，独立完成Stage A并保存记录；之后才读取解析目录的封存Stage B。尚无独立审查记录。以下逐题JSON包含完整题面，公共作答要求按原文复制；不能先打开学情或教师目标说明。

## 前置声明
P-MATH1-CALC-v1的范围绑定根目录01_高等数学_总入口.md §4.1第5—6项；以下P01—P12是本批明确声明的实际允许工具范围，不是对任何学习者的能力判断，也不是声称已核对教材原文。

### P01
多元可微与沿C1曲线求导；欧氏内积与切向量定义。

### P02
可微的线性近似与小o；线性映射的基向量像；叉乘模等于平行四边形面积；曲面面积的局部密度解释。

### P03
参数偏导、二阶行列式、叉乘坐标展开；投影的局部有向面积与无向面积。

### P04
平面Green公式及正向边界；复合求导；C2函数混合偏导相等；旋度定义；曲线积分参数化。

### P05
隐式曲面的梯度法向；单位化；面积投影关系；参数化面积公式；二重积分及极坐标。

### P06
第二类曲面积分定义；平面参数化、叉乘与方向；三角形上的二重积分。

### P07
旋度定义；Stokes公式的光滑性、边界与方向条件；三角形参数化和多项式积分。

### P08
Gauss公式的闭合边界、光滑性及外法向条件；通量线性；分片边界；奇点邻域的区域修改；重积分。

### P09
隐函数定理及可微条件；隐式求导与复合求导；二阶链式求导；梯度和单位方向导数。

### P10
Hessian和矩阵核；局部极值与鞍点定义；半正定二阶判据的局限；多项式配方、不等式与趋近路径。

### P11
一元Taylor及余项；复合展开的总次数；齐次多项式；O和o的定义；多元极限估计。

### P12
第一类重积分；向量场通量、散度、Gauss公式与分片边界；边界方向；直接积分。

## MV0916-01
```json
{
  "item_package": {
    "item_id": "MV0916-01",
    "package_version": 1,
    "title": "A组 第1题",
    "stem": "设 $G\\in C^1(U)$，$U\\subset\\mathbb R^3$ 为开集，$P\\in S=\\{X\\in U:G(X)=c\\}$，且 $\\nabla G(P)\\ne0$。曲面在 $P$ 附近正则；切向量可写为 $v=\\gamma'(0)$，其中 $\\gamma$ 是曲面上的 $C^1$ 曲线，$\\gamma(0)=P$。\n\n证明 $\\nabla G(P)\\cdot v=0$，并解释为什么这给出了曲面的一个法向量。若去掉 $\\nabla G(P)\\ne0$，上述正交等式本身是否仍足以给出法向方向？说明理由。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "多元可微与沿C1曲线求导；欧氏内积与切向量定义。",
      "source_ref": "本文件前置声明 P01；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-02
```json
{
  "item_package": {
    "item_id": "MV0916-02",
    "package_version": 1,
    "title": "A组 第2题",
    "stem": "设 $r:D\\subset\\mathbb R^2\\to\\mathbb R^3$ 是 $C^1$ 单射正则参数化，$D$ 为开集，$(u_0,v_0)\\in D$。从可微定义说明参数小矩形的两条邻边经映射后，为什么一阶近似分别为 $r_u\\Delta u$ 与 $r_v\\Delta v$（偏导在 $(u_0,v_0)$ 处取值）。\n\n由此解释 $Dr$ 两列的含义，并推出局部面积密度及 $dS$ 的表达式。说明你使用的是局部一阶近似，还是把有限曲面片当成精确的平行四边形；无需证明一般曲面面积存在定理。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "可微的线性近似与小o；线性映射的基向量像；叉乘模等于平行四边形面积；曲面面积的局部密度解释。",
      "source_ref": "本文件前置声明 P02；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-03
```json
{
  "item_package": {
    "item_id": "MV0916-03",
    "package_version": 1,
    "title": "A组 第3题",
    "stem": "设 $r(u,v)=(x(u,v),y(u,v),z(u,v))$ 为 $C^1$ 正则参数化，曲面定向与 $r_u\\times r_v$ 一致。记 $dS_x$ 为按有序坐标 $(y,z)$、正法向为 $+x$ 的平面所定义的局部有向投影面积元。\n\n从投影映射 $(u,v)\\mapsto(y,z)$ 的 Jacobian 出发，证明\n\\[\ndS_x=n_x\\,dS,\n\\]\n并说明 $dy\\,dz$ 与向量面积元第一分量的关系。若只求无向投影面积，应怎样修改？若 $n_x=0$，上述局部关系是否失效？",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "参数偏导、二阶行列式、叉乘坐标展开；投影的局部有向面积与无向面积。",
      "source_ref": "本文件前置声明 P03；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-04
```json
{
  "item_package": {
    "item_id": "MV0916-04",
    "package_version": 1,
    "title": "A组 第4题",
    "stem": "设 $D\\subset\\mathbb R^2$ 是有分段光滑边界的有界单连通区域，$r$ 在 $\\overline D$ 的邻域内为 $C^2$，且在 $\\overline D$ 上单射、正则；$S=r(\\overline D)$ 按 $r_u\\times r_v$ 定向。设 $F$ 在 $S$ 的某开邻域内为 $C^1$，$\\partial S$ 的方向由 $\\partial D$ 的平面正向经 $r$ 诱导。\n\n把曲线积分改写到参数平面，利用平面 Green 公式说明\n\\[\n\\oint_{\\partial S}F\\cdot dr\n=\\iint_D(\\nabla\\times F)(r(u,v))\\cdot(r_u\\times r_v)\\,du\\,dv.\n\\]\n要求写出改写后的两个系数和关键求导关系；另解释把 $D$ 分片时内部边界为什么抵消，以及为什么不能任意改变某一片的方向。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "平面Green公式及正向边界；复合求导；C2函数混合偏导相等；旋度定义；曲线积分参数化。",
      "source_ref": "本文件前置声明 P04；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-05
```json
{
  "item_package": {
    "item_id": "MV0916-05",
    "package_version": 1,
    "title": "B组 第5题",
    "stem": "曲面 $S$ 为\n\\[\nx^2+y^2=4z^2,\\qquad 1\\le z\\le2,\\quad x\\ge0,\\ y\\ge0.\n\\]\n计算 $\\iint_S z\\,dS$。写出从隐式方程得到的单位法向量（两侧任选其一），选一个投影平面并说明 $dS$ 与投影面积元的关系，再写清积分区域、完成计算。可以使用参数化辅助计算，但需保留前述投影关系。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "隐式曲面的梯度法向；单位化；面积投影关系；参数化面积公式；二重积分及极坐标。",
      "source_ref": "本文件前置声明 P05；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-06
```json
{
  "item_package": {
    "item_id": "MV0916-06",
    "package_version": 1,
    "title": "B组 第6题",
    "stem": "设 $S$ 为平面 $x+2y+z=2$ 在第一卦限内的三角形部分，取单位法向量的 $x$ 分量为负的方向。计算\n\\[\n\\iint_S x\\,dy\\,dz+y\\,dz\\,dx+z\\,dx\\,dy.\n\\]\n写明所用参数或投影区域，以及三个有向面积元的表示。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "第二类曲面积分定义；平面参数化、叉乘与方向；三角形上的二重积分。",
      "source_ref": "本文件前置声明 P06；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-07
```json
{
  "item_package": {
    "item_id": "MV0916-07",
    "package_version": 1,
    "title": "B组 第7题",
    "stem": "设 $A=(1,0,0)$、$B=(0,2,0)$、$C=(0,0,3)$，闭折线 $L$ 按 $A\\to B\\to C\\to A$ 行进。计算\n\\[\n\\oint_L y^2\\,dx+z^2\\,dy+x^2\\,dz.\n\\]\n本题要求写出对应向量场及其旋度，自选以 $L$ 为边界的曲面，给出参数化、参数区域与匹配方向，并据此完成积分。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "旋度定义；Stokes公式的光滑性、边界与方向条件；三角形参数化和多项式积分。",
      "source_ref": "本文件前置声明 P07；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-08
```json
{
  "item_package": {
    "item_id": "MV0916-08",
    "package_version": 1,
    "title": "B组 第8题",
    "stem": "设 $S$ 为 $z=2-x^2-y^2$ 位于 $z\\ge0$ 的部分，取法向量 $z$ 分量为正的方向。\n\n（1）计算向量场 $F=(x,y,z+1)$ 通过 $S$ 的通量；若引入辅助边界，需写清其方向和对结果的贡献。\n\n（2）将向量场换成\n\\[\nH=F+\\frac{(x,y,z-1)}{[x^2+y^2+(z-1)^2]^{3/2}}.\n\\]\n将 $S$ 与其在 $z=0$ 平面内的底面组成封闭边界后，能否直接在整个所围立体上应用散度与边界通量的公式？若不能，说明可以怎样调整积分区域、新边界及其方向；此问不要求计算最终通量。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "Gauss公式的闭合边界、光滑性及外法向条件；通量线性；分片边界；奇点邻域的区域修改；重积分。",
      "source_ref": "本文件前置声明 P08；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-09
```json
{
  "item_package": {
    "item_id": "MV0916-09",
    "package_version": 1,
    "title": "B组 第9题",
    "stem": "方程\n\\[\nz+z^3+xy-2x-y=0\n\\]\n在 $(0,0,0)$ 附近确定 $z=z(x,y)$。\n\n（1）说明局部隐函数存在且可微的依据，并求一般点处 $z_x$ 的表达式。\n\n（2）令 $w(t)=z(t,t^2)$，求 $w'(0)$ 与 $w''(0)$。\n\n（3）求 $z$ 在 $(0,0)$ 处沿向量 $(3,4)$ 所指方向的方向导数。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "隐函数定理及可微条件；隐式求导与复合求导；二阶链式求导；梯度和单位方向导数。",
      "source_ref": "本文件前置声明 P09；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-10
```json
{
  "item_package": {
    "item_id": "MV0916-10",
    "package_version": 1,
    "title": "C组 第10题",
    "stem": "设\n\\[\nf_a(x,y)=x^2+2xy^2+a y^4+y^6,\\qquad (x,y)\\in\\mathbb R^2.\n\\]\n求原点的 Hessian 矩阵及其核；分别对 $a=0,1,2$，严格判断原点是否为局部极小、局部极大或鞍点，并在有极值时说明是否严格。你的依据应控制整个邻域，或给出足以否定极值的证据，不能只列有限条直线的试算。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "Hessian和矩阵核；局部极值与鞍点定义；半正定二阶判据的局限；多项式配方、不等式与趋近路径。",
      "source_ref": "本文件前置声明 P10；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-11
```json
{
  "item_package": {
    "item_id": "MV0916-11",
    "package_version": 1,
    "title": "C组 第11题",
    "stem": "在 $|x|,|y|<1/4$ 内，令\n\\[\nu=x^2+y^2+xy^2,\\qquad\nf(x,y)=\\ln(1+u)-u+\\frac12u^2,\\qquad\n\\rho=\\sqrt{x^2+y^2}.\n\\]\n求 $f$ 在原点展开的最低次非零齐次多项式，写出相应余项的阶，并求\n\\[\n\\lim_{(x,y)\\to(0,0)}\\frac{f(x,y)}{\\rho^6}.\n\\]\n说明外层函数需要保留到哪一阶，以及代入内层量后为什么可以舍去其他项。",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "一元Taylor及余项；复合展开的总次数；齐次多项式；O和o的定义；多元极限估计。",
      "source_ref": "本文件前置声明 P11；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## MV0916-12
```json
{
  "item_package": {
    "item_id": "MV0916-12",
    "package_version": 1,
    "title": "C组 第12题",
    "stem": "设 $V=[0,1]^3$，$S$ 由 $\\partial V$ 去掉底面 $z=0$ 后的五个面组成，方向均向 $V$ 外。令\n\\[\nF=(x+\\sin(yz),\\ y+e^{xz},\\ z+xy).\n\\]\n先用2—3行说明你的方法选择理由，再计算\n\\[\n\\iint_S F\\cdot n\\,dS.\n\\]",
    "options": [],
    "instructions": "所有变量、参数及向量均取实数。独立作答，不查资料、不使用计算工具；遗忘或无法完成处如实保留已经建立的步骤。每题写“结论＋关键理由＋必要计算”，接受所有满足题意的合法路线。\n\n三维空间采用右手直角坐标系；单位法向量记为 $n$，$dS$ 为无向面积元。第二类曲面积分中的 $dy\\,dz,dz\\,dx,dx\\,dy$ 按所给方向解释为有向投影面积元。方向导数按单位方向定义。证明题写出核心数学链条，通常4—8行即可，必要时可增加；不能仅引用待证明的结论。\n\n可分组完成，并记下实际作答顺序；中途若查看讲解，在相应题旁注明。",
    "response_requirement": "完整完成题面各问，写结论、关键理由与必要计算；证明题须有推理链。",
    "scoring_rule": {
      "fully_acceptable": [
        "满足公开各问，条件、对象、方向及计算一致；接受所有合法路线。"
      ],
      "partially_acceptable": [
        "部分子问或有效中间步骤正确；仅记录实际展示的内容。"
      ],
      "unacceptable": [
        "仅给无依据结论；关键逻辑、必要条件或方向错误且未修正。"
      ]
    },
    "source_refs": [
      "原创；无外部原题或答案依赖。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "第一类重积分；向量场通量、散度、Gauss公式与分片边界；边界方向；直接积分。",
      "source_ref": "本文件前置声明 P12；入口范围§4.1第5—6项"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题stem、instructions、response_requirement及scoring_rule"
    }
  ],
  "allowed_tools": [
    "纸笔；本题前置声明中允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
