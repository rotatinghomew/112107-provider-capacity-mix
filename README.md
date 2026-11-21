# 服务机构能力结构与区域承接缺口分析

以下资料为合成记录，不含实际个人信息。文件以 UTF-8 编码，普通字段含日期或本地时间（东八区），分号表示同一字段的多值。空值表示在该记录中未提供，不自动当零。表内的凭据编号用于核对记录归属。

## 数据来源

- `data/skills.csv`：班组和被核验的服务资质；until 不含。
- `data/shift_offers.csv`：physical_shift 相同时属同一班组实际班，不可在两处同时承担。
- `data/travel.csv`：转站最短通勤时间，分钟。
- `data/tenders.csv`：报价包允许的签署范围，金额单位分；excludes 为互斥包。
- `data/floor_contracts.csv`：本轮前已承诺覆盖与先保地区约定。
- `data/tender_policy.csv`：续签会议使用的门槛和优先顺序，覆盖概率用小数。
- `data/assignment_history.csv`：旧轮次真实发派与承接记录；即使出现时段提前停派，也保留停止前实际发出的合格任务。

## 环境及检查

使用 Python 3.11.2 标准库，无需网络或额外安装。在项目目录可执行 `python3 -m unittest discover -s tests -v` 核对输入文件、表头与记录形状。各来源字段及记录数量见 `data-contract.json`。目前提供资料读取检查，不生成业务分析结果。
