# 数学题 Structural Validation Protocol

> 版本：1.1.0  
> 依赖声明集：`MATH-ITEM-DECL-v1.0.0`  
> 职责：对完整 item package 在显式声明集下支持哪些结构性 measurement claim 作出可审计判断。  
> 不负责：判断当前学生是否适合、预测群体答对率、更新学习状态或宣称长期掌握。

## 1. 验收对象与角色隔离

Structural Validation 验收的是：

```text
完整 item package Q
+ 允许前置 P
+ Convention C
+ allowed tools A
+ 已注册 measurement claim k
+ 对 Full 检查必要的 generator sealed packet
```

其中完整 $Q$ 至少包含：

```yaml
item_id: ...
package_version: ...
title: ...
stem: ...
options: []
instructions: ...
response_requirement: ...
scoring_rule: ...
source_refs: []
```

题干、标题、选项、instructions、作答要求或评分规则的变化都视为 $Q$ 变化；不能只对 stem 做缓存。

Validator 必须对当前学生状态 $s_u$ 盲。以下内容不得进入 Structural Validation 判断：

- 当前学生会不会；
- 学生觉得难不难；
- 是否“正好适合他”；
- 学生是否长期掌握；
- 学生近期情绪、速度或偏好。

Validator 可以使用 $P$，但不得把 $P$ 偷换为 $s_u$。

## 2. 输入封装与两阶段盲验收

### 2.1 Stage A packet

Stage A使用下列统一接口。所有等级的Core先独立求解；Full另须完成全部适用的两阶段Extended检查：

```yaml
stage_A_packet:
  item_package: 完整Q，包含package_version及无答案键的评分准则
  prerequisite_profile: 已登记profile ID
  required_prerequisites: 本题实际调用项及精确来源
  convention_bindings: 已登记约定及绑定来源
  allowed_tools: []
  declaration_set_version: MATH-ITEM-DECL-v1.0.0
```

Stage A 不得看到：

- generator solution；
- generator rationale；
- “为什么这样设计”；
- target claim；
- diagnostic partition $\mathcal M_q$；
- 当前学生状态或 Error Log。

Stage A 先独立求解、列出合理解释、检查条件与边界，并形成不可被 Stage B 覆盖改写的记录。

旧接口的`conventions`可规范化为`convention_bindings`并记录转换；两字段并存但不一致时停止受影响检查，要求提供一致的实际绑定，不猜测。`required_prerequisites`不能省成课程目录或学生会什么的描述。

不仅检查字段名，还检查字段内容、文件名、标题与引用目标是否夹带答案、target claim、rationale或个人状态。来源只读取实际需要的定义和约定，不整份加载含解答的文档。

`scoring_rule`保留完整评价准则，答案键和参考解答放在Stage B。若评分字段已经含答案或决定性路线，要求先重构题目包；不能删掉必要评分条件假装盲验成功。题面本来要求证明的结论、明确给定的方法属于Q，不因此自动判为答案键泄露；仍按实际用途审查。发生预先暴露按§2.3记录。

Stage A封存记录至少包含Q/P/C/A精确版本、独立答案与核验、预先声明的搜索族和实际执行记录。没有可核对产物，不能只凭“已独立验算”记为执行完成。

### 2.2 Stage B packet

Stage A 封存后才解封：

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

Stage B用于比较Generator是否漏解、误判前置、夸大feature、泄露方法或错配claim，并据目标与实际呈现完成等级判断和适用审计。不得用generator rationale倒写Stage A的“自然思路”。

`presentation_evidence`只含审计呈现所需文本与顺序，不含学生能力判断、错误模型归属、答题速度或Error Log。去除个人状态时保留真正造成提示的方法名、公式及答案片段；无法同时隔离状态和保留线索时报告缺口，不能宣称审计完成。具体个人近期暴露与能力解释仍留在03/02。

### 2.3 隔离失败

只有新上下文、独立 Validator invocation 或其他能证明 Stage A 未接触 sealed packet 的机制，才可记录：

```yaml
rationale_blind_check: executed
```

若同一 Validator 在 Stage A 前已经看过 generator solution/rationale，必须记录：

```yaml
rationale_blind_check: skipped(reason: validator_context_already_exposed)
```

这不是`undecidable`：判据存在，但必需执行没有完成。没有直接反例而只是隔离执行不足时，要求Full且依赖该检查的目标claim为`not_established`；已有直接反例则按五态规则记`contradicted`。两者都不能伪称Full已完成。

Light的Core也要求初始答案盲的独立求解。Light能省略不要求的Extended，不能让已看过答案的生成者把复算标成独立验证。Core独立性未实现时，其所支持的目标claim不得为`supported`；若没有直接反例而只是执行不足，记`not_established`，已有直接反例仍按五态规则记`contradicted`。可交付缺失步骤，不伪造Validator身份或执行记录。

Stage A在未知target claim和建议等级时先执行Core，并按题面结构在解封rationale前登记实际适用的搜索族；可以在Stage A执行相关搜索并封存。Stage B再计算最终等级、比较目标、完成适用审计。解封后执行的搜索须明确记录为追加检查，不冒充盲搜索；如目标要求的某项盲检查未完成，不能用追加检查掩盖该缺口。

## 3. 最小可运行核：固定执行顺序

Validation 报告必须按以下顺序产生，不能先填 Task Fingerprint 再补求解。

### 第一部分：Core

所有等级都逐条执行：

1. `independent_solve`
2. `condition_sufficiency`
3. `prerequisite_scope_P`
4. `answer_response_requirement_consistency`
5. `undecidable_reporting`

### 第二部分：Claim / level determination

确认 claim 已注册，并计算：

$$
L(q,k)=\max\left(L_{\min}(k),L_{risk}(q)\right).
$$

### 第三部分：Extended

逐项写 `executed` 或 `skipped(reason)`：

- `rationale_blind_two_stage_check`
- `route_family_search`
- `feature_witness_audit`
- `leakage_search`
- `diagnostic_model_simulation`
- `task_fingerprint_full_profile`

### 第四部分：Task Fingerprint / claim result

最后才生成标准化 fingerprint、claim 五态、dependency、lineage 与 calibration 状态。

## 4. Core 的逐项判据

Core 不得静默跳过。输入缺失或判据缺失时，也必须执行“识别缺口”并输出对应状态。

### 4.1 `independent_solve`

Validator 在 generator solution 初始盲的情况下：

1. 按 $Q,P,C,A$ 求解；
2. 写出答案集合或可接受响应边界；
3. 标出每个关键结论的条件；
4. 至少做一种适用的终点核验：代回、逆推、边界、反例、分支穷尽或局部独立路线；
5. 区分证明、计算验证和有限搜索。

输出至少包括：

```yaml
independent_solve:
  execution: executed
  answer_set: ...
  route_id: V-A-R1
  verification: ...
  evidence_strength: proved | witnessed | verified_within_declared_scope
```

数值试验可以发现 counter-witness，但不能证明一般结论。

### 4.2 `condition_sufficiency`

检查：

- 对象、数域、定义域、参数范围和量词；
- 定理与程序适用条件；
- 答案是否唯一或评分边界是否覆盖多解；
- 是否存在第二种在 $P,C$ 下自洽解释；
- 边界、退化情形和反例；
- 信息不足是否被题目明确设计为 `K-COMP` 的响应对象。

若题目无意中缺条件，结构合法性被 counter-witness 反驳。若题目明确要求“找缺失条件/说明不可判定”，且 scoring rule 覆盖合法响应，则不能把这种有意不完备误判成坏题。

### 4.3 `prerequisite_scope_P`

列出真实求解所需的每个定义、定理、表示和程序，并逐项标记：

```yaml
- prerequisite: ...
  source: item | P-profile | C-binding | absent
  required_for: 哪一步
```

若必要项为 `absent`，且它不是 `K-COMP` 明确要求补出的对象，则该检查不能支持题目合法性。不得根据当前学生会不会判断这一项。

### 4.4 `answer_response_requirement_consistency`

检查：

- stem 实际提出的问题；
- instructions 要求的动作；
- response requirement 要求提交的证据；
- scoring rule 接受与拒绝的响应；
- options 是否与唯一/多选规则一致。

只要求选项却把“方法选择理由”作为 claim 证据，或题面允许多解而评分只收一个答案，均构成不一致。

接受所有满足公开题意和工具限制的合法路线，不临时加入未公开的指定解法要求。某合法路线没有展示目标能力时，记录证据覆盖限制；若击穿目标claim的必需条件，按该claim处理，不把合法作答判错。

### 4.5 `undecidable_reporting`

逐项查询 `数学出题_共享声明集.md`。若缺少 $P,C,\mathcal K,\mathcal M$、level 或 protocol 判据：

```yaml
undecidable_reporting:
  execution: executed
  status: undecidable
  missing_declaration: ...
  pending_declaration_candidate: ...
```

Validator 到此停止受影响的结论，不得自行补规则继续跑。若判据存在但本次没有取得足够证据，应使用 `not_established`，不是 `undecidable`。

同时把 `pending_declaration_candidate` 以 `status: open` 追加到共享声明集的 `pending_declarations`；若当前无写权限，则输出可原样追加的完整 YAML 并保持 claim 阻塞，不能只留一句自由文本备注。

## 5. Claim requirement table v1

表中“必需”表示目标 claim 要得到 `supported` 时必须执行并达到指定强度；risk 升级后还要执行所有 Full 通用检查。

跨 claim 的 negative-claim 下限固定为：声称“不存在、唯一、没有其他合法解释/路线、最小或最优”必须达到 `proved`。有限 leakage/route 搜索的 `not_found` 只能支持已声明范围内的审计记录，不能支持不受限的否定命题；若某 target claim 必须依赖该否定而又没有证明，则为 `not_established`，若已有反例 witness 则为 `contradicted`。

| claim | 最低等级 | Core | feature witness | leakage audit | route search | diagnostic simulation | 关键证据要求 |
|---|---|---|---|---|---|---|---|
| `K-EXEC` | Light | 全部必需 | 非必需 | 非必需 | 非必需 | 不适用 | 已知方法给定后，执行链与评分规则一致 |
| `K-RECON` | Light | 全部必需 | 非必需 | Core 内检查直接答案注入；Full 风险时扩展审计 | 非必需 | 不适用 | 被撤去的局部动作没有在题面或作答要求中直接复述 |
| `K-COND` | Light | 全部必需 | Full 风险时必需 | Full 风险时必需 | Full 风险时按 claim-relative 范围执行 | 不适用 | 条件变化确实改变合法性、分支、优先级或结论；至少 `witnessed` |
| `K-SELECT` | Full | 全部必需 | 必需 | 必需 | 必需 | 不适用 | 有合法解前 feature witness；未发现泄露只能记有限范围 `not_found`；不主张唯一路线 |
| `K-REP` | Full | 全部必需 | 必需 | 必需 | 必需 | 不适用 | 表示转换规则、可逆性/信息损失和保持结构均已核验 |
| `K-BOUND` | Full | 全部必需 | 按题型必需 | 必需 | 必需 | 不适用 | 边界或反例有具体 witness；任何“不存在”主张需要 `proved` |
| `K-COMP` | Full | 全部必需 | 非必需 | 必需 | 必需 | 不适用 | 至少一个缺条件 counterexample/第二模型被 `witnessed`，且 scoring rule 接受补全或不可判定 |
| `K-DIAG` | Full | 全部必需 | 按 partition 必需 | 必需 | 按题型执行 | 必需 | 只对声明的 $\mathcal M_q$ 模拟；每侧产生可观察不同响应；不外推全库 |

表中未要求且实际未执行的Extended项，在Light报告中写`skipped(reason: not_required_at_light_level)`；已实际执行的项如实写`executed`。Full仍须按risk和目标claim判断是否执行。必需项被跳过时不能支持目标claim；没有直接反例但执行不足时为`not_established`。

## 6. Light / Full Validation

### 6.1 Light

Light 适用于低风险 `K-EXEC`、`K-RECON` 和部分 `K-COND`。

必须：

- 逐条完成 Core；
- 计算 claim/risk；
- 每个Extended项按实际情况写`executed`或`skipped(reason)`；不为填字段增加无关检查；
- 生成最小标准化 fingerprint，未检查字段写 `not_assessed`；
- 输出目标 claim 五态。

Light 不是“快速看一眼”，也不能跳过独立求解或条件检查。

“对话里的一道小题”不是降级理由。建议Light后若发现Full触发器，仍按共享声明集升级；不改名claim来规避检查。

### 6.2 Full

Full 必须：

- 完成 Core；
- 完成真正隔离的 Stage A → Stage B；
- 执行 requirement table 和 risk 要求的 Extended；
- 对不适用项写 `skipped(reason: not_applicable_to_claim)`；
- 完成完整 Task Fingerprint、granular dependency 与 claim lineage。

同一上下文已经暴露 rationale 时，不得把普通复核冒充两阶段盲验收。

## 7. Extended 检查

### 7.1 Route-family search

使用 `ROUTE-SEARCH-v1.0`，在看 generator rationale 前声明适用 family，并记录：

```yaml
route_search:
  execution: executed
  protocol_version: ROUTE-SEARCH-v1.0
  families_declared: []
  families_scanned: []
  routes_verified: []
  budget_used:
    families_scanned: 0
    candidate_routes_considered: 0
    routes_fully_verified: 0
  stopping_reason: ...
  minimality: not_claimed
```

相同尝试次数不表示相同搜索强度。除非有穷尽证明或复杂度下界，禁止写“最简单、最短、唯一自然路线”。

### 7.2 Feature witness audit

Feature availability 属于 Validation；recognition 和 candidate generation 不属于。

每个 feature 必须给 paper witness：

```yaml
- feature_id: FTR-...
  witness:
    item_location: 题面/目标/选项中的精确位置
    pre_solution_transform: 不知道答案时允许执行的转换
    resulting_feature: 得到的结构
  evidence_strength: proved | witnessed
```

不能只写 `feature_exists: yes`。Validator 只能说 feature 在纸面上可取得，不能说“当前学生自然会想到”。

### 7.3 Leakage search

搜索范围至少包括：

- title；
- stem；
- options；
- instructions；
- response requirement；
- 当前 administration context 中紧邻的提示、章节标题或方法菜单。

记录 scope、budget 和 protocol version。发现一个决定性泄露即为 `witnessed`。没有发现只能记：

```yaml
leakage_search:
  result: not_found
  search_scope: ...
  budget_used: ...
  protocol_version: ...
```

不得写“无泄露”，除非另有覆盖完整信息通道的正式证明。

使用Stage B的`presentation_evidence`审计真实呈现；题组题序、前题解答、章节标题和刚给的公式都可能改变后题用途。教师侧评分准则只在实际展示给学习者时才属于其泄露范围，但它对Validator初始答案盲的影响始终须检查。

未提供的呈现背景标为未覆盖，不能默认为没有提示。若欠缺目标claim必需的审计证据，使用`not_established`，不因缺材料直接声称题目有错。题面无提示不等于冷启动保持；重建可支持即时用途，但学生实际近期暴露与能力解释仍由03/02处理。

组题按每题实际位置分别审计；一题的提示或解答若影响后题，重算受影响后题的leakage及下游claim，不笼统废弃整套或笼统声称整套通过。

### 7.4 Diagnostic model simulation

只模拟单题绑定的 $\mathcal M_q$：

```yaml
diagnostic_simulation:
  execution: executed
  partition:
    side_A: []
    side_B: []
  traces:
    - model_id: ...
      trigger_match: ...
      action_trace: ...
      termination: ...
      predicted_response: ...
  observable_separation: ...
  coverage_claim: local_partition_only
```

若两个模型在当前 response requirement 下产生同样可接受响应，`K-DIAG` 被 `contradicted`。新增与 $\mathcal M_q$ 无关的模型不触发重验。

## 8. Item feature 与 validated-route profile

必须分开保存：

### 8.1 Item-level feature

只记录由完整 $Q,P,C,A$ 决定、并有 paper witness 的结构。若“所有合法路线都必须经过三个决策”没有证明，则不能写成 item-level 必要结构。

### 8.2 Validated-route profile

每条已核验路线可以记录：

```yaml
route_id: ...
decision_nodes: []
forced_cases: []
calculation_chain: []
representation_conversions: []
verification_opportunities: []
search_or_backtracking: []
minimality: proved | not_claimed
```

这些字段描述该路线，不自动描述题目本身。

## 9. Task Fingerprint

所有报告输出同一 container；Light 未检查的 Extended 字段写 `not_assessed`，Full 完成全部适用字段。

```yaml
task_fingerprint:
  fingerprint_version: TASK-FP-v1.0
  validation_level: Light | Full
  item_package_ref: ...
  required_prerequisites: []
  required_recognitions: []
  representation_form: ...
  available_pre_solution_features: []
  item_level_decision_structure: proved_structure | not_established
  forced_branches_item_level: [] | not_established
  validated_route_profiles: []
  execution_demands: []
  response_requirement: ...
  diagnostic_target: none | local_partition
  target_claim: K-...
  validation_status: supported | contradicted | not_established | not_assessed | undecidable
  validation_confidence:
    evidence_strength: proved | witnessed | verified_within_declared_scope | not_found
    scope: ...
```

`required_recognitions` 只描述成功响应需要识别什么，不表示任何学生已经识别。`validation_confidence` 是证据强度与范围，不是主观分数或统一难度值。

## 10. Claim-relative 结论

Validation 不输出笼统“题目通过/不通过”，而输出：

$$
q\mapsto\{k\in\mathcal K:\text{当前证据支持}\}.
$$

实际报告至少包含目标 claim：

```yaml
claim_results:
  - claim_id: K-SELECT
    status: not_established
    satisfied_requirements: []
    failed_requirements: []
    unexecuted_requirements: []
    evidence_refs: []
```

题目可以在 Core 下数学合法，却没有任何已注册 measurement claim 得到支持。此时结论是：

> 当前未授权用于任何已注册 measurement claim。

不得在失败后临场发明较弱 claim；若要降级，必须使用已注册 claim 并记录 lineage。

## 11. Population Calibration

没有真实群体行为数据时固定输出：

```yaml
population_calibration:
  status: uncalibrated
```

不得由 GPT 根据题面估计群体答对率、Rasch/IRT 难度或 empirical difficulty。Task Fingerprint 和 route profile 不是经验难度。

## 12. Granular validation dependency

不同结论分别绑定依赖：

```text
K_validity = H(Q, P, C, A, V_base)
K_feature  = H(Q, P, C, V_feature)
K_route    = H(Q, P, C, A, V_route)
K_leakage  = H(Q, P, C, A, E, V_leakage)
K_diag     = H(Q, M_q, k, V_diag)
K_claim    = H(K_validity, required sub-conclusions, k, requirement-table-version)
```

其中：

- $Q$ 是完整 item package；
- $V_*$ 是相应 protocol version；
- $E$是去除个人状态后的`presentation_evidence`及其精确版本；当claim要求leakage审计时，`K_claim`的必需子结论须包含`K_leakage`；
- 依赖可以用稳定 digest 或精确版本元组实现；不得只写一个全局 `K_V` 绑定整份报告。

变更影响规则：

| 变化 | 至少重验 |
|---|---|
| title、stem、options、instructions、response requirement、scoring rule、source refs | validity；并按影响传播到 feature/route/leakage/diag/claim |
| $P$ 或 $C$ | validity；可能传播到 feature/route/leakage/claim |
| 允许工具$A$ | validity、适用route及下游claim；也检查依赖A的leakage，不能只因题干未变而复用 |
| 实际提示、题序、前题解答可见性或$E$覆盖范围 | leakage及其下游claim；Q/P/C/A未变且依赖仍有效时，不自动推翻原独立求解 |
| 实际使用的协议子版本或requirement table | 对应子结论及下游claim；旧报告保留原版本，不自动继承新增检查 |
| generator rationale 但 $Q$ 不变 | 不自动使 Stage A validity 失效；需要重做 Stage B comparison |
| route protocol | route 及依赖 route 的 claim |
| $\mathcal M_q$ | diagnostic 及 `K-DIAG`；不影响无关 validity/route |
| 新增不属于 $\mathcal M_q$ 的 library model | 原 local diagnostic cache 不失效 |

旧报告没有呈现依赖绑定时，不能直接授权新场景的无提示用途；按实际依赖补做受影响审计，可复用仍有效的独立求解。不因升级文档就将旧报告改成新版本已通过。

## 13. Claim lineage

高 claim 失败后降级必须留痕：

```yaml
claim_lineage:
  original_claim: K-DIAG
  validation_result: not_established
  failed_requirements: []
  demoted_from: K-DIAG
  current_claim: K-COND
  reused_evidence: []
  revalidated_evidence: []
```

Item package 不变时可以复用依赖仍有效的证据；题目本身被修改时，受影响结论必须重验。禁止把失败的诊断题静默洗成普通巩固题。

## 14. Counter-witness、quarantine 与 targeted revalidation

### 14.1 Challenge witness

学生作答可能提供：

- 第二个合法答案；
- 第二种在 $P,C$ 下自洽解释；
- 缺条件反例；
- leakage witness；
- 其他直接反驳 validation 结论的对象。

这与“学生答错”不同。只找到另一条正确路线，但不改变题意、答案合法性或 claim 时，只更新 route profile。

### 14.2 状态转换

```text
validated
→ challenged
→ quarantine
→ targeted_revalidation
```

进入 quarantine 后：

1. 暂停该题产生的学习证据；
2. 不更新 Error Log、M_candidate、user-active model 或长期学习状态；
3. 保存 witness 原文和它声称影响的 dependency；
4. 只重验受影响部分及其下游 claim。

重验结果：

```text
witness_confirmed
→ 相应 validation conclusion 失效，依赖它的 claim 重新计算

witness_rejected
→ 恢复未受影响状态，记录拒绝理由，再决定是否恢复暂存行为证据

unresolved
→ 继续 quarantine，不产生学习结论
```

### 14.3 Targeted revalidation packet

```yaml
challenge_id: ...
item_package_version: ...
witness: ...
affected_dependency: validity | feature | route | leakage | diagnostic | claim
prior_conclusion: ...
revalidation_scope: ...
result: witness_confirmed | witness_rejected | unresolved
reason: ...
```

## 15. 标准输出模板

```yaml
validation_report:
  protocol_version: MATH-ITEM-VALIDATION-v1.1.0
  declaration_set_version: MATH-ITEM-DECL-v1.0.0
  stage_A_record_ref: 精确版本与封存记录位置
  presentation_evidence_ref: 已取得呈现版本及覆盖范围，未取得须明确标注

  core:
    independent_solve: {execution: executed, result: ...}
    condition_sufficiency: {execution: executed, result: ...}
    prerequisite_scope_P: {execution: executed, result: ...}
    answer_response_requirement_consistency: {execution: executed, result: ...}
    undecidable_reporting: {execution: executed, result: ...}

  claim_and_level:
    target_claim: K-...
    claim_registered: true
    L_min: Light | Full
    L_risk: Light | Full
    required_level: Light | Full

  extended:
    rationale_blind_two_stage_check: executed | skipped(reason)
    route_family_search: executed | skipped(reason)
    feature_witness_audit: executed | skipped(reason)
    leakage_search: executed | skipped(reason)
    diagnostic_model_simulation: executed | skipped(reason)
    task_fingerprint_full_profile: executed | skipped(reason)

  task_fingerprint: ...
  claim_results: ...
  population_calibration: {status: uncalibrated}
  dependencies: ...
  claim_lineage: ...
```

## 16. 停止规则

- 找到直接 counter-witness 后，可以停止与该 claim 无关的昂贵搜索，但必须完成受影响状态记录；
- 遇到声明集缺口，登记 pending candidate 后停止受影响检查；
- 达到 route budget 只能写 `not_found` 或有限范围支持，不能改写成穷尽；
- 完成 validation 不授权投放；必须再经过 Assignment Fit；
- 用户说“问题审查”时，对外不展示解法或答案，但内部 Core 的 independent solve 仍必须执行。

## 17. 版本与本轮依据

1.1.0（2026-09-06）：统一Generation/Validation的Stage A/B封装，补足评分及引用目标的暴露检查、Light独立求解、Extended执行状态、呈现依赖及targeted revalidation字段。`MATH-ITEM-DECL-v1.0.0`、`TASK-FP-v1.0`、`ROUTE-SEARCH-v1.0`和claim最低等级保持不变；新字段为交接或报告元数据。

用户明确授权本轮不等待缺失研究依据版，依据现行入口、共享声明集、03及用户教学规则修订。只说明文档规则已更新，不声称执行过实际题目的盲验或取得教学效果证据。未来维护仍按入口及届时用户授权执行。
