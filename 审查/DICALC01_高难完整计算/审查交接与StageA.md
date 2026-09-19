# DI-CALC-01 审查交接与Stage A
元信息：批次 DICALC01 | 卷版本 v1 | 更新 2026-09-19 | 状态 independent_validation_pending | 可见性 审查（教师侧，作答前不展示） | 学生卷 `../../题库/DICALC01_高难完整计算/学生卷.md`

先独立审查并封存，再读取解析侧声明；本地未做独立解题验收。

## 允许前置
P-MATH1-CALC-v1；根目录01_高等数学_总入口.md §4.1重积分及直接一元积分前置。以下为工具范围，不是学习者状态：二重积分定限、可加性、对称性、换序、极坐标；分段函数；一元代换、分部积分、有理函数与三角函数定积分。所有题不要求一般多元Jacobian。

## DICALC01-01
```json
{
  "item_package": {
    "item_id": "DICALC01-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "计算\n\\[\nI=\\iint_D\\left(\\frac{x^2y}{3+x}+xe^{y^2}\\right)\\,dx\\,dy,\n\\qquad D=\\{(x,y):x^2+y^2\\le4,\\ y\\ge0\\}.\n\\]",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DICALC01-02
```json
{
  "item_package": {
    "item_id": "DICALC01-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "计算\n\\[\nI=\\int_0^2 dx\\int_0^{\\min\\{x,2-x\\}}(1+x^2)e^{(1-y)^2}\\,dy.\n\\]",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DICALC01-03
```json
{
  "item_package": {
    "item_id": "DICALC01-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "计算\n\\[\nI=\\iint_D\\frac{x^2-y^2}{(x^2+y^2)^3}\\,dx\\,dy,\n\\qquad D=\\{(x,y):1\\le x\\le2,\\ 0\\le y\\le x\\}.\n\\]",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DICALC01-04
```json
{
  "item_package": {
    "item_id": "DICALC01-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "计算\n\\[\nI=\\int_0^1\\int_0^1\\frac{|x-y|}{1+(\\max\\{x,y\\})^2}\\,dx\\,dy.\n\\]\n其中 \\(\\max\\{x,y\\}\\) 表示 \\(x,y\\) 中较大的数。",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DICALC01-05
```json
{
  "item_package": {
    "item_id": "DICALC01-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "设\n\\[\nD_1=\\{(x,y):1\\le x\\le2,\\ 0\\le y\\le1\\},\n\\]\n\\[\nD_2=\\{(x,y):x\\le0,\\ y\\ge0,\\ 1\\le x^2+y^2\\le4\\},\n\\qquad D=D_1\\cup D_2.\n\\]\n计算\n\\[\nI=\\iint_Dxy e^{x^2+y^2}\\,dx\\,dy.\n\\]",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DICALC01-06
```json
{
  "item_package": {
    "item_id": "DICALC01-06",
    "package_version": 1,
    "title": "第6题",
    "stem": "计算\n\\[\nI=\\iint_D\\frac{|x^2-y^2|}{1+x^2+y^2}\\,dx\\,dy,\n\\qquad D=\\{(x,y):x\\ge0,\\ y\\ge0,\\ 1\\le x^2+y^2\\le4\\}.\n\\]",
    "options": [],
    "instructions": "所有变量取实数。独立纸笔作答，每题给出准确结果和完整计算过程，保留必要的区域界限、变换依据与中间步骤；不只写方法名称或积分骨架。方法不限，不要求比较每一种方法；如接受提示，请注明提示发生在哪一步。无需一般多元Jacobian换元，不查答案。",
    "response_requirement": "准确结果＋完整过程＋关键合法性依据",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，界限正确，完整计算与最终结果一致；接受全部合法路线。"
      ],
      "partially_acceptable": [
        "记录完成的正确步骤，分别标记方法断点、计算执行错误与普通书写失误。"
      ],
      "unacceptable": [
        "只写方法或骨架而未完成公开要求，或关键推理不成立。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "本文件允许前置所列普通二重积分及一元积分工具",
      "source_ref": "本文件允许前置；01_高等数学_总入口.md §4.1"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题及公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题显式数学前置"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
