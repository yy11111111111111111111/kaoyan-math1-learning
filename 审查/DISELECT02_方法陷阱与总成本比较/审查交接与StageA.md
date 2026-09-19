# DISELECT02 审查交接与Stage A
元信息：批次 DISELECT02 | 卷版本 v1 | 更新 2026-09-18 | 状态 independent_validation_pending | 可见性 审查（先独立审查并封存） | 学生卷 `../../题库/DISELECT02_方法陷阱与总成本比较/学生卷.md`

完整Q及允许前置如下。外部审查先按根目录Validation协议独立执行并封存Stage A，再读解析侧目标声明；本地未实施独立数学验收。只评路线与最少预演，不增加完整计算或最终值要求。

## 允许前置
profile=P-MATH1-CALC-v1；范围依据为根目录01_高等数学_总入口.md §4.1重积分与直接一元积分前置。P01—P06为本批显式允许工具范围，不是学生能力断言；无需一般多元Jacobian。

### P01
圆域定限；直角坐标、极坐标；一元有理函数积分。

### P02
二重积分换次序；抛物线区域；幂函数、指数函数及一元代换。

### P03
平面直线与角度区域；极坐标；有理/三角函数积分和一元代换。

### P04
区域对称及面积保持；积分线性性；圆环分段；极坐标和积分次序；指数积分。

### P05
区域可加性；矩形与圆域定限；直角坐标、极坐标及一元代换；积分符号控制。

### P06
最大值分段；交换对称；二重积分定限及换次序；指数函数与一元代换。

## DISELECT02-01
```json
{
  "item_package": {
    "item_id": "DISELECT02-01",
    "package_version": 1,
    "title": "第1题",
    "stem": "\\[\nI=\\iint_D\\frac{y}{2+x}\\,dx\\,dy,\n\\qquad D=\\{(x,y):x^2+y^2\\le1,\\ y\\ge0\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "圆域定限；直角坐标、极坐标；一元有理函数积分。",
      "source_ref": "本文件P01；入口§4.1及直接前置"
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

## DISELECT02-02
```json
{
  "item_package": {
    "item_id": "DISELECT02-02",
    "package_version": 1,
    "title": "第2题",
    "stem": "\\[\nI=\\int_0^1 dx\\int_{x^2}^1 x^3e^{y^3}\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "二重积分换次序；抛物线区域；幂函数、指数函数及一元代换。",
      "source_ref": "本文件P02；入口§4.1及直接前置"
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

## DISELECT02-03
```json
{
  "item_package": {
    "item_id": "DISELECT02-03",
    "package_version": 1,
    "title": "第3题",
    "stem": "\\[\nI=\\iint_D\\frac{x^2}{(x^2+y^2)^2}\\,dx\\,dy,\n\\qquad D=\\{(x,y):1\\le x\\le2,\\ 0\\le y\\le x\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "平面直线与角度区域；极坐标；有理/三角函数积分和一元代换。",
      "source_ref": "本文件P03；入口§4.1及直接前置"
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

## DISELECT02-04
```json
{
  "item_package": {
    "item_id": "DISELECT02-04",
    "package_version": 1,
    "title": "第4题",
    "stem": "\\[\nI=\\iint_D\\left(ye^{x^2}+xe^y\\right)dx\\,dy,\n\\qquad D=\\{(x,y):1\\le x^2+y^2\\le4,\\ x\\ge0\\}.\n\\]",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "区域对称及面积保持；积分线性性；圆环分段；极坐标和积分次序；指数积分。",
      "source_ref": "本文件P04；入口§4.1及直接前置"
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

## DISELECT02-05
```json
{
  "item_package": {
    "item_id": "DISELECT02-05",
    "package_version": 1,
    "title": "第5题",
    "stem": "积分区域由下面两部分合在一起：\n\\[\nD=\\{(x,y):1\\le x\\le2,\\ 0\\le y\\le1\\}\n\\ \\cup\\ \n\\{(x,y):x\\le0,\\ y\\ge0,\\ x^2+y^2\\le1\\}.\n\\]\n\\[\nI=\\iint_D xy\\,e^{x^2+y^2}\\,dx\\,dy.\n\\]",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "区域可加性；矩形与圆域定限；直角坐标、极坐标及一元代换；积分符号控制。",
      "source_ref": "本文件P05；入口§4.1及直接前置"
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

## DISELECT02-06
```json
{
  "item_package": {
    "item_id": "DISELECT02-06",
    "package_version": 1,
    "title": "第6题",
    "stem": "\\[\nI=\\int_0^1\\int_0^1\n\\max\\{x,y\\}\\,e^{(\\max\\{x,y\\})^3}\\,dx\\,dy.\n\\]\n其中 $\\max\\{x,y\\}$ 表示 $x,y$ 中较大的一个。",
    "options": [],
    "instructions": "本组只判断路线，不要求完整计算或最终数值。所有变量取实数，独立纸笔作答。\n\n每题写出你优先采用的路线，并与另一条你认为可能的路线作具体比较。给出足以支持判断的区域、积分骨架和最后一维积分的预期形式，说明还有什么运算要做，然后停止；不必求出原函数。\n\n只报方法名称不够，也不要求证明自己的路线唯一最优。允许组合方法、分别处理不同部分；如有成本相当的方案，可以并列并说明理由。无需一般多元Jacobian换元，不查答案，接受提示时注明。",
    "response_requirement": "路线、具体比较、积分骨架及最后一维积分预判；不完整计算。",
    "scoring_rule": {
      "fully_acceptable": [
        "路线合法，区域与函数处理一致，比较具体，尾项预判能支撑成本判断。",
        "接受不同或成本相当的方案；不得因与生成者偏好不同而判错。"
      ],
      "partially_acceptable": [
        "方法方向正确但预演未闭环，记录缺失环节，不泛化为方法不会。"
      ],
      "unacceptable": [
        "只凭表面标签作选择；区域/函数处理不成立；未识别所选路线的实际尾项障碍。"
      ]
    },
    "source_refs": [
      "原创候选；无外部题目来源。"
    ]
  },
  "prerequisite_profile": "P-MATH1-CALC-v1",
  "required_prerequisites": [
    {
      "nodes": "最大值分段；交换对称；二重积分定限及换次序；指数函数与一元代换。",
      "source_ref": "本文件P06；入口§4.1及直接前置"
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
