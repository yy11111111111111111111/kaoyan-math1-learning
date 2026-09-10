# 数学题 Generation Specification

> 版本：1.1.0  
> 依赖：`数学出题_共享声明集.md`、`数学题_Validation_Protocol.md`  
> 职责：利用当前学习目标和学生状态生成候选 item package，并把可盲验收的 Stage A packet 与 sealed Stage B packet 分开。  
> Generation 的自评只用于塑形和淘汰明显失败候选，不构成 Structural Validation 证据。

## 1. Generation 的权限边界

Generation 可以读取：

- 当前学习目标；
- 当前学生行为状态 $s_u$；
- 已学、未学和状态未知的节点；
- 当前训练目的与 administration context；
- 当前提供的 Error Log 和经 00 筛选的相关 user-active model；
- 允许前置 profile $P$、Convention $C$ 与已注册 claim $\mathcal K$。

Generation 不得：

- 自己宣布目标 claim 已通过；
- 把 $P$ 与 $s_u$ 合并成一个 `prerequisites` 字段；
- 在题目写完后才倒推 measurement claim；
- 临时发明未注册 claim、约定或错误模型；
- 把 `not_found` 写成“唯一、无泄露、没有其他路线”；
- 根据题面估计群体答对率或 empirical difficulty；
- 把一次当前错误直接写成 `M_user-active`；
- 把某条 generator route 的决策数写成 item-level 必要结构。

## 2. 固定生成顺序

```text
确认交付对象与当前授权
→ 绑定当前节点或题组覆盖范围
→ 锁定 assignment purpose
→ 选择已注册 target claim
→ 绑定 P / C / allowed tools
→ 分离 P 与 s_u
→ 必要时声明局部 M_q
→ 设计 Evidence
→ 生成完整 item package Q
→ 低成本 self-audit 与塑形
→ 计算建议 validation level
→ 输出 Stage A / sealed Stage B
→ 交给独立 Structural Validation
```

不能先写题面再选择 claim。若缺少决定生成的声明，按共享声明集登记 `pending_declarations` 候选并停止受影响生成。

## 3. Generation request

```yaml
generation_request:
  current_request: ...
  learning_target: ...
  delivery_mode: dialogue_item | review_set | candidate_only
  route_binding:
    route_ref: 文件及精确版本，独立任务可为none
    node_ids: []
    current_target_action: 本题主要可观察动作
    coverage_limit: 不由本题认领的能力
  assignment_purpose: instruction | practice | retrieval | transfer | diagnosis | review
  practice_level: R0 | R1 | T1 | T2 | T3
  target_claim: K-...
  prerequisite_profile: P-...
  conventions: [C-...]
  allowed_tools: []
  behavioral_state_ref: ...
  administration_context:
    recent_exposure: ...
    visible_title_or_section: ...
    hints_already_given: ...
    answer_source_visible: false
```

`behavioral_state_ref` 只用于生成瞄准与后续 Assignment Fit，不得进入 Validator Stage A packet。

`delivery_mode`与`route_binding`是生成侧编排信息，留在生成/Fit侧；独立题目不强制绑定个人路线。

- `dialogue_item`：只准备当前一个核心目标。新前置或工具缺失时先转01教学，不用未知知识让学生盲猜。
- `review_set`：在用户授权的节点或模型簇范围内编排，每题保留独立目标、版本和验收结果；题量是可调整预算，不是最低配额。
- `candidate_only`：向委托者交付分离的待验收材料后停止，不向学习者自动投放。

对话小题用于定位和修复断点；阶段题组用于撤去支架后的提取、条件判断、表示转换与方法选择。基础未稳定时先同类巩固，稳定后再交错。不机械每讲必出一套；用户明确要求题组时可以整组交付，不受默认一次一题限制。

日常“初诊”不自动选择`K-DIAG`；只有承诺区分已登记的局部模型分区时才使用它。未知前置与已确认缺失分别记录，不能把未观察到能力写成不会。具体投放仍交给03，不由生成者宣布适配。

## 4. R/T 层级与 claim 的关系

保留现有 R0/R1/T1/T2/T3；它们描述练习结构，不是 measurement claim 的替代品。

| practice_level | 常见 target claim | 边界 |
|---|---|---|
| `R0` | `K-RECON` | 撤去一个已经完成首次编码的局部动作；不证明长期掌握 |
| `R1` | `K-EXEC` 或 `K-SELECT` | 方法已给定时是执行；真正无提示选法时才是 `K-SELECT`，且要求 Full |
| `T1` | `K-COND` | 必须改变会影响合法性、分支、优先级或结论的条件 |
| `T2` | `K-REP` | 改变表示并要求保持深层结构，不只是改写措辞 |
| `T3` | `K-BOUND` 或 `K-COMP` | 改假设、定义域、可逆性、边界或证据充分性 |

`K-DIAG` 可以与某个 practice level 组合，但必须另行声明局部 $\mathcal M_q$，不能由 R/T 标签自动推出。

## 5. Claim–Evidence–Task

### 5.1 Claim

从封闭 $\mathcal K$ 选择 item eligibility 目标：

```yaml
target_claim:
  claim_id: K-SELECT
  wording: eligible_for_unprompted_method_selection
```

禁止写：

```text
student_can_select_method
```

后者需要真实作答和 Assignment Fit/02 的行为证据。

### 5.2 Evidence

预先声明最低充分响应证据：

```yaml
planned_response_evidence:
  conclusion: ...
  required_conditions: []
  required_relation_or_choice: ...
  required_justification: ...
  rejected_alternative_if_needed: ...
```

Evidence 必须与本题claim对应；若目标要求区分竞争模型，须使它们产生可观察差异，不为普通执行题虚构错误模型。只看最终数字不能支持方法选择或诊断claim。

每题只承担一个主要目标。接受所有符合公开题意与工具限制的合法路线；若某路线绕开目标能力，不据最终答案认领未展示的能力，也不临时扣分逼迫指定方法。送验前检查目标所需过程证据能否由公开作答要求引出；不足则调整题目或用途，重新计算claim与风险等级。

只换数字可以服务已授权的执行熟练度训练，但不构成迁移。迁移须说明决定性变化影响哪项合法性、分支、表示或结论，说明留在生成侧，不提前提示学习者。答案能从题面推导不等于答案注入；题面直接给出待检验结论或决定性机制才需按相应用途检查。

### 5.3 Task

最后生成能引出上述 evidence 的完整 $Q$。不得靠陌生阅读背景、无关计算或隐藏前置制造“难度”。

## 6. $P$ 与 $s_u$ 的生成侧分离

Generation 同时维护：

```yaml
allowed_prerequisites_P:
  profile: P-MATH1-LA-v1
  required_nodes: []

student_behavioral_state_su:
  stable_evidence: []
  untested: []
  failure_evidence: []
  unknown: []
```

若 $x\in P$，但当前行为状态没有该前置可调用的证据：

- 题目仍可提交 Structural Validation；
- Generation 应把真实状态（未知、未检验或已有失败证据）分别传给 Assignment Fit；
- 不得让 Validator 因此判题非法；
- 不得在投放时用“题目合法”覆盖学生当前不适配。

不得把“未记录”当作已证实缺失；已确认缺少新定义、表示或程序结构时先教学。03及共享声明集中`x not in s_u`按实际行为证据解释，不能抹去它们已有的`untested`分类，也不能从未知直接推出已掌握或已适配。

若 $x\notin P$ 且题面没有给出，则 Generation 应补进题面、改 claim、换 profile 或停止生成；不能依赖 Validator 猜测。

## 7. Convention 绑定

每个未写在题面的约定必须显式绑定 $C$：

```yaml
convention_bindings:
  - convention_id: C-PROB-RANDOM-SAMPLE-IID-v1
    source_ref: 指定教材定义位置
```

没有绑定时，Generation 不得写“通常默认”。当前 `PD-C-DEFAULT-DOMAIN-001` 未解决，因此受影响题必须显式写明数域。

## 8. 错误模型与 diagnostic generation

### 8.1 来源分离

- `M_library` 可以作为竞争程序，但不表示用户具有该错误；
- `M_candidate` 只是一种待判别解释；
- `M_user-active` 必须已有额外行为证据；
- Error Log 自然语言条目只有 operationalized 后才能作为正式模型运行。

### 8.2 局部 $\mathcal M_q$

诊断题只声明当前分区：

```yaml
diagnostic_partition:
  side_A: [M-LIB-COND-OMIT-v1]
  side_B: [M-LIB-COND-INVERT-v1]
  coverage_claim: local_partition_only
```

Generation 必须预演每个模型怎样触发、行动、终止并产生何种可观察响应，但该预演仍只是 generator rationale；最终 separability 由 Full Validator 独立模拟。

### 8.3 Candidate probe

当前一次作答刚形成 candidate 时，可以生成 discrimination probe，但必须标明：

```yaml
diagnostic_target_status: candidate_under_test
```

Probe 通过 Structural Validation 和 Assignment Fit 后投放；只有新行为证据符合 candidate 预测，02 才能考虑晋升 user-active。题面不得告诉用户旧错误名称或决定性条件。

## 9. 完整 item package

```yaml
item_package:
  item_id: ...
  package_version: 1
  title: ...
  stem: ...
  options: []
  instructions: ...
  response_requirement: 结论 + 关键依据
  scoring_rule:
    fully_acceptable: []
    partially_acceptable: []
    unacceptable: []
  source_refs: []
```

选择题必须明确单选/多选，且 scoring rule 不能靠未公开的隐含理由排除另一合法选项。组题时每个 item 单独形成 package、claim 和 validation 结果；整卷说明变化也可能使各题 leakage dependency 失效。

`scoring_rule`写与公开要求一致的评价准则，明确完整与部分响应的界限；不夹带生成者答案键或未公开的指定解法。具体答案集合与参考解答进入sealed Stage B。若评分准则本身含答案或决定性路线，先重构题目包及评分表达；不能删去必要评分条件以伪造盲验。无法保持完整包且避免预先暴露时，记录隔离失败，不声称独立求解已完成。题目本来要求证明的结论或题面明确给定的方法属于Q，不因其存在自动判为答案键泄露，仍按实际claim审查。

题组在生成侧记录每题ID/版本、主要目标、覆盖节点、建议用途、与前题的提示依赖及预期负担。此清单不进入Stage A；Stage B只提供去除个人状态后的实际呈现信息。不能用整套“已通过”掩盖单题未验收，也不因一题失败作废依赖独立的其他已验收题。

## 10. Stage A / sealed Stage B handoff

### 10.1 交给 Validator 的 Stage A

```yaml
stage_A_packet:
  item_package: 完整Q，包含package_version及无答案键的评分准则
  prerequisite_profile: 已登记profile ID
  required_prerequisites: 本题实际调用项及精确来源
  convention_bindings: 已登记约定及绑定来源
  allowed_tools: []
  declaration_set_version: MATH-ITEM-DECL-v1.0.0
```

Stage A 不含 target claim、solution、rationale、学生状态或 $\mathcal M_q$。

不仅查字段名，还检查内容、文件名、标题与引用目标是否夹带上述材料。来源只读实际需要的定义和约定，不整份加载包含解答的材料。保留Q自身公开内容；不得为了通过盲验删掉Q中的必要条件。

### 10.2 封存的 Stage B

```yaml
sealed_stage_B_packet:
  generator_solution: ...
  generator_answer_set: ...
  generator_rationale: ...
  target_claim: K-...
  diagnostic_partition: 不适用时为none
  generation_self_audit: ...
  suggested_validation_level: Light | Full
  presentation_evidence:
    presentation_version: ...
    visible_context_excerpt: 实际可见的相邻讲解、标题与提示
    visible_item_order: []
    prior_items_or_solutions_visible: []
    coverage: complete_within_declared_scope | incomplete | unknown
```

只有 Validator 封存 Stage A 后才可解封 Stage B。

封存记录须包含Q/P/C/A精确版本、独立答案与核验、预先声明的搜索族及实际完成记录；只说“已验算”不算可核对产物。Stage B只追加比较，不回写Stage A为“原本想到”。

`presentation_evidence`只含审计真实呈现所需文本和顺序，不含学生能力判断、错误模型归属、速度或Error Log。去除个人状态时保留真正造成提示的方法名、公式及答案片段；无法同时隔离状态与保留线索时报告缺口。未取得的呈现范围标为`incomplete/unknown`，不假定无提示。

Light的Core也要求初始答案盲的独立求解；不能把生成者复算当验证。缺少独立执行条件时交付待验收材料，不伪造执行记录。协议的角色分离不要求不同品牌模型，但要求满足Validation的上下文隔离条件。

## 11. Generation self-audit

Self-audit 是低成本预筛，不是最终验收：

```yaml
generation_self_audit:
  generator_solved_candidate: yes | no
  obvious_condition_gap: found | not_found
  obvious_second_interpretation: found | not_found
  obvious_leakage: found | not_found
  prerequisites_bound_to_P: yes | no
  response_and_scoring_aligned: yes | no
  route_scope_match: yes | no | not_applicable
  behavioral_unknowns_preserved: yes | no
  evidence_matches_claim: yes | no
  alternative_routes_scored_fairly: yes | no
  transfer_is_decisive: yes | no | not_applicable
  stage_A_allowlist_checked: yes | no
  scoring_wording_unambiguous: yes | no
  self_audit_disposition: submit_to_validation | reshape | discard
```

这里的 `not_found` 必须保留原词义，不能改成不存在。Generation 发现明显问题时先 reshape 或 discard；即使全为正面结果，也不能写“validated”。

## 12. 方法、feature 与 route 的生成侧措辞

Generation 可以提出：

- generator route；
- hypothesized pre-solution feature；
- expected decision points；
- intended failure boundary。

必须使用候选措辞：

```text
generator_hypothesis
candidate_route
intended_feature
```

只有 Validator 给出 paper witness 后才成为 `available_pre_solution_feature`。只有证明 route-minimality 后才能把某路线的决策数提升为 item-level 必要结构；默认：

```yaml
minimality: not_claimed
```

## 13. 建议 validation level

Generation 根据共享声明集计算建议值：

```yaml
level_determination:
  L_min_from_claim: Light | Full
  risk_triggers: []
  L_risk: Light | Full
  suggested_level: Light | Full
```

最终等级由 Validator 重新计算。Generator 不能通过把目标 claim 降级来逃避 high-risk Full 检查。

## 14. Assignment Fit handoff

Generation 不直接投放。只有 Validation 对目标 claim 输出 `supported` 后，才把以下内容交给 `03_数学_自适应出题.md`：

```text
Task Fingerprint
+ behavioral state
+ assignment policy
+ administration context
```

Assignment Fit 默认不读取 generator rationale。若 claim 为 `not_established`、`contradicted`、`not_assessed` 或 `undecidable`，不得以该 claim 用途投放。

## 15. Population Calibration

没有真实群体数据时，Generation 与 Validation 都固定记录：

```yaml
population_calibration:
  status: uncalibrated
```

不得生成 `difficulty: 3.7/5`、“中等偏难”、预测答对率或伪 IRT 参数作为底层驱动数据。当前学生实际负担只能在 Assignment Fit 中相对 Task Fingerprint、$s_u$ 与 administration context 判断。

## 16. 对用户的展示

先区分学习者、生成委托者与独立验收者。候选委托者按角色接收分离的材料，不把含Stage B的整包转发给Stage A盲验者。用户明确索取答案、完整解答或教师材料时按该请求交付，不拿防泄露规则拒绝；相应材料不再作为该用户独立发现的证据。

完成Validation与Assignment Fit、向学习者投放练习时，沿用轻量格式：

```text
【题目】……
【作答要求】结论 + 关键依据
```

若“当前目标”不会泄露可加一行；会泄露就省略。练习作答前不附generator solution、教师评分点、错误模型、决定性feature或首步。默认对话一次一题；明确要求复习题组时可整组交付，答案与教师材料分开，按真实题序审查相互提示。做完当前交付即停止，不自动追加下一组训练。

## 17. Generation failure-safe

遇到以下情况停止并暴露缺口：

- target claim 未注册；
- 必要前置无法绑定 $P$；
- 隐含约定无法绑定 $C$；
- diagnostic model 未 operationalize；
- administration context 已经使目标无提示 claim 不可能成立；
- item package 无法形成可判评分规则。

缺声明时输出 `undecidable + missing_declaration`；题目本身尚未生成完整时不得送入 Assignment Fit。

## 18. 版本与本轮依据

1.1.0（2026-09-06）：补充对话/题组编排、统一Stage A/B接口、评分与答案键分离、真实呈现依赖和独立执行边界。配套Validation 1.1.0；共享声明集仍为`MATH-ITEM-DECL-v1.0.0`，claim最低等级未降低。

用户在本轮明确授权“允许不等待”研究依据版，本次依据现行00、03、共享声明集及用户教学规则修订；不声称读过缺失研究档，也不将此次豁免推广到未来维护。旧报告保留原协议版本，新增检查按实际依赖补验。03仍有两处待同步措辞，详见90；当前用途按用户明确规则及本协议解释，不假装全套文件已无冲突。
