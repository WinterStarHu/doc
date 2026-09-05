# 安全与ILM

安全/加密/ILM/压缩/热图（对应 GaussDB DBE_OBFUSCATION_TOOLKIT、DBE_ILM、DBE_COMPRESSION、DBE_HEAT_MAP）。

---

## DBMS_OBFUSCATION_TOOLKIT

**包用途**：数据加密/解密与哈希工具（DES、Triple-DES、MD5）。已基本被 DBMS_CRYPTO 取代。主要接口：DES3ENCRYPT/DES3DECRYPT（Triple-DES 加解密）、DESGETKEY/DES3GETKEY（生成密钥）、MD5/GETHASH（哈希）。（本版本未抽取到独立清单表，详见英文原版。）

## DBMS_ILM

**包用途**：用 ADO（自动数据优化）策略实现信息生命周期管理（ILM）。支持立即评估/执行 ADO 任务、向任务添加/移除对象、预览策略评估。

| Subprogram | 说明 |
|---|---|
| ADD_TO_ILM | 将指定对象加入某 ADO 任务并评估其上的 ADO 策略 |
| ARCHIVESTATENAME | 返回行归档启用表的 ORA_ARCHIVE_STATE 列值 |
| EXECUTE_ILM | 执行一个 ADO 任务 |
| EXECUTE_ILM_TASK | 执行先前已评估的 ADO 任务 |
| PREVIEW_ILM | 评估参数指定范围内的所有 ADO 策略 |
| REMOVE_FROM_ILM | 从某 ADO 任务移除指定对象 |
| STOP_ILM | 停止为某 ADO 任务创建的 ADO 相关作业 |

## DBMS_COMPRESSION

**包用途**：汇集压缩相关信息，含估计分区/非分区表可压缩性、获取已压缩表的行级压缩信息，辅助做压缩决策。

| Subprogram | 说明 |
|---|---|
| GET_COMPRESSION_RATIO | 分析表的压缩比，给出可压缩性信息 |
| GET_COMPRESSION_TYPE | 返回指定行的压缩类型 |

## DBMS_HEAT_MAP

**包用途**：在块/区/段/对象/表空间各级导出热图（数据访问与修改跟踪），用于 ILM 与 ADO。SYSTEM/SYSAUX 表空间不跟踪。

| Subprogram | 说明 |
|---|---|
| BLOCK_HEAT_MAP | 返回表段每块的最后修改时间 |
| EXTENT_HEAT_MAP | 返回表段的区级热图统计 |
| OBJECT_HEAT_MAP | 返回对象所有段的最小/最大/平均访问时间 |
| SEGMENT_HEAT_MAP | 返回给定段的热图属性 |
| TABLESPACE_HEAT_MAP | 返回表空间所有段的最小/最大/平均访问时间 |
