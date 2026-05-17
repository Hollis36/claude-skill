# /debug — 科研代码系统调试

调用 `skills/systematic-debugging/` — 4 阶段系统化调试流程。

## 4 阶段（不要跳步）

### Phase 1: 复现与隔离

- 最小复现样本（minimal reproducible example）
- 固定 seed
- 确认非偶发
- 隔离环境（清掉缓存、用新进程）

### Phase 2: 假设与验证

- **列出所有可能原因**（不只是第一个想到的）
- 按"先排除最容易验证的"顺序
- 每验证一条记录结果

### Phase 3: 定位

- 二分法（git bisect / 注释一半代码）
- 对比正确实现（git diff / 重新克隆）
- 检查数值范围（NaN / Inf / 量级）
- 检查 shape / dtype 不匹配

### Phase 4: 修复 + 防回归

- 修复后写测试（防同样问题再现）
- 文档化 root cause（在 commit / 项目日志）
- 检查同类问题是否在别处

## 科研代码常见 root cause

| 症状 | 常见原因 |
|------|---------|
| Loss 不降 / NaN | lr 太大、梯度爆炸、数据归一化错 |
| Loss 降但指标不升 | 评估代码 bug、train/eval mode 错 |
| 单 seed 好，多 seed 差 | over-fitting 偶然性 |
| 复现不出 paper 数字 | hyper 不一致、数据 split 不同、库版本差异 |
| GPU 显存爆 | batch 太大、忘 `.detach()`、graph 没释放 |
| 训练慢 | data loader 瓶颈、混精未启用、IO 阻塞 |
| 结果"太好" | 数据泄漏 → **首要嫌疑** |

## 配套资源

- `skills/systematic-debugging/SKILL.md`
- 若涉及统计异常，配 `knowledge/methods/statistical-testing-ml.md`

$ARGUMENTS
