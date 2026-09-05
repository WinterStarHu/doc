# XML

XML 处理（对应 GaussDB DBE_XMLDOM、DBE_XMLPARSER、DBE_XMLGEN、DBE_XML）。

---

## DBMS_XMLDOM

**包用途**：访问 XMLType 对象，实现 DOM（文档对象模型）API，用于 HTML/XML 文档。可访问、修改、删除、添加文档节点；支持 schema 与非 schema 文档。文件读写须在服务器文件系统。

**接口清单（全部）**：

| Subprogram | 说明 |
|---|---|
| ADOPTNODE | 从另一文档收养节点 |
| APPENDCHILD | 向节点追加新子节点 |
| APPENDDATA | 向节点数据追加指定数据 |
| CLONENODE | 克隆节点 |
| CREATEATTRIBUTE | 创建属性 |
| CREATECDATASECTION | 创建 CDataSection 节点 |
| CREATECOMMENT | 创建注释节点 |
| CREATEDOCUMENT | 创建新文档 |
| CREATEDOCUMENTFRAGMENT | 创建新文档片段 |
| CREATEELEMENT | 创建新元素 |
| CREATEENTITYREFERENCE | 创建实体引用 |
| CREATEPROCESSINGINSTRUCTION | 创建处理指令 |
| CREATETEXTNODE | 创建文本节点 |
| DELETEDATA | 从指定偏移删除数据 |
| FINDENTITY | 在文档类型中查找指定实体 |
| FINDNOTATION | 在文档类型中查找指定记法 |
| FREEDOCFRAG | 释放文档片段 |
| FREEDOCUMENT | 释放文档 |
| FREEELEMENT | 释放 DOMElement 句柄内存 |
| FREENODE | 释放节点关联的所有资源 |
| FREENODELIST | 释放节点列表关联的所有资源 |
| GETATTRIBUTE | 按名取属性节点 |
| GETATTRIBUTENODE | 按名取属性节点 |
| GETATTRIBUTES | 取节点属性 |
| GETCHARSET | 取 DOM 文档字符集 |
| GETCHILDNODES | 取节点子节点 |
| GETCHILDRENBYTAGNAME | 按标签名取元素子节点 |
| GETDATA | 取节点数据/处理指令数据 |
| GETDOCTYPE | 取文档 DTD |
| GETDOCUMENTELEMENT | 取文档根元素 |
| GETELEMENTSBYTAGNAME | 按标签名取节点列表/子树元素 |
| GETENTITIES | 取文档类型中的实体节点映射 |
| GETEXPANDEDNAME | 取节点/属性/元素的展开名 |
| GETFIRSTCHILD | 取节点第一个子节点 |
| GETIMPLEMENTATION | 取 DOM 实现 |
| GETLASTCHILD | 取节点最后一个子节点 |
| GETLENGTH | 取数据长度/映射项数/列表项数 |
| GETLOCALNAME | 取限定名的本地部分/属性本地名/元素本地名 |
| GETNAME | 取属性名/文档类型名 |
| GETNAMEDITEM | 按名与命名空间 URI 取项 |
| GETNAMESPACE | 取节点/属性/元素的命名空间 URI |
| GETNEXTSIBLING | 取节点下一个兄弟 |
| GETNODENAME | 取节点名 |
| GETNODETYPE | 取节点类型 |
| GETNODEVALUE | 取节点值 |
| GETNODEVALUEASBINARYSTREAM | 以二进制流取节点值 |
| GETNODEVALUEASCHARACTERSTREAM | 以字符流取节点值 |
| GETNOTATIONNAME | 取实体记法名 |
| GETNOTATIONS | 取文档类型中的记法节点映射 |
| GETTARGET | 取处理指令目标 |
| GETOWNERDOCUMENT | 取节点所属文档 |
| GETOWNERELEMENT | 取属性的父元素节点 |
| GETPARENTNODE | 取节点父节点 |
| GETPREFIX | 取命名空间前缀 |
| GETPREVIOUSSIBLING | 取节点上一个兄弟 |
| GETPUBLICID | 取文档类型/实体/记法的 public ID |
| GETQUALIFIEDNAME | 取属性/元素的限定名 |
| GETSCHEMANODE | 取关联的 schema URI |
| GETSPECIFIED | 测试元素中是否指定了该属性 |
| GETSTANDALONE | 取文档 standalone 属性 |
| GETSYSTEMID | 取文档类型/实体/记法的 system ID |
| GETTAGNAME | 取元素标签名 |
| GETVALUE | 取属性值 |
| GETVERSION | 取文档版本 |
| GETXMLTYPE | 取与 DOM 文档关联的 XMLType |
| HASATTRIBUTES | 测试节点是否有属性 |
| HASATTRIBUTE | 测试属性是否存在 |
| HASCHILDNODES | 测试节点是否有子节点 |
| HASFEATURE | 测试 DOMImplementation 是否实现某特性 |
| IMPORTNODE | 从另一文档导入节点 |
| INSERTBEFORE | 在参照子节点前插入子节点 |
| INSERTDATA | 在节点指定偏移插入数据 |
| ISNULL | 测试节点/各类型节点是否为 NULL |
| ITEM | 按索引取映射/列表中的项 |
| MAKEATTR | 将节点转为属性 |
| MAKECDATASECTION | 将节点转为 CData Section |
| MAKECHARACTERDATA | 将节点转为 CharacterData |
| MAKECOMMENT | 将节点转为注释 |
| MAKEDOCUMENT | 将节点转为 DOM 文档 |
| MAKEDOCUMENTFRAGMENT | 将节点转为文档片段 |
| MAKEDOCUMENTTYPE | 将节点转为文档类型 |
| MAKEELEMENT | 将节点转为元素 |
| MAKEENTITY | 将节点转为实体 |
| MAKEENTITYREFERENCE | 将节点转为实体引用 |
| MAKENODE | 将各类型节点转为通用节点 |
| MAKENOTATION | 将节点转为记法 |
| MAKEPROCESSINGINSTRUCTION | 将节点转为处理指令 |
| MAKETEXT | 将节点转为文本 |
| NEWDOMDOCUMENT | 创建新文档 |
| NORMALIZE | 规范化元素的文本子节点 |
| REMOVEATTRIBUTE | 按名移除属性 |
| REMOVEATTRIBUTENODE | 移除元素中的属性节点 |
| REMOVECHILD | 从节点移除指定子节点 |
| REMOVENAMEDITEM | 按名移除项 |
| REPLACECHILD | 用新子节点替换旧子节点 |
| REPLACEDATA | 替换节点中一段字符 |
| RESOLVENAMESPACEPREFIX | 将前缀解析为命名空间 URI |
| SETATTRIBUTE | 按名设置属性 |
| SETATTRIBUTENODE | 在元素中设置属性节点 |
| SETCHARSET | 设置 DOM 文档字符集 |
| SETDATA | 设置节点数据/处理指令数据 |
| SETDOCTYPE | 设置文档 DTD |
| SETNAMEDITEM | 按名在映射中设置项 |
| SETNODEVALUE | 设置节点值 |
| SETNODEVALUEASBINARYSTREAM | 以二进制流设置节点值 |
| SETNODEVALUEASCHARACTERSTREAM | 以字符流设置节点值 |
| SETPREFIX | 设置命名空间前缀 |
| SETSTANDALONE | 设置文档 standalone 属性 |
| SETVALUE | 设置属性值 |
| SETVERSION | 设置文档版本 |
| SPLITTEXT | 将文本节点内容拆为两个文本节点 |
| SUBSTRINGDATA | 取数据子串 |
| USEBINARYSTREAM | 标记该流可用于使用 |
| WRITETOBUFFER | 将节点/文档/文档片段内容写入缓冲区 |
| WRITETOCLOB | 将节点/文档内容写入 CLOB |
| WRITETOFILE | 将节点/文档内容写入文件 |

---

## DBMS_XMLGEN

**包用途**：将 SQL 查询结果转为规范 XML 格式，以 CLOB 返回；用 C 编写编译进内核。

| Subprogram | 说明 |
|---|---|
| CLOSECONTEXT | 关闭上下文并释放所有资源 |
| CONVERT | 将 XML 转为转义/非转义等价形式 |
| GETNUMROWSPROCESSED | 获取上次 GETXML 调用处理的 SQL 行数 |
| GETXML | 获取 XML 文档 |
| GETXMLTYPE | 获取 XML 文档并以 XMLType 返回 |
| NEWCONTEXT | 创建新上下文句柄 |
| NEWCONTEXTFROMHIERARCHY | 获取用于生成带递归元素层级 XML 的句柄 |
| RESTARTQUERY | 重启查询从头取 |
| SETCONVERTSPECIALCHARS | 设置是否将 $ 等非 XML 特殊字符转义 |
| SETMAXROWS | 设置每次取的最大行数 |
| SETNULLHANDLING | 设置 NULL 处理选项 |
| SETROWSETTAG | 设置包络整个结果的元素名 |
| SETROWTAG | 设置包络每行的元素名 |
| SETSKIPROWS | 设置每次生成 XML 前跳过的行数 |
| USEITEMTAGSFORCOLL | 强制集合元素用集合列名加 _ITEM 标签 |
| USENULLATTRIBUTEINDICATOR | 指定用 XML 属性指示 NULL 还是通过省略实体 |

---

## DBMS_XMLPARSER

**包用途**：XML 解析器，将 XML 文档解析为 DOM 树以便访问与修改。（本版本未抽取到独立接口清单表，详见英文原版 `O/en/arpls/DBMS_XMLPARSER.html`。）

## DBMS_XML

**包用途**：XML 相关基础功能。（本版本未抽取到独立概述/清单，详见英文原版。）
