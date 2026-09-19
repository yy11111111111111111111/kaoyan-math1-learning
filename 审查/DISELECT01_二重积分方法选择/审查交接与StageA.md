# DISELECT01 审查交接与Stage A
元信息：批次 DISELECT01 | 卷版本 v1 | 更新 2026-09-18 | 状态 independent_validation_pending | 可见性 审查（先独立审查并封存） | 学生卷 `../../题库/DISELECT01_二重积分方法选择/学生卷.md`

本文件仅含完整Q与允许前置，不含学情、生成目标或解答。本地未独立解题验收；外部审查方按根目录Validation协议先执行Stage A并封存，再读解析目录声明。正式作答要求是方法判断及最少预演，不得自行增加完整计算或最终数值的评分要求。

## 允许前置
profile=P-MATH1-CALC-v1；范围依据根目录01_高等数学_总入口.md §4.1重积分及直接一元积分前置。P01—P08为本批实际允许工具的显式声明，不是学生已掌握的断言；一般多元Jacobian不作必要工具。

### P01
二重积分、Fubini与换次序；平面三角形定限；指数函数和一元代换。

### P02
圆域定限；直角坐标与极坐标积分；有理函数的一元积分。

### P03
二重积分线性性；区域的交换对称及面积保持；指数函数积分。

### P04
极坐标；圆环；对数函数积分；一元代换。

### P05
三角形定限及分段；积分次序；指数函数与一元代换。

### P06
圆与正方形交域；极坐标及角度分段；幂函数与三角函数积分。

### P07
区域对称映射与面积保持；二重积分线性性；极坐标；指数函数积分。

### P08
绝对值分段；区域交换对称；矩形与极坐标定限；三角函数和有理函数积分。

## DISELECT01-01
```json
{
  "item_package": {
    "item_id": "DISELECT01-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "\\[\nI=\\int_0^1 dx\\int_x^1 e^{y^2}\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "二重积分、Fubini与换次序；平面三角形定限；指数函数和一元代换。",
      "source_ref": "本文件P01；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-02
```json
{
  "item_package": {
    "item_id": "DISELECT01-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "\\[\nI=\\iint_D\\frac{x}{1+y^2}\\,dx\\,dy,\n\\qquad D=\\{(x,y):x\\ge0,\\ y\\ge0,\\ x^2+y^2\\le1\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "圆域定限；直角坐标与极坐标积分；有理函数的一元积分。",
      "source_ref": "本文件P02；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-03
```json
{
  "item_package": {
    "item_id": "DISELECT01-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "\\[\nI=\\int_0^1\\int_0^1\\frac{e^x}{e^x+e^y}\\,dx\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "二重积分线性性；区域的交换对称及面积保持；指数函数积分。",
      "source_ref": "本文件P03；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-04
```json
{
  "item_package": {
    "item_id": "DISELECT01-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "\\[\nI=\\iint_D\\frac{\\ln(1+x^2+y^2)}{1+x^2+y^2}\\,dx\\,dy,\n\\qquad D=\\{(x,y):x\\ge0,\\ y\\ge0,\\ 1\\le x^2+y^2\\le4\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "极坐标；圆环；对数函数积分；一元代换。",
      "source_ref": "本文件P04；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-05
```json
{
  "item_package": {
    "item_id": "DISELECT01-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "$D$ 是顶点为 $(0,0)$、$(2,0)$、$(1,1)$ 的闭三角形区域。\n\\[\nI=\\iint_D e^{(1-y)^2}\\,dx\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "三角形定限及分段；积分次序；指数函数与一元代换。",
      "source_ref": "本文件P05；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-06
```json
{
  "item_package": {
    "item_id": "DISELECT01-06",
    "package_version": 1,
    "title": "第6题",
    "stem": "\\[\nI=\\iint_D\\frac{1}{(x^2+y^2)^{3/2}}\\,dx\\,dy,\n\\qquad D=\\{(x,y):0\\le x\\le1,\\ 0\\le y\\le1,\\ x^2+y^2\\ge1\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "圆与正方形交域；极坐标及角度分段；幂函数与三角函数积分。",
      "source_ref": "本文件P06；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-07
```json
{
  "item_package": {
    "item_id": "DISELECT01-07",
    "package_version": 1,
    "title": "第7题",
    "stem": "\\[\nI=\\iint_D\\left[(x-y)e^{(x+y)^2}+e^{x^2+y^2}\\right]dx\\,dy,\n\\]\n\\[\nD=\\{(x,y):1\\le x^2+y^2\\le4,\\ x+y\\ge0\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "区域对称映射与面积保持；二重积分线性性；极坐标；指数函数积分。",
      "source_ref": "本文件P07；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```

## DISELECT01-08
```json
{
  "item_package": {
    "item_id": "DISELECT01-08",
    "package_version": 1,
    "title": "第8题",
    "stem": "\\[\nI=\\int_1^2\\int_1^2\\frac{|x^2-y^2|}{x^2+y^2}\\,dx\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断方法，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写一段简短方案，包含：\n\n- 你选择的路线，以及它为什么值得优先尝试；\n- 与另一条你认为可能的路线比较，具体指出复杂度差在哪里；\n- 写出足以支持判断的积分骨架，预判完成内层后还会剩下什么一维积分、能否用常用方法处理，然后停止。不必算出原函数；若你的路线已能直接确定积分，则只写依据，不为凑步骤继续积分。\n\n只报方法名称不够，不要求证明自己的方案是唯一或全局最优。可以画区域草图，可以组合方法；无需一般多元Jacobian换元。不要查阅解答，中途接受提示时注明。",
    "response_requirement": "选定路线，与自选一条候选比较，给足以支持判断的积分骨架和一维尾项可处理性；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "所选路线合法，区域与函数表示一致；比较有具体依据；预演足以说明余下积分可处理，或有合法直接判定依据。",
        "接受多个同样合理的方案，不要求唯一最优；不以未算最终数值扣分。"
      ],
      "partially_acceptable": [
        "路线合理但区域/尾项预判不完整，保留实际正确部分。"
      ],
      "unacceptable": [
        "只报名称，无理由；忽视条件或区域变化；声称简化却未识别余下积分障碍。"
      ]
    },
    "source_refs": [
      "原创训练，无指定外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "绝对值分段；区域交换对称；矩形与极坐标定限；三角函数和有理函数积分。",
      "source_ref": "本文件P08；入口§4.1重积分及直接前置"
    }
  ],
  "convention_bindings": [
    {
      "convention_id": "C-ITEM-EXPLICIT-v1",
      "source_ref": "本题与公共作答要求"
    }
  ],
  "allowed_tools": [
    "纸笔及本题明确允许的数学工具"
  ],
  "declaration_set_version": "MATH-ITEM-DECL-v1.0.0"
}
```
