# SERIESSTAGE01 审查交接与Stage A
元信息：批次 SERIESSTAGE01 | 卷版本 v1 | 更新 2026-09-19 | 状态 independent_validation_pending | 可见性 审查（先独立审查并封存） | 学生卷 `../../题库/SERIESSTAGE01_无穷级数阶段题组/学生卷.md`

外部审查先仅使用本文件的完整Q/P/C/A及根目录Validation协议，独立求解并封存Stage A；然后才可读取解析侧封存设计声明。本地未执行独立数学验收，以下评分规则只描述公开作答的可观察质量，不含答案键。

## 允许前置

profile=P-MATH1-CALC-v1；领域入口为 `../../01_高等数学_总入口.md` §4.1 的级数范围，单题直接前置如下；P01—P05是审查声明，不是学习者已掌握的判断。约定均写在题面和公共作答要求中。

### P01
实级数收敛与Cauchy判据；复数等比有限和或等价三角恒等式；部分和与单调衰减的基本关系。

### P02
数列最终单调、总变差及正项级数比较；有界部分和与衰减权重的关系；级数线性性。

### P03
部分和、离散分部求和恒等式；单调权重差分和望远镜估计；级数尾和。

### P04
部分和与离散分部求和；幂函数差分或等价估计；正项p级数比较及尾估计。

### P05
部分和与项的差分对应；离散分部求和；对数临界级数的基本敛散性；条件收敛的基本例子。

## SERIESSTAGE01-01
```json
{
  "item_package": {
    "item_id": "SERIESSTAGE01-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "判断下列级数是否收敛，并写出支撑判断的关键依据：\n\\[\n\\sum_{n=1}^{\\infty}\\frac{\\cos(2n)}{\\sqrt n}.\n\\]\n这里的角度以弧度计。",
    "options": [],
    "instructions": "本卷共5题。所有数列及参数取实数，\\(\\log\\) 为自然对数；含 \\(\\log n\\) 的级数从 \\(n=3\\) 起求和，其余按题面给定的起点。每题写结论与关键依据；要求证明的题须写出足以支撑结论的关键估计。独立纸笔作答；若参考材料或获得提示，请在相应题旁注明。",
    "response_requirement": "题面所问的结论及关键依据；证明题写出关键估计。",
    "scoring_rule": {
      "fully_acceptable": [
        "敛散结论与理由完整，说明所用累计量的控制和权重条件，接受所有合法路线。"
      ],
      "partially_acceptable": [
        "结论正确但关键累计控制或权重条件未说明。"
      ],
      "unacceptable": [
        "只凭正负号交替或项趋零直接作出结论。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "实级数收敛与Cauchy判据；复数等比有限和或等价三角恒等式；部分和与单调衰减的基本关系。",
      "source_ref": "本文件P01；../../01_高等数学_总入口.md §4.1级数范围及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔与本题显式允许的数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## SERIESSTAGE01-02
```json
{
  "item_package": {
    "item_id": "SERIESSTAGE01-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "设 \\(a_n=(-1)^n\\)，\n\\[\nb_n=\\frac1n+\\frac{(-1)^n}{n^2}\\qquad(n\\ge1).\n\\]\n判断 \\(b_n\\) 是否最终单调、是否满足 \\(\\sum_{n=1}^{\\infty}|b_{n+1}-b_n|<\\infty\\)，并判断 \\(\\sum_{n=1}^{\\infty}a_nb_n\\) 的敛散性。写出关键依据。",
    "options": [],
    "instructions": "本卷共5题。所有数列及参数取实数，\\(\\log\\) 为自然对数；含 \\(\\log n\\) 的级数从 \\(n=3\\) 起求和，其余按题面给定的起点。每题写结论与关键依据；要求证明的题须写出足以支撑结论的关键估计。独立纸笔作答；若参考材料或获得提示，请在相应题旁注明。",
    "response_requirement": "题面所问的结论及关键依据；证明题写出关键估计。",
    "scoring_rule": {
      "fully_acceptable": [
        "分别处理所问条件及级数敛散，理由足以支持每个判断；接受合法的等价路线。"
      ],
      "partially_acceptable": [
        "只给出级数结论，或未分别处理最终单调和变差问题。"
      ],
      "unacceptable": [
        "仅凭权重趋零断言乘积级数收敛；对条件作出未经论证的判断。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "数列最终单调、总变差及正项级数比较；有界部分和与衰减权重的关系；级数线性性。",
      "source_ref": "本文件P02；../../01_高等数学_总入口.md §4.1级数范围及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔与本题显式允许的数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## SERIESSTAGE01-03
```json
{
  "item_package": {
    "item_id": "SERIESSTAGE01-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "对 \\(m=0,1,2,\\ldots\\) 定义\n\\[\na_{3m+1}=1,\\qquad a_{3m+2}=1,\\qquad a_{3m+3}=-2.\n\\]\n用离散分部求和写出有限尾段的关系式，并证明存在与 \\(p\\) 无关的常数 \\(C>0\\)，使每个整数 \\(p\\ge1\\) 都满足\n\\[\n\\left|\\sum_{n=p}^{\\infty}\\frac{a_n}{\\sqrt n}\\right|\\le\\frac{C}{\\sqrt p}.\n\\]",
    "options": [],
    "instructions": "本卷共5题。所有数列及参数取实数，\\(\\log\\) 为自然对数；含 \\(\\log n\\) 的级数从 \\(n=3\\) 起求和，其余按题面给定的起点。每题写结论与关键依据；要求证明的题须写出足以支撑结论的关键估计。独立纸笔作答；若参考材料或获得提示，请在相应题旁注明。",
    "response_requirement": "题面所问的结论及关键依据；证明题写出关键估计。",
    "scoring_rule": {
      "fully_acceptable": [
        "有限尾段关系及边界指标正确，并以与上端点无关的界推出所要求的无穷尾和估计。"
      ],
      "partially_acceptable": [
        "累计控制正确，但边界项或有限到无穷尾段的过渡缺失。"
      ],
      "unacceptable": [
        "只写出目标估计而未给出足以验证的有限尾段论证。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "部分和、离散分部求和恒等式；单调权重差分和望远镜估计；级数尾和。",
      "source_ref": "本文件P03；../../01_高等数学_总入口.md §4.1级数范围及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔与本题显式允许的数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## SERIESSTAGE01-04
```json
{
  "item_package": {
    "item_id": "SERIESSTAGE01-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "设实数列 \\(a_n\\) 的部分和 \\(A_N=\\sum_{n=1}^{N}a_n\\) 满足\n\\[\n|A_N|\\le C N^{2/5}\\qquad(N\\ge1),\n\\]\n其中 \\(C>0\\) 与 \\(N\\) 无关。证明 \\(\\sum_{n=1}^{\\infty}a_n/n^{3/5}\\) 收敛，并给出其从 \\(n=p\\) 开始的尾和关于 \\(p\\) 的数量级上界。",
    "options": [],
    "instructions": "本卷共5题。所有数列及参数取实数，\\(\\log\\) 为自然对数；含 \\(\\log n\\) 的级数从 \\(n=3\\) 起求和，其余按题面给定的起点。每题写结论与关键依据；要求证明的题须写出足以支撑结论的关键估计。独立纸笔作答；若参考材料或获得提示，请在相应题旁注明。",
    "response_requirement": "题面所问的结论及关键依据；证明题写出关键估计。",
    "scoring_rule": {
      "fully_acceptable": [
        "收敛论证同时控制边界项和差分尾项，尾和数量级有可检查的依据。"
      ],
      "partially_acceptable": [
        "识别出可用的增长与衰减关系，但边界项或尾和估计缺失。"
      ],
      "unacceptable": [
        "由部分和增长上界直接声称原级数收敛，未处理带权和。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "部分和与离散分部求和；幂函数差分或等价估计；正项p级数比较及尾估计。",
      "source_ref": "本文件P04；../../01_高等数学_总入口.md §4.1级数范围及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔与本题显式允许的数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## SERIESSTAGE01-05
```json
{
  "item_package": {
    "item_id": "SERIESSTAGE01-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "设实数列 \\(a_n\\) 的部分和 \\(A_N=\\sum_{n=1}^{N}a_n\\) 满足\n\\[\n|A_N|\\le C\\sqrt N\\qquad(N\\ge1),\n\\]\n其中常数 \\(C>0\\) 可随数列而变，但不随 \\(N\\) 变化。对\n\\[\nT_s=\\sum_{n=3}^{\\infty}\\frac{a_n}{\\sqrt n\\,(\\log n)^s},\n\\]\n分别判断当 \\(s=2\\) 与 \\(s=1\\) 时，仅凭给定的部分和上界能否保证收敛。对于 \\(s=1\\)，请给出两个都满足该上界、但敛散结果不同的实数列 \\(a_n\\)，并说明它们为何满足要求。",
    "options": [],
    "instructions": "本卷共5题。所有数列及参数取实数，\\(\\log\\) 为自然对数；含 \\(\\log n\\) 的级数从 \\(n=3\\) 起求和，其余按题面给定的起点。每题写结论与关键依据；要求证明的题须写出足以支撑结论的关键估计。独立纸笔作答；若参考材料或获得提示，请在相应题旁注明。",
    "response_requirement": "题面所问的结论及关键依据；证明题写出关键估计。",
    "scoring_rule": {
      "fully_acceptable": [
        "分别说明两种参数的保证范围，两个例子均满足相同部分和上界且各自敛散结论有依据。"
      ],
      "partially_acceptable": [
        "能识别临界但仅给出一种情况，或例子缺少部分和上界/敛散核对。"
      ],
      "unacceptable": [
        "把充分估计失效直接当成任意具体级数发散的证明。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "部分和与项的差分对应；离散分部求和；对数临界级数的基本敛散性；条件收敛的基本例子。",
      "source_ref": "本文件P05；../../01_高等数学_总入口.md §4.1级数范围及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔与本题显式允许的数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
