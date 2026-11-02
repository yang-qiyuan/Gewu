# 数据不平衡：精简解决方案

## 1) 改数据（采样/增强）
- **过采样**：RandomOverSampler；SMOTE / Borderline-SMOTE / ADASYN（合成少数类）
- **欠采样**：RandomUnderSampler；TomekLinks / ENN / NearMiss（更“聪明”地删多数类）
- **数据增强**：图像/文本/语音对少数类做增强
- ✅ 经验：**轻度欠采样 + 适度过采样** 往往更稳

## 2) 改训练（loss/策略）
- **类别权重/代价敏感**：loss 给少数类更大权重（最通用）
- **Focal Loss**：极度不平衡、少数类难学时更有效
- **调阈值**：别固定 0.5，在验证集上找最优阈值（F1/Recall 等目标）
- **两阶段/级联**：先高召回（Recall）筛候选，再精筛提精度（Precision）
  - 高Recall确保少漏，多抓可以，防止漏掉真正的少数类别 （用简单模型/规则）
  - 高Precision确保少错（用更强模型精确判断）

## 3) 改评估（别被 Accuracy 骗）
- 重点看：**Precision / Recall / F1 / PR-AUC / 混淆矩阵**
- 多分类：**macro-F1**（更公平）

## 4) 场景推荐
- 1:3~1:10：类别权重 + macro-F1/PR-AUC
- 1:10~1:50：类别权重 +（SMOTE 或轻欠采样）+ 调阈值
- >1:100：Focal Loss / 两阶段 / 异常检测思路 + PR-AUC

## 5) 常见坑（很关键）
- **采样只做在训练集**；CV 用 **Pipeline**，避免数据泄漏
- 少数类噪声大时，过采样会放大噪声：先清洗再采样

# SMOTE Method
SMOTE 是一种用于**不平衡分类**的过采样方法，在少数类样本之间**插值生成**新的少数类样本。(**对于离散值不适用**)

## 2. 核心做法（插值公式）
对少数类样本 \(x\)：
1) 找到它的 \(k\) 个少数类近邻（常用 \(k=5\)）  
2) 随机选一个近邻 \(x_{nn}\)  
3) 生成合成样本：
$$
x_{\text{new}} = x + \lambda (x_{nn} - x),\quad \lambda \sim U(0,1)
$$

## 3. 优点
- 比随机复制更不容易过拟合（减少重复样本）
- 让少数类分布更“厚”，模型更容易学到少数类边界
- 常用于提升 Recall / F1 / PR-AUC（取决于任务与阈值）

## 4. 常见坑 / 不适用场景
- **类重叠严重**：可能把新点插到多数类区域，增加混淆  
- **少数类有离群点**：可能围绕离群点生成更多噪声  
- **高维稀疏特征（文本BOW等）**：插值会产生不自然的稠密向量  
- **含类别型特征**：对 one-hot 插值会生成“0.3/0.7”这种不合理值（建议用 SMOTENC）

## 5. 常见变体
- **Borderline-SMOTE**：更关注边界附近的少数类样本  
- **SMOTE + Tomek Links / ENN**：先补点再清洗，减少重叠/噪声  
- **ADASYN**：更偏向在难学区域生成更多样本

## 6. 分类 vs 回归
- **分类**：✅ 原版 SMOTE 主要用于不平衡分类  
- **回归**：❌ 原版不直接适用；可用“回归版SMOTE/目标区间重采样”的变体思路

## 7. 防止数据泄漏（非常重要）
SMOTE **只能在训练集上做**，不要在全数据上先 SMOTE 再划分训练/测试，否则评估会虚高。
（推荐把 SMOTE 放进交叉验证的 Pipeline 里）

---

## 代码模板（sklearn + imblearn）
```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# X, y = ...

clf = LogisticRegression(max_iter=2000, class_weight="balanced")  # 类别权重
pipe = Pipeline([
    ("under", RandomUnderSampler(sampling_strategy=0.5, random_state=0)),
    ("over", SMOTE(sampling_strategy=0.5, random_state=0)),
    ("model", clf),
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(pipe, X, y, cv=cv, scoring="f1_macro")
print("F1-macro:", scores.mean(), "+/-", scores.std())
