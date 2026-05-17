# /venue — 目标会议 / 期刊查询

按目标会议名（NeurIPS / ICML / ICLR / CVPR / ACL / EMNLP / NAACL）查询投稿信息。

## 资源

- `knowledge/venues/neurips.md`
- `knowledge/venues/icml.md`
- `knowledge/venues/iclr.md`
- `knowledge/venues/cvpr.md`
- `knowledge/venues/acl-emnlp.md`

## 流程

1. **识别用户问的会议**（从 $ARGUMENTS）
2. **读对应 `knowledge/venues/<venue>.md`** 输出关键信息：
   - Deadline
   - 格式（页数、模板、匿名）
   - 必填材料（checklist / impact / limitations）
   - 评审流程（score 范围、rebuttal 规则）
3. **若 deadline 临近**（< 1 个月）：主动提醒投稿前 5 分钟 checklist
4. **若用户问"现在投哪个"**：列对比表（按下一个 deadline 排序）

## 若知识库无对应 venue

诚实告知 Hollis 库里没有，然后选择：
- 用 WebFetch 查官网最新信息
- 建议 Hollis 让我补一个 `knowledge/venues/<name>.md`

不要硬编造 deadline。

$ARGUMENTS
