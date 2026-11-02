### 1. Accuracy（准确率）

```text
定义：
表示所有预测中，有多少比例是预测正确的。

公式：
Accuracy = (TP + TN) / (TP + TN + FP + FN)

适用场景：
- 数据集类别分布相对平衡时。
- 比如：判断图片里是否有猫，正负样本比例接近时使用准确率直观且有效。
```

---

### 2. Precision（精确率）

```text
定义：
在所有被模型预测为正样本的样本中，实际为正的比例。

公式：
Precision = TP / (TP + FP)

适用场景：
- 当“误报”成本高时（假阳性代价大）。
- 例子：垃圾邮件检测。若误将正常邮件归为垃圾，用户体验会受损，所以要高精确率。
```

---

### 3. Recall（召回率 / 灵敏度）

```text
定义：
在所有真实为正样本的样本中，模型正确识别出的比例。

公式：
Recall = TP / (TP + FN)

适用场景：
- 当“漏报”成本高时（假阴性代价大）。
- 例子：疾病筛查。如果没检测出病人（漏诊），后果严重，应提高召回率。
```

---

### 4. F1 Score（调和平均值）

```text
定义：
Precision 与 Recall 的调和平均数，兼顾两者的平衡。

公式：
F1 = 2 × (Precision × Recall) / (Precision + Recall)

适用场景：
- 当样本不平衡且希望平衡精确率与召回率时。
- 例子：情感分类任务中，正样本较少（比如负面评论占少数），F1比Accuracy更能反映真实性能。
```

---

### 5. AUROC（Area Under ROC Curve）

```text
定义：
ROC曲线下的面积，衡量模型区分正负样本的总体能力。

ROC曲线：以 FPR（假阳性率）为横轴，TPR（真正率=Recall）为纵轴绘制的曲线。

公式：
AUROC = ∫ TPR(FPR) dFPR （通常通过数值积分计算）

适用场景：
- 二分类模型整体评估，不依赖于阈值选择。
- 例子：信用评分系统。用于衡量模型能否正确排序高风险和低风险客户。
```

---

### 6. PR-ROC（Precision-Recall Curve / AUPRC）

```text
定义：
以 Recall 为横轴，Precision 为纵轴绘制的曲线；
AUPRC（曲线下面积）用于衡量模型在不平衡数据下的表现。

公式：
AUPRC = ∫ Precision(Recall) dRecall （通常通过数值积分计算）

适用场景：
- 样本极度不平衡的任务中更可靠。
- 例子：欺诈检测、癌症预测。正样本极少时，PR曲线比ROC曲线更能体现模型有效性。
```

---

### 🔹补充：关键对比总结

| 指标        | 强调点                    | 典型场景        |
| --------- | ---------------------- | ----------- |
| Accuracy  | 总体正确率                  | 类别平衡任务      |
| Precision | 少误报                    | 垃圾邮件检测      |
| Recall    | 少漏报                    | 疾病筛查        |
| F1        | Precision 与 Recall 的平衡 | 样本不平衡       |
| AUROC     | 排序能力                   | 信用评分、二分类    |
| PR-ROC    | 不平衡样本性能                | 欺诈检测、罕见事件识别 |

<!-- related:start -->
## 相关笔记

- [机器学习索引](%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%B4%A2%E5%BC%95.md)
- [mt-2面](../interview-prep/logs/2025/mt-2%E9%9D%A2.md)
- [模型评估](../llm/03-%E8%AE%AD%E7%BB%83%E4%B8%8E%E8%AF%84%E4%BC%B0/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0.md)
- [data_imbalance](../llm/08-%E6%95%B0%E6%8D%AE/data_imbalance.md)
- [金融违约风险检测](../llm/10-%E4%B8%9A%E5%8A%A1%E5%9C%BA%E6%99%AF/%E9%87%91%E8%9E%8D%E8%BF%9D%E7%BA%A6%E9%A3%8E%E9%99%A9%E6%A3%80%E6%B5%8B.md)
- [聚类.分类_算法](%E8%81%9A%E7%B1%BB.%E5%88%86%E7%B1%BB_%E7%AE%97%E6%B3%95.md)
<!-- related:end -->
