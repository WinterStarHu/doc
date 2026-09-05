# 安全与ILM

> 中文概述与接口清单见 [`中文速览.md`](中文速览.md)；下为英文详细语法（参考）。


安全/加密/ILM/压缩/热图（对应 GaussDB DBE_OBFUSCATION_TOOLKIT、DBE_ILM、DBE_COMPRESSION、DBE_HEAT_MAP）。
（英文原文，待精译；与 GaussDB `G/高级包/安全与ILM.md` 对应。）

---

## DBMS_OBFUSCATION_TOOLKIT

（抓取失败/未收录。）

---

## DBMS_ILM

## DBMS_ILM
The `DBMS_ILM` package provides an interface for implementing Information Lifecycle Management (ILM) strategies using Automatic Data Optimization (ADO) policies.
This chapter contains the following topics:
- Overview
- Security Model
- Constants
- Exceptions
- Summary of DBMS_ILM Subprograms
See Also:
- Oracle Database VLDB and Partitioning Guide for information about managing Automatic Data Optimization (ADO) with this package
- DBMS_ILM_ADMIN
- DBMS_HEAT_MAP
### DBMS_ILM Overview
To implement your ILM strategy, you can use Heat Map in Oracle Database to track data access and modification. You can also use Automatic Data Optimization (ADO) to automate the compression and movement of data between different tiers of storage within the database. The `DBMS_ILM` package supports immediate evaluation or execution of ADO related tasks. T
he package supports the following two ways for scheduling ADO actions.
- A database user schedules immediate ADO policy execution on a set of objects.
- A database user views the results of evaluation of ADO policies on a set of objects. The user then adds or deletes objects to this set and reviews the results of ADO policy evaluation again. The user repeats this step to determine the set of objects for ADO execution. The user can then schedule ADO actions for immediate execution on this set of objects.
The following procedures support the two usage modes. Before describing the procedures, we introduce the notion of an ADO task as an entity that helps to track a particular evaluation or (an evaluation and execution) of ADO policies. A particular ADO task could be in one of the following states.
- Inactive
- Active
- Completed
### DBMS_ILM Security Model
The `DBMS_ILM` package runs under invoker's rights.
### DBMS_ILM Constants
The table in this topic lists the constants used by the `DBMS_ILM` package.
Table 94-1 DBMS_ILM Constants

| Constant | Value | Type | Description |
|---|---|---|---|
| ILM_ALL_POLICIES | 'ALL POLICIES' | VARCHAR2(20) | Selects all ADO policies on an object |
| ILM_EXECUTION_OFFLINE | 1 | NUMBER | Specifies that the object may be offline while ADO action is performed |
| ILM_EXECUTION_ONLINE | 2 | NUMBER | Specifies that the object should be online while ADO action is performed |
| SCOPE_DATABASE | 1 | NUMBER | Selects all ADO policies in the database |
| SCOPE_SCHEMA | 2 | NUMBER | Selects all ADO policies in the current schema |
| SCHEDULE_IMMEDIATE | 1 | NUMBER | Schedules ADO task for immediate execution |
| ARCHIVE_STATE_ACTIVE | '0' | VARCHAR2(1) | Represents the value of the ORA_ARCHIVE_STATE column of a row-archival enabled table that would make the row active |
| ARCHIVE_STATE_ARCHIVED | '1' | VARCHAR2(1) | Represents the value of the ORA_ARCHIVE_STATE column of a row-archival enabled table that would make the row inactive |

### DBMS_ILM Exceptions
The table in this topic lists the exceptions raised by the `DBMS_ILM` package.
Table 94-2 DBMS_ILM Exceptions

| Exception | Error Code | Description |
|---|---|---|
| INVALID_ARGUMENT_VALUE | 38327 | Invalid argument value |
| INVALID_ILM_DICTIONARY | 38328 | Inconsistent dictionary state |
| INTERNAL_ILM_ERROR | 38329 | Internal error |
| INSUFFICIENT_PRIVILEGES | 38330 | Insufficient privileges |

### Summary of DBMS_ILM Subprograms
Thi table lists and describes the `DBMS_ILM` package subprograms.
Table 94-3 DBMS_ILM Package Subprograms

| Subprogram | Description |
|---|---|
| ADD_TO_ILM Procedure | Adds the object specified through the argument to a particular ADO task and evaluates the ADO policies on this object |
| ARCHIVESTATENAME Function | Returns the value of the ORA_ARCHIVE_STATE column of a row-archival enabled table |
| EXECUTE_ILM Procedure | Executes an ADO task. |
| EXECUTE_ILM_TASK Procedure | Executes an ADO task that has been evaluated previously |
| PREVIEW_ILM Procedure | Evaluates all ADO policies in the scope specified by means of an argument |
| REMOVE_FROM_ILM Procedure | Removes the object specified through the argument from a particular ADO task |
| STOP_ILM Procedure | Stops ADO-related jobs created for a particular ADO task |

#### ADD_TO_ILM Procedure
This procedure adds the object specified through the argument to a particular ADO task and evaluates the ADO policies on this object.
The procedure can only be executed on an ADO task in an inactive state. The results of the ADO policy evaluation on this object can be viewed using the appropriate views depending on role and access (`USER_ILMTASKS` or `DBA_ILMTASKS`, `USER_ILMEVALUATIONDETAILS` or `DBA_ILMEVALUATIONDETAILS`, `USER_ILMRESULTS` or `DBA_ILMRESULTS`).
Syntax
```
DBMS_ILM.ADD_TO_ILM (
   task_id           IN    NUMBER,
   owner             IN    VARCHAR2,
   object_name       IN    VARCHAR2,
   subobject_name    IN    VARCHAR2 DEFAULT NULL);
```
Parameters
Table 94-4 ADD_TO_ILM Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Identifies a particular ADO task |
| owner | Owner of the object |
| object_name | Name of the object |
| subobject_name | Name of the subobject (partition name in the case of partitioned tables) |

#### ARCHIVESTATENAME Function
This function returns the value of the `ORA_ARCHIVE_STATE` column of a row-archival enabled table.
Syntax
```
DBMS_ILM.ARCHIVESTATENAME (
   value      IN  VARCHAR2)
 RETURN VARCHAR2;
```
Parameters
Table 94-5 ARCHIVESTATENAME Function Parameters

| Parameter | Description |
|---|---|
| value | Value for which the archive state name is to be returned |

Usage Notes
Returns `ARCHIVE_STATE_ACTIVE` for `0`, `ARCHIVE_STATE_ARCHIVED` for others
See Also:
"Using In-Database Archiving" in Oracle Database VLDB and Partitioning Guide
#### EXECUTE_ILM Procedure
This procedure executes an ADO task.
There are two overloads to this procedure. The first overload executes an ADO task for a set of objects without having evaluated them previously. The second overload executes ADO policies for a specific object.
Syntax
```
DBMS_ILM.EXECUTE_ILM (
   task_id             OUT    NUMBER,
   ilm_scope           IN     NUMBER DEFAULT SCOPE_SCHEMA,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);
DBMS_ILM.EXECUTE_ILM (
   owner               IN     VARCHAR2,
   object_name         IN     VARCHAR2,
   task_id             OUT    NUMBER,
   subobject_name      IN     VARCHAR2 DEFAULT NULL,
   policy_name         IN     VARCHAR2 DEFAULT ILM_ALL_POLICIES,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);
```
Parameters
Table 94-6 EXECUTE_ILM Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Identifies a particular ADO task |
| ilm_scope | Determines the set of objects considered for ADO execution. The default is to consider only the objects in the schema. |
| execution_mode | Whether the ADO task be executed online (ILM_EXECUTION_ONLINE) or offline (ILM_EXECUTION_OFFLINE) |
| owner | Owner of the object |
| object_name | Name of the object |
| subobject_name | Name of the subobject (partition name in the case of partitioned tables) |
| policy_name | Name of the ADO policy to be evaluated on the object. The package constant ILM_ALL_POLICIES should be used if all ADO policies on an object should be evaluated. |

Usage Notes
- The EXECUTE_ILM procedure can be used by users who want more control of when ADO is performed, and who do not want to wait until the next maintenance window.
- The procedure executes like a DDL in that it auto commits before and after the ADO task and related jobs are created.
#### EXECUTE_ILM_TASK Procedure
This procedure executes an ADO task that has been evaluated previously and moves it to an active state.
Syntax
```
DBMS_ILM.EXECUTE_ILM_TASK (
   task_id             IN     NUMBER,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);
   execution_schedule  IN     NUMBER DEFAULT SCHEDULE_IMMEDIATE);
```
Parameters
Table 94-7 EXECUTE_ILM_TASK Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Identifies a particular ADO task |
| execution_mode | Whether the ADO task be executed online (ILM_EXECUTION_ONLINE) or offline (ILM_EXECUTION_OFFLINE) |
| execution_schedule | Identifies when the ADO task should be executed.Currently, the only choice available is immediate scheduling of ADO jobs |

#### PREVIEW_ILM Procedure
This procedure evaluates the ADO policies on the objects specified using the `ILM_SCOPE` argument.
It returns a number as `task_id` which identifies a particular ADO task. This can be used to view the results of the policy evaluation in the appropriate views depending on role and access (`USER_ILMTASKS` or `DBA_ILMTASKS`, `USER_ILMEVALUATIONDETAILS` or `DBA_ILMEVALUATIONDETAILS`, `USER_ILMRESULTS` or `DBA_ILMRESULTS`).
The `PREVIEW_ILM` procedure leaves the ADO task in an inactive state. Once you have previewed the results, you can add or delete objects to this task.
Syntax
```
DBMS_ILM.PREVIEW_ILM (
   task_id           OUT    NUMBER,
  ilm_scope          IN     NUMBER DEFAULT SCOPE_SCHEMA);
```
Parameters
Table 94-8 PREVIEW_ILM Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Identifies a particular ADO task |
| ilm_scope | Identifies the scope of execution. Should be either SCOPE_DATABASE or SCOPE_SCHEMA as described in Constants |

#### REMOVE_FROM_ILM Procedure
This procedure removes the object specified through the argument from a particular ADO task.
The procedure can only be executed on an ADO task in an inactive state.
Syntax
```
DBMS_ILM.REMOVE_FROM_ILM (
   task_id           IN    NUMBER,
   owner             IN    VARCHAR2,
   object_name       IN    VARCHAR2,
   subobject_name    IN    VARCHAR2 DEFAULT NULL);
```
Parameters
Table 94-9 REMOVE_FROM_ILM Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Identifies a particular ADO task |
| owner | Owner of the object |
| object_name | Name of the object |
| subobject_name | Name of the subobject (partition name in the case of partitioned tables) |

#### STOP_ILM Procedure
This procedure terminates ILM ADO jobs associated to a particular task Id or job name.
Syntax
```
DBMS_ILM.STOP_ILM (
   task_id               IN         NUMBER,
   p_drop_running_jobs   IN         BOOLEAN  DEFAULT FALSE),
   p_jobname             IN         VARCHAR2 DEFAULT NULL);
```
Parameters
Table 94-10 STOP_ILM Procedure Parameters

| Parameter | Description |
|---|---|
| task_id | Number that uniquely identifies a particular ADO task |
| p_drop_running_jobs | Determines whether running jobs are dropped |
| p_jobname | Name of job to be terminated |

---

## DBMS_COMPRESSION

## DBMS_COMPRESSION
The `DBMS_COMPRESSION` package provides an interface to facilitate choosing the correct compression level for an application.
This chapter contains the following topics:
- Overview
- Security Model
- Constants
- Data Structures
- Summary of DBMS_COMPRESSION Subprograms
See Also:
- Oracle Database Administrator’s Guide
- Oracle Database Concepts
- Oracle Database SQL Language Reference
- Oracle Database Data Warehousing Guide
- Oracle Database VLDB and Partitioning Guide
- Oracle Database Reference
### DBMS_COMPRESSION Overview
The `DBMS_COMPRESSION` package gathers compression-related information within a database environment. This includes tools for estimating compressibility of a table for both partitioned and non-partitioned tables, and gathering row-level compression information on previously compressed tables. This gives the user with adequate information to make compression-related decision.
### DBMS_COMPRESSION Security Model
The `DBMS_COMPRESSSION` package is defined with `AUTHID CURRENT USER`, so it executes with the privileges of the current user.
### DBMS_COMPRESSION Constants
The `DBMS_COMPRESSION` package uses constants that can be used for specifying parameter values.
These constants are shown in the following table:
Table 44-1 DBMS_COMPRESSION Constants - Compression Types

| Constant | Type | Value | Description |
|---|---|---|---|
| COMP_NOCOMPRESS | NUMBER | 1 | No compression |
| COMP_ADVANCED | NUMBER | 2 | Advanced row compression |
| COMP_QUERY_HIGH | NUMBER | 4 | High for query warehouse compression (Hybrid Columnar Compression) |
| COMP_QUERY_LOW | NUMBER | 8 | Low for query warehouse compression (Hybrid Columnar Compression) |
| COMP_ARCHIVE_HIGH | NUMBER | 16 | High archive compression (Hybrid Columnar Compression) |
| COMP_ARCHIVE_LOW | NUMBER | 32 | Low archive compression (Hybrid Columnar Compression) |
| COMP_BLOCK | NUMBER | 64 | Compressed block |
| COMP_LOB_HIGH | NUMBER | 128 | High compression level for LOB operations |
| COMP_LOB_MEDIUM | NUMBER | 256 | Medium compression level for LOB operations |
| COMP_LOB_LOW | NUMBER | 512 | Low compression level for LOB operations |
| COMP_INDEX_ADVANCED_HIGH | NUMBER | 1024 | High compression level for indexes |
| COMP_INDEX_ADVANCED_LOW | NUMBER | 2048 | Low compression level for indexes |
| COMP_RATIO_LOB_MINROWS | NUMBER | 1000 | Minimum required number of LOBs in the object for which LOB compression ratio is to be estimated |
| COMP_BASIC | NUMBER | 4096 | Basic table compression |
| COMP_RATIO_LOB_MAXROWS | NUMBER | 5000 | Maximum number of LOBs used to compute the LOB compression ratio |
| COMP_INMEMORY_NOCOMPRESS | NUMBER | 8192 | In-Memory with no compression |
| COMP_INMEMORY_DML | NUMBER | 16384 | In-Memory compression level for DML |
| COMP_INMEMORY_QUERY_LOW | NUMBER | 32768 | In-Memory compression level optimized for query performance |
| COMP_INMEMORY_QUERY_HIGH | NUMBER | 65536 | In-Memory compression level optimized on query performance as well as space saving |
| COMP_INMEMORY_CAPACITY_LOW | NUMBER | 131072 | In-Memory low compression level optimizing for capacity |
| COMP_INMEMORY_CAPACITY_HIGH | NUMBER | 262144 | In-Memory high compression level optimizing for capacity |
| COMP_RATIO_MINROWS | NUMBER | 1000000 | Minimum required number of rows in the object for which HCC ratio is to be estimated |
| COMP_RATIO_ALLROWS | NUMBER | -1 | To indicate the use of all the rows in the object to estimate HCC ratio |
| OBJTYPE_TABLE | PLS_INTEGER | 1 | Identifies the object whose compression ratio is estimated as of type table |
| OBJTYPE_INDEX | PLS_INTEGER | 2 | Identifies the object whose compression ratio is estimated as of type index |

Note:
Hybrid columnar compression is a feature of certain Oracle storage systems. See Oracle Database Concepts for more information.
### DBMS_COMPRESSION Data Structures
The `DBMS_COMPRESSION` package defines a `RECORD` type and a `TABLE` type.
RECORD TYPES
COMPREC Record Type
TABLE TYPES
COMPRECLIST Table Type
#### COMPREC Record Type
The COMPREC record type is a record for calculating an individual index compression ratio on a table.
Syntax
```
TYPE COMPREC IS RECORD(
  ownname           varchar2(255),
  objname           varchar2(255),
  blkcnt_cmp        PLS_INTEGER,
  blkcnt_uncmp      PLS_INTEGER,
  row_cmp           PLS_INTEGER,
  row_uncmp         PLS_INTEGER,
  cmp_ratio         NUMBER,
  objtype           PLS_INTEGER);
```
Fields
Table 44-2 COMPREC Attributes

| Field | Description |
|---|---|
| ownname | Schema of the object owner |
| objname | Name of the object |
| blkcnt_cmp | Number of blocks used by the compressed sample of the object |
| blkcnt_uncmp | Number of blocks used by the uncompressed sample of the object |
| row_cmp | Number of rows in a block in compressed sample of the object |
| row_uncmp | Number of rows in a block in uncompressed sample of the object |
| cmp_ratio | Compression ratio, blkcnt_uncmp divided by blkcnt_cmp |
| objtype | Type of the object |

#### COMPRECLIST Table Type
COMPRECLIST is a table type of the COMPREC Record Type.
Syntax
```
TYPE compreclist IS TABLE OF comprec;
```
**Related Topics**
                           - COMPREC Record Type
### Summary of DBMS_COMPRESSION Subprograms
The `DBMS_COMPRESSION` package uses the `GET_COMPRESSION_RATIO` Procedure and `GET_COMPRESSION_TYPE` Function subprograms.
Table 44-3 DBMS_COMPRESSION Package Subprograms

| Subprogram | Description |
|---|---|
| GET_COMPRESSION_RATIO Procedure | Analyzes the compression ratio of a table, and gives information about compressibility of a table |
| GET_COMPRESSION_TYPE Function | Returns the compression type for a specified row |

#### GET_COMPRESSION_RATIO Procedure
This procedure analyzes the compression ratio of a table or an index, and gives information about compressibility of the object. Various parameters can be provided by the user to selectively analyze different compression types.
Syntax
Get compression ratio for an object (table or index, default is table):
```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2,
   ownname               IN     VARCHAR2,
   objname               IN     VARCHAR2,
   subobjname            IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   row_cmp               OUT    PLS_INTEGER,
   row_uncmp             OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,
   subset_numrows        IN     NUMBER  DEFAULT COMP_RATIO_MINROWS,
   objtype               IN     PLS_INTEGER DEFAULT OBJTYPE_TABLE);
```
Get compression ratio for LOBs:
```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2,
   tabowner              IN     VARCHAR2,
   tabname               IN     VARCHAR2,
   lobname               IN     VARCHAR2,
   partname              IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   lobcnt                OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,
   subset_numrows        IN     number DEFAULT COMP_RATIO_LOB_MAXROWS);
```
Get compression ratio for all indexes on a table. The compression ratios are returned as a collection.
```
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
  scratchtbsname        IN     VARCHAR2,
  ownname               IN     VARCHAR2,
  tabname               IN     VARCHAR2,
  comptype              IN     NUMBER,
  index_cr              OUT    DBMS_COMPRESSION.COMPRECLIST,
  comptype_str          OUT    VARCHAR2,
  subset_numrows        IN     NUMBER DEFAULT COMP_RATIO_INDEX_MINROWS);
```
Parameters
Table 44-4 GET_COMPRESSION_RATIO Procedure Parameters

| Parameter | Description |
|---|---|
| scratchtbsname | Temporary scratch tablespace that can be used for analysis |
| ownname / tabowner | Schema of the table to analyze |
| tabname | Name of the table to analyze |
| objname | Name of the object |
| subobjname | Name of the partition or sub-partition of the object |
| comptype | Compression types for which analysis should be performed When the object is an index, only the following compression types are valid: COMP_INDEX_ADVANCED_HIGH (value 1024) and COMP_INDEX_ADVANCED_LOW (value 2048). Note: The following compression types cannot be specified in this parameter for any type of object: COMP_BLOCK (value 64) and COMP_BASIC (value 4096). |
| blkcnt_cmp | Number of blocks used by compressed sample of the table |
| blkcnt_uncmp | Number of blocks used by uncompressed sample of the table |
| row_cmp | Number of rows in a block in compressed sample of the table |
| row_uncmp | Number of rows in a block in uncompressed sample of the table |
| cmp_ratio | Compression ratio, blkcnt_uncmp divided by blkcnt_cmp |
| comptype_str | String describing the compression type |
| subset_numrows | Number of rows sampled to estimate compression ratio. |
| objtype | Type of the object, either OBJTYPE_TABLE or OBJTYPE_INDEX |
| lobname | Name of the LOB column |
| partname | In case of partitioned tables, the related partition name |
| lobcnt | Number of lobs actually sampled to estimate compression ratio |
| index_cr | List of indexes and their estimated compression ratios |

Examples
The following example shows how to estimate the compression ratio for advanced row compression:
```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp   PLS_INTEGER;
  1_blkcnt_uncmp PLS_INTEGER;
  1_row_cmp      PLS_INTEGER;
  1_row_uncmp    PLS_INTEGER;
  1_cmp_ratio    NUMBER;
  1_comptype_str VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname => 'USERS' ,
   ownname	  => 'TEST' ,
   objname	  => 'SALES' ,
   subobjname     =>  NULL ,
   comptype       =>  DBMS_COMPRESSION.COMP_ADVANCED,
   blkcnt_cmp     => 1_blkcnt_cmp,
   blkcnt_uncmp   => 1_blkcnt_uncmp,
   row_cmp	  => 1_row_cmp,
   row_uncmp      => 1_row_uncmp,
   cmp_ratio      => 1_cmp_ratio,
   comptype_str   => 1_comptype_str,
   subset_numrows => DBMS_COMPRESSION.comp_ratio_minrows,
   objtype	  => DBMS_COMPRESSION.objtype_table
  );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object	:  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object	:  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object	:  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object	:  ' || 1_row_uncmp);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                       	:  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type							:  ' || 1_comptype_str);
END;
/
```
Output of compression advisor estimate for advanced row compression (entire table):
```
Number of blocks used by the compressed sample of the object     : 165
Number of blocks used by the uncompressed sample of the object   : 629
Number of rows in a block in compressed sample of the object     : 599
Number of rows in a block in uncompressed sample of the object   : 157
Estimated Compression Ratio of Sample			         : 3.8
Compression Type						 : “Compress Advanced”
```
The following example shows how to estimate the compression ratio for advanced index compression (Low):
```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp	   PLS_INTEGER;
  1_blkcnt_uncmp   PLS_INTEGER
  1_row_cmp	   PLS_INTEGER;
  1_row_uncmp	   PLS_INTEGER;
  1_cmp_ratio	   NUMBER;
  1_comptype_str   VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
    scratchtbsname =>       'USERS' ,
    ownname	   =>       'TEST' ,
    objname	   =>       'SALES_IDX' ,
    subobjname     =>        NULL ,
    comptype       =>        DBMS_COMPRESSION.COMP_INDEX_ADVANCED_LOW,
    blkcnt_cmp     =>        1_blkcnt_cmp,
    blkcnt_uncmp   =>        1_blkcnt_uncmp,
    row_cmp	   =>        1_row_cmp,
    row_uncmp      =>        1_row_uncmp,
    cmp_ratio      =>        1_cmp_ratio,
    comptype_str   =>        1_comptype_str,
    subset_numrows =>        DBMS_COMPRESSION.comp_ratio_minrows,
    objtype	   =>        DBMS_COMPRESSION.objtype_index
   );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object   :  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object :  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object   :  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object :  ' || 1_row_uncmp);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                          :  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type						      :  ' || 1_comptype_str);
END;
/
```
Output of compression advisor estimate for advanced index compression (Low):
```
Number of blocks used by the compressed sample of the object     : 243
Number of blocks used by the uncompressed sample of the object   : 539
Number of rows in a block in compressed sample of the object     : 499
Number of rows in a block in uncompressed sample of the object   : 145
Estimated Compression Ratio of Sample				 : 2.2
Compression Type						 : “Compress Advanced Low”
```
The following example shows how to estimate the compression ratio for advanced LOB compression (Medium):
```
SET SERVEROUTPUT ON
DECLARE
  1_blkcnt_cmp     PLS_INTEGER;
  1_blkcnt_uncmp   PLS_INTEGER;
  1_row_cmp	   PLS_INTEGER;
  1_lobcnt	   PLS_INTEGER;
  1_cmp_ratio      NUMBER;
  1_comptype_str   VARCHAR2(32767);
BEGIN
   DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
    scratchtbsname => 'USERS' ,
    tabowner       => 'TEST' ,
    tabname	   => 'PARTS' ,
    lobname	   =>  'PART_DESCRIPTION' ,
    partname       =>  NULL ,
    comptype       =>  DBMS_COMPRESSION.COMP_LOB_MEDIUM,
    blkcnt_cmp     => 1_blkcnt_cmp,
    blkcnt_uncmp   => 1_blkcnt_uncmp,
    row_cmp	   => 1_row_cmp,
    lobcnt	   => 1_lobcnt,
    cmp_ratio      => 1_cmp_ratio,
    comptype_str   => 1_comptype_str,
    subset_numrows => DBMS_COMPRESSION.comp_ratio_lob_maxrows
   );
DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object    :  ' || 1_blkcnt_cmp);
DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object  :  ' || 1_blkcnt_uncmp);
DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object    :  ' || 1_row_cmp);
DBMS_OUTPUT.put_line( 'Number of LOBS actually sampled				       :  ' || 1_lobcnt);
DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample                           :  ' || 1_cmp_ratio);
DBMS_OUTPUT.put_line( 'Compression Type                                                :  ' || 1_comptype_str);
END;
/
```
Output of compression advisor estimate for advanced LOB compression (Medium):
```
Number of blocks used by the compressed sample of the object   : 199
Number of blocks used by the uncompressed sample of the object : 389
Number of rows in a block in compressed sample of the object   : 293
Number of LOBS actually sampled 			       : 55
Estimated Compression Ratio of Sample			       : 1.9
Compression Type					       : “Compress Medium”
```
Usage Notes
The procedure creates different tables in the scratch tablespace and runs analysis on these objects. It does not modify anything in the user-specified tables.
#### GET_COMPRESSION_TYPE Function
This function returns the compression type for a specified row. If the row is chained, the function returns the compression type of the head piece only, and does not examine the intermediate or the tail piece since head pieces can be differently compressed.
Syntax
```
DBMS_COMPRESSION.GET_COMPRESSION_TYPE (
   ownname      IN    VARCHAR2,
   tabname      IN    VARCHAR2,
   row_id       IN    ROWID,
   subobjname   IN    VARCHAR2 DEFAULT NULL))
  RETURN NUMBER;
```
Parameters
Table 44-5 GET_COMPRESSION_TYPE Function Parameters

| Parameter | Description |
|---|---|
| ownname | Schema name of the table |
| tabname | Name of table |
| rowid | Rowid of the row |
| subobjname | Name of the table partition or subpartition |

Return Values
Flag to indicate the compression type (see Table 44-1).

---

## DBMS_HEAT_MAP

## DBMS_HEAT_MAP
The `DBMS_HEAT_MAP` package provides an interface to externalize heatmaps at various levels of storage including block, extent, segment, object and tablespace. A second set of subprograms externalize the heatmaps materialized by the background for top N tablespaces.
This chapter contains the following topics:
- Overview
- Security Model
- Summary of DBMS_HEAT_MAP Subprograms
See Also:
- Heat Map in Oracle Database VLDB and Partitioning Guide
- DBMS_ILM
- DBMS_ILM_ADMIN
### DBMS_HEAT_MAP Overview
To implement your ILM strategy, you can use Heat Map in Oracle Database to track data access and modification. You can also use Automatic Data Optimization (ADO) to automate the compression and movement of data between different tiers of storage within the database.
The Heat Map tracks modification times at the block level, and multiple access statistics at the segment level. Objects in the `SYSTEM` and `SYSAUX` tablespaces are not tracked. `DBMS_HEAT_MAP` gives you access to the Heat Map statistics at various levels - block, extent, segment, object, and tablespace.
### DBMS_HEAT_MAP Security Model
The execution privilege is granted to `PUBLIC`. Procedures in this package run under the caller security. The user must have `ANALYZE` privilege on the object.
### Summary of DBMS_HEAT_MAP Subprograms
This table lists and briefly describes the `DBMS_HEAT_MAP` package subprograms.
Table 88-1 DBMS_HEAT_MAP Package Subprograms

| Subprogram | Description |
|---|---|
| BLOCK_HEAT_MAP Function | Returns last modification time for each block in a table segment |
| EXTENT_HEAT_MAP Function | Returns the extent level Heat Map statistics for a table segment |
| OBJECT_HEAT_MAP Function | Returns the minimum, maximum and average access times for all the segments belonging to the object |
| SEGMENT_HEAT_MAP Procedure | Returns the heatmap attributes for the given segment |
| TABLESPACE_HEAT_MAP Function | Returns the minimum, maximum and average access times for all the segments in the tablespace |

#### BLOCK_HEAT_MAP Function
This table function returns the last modification time for each block in a table segment. It returns no information for segment types that are not data.
Syntax
```
DBMS_HEAT_MAP.BLOCK_HEAT_MAP (
   owner             IN VARCHAR2,
   segment_name      IN VARCHAR2,
   partition_name    IN VARCHAR2 DEFAULT NULL,
   sort_columnid     IN NUMBER DEFAULT NULL,
   sort_order        IN VARCHAR2 DEFAULT NULL)
RETURN hm_bls_row PIPELINED;
```
Parameters
Table 88-2 BLOCK_HEAT_MAP Function Parameters

| Parameter | Description |
|---|---|
| owner | Owner of the segment |
| segment_name | Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. |
| partition_name | Defaults to NULL. For a partitioned table, specify the partition or subpartition segment name. |
| sort_columnid | ID of the column on which to sort the output. Valid values 1..9. Invalid values are ignored. |
| sort_order | Defaults to NULL. Possible values: ASC, DESC |

Return Values
Table 88-3 BLOCK_HEAT_MAP Function Return Values (Output Parameters)

| Parameter | Description |
|---|---|
| owner | Owner of the segment |
| segment_name | Segment name of the non-partitioned table |
| partition_name | Partition or subpartition name |
| tablespace_name | Tablespace containing the segment |
| file_id | Absolute file number of the block in the segment |
| relative_fno | Relative file number of the block in the segment |
| block_id | Block number of the block |
| write time | Last modification time of the block |

#### EXTENT_HEAT_MAP Function
This table function returns the extent level Heat Map statistics for a table segment. It returns no information for segment types that are not data. Aggregates at extent level, including minimum modification time and maximum modification time, are   included.
Syntax
```
DBMS_HEAT_MAP.EXTENT_HEAT_MAP (
   owner             IN VARCHAR2,
   segment_name      IN VARCHAR2,
   partition_name    IN VARCHAR2 DEFAULT NULL,
RETURN hm_els_row PIPELINED;
```
Parameters
Table 88-4 EXTENT_HEAT_MAP Function Parameters

| Parameter | Description |
|---|---|
| owner | Owner of the segment |
| segment_name | Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. |
| partition_name | Defaults to NULL. For a partitioned table, specify the partition or subpartition segment name. |

Return Values
Table 88-5 EXTENT_HEAT_MAP Function Return Values (Output Parameters)

| Parameter | Description |
|---|---|
| owner | Owner of the segment |
| segment_name | Segment name of the non-partitioned table |
| partition_name | Partition or subpartition name |
| tablespace_name | Tablespace containing the segment |
| file_id | Absolute file number of the block in the segment |
| relative_fno | Relative file number of the block in the segment |
| block_id | Block number of the block |
| blocks | Number of blocks in the extent |
| bytes | Number of bytes in the extent |
| min_writetime | Minimum of last modification time of the block |
| max_writetime | Maximum of last modification time of the block |
| avg_writetime | Average of last modification time of the block |

#### OBJECT_HEAT_MAP Function
This table function returns the minimum, maximum and average access times for all the segments belonging to the object.
The object must be a table. The table function raises an error if called on object tables other than table.
Syntax
```
DBMS_HEAT_MAP.OBJECT_HEAT_MAP (
   object_owner      IN VARCHAR2,
   object_name       IN VARCHAR2)
 RETURN hm_object_table PIPELINED;
```
Parameters
Table 88-6 OBJECT_HEAT_MAP Function Parameters

| Parameter | Description |
|---|---|
| object_owner | Tablespace containing the segment |
| object_name | Segment header relative file number |

Return Values
Table 88-7 OBJECT_HEAT_MAP Function Return Values (Output Parameters)

| Parameter | Description |
|---|---|
| segment_name | Name of the top level segment |
| partition_name | Name of the partition |
| tablespace_name | Name of the tablespace |
| segment_type | Type of segment as in DBA_SEGMENTS.SEGMENT_TYPE |
| segment_size | Segment size in bytes |
| min_writetime | Oldest write time for the segment |
| max_writetime | Latest write time for the segment |
| avg_writetime | Average write time for the segment |
| min_readtime | Oldest read time for the segment |
| max_readtime | Latest read time for the segment |
| avg_writetime | Average write time for the segment |
| min_lookuptime | Oldest index lookup time for the segment |
| max_lookuptime | Latest index lookup time for the segment |
| avg_lookuptime | Average index lookup time for the segment |
| min_ftstime | Oldest full table scan time for the segment |
| max_ftstime | Latest full table scan time for the segment |
| avg_ftstime | Average full table scan time for the segment |

#### SEGMENT_HEAT_MAP Procedure
This procedure returns the heatmap attributes for the given segment.
Syntax
```
DBMS_HEAT_MAP.SEGMENT_HEAT_MAP (
   tablespace_id          IN  NUMBER,
   header_file            IN  NUMBER,
   header_block           IN  NUMBER,
   segment_objd           IN  NUMBER,
   min_writetime          OUT DATE,
   max_writetime          OUT DATE,
   avg_writetime          OUT DATE,
   min_readtime           OUT DATE,
   max_readtime           OUT DATE,
   avg_readtime           OUT DATE,
   min_lookuptime         OUT DATE,
   max_lookuptime         OUT DATE,
   avg_lookuptime         OUT DATE,
   min_ftstime            OUT DATE,
   max_ftstime            OUT DATE,
   avg_ftstime            OUT DATE);
```
Parameters
Table 88-8 SEGMENT_HEAT_MAP Procedure Parameters

| Parameter | Description |
|---|---|
| tablespace_id | Tablespace containing the segment |
| header_file | Segment header relative file number |
| header_block | Segment header block number |
| segment_objd | DATAOBJ of the segment |

Return Values
Table 88-9 SEGMENT_HEAT_MAP Procedure Return Values (Output Parameters)

| Parameter | Description |
|---|---|
| min_writetime | Oldest write time for the segment |
| max_writetime | Latest write time for the segment |
| avg_writetime | Average write time for the segment |
| min_readtime | Oldest read time for the segment |
| max_readtime | Latest read time for the segment |
| avg_writetime | Average write time for the segment |
| min_lookuptime | Oldest index lookup time for the segment |
| max_lookuptime | Latest index lookup time for the segment |
| avg_lookuptime | Average index lookup time for the segment |
| min_ftstime | Oldest full table scan time for the segment |
| max_ftstime | Latest full table scan time for the segment |
| avg_ftstime | Average full table scan time for the segment |

#### TABLESPACE_HEAT_MAP Function
This table function returns the minimum, maximum and average access times for all the segments in the tablespace.
Syntax
```
DBMS_HEAT_MAP.TABLESPACE_HEAT_MAP (
    tablespace_name      IN VARCHAR2)
  RETURN hm_tablespace_table PIPELINED;
```
Parameters
Table 88-10 TABLESPACE_HEAT_MAP Procedure Parameters

| Parameter | Description |
|---|---|
| tablespace_name | Name of the tablespace |

Return Values
Table 88-11 TABLESPACE_HEAT_MAP Procedure Return Values (Output Parameters)

| Parameter | Description |
|---|---|
| segment_count | Total number of segments in the tablespace |
| allocated_bytes | Space used by the segments in the tablespace |
| min_writetime | Oldest write time for the segment |
| max_writetime | Latest write time for the segment |
| avg_writetime | Average write time for the segment |
| min_readtime | Oldest read time for the segment |
| max_readtime | Latest read time for the segment |
| avg_writetime | Average write time for the segment |
| min_lookuptime | Oldest index lookup time for the segment |
| max_lookuptime | Latest index lookup time for the segment |
| avg_lookuptime | Average index lookup time for the segment |
| min_ftstime | Oldest full table scan time for the segment |
| max_ftstime | Latest full table scan time for the segment |
| avg_ftstime | Average full table scan time for the segment |
