## GRPO 里的 Length Bias 问题

### 问题来源

GRPO 的 per-token loss 形状是 `[batch, seq_len]`,需要聚合成一个 scalar 才能 backward。聚合方式有两种选择:

- **`masked_mean`(原版 GRPO)**:每条 response 按**自己的有效长度** $|o_i|$ 求平均,$\mathcal{L}_i = \frac{1}{|o_i|}\sum_t \ell_{i,t}$
- **`masked_normalize`(Dr. GRPO)**:每条 response 按一个**全局固定常数** $L_{\max}$ 求和归一化,$\mathcal{L}_i = \frac{1}{L_{\max}}\sum_t \ell_{i,t}$

### Bias 的本质

`masked_mean` 等价于把每个 token 的权重设为 $1/|o_i|$——**短 response 里每个 token 权重大,长 response 里每个 token 权重小**。这从 per-token gradient 上看得最清楚:同样的 advantage、同样的 ratio,短 response 的 token 拿到 0.25 的梯度,长 response 的只有 0.143,差 1.75 倍,纯粹由长度决定。

而 policy gradient 的原始数学是 $\nabla \log \pi(o) = \sum_t \nabla \log \pi(o_t \mid o_{<t})$——每个 token 是独立决策,**权重应该都是 1**,没有理由按长度倒数加权。`masked_normalize` 用固定 $L_{\max}$ 除,所有 token 等权重,只是个全局学习率缩放,不引入 length-dependent 加权。

### 为什么会病理化训练

关键不在"长 vs 短哪个该多贡献"——长短本身不是 reasoning 质量的标准。问题在于 length-dependent 加权会**和 advantage 的 length-conditional 分布发生交互**:

- 如果训练某阶段"长 response 更容易答错"(R1-style 早期常见),`masked_mean` 把长错的惩罚摊薄,模型学到"想错就错长一点"
- 如果"长 response 更容易答对",`masked_mean` 又把长对的奖励摊薄,模型倾向写短

任一方向的 bias 都不是你想要的——你希望 response 长度由 reward 信号本身驱动自由演化,而不是被 normalization 的 quirk 推着走。

### 隐蔽性

这个 bias 在很多简化例子里**看不出来**(比如 advantage 在 batch 内都相同时,$|o_i|$ 会从分子分母同时消掉,两种聚合方式算出来的 scalar loss 一样)。要看出真实差别,必须同时满足两个条件:**advantage 在 group 内不均匀**(实际 GRPO 训练的常态),**且 response 长度在 group 内不均匀**。这时从 per-token gradient 上才能清楚看到 row 之间的权重不对称。

### Dr. GRPO 的修正

把 `masked_mean` 换成 `masked_normalize(..., constant_normalizer=L_max)`。改动很小,但让 loss 聚合回到 policy gradient 的原始数学形式,消除 length 维度上的隐性 bias。这是 Dr. GRPO 三个修正中的一个(另外两个是去掉 std normalization、保留 mean baseline)。