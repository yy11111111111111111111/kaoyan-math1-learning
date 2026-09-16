# MV0916 封存 Stage B
元信息：批次 MV0916 | 卷版本 v1 | 更新 2026-09-16 | 状态 independent_validation_pending | 可见性 解析（Stage A封存后解封） | 学生卷 `../../题库/MV0916_复习与理解证明/学生卷.md`


这里只是生成侧参考，不是独立验收；全部目标claim暂为not_established。diagnostic_partition=none，不使用已激活学习者错误模型。presentation_version=MV0916-v1；卷内呈现全文及顺序以学生卷为准；既往可见讲解的逐字记录未齐，presentation_evidence.coverage=incomplete，不能声明无历史提示。

设计总述：本轮连接局部解释与实际积分，另复查退化高阶项和方向导数。A组给定待证结论，B组部分给定程序要求，不能按自主发现或无提示选法计证。卷内前题可能提示后题，实际用途须结合独立审查及投放记录判断。

## 逐题封存包
建议等级保守采用Full（自然语言证明、多路线与卷内提示风险）；外部审查方依据注册表最终裁定，不要求生成者自行实施。generation_self_audit只包含生成时的条件与表达一致性检查，未执行独立求解或盲验，也未声称穷尽合法路线。

### MV0916-01

- target_claim：K-RECON；status：not_established。
- generator_rationale／主要目标：从曲面内运动重建梯度法向，保留非零条件。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：沿任意曲面曲线，G(γ(t))=c，故在0处求导得∇G(P)·γ′(0)=0；非零梯度因此是法向量。梯度为零时等式对任何v都成立，不能由零向量确定法向方向。

<details><summary>当前题面逐字副本</summary>

设 $G\in C^1(U)$，$U\subset\mathbb R^3$ 为开集，$P\in S=\{X\in U:G(X)=c\}$，且 $\nabla G(P)\ne0$。曲面在 $P$ 附近正则；切向量可写为 $v=\gamma'(0)$，其中 $\gamma$ 是曲面上的 $C^1$ 曲线，$\gamma(0)=P$。

证明 $\nabla G(P)\cdot v=0$，并解释为什么这给出了曲面的一个法向量。若去掉 $\nabla G(P)\ne0$，上述正交等式本身是否仍足以给出法向方向？说明理由。

</details>

### MV0916-02

- target_claim：K-RECON；status：not_established。
- generator_rationale／主要目标：从Dr的列与边向量解释局部面积密度。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：可微给出r(p+h)=r(p)+Dr(p)h+o(‖h‖)；分别令h=Δu e1、Δv e2，Dr e1=ru、Dr e2=rv。线性近似的平行四边形面积为‖ru×rv‖|ΔuΔv|，从而dS=‖ru×rv‖du dv。这里是面积密度，不把有限曲面片等同平行四边形。

<details><summary>当前题面逐字副本</summary>

设 $r:D\subset\mathbb R^2\to\mathbb R^3$ 是 $C^1$ 单射正则参数化，$D$ 为开集，$(u_0,v_0)\in D$。从可微定义说明参数小矩形的两条邻边经映射后，为什么一阶近似分别为 $r_u\Delta u$ 与 $r_v\Delta v$（偏导在 $(u_0,v_0)$ 处取值）。

由此解释 $Dr$ 两列的含义，并推出局部面积密度及 $dS$ 的表达式。说明你使用的是局部一阶近似，还是把有限曲面片当成精确的平行四边形；无需证明一般曲面面积存在定理。

</details>

### MV0916-03

- target_claim：K-REP；status：not_established。
- generator_rationale／主要目标：将投影Jacobian与向量面积分量对应。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：J(y,z)=yu zv−yv zu=(ru×rv)x。又n=(ru×rv)/‖ru×rv‖，故dSx=Jdu dv=nx dS；无向局部投影面积是|nx|dS。nx=0时有向密度为零，不能除以nx，但等式仍成立；不由局部式推断投影全局一一。

<details><summary>当前题面逐字副本</summary>

设 $r(u,v)=(x(u,v),y(u,v),z(u,v))$ 为 $C^1$ 正则参数化，曲面定向与 $r_u\times r_v$ 一致。记 $dS_x$ 为按有序坐标 $(y,z)$、正法向为 $+x$ 的平面所定义的局部有向投影面积元。

从投影映射 $(u,v)\mapsto(y,z)$ 的 Jacobian 出发，证明
\[
dS_x=n_x\,dS,
\]
并说明 $dy\,dz$ 与向量面积元第一分量的关系。若只求无向投影面积，应怎样修改？若 $n_x=0$，上述局部关系是否失效？

</details>

### MV0916-04

- target_claim：K-RECON；status：not_established。
- generator_rationale／主要目标：把曲面边界积分改写到参数域并处理方向。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：记A=F(r)·ru、B=F(r)·rv，则边界积分为∮∂D A du+B dv。B_u−A_v=(DF(r)ru)·rv−(DF(r)rv)·ru=(curl F)(r)·(ru×rv)，r_uv项相消。应用Green即得式；同一取向的相邻参数片在公共边界上诱导相反行进方向，因此线积分抵消。

<details><summary>当前题面逐字副本</summary>

设 $D\subset\mathbb R^2$ 是有分段光滑边界的有界单连通区域，$r$ 在 $\overline D$ 的邻域内为 $C^2$，且在 $\overline D$ 上单射、正则；$S=r(\overline D)$ 按 $r_u\times r_v$ 定向。设 $F$ 在 $S$ 的某开邻域内为 $C^1$，$\partial S$ 的方向由 $\partial D$ 的平面正向经 $r$ 诱导。

把曲线积分改写到参数平面，利用平面 Green 公式说明
\[
\oint_{\partial S}F\cdot dr
=\iint_D(\nabla\times F)(r(u,v))\cdot(r_u\times r_v)\,du\,dv.
\]
要求写出改写后的两个系数和关键求导关系；另解释把 $D$ 分片时内部边界为什么抵消，以及为什么不能任意改变某一片的方向。

</details>

### MV0916-05

- target_claim：K-REP；status：not_established。
- generator_rationale／主要目标：从隐式几何连接法向、投影面积与积分。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：取G=x²+y²−4z²，一侧单位法向为(x,y,−4z)/(2√5 z)。用xy投影，z=√(x²+y²)/2，|nz|=2/√5，dS=(√5/2)dxdy；投影是2≤r≤4、0≤θ≤π/2，积分为(√5/4)∫0^{π/2}∫2^4 r²drdθ=7π√5/3。其他合法投影或参数化亦接受。

<details><summary>当前题面逐字副本</summary>

曲面 $S$ 为
\[
x^2+y^2=4z^2,\qquad 1\le z\le2,\quad x\ge0,\ y\ge0.
\]
计算 $\iint_S z\,dS$。写出从隐式方程得到的单位法向量（两侧任选其一），选一个投影平面并说明 $dS$ 与投影面积元的关系，再写清积分区域、完成计算。可以使用参数化辅助计算，但需保留前述投影关系。

</details>

### MV0916-06

- target_claim：K-REP；status：not_established。
- generator_rationale／主要目标：在yz参数平面一致处理三个有向面积元。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：r(y,z)=(2−2y−z,y,z)，D为y,z≥0、2y+z≤2。按题向量面积为(−1,−2,−1)dy dz，因此被积函数为−x−2y−z=−2；D面积为1，答案−2。

<details><summary>当前题面逐字副本</summary>

设 $S$ 为平面 $x+2y+z=2$ 在第一卦限内的三角形部分，取单位法向量的 $x$ 分量为负的方向。计算
\[
\iint_S x\,dy\,dz+y\,dz\,dx+z\,dx\,dy.
\]
写明所用参数或投影区域，以及三个有向面积元的表示。

</details>

### MV0916-07

- target_claim：K-EXEC；status：not_established。
- generator_rationale／主要目标：执行旋度、选面、参数化及边界方向链。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：F=(y²,z²,x²)，curl F=(−2z,−2x,−2y)。取r=A+u(B−A)+v(C−A)，u,v≥0、u+v≤1；ru×rv=(6,3,2)，其边界方向为A→B→C→A。积分的被积函数为−6−2u−30v，利用∫D1=1/2、∫Du=∫Dv=1/6得−25/3。

<details><summary>当前题面逐字副本</summary>

设 $A=(1,0,0)$、$B=(0,2,0)$、$C=(0,0,3)$，闭折线 $L$ 按 $A\to B\to C\to A$ 行进。计算
\[
\oint_L y^2\,dx+z^2\,dy+x^2\,dz.
\]
本题要求写出对应向量场及其旋度，自选以 $L$ 为边界的曲面，给出参数化、参数区域与匹配方向，并据此完成积分。

</details>

### MV0916-08

- target_claim：K-COND；status：not_established。
- generator_rationale／主要目标：区分补面执行与奇点破坏定理前提。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：(1)底面z=0、半径√2，外法向向下，通量−2π；所围体积2π，散度3，闭面通量6π，原曲面通量8π。(2)a=(0,0,1)在内部，H在那里无定义；可去掉完全位于立体内部的小球，新增内球面法向指向球心。对挖洞后的区域应用公式，须保留底面和内球面通量，不能把新增内边界忽略。

<details><summary>当前题面逐字副本</summary>

设 $S$ 为 $z=2-x^2-y^2$ 位于 $z\ge0$ 的部分，取法向量 $z$ 分量为正的方向。

（1）计算向量场 $F=(x,y,z+1)$ 通过 $S$ 的通量；若引入辅助边界，需写清其方向和对结果的贡献。

（2）将向量场换成
\[
H=F+\frac{(x,y,z-1)}{[x^2+y^2+(z-1)^2]^{3/2}}.
\]
将 $S$ 与其在 $z=0$ 平面内的底面组成封闭边界后，能否直接在整个所围立体上应用散度与边界通量的公式？若不能，说明可以怎样调整积分区域、新边界及其方向；此问不要求计算最终通量。

</details>

### MV0916-09

- target_claim：K-EXEC；status：not_established。
- generator_rationale／主要目标：恢复隐式求导符号及单位方向，同时保留路径路线。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：Fz(0)=1且F光滑，隐函数存在并光滑；zx=(2−y)/(1+3z²)。路径代入得w+w³+t³−2t−t²=0，故w′(0)=2、w″(0)=2。梯度为(2,1)，与(3/5,4/5)点乘得方向导数2。

<details><summary>当前题面逐字副本</summary>

方程
\[
z+z^3+xy-2x-y=0
\]
在 $(0,0,0)$ 附近确定 $z=z(x,y)$。

（1）说明局部隐函数存在且可微的依据，并求一般点处 $z_x$ 的表达式。

（2）令 $w(t)=z(t,t^2)$，求 $w'(0)$ 与 $w''(0)$。

（3）求 $z$ 在 $(0,0)$ 处沿向量 $(3,4)$ 所指方向的方向导数。

</details>

### MV0916-10

- target_claim：K-COND；status：not_established。
- generator_rationale／主要目标：处理核外的高阶混合竞争并给邻域级判据。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：H=diag(2,0)，ker H={(0,y)}。f_a=(x+y²)²+(a−1)y⁴+y⁶。a=1、2在原点严格极小；a=0时x=0给y⁶>0，x=−y²给−y⁴+y⁶<0（0<|y|<1），故为鞍点。三者沿核均非负，因此仅查核不能完成区分。

<details><summary>当前题面逐字副本</summary>

设
\[
f_a(x,y)=x^2+2xy^2+a y^4+y^6,\qquad (x,y)\in\mathbb R^2.
\]
求原点的 Hessian 矩阵及其核；分别对 $a=0,1,2$，严格判断原点是否为局部极小、局部极大或鞍点，并在有极值时说明是否严格。你的依据应控制整个邻域，或给出足以否定极值的证据，不能只列有限条直线的试算。

</details>

### MV0916-11

- target_claim：K-EXEC；status：not_established。
- generator_rationale／主要目标：按总次数截断，控制复合展开余项。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：u=O(ρ²)，外层ln(1+u)−u+u²/2=u³/3+O(u⁴)。写u=q+c，q=x²+y²、c=xy²，则u³=q³+O(ρ⁷)，故f=q³/3+O(ρ⁷)。最低次数6，余项亦为o(ρ⁶)，商极限1/3；可以给更精确余项，不要求只用此写法。

<details><summary>当前题面逐字副本</summary>

在 $|x|,|y|<1/4$ 内，令
\[
u=x^2+y^2+xy^2,\qquad
f(x,y)=\ln(1+u)-u+\frac12u^2,\qquad
\rho=\sqrt{x^2+y^2}.
\]
求 $f$ 在原点展开的最低次非零齐次多项式，写出相应余项的阶，并求
\[
\lim_{(x,y)\to(0,0)}\frac{f(x,y)}{\rho^6}.
\]
说明外层函数需要保留到哪一阶，以及代入内层量后为什么可以舍去其他项。

</details>

### MV0916-12

- target_claim：K-SELECT；status：not_established。
- generator_rationale／主要目标：在无指定方法的题面下比较合法路线并计算。
- planned_response_evidence：完成该题公开要求的对象、条件、推理链和计算；不由结果反推未写出的过程。
- suggested_validation_level：Full。
- generator_solution／generator_answer_set：场在全空间光滑；div F=3，补底面封闭后总通量3。底面向外法向−ez，其通量为−∫0^1∫0^1xy dxdy=−1/4，五面通量13/4。直接按面对称抵消也是合法路线；只报数值不提供选法证据。

<details><summary>当前题面逐字副本</summary>

设 $V=[0,1]^3$，$S$ 由 $\partial V$ 去掉底面 $z=0$ 后的五个面组成，方向均向 $V$ 外。令
\[
F=(x+\sin(yz),\ y+e^{xz},\ z+xy).
\]
先用2—3行说明你的方法选择理由，再计算
\[
\iint_S F\cdot n\,dS.
\]

</details>
