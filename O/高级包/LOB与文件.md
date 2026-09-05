# LOB与文件

大对象与文件读写（对应 GaussDB DBE_LOB、DBE_FILE）。

---

## DBMS_LOB

**包用途**：操作 BLOB/CLOB/NCLOB/BFILE 及临时 LOB 的子程序。可读写、修改 LOB 的特定部分或整体；对 BFILE 提供只读操作。

**接口清单（全部）**：

| Subprogram | 说明 |
|---|---|
| APPEND | 将源 LOB 内容追加到目标 LOB |
| CLOB2FILE | 将 CLOB 内容写入文件 |
| CLOSE | 关闭先前打开的内部或外部 LOB |
| COMPARE | 比较两个整体 LOB 或其部分 |
| CONVERTTOBLOB | 将源 CLOB 字符数据转为二进制写入目标 BLOB，返回新偏移 |
| CONVERTTOCLOB | 将源 BLOB 二进制转为字符数据写入目标 CLOB，返回新偏移 |
| COPY | 将源 LOB 的全部或部分复制到目标 LOB |
| COPY_DBFS_LINK | 将源 LOB 的 DBFS 链接复制到目标 LOB |
| COPY_FROM_DBFS_LINK | 从 DBFS 存储取该 LOB 数据 |
| CREATETEMPORARY | 在用户默认临时表空间创建临时 BLOB/CLOB 及其索引 |
| DBFS_LINK_GENERATE_PATH | 返回用于创建 DBFS 链接的唯一文件路径名 |
| ERASE | 擦除 LOB 的全部或部分 |
| FILECLOSE | 关闭文件 |
| FILECLOSEALL | 关闭所有先前打开的文件 |
| FILEEXISTS | 检查文件在服务器上是否存在 |
| FILEGETNAME | 获取目录对象名与文件名 |
| FILEISOPEN | 检查文件是否用输入 BFILE 定位符打开 |
| FILEOPEN | 打开文件 |
| FRAGMENT_DELETE | 从 LOB 指定偏移起删除指定长度数据 |
| FRAGMENT_INSERT | 在 LOB 指定偏移插入指定数据（≤32K） |
| FRAGMENT_MOVE | 从指定偏移将指定字节数（BLOB）或字符数（CLOB/NCLOB）移到新偏移 |
| FRAGMENT_REPLACE | 用指定数据替换指定偏移处数据（≤32K） |
| FREETEMPORARY | 释放默认临时表空间中的临时 BLOB/CLOB |
| GET_DBFS_LINK | 返回指定 SecureFile 关联的 DBFS 链接路径 |
| GET_DBFS_LINK_STATE | 取指定 SecureFile 的当前 DBFS 链接状态 |
| GETCHUNKSIZE | 返回 LOB 块中存储 LOB 值所用空间量 |
| GETCONTENTTYPE | 返回先前由 SETCONTENTTYPE 设置的内容 ID 字符串 |
| GETLENGTH | 获取 LOB 值长度 |
| GETOPTIONS | 取特定 LOB 对应 option_type 字段的设置 |
| GET_STORAGE_LIMIT | 返回数据库配置中 LOB 的存储上限 |
| INSTR | 返回模式在 LOB 中第 n 次匹配的位置 |
| ISOPEN | 检查 LOB 是否已用输入定位符打开 |
| ISREMOTE | 检查 LOB 是本地还是属于远程数据库 |
| ISSECUREFILE | 是否 SecureFile LOB |
| ISTEMPORARY | 检查定位符是否指向临时 LOB |
| LOADBLOBFROMFILE | 将 BFILE 数据载入内部 BLOB |
| LOADCLOBFROMFILE | 将 BFILE 数据载入内部 CLOB |
| LOADFROMFILE | 将 BFILE 数据载入内部 LOB（自 12.2 已弃用） |
| MOVE_TO_DBFS_LINK | 将指定 SecureFile 数据写入 DBFS 存储 |
| OPEN | 以指定模式打开 LOB（内部/外部/临时） |
| READ | 从指定偏移读取 LOB 数据 |
| SET_DBFS_LINK | 将指定 SecureFile 链接到指定路径名（不复制数据） |
| SETCONTENTTYPE | 设置 LOB 中数据的内容类型字符串 |
| SETOPTIONS | 按 LOB 启用 CSCE 特性，覆盖默认 LOB 列设置 |
| SUBSTR | 从指定偏移返回 LOB 值的一部分 |
| TRIM | 将 LOB 值修剪到指定较短长度 |
| WRITE | 从指定偏移向 LOB 写数据 |
| WRITEAPPEND | 向 LOB 末尾写缓冲区 |

---

## UTL_FILE

**包用途**：服务端 PL/SQL 文件 I/O，类似客户端 TEXT_IO；用 PL/SQL 异常返回错误。

**接口清单（全部）**：

| Subprogram | 说明 |
|---|---|
| FCLOSE | 关闭文件 |
| FCLOSE_ALL | 关闭所有打开的文件句柄 |
| FCOPY | 将文件的连续部分复制到新文件 |
| FFLUSH | 将所有待输出物理写入文件 |
| FGETATTR | 读取并返回磁盘文件属性 |
| FGETPOS | 返回文件内当前相对偏移（字节） |
| FOPEN | 打开文件用于输入或输出 |
| FOPEN_NCHAR | 以 Unicode 打开文件用于输入或输出 |
| FREMOVE | 删除磁盘文件（须有足够权限） |
| FRENAME | 重命名文件（类似 UNIX mv） |
| FSEEK | 按指定字节数前/后调整文件指针 |
| GET_LINE | 从打开文件读文本 |
| GET_LINE_NCHAR | 以 Unicode 从打开文件读文本 |
| GET_RAW | 从文件读 RAW 值并前移文件指针 |
| IS_OPEN | 文件句柄是否指向打开的文件 |
| NEW_LINE | 向文件写一个或多个 OS 行结束符 |
| PUT | 向文件写字符串 |
| PUT_LINE | 向文件写一行并追加 OS 行结束符 |
| PUT_LINE_NCHAR | 向文件写 Unicode 行 |
| PUT_NCHAR | 向文件写 Unicode 字符串 |
| PUTF | 带格式的 PUT |
| PUTF_NCHAR | 带格式的 PUT_NCHAR（写 Unicode） |
| PUT_RAW | 接受 RAW 值写入输出缓冲区 |
