# Oracle Scheduler 文档归档

Oracle Database Scheduler 相关官方文档的本地归档，按官网目录结构组织，便于离线查阅与对照实现。

## 目录结构

```
en/                          # 英文（Oracle 19c）
  refrn/                     # Database Reference — 82 个 SCHEDULER 数据字典视图
    ALL_SCHEDULER_*.md
    DBA_SCHEDULER_*.md
    USER_SCHEDULER_*.md
  arpls/                     # PL/SQL Packages and Types Reference
    DBMS_SCHEDULER.md
  raw/                       # 原始 HTML（被 Oracle 模板 JS 遮蔽，故另存 Markdown）
    refrrn/
    arpls/
zh/                          # 中文（见下文说明）
```

## 内容

- **`en/refrn/`**：82 个 SCHEDULER 数据字典视图（`ALL_/DBA_/USER_SCHEDULER_*`），每个含完整列定义表（Column / Datatype / NULL / Description）。
- **`en/arpls/DBMS_SCHEDULER.md`**：`DBMS_SCHEDULER` 包内全部过程/函数，含语法代码块与参数表，包含 `CREATE_JOB` 等。

视图清单见 [INDEX.md](INDEX.md)。

## 关于中文版

Oracle 官网（含老版 `docs.oracle.com/cd` 系统）**已无简体中文数据库文档**：19c/12.2/12.1 新版中文路径全部 404，cd 老库仅保留日文翻译库。因此中文版无法从官方下载，需另行处理（机器翻译或日文版替代）——详见仓库内说明。

## 来源

- 英文 19c：https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ 、…/19/arpls/DBMS_SCHEDULER.html
- 日文 12.2（cd 老库，非中文）：https://docs.oracle.com/cd/E82638_01/

下载日期：2026-09-03
