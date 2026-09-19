# DIIMPROPER01 审查交接与Stage A
元信息：批次 DIIMPROPER01 | 卷版本 v1 | 更新 2026-09-19 | 状态 independent_validation_pending | 可见性 审查（教师侧，学生作答前不展示） | 学生卷 `../../题库/DIIMPROPER01_反常二重积分与可积性/学生卷.md`

先按Validation协议独立审查并封存，再解封解析侧；本地未独立解题验收。

## 允许前置
P-MATH1-CALC-v1，绑定01_高等数学_总入口.md §4.1一元积分与重积分；普通二重积分、对称性、极坐标、比较不等式、实幂及一元反常积分。反常二重积分与变号函数的本卷约定由公共要求显式提供；不要求一般Jacobian或测度论。

## DIIMPROPER01-01
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "分别求下列函数在其定义域各连通区间上的原函数，并用求导核对：\n\\[\n\\frac1{4-x^2},\\qquad \\frac1{4+x^2}.\n\\]\n再计算 \\(\\displaystyle\\int_0^1\\frac{dx}{4-x^2}\\)。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-02
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "设 \\(p\\in\\mathbb R\\)，\\(D=\\{(x,y):0<x^2+y^2<1\\}\\)。判断\n\\[\n\\iint_D\\frac{dx\\,dy}{(x^2+y^2)^{p/2}}\n\\]\n何时有限；有限时求其值。写出你使用的截断区域与极限。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-03
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "设 \\(p\\in\\mathbb R\\)，\\(D=\\{(x,y):x^2+y^2>1\\}\\)。判断\n\\[\n\\iint_D\\frac{dx\\,dy}{(x^2+y^2)^{p/2}}\n\\]\n何时有限；有限时求其值。写出截断区域与极限。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-04
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "设 \\(p,q\\in\\mathbb R\\)。求使下列积分有限的全部参数条件：\n\\[\n\\iint_{\\mathbb R^2\\setminus\\{(0,0)\\}}\n\\frac{dx\\,dy}{(x^2+y^2)^{p/2}(1+x^2+y^2)^{q/2}}.\n\\]\n不要求求出积分值；需说明每条条件分别控制哪一部分区域。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-05
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "设 \\(p\\in\\mathbb R\\)，\\(D=\\{(x,y):0<x<1,\\ 0<y<x^2\\}\\)。判断\n\\[\n\\iint_D\\frac{dx\\,dy}{x^p}\n\\]\n何时有限；有限时求其值。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-06
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-06",
    "package_version": 1,
    "title": "第6题",
    "stem": "设 \\(p\\in\\mathbb R\\)，\\(D=\\{(x,y):x^2+y^2<1\\}\\)。判断\n\\[\n\\iint_D\\frac{dx\\,dy}{(1-x^2-y^2)^p}\n\\]\n何时有限；有限时求其值，并指出需要截断的位置。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-07
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-07",
    "package_version": 1,
    "title": "第7题",
    "stem": "设 \\(p\\in\\mathbb R\\)，\\(D=\\{(x,y):x>1,\\ 0<y<1/x\\}\\)。求使\n\\[\n\\iint_D\\frac{dx\\,dy}{(x^2+y^2)^{p/2}}\n\\]\n有限的全部 \\(p\\)，不要求积分值；给出对整个相关区域有效的依据。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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

## DIIMPROPER01-08
```json
{
  "item_package": {
    "item_id": "DIIMPROPER01-08",
    "package_version": 1,
    "title": "第8题",
    "stem": "设\n\\[\nf(x,y)=\\frac{x^2-y^2}{(x^2+y^2)^2},\\qquad\nD=\\{(x,y):0<x^2+y^2<1\\}.\n\\]\n（1）求 \\(\\displaystyle\\lim_{\\varepsilon\\downarrow0}\\iint_{\\varepsilon^2<x^2+y^2<1}f(x,y)\\,dx\\,dy\\)。\n\n（2）判断 \\(\\displaystyle\\iint_D|f(x,y)|\\,dx\\,dy\\) 是否有限，并据本卷约定判断 \\(\\iint_D f\\) 是否存在有限积分。\n\n（3）求 \\(\\displaystyle\\lim_{\\varepsilon\\downarrow0}\\iint_{E_\\varepsilon}f(x,y)\\,dx\\,dy\\)，其中\n\\[\nE_\\varepsilon=\\left\\{(x,y):x^2+y^2<1,\\quad \\frac{x^2}{4}+y^2>\\varepsilon^2\\right\\},\\qquad 0<\\varepsilon<\\tfrac12.\n\\]\n比较（1）与（3），说明结果支持什么结论。",
    "options": [],
    "instructions": "所有变量与参数取实数，\\(\\ln\\) 为自然对数。写出结论、必要计算与依据；方法不限，无需一般多元Jacobian换元。不附答案，接受提示时注明发生在哪一步。\n\n本卷第2—8题使用如下定义：对非负函数，先在避开奇点、有界的子区域上作普通二重积分，再让这些区域逐步扩大并覆盖原区域；积分值的极限若有限，称该反常积分有限，否则记为 \\(+\\infty\\)。对本卷涉及的变号函数，“存在有限积分”指绝对值积分有限；仅某一种截断方式下的带符号极限，按该截断方式单独报告，不直接等同于这里的有限积分。\n\n若这些定义尚未学习，请先由教学方说明定义及截断操作，再分题作答；已接受的讲解不作为无提示发现的证据。",
    "response_requirement": "按题面给出参数条件/结果、截断或比较依据及必要计算",
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
      "nodes": "本文件允许前置及题面给出的定义",
      "source_ref": "本文件允许前置；公共要求；01_高等数学_总入口.md §4.1"
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
