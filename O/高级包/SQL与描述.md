# SQL与描述

SQL 执行与描述（对应 GaussDB DBE_SQL、DBE_DESCRIBE）。

---

## DBMS_SQL

**包用途**：提供用 PL/SQL 解析任意 DML/DDL 语句的动态 SQL 接口（如从存储过程执行 `DROP TABLE`）。多数情况原生动态 SQL（EXECUTE IMMEDIATE）更易用且性能更好，但 DBMS_SQL 支持 Method 4（输入/输出数未知）等场景。

**接口清单（全部）**：

| Subprogram | 说明 |
|---|---|
| BIND_ARRAY | 将给定值绑定到给定集合 |
| BIND_VARIABLE | 将给定值绑定到给定变量 |
| BIND_VARIABLE_PKG | 将给定值绑定到给定包变量 |
| CLOSE_CURSOR | 关闭给定游标并释放内存 |
| COLUMN_VALUE | 返回游标中指定位置元素的值 |
| COLUMN_VALUE_LONG | 返回用 DEFINE_COLUMN_LONG 定义的 LONG 列的选定部分 |
| DEFINE_ARRAY | 定义从给定游标选择的集合（仅 SELECT） |
| DEFINE_COLUMN | 定义从给定游标选择的列（仅 SELECT） |
| DEFINE_COLUMN_CHAR | 定义选择的 CHAR 类型列 |
| DEFINE_COLUMN_LONG | 定义选择的 LONG 列 |
| DEFINE_COLUMN_RAW | 定义选择的 RAW 类型列 |
| DEFINE_COLUMN_ROWID | 定义选择的 ROWID 类型列 |
| DESCRIBE_COLUMNS | 描述通过 DBMS_SQL 打开并解析的游标的列 |
| DESCRIBE_COLUMNS2 | 描述指定列（DESCRIBE_COLUMNS 的替代） |
| DESCRIBE_COLUMNS3 | 描述指定列（DESCRIBE_COLUMNS 的替代） |
| EXECUTE | 执行给定游标 |
| EXECUTE_AND_FETCH | 执行给定游标并取行 |
| FETCH_ROWS | 从给定游标取一行 |
| GET_NEXT_RESULT | 获取递归语句返回给调用者的下一条结果 |
| IS_OPEN | 游标是否打开 |
| LAST_ERROR_POSITION | 返回出错处 SQL 文本的字节偏移 |
| LAST_ROW_COUNT | 返回已取行的累计数 |
| LAST_ROW_ID | 返回最后处理行的 ROWID |
| LAST_SQL_FUNCTION_CODE | 返回语句的 SQL 函数码 |
| OPEN_CURSOR | 返回新游标的 ID 号 |
| PARSE | 解析给定语句 |
| RETURN_RESULT | 将已执行语句的结果返回给客户端应用 |
| TO_CURSOR_NUMBER | 将已打开的强/弱类型 ref 游标转为 DBMS_SQL 游标号 |
| TO_REFCURSOR | 将已打开、解析、执行的游标转为 PL/SQL 可用的 REF CURSOR |
| VARIABLE_VALUE | 返回给定游标中命名变量的值 |
| VARIABLE_VALUE_PKG | 返回包内命名变量的值（用于 returning 子句） |

---

## DBMS_DESCRIBE

**包用途**：声明两个 PL/SQL 表类型，用于保存 DESCRIBE_PROCEDURE 的 OUT 参数返回数据。功能同 OCI 的 OCIDescribeAny 调用。

| Subprogram | 说明 |
|---|---|
| DESCRIBE_PROCEDURE | 给出 PL/SQL 存储过程的简要描述 |
