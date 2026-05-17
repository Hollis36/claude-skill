---
name: experiment-tracking
description: |
  实验追踪与管理助手，帮助科研人员记录、组织和管理实验数据。支持电子实验记录本（ELN）最佳实践、实验版本控制、数据溯源、FAIR数据原则。当用户需要：(1) 记录实验流程和参数、(2) 管理实验数据和结果、(3) 追踪实验版本和变更、(4) 确保实验可重复性时触发。关键词：实验记录、lab notebook、实验管理、数据追踪、实验版本控制。
license: Apache-2.0
---

# 实验追踪与管理助手

帮助科研人员系统化地记录、组织和管理实验数据，确保研究的可重复性和可追溯性。

## 核心功能

### 1. 电子实验记录本（ELN）最佳实践
### 2. 实验版本控制
### 3. 数据溯源与元数据管理
### 4. FAIR 数据原则实施

## 工作流程

### 第一步：实验设计与计划

在开始实验前，记录完整的实验设计：

```markdown
# 实验记录模板

## 实验信息
- **实验编号**: EXP-2026-001
- **实验日期**: 2026-04-06
- **实验人员**: [姓名]
- **实验目的**: [简要描述实验目标]

## 实验设计
- **假设**: [研究假设]
- **变量**:
  - 自变量: [列出自变量及其水平]
  - 因变量: [列出因变量]
  - 控制变量: [列出需要控制的变量]
- **样本量**: [样本数量及计算依据]
- **分组**: [实验组、对照组设计]

## 材料与试剂
| 名称 | 规格/型号 | 批号 | 供应商 | 浓度/用量 |
|------|-----------|------|--------|-----------|
|      |           |      |        |           |

## 设备仪器
| 设备名称 | 型号 | 编号 | 校准日期 | 备注 |
|----------|------|------|----------|------|
|          |      |      |          |      |

## 实验步骤
1. [详细步骤1]
   - 参数设置：
   - 预期时间：
   - 注意事项：

2. [详细步骤2]
   ...

## 数据记录计划
- **原始数据格式**: [文件格式]
- **数据存储位置**: [路径/服务器]
- **备份策略**: [备份频率和位置]
```

### 第二步：实验执行与实时记录

#### 实时记录原则
1. **即时性**：实验过程中立即记录，不要事后补录
2. **完整性**：记录所有操作，包括失败和意外情况
3. **客观性**：如实记录观察结果，不做主观判断
4. **可追溯性**：记录时间戳、操作人员、设备参数

```python
# Python 实验记录辅助工具
import json
import datetime
from pathlib import Path

class ExperimentLogger:
    """实验记录工具类"""

    def __init__(self, experiment_id, output_dir="./experiments"):
        self.experiment_id = experiment_id
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.output_dir / f"{experiment_id}_log.json"
        self.logs = []

    def log_event(self, event_type, description, **kwargs):
        """记录实验事件

        Args:
            event_type: 事件类型 (start, step, observation, issue, end)
            description: 事件描述
            **kwargs: 额外参数（如温度、时间、浓度等）
        """
        event = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": event_type,
            "description": description,
            **kwargs
        }
        self.logs.append(event)
        self._save_logs()
        print(f"[{event['timestamp']}] {event_type.upper()}: {description}")

    def log_parameters(self, **params):
        """记录实验参数"""
        self.log_event("parameters", "Experiment parameters", parameters=params)

    def log_observation(self, observation, measurement=None):
        """记录观察结果"""
        self.log_event("observation", observation, measurement=measurement)

    def log_issue(self, issue, resolution=None):
        """记录问题和解决方案"""
        self.log_event("issue", issue, resolution=resolution)

    def _save_logs(self):
        """保存日志到文件"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump({
                "experiment_id": self.experiment_id,
                "logs": self.logs
            }, f, indent=2, ensure_ascii=False)

    def export_markdown(self):
        """导出为 Markdown 格式"""
        md_file = self.output_dir / f"{self.experiment_id}_report.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# Experiment Log: {self.experiment_id}\n\n")
            for log in self.logs:
                f.write(f"## {log['timestamp']} - {log['type']}\n")
                f.write(f"{log['description']}\n\n")
                if 'parameters' in log:
                    f.write("**Parameters:**\n")
                    for k, v in log['parameters'].items():
                        f.write(f"- {k}: {v}\n")
                f.write("\n")

# 使用示例
logger = ExperimentLogger("EXP-2026-001")
logger.log_event("start", "开始细胞培养实验")
logger.log_parameters(
    temperature="37°C",
    CO2_concentration="5%",
    medium="DMEM + 10% FBS",
    cell_density="1e5 cells/mL"
)
logger.log_observation("细胞贴壁良好，形态正常")
logger.log_issue("培养箱温度波动", resolution="已联系维修，更换温控器")
logger.log_event("end", "实验结束")
logger.export_markdown()
```

### 第三步：数据管理与组织

#### 数据组织结构

```
project-name/
├── README.md                 # 项目总体说明
├── experiments/              # 实验记录目录
│   ├── EXP-001/
│   │   ├── protocol.md       # 实验方案
│   │   ├── log.json          # 实验日志
│   │   ├── raw_data/         # 原始数据
│   │   │   ├── sample1.csv
│   │   │   └── sample2.csv
│   │   ├── processed_data/   # 处理后数据
│   │   └── analysis/         # 分析脚本和结果
│   │       ├── analysis.ipynb
│   │       └── figures/
│   ├── EXP-002/
│   └── ...
├── data/                     # 共享数据
│   ├── reference/            # 参考数据
│   └── metadata/             # 元数据
├── code/                     # 共享代码和脚本
│   ├── preprocessing/
│   ├── analysis/
│   └── utils/
└── docs/                     # 文档
    ├── protocols/            # 标准操作规程
    └── notes/                # 研究笔记
```

#### 元数据标准

使用 JSON 格式记录实验元数据：

```json
{
  "experiment_id": "EXP-2026-001",
  "title": "细胞毒性实验：化合物A对HeLa细胞的影响",
  "date": "2026-04-06",
  "researcher": {
    "name": "张三",
    "orcid": "0000-0001-2345-6789",
    "affiliation": "某大学生物系"
  },
  "project": "抗癌药物筛选",
  "keywords": ["细胞毒性", "HeLa细胞", "化合物A", "MTT"],
  "materials": [
    {
      "name": "化合物A",
      "cas_number": "123-45-6",
      "supplier": "Sigma-Aldrich",
      "catalog": "A1234",
      "lot_number": "SLCD1234"
    }
  ],
  "equipment": [
    {
      "name": "酶标仪",
      "model": "BioTek Synergy H1",
      "serial": "SN12345",
      "calibration_date": "2026-01-15"
    }
  ],
  "conditions": {
    "temperature": "37°C",
    "humidity": "85%",
    "CO2": "5%"
  },
  "data_files": [
    "raw_data/absorbance_readings.csv",
    "processed_data/viability_results.csv"
  ],
  "related_experiments": ["EXP-2026-000", "EXP-2026-002"],
  "protocol_doi": "10.17504/protocols.io.xxxxx",
  "notes": "实验过程顺利，无异常情况"
}
```

### 第四步：版本控制与变更追踪

#### Git 版本控制最佳实践

```bash
# 初始化 Git 仓库
git init
git lfs install  # 安装 Git LFS 用于大文件管理

# 配置 .gitignore
cat > .gitignore << 'EOF'
# 临时文件
*.tmp
*.log
*~

# 大型原始数据文件（使用 Git LFS）
*.nd2
*.tif
*.czi
*.lif

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/

# R
.Rhistory
.RData

# 系统文件
.DS_Store
Thumbs.db
EOF

# 配置 Git LFS 追踪大文件
git lfs track "*.tif"
git lfs track "*.nd2"
git lfs track "*.csv"

# 提交实验记录
git add experiments/EXP-001/
git commit -m "EXP-001: 初始细胞毒性实验

- 测试化合物A对HeLa细胞的影响
- 浓度梯度: 0, 1, 10, 100 μM
- 时间点: 24, 48, 72 小时
- 方法: MTT assay"

# 标记实验版本
git tag -a EXP-001-v1.0 -m "EXP-001 实验完成版本"
```

#### 实验变更日志

```markdown
# 实验变更日志 - EXP-2026-001

## v1.2 - 2026-04-08
**变更类型**: 方案修订
- **变更内容**: 增加72小时时间点
- **原因**: 初步结果显示效应延迟
- **影响**: 需要额外样本和测量
- **审批**: 导师已批准

## v1.1 - 2026-04-07
**变更类型**: 问题修正
- **变更内容**: 更换培养基批号
- **原因**: 原批号培养基污染
- **影响**: 可能影响结果一致性，需在分析中注明
- **决策**: 继续实验，但标注批号变更

## v1.0 - 2026-04-06
**初始版本**: 实验方案确定
```

### 第五步：FAIR 数据原则实施

#### FAIR 原则
- **F**indable（可发现）：数据有唯一标识符和丰富元数据
- **A**ccessible（可访问）：数据可通过标准协议访问
- **I**nteroperable（可互操作）：数据使用标准格式和词汇
- **R**eusable（可重用）：数据有清晰的使用许可和来源

```python
# FAIR 数据元数据生成工具
import json
from datetime import datetime
from pathlib import Path

class FAIRMetadata:
    """FAIR数据元数据管理"""

    def __init__(self):
        self.metadata = {
            "@context": "https://schema.org/",
            "@type": "Dataset",
            "dateCreated": datetime.now().isoformat(),
            "version": "1.0"
        }

    def add_basic_info(self, name, description, keywords):
        """添加基本信息（Findable）"""
        self.metadata.update({
            "name": name,
            "description": description,
            "keywords": keywords,
            "identifier": f"doi:10.xxxx/{name.lower().replace(' ', '-')}"
        })

    def add_creator(self, name, orcid=None, affiliation=None):
        """添加创建者信息"""
        creator = {"@type": "Person", "name": name}
        if orcid:
            creator["@id"] = f"https://orcid.org/{orcid}"
        if affiliation:
            creator["affiliation"] = {"@type": "Organization", "name": affiliation}
        self.metadata["creator"] = creator

    def add_distribution(self, format_type, url=None):
        """添加数据分发信息（Accessible）"""
        distribution = {
            "@type": "DataDownload",
            "encodingFormat": format_type
        }
        if url:
            distribution["contentUrl"] = url
        self.metadata["distribution"] = distribution

    def add_license(self, license_type="CC-BY-4.0"):
        """添加许可证信息（Reusable）"""
        licenses = {
            "CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/",
            "CC0": "https://creativecommons.org/publicdomain/zero/1.0/",
            "MIT": "https://opensource.org/licenses/MIT"
        }
        self.metadata["license"] = licenses.get(license_type, license_type)

    def add_measurement_technique(self, technique):
        """添加测量技术（Interoperable）"""
        self.metadata["measurementTechnique"] = technique

    def save(self, output_file):
        """保存元数据"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)

# 使用示例
fair = FAIRMetadata()
fair.add_basic_info(
    name="Cell Viability Assay - Compound A",
    description="MTT assay measuring HeLa cell viability after treatment with Compound A",
    keywords=["cell viability", "MTT assay", "HeLa cells", "cytotoxicity"]
)
fair.add_creator("张三", orcid="0000-0001-2345-6789", affiliation="某大学")
fair.add_distribution(format_type="text/csv", url="https://doi.org/10.xxxx/data")
fair.add_license("CC-BY-4.0")
fair.add_measurement_technique("MTT Colorimetric Assay")
fair.save("experiments/EXP-001/metadata.json")
```

## 数据备份策略

### 3-2-1 备份原则
- **3** 份数据副本：1 个原始 + 2 个备份
- **2** 种不同存储介质：本地硬盘 + 云存储
- **1** 份异地备份：防止物理灾难

```bash
# 自动备份脚本示例
#!/bin/bash

# 配置
PROJECT_DIR="/path/to/project"
BACKUP_LOCAL="/path/to/backup/drive"
BACKUP_CLOUD="user@cloud-server:/backup"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 创建备份
tar -czf "${BACKUP_LOCAL}/backup_${TIMESTAMP}.tar.gz" "${PROJECT_DIR}"

# 同步到云端
rsync -avz "${BACKUP_LOCAL}/" "${BACKUP_CLOUD}/"

# 保留最近30天的备份
find "${BACKUP_LOCAL}" -name "backup_*.tar.gz" -mtime +30 -delete

echo "Backup completed: ${TIMESTAMP}"
```

## 常用工具推荐

### 电子实验记录本（ELN）工具

| 工具 | 类型 | 特点 | 适用场景 |
|------|------|------|----------|
| **Jupyter Lab** | 开源 | 代码+文档结合，支持多种语言 | 计算密集型实验 |
| **RSpace** | 商业/学术免费 | 符合GLP/GMP规范，签名和审计追踪 | 需要合规性的实验室 |
| **LabArchives** | 商业 | 云端协作，移动端支持 | 团队协作 |
| **Benchling** | 商业 | 生物学专用，质粒和序列管理 | 分子生物学实验室 |
| **eLabFTW** | 开源 | 自托管，完全控制数据 | 注重隐私的实验室 |
| **SciNote** | 开源/商业 | 项目管理集成 | 多项目管理 |

### 数据管理工具

```python
# 常用Python数据管理库
import pandas as pd          # 数据处理
import openpyxl              # Excel 读写
import h5py                  # HDF5 大数据存储
import zarr                  # 云优化的数组存储
import dvc                   # 数据版本控制（需单独安装）

# 示例：使用 HDF5 存储大型实验数据
import h5py
import numpy as np

with h5py.File('experiment_data.h5', 'w') as f:
    # 创建数据集
    f.create_dataset('raw_images', data=raw_images, compression='gzip')

    # 添加元数据属性
    f.attrs['experiment_id'] = 'EXP-2026-001'
    f.attrs['date'] = '2026-04-06'
    f.attrs['instrument'] = 'Nikon Ti2-E'

    # 分组组织数据
    grp = f.create_group('processed')
    grp.create_dataset('segmented', data=segmented_images)
    grp.create_dataset('measurements', data=measurements)
```

## 实验可重复性检查清单

在发表或分享实验结果前，确保：

- [ ] 实验方案完整记录，包含所有关键参数
- [ ] 所有试剂和材料有批号和供应商信息
- [ ] 设备型号、编号和校准日期已记录
- [ ] 原始数据已备份（至少2个不同位置）
- [ ] 数据处理步骤有文档或代码记录
- [ ] 分析代码可执行（包含依赖项和版本信息）
- [ ] 元数据符合 FAIR 原则
- [ ] 实验变更有记录和说明
- [ ] 异常情况和问题已记录
- [ ] 数据和代码有版本标签

## 常见问题与解决方案

### Q1: 如何处理实验失败？
**A**: 失败的实验同样有价值！记录：
- 失败的具体表现
- 可能的原因分析
- 采取的排查步骤
- 最终解决方案或未解决原因

### Q2: 原始数据应该保存多久？
**A**: 建议：
- 发表论文相关数据：至少10年
- 专利相关数据：至少20年
- 临床试验数据：遵循法规要求（通常15-25年）
- 参考所在机构和期刊的数据保存政策

### Q3: 如何处理敏感数据？
**A**:
- 使用加密存储（BitLocker, VeraCrypt）
- 限制访问权限
- 匿名化个人信息（HIPAA, GDPR合规）
- 记录数据访问日志
- 定期安全审计

### Q4: 团队协作时如何避免数据冲突？
**A**:
- 使用版本控制系统（Git）
- 建立文件命名规范
- 使用协作平台（SharePoint, Google Drive）
- 定期同步和备份
- 明确数据所有权和编辑权限

## 参考资源

- [FAIR Data Principles](https://www.go-fair.org/fair-principles/)
- [Data Management Plans](https://dmptool.org/)
- [Jupyter Best Practices](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html)
- [Git for Scientists](https://www.nature.com/articles/d41586-018-05990-5)
- [Ten Simple Rules for Reproducible Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
