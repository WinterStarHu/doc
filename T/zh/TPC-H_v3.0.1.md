# TPC-H_v3.0.1（机器翻译草稿）

> ⚠️ 术语词典粗译，SQL/代码/大写标识符保留原文，可能生硬。仅供速览。

# TPC-H_v3.0.1

> 源文件: `T/../TPC-H_v3.0.1.pdf`，138 页。

                               TPC BENCHMARKTM H
                                         (Decision Support)
                                       Standard Specification
                                           Revision 3.0.1




                         Transaction Processing Performance Council (TPC)
                                      Presidio of San Francisco
                                 Building 572B Ruger St. (surface)
                                       P.O. Box 29920 (mail)
                                   San Francisco, CA 94129-0920
                                        Voice:415-561-6272
                                         Fax:415-561-6120
                                     Email: webmaster@tpc.org

                     © 1993 - 2022 Transaction Processing Performance Council




TPC BenchmarkTM H Standard Specification Revision 3.0.1                         Page 1
                                      Acknowledgments
The TPC acknowledges the work and contributions of the TPC-D subcommittee member companies in developing
Version 2 of the TPC-D 规范 which formed the basis for TPC-H Version 1. The subcommittee included
representatives from Compaq, Data General, Dell, EMC, HP, IBM, Informix, Microsoft, NCR, Oracle, Sequent,
SGI, Sun, Sybase, and Unisys. The TPC also acknowledges the contribution of Jack Stephens, consultant to the
TPC-D subcommittee, for his work on the 基准测试 规范 and DBGEN development.


                                       TPC Membership
                      A list of the current TPC member companies can be found at
               http://www.tpc.org/tpc_documents_current_versions/pdf/tpcmembers.pdf




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                              Page 2
                                            Document History


       Date              Version                                      Description

 26 February 1999    Draft 1.0.0        Mail ballot draft for Standard Specification

 24 June 1999        Revision 1.1.0     First minor revision of the Specification

 25 April 2002       Revision 1.4.0     Clarification about Primary Keys

 12 July 2002        Revision 1.5.0     Additions for EOL of 硬件 in 8.6

 15 July 2002        Revision 2.0.0     Mail ballot draft 3 year 维护 定价

 14 August 2003      Revision 2.1.0     Adding scale factors 30TB and 100TB

 29 June 2005        Revision 2.2.0     Adding Pricing Specification 1.0.0

 11 August 2005      Revision 2.3.0     Changing 定价 precision to cents and processor 定义

 23 June 2006        Revision 2.4.0     Adding reference data set and 审计 要求 to verify populated
                                        数据库, effect of update data and qgen substitution parameters.
                                        Scale factors larger than 10,000 are required to use this version.

 10 July 2006        Revision 2.5.0     dbgen bug fixes in parallel data generation, updates to reference data
                                        set/qualification 输出, modified 审计 规则 and updated executive
                                        summary 示例.

 26 October 2006     Revision 2.6.0     Added Clause 7.2.3.1 about 软件 license 定价, removed Clause
                                        7.1.3.3 about 8 hour log 要求 and updated executive summary
                                        示例 in Appendix E

 14 June 2006        Revision 2.6.1     Editorial correction in Clause 2.1.3.3. Clarification of Clause 9.2.4.5

 28 February 2008    Revision 2.6.2     Change substr into substring in Clause 2.25.2, update of membership
                                        list, TPC address and copyright statement

 17 April 2008       Revision 2.7.0     Incorporate BUG fix 595 of qgen

 11 September        Revision 2.8.0     Add wording to allow substitutions in Clause 7.2. Modify clauses 5.4,
 2008                                   5.4.6, 8.4.2.2 and 9.2.6.1 to refer to 定价 规范. Update TPC
                                        member companies.

 17 September        Revision 2.9.0     Add Clause 8.3.5.10 to require wording for memory-to-规模因子
 2009                                   ratio in ES. Removed references to RAID and added data redundancy
                                        to Clauses 3.1.4, 4.3.2, 4.3.6, 8.3.5.4, and 8.4.2.4. Editorial
                                        corrections. Update TPC member companies.

 11 February 2010    Revision 2.10.0    Adapted necessary modifications required by Energy Specification.
                                        Modified Clause 8 to require electronic version of FDR. Added vendor
                                        specific INCLDUES into dbgen/qgen. Modified Clause 1.5.4 and
                                        2.13.3. Updated TPC member companies. Included editorial changes
                                        from FogBugz 217, 218, 219.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 3
 29 April 2010        Revision 2.11.0   Added 子句 9.2.3.3 to the auditor check list (power off SUT as 零件
                                        of 持久性 testing). Added comment after 子句 2.1.3.5 (precision).
                                        Modified 子句 3.5.4 points 2 and 3 to clarify ACID testing.
                                        Clarification of rounding with a new definitions 节 10:
                                        Clarification of partitioning by 日期 (子句 1.5.4). Require 查询
                                        输出 to be put into the supporting file archive (子句 8.3.5.3 ).

 25 June 2010         Revision 2.12.0   Fixed numerous bad cross references and editorial edits (fogbugz 243
                                        & 245). Clarify primary and foreign keys as constraints and add them
                                        to the global definitions 节. Fix bugs 252 by simplifying the
                                        说明 of string lengths generated by dbgen. Clarify references to
                                        the 刷新 stream for bug 254. Added 要求 to split electronic
                                        Supporting Files Archive into 3 separate zip files for ease of
                                        download.

 11 November 2010     Revision 2.13.0   Clarified the procedure to follow if problems with DBGen or QGen
                                        are found (Fogbugz 259). Reorganized the 查询 definitions to show
                                        only a sample 输出 行 and reorganized the 子句 numbering.
                                        Regenerated the answer set files for easier comparison and to correct
                                        errors (fogbugz 293). Added an auditor checklist item to validate the
                                        qualification results (fogbugz 302). Fixed a distribution issue in
                                        DBGen (软件 only) (fogbugz 301), which necessitated new
                                        references data and answer set files. Restored 列 L_TAX to the
                                        说明 for 表 Lineitem in Clause 1.4.1 (fogbugz 358). Fixed a
                                        bad 子句 reference in 子句 9.1.4 that was targeting 1.5.7 and 应
                                        be 1.5.6 (Fogbugz 360).

 11 February 2011     Revision 2.14.0   Editorial fix of 子句 references (Fogbugz 370). Update membership
                                        list and 表 of icons (Fogbugz 391). Augment Clause 2.1.3.5 about
                                        precision of 查询 输出 (Fogbugz 359). Editorial clarification in
                                        Clause 1.4.2 (Fogbugz 421). Replace/update Executive Summary
                                        examples in Appendix E (Fogbugz 253). Clarify/update 要求
                                        relating to data generation and loading phases in Clause 4.3 (Fogbugz
                                        419).

 7 April 2011         Revision 2.14.1   Increment point-version number to align with DBGEN release. No
                                        editorial change.

 16 June 2011         Revision 2.14.2   Align 定义 of 数据库 population (for S_NAME, P_MFGR,
                                        P_BRAND, C_NAME and O_CLERK) with DBGen (Fogbugz 463,
                                        464 and 465)

 18 November 2011     Revision 2.14.3   Correct 说明 of Q19 to match SQL. Revise sample Executive
                                        Summary.

 13 April 2012        Revision 2.14.4   Correction for FogBugz entry 536: change bullet 5 in Clause 4.2.3
                                        from L_RECEIPTDATE = O_ORDERDATE + random 值 [1 ..
                                        30] to L_RECEIPTDATE = L_SHIPDATE + random 值 [1 .. 30].
                                        FogBugz 279: Mandate disclosure of user documentation
 7 February 2013      Revision 2.15.0
                                        FogBugz 512: Define GUI and 要求 around disclosure in
                                        Clause 8.3
                                        FogBugz 604: Reference wrong in 2.5.3.1
                                        FogBugz 606: DBgen bug - removing separators
                                        FogBugz 613: Code fix for Q4 wrong substitution parameter
 20 June 2013         Revision 2.16.0
                                        generation.
                                        FogBugz 614: Code fix for Q22 wrong substitution parameter
                                        generation.



TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 4
                                                     Replaced incorrect answer set with verified correct answer set.
 24 April 2014                Revision 2.17.0
                                                     Allowed truncation of specific 查询 answers to reduce supporting file
                                                     size.
                                                     Corrected bad references in clauses 2.6.2 and 2.7.2, as noted in
 13 November 2014             Revision 2.17.1
                                                     FogBugz items 669 and 855.

 21 April 2017                Revision 2.17.2        Added EULA 2.1

 21 September 2017            Revision 2.17.3        Added wording to include license compute services (Fogbugz item
                                                     1905).
                                                     Clarify Clause 9.4.1.9 (Fogbugz item 2146).
 6 December 2018              Revision 2.18.0        Change Query reporting time to 1/100th of seconds and adjust all
                                                     related clauses (Fogbugz item 1505).
                                                     Change 价格 性能 指标 to Price-per-kQphH@Size
 10 February 2021             Revision 3.0.0
                                                     Affected clauses are: 0.1, 4.1.3.1, 5.4, 5.4.4.1, 5.4.4.2, 5.4.6, 8.4.2.1,
                                                     8.4.4.1 Appendix E
                                                     Clarify change log history for Revisions 2.17.3 and 2.18.0
 28 April 2022                Revision 3.0.1
                                                     Add comment to Clause 9.2.4.3
                                                     Add comment to Clause 2.4.19.5

TPC Benchmark™, TPC-H, QppH, QthH, and QphH are trademarks of the Transaction Processing Performance
Council.

All parties are granted permission to copy and distribute to any party without fee all or 零件 of this material provided
that: 1) copying and distribution is done for the primary purpose of disseminating TPC material; 2) the TPC
copyright notice, the title of the publication, and its 日期 appear, and notice is given that copying is by permission of
the Transaction Processing Performance Council.

Parties wishing to copy and distribute TPC materials other than for the purposes outlined above (including incorporating TPC material in a non-
TPC document, 规范 or report), must secure the TPC's written permission.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                                               Page 5
                                                                             Table of Contents
0: INTRODUCTION ................................................................................................................................................................. 8
   0.1          PREAMBLE................................................................................................................................................................... 8
   0.2          GENERAL IMPLEMENTATION GUIDELINES ................................................................................................................... 9
   0.3          GENERAL MEASUREMENT GUIDELINES ..................................................................................................................... 10
1: LOGICAL DATABASE DESIGN ..................................................................................................................................... 11
   1.1          BUSINESS AND APPLICATION ENVIRONMENT ............................................................................................................ 11
   1.2          DATABASE ENTITIES, RELATIONSHIPS, AND CHARACTERISTICS ............................................................................... 13
   1.3          DATATYPE DEFINITIONS............................................................................................................................................ 14
   1.4          TABLE LAYOUTS ....................................................................................................................................................... 14
   1.5          IMPLEMENTATION RULES .......................................................................................................................................... 19
   1.6          DATA ACCESS TRANSPARENCY REQUIREMENTS ....................................................................................................... 21
2: QUERIES AND REFRESH FUNCTIONS ....................................................................................................................... 22
   2.1          GENERAL REQUIREMENTS AND DEFINITIONS FOR QUERIES ...................................................................................... 22
   2.2          QUERY COMPLIANCE ................................................................................................................................................ 25
   2.3          QUERY VALIDATION ................................................................................................................................................. 28
   2.4          QUERY DEFINITIONS ................................................................................................................................................. 29
   2.5          GENERAL REQUIREMENTS FOR REFRESH FUNCTIONS ................................................................................................ 68
   2.6          NEW SALES REFRESH FUNCTION (RF1) .................................................................................................................... 68
   2.7          OLD SALES REFRESH FUNCTION (RF2) ..................................................................................................................... 69
   2.8          DATABASE EVOLUTION PROCESS .............................................................................................................................. 69
3: THE ACID PROPERTIES ................................................................................................................................................. 70
   3.2          ATOMICITY REQUIREMENTS ...................................................................................................................................... 72
   3.3          CONSISTENCY REQUIREMENTS .................................................................................................................................. 72
   3.4          ISOLATION REQUIREMENTS ....................................................................................................................................... 73
   3.5          DURABILITY REQUIREMENTS .................................................................................................................................... 76
4: SCALING AND DATABASE POPULATION ................................................................................................................. 79
   4.1          DATABASE DEFINITION AND SCALING ...................................................................................................................... 79
   4.2          DBGEN AND DATABASE POPULATION ..................................................................................................................... 80
   4.3          DATABASE LOAD TIME ............................................................................................................................................. 89
5: PERFORMANCE METRICS AND EXECUTION RULES ........................................................................................... 92
   5.1          DEFINITION OF TERMS............................................................................................................................................... 92
   5.2          CONFIGURATION RULES ............................................................................................................................................ 92
   5.3          EXECUTION RULES .................................................................................................................................................... 94
   5.4          METRICS ................................................................................................................................................................... 98
6: SUT AND DRIVER IMPLEMENTATION .................................................................................................................... 102
   6.1          MODELS OF TESTED CONFIGURATIONS ................................................................................................................... 102
   6.2          SYSTEM UNDER TEST (SUT) DEFINITION................................................................................................................ 102
   6.3          DRIVER DEFINITION ................................................................................................................................................ 103
7: PRICING ............................................................................................................................................................................ 105
   7.0          GENERAL................................................................................................................................................................. 105
   7.1          PRICED CONFIGURATION ......................................................................................................................................... 105
   7.2          ALLOWABLE SUBSTITUTIONS .................................................................................................................................. 107
8: FULL DISCLOSURE ....................................................................................................................................................... 108
   8.1          REPORTING REQUIREMENTS .................................................................................................................................... 108
   8.2          FORMAT GUIDELINES .............................................................................................................................................. 108
   8.3          FULL DISCLOSURE REPORT CONTENTS AND SUPPORTING FILES ARCHIVE.............................................................. 108

             TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                                                                               Page 6
   8.4          EXECUTIVE SUMMARY ............................................................................................................................................ 115
   8.5          AVAILABILITY OF THE FULL DISCLOSURE REPORT AND SUPPORTING FILES ARCHIVE ............................................ 119
   8.6          REVISIONS TO THE FULL DISCLOSURE REPORT AND SUPPORTING FILES ARCHIVE.................................................. 119
9: AUDIT ................................................................................................................................................................................ 121
   9.1          GENERAL RULES ..................................................................................................................................................... 121
   9.2          AUDITOR'S CHECK LIST........................................................................................................................................... 121
10: GLOBAL DEFINITIONS ............................................................................................................................................... 125
APPENDIX A:                  ORDERED SETS ................................................................................................................................... 126
APPENDIX B:                  APPROVED QUERY VARIANTS ...................................................................................................... 127
APPENDIX C:                  QUERY VALIDATION ........................................................................................................................ 131
APPENDIX D:                  DATA AND QUERY GENERATION PROGRAMS ......................................................................... 132
APPENDIX E:                  SAMPLE EXECUTIVE SUMMARY .................................................................................................. 133
APPENDIX F:                  REFERENCE DATA SET .................................................................................................................... 138




             TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                                                                              Page 7
                                              0: INTRODUCTION

0.1   Preamble
      The TPC Benchmark™H (TPC-H) is a decision support 基准测试. It consists of a suite of business oriented ad-hoc
      queries and concurrent data modifications. The queries and the data populating the 数据库 have been chosen to
      have broad industry-wide relevance while maintaining a sufficient degree of ease of 实现. This
      基准测试 illustrates decision support 系统 that
      •       Examine large volumes of data;
      •       Execute queries with a high degree of complexity;
      •       Give answers to critical business questions.

      TPC-H evaluates the 性能 of various decision support 系统 by the 执行 of sets of queries against a
      standard 数据库 under controlled conditions. The TPC-H queries:
      •       Give answers to real-world business questions;
      •       Simulate generated ad-hoc queries (e.g., via a point and click GUI interface);
      •       Are far more complex than most OLTP transactions;
      •       Include a rich breadth of operators and selectivity constraints;
      •       Generate intensive activity on the 零件 of the 数据库 server 组件 of the 系统 under test;
      •       Are executed against a 数据库 complying to specific population and scaling 要求;
      •       Are implemented with constraints derived from staying closely synchronized with an on-line production
              数据库.
      The TPC-H operations are modeled as follows:
      •       The 数据库 is continuously available 24 hours a day, 7 days a week, for ad-hoc queries from multiple end
              users and data modifications against all 表, except possibly during infrequent (e.g., once a month)
              维护 sessions;
      •       The TPC-H 数据库 tracks, possibly with some delay, the state of the OLTP 数据库 through on-going
              刷新 functions which batch together a number of modifications impacting some 零件 of the decision
              support 数据库;
      •       Due to the world-wide nature of the business data stored in the TPC-H 数据库, the queries and the 刷新
              functions 可 be executed against the 数据库 at any time, especially in relation to each other. In addition,
              this mix of queries and 刷新 functions is subject to specific ACIDity 要求, since queries and
              刷新 functions 可 execute concurrently;
      •       To achieve the optimal compromise between 性能 and operational 要求, the 数据库
              administrator can set, once and for all, the locking levels and the concurrent scheduling 规则 for queries
              and 刷新 functions.

      The minimum 数据库 required to run the 基准测试 holds business data from 10,000 suppliers. It contains almost
      ten million 行 representing a raw storage capacity of about 1 gigabyte. Compliant 基准测试 implementations
      可 also use one of the larger permissible 数据库 populations (e.g., 100 gigabytes), as defined in Clause 4.1.3.

      The 性能 指标 reported by TPC-H is called the TPC-H Composite Query-per-Hour Performance Metric
      (QphH@Size), and reflects multiple aspects of the capability of the 系统 to process queries. These aspects include
      the selected 数据库 size against which the queries are executed, the 查询 processing power when queries are
      submitted by a single stream and the 查询 吞吐量 when queries are submitted by multiple concurrent users. The
      TPC-H Price/Performance 指标 is expressed as $/kQphH@Size. To be compliant with the TPC-H standard, all
      references to TPC-H results for a given 配置 must include all required reporting components (see Clause


      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 8
      5.4.6). The TPC believes that comparisons of TPC-H results measured against different 数据库 sizes are
      misleading and discourages such comparisons.

      The TPC-H 数据库 必须 implemented using a commercially available 数据库 management 系统 (DBMS)
      and the queries executed via an interface using dynamic SQL. The 规范 provides for variants of SQL, as
      implementers are not required to have implemented a specific SQL standard in full.

      TPC-H uses terminology and metrics that are similar to other benchmarks, originated by the TPC and others. Such
      similarity in terminology does not in any way imply that TPC-H results are comparable to other benchmarks. The
      only 基准测试 results comparable to TPC-H are other TPC-H results compliant with the same revision.

      Despite the fact that this 基准测试 offers a rich environment representative of many decision support 系统, this
      基准测试 does not reflect the entire range of decision support 要求. In addition, the extent to which a
      客户 can achieve the results reported by a vendor is highly dependent on how closely TPC-H approximates the
      客户 application. The relative 性能 of 系统 derived from this 基准测试 does not necessarily hold
      for other workloads or environments. Extrapolations to any other environment are not recommended.

      Benchmark results are highly dependent upon 工作负载, specific application 要求, and 系统 design and
      实现. Relative 系统 性能 will vary as a 结果 of these and other factors. Therefore, TPC-H
      应 not be used as a substitute for a specific 客户 application benchmarking when critical capacity planning
      and/or product evaluation decisions are contemplated.

      Benchmark sponsors are permitted several possible 系统 designs, provided that they adhere to the model
      described in Clause 6: . A full disclosure report (FDR) of the 实现 details, as specified in Clause 8, must
      be made available along with the reported results.

      Comment 1: While separated from the main text for readability, comments and appendices are a 零件 of the standard
      and their provisions 必须 complied with.

      Comment 2: The contents of some appendices are provided in a machine readable format and are not included in
      the printed copy of this document.


0.2   General Implementation Guidelines
      The 规则 for 定价 are included in the TPC Pricing Specification located at www.tpc.org.

      The purpose of TPC benchmarks is to provide relevant, objective 性能 data to industry users. To achieve
      that purpose, TPC 基准测试 specifications require that 基准测试 tests be implemented with 系统, products,
      technologies and 定价 that:
      •        Are generally available to users;
      •        Are relevant to the market segment that the individual TPC 基准测试 models or represents (e.g., TPC-H
               models and represents complex, high data volume, decision support environments);
      •        Would plausibly be implemented by a significant number of users in the market segment the 基准测试
               models or represents.
      The use of new 系统, products, technologies (硬件 or 软件) and 定价 is encouraged so long as they
      meet the 要求 above. Specifically prohibited are 基准测试 系统, products, technologies or 定价
      (hereafter referred to as "implementations") whose primary purpose is 性能 优化 of TPC 基准测试
      results without any corresponding applicability to real-world applications and environments. In other words, all
      "基准测试 special" implementations that improve 基准测试 results but not real-world 性能 or 定价, are
      prohibited.

      The following characteristics 应 be used as a guide to judge whether a particular 实现 is a 基准测试
      special. It is not required that each point below be met, but that the cumulative weight of the evidence be considered
      to identify an unacceptable 实现. Absolute certainty or certainty beyond a reasonable doubt is not
      required to make a judgment on this complex issue. The question that 必须 answered is: "Based on the available


      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 9
      evidence, does the clear preponderance (the greater share or weight) of evidence indicate that this 实现 is
      a 基准测试 special?"

      The following characteristics 应 be used to judge whether a particular 实现 is a 基准测试 special:
      a)       Is the 实现 generally available, externally documented, and supported?
      b)       Does the 实现 have significant restrictions on its use or applicability that limits its use beyond
               TPC benchmarks?
      c)       Is the 实现 or 零件 of the 实现 poorly integrated into the larger product?
      d)       Does the 实现 take special advantage of the limited nature of TPC benchmarks (e.g., 查询
               profiles, 查询 mix, concurrency and/or contention, isolation 要求, etc.) in a manner that would not
               be generally applicable to the environment the 基准测试 represents?
      e)       Is the use of the 实现 discouraged by the vendor? (This includes failing to promote the
               实现 in a manner similar to other products and technologies.)
      f)       Does the 实现 require uncommon sophistication on the 零件 of the end-user, programmer, or
               系统 administrator?
      g)       Is the 实现 (including beta) being purchased or used for applications in the market area the
               基准测试 represents? How many sites implemented it? How many end-users benefit from it? If the
               实现 is not currently being purchased or used, is there any evidence to indicate that it will be
               purchased or used by a significant number of end-user sites?

      Comment: The characteristics listed in this 子句 are not intended to include the driver or 实现 specific
      layer, which are not necessarily commercial 软件, and have their own specific 要求 and limitation
      enumerated in Clause 6: . The listed characteristics and prohibitions of Clause 6 应 be used to determine if the
      driver or 实现 specific layer is a 基准测试 special.


0.3   General Measurement Guidelines
      TPC 基准测试 results are expected to be accurate representations of 系统 性能. Therefore, there are
      certain guidelines that are expected to be followed when measuring those results. The approach or methodology to
      be used in the measurements are either explicitly described in the 规范 or left to the discretion of the test
      sponsor. When not described in the 规范, the methodologies and approaches used must meet the following
      要求:
      •        The approach is an accepted engineering practice or standard;
      •        The approach does not enhance the 结果;
      •        Equipment used in measuring the results is calibrated according to established quality standards;
      •        Fidelity and candor is maintained in reporting any anomalies in the results, even if not specified in the TPC
               基准测试 要求.

      Comment: The use of new methodologies and approaches is encouraged so long as they meet the 要求
      above.




      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 10
                                     1: LOGICAL DATABASE DESIGN

1.1   Business and Application Environment
      TPC Benchmark™ H is comprised of a set of business queries designed to exercise 系统 functionalities in a
      manner representative of complex business analysis applications. These queries have been given a realistic context,
      portraying the activity of a wholesale 供应商 to help the reader relate intuitively to the components of the
      基准测试.

      TPC-H does not represent the activity of any particular business segment, but rather any industry which must
      manage sell, or distribute a product worldwide (e.g., car rental, food distribution, parts, suppliers, etc.). TPC-H does
      not attempt to be a model of how to build an actual information analysis application.

      The purpose of this 基准测试 is to reduce the diversity of operations found in an information analysis application,
      while retaining the application's essential 性能 characteristics, namely: the level of 系统 utilization and the
      complexity of operations. A large number of queries of various types and complexities needs to be executed to
      completely manage a business analysis environment. Many of the queries are not of primary interest for
      性能 analysis because of the length of time the queries run, the 系统 resources they use and the frequency
      of their 执行. The queries that have been selected exhibit the following characteristics:
      •        They have a high degree of complexity;
      •        They use a variety of access
      •        They are of an ad hoc nature;
      •        They examine a large percentage of the available data;
      •        They all differ from each other;
      •        They contain 查询 parameters that change across 查询 executions.

      These selected queries provide answers to the following classes of business analysis:
      •        Pricing and promotions;
      •        Supply and demand management;
      •        Profit and 收入 management;
      •        Customer satisfaction study;
      •        Market share study;
      •        Shipping management.

      Although the emphasis is on information analysis, the 基准测试 recognizes the need to periodically 刷新 the
      数据库. The 数据库 is not a one-time snapshot of a business operations 数据库 nor is it a 数据库 where OLTP
      applications are running concurrently. The 数据库 must, however, be able to support queries and 刷新 functions
      against all 表 on a 7 day by 24 hour (7 x 24) basis.

      While the 基准测试 models a business environment in which 刷新 functions are an integral 零件 of data
      维护, the 刷新 functions actually required in the 基准测试 do not attempt to model this aspect of the
      business environment. Their purpose is rather to demonstrate the update functionality for the DBMS, while
      simultaneously assessing an appropriate 性能 成本 to the 维护 of auxiliary data structures, such as
      secondary indices.

      Comment: The 基准测试 does not include any test or measure to verify continuous 数据库 可用性 or
      particular 系统 features which would make the benchmarked 配置 appropriate for 7x24 operation.
      References to continuous 可用性 and 7x24 operation are included in the 基准测试 规范 to provide a
      more complete picture of the anticipated decision support environment. A 配置 offering less that 7x24


      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 11
可用性 can produce compliant 基准测试 results as long as it meets all the 要求 described in this
规范.



                                Decision Makers




                                  DSS Queries




                                        DSS
                                      Database
                                                            Business
                                       TPC-H
                                                             Analysis




     Business
     Operations




                     OLTP
                     Database




                                                                        OLTP
                                                                        Transactions


Figure 1: The TPC-H Business Environment illustrates the TPC-H business environment and highlights the basic
differences between TPC-H and other TPC benchmarks.

Figure 1: The TPC-H Business Environment

Other TPC benchmarks model the operational end of the business environment where transactions are executed on a
real time basis. The TPC-H 基准测试, however, models the analysis end of the business environment where trends
are computed and refined data are produced to support the making of sound business decisions. In OLTP
benchmarks the raw data flow into the OLTP 数据库 from various sources where it is maintained for some period
of time. In TPC-H, periodic 刷新 functions are performed against a DSS 数据库 whose content is queried on
behalf of or by various decision makers.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                Page 12
1.2     Database Entities, Relationships, and Characteristics
        The components of the TPC-H 数据库 are defined to consist of eight separate and individual 表 (the Base
        Tables). The relationships between 列 of these 表 are illustrated in Figure 2: The TPC-H Schema.

        Figure 2: The TPC-H Schema


       PART (P_)                  PARTSUPP (PS_)                  LINEITEM (L_)                    ORDERS (O_)
      SF*200,000                   SF*800,000                    SF*6,000,000                     SF*1,500,000
      PARTKEY                      PARTKEY                        ORDERKEY                       ORDERKEY

      NAME                         SUPPKEY                        PARTKEY                        CUSTKEY

      MFGR                         AVAILQTY                       SUPPKEY                        ORDERSTATUS

      BRAND                        SUPPLYCOST                     LINENUMBER                     TOTALPRICE

      TYPE                         COMMENT                        QUANTITY                       ORDERDATE

      SIZE                                                       EXTENDEDPRICE                   ORDER-
                                  CUSTOMER (C_)                                                  PRIORITY
      CONTAINER                    SF*150,000                     DISCOUNT
                                                                                                 CLERK
                                  CUSTKEY
      RETAILPRICE                                                 TAX                            SHIP-
                                  NAME                                                           PRIORITY
      COMMENT                                                     RETURNFLAG
                                  ADDRESS                                                        COMMENT
                                                                  LINESTATUS
      SUPPLIER (S_)               NATIONKEY
      SF*10,000                                                   SHIPDATE
                                  PHONE
      SUPPKEY                                                     COMMITDATE
                                  ACCTBAL
      NAME                                                        RECEIPTDATE
                                  MKTSEGMENT
      ADDRESS
                                                                  SHIPINSTRUCT
                                  COMMENT
      NATIONKEY                                                   SHIPMODE
      PHONE                          NATION (N_)                  COMMENT
                                         25
      ACCTBAL
                                  NATIONKEY                        REGION (R_)
      COMMENT                                                          5
                                  NAME
                                                                 REGIONKEY
                                  REGIONKEY
                                                                 NAME
                                  COMMENT
                                                                 COMMENT


        Legend:
        •         The parentheses following each 表 name contain the prefix of the 列 names for that 表;
        •         The arrows point in the direction of the one-to-many relationships between 表;
        •         The number/formula below each 表 name represents the cardinality (number of 行) of the 表. Some
                  are factored by SF, the Scale Factor, to obtain the chosen 数据库 size. The cardinality for the LINEITEM
                  表 is approximate (see Clause 4.2.5).




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 13
1.3     Datatype Definitions

1.3.1   The following datatype definitions apply to the list of 列 of each 表:
        •        Identifier means that the 列 必须 able to hold any key 值 generated for that 列 and be able
                 to support at least 2,147,483,647 unique 值;

        Comment: A common 实现 of this datatype will be an integer. However, for SF greater than 300 some
        列 值 will exceed the range of integer 值 supported by a 4-byte integer. A test sponsor 可 use some
        other datatype such as 8-byte integer, decimal or character string to 实现 the identifier datatype;

        •        Integer means that the 列 必须 able to exactly represent integer 值 (i.e., 值 in increments
                 of 1) in the range of at least -2,147,483,646 to 2,147,483,647.
        •        Decimal means that the 列 必须 able to represent 值 in the range -9,999,999,999.99 to
                 +9,999,999,999.99 in increments of 0.01; the 值 can be either represented exactly or interpreted to be in
                 this range;
        •        Big Decimal is of the Decimal datatype as defined above, with the additional property that it 必须 large
                 enough to represent the aggregated 值 stored in temporary 表 created within 查询 variants;
        •        Fixed text, size N means that the 列 必须 able to hold any string of characters of a fixed length of
                 N.
        Comment: If the string it holds is shorter than N characters, then trailing spaces 必须 stored in the 数据库 or
        the 数据库 must automatically pad with spaces upon retrieval such that a CHAR_LENGTH() function will return
        N.
        •        Variable text, size N means that the 列 必须 able to hold any string of characters of a variable
                 length with a maximum length of N. Columns defined as "variable text, size N" 可 optionally be
                 implemented as "fixed text, size N";
        •        Date is a 值 whose external representation can be expressed as YYYY-MM-DD, where all characters
                 are numeric. A 日期 必须 able to express any day within at least 14 consecutive years. There is no
                 要求 specific to the internal representation of a 日期.

        Comment: The 实现 datatype chosen by the test sponsor for a particular datatype 定义 必须
        applied consistently to all the instances of that datatype 定义 in the 模式, except for identifier 列,
        whose datatype 可 be selected to satisfy 数据库 scaling 要求.
1.3.2   The symbol SF is used in this document to represent the 规模因子 for the 数据库 (see Clause 4: ).

1.4     Table Layouts

1.4.1   Required Tables
        The following list defines the required structure (list of 列) of each 表.

        The annotations ‘Primary Key’ and ‘Foreign Key’, as used in this Clause, are for information only and do not imply
        additional 要求 to 实现 主键 and 外键 constraints (see Clause 1.4.2).

            PART Table Layout

            Column Name                    Datatype Requirements            Comment

            P_PARTKEY                      identifier                       SF*200,000 are populated

            P_NAME                         variable text, size 55

            P_MFGR                         fixed text, size 25



        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 14
  P_BRAND                      fixed text, size 10

  P_TYPE                       variable text, size 25

  P_SIZE                       integer

  P_CONTAINER                  fixed text, size 10

  P_RETAILPRICE                decimal

  P_COMMENT                    variable text, size 23

  Primary Key: P_PARTKEY



  SUPPLIER Table Layout

  Column Name                  Datatype Requirements      Comment

  S_SUPPKEY                    identifier                 SF*10,000 are populated

  S_NAME                       fixed text, size 25

  S_ADDRESS                    variable text, size 40

  S_NATIONKEY                  Identifier                 Foreign Key to N_NATIONKEY

  S_PHONE                      fixed text, size 15

  S_ACCTBAL                    decimal

  S_COMMENT                    variable text, size 101

  Primary Key: S_SUPPKEY



  PARTSUPP Table Layout

  Column Name                  Datatype Requirements      Comment

  PS_PARTKEY                   Identifier                 Foreign Key to P_PARTKEY

  PS_SUPPKEY                   Identifier                 Foreign Key to S_SUPPKEY

  PS_AVAILQTY                  integer

  PS_SUPPLYCOST                Decimal

  PS_COMMENT                   variable text, size 199

  Primary Key: PS_PARTKEY, PS_SUPPKEY



  CUSTOMER Table Layout

  Column Name                  Datatype Requirements      Comment

  C_CUSTKEY                    Identifier                 SF*150,000 are populated


TPC BenchmarkTM H Standard Specification Revision 3.0.1                                Page 15
  C_NAME                         variable text, size 25

  C_ADDRESS                      variable text, size 40

  C_NATIONKEY                    Identifier                     Foreign Key to N_NATIONKEY

  C_PHONE                        fixed text, size 15

  C_ACCTBAL                      Decimal

  C_MKTSEGMENT                   fixed text, size 10

  C_COMMENT                      variable text, size 117

  Primary Key: C_CUSTKEY



  ORDERS Table Layout

  Column Name                    Datatype Requirements          Comment

  O_ORDERKEY                     Identifier                     SF*1,500,000 are sparsely populated

  O_CUSTKEY                      Identifier                     Foreign Key to C_CUSTKEY

  O_ORDERSTATUS                  fixed text, size 1

  O_TOTALPRICE                   Decimal

  O_ORDERDATE                    Date

  O_ORDERPRIORITY                fixed text, size 15

  O_CLERK                        fixed text, size 15

  O_SHIPPRIORITY                 Integer

  O_COMMENT                      variable text, size 79

  Primary Key: O_ORDERKEY



  Comment: Orders are not present for all customers. In fact, one-third of the customers do not have any 订单 in
  the 数据库. The orders are assigned at random to two-thirds of the customers (see Clause 4: ). The purpose of
  this is to exercise the capabilities of the DBMS to handle "dead data" when joining two or more 表.



  LINEITEM Table Layout

  Column Name                    Datatype Requirements          Comment

  L_ORDERKEY                     identifier                     Foreign Key to O_ORDERKEY

  L_PARTKEY                      identifier                     Foreign key to P_PARTKEY, first 零件 of the
                                                                compound Foreign Key to (PS_PARTKEY,
                                                                PS_SUPPKEY) with L_SUPPKEY

  L_SUPPKEY                      Identifier                     Foreign key to S_SUPPKEY, second 零件 of the
                                                                compound Foreign Key to (PS_PARTKEY,

TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 16
                                                          PS_SUPPKEY) with L_PARTKEY

  L_LINENUMBER                 integer

  L_QUANTITY                   decimal

  L_EXTENDEDPRICE              decimal

  L_DISCOUNT                   decimal

  L_TAX                        decimal

  L_RETURNFLAG                 fixed text, size 1

  L_LINESTATUS                 fixed text, size 1

  L_SHIPDATE                   日期

  L_COMMITDATE                 日期

  L_RECEIPTDATE                日期

  L_SHIPINSTRUCT               fixed text, size 25

  L_SHIPMODE                   fixed text, size 10

  L_COMMENT                    variable text size 44

  Primary Key: L_ORDERKEY, L_LINENUMBER



  NATION Table Layout

  Column Name                  Datatype Requirements      Comment

  N_NATIONKEY                  identifier                 25 nations are populated

  N_NAME                       fixed text, size 25

  N_REGIONKEY                  identifier                 Foreign Key to R_REGIONKEY

  N_COMMENT                    variable text, size 152

  Primary Key: N_NATIONKEY



  REGION Table Layout

  Column Name                  Datatype Requirements      Comment

  R_REGIONKEY                  identifier                 5 regions are populated

  R_NAME                       fixed text, size 25

  R_COMMENT                    variable text, size 152

  Primary Key: R_REGIONKEY




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                Page 17
1.4.2   Constraints
        The use of constraints is optional and limited to 主键, 外键, check, and not null constraints. If
        constraints are used, they must satisfy the following 要求:
        •        They 必须 specified using SQL. There is no specific 实现 要求. For 示例,
                 CREATE TABLE, ALTER TABLE, CREATE UNIQUE INDEX, and CREATE TRIGGER are all valid
                 statements;
        •        Constraints 必须 enforced either at the statement level or at the 事务 level;
        •        All defined constraints 必须 enforced and validated before the load test is complete (see Clause 5.1.1.2);

1.4.2.1 The NOT NULL 属性 可 be used for any 列.

1.4.2.2 The following 列 or set of 列 listed in Clause 1.4.1 as ‘Primary Key’ 可 be defined as 主键
        constraints (using the PRIMARY KEY 子句 or other equivalent syntax):
        •        P_PARTKEY;
        •        S_SUPPKEY;
        •        PS_PARTKEY, PS_SUPPKEY;
        •        C_CUSTKEY;
        •        O_ORDERKEY;
        •        L_ORDERKEY, L_LINENUMBER;
        •        N_NATIONKEY;
        •        R_REGIONKEY.
        Defining a 主键 约束 can only be done for the 列 listed above.

1.4.2.3 Columns listed in the comments of Clause 1.4.1 as ‘Foreign Key’ 可 be defined as 外键 constraints. There
        is no specific 要求 to use referential actions (e.g., RESTRICT, CASCADE, NO ACTION, etc.). If any
        外键 约束 is defined by an 实现, then all the 外键 constraints listed below 必须
        defined by the 实现 (using the FOREIGN KEY 子句 or other equivalent syntax):S_NATIONKEY
        (referencing N_NATIONKEY);
        •        PS_PARTKEY (referencing P_PARTKEY);
        •        PS_SUPPKEY (referencing S_SUPPKEY);
        •        C_NATIONKEY (referencing N_NATIONKEY);
        •        O_CUSTKEY (referencing C_CUSTKEY);
        •        L_ORDERKEY (referencing O_ORDERKEY);
        •        L_PARTKEY (referencing P_PARTKEY);
        •        L_SUPPKEY (referencing S_SUPPKEY);
        •        L_PARTKEY, L_SUPPKEY (referencing PS_PARTKEY, PS_SUPPKEY);
        •        N_REGIONKEY (referencing R_REGIONKEY);
        Defining a 外键 约束 can only be done for the 列 listed above.

1.4.2.4 Check Constraints: Check constraints 可 be defined to restrict the 数据库 contents. In 订单 to support
        evolutionary change, the check constraints must not rely on knowledge of the enumerated domains of each 列.
        The following list of expressions defines permissible check constraints:
        1.   Positive Keys
             P_PARTKEY >= 0
             S_SUPPKEY >= 0
             C_CUSTKEY >= 0

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 18
             PS_PARTKEY >= 0
             R_REGIONKEY >= 0
             N_NATIONKEY >= 0
        2.   Open-interval constraints
             P_SIZE >= 0
             P_RETAILPRICE >= 0
             PS_AVAILQTY >= 0
             PS_SUPPLYCOST >= 0
             O_TOTALPRICE >= 0
             L_QUANTITY >= 0
             L_EXTENDEDPRICE >= 0
             L_TAX >= 0
        3.   Closed-interval constraints
             L_DISCOUNT between 0.00 and 1.00
        4.   Multi-列 constraints
             L_SHIPDATE <= L_RECEIPTDATE

        Comment: The constraints rely solely on the diagram provided in Clause 1.2and the 说明 in Clause 1.4. They
        are not derived from explicit knowledge of the data population specified in Clause 4.2.

1.5     Implementation Rules

1.5.1   The 数据库 应 be implemented using a commercially available 数据库 management 系统 (DBMS).
1.5.2   The physical clustering of 记录 within the 数据库 is allowed as long as this clustering does not alter the logical
        independence of each 表.

        Comment: The intent of this 子句 is to permit flexibility in the physical design of a 数据库 while preserving a
        strict logical view of all the 表.

1.5.3   At the end of the Load Test, all 表 must have exactly the number of 行 defined for the 规模因子, SF, and the
        数据库 population, both specified in Clause 4: .

1.5.4   Horizontal partitioning of base 表 or auxiliary structures created by 数据库 directives (see Clause 1.5.7) is
        allowed. Groups of 行 from a 表 or auxiliary structure 可 be assigned to different files, disks, or areas. If this
        assignment is a function of data in the 表 or auxiliary structure, the assignment 必须 based on the 值 of a
        partitioning 字段. A partitioning 字段 必须 one and only one of the following:
        •        A 列 or set of 列 listed in Clause 1.4.2.2, whether or not it is defined as a 主键
                 约束;
        •        A 列 or set of 列 listed in Clause 1.4.2.3, whether or not it is defined as a 外键 约束;
        •        A 列 having a 日期 datatype as defined in Clause 1.3.

        Some partitioning schemes require the use of directives that specify explicit 值 for the partitioning 字段. If such
        directives are used they must satisfy the following conditions:

        •        They 可 not rely on any knowledge of the data stored in the 表 except the minimum and maximum
                 值 of 列 used for the partitioning 字段. The minimum and maximum 值 of 列 are
                 specified in Clause 4.2.3
        •        Within the limitations of integer division, they must define each partition to accept an equal portion of the
                 range between the minimum and maximum 值 of the partitioning 列(s). For 日期-based partitions,
                 it is permissible to partition into equally sized domains based upon an integer granularity of days, weeks,
                 months, or years (e.g., 30 days, 4 weeks, 1 month, 1 year, etc.). For 日期-based partition granularities other

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 19
                 than days, a partition boundary 可 extend beyond the minimum or maximum boundaries as established in
                 that 表’s data characteristics as defined in Clause 4.2.3.
        •        The directives must allow the insertion of 值 of the partitioning 列(s) outside the range covered by
                 the minimum and maximum 值, as required by Clause 1.5.13.

        Multiple-level partitioning of base 表 or auxiliary structures is allowed only if each level of partitioning satisfies
        the conditions stated above and each level references only one partitioning 字段 as defined above. If implemented,
        the details of such partitioning 必须 disclosed.

1.5.5   Physical placement of data on durable media is not auditable. SQL DDL that explicitly partitions data vertically is
        prohibited. The 行 必须 logically presented as an atomic set of 列.

        Comment: This implies that vertical partitioning which does not rely upon explicit partitioning directives is
        allowed. Explicit partitioning directives are those that assign groups of 列 of one 行 to files, disks or areas
        different from those storing the other 列 in that 行.

1.5.6   Except as provided in Clause 1.5.7, logical 复制 of 数据库 objects (i.e., 表, 行, or 列) is not
        allowed. The physical 实现 of auxiliary data structures to the 表 可 involve data 复制 of
        selected data from the 表 provided that:
        •        All replicated data are managed by the DBMS, the operating 系统, or the 硬件;
        •        All replications are transparent to all data manipulation operations;
        •        Data modifications are reflected in all logical copies of the replicated data by the time the updating
                 事务 is committed;
        •        All copies of replicated data maintain full ACID properties (see Clause 3: ) at all times.


1.5.7   Auxiliary data structures that constitute logical replications of data from one or more 列 of a base 表 (e.g.,
        indexes, materialized views, summary 表, structures used to enforce relational integrity constraints) must
        conform to the provisions of Clause 1.5.6. The directives defining and creating these structures are subject to the
        following limitations:
        •        Each directive 可 reference no more than one base 表, and 可 not reference other auxiliary structures.
        •        Each directive 可 reference one and only one of the following:
            o    A 列 or set of 列 listed in Clause 1.4.2.2, whether or not it is defined as a 主键
                 约束;
            o    A 列 or set of 列 listed in Clause 1.4.2.3, whether or not it is defined as a 外键 约束;
            o    A 列 having a 日期 datatype as defined in Clause 1.3.
        •        Each directive 可 contain functions or expressions on explicitly permitted 列
        No directives (e.g. DDL, session options, global 配置 parameters) are permitted in TPC-H scripts whose
        effect is to cause the materialization of 列 (or functions on 列) in auxiliary data structures other than
        those 列 explicitly permitted by the above limitations. Further, no directives are permitted whose effect is to
        cause the materialization of 列 in auxiliary data structures derived from more than one 表.

        Comment: Database implementations of auxiliary structures generated as a 结果 of compliant directives usually
        contain embedded pointers or references to corresponding base 表 行. Database implementations that
        transparently employ either ‘行 IDs’ or embedded base 表 ‘Primary Key’ 值 for this purpose are equally
        acceptable.

        In particular, the generation of transparently embedded ‘Primary Key’ 值 required by auxiliary structures is a
        permitted materialization of the ‘Primary Key’ 列(s). ‘Primary Key’ and ‘Foreign Key’ 列 are listed in
        Clause 1.4.1.


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 20
1.5.8    Table names 应 match those provided in Clause 1.4.1. In cases where a 表 name conflicts with a reserved
         word in a given 实现, delimited identifiers or an alternate meaningful name 可 be chosen.
1.5.9    For each 表, the set of 列 must include all those defined in Clause 1.4. No 列 can be added to any of
         the 表. However, the 订单 of the 列 is not constrained.
1.5.10   Column names must match those provided in Clause 1.4

1.5.11   Each 列, as described in Clause 1.4, 必须 logically discrete and independently accessible by the data
         manager. For 示例, C_ADDRESS and C_PHONE cannot be implemented as two sub-parts of a single discrete
         列 C_DATA.
1.5.12   Each 列, as described in Clause 1.4, 必须 accessible by the data manager as a single 列. For 示例,
         P_TYPE cannot be implemented as two discrete 列 P_TYPE1 and P_TYPE2.
1.5.13   The 数据库 must allow for insertion of arbitrary data 值 that conform to the datatype and optional 约束
         definitions from Clause 1.3 and Clause 1.4.

         Comment 1: Although the 刷新 functions (see Clause 2.5) do not insert arbitrary 值 and do not modify all
         表, all 表 必须 modifiable throughout the 性能 test.

         Comment 2: The intent of this Clause is to prevent the 数据库 模式 定义 from taking undue advantage of
         the limited data population of the 数据库 (see also Clause 0.2 and Clause 5.2.7).


1.6      Data Access Transparency Requirements

1.6.1    Data Access Transparency is the property of the 系统 that removes from the 查询 text any knowledge of the
         location and access mechanisms of partitioned data. No finite series of tests can prove that the 系统 supports
         complete data access transparency. The 要求 below describe the minimum capabilities needed to establish
         that the 系统 provides transparent data access. An 实现 that uses horizontal partitioning must meet the
         要求 for transparent data access described in Clause 1.6.2 and Clause 1.6.3.

         Comment: The intent of this Clause is to require that access to physically and/or logically partitioned data be
         provided directly and transparently by services implemented by commercially available layers such as the
         interactive SQL interface, the 数据库 management 系统 (DBMS), the operating 系统 (OS), the 硬件, or
         any combination of these.

1.6.2    Each of the 表 described in Clause 1.4 必须 identifiable by names that have no relationship to the partitioning
         of 表. All data manipulation operations in the executable 查询 text (see Clause 2.1.1.2) must use only these
         names.
1.6.3    Using the names which satisfy Clause 1.6.2, any arbitrary non-TPC-H 查询 必须 able to reference any set of
         行 or 列:
         •        Identifiable by any arbitrary condition supported by the underlying DBMS;
         •        Using the names described in Clause 1.6.2 and using the same data manipulation semantics and syntax for
                  all 表.
         For 示例, the semantics and syntax used to 查询 an arbitrary set of 行 in any one 表 must also be usable
         when querying another arbitrary set of 行 in any other 表.

         Comment: The intent of this 子句 is that each TPC-H 查询 uses general purpose mechanisms to access data in the
         数据库.




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 21
                                 2: QUERIES AND REFRESH FUNCTIONS
        This Clause describes the twenty-two decision support queries and the two 数据库 刷新 functions that 必须
        executed as 零件 of the TPC-H 基准测试.

2.1     General Requirements and Definitions for Queries

2.1.1   Query Overview

2.1.1.1 Each 查询 is defined by the following components:
        •        The business question, which illustrates the business context in which the 查询 could be used;
        •        The functional 查询 定义, which defines, using the SQL-92 language, the function to be performed
                 by the 查询;
        •        The substitution parameters, which describe how to generate the 值 needed to complete the 查询
                 syntax;
        •        The 查询 validation, which describes how to validate the 查询 against the qualification 数据库.

2.1.1.2 For each 查询, the test sponsor must create an 实现 of the functional 查询 定义, referred to as the
        executable 查询 text.
2.1.2   Functional Query Definitions

2.1.2.1 The functional 查询 definitions are written in the SQL-92 language (ISO/IEC 9075:1992), annotated where
        necessary to specify the number of 行 to be returned. They define the function that each executable 查询 text
        must perform against the test 数据库 (see Clause 4.1.1).

2.1.2.2 If an executable 查询 text, with the exception of its substitution parameters, is not identical to the specified
        functional 查询 定义 it must satisfy the 合规 要求 of Clause 2.2.

2.1.2.3 When a functional 查询 定义 includes the creation of a new entity (e.g., cursor, view, or 表) some
        mechanism 必须 used to ensure that newly created entities do not interfere with other 执行 streams and are
        not shared between multiple 执行 streams (see Clause 5.1.2.3).

        Functional 查询 definitions in this document (as well as QGEN, see Clause 2.1.4) achieve this separation by
        appending a text-token to the new entity name. This text-token is expressed in upper case letters and enclosed in
        square brackets (i.e., [STREAM_ID]). This text-token, whenever found in the functional 查询 定义, 必须
        replaced by a unique stream identification number (starting with 0) to complete the executable 查询 text.

        Comment: Once an identification number has been generated and assigned to a given 查询 stream, the same
        identification number 必须 used for that 查询 stream for the duration of the test.

2.1.2.4 When a functional 查询 定义 includes the creation of a 表, the datatype 规范 of the 列 uses
        the <datatype> notation. The 定义 of <datatype> is obtained from Clause 1.3.1.

2.1.2.5 Any entity created within the scope of an executable 查询 text must also be deleted within the scope of that same
        executable 查询 text.

2.1.2.6 A logical tablespace is a named collection of physical storage devices referenced as a single, logically contiguous,
        non-divisible entity.

2.1.2.7 If CREATE TABLE statements are used during the 执行 of the queries, these CREATE TABLE statements
        可 be extended only with a tablespace reference (e.g., IN <tablespacename>). A single tablespace 必须 used for
        all these 表.
        Comment: The allowance for tablespace syntax applies only to variants containing CREATE TABLE statements.


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 22
2.1.2.8 All 表 created during the 执行 of a 查询 must meet the ACID properties defined in Clause 3: .

2.1.2.9 Queries 2, 3, 10, 18 and 21 require that a given number of 行 are to be returned (e.g., “Return the first 10 selected
        行”). If N is the number of 行 to be returned, the 查询 must return exactly the first N 行 unless fewer than N
        行 qualify, in which case all 行 必须 returned. There are three permissible ways of satisfying this
        要求. A test sponsor must select any one of them and use it consistently for all the queries that require that a
        specified number of 行 be returned.
         1.   Vendor-specific control statements supported by a test sponsor’s interactive SQL interface 可 be used (e.g.,
              SET ROWCOUNT n) to limit the number of 行 returned.
         2.   Control statements recognized by the 实现 specific layer (see Clause 6.2.4) and used to control a
              loop which fetches the 行 可 be used to limit the number of 行 returned (e.g., while rowcount <= n).
         3.   Vendor-specific SQL syntax 可 be added to the SELECT statement to limit the number of 行 returned (e.g.,
              SELECT FIRST n). This syntax is not classified as a minor 查询 modification since it completes the functional
              要求 of the functional 查询 定义 and there is no standardized syntax defined. In all other respects,
              the 查询 must satisfy the 要求 of Clause 2.2. The syntax must deal solely with the answer set, and
              must not make any additional explicit reference, for 示例 to 表, indices, or access paths.


2.1.3    Substitution Parameters and Output Data

2.1.3.1 Each 查询 has one or more substitution parameters. When generating executable 查询 text a 值 必须
        supplied for each substitution parameter of that 查询. These 值 必须 used to complete the executable 查询
        text. These substitution parameters are expressed as names in uppercase and enclosed in square brackets. For
        示例, in the Pricing Summary Report Query (see Clause 2.4) the substitution parameter [DELTA], whenever
        found in the functional 查询 定义, 必须 replaced by the 值 generated for DELTA to complete the
        executable 查询 text.

         Comment 1: When dates are 零件 of the substitution parameters, they 必须 expressed in a format that includes
         the year, month and day in integer form, in that 订单 (e.g., YYYY-MM-DD). The delimiter between the year,
         month and day is not specified. Other 日期 representations, for 示例 the number of days since 1970-01-01, are
         specifically not allowed.

         Comment 2: When a substitution parameter appears more than once in a 查询, a single 值 is generated for that
         substitution parameter and each of its occurrences in the 查询 必须 replaced by that same 值.

         Comment 3: Generating executable 查询 text 可 also involve additional text substitution (see Clause 2.1.2.3).


2.1.3.2 The term randomly selected when used in the definitions of substitution parameters means selected at random
        from a uniform distribution over the range or list of 值 specified.

2.1.3.3 Seeds to the random number generator used to generate substitution parameters 必须 selected using the following
        method:
        An initial seed (seed0) is first selected as the time stamp of the end of the 数据库 load time expressed in the format
        mmddhhmmss where mm is the month, dd the day, hh the hour, mm the minutes and ss the seconds. This seed is
        used to seed the Power test of Run 1. Further seeds (for the Throughput test) are chosen as seed0 + 1, seed0 +
        2,...,seed0 + n where s is the number of 吞吐量 streams selected by the vendor. This process leads to s + 1 seeds
        required for Run 1 of a 基准测试 with s streams. The seeds for Run 2 can be the same as those for Run 1 (see
        5.3.2). However, 应 the test sponsor decide to use different seeds for Run 2 from those used for Run 1, the
        sponsor must use a selection process similar to that of Run 1. The seeds must again be of the form seed0, seed0 + 1,
        seed0 + 2,...., seed0 + s, where and seed0 is be the time stamp of the end of Run 1, expressed in the format defined
        above.

         Comment 1: The intent of this Clause is to prevent 性能 advantage that could 结果 from multiple streams
         beginning work with identical seeds or using seeds known in advance while providing a well-defined and unified
         method for seed selection.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 23
        Comment 2: QGEN is a utility provided by the TPC (see Clause 2.1.4) to generate executable 查询 text. If a
        sponsor- created tool is used instead of QGEN, the behavior of its seeds must satisfy this Clause and its code must
        be disclosed. After 执行, the 查询 returns one or more 行. The 行 returned are either 行 from the
        数据库 or 行 built from data in the 数据库 and are called the 输出 data.

2.1.3.4 Output data for each 查询 应 be expressed in a format easily readable by a non-sophisticated computer user. In
        particular, in 订单 to be comparable with known 输出 data for the purpose of 查询 validation (see Clause 2.3),
        the format of the 输出 data for each 查询 must adhere to the following guidelines:
        a)       Columns appear in the 订单 specified by the SELECT list of either the functional 查询 定义 or an
                 approved variant. Column headings are optional.
        b)       Non-integer expressions including prices are expressed in decimal notation with at least two digits behind
                 the decimal point.
        c)       Integer quantities contain no leading zeros.
        d)       Dates are expressed in a format that includes the year, month and day in integer form, in that 订单 (e.g.,
                 YYYY-MM-DD). The delimiter between the year, month and day is not specified. Other 日期
                 representations, for 示例 the number of days since 1970-01-01, are specifically not allowed.
        e)       Strings are case-sensitive and 必须 displayed as such. Leading or trailing blanks are acceptable.
        f)       The amount of white space between 列 is not specified.

2.1.3.5 The precision of all 值 contained in the 查询 validation 输出 data must adhere to the following 规则:
        a)       For singleton 列 值 and results from COUNT aggregates, the 值 must exactly match the 查询
                 validation 输出 data.
        b)       For ratios, results r 必须 within 1% of the 查询 validation 输出 data v when rounded to the nearest
                 1/100th. That is, 0.99*v<=round(r,2)<=1.01*v.
        c)       For results from SUM aggregates, the resulting 值 必须 within $100 of the 查询 validation 输出
                 data.
        d)       For results from AVG aggregates, the resulting 值 r 必须 within 1% of the 查询 validation 输出
                 data when rounded to the nearest 1/100th. That is, 0.99*v<=round(r,2)<=1.01*v.
        Comment 1: In cases where validation 输出 data is computed using a combination of SUM 聚合 and ratios
        (e.g. queries 8,14 and 17), the precision for this validation 输出 data must adhere to bullets b) and c) above.
        Comment 2: In cases where validation 输出 data resembles a 行 count operation by summing up 0 and 1 using a
        SUM 聚合 (e.g. 查询 12), the precision for this validation 输出 data must adhere to bullet a) above.
        Comment 3: In cases were validation 输出 data is selected from views without any further computation (e.g. total
        收入 in Query 15), the precision for this validation 输出 data must adhere to bullet c) above.
        Comment 4: In cases where validation 输出 data is from the 聚合 SUM(l_数量) (e.g. queries 1 and 18),
        the precision for this validation 输出 data must exactly match the 查询 validation data.


2.1.4   The QGEN Program

2.1.4.1 Executable 查询 text 必须 generated according to the 要求 of Clause 2.1.2 and Clause 2.1.3. . QGen is a
        TPC provided 软件 package that 必须 used to generate the 查询 text.

2.1.4.2 The data generated by QGen are meant to be compliant with the 规范 as per Clause 2.1.2 and Clause 2.1.3.
        In case of differences between the content of these two clauses and the text generated by QGen, the 规范
        prevails.

2.1.4.3 The TPC Policies Clause 5.3.1 requires that the version of the 规范 and QGen must match. It is the test
        sponsor’s responsibility to ensure the correct version of QGen is used.

2.1.4.4 QGen has been tested on a variety of platforms. Nonetheless, it is impossible to guarantee that QGen is functionally

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 24
        correct in all aspects or will run correctly on all platforms. It is the Test Sponsor's responsibility to ensure the TPC
        provided 软件 runs in 合规 with the 规范 in their environment(s).


2.1.4.5 If a Test Sponsor must correct an error in QGen in 订单 to publish a Result, the following steps 必须
        performed:
             a. The error 必须 reported to the TPC administrator no later than the time when the Result is submitted.
             b. The error and the modification (i.e. diff of source files) used to correct the error 必须 reported in the
                FDR as described in 子句 8.3.5.5.
             c. The modification used to correct the error 必须 reviewed by a TPC-Certified Auditor as 零件 of the 审计
                process.
        Furthermore any consequences of the modification 可 be used as the basis for a non-合规 challenge.



2.2     Query Compliance

2.2.1   The queries 必须 expressed in a commercially available 实现 of the SQL language. Since the latest
        ISO SQL standard (currently ISO/IEC 9075:1992) has not yet been fully implemented by most vendors, and since
        the ISO SQL language is continually evolving, the TPC-H 基准测试 规范 includes a number of
        permissible deviations from the formal functional 查询 definitions found in Clause 2: . An on-going process is also
        defined to approve additional deviations that meet specific criteria.
2.2.2   There are two types of permissible deviations from the functional 查询 definitions, as follows:
        a)       Minor 查询 modifications;
        b)       Approved 查询 variants.
2.2.3   Minor Query Modifications

2.2.3.1 It is recognized that implementations require specific adjustments for their operating environment and the syntactic
        variations of its dialect of the SQL language. Therefore, minor 查询 modifications are allowed. Minor 查询
        modifications are those that fall within the bounds of what is described in Clause 2.2.3.3. They do not require
        approval. Modifications that do not fall within the bounds of what is described in Clause 2.2.3.3are not minor and
        are not compliant unless they are an integral 零件 of an approved 查询 variant (see Clause 2.2.4).

        Comment 1: The intent of this Clause is to allow the use of any number of minor 查询 modifications. These 查询
        modifications are labeled minor based on the assumption that they do not significantly impact the 性能 of
        the queries.

        Comment 2: The only exception is for the queries that require a given number of 行 to be returned. The
        要求 governing this exception are given in Clause 2.1.2.9.


2.2.3.2 Minor 查询 modifications can be used to produce executable 查询 text by modifying either a functional 查询
        定义 or an approved variant of that 定义.

2.2.3.3 The following 查询 modifications are minor:
        a)       Table names - The 表 and view names found in the CREATE TABLE, CREATE VIEW, DROP VIEW
                 and in the FROM 子句 of each 查询 可 be modified to reflect the customary naming conventions of the
                 系统 under test.
        b)       Select-list expression aliases - For queries that include the 定义 of an alias for a SELECT-list item
                 (e.g., AS CLAUSE), vendor-specific syntax 可 be used instead of the specified SQL-92 syntax.
                 Replacement syntax must have equivalent semantic behavior. Examples of acceptable implementations
                 include "TITLE <string>", or "WITH HEADING <string>". Use of a select-list expression alias is optional.
        c)       Date expressions - For queries that include an expression involving manipulation of dates (e.g.,
                 adding/subtracting days/months/years, or extracting years from dates), vendor-specific syntax 可 be used

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 25
                 instead of the specified SQL-92 syntax. Replacement syntax must have equivalent semantic behavior.
                 Examples of acceptable implementations include "YEAR(<列>)" to extract the year from a 日期
                 列 or "DATE(<日期>) + 3 MONTHS" to add 3 months to a 日期.
        d)       GROUP BY and ORDER BY - For queries that utilize a view, nested 表-expression, or select-list alias
                 solely for the purposes of grouping or ordering on an expression, vendors 可 replace the view, nested
                 tableexpression or select-list alias with a vendor-specific SQL extension to the GROUP BY or ORDER BY
                 子句. Examples of acceptable implementations include "GROUP BY <ordinal>", "GROUP BY
                 <expression>", "ORDER BY <ordinal>", and "ORDER BY <expression>".
        e)       Command delimiters - Additional syntax 可 be inserted at the end of the executable 查询 text for the
                 purpose of signaling the end of the 查询 and requesting its 执行. Examples of such command
                 delimiters are a semicolon or the word "GO".
        f)       Output formatting functions - Scalar functions whose sole purpose is to affect 输出 formatting or
                 intermediate arithmetic 结果 precision (such as CASTs) 可 be applied to items in the outermost SELECT
                 list of the 查询.
        g)       Transaction control statements - A CREATE/DROP TABLE or CREATE/DROP VIEW statement 可 be
                 followed by a COMMIT WORK statement or an equivalent vendor-specific 事务 control statement.
        h)       Correlation names – Table-name aliases 可 be added to the executable 查询 text. The keyword "AS"
                 before the 表-name alias 可 be omitted.
        i)       Explicit ASC - ASC 可 be explicitly appended to 列 in the ORDER BY.
        j)       CREATE TABLE statements 可 be augmented with a tablespace reference conforming to the
                 要求 of Clause 2.1.2.6.
        k)       In cases where identifier names conflict with SQL-92 reserved words in a given 实现, delimited
                 identifiers 可 be used.
        l)       Relational operators - Relational operators used in queries such as "<", ">", "<>", "<=", and "=", 可 be
                 replaced by equivalent vendor-specific operators, for 示例 ".LT.", ".GT.", "!=" or "^=", ".LE.", and
                 "==", respectively.
        m)       Nested 表-expression aliasing - For queries involving nested 表-expressions, the nested keyword "AS"
                 before the 表 alias 可 be omitted.
        n)       If an 实现 is using variants involving views and the 实现 only supports “DROP
                 RESTRICT” semantics (i.e., all dependent objects 必须 dropped first), then additional DROP statements
                 for the dependent views 可 be added.
        o)       At large scale factors, the aggregates 可 exceed the range of the 值 supported by an integer. The
                 聚合 functions AVG and COUNT 可 be replaced with equivalent vendor-specific functions to
                 handle the expanded range of 值 (e.g., AVG_BIG and COUNT_BIG).
        p)       Substring Scalar Functions – For queries which use the SUBSTRING() scalar function, vendor-specific
                 syntax 可 be used instead of the specified SQL 92 syntax. Replacement syntax must have equivalent
                 semantic behavior. For 示例, “SUBSTRING(C_PHONE, 1, 2)”.
        q)       Outer Join – For outer 连接 queries, vendor specific syntax 可 be used instead of the specified SQL 92
                 syntax. Replacement syntax must have equivalent semantic behavior. For 示例, the 连接 expression
                 “CUSTOMER LEFT OUTER JOIN ORDERS ON C_CUSTKEY = O_CUSTKEY” 可 be replaced by
                 adding CUSTOMER and ORDERS to the from 子句 and adding a specially-marked 连接 谓词 (e.g.,
                 C_CUSTKEY *= O_CUSTKEY).

2.2.3.4 The application of minor 查询 modifications to functional 查询 definitions or approved variants 必须 consistent
        over the 查询 set. For 示例, if a particular vendor-specific 日期 expression or 表 name syntax is used in one
        查询, it 必须 used in all other queries involving 日期 expressions or 表 names.

2.2.3.5 The use of minor modifications to obtain executable 查询 text 必须 disclosed and justified (see Clause 8.3.5.3).




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 26
2.2.4   Approved Query Variants

2.2.4.1 Approval of any new 查询 variant is required prior to using such variant to produce compliant TPC-H results. The
        approval process is based on criteria defined in Clause 2.2.4.3.

2.2.4.2 Query variants that have already been approved are listed in Appendix B of this 规范.

        Comment: Since Appendix B is updated each time a new variant is approved, test sponsors 应 obtain the latest
        version of this appendix prior to implementing the 基准测试.

2.2.4.3 The executable 查询 text for each 查询 in a compliant 实现 必须 taken from either the functional
        查询 定义 (see Clause 2: ) or an approved 查询 variant (see Appendix B). Except as specifically allowed in
        Clause 2.2.3.3, executable 查询 text 必须 used in full exactly as written in the TPC-H 规范. New 查询
        variants will be considered for approval if they meet one of the following criteria:
        a)       The vendor cannot successfully run the executable 查询 text against the qualification 数据库 using the
                 functional 查询 定义 or an approved variant even after applying appropriate minor 查询
                 modifications as per Clause 2.2.3.
        b)       The variant contains new or enhanced SQL syntax, relevant to the 基准测试, which is defined in an
                 Approved Committee Draft of a new ISO SQL standard.
        c)       The variant contains syntax that brings the proposed variant closer to adherence to an ISO SQL standard.
        d)       The variant contains minor syntax differences that have a straightforward mapping to ISO SQL syntax used
                 in the functional 查询 定义 and offers functionality substantially similar to the ISO SQL standard.

2.2.4.4 To be approved, a proposed variant 应 have the following properties. Not all of the following properties are
        specifically required. Rather, the cumulative weight of each property satisfied by the proposed variant will be the
        determining factor in approving it.
        a)       Variant is syntactical only, seeking functional compatibility and not 性能 gain.
        b)       Variant is minimal and restricted to correcting a missing functionality.
        c)       Variant is based on knowledge of the business question rather than on knowledge of the 系统 under test
                 (SUT) or knowledge of specific data 值 in the test 数据库.
        d)       Variant has broad applicability among different vendors.
        e)       Variant is non procedural.
        f)       Variant is an SQL-92 standard [ISO/IEC 9075:1992] 实现 of the functional 查询 定义.
        g)       Variant is sponsored by a vendor who can 实现 it and who intends on using it in an upcoming
                 实现 of the 基准测试.

2.2.4.5 Query variants that are submitted for approval will be recorded, along with a rationale describing why they were or
        were not approved.

2.2.4.6 Query variants listed in Appendix B are defined using the conventions defined for functional 查询 definitions (see
        Clause 2.1.2.3 through Clause 2.1.2.6).
2.2.5   Coding Style
        Implementers 可 code the executable 查询 text in any desired coding style, including:
        a)       additional line breaks, tabs or white space
        b)       choice of upper or lower case text
        The coding style used must have no impact on the 性能 of the 系统 under test, and 必须 consistently
        applied across the entire 查询 set. Any coding style that differs from the functional 查询 definitions in Clause 2:
        必须 disclosed.

        Comment: This does not preclude the auditor from verifying that the coding style does not affect 性能.


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 27
2.3     Query Validation

2.3.1   To validate the 合规 of the executable 查询 text, the following validation test 必须 executed by the test
        sponsor and the results reported in the full disclosure report:
        1.   A qualification 数据库 必须 built in a manner substantially the same as the test 数据库 (see Clause 4.1.2).
        2.   The 查询 validation test 必须 run using a qualification 数据库 that has not been modified by any update
             activity (e.g., RF1, RF2, or ACID Transaction executions).
        3.   The 查询 text used (see Clause 2.1.3) 必须 the same as that used in the 性能 test. The default
             substitution parameters provided for each 查询 必须 used. The 刷新 functions, RF1 and RF2, are not
             executed.
        4.   The same driver and 实现 specific layer used to execute the queries against the test 数据库 必须
             used for the validation of the qualification 数据库.
        5.   The resulting 输出 must match the 输出 data specified for the 查询 validation (see Appendix C).
        6.   Any difference between the 输出 obtained and the 查询 validation 输出 must satisfy the 要求 of
             Clause 2.1.3.5.
        Any 查询 whose 输出 differs from the 查询 validation 输出 to a greater degree than allowed by Clause 2.1.3.5
        when run against the qualification 数据库 as specified above is not compliant.

        Comment: The validation test, above, provides a minimum level of assurance of 合规. The auditor 可
        request additional assurance that the 查询 texts execute in accordance with the 基准测试 要求.

2.3.2   No aspect of the System Under Test (e.g., 系统 parameters and conditional 软件 features such as those listed
        in Clause 5.2.7, 硬件 配置, 软件 releases, etc.), 可 differ between this demonstration of
        合规 and the 性能 test.

        Comment: While the intent of this validation test is that it be executed without any change to the 硬件
        配置, building the qualification 数据库 on additional disks (i.e., disks not included in the priced
        配置) is allowed as long as this change has no impact on the results of the demonstration of 合规.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 28
2.4     Query Definitions
        For each 查询 a single 示例 输出 行 is shown (even though queries often produce multiple 行) along with
        the 列 headers. This is for illustration only. See Appendix F: for the precise validation 输出 for each 查询.

2.4.1   Pricing Summary Report Query (Q1)
        This 查询 reports the amount of business that was billed, shipped, and returned.

2.4.1.1 Business Question
        The Pricing Summary Report Query provides a summary 定价 report for all lineitems shipped as of a given 日期.
        The 日期 is within 60 - 120 days of the greatest ship 日期 contained in the 数据库. The 查询 lists totals for
        extended 价格, discounted extended 价格, discounted extended 价格 plus 税, average 数量, average extended
        价格, and average 折扣. These aggregates are grouped by RETURNFLAG and LINESTATUS, and listed in
        ascending 订单 of RETURNFLAG and LINESTATUS. A count of the number of lineitems in each group is
        included.

2.4.1.2 Functional Query Definition

        select
                   l_returnflag,
                   l_linestatus,
                   sum(l_数量) as sum_qty,
                   sum(l_extendedprice) as sum_base_价格,
                   sum(l_extendedprice*(1-l_折扣)) as sum_disc_价格,
                   sum(l_extendedprice*(1-l_折扣)*(1+l_税)) as sum_charge,
                   avg(l_数量) as avg_qty,
                   avg(l_extendedprice) as avg_价格,
                   avg(l_折扣) as avg_disc,
                   count(*) as count_订单
        from
                   行项
        where
                   l_shipdate <= 日期 '1998-12-01' - interval '[DELTA]' day (3)
        group by
                   l_returnflag,
                   l_linestatus
        订单 by
                   l_returnflag,
                   l_linestatus;

2.4.1.3 Substitution Parameters
        Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:

        1.         DELTA is randomly selected within [60. 120].

        Comment: 1998-12-01 is the highest possible ship 日期 as defined in the 数据库 population. (This is ENDDATE -
        30). The 查询 will include all lineitems shipped before this 日期 minus DELTA days. The intent is to choose
        DELTA so that between 95% and 97% of the 行 in the 表 are scanned.

2.4.1.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:

        1.   DELTA = 90.

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 29
2.4.1.5 Sample Output




 L_RETURNFLAG         L_LINESTATUS           SUM_QTY            SUM_BASE_PRICE             SUM_DISC_PRICE

 A                    F                      37734107.00        56586554400.73             53758257134.87



 SUM_CHARGE               AVG_QTY                   AVG_PRICE                  AVG_DISC                  COUNT_ORDER

 55909065222.83           25.52                     38273.13                   .05                       1478493


2.4.2   Minimum Cost Supplier Query (Q2)

        This 查询 finds which 供应商 应 be selected to place an 订单 for a given 零件 in a given 地区.

2.4.2.1 Business Question
        The Minimum Cost Supplier Query finds, in a given 地区, for each 零件 of a certain type and size, the 供应商 who
        can supply it at minimum 成本. If several suppliers in that 地区 offer the desired 零件 type and size at the same
        (minimum) 成本, the 查询 lists the parts from suppliers with the 100 highest account balances. For each 供应商,
        the 查询 lists the 供应商's account balance, name and 国家; the 零件's number and manufacturer; the 供应商's
        address, phone number and comment information.

2.4.2.2 Functional Query Definition

        Return the first 100 selected 行

        select
                 s_acctbal,
                 s_name,
                 n_name,
                 p_partkey,
                 p_mfgr,
                 s_address,
                 s_phone,
                 s_comment
        from
                 零件,
                 供应商,
                 partsupp,
                 国家,
                 地区
        where
                 p_partkey = ps_partkey
                 and s_suppkey = ps_suppkey
                 and p_size = [SIZE]
                 and p_type like '%[TYPE]'
                 and s_nationkey = n_nationkey
                 and n_regionkey = r_regionkey
                 and r_name = '[REGION]'
                 and ps_supplycost = (
                          select

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 30
                             min(ps_supplycost)
                    from
                             partsupp, 供应商,
                             国家, 地区
                    where
                             p_partkey = ps_partkey
                             and s_suppkey = ps_suppkey
                             and s_nationkey = n_nationkey
                             and n_regionkey = r_regionkey
                             and r_name = '[REGION]'
                    )
订单 by
           s_acctbal desc,
           n_name,
           s_name,
           p_partkey;




TPC BenchmarkTM H Standard Specification Revision 3.0.1      Page 31
2.4.2.3 Substitution Parameters
        Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
        1.   SIZE is randomly selected within [1. 50];
        2.   TYPE is randomly selected within the list Syllable 3 defined for Types in Clause 4.2.2.13;
        3.   REGION is randomly selected within the list of 值 defined for R_NAME in 4.2.3.

2.4.2.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
        1.   SIZE = 15;
        2.   TYPE = BRASS;
        3.   REGION = EUROPE.

2.4.2.5 Sample Output



 S_ACCTBAL         S_NAME                        N_NAME                   P_PARTKEY        P_MFGR

 9938.53           Supplier#000005359            UNITED KINGDOM           185358           Manufacturer#4


 S_ADDRESS                   S_PHONE                     S_COMMENT

 QKuHYh,vZGiwu2FW            33-429-790-6131             uriously regular requests hag
 EJoLDx04




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 32
2.4.3    Shipping Priority Query (Q3)
         This 查询 retrieves the 10 unshipped orders with the highest 值.

2.4.3.1 Business Question
        The Shipping Priority Query retrieves the shipping 优先级 and potential 收入, defined as the sum of
        l_extendedprice * (1-l_折扣), of the orders having the largest 收入 among those that had not been shipped as
        of a given 日期. Orders are listed in decreasing 订单 of 收入. If more than 10 unshipped orders exist, only the 10
        orders with the largest 收入 are listed.

2.4.3.2 Functional Query Definition

         Return the first 10 selected 行

         select
                    l_orderkey,
                    sum(l_extendedprice*(1-l_折扣)) as 收入,
                    o_orderdate,
                    o_shippriority
         from
                    客户,
                    orders,
                    行项
         where
                    c_mktsegment = '[SEGMENT]'
                    and c_custkey = o_custkey
                    and l_orderkey = o_orderkey
                    and o_orderdate < 日期 '[DATE]'
                    and l_shipdate > 日期 '[DATE]'
         group by
                    l_orderkey,
                    o_orderdate,
                    o_shippriority
         订单 by
                    收入 desc,
                    o_orderdate;

2.4.3.3 Substitution Parameters
        Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
         1.   SEGMENT is randomly selected within the list of 值 defined for Segments in Clause 4.2.2.13;
         2.   DATE is a randomly selected day within [1995-03-01 .. 1995-03-31].

2.4.3.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
         1.   SEGMENT = BUILDING;
         2.   DATE = 1995-03-15.

2.4.3.5 Sample Output


 L_ORDERKEY                          REVENUE                      O_ORDERDATE                     O_SHIPPRIORITY

 2456423                             406181.01                    1995-03-05                      0


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 33
TPC BenchmarkTM H Standard Specification Revision 3.0.1   Page 34
2.4.4   Order Priority Checking Query (Q4)
        This 查询 determines how well the 订单 优先级 系统 is working and gives an assessment of 客户 satisfac-
        tion.

2.4.4.1 Business Question
        The Order Priority Checking Query counts the number of orders ordered in a given quarter of a given year in which
        at least one 行项 was received by the 客户 later than its committed 日期. The 查询 lists the count of such
        orders for each 订单 优先级 sorted in ascending 优先级 订单.

2.4.4.2 Functional Query Definition

        select
                   o_orderpriority,
                   count(*) as 订单_count
        from
                   orders
        where
                   o_orderdate >= 日期 '[DATE]'
                   and o_orderdate < 日期 '[DATE]' + interval '3' month
                   and exists (
                            select
                                    *
                            from
                                    行项
                            where
                                    l_orderkey = o_orderkey
                                    and l_commitdate < l_receiptdate
                   )
        group by
                   o_orderpriority
        订单 by
                   o_orderpriority;


2.4.4.3 Substitution Parameters
        Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
        1.   DATE is the first day of a randomly selected month between the first month of 1993 and the 10th month of
             1997.

2.4.4.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
        1.   DATE = 1993-07-01.

2.4.4.5 Sample Output



          O_ORDERPRIORITY                     ORDER_COUNT

          1-URGENT                            10594




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 35
2.4.5    Local Supplier Volume Query (Q5)
         This 查询 lists the 收入 volume done through local suppliers.

2.4.5.1 Business Question
        The Local Supplier Volume Query lists for each 国家 in a 地区 the 收入 volume that resulted from 行项
        transactions in which the 客户 ordering parts and the 供应商 filling them were both within that 国家. The
        查询 is run in 订单 to determine whether to institute local distribution centers in a given 地区. The 查询 consid-
        ers only parts ordered in a given year. The 查询 displays the nations and 收入 volume in descending 订单 by
        收入. Revenue volume for all qualifying lineitems in a particular 国家 is defined as sum(l_extendedprice * (1 -
        l_折扣)).

2.4.5.2 Functional Query Definition

         select
                    n_name,
                    sum(l_extendedprice * (1 - l_折扣)) as 收入
         from
                    客户,
                    orders,
                    行项,
                    供应商,
                    国家,
                    地区
         where
                    c_custkey = o_custkey
                    and l_orderkey = o_orderkey
                    and l_suppkey = s_suppkey
                    and c_nationkey = s_nationkey
                    and s_nationkey = n_nationkey
                    and n_regionkey = r_regionkey
                    and r_name = '[REGION]'
                    and o_orderdate >= 日期 '[DATE]'
                    and o_orderdate < 日期 '[DATE]' + interval '1' year
         group by
                    n_name
         订单 by
                    收入 desc;

2.4.5.3 Substitution Parameters
        Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
         1.   REGION is randomly selected within the list of 值 defined for R_NAME in C;aise 4.2.3;
         2.   DATE is the first of January of a randomly selected year within [1993 .. 1997].

2.4.5.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:

         Values for substitution parameters:
         1.   REGION = ASIA;
         2.   DATE = 1994-01-01.




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 36
2.4.5.5 Sample Output


         N_NAME                      REVENUE

         INDONESIA                   55502041.17




       TPC BenchmarkTM H Standard Specification Revision 3.0.1   Page 37
2.4.6   Forecasting Revenue Change Query (Q6)
        This 查询 quantifies the amount of 收入 increase that would have resulted from eliminating certain company-
        wide discounts in a given percentage range in a given year. Asking this type of "what if" 查询 can be used to look
        for ways to increase revenues.

2.4.6.1 Business Question
        The Forecasting Revenue Change Query considers all the lineitems shipped in a given year with discounts between
        DISCOUNT-0.01 and DISCOUNT+0.01. The 查询 lists the amount by which the total 收入 would have
        increased if these discounts had been eliminated for lineitems with l_数量 less than 数量. Note that the
        potential 收入 increase is equal to the sum of [l_extendedprice * l_折扣] for all lineitems with discounts and
        quantities in the qualifying range.

2.4.6.2 Functional Query Definition

        select
                 sum(l_extendedprice*l_折扣) as 收入
        from
                 行项
        where
                 l_shipdate >= 日期 '[DATE]'
                 and l_shipdate < 日期 '[DATE]' + interval '1' year
                 and l_折扣 between [DISCOUNT] - 0.01 and [DISCOUNT] + 0.01
                 and l_数量 < [QUANTITY];


2.4.6.3 Substitution Parameters
        Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
        1.   DATE is the first of January of a randomly selected year within [1993 .. 1997];
        2.   DISCOUNT is randomly selected within [0.02 .. 0.09];
        3.   QUANTITY is randomly selected within [24 .. 25].

2.4.6.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
        1.   DATE = 1994-01-01;
        2.   DISCOUNT = 0.06;
        3.   QUANTITY = 24.

2.4.6.5 Sample Output



          REVENUE

          123141078.23




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 38
2.4.7   Volume Shipping Query (Q7)
        This 查询 determines the 值 of goods shipped between certain nations to help in the re-negotiation of shipping
        contracts.

2.4.7.1 Business Question
        The Volume Shipping Query finds, for two given nations, the gross discounted revenues derived from lineitems in
        which parts were shipped from a 供应商 in either 国家 to a 客户 in the other 国家 during 1995 and 1996.
        The 查询 lists the 供应商 国家, the 客户 国家, the year, and the 收入 from shipments that took place in
        that year. The 查询 orders the answer by Supplier 国家, Customer 国家, and year (all ascending).

2.4.7.2 Functional Query Definition

        select
                   supp_国家,
                   cust_国家,
                   l_year, sum(volume) as 收入
        from (
                   select
                            n1.n_name as supp_国家,
                            n2.n_name as cust_国家,
                            extract(year from l_shipdate) as l_year,
                            l_extendedprice * (1 - l_折扣) as volume
                   from
                            供应商,
                            行项,
                            orders,
                            客户,
                            国家 n1,
                            国家 n2
                   where
                             s_suppkey = l_suppkey
                             and o_orderkey = l_orderkey
                             and c_custkey = o_custkey
                             and s_nationkey = n1.n_nationkey
                             and c_nationkey = n2.n_nationkey
                             and (
                                      (n1.n_name = '[NATION1]' and n2.n_name = '[NATION2]')
                                      or (n1.n_name = '[NATION2]' and n2.n_name = '[NATION1]')
                             )
                             and l_shipdate between 日期 '1995-01-01' and 日期 '1996-12-31'
                   ) as shipping
        group by
                   supp_国家,
                   cust_国家,
                   l_year
        订单 by
                   supp_国家,
                   cust_国家,
                   l_year;

2.4.7.3 Substitution Parameters
        Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
        1.   NATION1 is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3;
        2.   NATION2 is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3 and 必须 dif-
             ferent from the 值 selected for NATION1 in item 1 above.


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 39
2.4.7.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:

        Values for substitution parameters:
        1.   NATION1 = FRANCE;
        2.   NATION2 = GERMANY.

2.4.7.5 Sample Output



          SUPP_NATION             CUST_NATION            YEAR           REVENUE

          FRANCE                  GERMANY                1995           54639732.73




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 40
2.4.8   National Market Share Query (Q8)
        This 查询 determines how the market share of a given 国家 within a given 地区 has changed over two years for
        a given 零件 type.

2.4.8.1 Business Question
        The market share for a given 国家 within a given 地区 is defined as the fraction of the 收入, the sum of
        [l_extendedprice * (1-l_折扣)], from the products of a specified type in that 地区 that was supplied by suppli-
        ers from the given 国家. The 查询 determines this for the years 1995 and 1996 presented in this 订单.

2.4.8.2 Functional Query Definition

        select
                   o_year,
                   sum(case
                            when 国家 = '[NATION]'
                            then volume
                            else 0
                   end) / sum(volume) as mkt_share
        from (
                   select
                             extract(year from o_orderdate) as o_year,
                             l_extendedprice * (1-l_折扣) as volume,
                             n2.n_name as 国家
                   from
                             零件,
                             供应商,
                             行项,
                             orders,
                             客户,
                             国家 n1,
                             国家 n2,
                             地区
                   where
                             p_partkey = l_partkey
                             and s_suppkey = l_suppkey
                             and l_orderkey = o_orderkey
                             and o_custkey = c_custkey
                             and c_nationkey = n1.n_nationkey
                             and n1.n_regionkey = r_regionkey
                             and r_name = '[REGION]'
                             and s_nationkey = n2.n_nationkey
                             and o_orderdate between 日期 '1995-01-01' and 日期 '1996-12-31'
                             and p_type = '[TYPE]'
                   ) as all_nations
        group by
                   o_year
        订单 by
                   o_year;

2.4.8.3 Substitution Parameters
        Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
        1.   NATION is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3;
        2.   REGION is the 值 defined in Clause 4.2.3 for R_NAME where R_REGIONKEY corresponds to
             N_REGIONKEY for the selected NATION in item 1 above;
        3.   TYPE is randomly selected within the list of 3-syllable strings defined for Types in Clause 4.2.2.13.

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 41
2.4.8.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
        1.   NATION = BRAZIL;
        2.   REGION = AMERICA;
        3.   TYPE = ECONOMY ANODIZED STEEL.

2.4.8.5 Sample Output



          YEAR                MKT_SHARE

          1995                .03




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 42
2.4.9    Product Type Profit Measure Query (Q9)
         This 查询 determines how much profit is made on a given line of parts, broken out by 供应商 国家 and year.

2.4.9.1 Business Question
        The Product Type Profit Measure Query finds, for each 国家 and each year, the profit for all parts ordered in that
        year that contain a specified substring in their names and that were filled by a 供应商 in that 国家. The profit is
        defined as the sum of [(l_extendedprice*(1-l_折扣)) - (ps_supplycost * l_数量)] for all lineitems describing
        parts in the specified line. The 查询 lists the nations in ascending alphabetical 订单 and, for each 国家, the year
        and profit in descending 订单 by year (most recent first).

2.4.9.2 Functional Query Definition

         select
                    国家,
                    o_year,
                    sum(amount) as sum_profit
         from (
                    select
                              n_name as 国家,
                              extract(year from o_orderdate) as o_year,
                              l_extendedprice * (1 - l_折扣) - ps_supplycost * l_数量 as amount
                    from
                              零件,
                              供应商,
                              行项,
                              partsupp,
                              orders,
                              国家
                    where
                              s_suppkey = l_suppkey
                              and ps_suppkey = l_suppkey
                              and ps_partkey = l_partkey
                              and p_partkey = l_partkey
                              and o_orderkey = l_orderkey
                              and s_nationkey = n_nationkey
                              and p_name like '%[COLOR]%'
                    ) as profit
         group by
                    国家,
                    o_year
         订单 by
                    国家,
                    o_year desc;

2.4.9.3 Substitution Parameters
        Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   COLOR is randomly selected within the list of 值 defined for the generation of P_NAME in Clause 4.2.3.

2.4.9.4 Query Validation
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
         1.   COLOR = green.



         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 43
2.4.9.5 Sample Output


          NATION                          YEAR                   SUM_PROFIT

          ALGERIA                         1998                   31342867.24




       TPC BenchmarkTM H Standard Specification Revision 3.0.1                 Page 44
2.4.10   Returned Item Reporting Query (Q10)
         The 查询 identifies customers who might be having problems with the parts that are shipped to them.

2.4.10.1 Business question
         The Returned Item Reporting Query finds the top 20 customers, in terms of their effect on lost 收入 for a given
         quarter, who have returned parts. The 查询 considers only parts that were ordered in the specified quarter. The
         查询 lists the 客户's name, address, 国家, phone number, account balance, comment information and 收入
         lost. The customers are listed in descending 订单 of lost 收入. Revenue lost is defined as
         sum(l_extendedprice*(1-l_折扣)) for all qualifying lineitems.

2.4.10.2 Functional Query Definition

         Return the first 20 selected 行

         select
                    c_custkey,
                    c_name,
                    sum(l_extendedprice * (1 - l_折扣)) as 收入,
                    c_acctbal,
                    n_name,
                    c_address,
                    c_phone,
                    c_comment
         from
                    客户,
                    orders,
                    行项,
                    国家
         where
                    c_custkey = o_custkey
                    and l_orderkey = o_orderkey
                    and o_orderdate >= 日期 '[DATE]'
                    and o_orderdate < 日期 '[DATE]' + interval '3' month
                    and l_returnflag = 'R'
                    and c_nationkey = n_nationkey
         group by
                    c_custkey,
                    c_name,
                    c_acctbal,
                    c_phone,
                    n_name,
                    c_address,
                    c_comment
         订单 by
                    收入 desc;

2.4.10.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   DATE is the first day of a randomly selected month from the second month of 1993 to the first month of 1995.

2.4.10.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   DATE = 1993-10-01.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 45
2.4.10.5 Sample Output



       C_CUSTKEY         C_NAME                     REVENUE       C_ACCTBAL   N_NAME

       57040             Customer#000057040         734235.24     632.87      JAPAN




       C_ADDRESS            C_PHONE                 C_COMMENT

       Eioyzjf4pp           22-895-641-3466         sits. slyly regular requests sleep alongside
                                                    of the regular inst




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                             Page 46
2.4.11   Important Stock Identification Query (Q11)
         This 查询 finds the most important subset of suppliers' stock in a given 国家.

2.4.11.1 Business Question
         The Important Stock Identification Query finds, from scanning the available stock of suppliers in a given 国家, all
         the parts that represent a significant percentage of the total 值 of all available parts. The 查询 displays the 零件
         number and the 值 of those parts in descending 订单 of 值.

2.4.11.2 Functional Query Definition

         select
                    ps_partkey,
                    sum(ps_supplycost * ps_availqty) as 值
         from
                    partsupp,
                    供应商,
                    国家
         where
                    ps_suppkey = s_suppkey
                    and s_nationkey = n_nationkey
                    and n_name = '[NATION]'
         group by
                    ps_partkey having
                            sum(ps_supplycost * ps_availqty) > (
                                     select
                                            sum(ps_supplycost * ps_availqty) * [FRACTION]
                                     from
                                            partsupp,
                                            供应商,
                                            国家
                                     where
                                            ps_suppkey = s_suppkey
                                            and s_nationkey = n_nationkey
                                            and n_name = '[NATION]'
                            )
         订单 by
                    值 desc;

2.4.11.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   NATION is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3;
         2.   FRACTION is chosen as 0.0001 / SF.

2.4.11.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:

         Values for substitution parameters:
         1.   NATION = GERMANY;
         2.   FRACTION = 0.0001.




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 47
2.4.11.5 Sample Output




         PS_PARTKEY         VALUE

         129760             17538456.86




        TPC BenchmarkTM H Standard Specification Revision 3.0.1   Page 48
2.4.12   Shipping Modes and Order Priority Query (Q12)
         This 查询 determines whether selecting less expensive modes of shipping is negatively affecting the critical-prior-
         ity orders by causing more parts to be received by customers after the committed 日期.

2.4.12.1 Business Question
         The Shipping Modes and Order Priority Query counts, by ship mode, for lineitems actually received by customers in
         a given year, the number of lineitems belonging to orders for which the l_receiptdate exceeds the l_commitdate for
         two different specified ship modes. Only lineitems that were actually shipped before the l_commitdate are con-
         sidered. The late lineitems are partitioned into two groups, those with 优先级 URGENT or HIGH, and those with a
         优先级 other than URGENT or HIGH.

2.4.12.2 Functional Query Definition

         select
                    l_shipmode,
                    sum(case
                             when o_orderpriority ='1-URGENT'
                                      or o_orderpriority ='2-HIGH'
                             then 1
                             else 0
                    end) as high_line_count,
                    sum(case
                             when o_orderpriority <> '1-URGENT'
                                      and o_orderpriority <> '2-HIGH'
                             then 1
                             else 0
                    end) as low_line_count
         from
                    orders,
                    行项
         where
                    o_orderkey = l_orderkey
                    and l_shipmode in ('[SHIPMODE1]', '[SHIPMODE2]')
                    and l_commitdate < l_receiptdate
                    and l_shipdate < l_commitdate
                    and l_receiptdate >= 日期 '[DATE]'
                    and l_receiptdate < 日期 '[DATE]' + interval '1' year
         group by
                    l_shipmode
         订单 by
                    l_shipmode;

2.4.12.3 Substitution Parameters
         Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
         1.   SHIPMODE1 is randomly selected within the list of 值 defined for Modes in Clause 4.2.2.13;
         2.   SHIPMODE2 is randomly selected within the list of 值 defined for Modes in Clause 4.2.2.13 and 必须
              different from the 值 selected for SHIPMODE1 in item 1;
         3.   DATE is the first of January of a randomly selected year within [1993 .. 1997].

2.4.12.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   SHIPMODE1 = MAIL;

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 49
        2.   SHIPMODE2 = SHIP;
        3.   DATE = 1994-01-01.

2.4.12.5 Sample Output


         L_SHIPMODE                   HIGH_LINE_COUNT             LOW_LINE_COUNT

         MAIL                         6202                        9324




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                    Page 50
2.4.13   Customer Distribution Query (Q13)
         This 查询 seeks relationships between customers and the size of their orders.

2.4.13.1 Business Question
         This 查询 determines the distribution of customers by the number of orders they have made, including customers
         who have no 记录 of orders, past or present. It counts and reports how many customers have no orders, how many
         have 1, 2, 3, etc. A check is made to ensure that the orders counted do not fall into one of several special categories
         of orders. Special categories are identified in the 订单 comment 列 by looking for a particular pattern.

2.4.13.2 Functional Query Definition

         select
                    c_count, count(*) as custdist
         from (
                    select
                               c_custkey,
                               count(o_orderkey)
                    from
                               客户 left outer 连接 orders on
                                       c_custkey = o_custkey
                                       and o_comment not like ‘%[WORD1]%[WORD2]%’
                    group by
                             c_custkey
                    )as c_orders (c_custkey, c_count)
         group by
                    c_count
         订单 by
                    custdist desc,
                    c_count desc;

2.4.13.3 Substitution Parameters
         1.   WORD1 is randomly selected from 4 possible 值: special, pending, unusual, express.
         2.   WORD2 is randomly selected from 4 possible 值: packages, requests, accounts, deposits.

2.4.13.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following substitution param-
         eters and must produce the following 输出 data:

         Values for substitution parameters:
         1.   WORD1 = special.
         2.   WORD2 = requests.

2.4.13.5 Sample Output



          C_COUNT            CUSTDIST

          9                  6641




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 51
2.4.14   Promotion Effect Query (Q14)
         This 查询 monitors the market response to a promotion such as TV advertisements or a special campaign.

2.4.14.1 Business Question
         The Promotion Effect Query determines what percentage of the 收入 in a given year and month was derived from
         promotional parts. The 查询 considers only parts actually shipped in that month and gives the percentage. Revenue
         is defined as (l_extendedprice * (1-l_折扣)).

2.4.14.2 Functional Query Definition

         select
                  100.00 * sum(case
                           when p_type like 'PROMO%'
                           then l_extendedprice*(1-l_折扣)
                           else 0
                  end) / sum(l_extendedprice * (1 - l_折扣)) as promo_收入
         from
                  行项,
                  零件
         where
                  l_partkey = p_partkey
                  and l_shipdate >= 日期 '[DATE]'
                  and l_shipdate < 日期 '[DATE]' + interval '1' month;


2.4.14.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   DATE is the first day of a month randomly selected from a random year within [1993 .. 1997].

2.4.14.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   DATE = 1995-09-01.

2.4.14.5 Sample Output



          PROMO_REVENUE

          16.38




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 52
2.4.15   Top Supplier Query (Q15)
         This 查询 determines the top 供应商 so it can be rewarded, given more business, or identified for special recogni-
         tion.

2.4.15.1 Business Question
         The Top Supplier Query finds the 供应商 who contributed the most to the overall 收入 for parts shipped during
         a given quarter of a given year. In case of a tie, the 查询 lists all suppliers whose contribution was equal to the
         maximum, presented in 供应商 number 订单.

2.4.15.2 Functional Query Definition

         create view 收入[STREAM_ID] (供应商_no, total_收入) as
                  select
                           l_suppkey,
                           sum(l_extendedprice * (1 - l_折扣))
                  from
                           行项
                  where
                           l_shipdate >= 日期 '[DATE]'
                           and l_shipdate < 日期 '[DATE]' + interval '3' month
                  group by
                           l_suppkey;

         select
                    s_suppkey,
                    s_name,
                    s_address,
                    s_phone,
                    total_收入
         from
                    供应商,
                    收入[STREAM_ID]
         where
                    s_suppkey = 供应商_no
                    and total_收入 = (
                             select
                                     max(total_收入)
                             from
                                     收入[STREAM_ID]
                    )
         订单 by
                    s_suppkey;

         drop view 收入[STREAM_ID];

2.4.15.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   DATE is the first day of a randomly selected month between the first month of 1993 and the 10th month of
              1997.

2.4.15.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   DATE = 1996-01-01.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 53
2.4.15.5 Sample Output




 S_SUPPKEY      S_NAME                      S_ADDRESS             S_PHONE           TOTAL_REVENUE

 8449           Supplier#000008449          Wp34zim9qYFbVctdW     20-469-856-8873   1772627.21




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                              Page 54
2.4.16   Parts/Supplier Relationship Query (Q16)
         This 查询 finds out how many suppliers can supply parts with given attributes. It might be used, for 示例, to
         determine whether there is a sufficient number of suppliers for heavily ordered parts.

2.4.16.1 Business Question
         The Parts/Supplier Relationship Query counts the number of suppliers who can supply parts that satisfy a particular
         客户's 要求. The 客户 is interested in parts of eight different sizes as long as they are not of a given
         type, not of a given brand, and not from a 供应商 who has had complaints registered at the Better Business Bureau.
         Results 必须 presented in descending count and ascending brand, type, and size.

2.4.16.2 Functional Query Definition

         select
                    p_brand,
                    p_type,
                    p_size,
                    count(distinct ps_suppkey) as 供应商_cnt
         from
                    partsupp,
                    零件
         where
                    p_partkey = ps_partkey
                    and p_brand <> '[BRAND]'
                    and p_type not like '[TYPE]%'
                    and p_size in ([SIZE1], [SIZE2], [SIZE3], [SIZE4], [SIZE5], [SIZE6], [SIZE7], [SIZE8])
                    and ps_suppkey not in (
                             select
                                      s_suppkey
                             from
                                      供应商
                             where
                                      s_comment like '%Customer%Complaints%'
                    )
         group by
                    p_brand,
                    p_type,
                    p_size
         订单 by
                    供应商_cnt desc,
                    p_brand,
                    p_type,
                    p_size;

2.4.16.3 Substitution Parameters
         Values for the following substitution parameters 必须 generated and used to build the executable 查询 text:
         1.   BRAND = Brand#MN where M and N are two single character strings representing two numbers randomly and
              independently selected within [1 .. 5];
         2.   TYPE is made of the first 2 syllables of a string randomly selected within the list of 3-syllable strings defined
              for Types in Clause 4.2.2.13;
         3.   SIZE1 is randomly selected as a set of eight different 值 within [1 .. 50];
         4.   SIZE2 is randomly selected as a set of eight different 值 within [1 .. 50];
         5.   SIZE3 is randomly selected as a set of eight different 值 within [1 .. 50];
         6.   SIZE4 is randomly selected as a set of eight different 值 within [1 .. 50];


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 55
         7.   SIZE5 is randomly selected as a set of eight different 值 within [1 .. 50];
         8.   SIZE6 is randomly selected as a set of eight different 值 within [1 .. 50];
         9.   SIZE7 is randomly selected as a set of eight different 值 within [1 .. 50];
         10. SIZE8 is randomly selected as a set of eight different 值 within [1 .. 50].

2.4.16.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:

         Values for substitution parameters:
         1.   BRAND = Brand#45.
         2.   TYPE = MEDIUM POLISHED .
         3.   SIZE1 = 49
         4.   SIZE2 = 14
         5.   SIZE3 = 23
         6.   SIZE4 = 45
         7.   SIZE5 = 19
         8.   SIZE6 = 3
         9.   SIZE7 = 36
         10. SIZE8 = 9.

2.4.16.5 Sample Output


       P_BRAND                          P_TYPE                                    P_SIZE        SUPPLIER_CNT

       Brand#41                         MEDIUM BRUSHED TIN                        3             28




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 56
2.4.17   Small-Quantity-Order Revenue Query (Q17)
         This 查询 determines how much average yearly 收入 would be lost if orders were no longer filled for small
         quantities of certain parts. This 可 reduce overhead expenses by concentrating sales on larger shipments.

2.4.17.1 Business Question
         The Small-Quantity-Order Revenue Query considers parts of a given brand and with a given container type and
         determines the average 行项 数量 of such parts ordered for all orders (past and pending) in the 7-year data-
         base. What would be the average yearly gross (undiscounted) loss in 收入 if orders for these parts with a 数量
         of less than 20% of this average were no longer taken?

2.4.17.2 Functional Query Definition

         select
                  sum(l_extendedprice) / 7.0 as avg_yearly
         from
                  行项,
                  零件
         where
                  p_partkey = l_partkey
                  and p_brand = '[BRAND]'
                  and p_container = '[CONTAINER]'
                  and l_数量 < (
                          select
                                     0.2 * avg(l_数量)
                          from
                                     行项
                          where
                                     l_partkey = p_partkey
                  );

2.4.17.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   BRAND = 'Brand#MN' where MN is a two character string representing two numbers randomly and indepen-
              dently selected within [1 .. 5];
         2.   CONTAINER is randomly selected within the list of 2-syllable strings defined for Containers in Clause
              4.2.2.13.

2.4.17.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   BRAND = Brand#23;
         2.   CONTAINER = MED BOX.

2.4.17.5 Sample Output


          AVG_YEARLY

          348406.05




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 57
2.4.18   Large Volume Customer Query (Q18)
         The Large Volume Customer Query ranks customers based on their having placed a large 数量 订单. Large
         数量 orders are defined as those orders whose total 数量 is above a certain level.

2.4.18.1 Business Question
         The Large Volume Customer Query finds a list of the top 100 customers who have ever placed large 数量 orders.
         The 查询 lists the 客户 name, 客户 key, the 订单 key, 日期 and total 价格 and the 数量 for the 订单.

2.4.18.2 Functional Query Definition

         Return the first 100 selected 行

         select
                    c_name,
                    c_custkey,
                    o_orderkey,
                    o_orderdate,
                    o_totalprice,
                    sum(l_数量)
         from
                    客户,
                    orders,
                    行项
         where
                    o_orderkey in (
                            select
                                         l_orderkey
                             from
                                         行项
                             group by
                                         l_orderkey having
                                                 sum(l_数量) > [QUANTITY]
                    )
                    and c_custkey = o_custkey
                    and o_orderkey = l_orderkey
         group by
                    c_name,
                    c_custkey,
                    o_orderkey,
                    o_orderdate,
                    o_totalprice
         订单 by
                    o_totalprice desc,
                    o_orderdate;

2.4.18.3 Substitution Parameters
         Values for the following substitution parameter 必须 generated and used to build the executable 查询 text:
         1.   QUANTITY is randomly selected within [312..315].

2.4.18.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   QUANTITY = 300


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 58
2.4.18.5 Sample Output




 C_NAME                      C_CUSTKEY      O_ORDERKE        O_ORDERDATE   O_TOTALPRICE   Sum(L_QUANTITY)
                                            Y

 Customer#000128120          128120         4722021          1994-04-07    544089.09      323.00




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                    Page 59
2.4.19   Discounted Revenue Query (Q19)
         The Discounted Revenue Query reports the gross discounted 收入 attributed to the sale of selected parts handled
         in a particular manner. This 查询 is an 示例 of code such as might be produced programmatically by a data
         mining tool.

2.4.19.1 Business Question
         The Discounted Revenue 查询 finds the gross discounted 收入 for all orders for three different types of parts
         that were shipped by air and delivered in person. Parts are selected based on the combination of specific brands, a
         list of containers, and a range of sizes.

2.4.19.2 Functional Query Definition

         select
                  sum(l_extendedprice * (1 - l_折扣) ) as 收入
         from
                  行项,
                  零件
         where
                  (
                              p_partkey = l_partkey
                              and p_brand = ‘[BRAND1]’
                              and p_container in ( ‘SM CASE’, ‘SM BOX’, ‘SM PACK’, ‘SM PKG’)
                              and l_数量 >= [QUANTITY1] and l_数量 <= [QUANTITY1] + 10
                              and p_size between 1 and 5
                              and l_shipmode in (‘AIR’, ‘AIR REG’)
                              and l_shipinstruct = ‘DELIVER IN PERSON’
                  )
                  or
                  (
                              p_partkey = l_partkey
                              and p_brand = ‘[BRAND2]’
                              and p_container in (‘MED BAG’, ‘MED BOX’, ‘MED PKG’, ‘MED PACK’)
                              and l_数量 >= [QUANTITY2] and l_数量 <= [QUANTITY2] + 10
                              and p_size between 1 and 10
                              and l_shipmode in (‘AIR’, ‘AIR REG’)
                              and l_shipinstruct = ‘DELIVER IN PERSON’
                  )
                  or
                              (
                              p_partkey = l_partkey
                              and p_brand = ‘[BRAND3]’
                              and p_container in ( ‘LG CASE’, ‘LG BOX’, ‘LG PACK’, ‘LG PKG’)
                              and l_数量 >= [QUANTITY3] and l_数量 <= [QUANTITY3] + 10
                              and p_size between 1 and 15
                              and l_shipmode in (‘AIR’, ‘AIR REG’)
                              and l_shipinstruct = ‘DELIVER IN PERSON’
                  );

2.4.19.3 Substitution Parameters
         1.   QUANTITY1 is randomly selected within [1..10].
         2.   QUANTITY2 is randomly selected within [10..20].
         3.   QUANTITY3 is randomly selected within [20..30].
         4.   BRAND1, BRAND2, BRAND3 = 'Brand#MN' where each MN is a two character string representing two num-
              bers randomly and independently selected within [1 .. 5]


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 60
2.4.19.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
         tion parameters and must produce the following 输出 data:
         Values for substitution parameters:
         1.   QUANTITY1 = 1.
         2.   QUANTITY2 = 10.
         3.   QUANTITY3 = 20.
         4.   BRAND1 = Brand#12.
         5.   BRAND2 = Brand#23.
         6.   BRAND3 = Brand#34.



2.4.19.5 Sample Output



          REVENUE

          3083843.05

         Comment: The TPC recognizes that the predicates on l_shipmode include the non-existing shipmode “AIR REG”.




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 61
2.4.20   Potential Part Promotion Query (Q20)
         The Potential Part Promotion Query identifies suppliers in a particular 国家 having selected parts that 可 be can-
         didates for a promotional offer.

2.4.20.1 Business Question
         The Potential Part Promotion 查询 identifies suppliers who have an excess of a given 零件 available; an excess is
         defined to be more than 50% of the parts like the given 零件 that the 供应商 shipped in a given year for a given
         国家. Only parts whose names share a certain naming convention are considered.

2.4.20.2 Functional Query Definition

         select
                    s_name,
                    s_address
         from
                    供应商, 国家
         where
                    s_suppkey in (
                            select
                                       ps_suppkey
                              from
                                       partsupp
                              where
                                       ps_partkey in (
                                               select
                                                          p_partkey
                                                  from
                                                          零件
                                                  where
                                                        p_name like '[COLOR]%'
                                      )
                              and ps_availqty > (
                                      select
                                               0.5 * sum(l_数量)
                                      from
                                               行项
                                      where
                                               l_partkey = ps_partkey
                                               and l_suppkey = ps_suppkey
                                               and l_shipdate >= 日期('[DATE]’)
                                               and l_shipdate < 日期('[DATE]’) + interval ‘1’ year
                              )
                    )
                    and s_nationkey = n_nationkey
                    and n_name = '[NATION]'
         订单 by
                    s_name;

2.4.20.3 Substitution Parameters
         1.   COLOR is randomly selected within the list of 值 defined for the generation of P_NAME.
         2.   DATE is the first of January of a randomly selected year within 1993..1997.
         3.   NATION is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3.

2.4.20.4 Query Validation


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 62
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:

        Values for substitution parameters:
        1.   COLOR = forest.
        2.   DATE = 1994-01-01.
        3.   NATION = CANADA.

2.4.20.5 Sample Output


        S_NAME                                     S_ADDRESS

        Supplier#000000020                         iybAE,RmTymrZVYaFZva2SH,j




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 63
2.4.21   Suppliers Who Kept Orders Waiting Query (Q21)
         This 查询 identifies certain suppliers who were not able to ship required parts in a timely manner.

2.4.21.1 Business Question
         The Suppliers Who Kept Orders Waiting 查询 identifies suppliers, for a given 国家, whose product was 零件 of a
         multi-供应商 订单 (with current status of 'F') where they were the only 供应商 who failed to meet the committed
         delivery 日期.

2.4.21.2 Functional Query Definition

         Return the first 100 selected 行.

         select
                    s_name,
                    count(*) as numwait
         from
                    供应商,
                    行项 l1,
                    orders,
                    国家
         where
                    s_suppkey = l1.l_suppkey
                    and o_orderkey = l1.l_orderkey
                    and o_orderstatus = 'F'
                    and l1.l_receiptdate > l1.l_commitdate
                    and exists (
                             select
                                      *
                             from
                                      行项 l2
                             where
                                      l2.l_orderkey = l1.l_orderkey
                                      and l2.l_suppkey <> l1.l_suppkey
                    )
                    and not exists (
                             select
                                      *
                             from
                                      行项 l3
                             where
                                      l3.l_orderkey = l1.l_orderkey
                                      and l3.l_suppkey <> l1.l_suppkey
                                      and l3.l_receiptdate > l3.l_commitdate
                    )
                    and s_nationkey = n_nationkey
                    and n_name = '[NATION]'
         group by
                    s_name
         订单 by
                    numwait desc,
                    s_name;

2.4.21.3 Substitution Parameters
         1.   NATION is randomly selected within the list of 值 defined for N_NAME in Clause 4.2.3.

2.4.21.4 Query Validation

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 64
        For validation against the qualification 数据库 the 查询 必须 executed using the following 值 for substitu-
        tion parameters and must produce the following 输出 data:
        Values for substitution parameters:
        1.   NATION = SAUDI ARABIA.

2.4.21.5 Sample Output


         S_NAME                                       NUMWAIT

         Supplier#000002829                           20




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 65
2.4.22   Global Sales Opportunity Query (Q22)
         The Global Sales Opportunity Query identifies geographies where there are customers who 可 be likely to make a
         purchase.

2.4.22.1 Business Question
         This 查询 counts how many customers within a specific range of country codes have not placed orders for 7 years
         but who have a greater than average “positive” account balance. It also reflects the magnitude of that balance.
         Country code is defined as the first two characters of c_phone.

2.4.22.2 Functional Query Definition

         select
                    cntrycode,
                    count(*) as numcust,
                    sum(c_acctbal) as totacctbal
         from (
                    select
                               substring(c_phone from 1 for 2) as cntrycode,
                               c_acctbal
                    from
                               客户
                    where
                              substring(c_phone from 1 for 2) in
                                       ('[I1]','[I2]’,'[I3]','[I4]','[I5]','[I6]','[I7]')
                              and c_acctbal > (
                                       select
                                                   avg(c_acctbal)
                                       from
                                                   客户
                                       where
                                                   c_acctbal > 0.00
                                                   and substring (c_phone from 1 for 2) in
                                                               ('[I1]','[I2]','[I3]','[I4]','[I5]','[I6]','[I7]')
                              )
                              and not exists (
                                       select
                                                   *
                                       from
                                                   orders
                                       where
                                                   o_custkey = c_custkey
                              )
                    ) as custsale
         group by
                    cntrycode
         订单 by
                    cntrycode;

2.4.22.3 Substitution Parameters
         1.   I1 … I7 are randomly selected without repetition from the possible 值 for Country code as defined in Clause
              4.2.2.9.

2.4.22.4 Query Validation
         For validation against the qualification 数据库 the 查询 必须 executed using the following substitution param-
         eters and must produce the following 输出 data:


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 66
        1.    I1 = 13.
        2.    I2 = 31.
        3.    I3 = 23.
        4.    I4 = 29.
        5.    I5 = 30.
        6.    I6 = 18.
        7.    I7 = 17.

2.4.22.5 Sample Output



         CNTRYCODE              NUMCUST                     TOTACCTBAL

         13                     888                         6737713.99




        TPC BenchmarkTM H Standard Specification Revision 3.0.1          Page 67
2.5     General Requirements for Refresh functions

2.5.1   Refresh Function Overview
        Each 刷新函数 is defined by the following components:
        •        The business rationale, which illustrates the business context in which the 刷新 functions could be used;
        •        The 刷新函数 定义, which defines in pseudo-code the function to be performed by the 刷新
                 function;
        •        The 刷新 data set, which defines the set of 行 to be inserted or deleted by each 执行 of the 刷新
                 function into or from the ORDERS and LINEITEM 表. This set of 行 represents 0.1% of the initial
                 population of these two 表 (see Table 4: LINEITEM Cardinality).
2.5.2   Transaction Requirements for Refresh functions
        The 执行 of each 刷新函数 (RF1 or RF2) can be decomposed into any number of 数据库 transactions
        as long as the following conditions are met:
        •        All ACID properties are met;
        •        Each atomic 事务 includes a sufficient number of data modifications to maintain the logical 数据库
                 一致性. For 示例, when adding or deleting a new 订单, the LINEITEM and the ORDERS 表
                 are both modified within the same 事务;
        •        An 输出 message is sent when the last 事务 of the 刷新函数 has completed successfully.
2.5.3   Refresh Function Compliance

2.5.3.1 The 基准测试 规范 does not place any 要求 on the 实现 of the 刷新 functions other
        than their functional equivalence to the 刷新函数 定义 and 合规 with Clause 2.5.2. For RF1 and
        RF2 only, the 实现 is permitted to:
        •        Use any language to write the code for the 刷新 functions;
        •        Pre-process, compile and link the executable code on the SUT at any time prior to or during the
                 measurement interval;
        •        Provide the SUT with the data to be inserted by RF1 or the set of keys for the 行 to be deleted by RF2
                 prior to the 执行 of the 基准测试 (this specifically does not allow pre-执行 of the 刷新
                 functions).
        Comment: The intent is to separate the resources required to generate the data to be inserted (or the set of key for
        the 行 to be deleted) from the resources required to execute insert and delete operations against the 数据库.
        •        Group the individual 刷新 functions into transactions and organize their 执行 serially or in parallel.
                 This grouping 可 be different in the power test and in the 吞吐量 test.

2.5.3.2 The 刷新 functions do not produce any 输出 other than a message of successful completion.

2.5.3.3 The proper 实现 of the 刷新 functions 必须 validated by the independent auditor who 可 request
        additional tests to ascertain that the 刷新 functions execute in accordance with the 基准测试 要求.

2.6     New Sales Refresh Function (RF1)
        This 刷新函数 adds new sales information to the 数据库.
2.6.1   Business Rationale
        The New Sales 刷新函数 inserts new 行 into the ORDERS and LINEITEM 表 in the 数据库 following
        the scaling and data generation methods used to populate the 数据库.
2.6.2   Refresh Function Definition

        LOOP (SF * 1500) TIMES



        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 68
        INSERT a new 行 into the ORDERS 表
        LOOP RANDOM(1, 7) TIMES
              INSERT a new 行 into the LINEITEM 表
        END LOOP
        END LOOP

        Comment: The 刷新 functions can be implemented with much greater flexibility than the queries (see Clause
        2.5.3). The 定义 provided here is an 示例 only. Test sponsors 可 wish to explore other implementations.
2.6.3   Refresh Data Set
        The set of 行 to be inserted 必须 produced by DBGen using the -U option. This option will produce as many
        sets of 行 as required for use in multi-stream tests.

2.7     Old Sales Refresh Function (RF2)
        This 刷新函数 removes old sales information from the 数据库.
2.7.1   Business Rationale
        The Old Sales 刷新函数 removes 行 from the ORDERS and LINEITEM 表 in the 数据库 to emulate
        the removal of stale or obsolete information.
2.7.2   Refresh Function Definition

        LOOP (SF * 1500) TIMES
               DELETE FROM ORDERS WHERE O_ORDERKEY = [值]
               DELETE FROM LINEITEM WHERE L_ORDERKEY = [值]
        END LOOP

        Comment: The 刷新 functions can be implemented with much greater flexibility than the queries (see Clause
        2.5.3). The 定义 provided here is an 示例 only. Test sponsors 可 wish to explore other 实现
2.7.3   Refresh Data Set
        The ’Primary Key’ 值 for the set of 行 to be deleted 必须 produced by DBGen using the -U option. This
        option will produce as many sets of ’Primary Keys’ as required for use in multi-stream 吞吐量 tests. The 行
        being deleted begin with the first 行 of each of the two targeted 表.

2.8     Database Evolution Process
        The test sponsor must assure the correctness of the 数据库 for each run within the 性能 test.
        This is accomplished by ”evolving” the test 数据库, keeping track of which set of inserted and deleted 行 应
        be used by RF1 and RF2 for each run (see Clause 5.1.1.4).

        Comment: It is explicitly not permitted to rebuild or reload the test 数据库 during the 性能 test (see Clause
        5.1.1.3).
2.8.1   The test 数据库 可 be endlessly reused if the test sponsor keeps careful track of how many pairs of 刷新 func-
        tions RF1/RF2 have been executed and completed successfully. For 示例, a test sponsor running five streams
        would execute one RF1/RF2 pair during the power test using the first set of insert/delete 行 produced by DBGEN
        (see Clause 4.2.1). The 吞吐量 test would then execute the next five RF1/RF2 pairs using the second through the
        sixth sets of inset/delete 行 produced by DBGEN. The next run would use the sets of insert/delete 行 produced
        by DBGEN for the seventh RF1/RF2 pair, and continue from there.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 69
                                           3: THE ACID PROPERTIES

3.1.1   The ACID (Atomicity, Consistency, Isolation, and Durability) properties of 事务 processing 系统 必须
        supported by the 系统 under test during the timed portion of this 基准测试. Since TPC-H is not a 事务
        processing 基准测试, the ACID properties 必须 evaluated outside the timed portion of the test. It is the intent of
        this 节 to informally define the ACID properties and to specify a series of tests that can be performed to
        demonstrate that these properties are met.
3.1.2   While it is required for the 系统 under test (SUT) to support the ACID properties defined in this Clause, the exe-
        cution of the corresponding ACID tests is only required in lieu of supplying other sufficient evidence of the SUT's
        support for these ACID properties. The existence of another published TPC-H 基准测试 for which support for the
        ACID properties have been demonstrated using the tests defined in this Clause 可 be sufficient evidence that the
        new SUT supports some or all of the required ACID properties. The determination of whether previously published
        TPC-H test results are sufficient evidence of the above is left to the discretion of the auditor.

        Comment 1: No finite series of tests can prove that the ACID properties are fully supported. Being able to pass the
        specified tests is a necessary, but not sufficient, condition for meeting the ACID 要求.

        Comment 2: The ACID tests are intended to demonstrate that the ACID properties are supported by the SUT and
        enabled during the 性能 measurements. They are not intended to be an exhaustive quality assurance test.
3.1.3   The ACID tests 必须 performed against the qualification 数据库. The same set of mechanisms used to ensure
        full ACID properties of the qualification 数据库 during the ACID tests 必须 used/enabled for the test 数据库
        during the 性能 test. This applies both to attributes of the 数据库 and to attributes of the 数据库 session(s)
        used to execute the ACID and 性能 tests. The attributes of the session executing the ACID Query (see
        Clause 3.1.6.3) 必须 the same as those used in the 性能 test 查询 stream(s) (see Clause 5.1.2.3), and the
        attributes of the session executing the ACID 事务 (see Clause 3.1.6.2) 必须 the same as those used in the
        性能 test 刷新 stream (see Clause 5.1.2.4).
3.1.4   The mechanisms used to ensure 持久性 of the qualification 数据库 必须 enabled for the test 数据库. For
        示例:

          a)   If the qualification 数据库 relies on undo logs to ensure atomicity, then such logging must also be enabled
               for the test 数据库 during the 性能 test, even though no transactions are aborted.

          b)   If the qualification 数据库 relies on a 数据库 backup to meet the 持久性 要求 (see Clause 3.5), a
               backup 必须 taken of the test 数据库.

          c)   If the qualification 数据库 relies on data redundancy mechanisms to meet the 持久性 要求 (see
               Clause 3.5), these mechanisms 必须 active during the 执行 of the 性能 test.
3.1.5   The test sponsor must attest that the reported 配置 would also pass the ACID tests with the test 数据库.
3.1.6   The ACID Transaction and The ACID Query

        Since this 基准测试 does not contain any OLTP 事务, a special ACID Transaction is defined for use in
        some of the ACID tests. In addition, to simplify the demonstration that ACID properties are enabled while read-only
        queries are executing concurrently with other activities, a special ACID Query is defined.

3.1.6.1 Both the ACID 事务 and the ACID Query utilize a truncation function to guarantee arithmetic function por-
        tability and 一致性 of results. Define trunc(n,p) as

                                             Trunk(n, p) =  n * 10p   10p
                 which truncates n to the pth decimal place (e.g., trunc(1.357,2) = 1.35).

        Comment: The intent of this 子句 is to specify the required functionality without dictating a particular implemen-
        tation.

3.1.6.2 The ACID Transaction 必须 implemented to conform to the following 事务 profile:

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 70
Given the set of 输入 data (O_KEY, L_KEY, [delta]), with
•       O_KEY selected at random from the same distribution as that used to populate L_ORDERKEY in the
        qualification 数据库 (see Clause 4.2.3),
•       L_KEY selected at random from [1 .. M] where

        M = SELECT MAX(L_LINENUMBER) FROM LINEITEM WHERE L_ORDERKEY = O_KEY

        using the qualification 数据库, and [delta] selected at random within [1 .. 100]:

        BEGIN TRANSACTION

        Read O_TOTALPRICE from ORDERS into [ototal] where O_ORDERKEY = [o_key]

        Read L_QUANTITY, L_EXTENDEDPRICE, L_PARTKEY, L_SUPPKEY, L_TAX, L_DISCOUNT into
            [数量], [extprice], [pkey], [skey], [税], [disc]
            where L_ORDERKEY = [o_key] and L_LINENUMBER = [l_key]

        Set [ototal] = [ototal] -
              trunc( trunc([extprice] * (1 - [disc]), 2) * (1 + [税]), 2)

        Set [rprice] = trunc([extprice]/[数量], 2)

        Set [成本] = trunc([rprice] * [delta], 2)

        Set [new_extprice] = [extprice] + [成本]

        Set [new_ototal] = trunc([new_extprice] * (1.0 - [disc]), 2)

        Set [new_ototal] = trunc([new_ototal] * (1.0 + [税]), 2)

        Set [new_ototal] = [ototal] + [new_ototal]

        Update LINEITEM
            where L_ORDERKEY = [o_key] and L_LINENUMBER = [l_key]

        Set L_EXTENDEDPRICE = [new_extprice]

        Set L_QUANTITY = [数量] + [delta]

        Write L_EXTENDEDPRICE, L_QUANTITY to LINEITEM

        Update ORDERS where O_ORDERKEY = [o_key]

        Set O_TOTALPRICE = [new_ototal]

        Write O_TOTALPRICE to ORDERS

        Insert Into HISTORY
              Values ([pkey], [skey], [o_key], [l_key], [delta], [current_日期_time])

        COMMIT TRANSACTION

        Return [rprice], [数量], [税], [disc], [extprice], [ototal] to driver




Where HISTORY is a 表 required only for the ACID tests and defined as follows:


TPC BenchmarkTM H Standard Specification Revision 3.0.1                                        Page 71
            Column Name                Datatype Requirements

            H_P_KEY                    identifier                        Foreign reference to P_PARTKEY

            H_S_KEY                    identifier                        Foreign reference to S_SU

            H_O_KEY                    identifier                        Foreign reference to
                                                                         O_ORDERKEY

            H_L_KEY                    integer

            H_DELTA                    integer

            H_DATE_T                   日期 and time to second

        Comment: The 值 returned by the ACID Transaction are the old 值, as read before the updates.

3.1.6.3 The ACID Query 必须 implemented to conform to the following functional 查询 定义:
        Given the 输入 data:
        •        O_KEY, selected within the same distributions as those used for the population of L_ORDERKEY in the
                 qualification 数据库:

                 SELECT SUM(trunc(
                     trunc(L_EXTENDEDPRICE * (1 - L_DISCOUNT),2) * (1 + L_TAX),2))
                     FROM LINEITEM
                     WHERE L_ORDERKEY = [o_key]

3.1.6.4 The ACID Transaction and the ACID Query 必须 used to demonstrate that the ACID properties are fully sup-
        ported by the 系统 under test.

3.1.6.5 Although the ACID Transaction and the ACID Query do not involve all the 表 of the TPC-H 数据库, the ACID
        properties 必须 supported for all 表 of the TPC-H 数据库.

3.2     Atomicity Requirements

3.2.1   Atomicity Property Definition
        The 系统 under test must guarantee that transactions are atomic; the 系统 will either perform all individual
        operations on the data, or will assure that no partially-completed operations leave any effects on the data.
3.2.2   Atomicity Tests

3.2.2.1 Perform the ACID Transaction (see Clause 3.1.5) for a randomly selected set of 输入 data and verify that the appro-
        priate 行 have been changed in the ORDERS, LINEITEM, and HISTORY 表.

3.2.2.2 Perform the ACID Transaction for a randomly selected set of 输入 data, substituting a ROLLBACK of the transac-
        tion for the COMMIT of the 事务. Verify that the appropriate 行 have not been changed in the ORDERS,
        LINEITEM, and HISTORY 表.

3.3     Consistency Requirements

3.3.1   Consistency Property Definition
        Consistency is the property of the application that requires any 执行 of transactions to take the 数据库 from
        one consistent state to another.
3.3.2   Consistency Condition

3.3.2.1 A consistent state for the TPC-H 数据库 is defined to exist when:


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 72
                  O_TOTALPRICE =
                     SUM(trunc(trunc(L_EXTENDEDPRICE *(1 - L_DISCOUNT),2) * (1+L_TAX),2))

        for each ORDERS and LINEITEM defined by (O_ORDERKEY = L_ORDERKEY)

3.3.2.2 A TPC-H 数据库, when populated as defined in Clause 4.2, must meet the 一致性 condition defined in Clause
        3.3.2.1.

3.3.2.3 If data is replicated, as permitted under Clause 1.5.7, each copy must meet the 一致性 condition defined in
        Clause 3.3.2.1.
3.3.3   Consistency Tests
        To verify the 一致性 between the ORDERS, and LINEITEM 表, perform the following steps:
        1.   Verify that the ORDERS, and LINEITEM 表 are initially consistent as defined in Clause 3.3.2.1, based on a
             random sample of at least 10 distinct 值 of O_ORDERKEY.
        2.   Submit at least 100 ACID Transactions from each of at least the number of 执行 streams ( # 查询 streams
             + 1 刷新 stream) used in the reported 吞吐量 test (see Clause 5.3.4). Each 事务 must use 值 of
             (O_KEY, L_KEY, DELTA) randomly generated within the ranges defined in Clause 3.1.6.2. Ensure that all the
             值 of O_ORDERKEY chosen in Step 1 are used by some 事务 in Step 2.
        3.   Re-verify the 一致性 of the ORDERS, and LINEITEM 表 as defined in Clause 3.3.2.1 based on the
             same sample 值 of O_ORDERKEY selected in Step 1.

3.4     Isolation Requirements

3.4.1   Isolation Property Definition
        Isolation can be defined in terms of the following phenomena that 可 occur during the 执行 of concurrent
        数据库 transactions (i.e., read-write transactions or read-only queries):
        P0 (“Dirty Write”): Database 事务 T1 reads a data element and modifies it. Database 事务 T2
                then modifies or deletes that data element, and performs a COMMIT. If T1 were to attempt to re-
                read the data element, it 可 receive the modified 值 from T2 or discover that the data element
                has been deleted.
        P1 (“Dirty Read”): Database 事务 T1 modifies a data element. Database 事务 T2 then reads
                that data element before T1 performs a COMMIT. If T1 were to perform a ROLLBACK, T2 will
                have read a 值 that was never committed and that 可 thus be considered to have never existed.
        P2 (“Non-repeatable Read”): Database 事务 T1 reads a data element. Database 事务 T2 then
               modifies or deletes that data element, and performs a COMMIT. If T1 were to attempt to re-read
               the data element, it 可 receive the modified 值 or discover that the data element has been
               deleted.
        P3 (“Phantom”): Database 事务 T1 reads a set of 值 N that satisfy some <search condition>.
                Database 事务 T2 then executes statements that generate one or more data elements that
                satisfy the <search condition> used by 数据库 事务 T1. If 数据库 事务 T1 were to
                repeat the initial read with the same <search condition>, it obtains a different set of 值.
        Each 数据库 事务 T1 and T2 above 必须 executed completely or not at all.

        The following 表 defines four isolation levels with respect to the phenomena P0, P1, P2, and P3.



                     Phenomena P0      Phenomena P1       Phenomena P2        Phenomena P3

        Level 0      Not Possible      Possible           Possible            Possible

        Level 1      Not Possible      Not Possible       Possible            Possible

        Level 2      Not Possible      Not Possible       Not Possible        Possible

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 73
        Level 3       Not Possible       Not Possible      Not Possible         Not Possible

        Table 1: Isolation Levels

        The following terms are defined:
        T1 = An instance of the ACID Transaction;
        T2 = An instance of the ACID Transaction;
        T3 = Any of the TPC-H queries 1 to 22 or an instance of the ACID 查询;
        Tn = Any arbitrary 事务.
        Although arbitrary, the 事务 Tn 应 not do dirty writes.
        The following 表 defines the isolation 要求 that 必须 met by TPC-H implementations.



 Req. #     For transactions in      these phenomena:    must NOT be seen        Textual Description:
            this set:                                    by this 事务:

 1.         { Ti, Tj} 1  i,j  2    P0, P1, P2, P3      Ti                      Level 3 isolation between any two ACID
                                                                                 Transactions.

 2.         { Ti, Tn} 1  i  2      P0, P1, P2          Ti                      Level 2 isolation for any ACID Transaction
                                                                                 relative to any arbitrary 事务.

 3.         { Ti, T3}1  i  n       P0, P1              Ti                      Level 1 isolation for any of TPC-H queries
                                                                                 1 to 22 relative to any ACID Transaction
                                                                                 and any arbitrary 事务.

        Table 2: Isolation Requirements
        Sufficient conditions 必须 enabled at either the 系统 or application level to ensure the required isolation
        defined above is obtained.

        However, the required isolation levels must not be obtained by the use of configurations or explicit session-level
        options that give a particular session or 事务 a priori exclusive access to the 数据库.

        The intent is not to preclude automatic mechanisms such as lock escalation, but to disallow configurations and
        options that would a priori preclude queries and update transactions against the same 数据库 from making progress
        concurrently.

        In addition, the 配置 of the 数据库 or session-level options 必须 such that the continuous submission
        of arbitrary (read-only) queries against one or more 表 could not indefinitely delay update transactions affecting
        those 表 from making progress.
3.4.2   Isolation Tests
        For conventional locking schemes, isolation 应 be tested as described below. Systems that 实现 other isola-
        tion schemes 可 require different validation techniques. It is the responsibility of the test sponsor to disclose those
        techniques and the tests for them. If isolation schemes other than conventional locking are used, it is permissible to
        实现 these tests differently provided full details are disclosed.

        The six tests described here are designed to verify that the 系统 under test is configured to support the required
        isolation levels, as defined in Clause 3.4.1. All Isolation Tests are performed using a randomly selected set of 值
        (P_KEY, S_KEY, O_KEY, L_KEY, DELTA).
        Comment: In the isolation tests, the 值 returned by the ACID Transaction are the old 值, as read before the
        updates.

3.4.2.1 Isolation Test 1


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 74
         This test demonstrates isolation for the read-write conflict of a read-write 事务 and a read-only 事务
         when the read-write 事务 is committed. Perform the following steps:
         1.   Start an ACID Transaction Txn1 for a randomly selected O_KEY, L_KEY, and DELTA.
         2.   Suspend Txn1 immediately prior to COMMIT.
         3.   Start an ACID Query Txn2 for the same O_KEY as in Step 1. (Txn2 attempts to read the data that has just been
              updated by Txn1.)
         4.   Verify that Txn2 does not see Txn1's updates.
         5.   Allow Txn1 to complete.
         6.   Txn2 应 now have completed.

3.4.2.2 Isolation Test 2
        This test demonstrates isolation for the read-write conflict of a read-write 事务 and a read-only 事务
        when the read-write 事务 is rolled back. Perform the following steps:
         1.   Start an ACID Transaction Txn1 for a randomly selected O_KEY, L_KEY, and DELTA.
         2.   Suspend Txn1 immediately prior to COMMIT.
         3.   Start an ACID Query Txn2 for the same O_KEY as in Step 1. (Txn2 attempts to read the data that has just been
              updated by Txn1.)
         4.   Verify that Txn2 does not see Txn1's updates.
         5.   Force Txn1 to rollback.
         6.   Txn2 应 now have completed.

3.4.2.3 Isolation Test 3
        This test demonstrates isolation for the write-write conflict of two update transactions when the first 事务 is
        committed. Perform the following steps:
         1.   Start an ACID Transaction Txn1 for a randomly selected O_KEY, L_KEY, and DELTA1.
         2.   Stop Txn1 immediately prior to COMMIT.
         3.   Start another ACID Transaction Txn2 for the same O_KEY, L_KEY and for a randomly selected DELTA2.
              (Txn2 attempts to read and update the data that has just been updated by Txn1.)
         4.   Verify that Txn2 waits.
         5.   Allow Txn1 to complete. Txn2 应 now complete.
         6.   Verify that

                  Txn2.L_EXTENDEDPRICE = Txn1.L_EXTENDEDPRICE+

                  (DELTA1 * (Txn1.L_EXTENDEDPRICE / Txn1.L_QUANTITY))

3.4.2.4 Isolation Test 4
        This test demonstrates isolation for the write-write conflict of two update transactions when the first 事务 is
        rolled back. Perform the following steps:
         1.   Start an ACID Transaction Txn1 for a randomly selected O_KEY, L_KEY, and DELTA1.
         2.   Stop Txn1 immediately prior to COMMIT.
         3.   Start another ACID Transaction Txn2 for the same O_KEY, L_KEY and for a randomly selected DELTA2.
              (Txn2 attempts to read and update the data that has just been updated by Txn1.)
         4.   Verify that Txn2 waits.
         5.   Force Txn1 to rollback. Txn2 应 now complete.
         6.   Verify that

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 75
                   Txn2.L_EXTENDEDPRICE = Txn1.L_EXTENDEDPRICE

3.4.2.5 Isolation Test 5
        This test demonstrates the ability of read and write transactions affecting different 数据库 表 to make progress
        concurrently.
         1.    Start an ACID Transaction Txn1 with randomly selected 值 of O_KEY, L_KEY and DELTA.
         2.    Suspend Txn1 immediately prior to COMMIT.
         3.    Start a 事务 Txn2 that does the following:
         4.    Select random 值 of PS_PARTKEY and PS_SUPPKEY. Return all 列 of the PARTSUPP 表 for
               which PS_PARTKEY and PS_SUPPKEY are equal to the selected 值.
         5.    Verify that Txn2 completes.
         6.    Allow Txn1 to complete. Verify that the appropriate 行 in the ORDERS, LINEITEM and HISTORY 表
               have been changed.

3.4.2.6 Isolation Test 6
        This test demonstrates that the continuous submission of arbitrary (read-only) queries against one or more 表 of
        the 数据库 does not indefinitely delay update transactions affecting those 表 from making progress.
         1.    Start a 事务 Txn1. Txn1 executes Q1 (from Clause 2.4) against the qualification 数据库 where the sub-
               stitution parameter [delta] is chosen from the interval [0 .. 2159] so that the 查询 runs for a sufficient length of
               time.
         Comment: Choosing [delta] = 0 will maximize the run time of Txn1.
         2.    Before Txn1 completes, submit an ACID Transaction Txn2 with randomly selected 值 of O_KEY, L_KEY
               and DELTA.
         If Txn2 completes before Txn1 completes, verify that the appropriate 行 in the ORDERS, LINEITEM and HIS-
         TORY 表 have been changed. In this case, the test is complete with only Steps 1 and 2. If Txn2 will not complete
         before Txn1 completes, perform Steps 3 and 4:
         3.    Ensure that Txn1 is still active. Submit a third 事务 Txn3, which executes Q1 against the qualification
               数据库 with a test-sponsor selected 值 of the substitution parameter [delta] that is not equal to the one used
               in Step 1.
         4.    Verify that Txn2 completes before Txn3, and that the appropriate 行 in the ORDERS, LINEITEM and HIS-
               TORY 表 have been changed.
         Comment: In some implementations Txn2 will not queue behind Txn1. If Txn2 completes prior to Txn1 comple-
         tion, it is not necessary to run Txn3 in 订单 to demonstrate that updates will be processed in a timely manner as
         required by Isolation Tests.

3.5      Durability Requirements
         The SUT must guarantee 持久性: the ability to preserve the effects of committed transactions and ensure 数据库
         一致性 after 恢复 from any one of the failures listed in Clause 3.5.3.

         Comment: No 系统 provides complete 持久性 (i.e., 持久性 under all possible types of failures). The specific
         set of single failures addressed in Clause 3.5.3 is deemed sufficiently significant to justify demonstration of
         持久性 across such failures.
3.5.1    Durable Medium Definition
         A durable medium is a data storage medium that is either:

          a)     An inherently non-volatile medium (e.g., magnetic disk, magnetic tape, optical disk, etc.) or;

          b)     A volatile medium with its own self-contained power supply that will retain and permit the transfer of data,
                 before any data is lost, to an inherently non-volatile medium after the failure of external power.



         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                           Page 76
        A configured and priced Uninterruptible Power Supply (UPS) is not considered external power.

        Comment: A durable medium can fail; this is usually protected against by 复制 on a second durable medium
        (e.g., mirroring) or logging to another durable medium. Memory can be considered a durable medium if it can pre-
        serve data long enough to satisfy the 要求 (b) above, for 示例, if it is accompanied by an Uninterruptible
        Power Supply, and the contents of memory can be transferred to an inherently non-volatile medium during the fail-
        ure. Note that no distinction is made between main memory and memory performing similar permanent or tempo-
        rary data storage in other parts of the 系统 (e.g., disk controller caches).
3.5.2   Committed Property Definition

3.5.2.1 A 事务 is considered committed when the 事务 manager 组件 of the 系统 has either written the
        log or written the data for the committed updates associated with the 事务 to a durable medium.

        Comment 1: Transactions can be committed without the user subsequently receiving notification of that fact, since
        message integrity is not required for TPC-H.

        Comment 2: Although the 订单 of operations in the ACID Transaction is immaterial, the actual return of data can-
        not begin until the commit operation has successfully completed.

3.5.2.2 To facilitate the 执行 of the 持久性 tests the driver must maintain a durable success file that 记录 the
        details of each 事务 which has successfully completed and whose message has been returned to the driver. At
        the time of an induced failure this success file must contain a 记录 of all transactions which have been committed,
        except for transactions whose commit notification message to the driver was interrupted by the failure.

        The 持久性 success file is required only for the 持久性 tests and must contain the following 字段:

            Fields                                                  Datatype Definition

            P_KEY                                                   Identifier ‘Foreign Key’ to P_PARTKEY

            S_KEY                                                   Identifier ‘Foreign Key’ to S_SUPPKEY

            O_KEY                                                   Identifier ‘Foreign Key’ to O_ORDERKEY

            L_KEY                                                   integer

            DELTA                                                   Integer

            DATE_T                                                  日期 and time to second

        Comment: If the driver resides on the SUT, the success file 必须 isolated from the TPC-H 数据库. For exam-
        ple, the success file 必须 written outside of the ACID Transaction, and if the 持久性 of the success file is pro-
        vided by the same data manager as the TPC-H 数据库, it must use a different log file.
3.5.3   Durability Across Single Failures
        The test sponsor is required to guarantee that the test 系统 will preserve the 数据库 and the effects of committed
        updates after 恢复 from any of the failures listed below:
        •            Permanent irrecoverable failure of any single durable medium containing TPC-H 数据库 表 or
                     恢复 log data. The media to be failed is to be chosen at random by the auditor, and cannot be specially
                     prepared.
        Comment: If main memory is used as a durable medium, then it 必须 considered as a potential single point of
        failure. Sample mechanisms to survive single durable medium failures are 数据库 archiving in conjunction with a
        redo (after image) log, and mirrored durable media. If memory is the durable medium and mirroring is the mecha-
        nism used to ensure 持久性, then the mirrored memories 必须 independently powered.
        •            Instantaneous interruption (系统 crash/系统 hang) in processing which requires 系统 re-boot to
                     recover.


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 77
        Comment: This implies abnormal 系统 shutdown, which requires loading of a fresh copy of the operating 系统
        from the boot device. It does not necessarily imply loss of volatile memory. When the 恢复 mechanism relies on
        the pre-failure contents of volatile memory, the means used to avoid the loss of volatile memory (e.g., an Uninter-
        ruptible Power Supply) 必须 included in the 系统 成本 calculation. A sample mechanism to survive an instan-
        taneous interruption in processing is an undo/redo log.
        •        Failure of all or 零件 of memory (loss of contents).
        Comment: This implies that all or 零件 of memory has failed. This 可 be caused by a loss of external power or the
        permanent failure of a memory board.
        •        SUT Power Failure: Loss of all external power to the SUT for an indefinite time period.
        Comment: To demonstrate 持久性 in a cluster during a power failure, the largest subset of the SUT maintained
        by a single UPS 必须 failed. For 示例, if a 系统 has one UPS per node or set of nodes, it is sufficient to fail
        one node or that set of nodes. If there is only one UPS for the entire 系统, then the entire 系统 必须 failed. In
        either case, all UPSs 必须 priced.

        Regardless of UPS 配置, at least one node of each subset of the nodes in the cluster providing a distinct
        function 必须 failed.
3.5.4   Durability Tests
        The intent of these tests is to demonstrate that all transactions whose 输出 messages have been received by the
        driver have in fact been committed in spite of any single failure from the list in Clause 3.5.3 and that all 一致性
        conditions are still met after the 数据库 is recovered.

        For each of the failure types defined in Clause 3.5.3 perform the following steps:
        1.   Verify that the ORDERS, and LINEITEM 表 are initially consistent as defined in Clause 3.3.2.1, based on a
             random sample of at least 10 distinct 值 of O_ORDERKEY.
        2.   Submit ACID transactions from a number of concurrent streams. The number of streams 必须 at least the
             number of the 执行 streams (# 查询 streams + 1 刷新 stream) used in the reported 吞吐量 test. Each
             stream must submit ACID transactions continuously, i.e. without delay between the completion of one
             事务 and the submission of the next. The submission of transactions 可 not be synchronized to any
             actions outside of the stream on which they are submitted. Each 事务 must use 值 of (O_KEY,
             L_KEY, DELTA) randomly generated within the ranges defined in Clause 3.1.6.2. Ensure that all the 值 of
             O_ORDERKEY chosen in Step 1 are used by some 事务 in Step 2. It 必须 demonstrated that
             transactions are in progress at the time of the failure.
        3.   Wait until at least 100 of the ACID transactions from each stream submitted in Step 2 have completed. Cause
             the failure selected from the list in Clause 3.5.3. At the time of the failure, it 必须 demonstrated that:
        •        At least one 事务 is in flight.
        •        All streams are submitting ACID transactions as defined in Step 2.
        Comment: The intent is that the failure is induced while all streams are continuously submitting and executing
        transactions. If the number of in-flight transactions at the point of failure is less than the number of streams, this is
        assumed to be a random consequence of interrupting some streams during the very small interval between commit-
        ting one 事务 and submitting the next.
        4.   Restart the 系统 under test using normal 恢复 procedures.
        5.   Compare the contents of the 持久性 success file and the HISTORY 表 to verify that 记录 in the success
             file for a committed ACID Transaction have a corresponding 记录 in the HISTORY 表 and that no success
             记录 exists for uncommitted transactions. Count the number of entries in the success file and in the HISTORY
             表 and report any difference.
        Comment: This difference can only be due to transactions that were committed on the 系统 under test, but for
        which the data was not written in the success file before the failure.
        6.   Re-verify the 一致性 of the ORDERS, and LINEITEM 表 as defined in Clause 3.3.2.1.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 78
                                4: SCALING AND DATABASE POPULATION

4.1      Database Definition and Scaling

4.1.1    Test Database

4.1.1.1 The test 数据库 is the 数据库 used to execute the load test and the 性能 test (see Clause 5.1.1.4).

4.1.1.2 The test 数据库 必须 scaled as defined in Clause 4.1.3

4.1.1.3 The test 数据库 必须 populated according to Clause 4.2.
4.1.2    Qualification Database

4.1.2.1 A qualification 数据库 必须 created and populated for use in the 查询 validation test described in Clause 2.3.
        The intent is that the functionality exercised by running the validation queries against the qualification 数据库 be
        the same as that exercised against the test 数据库 during the 性能 test. To this end, the qualification data-
        base 必须 identical to the test 数据库 in virtually every regard except size, including but not limited to:
         •        Column definitions;
         •        Method of data generation and loading;
         •        Statistics gathering method;
         •        ACID property 实现;
         •        Type of partitioning (but not degree of partitioning);
         •        Replication
         •        Table type (if there is a choice);
         •        Auxiliary data structures (e.g., indices).
         The qualification 数据库 可 differ from the test 数据库 only if the difference is directly related to the difference
         in sizes. For 示例, if the test 数据库 employs horizontal partitioning (see Clause 1.5.4), then the qualification
         数据库 must also employ horizontal partitioning, though the number of partitions 可 differ in each case. As
         another 示例, the qualification 数据库 could be configured such that it uses a representative sub-set of the
         processors/cores/threads, memory and disks used by the test 数据库 配置. If the qualification 数据库
         配置 differs from the test 数据库 配置 in any way, the differences 必须 disclosed (see Clause
         8.3.7.8).

4.1.2.2 The population of the qualification 数据库 必须 exactly equal to a 规模因子, SF, of 1 (see Clause 4.1.3 for a
        定义 of SF).
4.1.3    Database Scaling Requirements

4.1.3.1 Scale factors used for the test 数据库 必须 chosen from the set of fixed scale factors defined as follows:
                  1, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000
        The 数据库 size is defined with reference to 规模因子 1 (i.e., SF = 1; approximately 1GB as per Clause 4.2.5),
        the minimum required size for a test 数据库. Therefore, the following series of 数据库 sizes corresponds to the
        series of scale factors and 必须 used in the 指标 names QphH@Size and Price-per-kQphH@Size (see Clause
        5.4), as well as in the executive summary statement (see Appendix E):

                  1GB, 10GB, 30GB, 100GB, 300GB, 1000GB, 3000GB, 10000GB, 30000GB, 100000GB

                  Where GB stands for gigabyte, defined to be 2 30 bytes.

         Comment 1: Although the minimum size of the test 数据库 for a valid 性能 test is 1GB (i.e., SF = 1), a
         test 数据库 of 3GB (i.e., SF = 3) is not permitted. This 要求 is intended to encourage comparability of
         results at the low end and to ensure a substantial actual difference in test 数据库 sizes.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 79
         Comment 2: The maximum size of the test 数据库 for a valid 性能 test is currently set at 100000 (i.e., SF
         = 100,000). The TPC recognizes that additional 基准测试 development work is necessary to allow TPC-H to scale
         beyond that limit.

4.1.3.2 Test sponsors must choose the 数据库 size they want to execute against by selecting a size and corresponding scale
        factor from the defined series.

4.1.3.3 The ratio of total data storage to 数据库 size r 必须 computed by dividing the total durable data storage of the
        priced 配置 (expressed in GB) by the size chosen for the test 数据库 as defined in the 规模因子 used for
        the test 数据库. The reported 值 for the ratio v 必须 rounded to the nearest 0.01. That is, v=round(r,2). The
        ratio 必须 included in both the Full Disclosure report and the Executive Summary.

4.2      DBGEN and Database Population

4.2.1    The DBGEN Program

4.2.1.1 The test 数据库 and the qualification 数据库 必须 populated with data that meets the 要求 of Clause
        4.2.2 and Clause 4.2.3. DBGen is a TPC provided 软件 package that 必须 used to produce the data used to
        populate the 数据库..

4.2.1.2 The data generated by DBGen are meant to be compliant with the 规范 as per Clause 4.2.2 and Clause 4.2.3.
        In case of differences between the content of these two clauses and the data generated by DBGen, the 规范
        prevails.

4.2.1.3 The TPC Policies Clause 5.3.1 requires that the version of the 规范 and DBGen must match. It is the test
        sponsor’s responsibility to ensure the correct version of DBGen is used.

4.2.1.4 DBGen has been tested on a variety of platforms. Nonetheless, it is impossible to guarantee that DBGen is
        functionally correct in all aspects or will run correctly on all platforms. It is the Test Sponsor's responsibility to
        ensure the TPC provided 软件 runs in 合规 with the 规范 in their environment(s).

4.2.1.5 If a Test Sponsor must correct an error in DBGen in 订单 to publish a Result, the following steps 必须
        performed:
             a. The error 必须 reported to the TPC administrator, following the method described in 子句 4.2.1.7, no
                later than the time when the Result is submitted.
             b. The error and the modification (i.e. diff of source files) used to correct the error 必须 reported in the
                FDR as described in 子句 8.3.5.5.
             c. The modification used to correct the error 必须 reviewed by a TPC-Certified Auditor as 零件 of the 审计
                process.
        Furthermore any consequences of the modification 可 be used as the basis for a non-合规 challenge.

4.2.2    Definition Of Terms

4.2.2.1 The term random means independently selected and uniformly distributed over the specified range of 值.

4.2.2.2 The term unique within [x] represents any one 值 within a set of x 值 between 1 and x, unique within the
        scope of 行 being populated.

4.2.2.3 The notation random 值 [x .. y] represents a random 值 between x and y inclusively, with a mean of (x+y)/2,
        and with the same number of digits of precision as shown. For 示例, [0.01 .. 100.00] has 10,000 unique 值,
        whereas [1..100] has only 100 unique 值.

4.2.2.4 The notation random string [list_name] represents a string selected at random within the list of strings list_name as
        defined in Clause 4.2.2.13. Each string 必须 selected with equal probability.

4.2.2.5 The notation text appended with digit [text, x] represents a string generated by concatenating the sub-string text,
        the character "# ", and the sub-string representation of the number x.

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 80
4.2.2.6 This 子句 intentionally left blank.

4.2.2.7 The notation random v-string [min, max] represents a string comprised of randomly generated alphanumeric
        characters within a character set of at least 64 symbols. The length of the string is a random 值 between min and
        max inclusive.

4.2.2.8 The term 日期 represents a string of numeric characters separated by hyphens and comprised of a 4 digit year, 2 digit
        month and 2 digit day of the month.

4.2.2.9 The term phone number represents a string of numeric characters separated by hyphens and generated as follows:
        Let i be an 索引 into the list of strings Nations (i.e., ALGERIA is 0, ARGENTINA is 1, etc., see Clause 4.2.3),
        Let country_code be the sub-string representation of the number (i + 10),
        Let local_number1 be random [100 .. 999],
        Let local_number2 be random [100 .. 999],
        Let local_number3 be random [1000 .. 9999],
        The phone number string is obtained by concatenating the following sub-strings:
                  country_code, "-", local_number1, "-", local_number2, "-", local_number3

4.2.2.10 The term text string[min, max] represents a substring of a 300 MB string populated according to the pseudo text
         grammar defined in Clause 4.2.2.14. The length of the substring is a random number between min and max
         inclusive. The substring offset is randomly chosen.

4.2.2.11 This 子句 intentionally left blank.

4.2.2.12 All dates 必须 computed using the following 值:

                  STARTDATE = 1992-01-01               CURRENTDATE = 1995-06-17           ENDDATE = 1998-12-31

4.2.2.13 The following list of strings 必须 used to populate the 数据库:
         List name:Types

         Each string is generated by the concatenation of a variable length syllable selected at random from each of the three
         following lists and separated by a single space (for a total of 150 combinations).


          Syllable 1                      Syllable 2                     Syllable 3

          STANDARD                        ANODIZED                       TIN

          SMALL                           BURNISHED                      NICKEL

          MEDIUM                          PLATED                         BRASS

          LARGE                           POLISHED                       STEEL

          ECONOMY                         BRUSHED                        COPPER

          PROMO

         List name: Containers
         Each string is generated by the concatenation of a variable length syllable selected at random from each of the two
         following lists and separated by a single space (for a total of 40 combinations).



          Syllable 1      Syllable 2

          SM              CASE


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 81
 LG             BOX

 MED            BAG

 JUMBO          JAR

 WRAP           PKG

                PACK

                CAN

                DRUM

List name: Segments

 AUTOMOBILE             BUILDING                FURNITURE          MACHINERY

 HOUSEHOLD

List name: Priorities


 1-URGENT               2-HIGH                  3-MEDIUM           4-NOT SPECIFIED

 5-LOW


List name: Instructions

 DELIVER IN PERSON               COLLECT COD         NONE                TAKE BACK RETURN

List name: Modes



 REG AIR                         AIR                 RAIL                SHIP

 TRUCK                           MAIL                FOB

List name:Nouns

 foxes                           ideas               theodolites         pinto beans

 instructions                    dependencies        excuses             platelets

 asymptotes                      courts              dolphins            multipliers

 sauternes                       warthogs            frets               dinos

 attainments                     somas               Tiresias'           patterns

 forges                          braids              hockey players      frays

 warhorses                       dugouts             notornis            epitaphs


TPC BenchmarkTM H Standard Specification Revision 3.0.1                                     Page 82
 pearls                       tithes                waters      orbits

 gifts                        sheaves               depths      sentiments

 decoys                       realms                pains       grouches

 escapades

List name: Verbs


 sleep                        wake                  are         cajole

 haggle                       nag                   use         boost

 affix                        detect                integrate   maintain

 nod                          was                   lose        sublate

 solve                        thrash                promise     engage

 hinder                       print                 x-ray       breach

 eat                          grow                  impress     mold

 poach                        serve                 run         dazzle

 snooze                       doze                  unwind      kindle

 play                         hang                  believe     doubt

List name: Adjectives

 furious                      sly                   careful     blithe

 quick                        fluffy                slow        quiet

 ruthless                     thin                  close       dogged

 daring                       brave                 stealthy    permanent

 enticing                     idle                  busy        regular

 final                        ironic                even        bold

 silent

List name: Adverbs

 sometimes                    always                never       furiously

 slyly                        carefully             blithely    quickly

 fluffily                     slowly                quietly     ruthlessly

 thinly                       closely               doggedly    daringly



TPC BenchmarkTM H Standard Specification Revision 3.0.1                      Page 83
          bravely                              stealthily        permanently         enticingly

          idly                                 busily            regularly           finally

          ironically                           evenly            boldly              silently

        List name: Prepositions

          about                                above             according to        across

          after                                against           along               alongside of

          among                                around            at                  atop

          before                               behind            beneath             beside

          besides                              between           beyond              by

          despite                              during            except              for

          from                                 in place of       inside              instead of

          into                                 near              of                  on

          outside                              over              past                since

          through                              throughout        to                  toward

          under                                until             up                  upon

          without                              with              within

        List name: Auxiliaries

          do                                   可               might               应

          will                                 would             can                 could

          应                               ought to          must                will have to

          应 have to                        could have to     应 have to      must have to

          need to                              try to

        List name: Terminators

          .                       ;                       :           ?

          !                       --



4.2.2.14 Pseudo text used in the data population (see Clause 4.2.2.10) must conform to the following grammar:

                    text:<sentence>
                          |<text> <sentence>
                          ;

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                 Page 84
                 sentence:<noun phrase> <verb phrase> <terminator>
                      |<noun phrase> <verb phrase> <prepositional phrase> <terminator>
                      |<noun phrase> <verb phrase> <noun phrase> <terminator>
                      |<noun phrase> <prepositional phrase> <verb phrase>
                      <noun phrase> <terminator>
                      |<noun phrase> <prepositional phrase> <verb phrase>
                      <prepositional phrase> <terminator>
                      ;

                 noun phrase:<noun>
                      |<adjective> <noun>
                      |<adjective>, <adjective> <noun>
                      |<adverb> <adjective> <noun>
                      ;

                 verb phrase:<verb>
                      |<auxiliary> <verb>
                      |<verb> <adverb>
                      |<auxiliary> <verb> <adverb>
                      ;

                 prepositional phrase: <preposition> the <noun phrase>
                      ;

                 noun:selected from Nouns (as defined in Clause 4.2.2.13)

                 verb: selected from Verbs (as defined in Clause 4.2.2.13)

                 adjective: selected from Adjectives (as defined in Clause 4.2.2.13)

                 adverb: selected from Adverbs (as defined in Clause 4.2.2.13)

                 preposition: selected from Prepositions (as defined in Clause 4.2.2.13)

                 terminator: selected from Terminators (as defined in Clause 4.2.2.13)

                 auxiliary: selected from Auxiliary (as defined in Clause 4.2.2.13)

4.2.2.15 The grammar defined in Clause 4.2.2.14 relies on the weighted, non-uniform distribution of its constituent distribu-
         tions (nouns, verbs, auxiliaries, etc.).
4.2.3   Test Database Data Generation
        The data generated by DBGEN (see Clause 4.2.1) 必须 used to populate the 数据库 as follows (where SF is the
        规模因子, see Clause 4.1.3.1):
        •        SF * 10,000 行 in the SUPPLIER 表 with:
                 S_SUPPKEY unique within [SF * 10,000].
                 S_NAME text appended with minimum 9 digits with leading zeros ["Supplie#r", S_SUPPKEY].
                 S_ADDRESS random v-string[10,40].
                 S_NATIONKEY random 值 [0 .. 24].
                 S_PHONE generated according to Clause 4.2.2.9.
                 S_ACCTBAL random 值 [-999.99 .. 9,999.99].
                 S_COMMENT text string [25,100].
                       SF * 5 行 are randomly selected to hold at a random position a string matching "Cus-
                       tomer%Complaints". Another SF * 5 行 are randomly selected to hold at a random position a
                       string matching "Customer%Recommends", where % is a wildcard that denotes zero or more
                       characters.
        •        SF * 200,000 行 in the PART 表 with:


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 85
        P_PARTKEY unique within [SF * 200,000].
        P_NAME generated by concatenating five unique randomly selected strings from the following list,
        separated by a single space:
                 {"almond", "antique", "aquamarine", "azure", "beige", "bisque", "black", "blanched", "blue",
                 "blush", "brown", "burlywood", "burnished", "chartreuse", "chiffon", "chocolate", "coral",
                 "cornflower", "cornsilk", "cream", "cyan", "dark", "deep", "dim", "dodger", "drab", "firebrick",
                 "floral", "forest", "frosted", "gainsboro", "ghost", "goldenrod", "green", "grey", "honeydew",
                 "hot", "indian", "ivory", "khaki", "lace", "lavender", "lawn", "lemon", "light", "lime", "linen",
                 "magenta", "maroon", "medium", "metallic", "midnight", "mint", "misty", "moccasin", "navajo",
                 "navy", "olive", "orange", "orchid", "pale", "papaya", "peach", "peru", "pink", "plum", "powder",
                 "puff", "purple", "red", "rose", "rosy", "royal", "saddle", "salmon", "sandy", "seashell", "sienna",
                 "sky", "slate", "smoke", "snow", "spring", "steel", "tan", "thistle", "tomato", "turquoise", "violet",
                 "wheat", "white", "yellow"}.
        P_MFGR text appended with digit ["Manufacturer#",M], where M = random 值 [1,5].
        P_BRAND text appended with digits ["Brand#",MN], where N = random 值 [1,5] and M is defined
                 while generating P_MFGR.
        P_TYPE random string [Types].
        P_SIZE random 值 [1 .. 50].
        P_CONTAINER random string [Containers].
        P_RETAILPRICE = (90000 + ((P_PARTKEY/10) modulo 20001 ) + 100 * (P_PARTKEY modulo
                 1000))/100
        P_COMMENT text string [5,22].
        For each 行 in the PART 表, four 行 in PartSupp 表 with:
        PS_PARTKEY = P_PARTKEY.
        PS_SUPPKEY = (ps_partkey + (i * (( S/4 ) + (int)(ps_partkey-1 )/S)))) modulo S + 1 where i is the ith
                 供应商 within [0 .. 3] and S = SF * 10,000.
        PS_AVAILQTY random 值 [1 .. 9,999].
        PS_SUPPLYCOST random 值 [1.00 .. 1,000.00].
        PS_COMMENT text string [49,198].
•       SF * 150,000 行 in CUSTOMER 表 with:
        C_CUSTKEY unique within [SF * 150,000].
        C_NAME text appended with minimum 9 digits with leading zeros ["Customer#", C_CUSTKEY].
        C_ADDRESS random v-string [10,40].
        C_NATIONKEY random 值 [0 .. 24].
        C_PHONE generated according to Clause 4.2.2.9.
        C_ACCTBAL random 值 [-999.99 .. 9,999.99].
        C_MKTSEGMENT random string [Segments].
        C_COMMENT text string [29,116].
•       For each 行 in the CUSTOMER 表, ten 行 in the ORDERS 表 with:
        O_ORDERKEY unique within [SF * 1,500,000 * 4].

Comment: The ORDERS and LINEITEM 表 are sparsely populated by generating a key 值 that causes the
first 8 keys of each 32 to be populated, yielding a 25% use of the key range. Test sponsors must not take advantage
of this aspect of the 基准测试. For 示例, horizontally partitioning the test 数据库 onto different devices in
订单 to place unused areas onto separate peripherals is prohibited.

        O_CUSTKEY = random 值 [1 .. (SF * 150,000)].
              The generation of this random 值 必须 such that O_CUSTKEY modulo 3 is not zero.

Comment: Orders are not present for all customers. Every third 客户 (in C_CUSTKEY 订单) is not assigned
any 订单.
        O_ORDERSTATUS set to the following 值:
                 "F" if all lineitems of this 订单 have L_LINESTATUS set to "F".
                 "O" if all lineitems of this 订单 have L_LINESTATUS set to "O".
        "P" otherwise.

TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 86
        O_TOTALPRICE computed as:
              sum (L_EXTENDEDPRICE * (1+L_TAX) * (1-L_DISCOUNT)) for all LINEITEM of this 订单.
        O_ORDERDATE uniformly distributed between STARTDATE and (ENDDATE - 151 days).
        O_ORDERPRIORITY random string [Priorities].
        O_CLERK text appended with minimum 9 digits with leading zeros ["Clerk#", C] where C = random 值
              [000000001 .. (SF * 1000)].
        O_SHIPPRIORITY set to 0.
        O_COMMENT text string [19,78].
•       For each 行 in the ORDERS 表, a random number of 行 within [1 .. 7] in the LINEITEM 表 with:
        L_ORDERKEY = O_ORDERKEY.
        L_PARTKEY random 值 [1 .. (SF * 200,000)].
        L_SUPPKEY = (L_PARTKEY + (i * (( S/4 ) + (int)(L_partkey-1 )/S)))) modulo S + 1
               where i is the corresponding 供应商 within [0 .. 3] and S = SF * 10,000.
        L_LINENUMBER unique within [7].
        L_QUANTITY random 值 [1 .. 50].
        L_EXTENDEDPRICE = L_QUANTITY * P_RETAILPRICE
               Where P_RETAILPRICE is from the 零件 with P_PARTKEY = L_PARTKEY.
        L_DISCOUNT random 值 [0.00 .. 0.10].
        L_TAX random 值 [0.00 .. 0.08].
        L_RETURNFLAG set to a 值 selected as follows:
               If L_RECEIPTDATE <= CURRENTDATE
               then either "R" or "A" is selected at random
               else "N" is selected.
        L_LINESTATUS set the following 值:
               "O" if L_SHIPDATE > CURRENTDATE
               "F" otherwise.
        L_SHIPDATE = O_ORDERDATE + random 值 [1 .. 121].
        L_COMMITDATE = O_ORDERDATE + random 值 [30 .. 90].
        L_RECEIPTDATE = L_SHIPDATE + random 值 [1 .. 30].
        L_SHIPINSTRUCT random string [Instructions].
        L_SHIPMODE random string [Modes].
        L_COMMENT text string [10,43].
•       25 行 in the NATION 表 with:
        N_NATIONKEY unique 值 between 0 and 24.
        N_NAME string from the following series of (N_NATIONKEY, N_NAME, N_REGIONKEY).
              (0, ALGERIA, 0);(1, ARGENTINA, 1);(2, BRAZIL, 1);
              (3, CANADA, 1);(4, EGYPT, 4);(5, ETHIOPIA, 0);
              (6, FRANCE, 3);(7, GERMANY, 3);(8, INDIA, 2);
              (9, INDONESIA, 2);(10, IRAN, 4);(11, IRAQ, 4);
              (12, JAPAN, 2);(13, JORDAN, 4);(14, KENYA, 0);
              (15, MOROCCO, 0);(16, MOZAMBIQUE, 0);(17, PERU, 1);
              (18, CHINA, 2);(19, ROMANIA, 3);(20, SAUDI ARABIA, 4);
              (21, VIETNAM, 2);(22, RUSSIA, 3);(23, UNITED KINGDOM, 3);
              (24, UNITED STATES, 1)
        N_REGIONKEY is taken from the series above.
        N_COMMENT text string [31,114].
•       5 行 in the REGION 表 with:
        R_REGIONKEY unique 值 between 0 and 4.
        R_NAME string from the following series of (R_REGIONKEY, R_NAME).
              (0, AFRICA);(1, AMERICA);           (2, ASIA);
              (3, EUROPE);(4, MIDDLE EAST)
        R_COMMENT text string [31,115].



TPC BenchmarkTM H Standard Specification Revision 3.0.1                                               Page 87
4.2.4    Refresh Function Data Generation

4.2.4.1 The test 数据库 is initially populated with 75% sparse ‘Primary Keys’ for the ORDERS and LINEITEM 表
        (see Clause 4.2.3) where only the first eight key 值 of each group of 32 keys are used. Subsequently, the 刷新
        function RF1 uses the 'holes' in the key ranges for inserting new 行.

4.2.4.2 DBGEN generates 刷新 data sets for the 刷新 functions such that:
         •           For the first through the 1,000th 执行 of RF1 data sets are generated for inserting 0.1% new 行 with
                     a ‘Primary Keys’ within the second 8 key 值 of each group of 32 keys;
         •           For the first through the 1,000th 执行 of RF2 data sets are generated for deleting 0.1% existing 行
                     with a ‘Primary Keys’ within the original first 8 key 值 of each group of 32 keys.
         Comment: As a 结果, after 1,000 executions of RF1/RF2 pairs the test 数据库 is still populated with 75% sparse
         ‘Primary Keys’ , but the second 8 key 值 of each group of 32 keys are now used.

4.2.4.3 The 刷新函数 data set generation scheme can be repeated until 4000 RF1/RF2 pairs have been executed, at
        which point the population of the test 数据库 is once again in its initial state.
4.2.5    Database Size

4.2.5.1 Table 3: Estimated Database Size shows the test 数据库 size for a 规模因子, SF, of 1.
         Table 3: Estimated Database Size



             Table Name                    Cardinality       Length (in bytes)      Typical2 Table
                                           (in 行)         of Typical2 Row        Size (in MB)

             SUPPLIER                      10,000            159                    2

             PART                          200,000           155                    30

             PARTSUPP                      800,000           144                    110

             CUSTOMER                      150,000           179                    26

             ORDERS                        1,500,000         104                    149

             LINEITEM3                     6,001,215         112                    641

             NATION1                       25                128                    <1

             REGION1                       5                 124                    <1

             Total                         8,661,245                                956




         1
             Fixed cardinality: does not scale with SF.
         2
             Typical lengths and sizes given here are examples, not 要求, of what could 结果 from an
                   实现 (sizes do not include storage/access overheads).
         3
             The cardinality of the LINEITEM 表 is not a strict multiple of SF since the number of lineitems in an
                    订单 is chosen at random with an average of four (see Clause 4.2.5.2).




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 88
        Comment : 1 MB is defined to be 220 bytes. Data types are sized as follows: 4-byte integers, 8-byte decimals, 4-byte
        dates.

4.2.5.2 Table 4: LINEITEM Cardinality shows the cardinality of the LINEITEM 表 at all authorized scale factors.
        Table 4: LINEITEM Cardinality

          Scale Factor (SF)                          Cardinality of LINEITEM Table

          1                                          6001215

          10                                         59986052

          30                                         179998372

          100                                        600037902

          300                                        1799989091

          1000                                       5999989709

          3000                                       18000048306

          10000                                      59999994267

          30000                                      179999978268

          100000                                     599999969200



4.3     Database Load Time

4.3.1   The process of building the test 数据库 is known as 数据库 load. Database load consists of timed and untimed
        components. However, all components 必须 fully disclosed (see Clause 8.3.5.6).
4.3.2   The total 耗时 to prepare the test 数据库 for the 执行 of the 性能 test is called the 数据库
        load time, and 必须 reported. This includes all of the 耗时 to create the 表 defined in Clause 1.4, load
        data, create indices, define and validate constraints, gather statistics for the test 数据库, configure the 系统 under
        test as it will be during the 性能 test, and ensure that the test 数据库 meets the ACID 要求
        including syncing loaded data on devices used to 实现 data redundancy mechanisms and the taking of a
        backup of the 数据库, when necessary.
4.3.3   The population of the test 数据库, as defined in Clause 4.2, consists of two logical phases:
        1.     Generation Phase: the process of using DBGen to generate 记录 in a format for use by the DBMS load
               facility. The generated 记录 可 be passed through a communication channel, stored in memory, or stored in
               files on storage media.
        2.     Loading Phase: the process of loading the generated 记录 into the 数据库 表.
        Generation and loading of the 记录 can be accomplished in one of two ways:
        1.     Load from stored 记录: The 记录 generated by DBGen are first stored (in memory or on storage media).
               The stored 记录 可 optionally be sorted, partitioned or relocated to the SUT. After 表 creation on the
               SUT, the stored 记录 are loaded into the 数据库 表. In this case only the loading phase contributes to
               the 数据库 load time.
        2.     In-line load: The 记录 generated by DBGen are passed through a communication channel and directly
               loaded into the 数据库 表. In this case generation phase and loading phase occur concurrently and both
               contribute to the 数据库 load time.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 89
4.3.4   The 数据库 load time 必须 measured on the 系统 under test (SUT).
4.3.5   The timing of the 数据库 load time begins with the creation of the 表 defined in Clause 1.4.
4.3.6   There are five classes of operations which 可 be excluded from 数据库 load time:
        •        Any operation that does not affect the state of the DBMS (e.g., generation of 记录 by DBGen, storage of
                 generated 记录, relocation of stored 记录 to the SUT, sorting or partitioning of stored 记录,
                 operating-系统-level disk partitioning or 配置);
        •        Any modification to the state of the DBMS that is not specific to the TPC-H 工作负载 (e.g. logical
                 tablespace creation or 数据库 block formatting);
        •        The time required to install or remove physical resources (e.g. processors/cores/threads, memory or disk
                 drives) on the SUT that are not priced (see Clause 4.3.9);
        •        An optional backup of the test 数据库 performed at the test sponsor’s discretion. However, if a backup is
                 required to ensure that the ACID properties can be met it 必须 included in the load time;
        •        Operations that create devices used to 实现 data redundancy mechanisms.
        Comment: The time required to perform any necessary 软件 reconfiguration (such as DBMS or operating
        系统 parameters) 必须 included in the 数据库 load time.
4.3.7   The timing of the 数据库 load ends when the 数据库 is fully populated and the SUT is configured as it will be
        during the 性能 test.

        Comment 1: The intent of this Clause is that when the timing ends the 系统 under test be capable of executing the
        性能 test without any further change. The 数据库 load 可 be decomposed into several phases. Database
        load time is the sum of the elapsed times of all phases during which activity other than that detailed in Clause 4.3.6
        occurred on the SUT. The timing of a load phase completes only when any change to the test 数据库 has been
        written to durable media (see Clause 3.5.1).

        Comment 2: Since the time of the end of the 数据库 load is used to seed the random number generator for the
        substitution parameter, that time cannot be delayed in any way that would make it predictable to the test sponsor.
4.3.8   The resources used to generate DBGen 记录, sort or partition the 记录, store the 记录 or relocate the 记录
        to the SUT 可 optionally be distinct from those used to run the actual 基准测试. For 示例:
        •        For load from stored 记录, a separate 系统 or a distinct storage subsystem 可 be used to generate,
                 store, sort, partition or relocate the DBGen 记录 to be delivered to the DBMS load facility.
        •        Fo rin-line load, separate and distinct processing elements 可 be used to generate the DBGen 记录
                 passed to the DBMS load facility.
4.3.9   Resources used only in the generation phase of the population of the test 数据库 必须 treated as follows:

        For load from stored 记录,
        •        Any processing element (e.g., processor/core/thread or memory) used exclusively to generate and store,
                 sort, or partition DBGen 记录 or relocate the 记录 to the SUT prior to the loading phase 应 not be
                 included in the total priced 配置 (see Clause 7.0) and 必须 physically removed from or made
                 inaccessible to the SUT prior to the start of the loading phase;
        •        Any storage facility (e.g., disk drive, tape drive or peripheral controller) used exclusively to generate and
                 deliver DBGen 记录 to the SUT during the loading phase 应 not be included in the total priced
                 配置. The test sponsor must demonstrate to the satisfaction of the auditor that this facility is not
                 being used in the 性能 test.
        For in-line load,
        •        Any processing element (e.g., processor/core/thread or memory) or storage facility (e.g., disk drive, tape
                 drive or peripheral controller) used exclusively to generate and deliver DBGen 记录 to the SUT during
                 the loading phase 应 not be included in the total priced 配置 and 必须 physically removed
                 from or made inaccessible to the SUT prior to the start of the 性能 test.
        Comment: The intent is to isolate the 成本 of resources required to generate 记录 from those required to load
        记录 into the 数据库 表.
        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 90
4.3.10   An 实现 可 require additional programs to transfer DBGen 记录 into the 数据库 表 (for either
         load from stored 记录 or in-line load). If non-commercial programs are used for this purpose, their source code
         必须 disclosed. If commercially available programs are used for this purpose, their invocation and 配置
         必须 disclosed. Whether or not the 软件 is commercially available, use of the 软件's functionality's must
         be limited to:
         1.   Storing, sorting, or partitioning of the 记录 generated by DBGen ;
         2.   Delivery of the 记录 generated by DBGen to the DBMS load facility.
4.3.11   The 数据库 load 必须 implemented using commercially available utilities (invoked at the command level or
         through an API) or an SQL programming interface (such as embedded SQL or ODBC).




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 91
                       5: PERFORMANCE METRICS AND EXECUTION RULES

5.1      Definition of Terms

5.1.1    Components of the Benchmark

5.1.1.1 The 基准测试 is defined as the 执行 of the load test followed by the 性能 test.

5.1.1.2 The load test begins with the creation of the 数据库 表 and includes all activity required to bring the 系统
        under test to the 配置 that immediately precedes the beginning of the 性能 test (see Clause 5.1.1.3).
        The load test 可 not include the 执行 of any of the queries in the 性能 test (see Clause 5.1.2.1) or any
        similar 查询.

5.1.1.3 The 性能 test consists of two runs.

5.1.1.4 A run consists of one 执行 of the Power test described in Clause 5.3.3 followed by one 执行 of the
        Throughput test described in Clause 5.3.4.

5.1.1.5 Run 1 is the first run following the load test (see Clause 5.3.1.4). Run 2 is the run following Run 1.

5.1.1.6 A failed run is defined as a run that did not complete successfully due to unforeseen 系统 failures.
5.1.2    Components of a Run

5.1.2.1 A 查询 is defined as any one of the 22 TPC-H queries specified in Clause 2: .
         •        The symbol "Qi ", with i in lowercase and from 1 to 22, represents a given 查询.

5.1.2.2 A 查询 set is defined as the sequential 执行 of each and every one of the queries.

5.1.2.3 A 查询 stream is defined as the sequential 执行 of a single 查询 set submitted by a single emulated user.
         •        The symbol "S", in uppercase, is used to represent the number of 查询 streams used during the 吞吐量
                  test;
         •        The symbol "s", in lowercase and from 1 to S, is used to represent a given 查询 stream.

5.1.2.4 A 刷新 stream is defined as the sequential 执行 of an integral number of pairs of 刷新 functions submit-
        ted from within a batch program.

5.1.2.5 A pair of 刷新 functions is defined as one of each of the two TPC-H 刷新 functions specified in Clause 2: .
         •        The symbol "RFj ", with j in lowercase and from 1 to 2, represents a given 刷新函数.
         A session is defined as the process context capable of supporting the 执行 of either a 查询 stream or a 刷新
         stream.

5.2      Configuration Rules

5.2.1    The mechanism used to submit queries and 刷新 functions to the 系统 under test (SUT) and measure their exe-
         cution time is called a driver. The driver is a logical entity that can be implemented using one or more physical pro-
         grams, processes, or 系统 (see Clause 6.3).
5.2.2    The communication between the driver and the SUT 必须 limited to one session per 查询 stream or per 刷新
         stream. These sessions are prohibited from communicating with one another except for the purpose of scheduling
         刷新 functions (see Clause 5.3.7.8).
5.2.3    All sessions supporting the 执行 of a 查询 stream 必须 initialized in exactly the same way. The initializa-
         tion of the session supporting the 执行 of the 刷新 stream 可 be different than that of the 查询 streams. All
         session initialization parameters, settings and commands 必须 disclosed.

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 92
        Comment 1: The attributes of the session used in the 查询 stream(s) (see Clause 5.1.2.3) 必须 the same as the
        attributes of the session used by the ACID Query (see Clause 3.1.6.3). Similarly, the attributes of the session used in
        the 刷新 stream (see Clause 5.1.2.4) 必须 the same as the attributes of the session used by the ACID Transac-
        tion (see Clause 3.1.6.3)

        Comment 2: The intent of this Clause is to provide the information needed to precisely recreate the 执行 envi-
        ronment of any given stream prior to the submission of the first 查询 or 刷新函数.
5.2.4   The driver submits each TPC-H 查询 for 执行 by the SUT via the session associated with the corresponding
        查询 stream.
5.2.5   In the case of the two 刷新 functions (RF1 and RF2), the driver is only required to submit the commands neces-
        sary to cause the 执行 of each 刷新函数.
5.2.6   The driver's submittal to the SUT of the queries in the 性能 test (see Clause 5.1.2.1) is constrained by the
        following restrictions:
        •        It must comply with the 查询 合规 要求 of Clause 2.2;
        •        No 零件 of the interaction between the driver and the SUT can have the purpose of indicating to the DBMS
                 or operating 系统 an 执行 strategy or 优先级 that is time dependent or 查询 specific;
        Comment: Automatic 优先级 adjustment performed by the operating 系统 is not prohibited, but specifying a
        varying 优先级 to the operating 系统 on a 查询 by 查询 basis is prohibited.
        •        The settings of the SUT's components, such as DBMS (including 表 and tablespaces) and operating sys-
                 tem, are not to be modified on a 查询 by 查询 basis. These parameters have to be set once before any
                 查询 or 刷新函数 is run and left in that setting for the duration of the 性能 test.
5.2.7   The 配置 and initialization of the SUT, the 数据库, or the session, including any relevant parameter,
        switch or option settings, 必须 based only on externally documented capabilities of the 系统 that can be rea-
        sonably interpreted as useful for an ad-hoc decision support 工作负载. This 工作负载 is characterized by:
        •        Sequential scans of large amounts of data;
        •        Aggregation of large amounts of data;
        •        Multi-表 joins;
        •        Possibly extensive sorting.
        While the 配置 and initialization can reflect the general nature of this expected 工作负载, it 应 not take
        special advantage of the limited functions actually exercised by the 基准测试. The queries actually chosen in the
        基准测试 are merely examples of the types of queries that might be used in such an environment, not necessarily
        the actual user queries. Due to this limit in the number and scope of the queries and test environment, TPC-H has
        chosen to restrict the use of some 数据库 technologies (see Clause 1.5 ). In general, the effect of the 配置
        on 基准测试 性能 应 be representative of its expected effect on the 性能 of the class of
        applications modeled by the 基准测试.

        Furthermore, the features, switches or parameter settings that comprise the 配置 of the operating 系统,
        the DBMS or the session 必须 such that it would be reasonable to expect a 数据库 administrator with the fol-
        lowing characteristics be able to decide to use them:
        •        Knowledge of the general characteristics of the 工作负载 as defined above;
        •        Knowledge of the logical and physical 数据库 layout;
        •        Access to operating 系统 and 数据库 documentation;
        •        No knowledge of product internals beyond what is externally documented externally.
        Each feature, switch or parameter setting used in the 配置 and initialization of the operating 系统, the
        DBMS or the session must meet the following criteria:
        •        It 应 remain in effect without change throughout the 性能 test;
        •        It 应 not make reference to specific 表, indices or queries for the purpose of providing hints to the
                 查询 优化器.
        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 93
5.2.8    The gathering of statistics is 零件 of the 数据库 load (see Clause 4.3) but it also serves as an important configura-
         tion vehicle, particularly for the 查询 优化器. In 订单 to satisfy the 要求 of Clause 5.2.7, it is desirable
         to collect the same quality of statistics for every 列 of every 表. However, in 订单 to reduce processing
         要求, it is permissible to segment 列 into distinct classes and base the level of statistics collection for a
         particular 列 on class membership. Class definitions must rely solely on 模式-related attributes of a 列
         and 必须 applied consistently across all 表. For 示例:
         •        Membership in an 索引;
         •        Leading or other position in an 索引;
         •        Use in a 约束 (including a 主键 or 外键 constraints).
         Statistics that operate in sets, such as distribution statistics, 应 employ a fixed set appropriate to the 规模因子
         used. Knowledge of the cardinality, 值 or distribution of a non-key 列 as specified in Clause 4: cannot be
         used to tailor statistics gathering.
5.2.9    Special 规则 apply to the use of so-called profile-directed 优化 (PDO), in which binary executables are
         reordered or otherwise optimized to best suit the needs of a particular 工作负载. These 规则 do not apply to the rou-
         tine use of PDO by a 数据库 vendor in the course of building commercially available and supported 数据库
         products; such use is not restricted. Rather, the 规则 apply to the use of PDO by a test sponsor to optimize executa-
         bles of a 数据库 product for a particular 工作负载. Such 优化 is permissible if all of the following condi-
         tions are satisfied:
         1.   The use of PDO or similar procedures by the test sponsor 必须 disclosed.
         2.   The procedure and any scripts used to perform the 优化 必须 disclosed.
         3.   The procedure used by the test sponsor could reasonably be used by a 客户 on a shipped 数据库 execut-
              able.
         4.   The optimized 数据库 executables resulting from the application of the procedure 必须 supported by the
              数据库 软件 vendor.
         5.   The 工作负载 used to drive the 优化 is as described in Clause 5.2.10.
         6.   The same set of DBMS executables 必须 used for all phases of the 基准测试.
5.2.10   If profile-directed 优化 is used under the circumstances described in Clause 5.2.9, the 工作负载 used to
         drive it 必须 the (possibly repeated) 执行 of Queries 1,2,4 and 5 in any 订单, against a TPC-H 数据库 of
         any desired Scale Factor with default substitution parameters applied.

5.3      Execution Rules

5.3.1    General Rules

5.3.1.1 The driver must submit queries through one or more sessions on the SUT. Each session corresponds to one, and only
        one, 查询 stream on the SUT.

5.3.1.2 Parallel activity within the SUT directed toward the 执行 of a single 查询 (i.e., intra-查询 parallelism) is not
        restricted.

5.3.1.3 To measure the 性能 of a 系统 using the TPC Benchmark™ H, the test sponsor will execute runs com-
        posed of:
         •        A power test, to measure the raw 查询 执行 power of the 系统 when connected with a single active
                  user. In this test, a single pair of 刷新 functions are executed exclusively by a separate 刷新 stream and
                  scheduled before and after the 执行 of the queries (see Clause 5.3.3);
         •        A 吞吐量 test, to measure the ability of the 系统 to process the most queries in the least amount of
                  time. In this test, several pairs of 刷新 functions are executed exclusively by a separate 刷新 stream
                  and scheduled as defined by the test sponsor.
         Comment: The 吞吐量 test is where test sponsors can demonstrate the 性能 of their 系统 against a
         multi-user 工作负载.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                           Page 94
5.3.1.4 The 性能 test follows the load test. However, any 系统 activity that takes place between the completion of
        the load test (see Clause 5.1.1.2) and the beginning of the 性能 test is limited to that which is not likely to
        improve the results of the subsequent 性能 test. All such activity 必须 disclosed (see Clause 8.3.8.1).
        Examples of acceptable activity include but are not limited to:
         •        Execution of scripts or queries requested by the auditor;
         •        Processing or archiving of files or timing data gathered during the load test;
         •        Configuration of 性能 monitoring tools;
         •        Execution of simple queries to verify that the 数据库 is correctly loaded;
         •        Taking 数据库 backups (if not needed to meet the ACID 要求);
         •        Rebooting the SUT or restarting the RDBMS.

5.3.1.5 The power test and the 吞吐量 test must both be executed under the same conditions, using the same 硬件
        and 软件 配置 and the same data manager and operating 系统 parameters. All such parameters must
        be reported.
        Comment: The intent of this Clause is to require that both tests (i.e., the power and 吞吐量 tests) be run in iden-
        tical conditions except for the number of 查询 streams and the scheduling of the 刷新 functions within the 刷新
        stream.

5.3.1.6 For each 查询, at least one atomic 事务 必须 started and completed.
        Comment: The intent of this Clause is to specifically prohibit the 执行 of an entire 查询 stream as a single
        事务.

5.3.1.7 Each 刷新函数 must consist of at least one atomic 事务. However, logically consistent portions of the
        刷新 functions 可 be implemented as separate transactions as defined in Clause 2.5.
        Comment: This intent of this Clause is to specifically prohibit the 执行 of multiple 刷新 functions as a single
        事务. The splitting of each 刷新函数 into multiple transactions is permitted to encourage "trickle"
        updates performed concurrently with one or more 查询 streams in the 吞吐量 test.
5.3.2    Run Sequencing
         The 性能 test consists of two runs. If Run 1 is a failed run (see Clause 5.1.1.6) the 基准测试 必须
         restarted with a new load test. If Run 2 is a failed run, it 可 be restarted without a reload. The reported perfor-
         mance 指标 必须 for the run with the lower TPC-H Composite Query-Per-Hour Performance Metric. The same
         set of seed 值 可 be used in the consecutive runs.

         The TPC-H metrics reported for a given 系统 must represent a conservative evaluation of the 系统’s level of
         性能. Therefore, the reported 性能 metrics 必须 for the run with the lower Composite Query-per-
         Hour 指标
5.3.3    Power Test

5.3.3.1 The power test 必须 driven by queries submitted by the driver through a single session on the SUT. The session
        executes queries one after another. This test is used to measure the raw 查询 执行 power of the SUT with a
        single 查询 stream. The power test 必须 executed in parallel with a single 刷新 stream (see Clause 5.1.2.4).

5.3.3.2 The power test must follow these steps in 订单:
         1.   The 刷新函数 RF1 is executed by the 刷新 stream.
         2.   The full 查询 set is executed once by the 查询 stream.
         3.   The 刷新函数 RF2 is executed by the 刷新 stream.

5.3.3.3 The timing intervals (see Clause 5.3.7) for each 查询 and for both 刷新 functions are collected and reported.
5.3.4    Throughput Test
         Table 11: Minimum Required Stream Count


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 95
                                                    SF             S(Streams)

                                             1                 2

                                             10                3

                                             30                4

                                             100               5

                                             300               6

                                             1000              7

                                             3000              8

                                             10000             9

                                             30000             10

                                             100000            11


5.3.4.1 The 吞吐量 test 必须 driven by queries submitted by the driver through two or more sessions on the SUT.
        There 必须 one session per 查询 stream on the SUT and each stream must execute queries serially (i.e., one after
        another). The 值 of S, the minimum number of 查询 streams, is given in Table 11. The 吞吐量 test 必须
        executed in parallel with a single 刷新 stream (see Clause 5.1.2.4).

        The 吞吐量 test must immediately follow one, and only one, power test. No changes to the 配置 of the
        SUT can be made between the power test and the 吞吐量 test (see 5.2.7). Any operations performed on the SUT
        between the power and 吞吐量 tests must have the following characteristics:
        •        They are related to data collection required for the 基准测试 or requested by the auditor
        •        They are not likely to improve the 性能 of the 吞吐量 test

5.3.4.2 When measuring and reporting a 吞吐量 test, the number, S, of 查询 streams must remain constant during the
        whole measurement interval. When results are reported with S 查询 streams, these S streams 必须 the only ones
        executing during the measurement interval (i.e., it is not allowed to execute more than S 查询 streams and report
        only the S best ones).

5.3.4.3 For 查询 sequencing purposes (see Clause 5.3.5), each 查询 stream within the 吞吐量 test 必须 assigned a
        unique stream identification number ranging from 1 to S, the number of 查询 streams in the test.

5.3.4.4 When measuring and reporting a 吞吐量 test, a single 刷新 stream (see Clause 5.1.2.4) 必须 executed in
        parallel with the S 查询 streams.
5.3.5   Query Sequencing Rules

5.3.5.1 The 查询 sequencing 规则 apply to each and every 查询 stream, whether 零件 of the power test or 零件 of the
        吞吐量 test.

5.3.5.2 Each 查询 set has an ordering number, O(s), based on the identification number, s, of the 查询 stream executing
        the set. For 示例:
        •        The 查询 set within the unique 查询 stream of the power test has the ordering number O(00);
        •        The 查询 set within the first 查询 stream of the 吞吐量 test has the ordering number O(01);
        •        The 查询 set within the last of s 查询 streams of the 吞吐量 test has the ordering number O(s).


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 96
5.3.5.3 The sequencing of 查询 executions is done within a 查询 set. The ordering number, O(s), of a 查询 set determines
        the 订单 in which queries 必须 submitted (i.e., sequenced for 执行) within that set and is independent of
        any other 查询 set.

5.3.5.4 The 查询 submission 订单 of an ordering number, O(s), is given in Appendix A by the ordered set with reference s.
        Comment: For tests where the list of ordered sets in Appendix A is exhausted, the last reference in the list 必须
        followed by the first reference in the list (i.e., wrapping around to s = 00).
5.3.6    Measurement Interval

5.3.6.1 The measurement interval, Ts, for the 吞吐量 test is measured as follows:
         •        It starts either when the first character of the executable 查询 text of the first 查询 of the first 查询
                  stream is submitted to the SUT by the driver, or when the first character requesting the 执行 of the
                  first 刷新函数 is submitted to the SUT by the driver, whichever happens first;
         Comment: In this 子句 a 查询 stream is said to be first if it starts submitting queries before any other 查询
         streams.
         •        It ends either when the last character of 输出 data from the last 查询 of the last 查询 stream is received
                  by the driver from the SUT, or when the last 事务 of the last 刷新函数 has been completely
                  and successfully committed at the SUT and a success message has been received by the driver from the
                  SUT, whichever happens last.
         Comment: In this 子句 the last 查询 stream is defined to be that 查询 stream whose 输出 data are received last
         by the driver.

5.3.6.2 The measurement interval, Ts, 必须 rounded up to the next 0.01 second when used in 指标 calculations and
        when reported. For 示例, 923.741 and 923.749 are both rounded to 923.75.
5.3.7    Timing Intervals

5.3.7.1 Each of the TPC-H queries and 刷新 functions 必须 executed in an atomic fashion and timed in seconds.

5.3.7.2 The timing interval, QI(i,s), for the 执行 of the 查询, Qi, within the 查询 stream, s, 必须 measured
        between:
         •        The time when the first character of the executable 查询 text is submitted to the SUT by the driver;
         •        The time when the first character of the next executable 查询 text is submitted to the SUT by the driver,
                  except for the last 查询 of the set for which it is the time when the last character of the 查询's 输出 data
                  is received by the driver from the SUT.
         Comment: All the operations that are 零件 of the 执行 of a 查询 (e.g., creation and deletion of a temporary
         表 or a view) 必须 included in the timing interval of that 查询.

5.3.7.3 The timing interval, RI(j,s), for the 执行 of the 刷新函数, RFj, within the 刷新 stream for the power
        test and the 吞吐量 test where s is 0 for the power test and s is the position of the pair of 刷新 functions for
        the 吞吐量 test, 必须 measured between:
         •        The time when the first character requesting the 执行 of the 刷新函数 is submitted to the SUT
                  by the driver;
         •        The last 事务 of the 刷新函数 has been completely and successfully committed at the SUT and
                  a success message has been received by the driver from the SUT.

5.3.7.4 The real-time clock used by the driver to compute the timing intervals 必须 capable of a resolution of at least
        0.001 second.

5.3.7.5 The timing interval of each 查询 and 刷新函数 executed during both tests (i.e., during the power test and the
        吞吐量 test) 必须 rounded to the nearest 0.01 second when used in 指标 calculations and when reported.
        For 示例, 23.714 is rounded to 23.71, and 23.715 is rounded to 23.72. Values of less than 0.005 second 必须
        rounded up to 0.01 second to avoid zero 值.

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 97
5.3.7.6 The 吞吐量 test must include the 执行 of a single 刷新 stream. This 刷新 stream 必须 used exclu-
        sively for the 执行 of the New Sales 刷新函数 (RF1) and the Old Sales 刷新函数 (RF2).

         Comment: The purpose of the 刷新 stream is to simulate a sequence of batched data modifications executing
         against the 数据库 to bring it up to 日期 with its operational data source.

5.3.7.7 The 刷新 stream must execute a number of pairs of 刷新 functions serially (i.e., one RF1 followed by one RF2)
        equal to the number of 查询 streams used for the 吞吐量 test.

         Comment: The purpose of this 要求 is to maintain a consistent read/write ratio across a wide range of num-
         ber of 查询 streams.

5.3.7.8 The scheduling of each 刷新函数 within the 刷新 stream is left to the test sponsor with the only 要求
        that a given pair must complete before the next pair can be initiated and that within a pair RF1 must complete before
        RF2 can be initiated.

         Comment: The intent of this Clause is to allow implementations that execute the 刷新 functions in parallel with
         the ad-hoc queries as well as 系统 that segregate 查询 executions from 数据库 refreshes.

5.3.7.9 The scheduling of individual 刷新 functions within an instance of RF1 or RF2 is left to the test sponsor as long as
        they meet the 要求 of Clause 2.5.2 and Clause 2.5.3.

         Comment: The intent of this Clause is to allow test sponsors to “trickle” the scheduling of 刷新 functions to
         maintain a more even 刷新 load throughout the 吞吐量 test.

5.3.7.10 Prior to the 执行 of the 刷新 stream the DBGEN data used for RF1 and RF2 可 only be generated, per-
         muted and relocated to the SUT. Any other operations on these data, such as data formatting or 数据库 activity,
         必须 included in the 执行 and the timing of the 刷新 functions.

5.4      Metrics
         TPC-H defines the following primary metrics:
         •        The TPC-H Composite Query-per-Hour Metric (QphH@Size) is the 性能 指标, defined in Clause
                  5.4.3;
         •        The 价格-性能 指标 is the TPC-H Price/Performance ($/kQphH/@Size) and is defined in Clause
                  5.4.4;
         •        The Availability Date of the 系统, defined in Clause 0 of the TPC Pricing Specification.
         When TPC_Energy option is chosen for reporting, the TPC-H energy 指标 reports the power per 性能 and
         is expressed as Watts/kQphH@Size. (see TPC-Energy 规范 for additional 要求)
         No other TPC-H primary 指标 exists. However, secondary metrics and numerical quantities such as TPC-H Power
         and TPC-H Throughput (defined in Clause 5.4.1 and Clause 5.4.2 respectively) and S, the number of 查询 streams
         in the 吞吐量 test, 必须 disclosed in the numerical quantities summary (see Clause 8.4.4).
5.4.1    TPC-H Power

5.4.1.1 The results of the power test are used to compute the TPC-H 查询 processing power at the chosen 数据库 size. It
        is defined as the inverse of the geometric mean of the timing intervals, and 必须 computed as:


                                                                      3600 * SF
                                                             i = 22              j =2
                                                        24    QI (i,0) *  RI ( j,0)
                                                              i =1               j =1
                          TPC-H Power@Size =

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 98
        Where:
        QI(i,0) is the timing interval, in seconds, of 查询 Q i within the single 查询 stream of the power test (see
                  Clause 5.3.7)
        RI(j,0) is the timing interval, in seconds, of 刷新函数 RFj within the single 查询 stream of the
                  power test (see Clause 5.3.7)
        Size is the 数据库 size chosen for the measurement and SF the corresponding 规模因子, as defined in
                  Clause 4.1.3.

        Comment: the power numerical 数量 is based on a 查询 per hour rate (i.e., factored by 3600).

5.4.1.2 The units of TPC-H Power@Size are Queries per hour * Scale-Factor, reported to one digit after the decimal point,
        rounded to the nearest 0.1.

5.4.1.3 The TPC-H Power can also be computed as:


                                      1                      i = 22                   j =2
                                                                                                                
                           3600 * exp−                              ln (QI (i ,0 )) +     ln ( RI ( j ,0 ))  * SF
                                       24                      i =1                   j =1                   
        TPC-H Power@Size =
        Where:
        ln(x) is the natural logarithm of x

5.4.1.4 If the ratio between the longest 查询 timing interval and the shortest 查询 timing interval in the power test is
        greater than 1000 (i.e., max[QI(i,0)]/min[QI(i,0)] > 1000), then all 查询 timing intervals which are smaller than
        max[QI(i,0)]/1000 必须 increased to max[QI(i,0)]/1000. The 数量 max[QI(i,0)]/1000 必须 treated as a
        timing interval as specified in Clause 5.3.7.5 for the purposes of computing the TPC-H Power@Size.

        Comment: The adjusted 查询 timings affect only TPC-H Power@Size and no other 组件 of the FDR.
5.4.2   TPC-H Throughput Numerical Quantity

5.4.2.1 The results of the 吞吐量 test are used to compute TPC-H Throughput at the chosen 数据库 size. It is defined
        as the ratio of the total number of queries executed over the length of the measurement interval, and 必须
        computed as:

                 TPC-H Throughput@Size = (S*22*3600)/Ts *SF

                 Where:

                 Ts is the measurement interval defined in Clause 5.3.6

                 S is the number of 查询 streams used in the 吞吐量 test.

                 Size is the 数据库 size chosen for the measurement and SF the corresponding 规模因子, as defined in
                       Clause 4.1.3.

5.4.2.2 The units of TPC-H Throughput@Size are Queries per hour * Scale-Factor, reported to one digit after the decimal
        point, rounded to the nearest 0.1.
5.4.3   The TPC-H Composite Query-Per-Hour Performance Metric

5.4.3.1 The numerical quantities TPC-H Power and TPC-H Throughput are combined to form the TPC-H composite 查询-
        per-hour 性能 指标 which 必须 computed as:




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                           Page 99
                 QphH@Size =
                                     Power @ Size * Throughput @ Size

5.4.3.2 The units of QphH@Size are Queries per hour * Scale-Factor, reported to one digit after the decimal point, rounded
        to the nearest 0.1.
5.4.4   The TPC-H Price/Performance Metric

5.4.4.1 The TPC-H Price/Performance 指标 at the chosen 数据库 size, TPC-H Price-per-kQphH@Size , 必须 com-
        puted using the 性能 指标 QphH@Size as follows:

                 TPC-H Price-per-kQphH@Size = 1000*$/QphH@Size

                 Where:
                    $ is the total 系统 价格 in the reported currency. The list of components to be priced is described in
                    Clause 7.0 of this 规范. How to 价格 the components and how to express the total 系统
                    价格 are defined in Clause 7 of the TPC Pricing Specification.

                 QphH@Size is the composite 查询-per-hour 性能 指标 defined in Clause 5.4.3.

                 Size is the 数据库 size chosen for the measurement, as defined in Clause 4.1.3.

5.4.4.2 The units of Price-per-kQphH@Size are expressed as in Clause 7 of TPC Pricing Specification. In the United States
        the 价格 性能 is expressed as USD per kQphH@Size rounded to the highest cent (e.g., $12.123 必须
        shown as $12.13USD for 性价比).
5.4.5   Fair Metric Comparison

5.4.5.1 Comparisons of TPC-H 基准测试 results measured against databases of different sizes are believed to be mislead-
        ing because 数据库 性能 and capabilities 可 not scale up proportionally with an increase in 数据库 size
        and, similarly, the 系统 性价比 ratio 可 not scale down with a decrease in 数据库 size.

        If results measured against different 数据库 sizes (i.e., with different scale factors) appear in a printed or electronic
        communication, then each reference to a 结果 or 指标 must clearly indicate the 数据库 size against which it was
        obtained. In particular, all textual references to TPC-H metrics (性能 or 性价比) appearing must
        be expressed in the form that includes the size of the test 数据库 as an integral 零件 of the 指标’s name; i.e.
        including the “@size” suffix. This applies to metrics quoted in text or 表 as well as those used to annotate charts
        or graphs. If metrics are presented in graphical form, then the test 数据库 size on which 指标 is based 必须
        immediately discernible either by appropriate axis labeling or data point labeling.

        In addition, the results 必须 accompanied by a disclaimer stating:
        “The TPC believes that comparisons of TPC-H results measured against different 数据库 sizes are misleading and
        discourages such comparisons”.

5.4.5.2 Any TPC-H 结果 is comparable to other TPC-H results regardless of the number of 查询 streams used during the
        test (as long as the scale factors chosen for their respective test databases were the same).
5.4.6   Required Reporting Components
        To be compliant with the TPC-H standard and the TPC's fair use policies, all public references to TPC-H results for
        a given 配置 must include the following components:
        •        The size of the test 数据库, expressed separately or as 零件 of the 指标's names (e.g., QphH@10GB);
        •        The TPC-H Performance Metric, QphH@Size;
        •        The TPC-H Price/Performance 指标, $/kQphH@Size;
        •        The 可用性 日期 of the priced 配置 (see Clause 7 of the TPC Pricing Specification).
        Following are two examples of compliant reporting of TPC-H results:

        Example 1: At 10000GB the RALF/3000 Server, priced at 205,345, has a TPC-H Composite Query-per-Hour

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 100
指标 of 3,010,324 yielding a TPC-H Price/Performance of $68.21 per 1000 查询-per-hour and will be available 1-
Apr-99.
Example 2: The RALF/3000 Server, which will start shipping on 1-Apr-99, is rated 3,010,324QphH@10000GB
and 68.21 $/kQphH@10000GB.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                 Page 101
                                       6: SUT AND DRIVER IMPLEMENTATION

6.1     Models of Tested Configurations

6.1.1   The tested and reported 配置(s) is composed of a driver that submits queries to a 系统 under test (SUT).
        The SUT executes these queries and replies to the driver. The driver resides on the SUT 硬件 and 软件.
6.1.2   Figure 3: Two driver/SUT configurations, a “host-based” and a “client/server” 配置 illustrates examples of
        driver/SUT configurations. The driver is the shaded area. The diagram also depicts the driver/SUT boundary (see
        Clause 5.2 and Clause 5.3) where timing intervals are measured.
        Figure 3: Two driver/SUT configurations, a “host-based” and a “client/server” 配置
                                                        Host Systems
                                                                          *
                                                                              *

                                                                Query
                                               DRIVER




                                                              Execution                   Network*
                                                                  &
                                                              Database
                                                               Acc ess




                 Client(s)                                                        Server(s)
                                       *                                                      *
                                           *                                                      *
               DRIVER




                             Query                         Network
                           Execution                                                  Database            Network*
                                                                                       Acc ess




            Items marked by an * are optional


6.2     System Under Test (SUT) Definition

6.2.1   The SUT consists of:
        •               The host 系统(s) or server(s) including 硬件 and 软件 supporting access to the 数据库
                        employed in the 性能 test and whose 成本 and 性能 are described by the 基准测试 metrics;
        •               One or more client processing units (e.g., front-end processors/cores/threads, workstations, etc.) that will
                        execute the queries (if used);
        •               The 硬件, Licensed Compute Services and 软件 components needed to communicate with user
                        interface devices;
        •               The 硬件, Licensed Compute Services and 软件 components of all networks required to connect
                        and support the SUT components;
        •               Data storage media sufficient to satisfy both the scaling 规则 in Clause 4: and the ACID properties of
                        Clause 3: . The data storage media must hold all the data described in Clause 4: and be attached to the
                        processing units(s).

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                           Page 102
6.2.2   All SUT components, as described in Clause 6.2.1, 必须 commercially available 软件 or 硬件 products.
6.2.3   An 实现 specific layer can be implemented on the SUT. This layer 必须 logically located between the
        driver and the SUT, as depicted by Figure 4: Implementation Specific Layer.
        Figure 4: Implementation Specific Layer




                                                             DRIVER


                     Exec. Query Text + Row Count
                                                                           Output Data


                                             Implementation Specific Layer


                                                  Commercially Available
                                                           Products
                                                  (e.g., OS, DBMS, ISQL)
             SUT

6.2.4   An 实现 specific layer, if present on the SUT, 必须 minimal, general purpose (i.e., not limited to the
        TPC-H queries) and its source code 必须 disclosed. Furthermore, the functions performed by an 实现
        specific layer 必须 strictly limited to the following:
        •       Database 事务 control operations before and after each 查询 执行;
        •       Cursor control and manipulation operations around the executable 查询 text;
        •       Definition of procedures and data structures required to process dynamic SQL, including the
                communication of the executable 查询 text to the commercially available layers of the SUT and the
                reception of the 查询 输出 data;
        •       Communication with the commercially available layers of the SUT;
        •       Buffering of the 查询 输出 data;
        •       Communication with the driver.
        The following are examples of functions that the 实现 specific layer 应 not perform:
        •       Any modification of the executable 查询 text;
        •       Any use of stored procedures to execute the queries;
        •       Any sorting or translation of the 查询 输出 data;
        •       Any function prohibited by the 要求 of Clause 5.2.7.

6.3     Driver Definition

6.3.1   The driver presents the 工作负载 to the SUT.
6.3.2   The driver is a logical entity that can be implemented using one or more programs, processes, or 系统 and per-

        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                   Page 103
        forms the functions defined in Clause 6.3.3.
6.3.3   The driver can perform only the following functions:
        •        Generate a unique stream ID, starting with 1 (or 0 for the power test), for each 查询 stream;
        •        Sequence queries for 执行 by the 查询 streams (see Clause 5.3.5);
        •        Activate, schedule, and/or synchronize the 执行 of 刷新 functions in the 刷新 stream (see Clause
                 5.3.7.8);
        •        Generate the executable 查询 text for each 查询;
        •        Generate 值 for the substitution parameters of each 查询;
        •        Complete the executable 查询 text by replacing the substitution parameters by the 值 generated for
                 them and, if needed, replacing the text-tokens by the 查询 stream ID;
        •        Submit each complete executable 查询 text to the SUT for 执行, including the number of 行 to be
                 returned when specified by the functional 查询 定义;
        •        Submit each executable 刷新函数 to the SUT for 执行;
        •        Receive the 输出 data resulting from each 查询 执行 from the SUT;
        •        Measure the 执行 times of the queries and the 刷新 functions and compute measurement statistics;
        •        Maintain an 审计 log of 查询 text and 查询 执行 输出.
6.3.4   The generation of executable 查询 text used by the driver to submit queries to the SUT does not need to occur on
        the SUT and does not have to be included in any timing interval.
6.3.5   The driver 应 not perform any function other than those described in Clause 6.3.3. Specifically, the driver 应
        not perform any of the following functions:
        •        Performing, activating, or synchronizing any operation other than those mentioned in Clause 6.3.3;
        •        Delaying the 执行 of any 查询 after the 执行 of the previous 查询 other than for delays
                 necessary to process the functions described in Clause 6.3.3. This delay 必须 reported and cannot
                 exceed half a second between any two consecutive queries of the same 查询 stream;
        •        Modifying the compliant executable 查询 text prior to its submission to the SUT;
        •        Embedding the executable 查询 text within a stored procedure 定义 or an application program;
        •        Submitting to the SUT the 值 generated for the substitution parameters of a 查询 other than as 零件 of
                 the executable 查询 text submitted;
        •        Submitting to the SUT any data other than the instructions to execute the 刷新 functions, the compliant
                 executable 查询 text and, when specified by the functional 查询 定义, the number of 行 to be
                 returned;
        •        Artificially extending the 执行 time of any 查询.
6.3.6   The driver is not required to be priced.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                   Page 104
                                                       7: PRICING
         This 节 defines the components, functional 要求 of what is priced, and what substitutions are allowed.
         Rules for 定价 the Priced Configuration and associated 软件 and 维护 are included in the current
         revision of the TPC Pricing Specification located at www.tpc.org.

7.0      General

7.0.1    The 定价 methodology used for 定价 the Priced Configuration is the “Default 3-Year Pricing Methodology”, as
         defined in the current revision of the TPC Pricing 规范.
7.0.2    The 定价 model used for 定价 the Priced Configuration is the “Default Pricing Model”, as defined in the current
         revision of the TPC Pricing 规范.
7.0.3    The components to be priced are defined by the Priced Configuration (see Clause 7.1).
7.0.4    The functional 要求 of the Priced Configuration are defined in terms of the Measured Configuration (see
         Clause 6.2).
7.0.5    The allowable substitutions are defined in Clause 7.2 (Allowable Substitution).

7.1      Priced Configuration
         The 系统 to be priced 应 include the 硬件, Licensed Compute Services and 软件 components present in
         the System Under Test (SUT), a communication interface that can support user interface devices, additional
         operational components configured on the test 系统, and 维护 on all of the above
7.1.1    System Under Test
         Calculation of the priced 配置 consists of:
         •        Price of the SUT as tested and defined in Clause 6: ;
         •        Price of a communication interface capable of supporting the required number of user interface devices
                  defined in Clause 7.1.2.1;
         •        Price of on-line storage for the 数据库 as described in Clause 7.1.3 and storage for all 软件 included
                  in the priced 配置;
         •        Price of additional products (软件 or 硬件) required for customary operation, administration and
                  维护 of the SUT for a period of 3 years
         •        Price of all products required to create, execute, administer, and maintain the executable 查询 texts or
                  necessary to create and populate the test 数据库.
         Specifically excluded from the priced 配置 calculation are:
         •        End-user communication devices and related cables, connectors, and concentrators;
         •        Equipment and tools used exclusively in the production of the full disclosure report;
         •        Equipment and tools used exclusively for the 执行 of the DBGEN or QGEN (see Clause 4.2.1 and
                  Clause 2.1.4) programs.
7.1.2    User Interface Devices and Communications

7.1.2.1 The priced 配置 must include the 硬件 and 软件 components of a communication interface capable
        of supporting a number of user interface devices (e.g., terminals, workstations, PCs, etc.) at least equal to 10 times
        the number of 查询 streams used for the 吞吐量 test (see 5.3.4).
        Comment: Test sponsors are encouraged to configure the SUT with a general-purpose communication interface
        capable of supporting a large number of user interface devices.

7.1.2.2 Only the interface is to be priced. Not to be included in the priced 配置 are the user interface devices
        themselves and the cables, connectors and concentrators used to connect the user interface devices to the SUT. For
        示例, in a 配置 that includes an Ethernet interface to communicate with PCs, the Ethernet card and

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 105
         supporting 软件 必须 priced, but not the Ethernet cables and the PCs.
         Comment: Active components (e.g., workstations, PCs, concentrators, etc.) can only be excluded from the priced
         配置 under the assumption that their role is strictly limited to submitting executable 查询 text and
         receiving 输出 data and that they do not participate in the 查询 执行. All 查询 processing performed by the
         tested 配置 is considered 零件 of the 性能 test and can only be done by components that are included
         in the priced 配置.

7.1.2.3 The communication interface used 必须 an industry standard interface, such as Ethernet, Token Ring, or RS232.

7.1.2.4 The following diagram illustrates the boundary between what is priced (on the right) and what is not (on the left):




         Figure 5: The Pricing Boundary


                                                   Driver                           SUT


                                                                          (Implementation Specific Layer)
               User Interface            Network                             Commercially Available
                 Device(s)                                                           Products
                                                                             (e.g., OS, DBMS, ISQL)



                                      Pricing Boundary



7.1.3    Database Storage and Recovery Log

7.1.3.1 Recovery data 必须 maintained for at least the duration of the run used to compute the published 性能
        metrics (see Clause 5.1.1.3).

         Roll-back 恢复 data 必须 either in memory or in on-line storage at least until all transactions dependent on it
         are committed. Roll-forward 恢复 data 可 be stored on an off-line device provided that:
         •        The process that stores the roll-forward data is active during the measurement interval;
         •        The roll-forward data that is stored off-line during the measurement interval 必须 at least as great as the
                  roll-forward 恢复 data that is generated during the period (i.e., the data 可 be first created in on-line
                  storage and then moved to off-line storage, but the creation and the movement of the data 必须 in steady
                  state);
         •        All ACID properties 必须 retained.
         Comment: Storage is considered on-line if any 记录 can be accessed randomly and updated within 1 second even
         if this access time requires the creation of a logical access path not present in the tested 数据库. For 示例, a
         disk-based sequential file might require the creation of an 索引 to satisfy the access time 要求. On-line stor-
         age 可 include magnetic disks, optical disks, or any combination of these, provided that the above mentioned
         access criteria are met.

7.1.3.2 While the 基准测试 requires the 配置 of storage sufficient to hold the requisite 恢复 data as specified
        in Clause 7.1.3.1, it does not explicitly require the demonstration of rollforward 恢复 except as required by the
        ACID tests (See Clause 3.5).

7.1.3.3 This 子句 has been left intentionally blank.

7.1.3.4 The storage that is required to be priced includes:
         •        storage required to execute the 基准测试;

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 106
        •        storage to hold 恢复 data (see Clause 7.1.3);
        •        storage and media needed to assure that the test 数据库 meets the ACID 要求 defined in Clause 3:
                 .

7.1.3.5 All storage required for the priced 配置 必须 present on the measured 配置.
7.1.4   Additional Operational Components

7.1.4.1 Additional products that might be included on a 客户 installed 配置, such as operator consoles and
        magnetic tape drives, are also to be included in the priced 配置 if explicitly required for the operation,
        administration, or 维护, of the priced 配置.

7.1.4.2 Copies of the 软件, on appropriate media, and a 软件 load device, if required for initial load or 维护
        updates, 必须 included.

7.1.4.3 The 价格 of an Uninterruptible Power Supply, if specifically contributing to a 持久性 solution, 必须 included
        (see Clause 3.5.

7.1.4.4 The 价格 of all cables used to connect components of the 系统 (except as noted in Clause 7.1.2.2) 必须
        included.
7.1.5   Software

7.1.5.1 All 软件 licenses 必须 priced for a number of users at least equal to 10 times the number of 查询 streams
        used for the multi-stream 吞吐量 test (see Clause 5.3.4). Any usage 定价 for this number of users 必须
        based on the 定价 policy of the company supplying the priced 组件.

7.2     Allowable Substitutions

7.2.1   Substitution is defined as a deliberate act to replace components of the Priced Configuration by the test sponsor as a
        结果 of failing the 可用性 要求 of the TPC Pricing Specification or when the 零件 number for a com-
        ponent changes.

        Comment 1: Corrections or "fixes" to components of the Priced Configuration are often required during the life of
        products. These changes are not considered Substitutions so long as the 零件 number of the priced 组件 does
        not change. Suppliers of 硬件 and 软件 可 update the components of the Priced Configuration, but these
        updates must not impact the reported 性能 指标 or numerical quantities. The following are not considered
        substitutions:
        •        软件 patches to resolve a security vulnerability
        •        silicon revision to correct errors
        •        new 供应商 of functionally equivalent components (i.e. memory chips, disk drives, ...)
        Durable Medium is defined as a data storage medium that is inherently non-volatile such as a magnetic disk or tape.
7.2.2   Some 硬件 components of the Priced Configuration 可 be substituted after the test sponsor has demonstrated
        to the auditor's satisfaction that the substituting components do not negatively impact the reported 性能
        指标 or numerical quantities. All substitutions 必须 reported in the FDR and noted in the auditor's attestation
        letter. The following 硬件 components 可 be substituted:
        •        Durable Medium, Disk Enclosure, external storage controllers
        •        Network interface cards
        •        Routers, Bridges, Repeaters, Switches
        •        Cables




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 107
                                             8: FULL DISCLOSURE


8.1     Reporting Requirements

8.1.1   A Full Disclosure Report (FDR) in pdf format, Executive Summary and a Supporting Files Archive (zip format)
        consisting of various source files, scripts, and listing files are required.
8.1.2   The intent of this disclosure is to simplify comparison between results and for a 客户 to be able to replicate the
        results of this 基准测试 given appropriate documentation and products.

8.2     Format Guidelines

8.2.1   While established practice or practical limitations 可 cause a particular 基准测试 disclosure to differ from the
        examples provided in various small ways, every effort 应 be made to conform to the format guidelines. The
        intent is to make it as easy as possible for a reviewer to read, compare and evaluate material in different 基准测试
        disclosures.
8.2.2   All sections of the report, including appendices, 必须 printed using font sizes of a minimum of 8 points.
8.2.3   The Executive Summary 必须 included near the beginning of the full disclosure report.

8.3     Full Disclosure Report Contents and Supporting Files Archive
        The FDR 应 be sufficient to allow an interested reader to evaluate and, if necessary, recreate an 实现
        of TPC-H. If any sections in the FDR refer to another 节 of the report (e.g., an appendix), the names of the ref-
        erenced scripts/programs 必须 clearly labeled in each 节. Unless explicitly stated otherwise “disclosed”
        refers to disclosed in the FDR.

        The “Supporting Files Archive” are compressed files containing a directory tree of all the files required to be
        disclosed electronically as 零件 of the FDR. All files 必须 compressed using the Zip 2.0 standard file format
        without password protection or encryption. These archives will contain a mix of human readable and machine
        executable code or scripts (i.e., able to be performed by the appropriate program without modification) that are
        required to recreate the 基准测试 结果. Any machine executable code or scripts requiring compilation 必须
        included as source code including any build or compilation flags (e.g., a make file). If there is a choice of using a
        GUI (Graphical User Interface) or a script, then the machine executable script 必须 provided in the Supporting
        Files Archive. If no corresponding script is available for a GUI, then the Supporting Files Archive must contain a
        detailed step-by-step 说明 of how to manipulate the GUI (e.g. a PDF document containing screen shots of
        each completed dialog just prior to clicking “ok” with clear instructions on how to bring up each dialog or window).
        These archives will also contain all the 输出 required to validate the 结果’s 合规 with the 规范.

        The Supporting Files Archive 应 be split into three separate compressed files. For the 查询 输出 data of Q11,
        Q16, and Q20, the sponsor must report the first and last 1000 行, 1000 random non-consecutive 行 between the
        first and last 1000 行, and the 行 number from the respective 查询 输出. All 输出 from other queries must
        be provided in their entirety. The sponsor must provide the full 查询 输出 for the duration of the review period
        upon request.
              • All 查询 输出 data from the 1st run of both the power and 吞吐量 tests 必须 contained in the first
                  file named “run1结果.zip”
              • All 查询 输出 data from the 2nd successful run of both the power and 吞吐量 tests 必须 contained
                  in the second file named “run2结果.zip”.
              • All other data that is required to be disclosed in the Supporting Files Archive 必须 contained in the third
                  file named “基准测试_scripts.zip”.

        If any one compressed file will be greater than 2GB, it 必须 broken into multiple files, each of which is no
        greater than 2GB. In this case, a sequence number 必须 appended to the appropriate filename above (e.g.
        run1结果_1.zip, run1结果_2.zip).


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 108
        Comment: Since the building of a 数据库 可 consist of a set of scripts and corresponding 输入 files, it is impor-
        tant to disclose and clearly identify, by name, scripts and 输入 files in the FDR.
        The 订单 and titles of sections in the test sponsor's full disclosure report must correspond with the 订单 and titles of
        sections from the TPC-H standard 规范 (i.e., this document).
        Comment: The purpose of disclosing Supporting Files is to show how the 硬件 and 软件 is changed from
        their defaults to reproduce the 基准测试 结果.
8.3.1   General Items

8.3.1.1 A statement identifying the 基准测试 sponsor(s) and other participating companies 必须 provided.

8.3.1.2 Settings 必须 provided for all 客户-tunable parameters and options that have been changed from the defaults
        found in actual products, including but not limited to:
        •        Database tuning options;
        •        Optimizer/Query 执行 options;
        •        Query processing tool/language 配置 parameters;
        •        Recovery/commit options;
        •        Consistency/locking options;
        •        Operating 系统 and 配置 parameters;
        •        Configuration parameters and options for any other 软件 组件 incorporated into the 定价 struc-
                 ture;
        •        Compiler 优化 options.
        Comment 1: In the event that some parameters and options are set multiple times, it 必须 easily discernible by an
        interested reader when the parameter or option was modified and what new 值 it received each time.

        Comment 2: This 要求 can be satisfied by providing a full list of all parameters and options, as long as all
        those that have been modified from their default 值 have been clearly identified and these parameters and
        options are only set once.

8.3.1.3 Explicit response to individual disclosure 要求 specified in the body of earlier sections of this document
        必须 provided.

8.3.1.4 Diagrams of both measured and priced configurations 必须 provided, accompanied by a 说明 of the differ-
        ences. This includes, but is not limited to:
        •        Total number of nodes used, total number and type of processors used/total number of cores used/total
                 number of threads used (including sizes of L2 and L3 caches);
        •        Size of allocated memory, and any specific mapping/partitioning of memory unique to the test;
        •        Number and type of disk units (and controllers, if applicable);
        •        Number of channels or bus connections to disk units, including their protocol type;
        •        Number of LAN (e.g., Ethernet) connections, including routers, workstations, terminals, etc., that were
                 physically used in the test or are incorporated into the 定价 structure;
        •        Type and the run-time 执行 location of 软件 components (e.g., DBMS, 查询 processing tools/lan-
                 guages, middleware components, 软件 drivers, etc.).
        The following sample diagram illustrates a measured 基准测试 配置 using Ethernet, an external driver,
        and four processors each with two cores and four threads per node in the SUT. Note that this diagram does not
        depict or imply any optimal 配置 for the TPC-H 基准测试 measurement.




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 109
        Figure 1: Sample Configuration Diagram (the front 系统 box describes one node)




        LAN: Ethernet using NETplus routers
        Total number of nodes used/total number of processors used/total number of cores used/total number of threads
        used:
                4/16/32/64 x a243DX 3GHz with 4 MByte Second Level Cache
                4 gigabyte of main memory
                16 x SCSI-2 Fast Controllers
                Disk: 96 x 2.1 gigabyte SCSI-2 drives

        Comment: Detailed diagrams for 系统 configurations and architectures can vary widely, and it is impossible to
        provide exact guidelines suitable for all implementations. The intent here is to describe the 系统 components and
        connections in sufficient detail to allow independent reconstruction of the measurement environment. This 示例
        diagram shows homogeneous nodes. This does not preclude tests sponsors from using heterogeneous nodes as long
        as the 系统 diagram reflects the correct 系统 配置.
8.3.2   Rules for reporting 定价 information are included in the current revision of the TPC Pricing Specification located
        at www.tpc.org.

8.3.3   Supporting Files Index Table

8.3.3.1 An 索引 for all files and/or directories included in the Supporting Files Archive as required by Clauses 8.3.2
        through 8.3.8 必须 provided in the report. The “Supporting Files Index Table” is presented in a tabular format
        where the 列 specify the following:
               •      The first 列 denotes the 子句 in the TPC-H Specification
               •      The second 列 provides a short 说明 of the file(s) and/or directory(s) contents.
               •      The third 列 contains the zip filename(s) containing this file(s) or directory(s).
               •      The fourth 列 contains the pathname for the file(s) or directory(s) starting at the root of the archive.
             Patterns and/or wildcards 可 be used to specify multiple files or directories.
             If there are no supporting files or directories provided then the 说明 列 must indicate that there is no
             supporting file and the pathname 列 必须 left blank



8.3.3.2 The following 表 is an 示例 of the Supporting Files Index Table that 必须 reported in the Report.

  Clause           Description              Archive File            Pathname
                   Partitioning scripts     基准测试_scripts.zip   SupportingFiles/Clause1/Partitioning/
  Clause 1
                   OS Tunable Parameters    基准测试_scripts.zip   SupportingFiles/Clause1/OStune.txt


        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                             Page 110
               QGEN Modifications         基准测试_scripts.zip   SupportingFiles/Clause2/QGEN.txt

               Minor 查询                基准测试_scripts.zip
  Clause 2                                                        SupportingFiles/Clause2/MinorQuery.txt
               modifications

               Code Style Usage           基准测试_scripts.zip   SupportingFiles/Clause2/CodeStyle.txt

               ACID Test scripts          基准测试_scripts.zip   SupportingFiles/Clause3/ACIDScripts/
  Clause 3
               ACID Test Results          基准测试_scripts.zip   SupportingFiles/Clause3/ACIDResults/

               Qualification db           基准测试_scripts.zip
                                                                  SupportingFiles/Clause4/QualResults/
               differences

  Clause 4     DBGEN Modifications        基准测试_scripts.zip   SupportingFiles/Clause4/DBGEN.txt

              Database Load Scripts       基准测试_scripts.zip   SupportingFiles/Clause4/Load.txt

               Data Transfer Programs     基准测试_scripts.zip   SupportingFiles/Clause4/DataTransfer/

                                          run1results.zip         SupportingFiles/Clause5/QueryOutput/Run1/
               Query Output Results                               SupportingFiles/Clause5/QueryOutput/Run2/
                                          run2results.zip

               Session Implementation     基准测试_scripts.zip
                                                                  SupportingFiles/Clause5/Session.txt
               Configuration
  Clause 5
               PDO Procedures             基准测试_scripts.zip   SupportingFiles/Clause5/PDO.txt

               Steps performed            基准测试_scripts.zip
               between end of Load
                                                                  SupportingFiles/Clause5/EOLStart.txt
               and start of Performance
               Run.

               Implementation Specific    基准测试_scripts.zip
  Clause 6                                                        SupportingFiles/Clause6/ImplementationSource/
               layer source code

               There are no files
  Clause 7     required to be included             n/a            n/a
               for Clause 7.

               Horizontal Partitioning    基准测试_scripts.zip
                                                                  SupportingFiles/Clause8/HorizontalPart.txt
               scripts

               Executable 查询 test      基准测试_scripts.zip   SupportingFiles/Clause8/QueryText.txt
  Clause 8
               Query substitution         基准测试_scripts.zip
                                                                  SupportingFiles/Clause8/QueryParmsSeeds.txt
               parameters and seeds

               RF function source code    基准测试_scripts.zip   SupportingFiles/Clause8/RFfunctionsource/




8.3.4    Clause 1 - Logical Database Design Related Items

8.3.4.1 Listings 必须 provided for all 表 定义 statements and all other statements used to set-up the test and qual-
        ification databases. All listings 必须 reported in the supporting files archive.

8.3.4.2 The physical organization of 表 and indices within the test and qualification databases 必须 disclosed. If the
        列 ordering of any 表 is different from that specified in Clause 1.4, it 必须 noted. The physical
        organization of 表 必须 reported in the supporting files archive.

         Comment: The concept of physical organization includes, but is not limited to: 记录 clustering (i.e., 行 from
         different logical 表 are co-located on the same physical data page), 索引 clustering (i.e., 行 and leaf nodes of
         an 索引 to these 行 are co-located on the same physical data page), and partial fill-factors (i.e., physical data
         pages are left partially empty even though additional 行 are available to fill them).

8.3.4.3 Horizontal partitioning of 表 and 行 in the test and qualification databases (see Clause 1.5.4) 必须
        disclosed. Scripts to perform horizontal partitioning 必须 reported in the supporting files archive.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 111
8.3.4.4 Any 复制 of physical objects 必须 disclosed and must conform to the 要求 of Clause 1.5.7. Scripts
        to perform any 复制 必须 reported in the supporting files archive.

8.3.4.5 Script or text for all 硬件 and 软件 tunable parameters 必须 reported in the supporting files archive.
8.3.5    Clause 2 - Query and Refresh function-Related Items

8.3.5.1 The 查询 language used to 实现 the queries 必须 identified (e.g., “RALF/SQL-Plus”).

8.3.5.2 The version number, release number, modification number, and patch level of QGen 必须 disclosed. Any
        modifications to the QGen (see Clause 2.1.4) source code (see Appendix D) 必须 reported in the supporting files
        archive

8.3.5.3 The executable 查询 text used for 查询 validation 必须 reported in the supporting files archive along with the
        corresponding 输出 data generated during the 执行 of the 查询 text against the qualification 数据库. If
        minor modifications (see Clause 2.2.3) have been applied to any functional 查询 definitions or approved variants in
        订单 to obtain executable 查询 text, these modifications 必须 disclosed and justified. The justification for a
        particular minor 查询 modification can apply collectively to all queries for which it has been used.

8.3.5.4 All the 查询 substitution parameters used during the 性能 test 必须 disclosed in tabular format, along
        with the seeds used to generate these parameters.

8.3.5.5 The isolation level used to run the queries 必须 disclosed. If the isolation level does not map closely to one of the
        isolation levels defined in Clause 3.4, additional descriptive detail 必须 provided.

8.3.5.6 The details of how the 刷新 functions were implemented 必须 reported in the supporting files
        archive(including source code of any non-commercial program used).
8.3.6    Clause 3 - Database System Properties Related Items

8.3.6.1 The results of the ACID tests 必须 disclosed along with a 说明 of how the ACID 要求 were met.
        All code (including queries, stored procedures etc.) used to test the ACID 要求 and their entire 输出 must
        be reported in the supporting files archive.
8.3.7    Clause 4 - Scaling and Database Population Related Items

8.3.7.1 The cardinality (e.g., the number of 行) of each 表 of the test 数据库, as it existed at the completion of the
        数据库 load (see Clause 4.2.5), 必须 disclosed.

8.3.7.2 The distribution of 表 and logs across all media 必须 explicitly described using a format similar to that shown
        in the following 示例 for both the measured and priced configurations.

         Comment: Detailed diagrams for layout of 数据库 表 on disks can widely vary, and it is difficult to provide
         exact guidelines suitable for all implementations. The intent is to provide sufficient detail to allow independent
         reconstruction of the test 数据库. The 表 below is an 示例 of 数据库 layout descriptions and is not intended
         to describe any optimal layout for the TPC-H 数据库.

                                          Table 12: Sample Database Layout Description


            Controller             Disk Drive         Description of Content

            40A                    0                  Operating 系统, root

                                   1                  System page and swap

                                   2                  Physical log

                                   3                  100% of PART and SUPPLIER 表

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 112
            40B                    0                 33% of CUSTOMER, ORDERS and LINEITEM 表

                                   1                 33% of CUSTOMER, ORDERS and LINEITEM 表

                                   2                 34% of CUSTOMER, ORDERS and LINEITEM 表

                                   3                 100% of PARTSUPP, NATION and REGION 表


8.3.7.3 The mapping of 数据库 partitions/replications 必须 explicitly described.
        Comment: The intent is to provide sufficient detail about partitioning and 复制 to allow independent recon-
        struction of the test 数据库.

8.3.7.4 Implementations 可 use data redundancy mechanism(s). The type of data redundancy mechanism(s) and any
        配置 parameters (e.g., RAID level used 必须 disclosed for each device). If data redundancy
        mechanism(s) are used in an 实现, the logical intent of their use 必须 disclosed. Four levels of usage
        are defined in 子句 8.3.5.4.1:
        •           - Base Tables
        •           - Auxiliary Data Structures
        •           - DBMS Temporary Space
        •          - OS and DBMS Software (binaries and 配置 files)

8.3.7.4.1 Storage Redundancy
             −    Storage Redundancy Level Zero (No Redundancy): Does not guarantee access to any data on Durable
                  Media when a single Durable Media failure occurs.
             −    Storage Redundancy Level One (Durable Media Redundancy): Guarantees access to the data on Durable
                  Media when a single Durable Media failure occurs.
             −    Storage Redundancy Level Two (Durable Media Controller Redundancy): Includes Redundancy Level One
                  and guarantees access to the data on Durable Media when a single failure occurs in the storage controller
                  used to satisfy the redundancy level or in the communication media between the storage controller and the
                  Durable Media.
                  Storage Redundancy Level Three (Full Redundancy): Includes Redundancy Level Two and guarantees
                  access to the data on Durable Media when a single failure occurs within the Durable Media 系统,
                  including communications between 数据库 host 系统(s)/server(s) and the Durable Media 系统

8.3.7.5 The version number, release number, modification number, and patch level of DBGen 必须 disclosed. Any
        modifications to the DBGen (see Clause 4.2.1) source code (see Appendix D) 必须 reported in the supporting
        files archive.

8.3.7.6 The 数据库 load time for the test 数据库 (see Clause 4.3) 必须 disclosed.

8.3.7.7 The data storage ratio 必须 disclosed. It is computed by dividing the total data storage of the priced 配置
        (expressed in GB) by the size chosen for the test 数据库 as defined in Clause 4.1.3.1. Let r be the ratio. The
        reported 值 for r 必须 rounded to the nearest 0.01. That is, reported 值=round(r,2). For 示例, a 系统
        configured with 96 disks of 2.1 GB capacity for a 100GB test 数据库 has a data storage ratio of 2.02.
        Comment: For the reporting of configured disk capacity, gigabyte (GB) is defined to be 2^30 bytes. Since disk
        manufacturers typically report disk size using base ten (i.e., GB = 10^9), it 可 be necessary to convert the adver-
        tised size from base ten to base two.

8.3.7.8 The details of the 数据库 load 必须 reported in the supporting files archive. Disclosure of the load procedure
        includes all steps, scripts, 输入 and 配置 files required to completely reproduce the test and qualification
        databases. A block diagram illustrating the overall process 必须 disclosed.

8.3.7.9 Any differences between the 配置 of the qualification 数据库 and the test 数据库 必须 disclosed.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                     Page 113
8.3.7.10 The memory to 数据库 size percentage 必须 disclosed. It is computed by multiplying by 100 the total memory
         size priced on the SUT (see 子句 6.2.1 ) and dividing this number by the size chosen for the test 数据库 as
         defined in Clause 4.1.3.1. Let r be this ratio. The reported ratio 必须 rounded to the nearest 0.1. That is, reported
         值=round(r,1). For 示例, a 系统 configured with 256GB of memory for a 1000GB test 数据库 has a
         memory/数据库 size percentage of 25.6.
8.3.8    Clause 5 - Performance Metrics and Execution Rules Related Items

8.3.8.1 Any 系统 activity on the SUT that takes place between the conclusion of the load test and the beginning of the
        性能 test 必须 fully reported in the supporting files archive including listings of scripts, command logs
        and 系统 activity.

8.3.8.2 The details of the steps followed to 实现 the power test (e.g., 系统 boot, 数据库 restart, etc.) 必须
        reported in the supporting files archive.

8.3.8.3 The timing intervals (see Clause 5.3.7) for each 查询 and for both 刷新 functions 必须 reported for the power
        test. The 输出 for each 查询 and for both 刷新 functions 必须 reported in the supporting files archive.

8.3.8.4 The number of 查询 streams used for the 吞吐量 test 必须 disclosed.

8.3.8.5 The start time and finish time for each 查询 stream for the 吞吐量 test 必须 disclosed. The 输出 for each
        查询 stream for the 吞吐量 test 必须 reported in the supporting files archive.

8.3.8.6 The total 耗时 of the measurement interval (see Clause 5.3.6) 必须 disclosed for the 吞吐量 test.

8.3.8.7 The start time and, finish time for each 刷新函数 in the 刷新 stream for the 吞吐量 test 必须
        disclosed. The 输出 of each 刷新函数 in the 刷新 stream for the 吞吐量 test 必须 reported in the
        supporting files archive.

8.3.8.8 The start time and finish time for each 查询 and 刷新 stream 应 be reported to the hundredth of a second. If
        times are measured with the precision greater than one hundredth of a second, the reported times 应 be truncated
        to the hundredth of a second.

8.3.8.9 The computed 性能 指标, related numerical quantities and the 性价比 指标 必须 disclosed.

8.3.8.10 The 性能 指标 (QphH@Size) and the numerical quantities (TPC-H Power@Size and TPC-H Through-
         put@Size) from both of the runs 必须 disclosed (see Clause 5.4).

8.3.8.11 Any activity on the SUT that takes place between the conclusion of Run1 and the beginning of Run2 必须 fully
         disclosed including 系统 activity, listings of scripts or command logs along with any 系统 reboots or 数据库
         restarts.

8.3.8.12 All documentation necessary to satisfy Clause 5.2.7 必须 made available upon request.

8.3.8.13 The 输出 of the Query Output Validation Test must reported in the supporting files archive.



8.3.9    Clause 6 - SUT and Driver Implementation Related Items

8.3.9.1 A detailed textual 说明 of how the driver performs its functions, how its various components interact and any
        product functionalities or environmental settings on which it relies and all related source code, scripts and
        配置 files 必须 reported in the supporting files archive. The information provided 应 be sufficient
        for an independent reconstruction of the driver.

8.3.9.2 If an 实现 specific layer is used, then a detailed 说明 of how it performs its functions, how its var-
        ious components interact and any product functionalities or environmental setting on which it relies 必须
        disclosed. All related source code, scripts and 配置 files 必须 reported in the supporting files archive.
        The information provided 应 be sufficient for an independent reconstruction of the 实现 specific

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 114
         layer.

8.3.9.3 If profile-directed 优化 as described in Clause 5.2.9 is used, such use 必须 disclosed. In particular, the
        procedure and any scripts used to perform the 优化 必须 reported in the supporting files archive.
8.3.10   Clause 9 - Audit Related Items

8.3.10.1 The auditor's agency name, address, phone number, and attestation letter with a brief 审计 summary report indicat-
         ing 合规 必须 included in the full disclosure report. A statement 应 be included specifying whom to
         contact in 订单 to obtain further information regarding the 审计 process.

8.4      Executive Summary
         The executive summary is meant to be a high level overview of a TPC-H 实现. It 应 provide the
         salient characteristics of a 基准测试 执行 (metrics, 配置, 定价, etc.) without the exhaustive detail
         found in the FDR. When the TPC-Energy optional reporting is selected by the test sponsor, the additional
         要求 and format of TPC-Energy related items in the executive summary are included in the TPC Energy
         Specification, located at www.tpc.org.
         The executive summary has three components:
         •        Implementation Overview
         •        Pricing Spreadsheet
         •        Numerical Quantities
8.4.1    Page Layout
         Each 组件 of the executive summary 应 appear on a page by itself. Each page 应 use a standard
         header and format, including
         •        1/2 inch margins, top and bottom;
         •        3/4 inch left margin, 1/2 inch right margin;
         •        2 pt. frame around the body of the page. All interior lines 应 be 1 pt.;
         •        Sponsor identification and System identification, each set apart by a 1 pt. 规则, in 16-20 pt. Times Bold
                  font;
         TPC-H, TPC-Pricing, TPC-Energy (if reported) with three tier versioning (e.g., 1.2.3), and report 日期, separated
                from other header items and each other by a 1 pt. Rule, in 9-12 pt. Times font.
         Comment 1: It is permissible to use or include company logos when identifying the sponsor.

         Comment 2: The report 日期 必须 disclosed with a precision of 1 day. The precise format is left to the test spon-
         sor.

         Comment : Appendix E contains a sample executive summary. It is meant to help clarify the 要求 in
         节 8.4 and is provided solely as an 示例.
8.4.2    Implementation Overview
         The 实现 overview page contains six sets of data, each laid out across the page as a sequence of boxes
         using 1 pt. 规则, with a title above the required 数量. Both titles and quantities 应 use a 9-12 pt. Times font
         unless otherwise noted.

8.4.2.1 The first 节 contains the results that were obtained from the reported run of the Performance test.


                                           Table 13: Implementation Overview Information


 Title                          Quantity                           Precision     Units                   Font




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 115
 Total System Cost              3 yr. Cost of ownership (see     1              $1                          16-20 pt. Bold
                                Clause 7: )

 TPC-H Composite Query          QphH (see Clause 5.4.3)          0.1            QphH@nGB                    16-20 pt. Bold
 per Hour Metric

 Price/Performance              $/kQphH (see Clause 5.4.4)       1              $/kQphH@nGB                 16-20 pt. Bold



8.4.2.2 The next 节 details the 系统 配置


                                            Table 14: System Configuration Information


 Title                          Quantity                         Precision           Units                     Font

 Database Size                  Raw data size of test 数据库   1                   GB                        9-12 pt. Times
                                (see Clause 4.1.3 and Clause
                                                                                     (see Clause 8.3.7.7)
                                8.3.7.7)

 DBMS Manager                   Brand, Software Version of                                                     9-12 pt. Times
                                DBMS used

 Operating System               Brand, Software Version of                                                     9-12 pt. Times
                                OS used

 Other Software                 Brand, Software Version of                                                     9-12 pt. Times
                                other 软件 components

 System Availability Date       The Availability Date of the     1 day                                         9-12 pt. Times
                                系统, defined in Clause 0 of
                                the TPC Pricing Specification.


         Comment: The Software Version must uniquely identify the orderable 软件 product referenced in the Priced
         Configuration (e.g., RALF/2000 4.2.1)

8.4.2.3 This 节 is the largest in the 实现 overview, and contains a graphic representation of the reported
        查询 times. Each 查询 and 刷新函数 executed during the 基准测试 应 be listed in the graph, with any
        查询 variants clearly identified. In addition:
         •        All labels and scales must use a 10 point Courier font, except for the legend and the graph title which must
                  use a Times font;
         •        All line sizes 必须 1 point;
         •        The legend 必须 reproduced as depicted in the 示例, and 必须 placed where needed to avoid
                  overlapping any portion of the graph;
         •        The 查询 time axis must labeled with no more than 8 值, including the zero origin;
         •        Each pair of bars 必须 separated by a gap of 50% of the bar's width;
         •        A zero-based linear scale 必须 used for the 查询 times;
         •        The upper bound of the time scale 必须 no greater than 120% of the longest 查询 timing interval;
         •        The bars used for the power test 必须 sized based on the measured (i.e., without the adjustment defined
                  in Clause 5.4.1.4) 查询 timing intervals of the power test, and 必须 solid white;



         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                        Page 116
         •       The bars used for the 吞吐量 test 必须 sized based on the arithmetic mean by 查询 type of the mea-
                 sured 查询 timing intervals of the 吞吐量 test, and 必须 solid black;
         •       The geometric mean of the power test components 必须 computed using unadjusted timings of queries
                 and 刷新 functions and 必须 placed on the graph as a dashed line labeled on top with its 值. It must
                 be expressed using the same format and precision as TPC-H Power specified in Clause 5: ;
         •       The arithmetic mean of the 吞吐量 test 必须 calculated using unadjusted timings with the following
                 computation:




                 where QI(i,s) is defined in Clause 5.3.7.2, and S is defined in Clause 5.1.2.3;
         •       A solid line representing the mean 必须 placed on the graph intersecting only the queries and 必须
                 labeled on top with its 值. The arithmetic mean of the 吞吐量 test 必须 expressed with the same
                 format and precision as TPC-H Throughput specified in Clause 5: ;
         •       All 查询 numbers 必须 followed by a variant letter when a variant was used in the tests.

8.4.2.4 This 节 contains the 数据库 load and sizing information


         Table 15: Database Load and Sizing Information


 Title                         Quantity                           Precision        Units                Font

 Database Load Time            Load Time (see Clause 4.3)         1 sec.           hh:mm:ss             9-12 pt. Times

 Total Disk/Database Size      Data Storage       Ratio    (see   0.01                                  9-12 pt. Times
                               Clause 8.3.7.7)
                                                                                                        9-12 pt. Times
                               Size Percentage (see Clause
 Memory/Database Size                                             0.1
                               8.3.7.10)
 Percentage


 Load includes backup          Y/N (see Clause 4.3.6)             N/A              N/A                  9-12 pt. Times

 Data Redundancy               Y/N (see Clause 8.3.7.4)           N/A              N/A                  9-12 pt. Times
 mechanisms used for (Base
 表 only)

 Data Redundancy               Y/N (see Clause 8.3.7.4)           N/A              N/A                  9-12 pt. Times
 mechanisms used for
 (Base 表 and auxiliary
 data structures)

 Data         Redundancy       Y/N (see Clause 8.3.7.4)           N/A              N/A                  9-12 pt. Times
 mechanisms    used   for
 (Everything)

         Data Redundancy Level (See Clause 8.3.7.4)        N/A N/A 9-12 pt. Times Bold
         Base Tables [0..3] (See Clause 8.3.7.4)          N/A N/A 9-12 pt. Times
         Auxiliary Structures [0..3] (See Clause 8.3.7.4) N/A N/A 9-12 pt. Times
         DBMS Temporary Space [0..3] (See Clause 8.3.7.4)      N/A N/A 9-12 pt. Times
         OS and DBMS Software[0..3] (See Clause 8.3.7.4)      N/A N/A 9-12 pt. Times

         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 117
8.4.2.5 The next 节 of the Implementation Overview 应 contain a synopsis of the SUT's major 系统 components,
        including
        •          total number of nodes used/total number of processors used with their types and speeds in GHz/ total
                   number of cores used/total number of threads used;
        •          Main and cache memory sizes;
        •          Network and I/O connectivity;
        •          Disk 数量 and geometry.
        If the 实现 used a two-tier architecture, front-end and back-end 系统 应 be detailed separately.

8.4.2.5.1 The term "main memory" as referenced in Clause 8.4.2.5 refers to the memory of the host 系统 or server / client
components of the SUT in Clause 6.2.1 that perform 数据库 and 查询 logic processing. The main memory size to be
disclosed in Clause 8.4.2.5 is the amount of memory that is directly addressable by the processors/cores/threads of each
组件 and accessible to store data or instructions.

8.4.2.6 The final 节 of the 实现 Overview 应 contain a 注 stating:
        “Database Size includes only raw data (e.g., no temp, 索引, redundant storage space, etc.).”
8.4.3   Pricing Spreadsheet

        The major categories in the Price Spreadsheet, as appropriate, are:
        •          Server Hardware
        •          Server Storage
        •          Server Software
        Discounts (可 optionally be included with above major category subtotal calculations)t.
8.4.4   Numerical Quantities Summary
        The Numerical Quantities Summary page contains three sets of data, presented in tabular form, detailing the execu-
        tion timings for the reported 执行 of the 性能 test. Each set of data 应 be headed by its given title
        and clearly separated from the other 表.

8.4.4.1 The first 节 contains measurement results from the 基准测试 执行.
        Section Title: Measurement Results


                                     Item Title                                          Precision               注

            Database Scale Factor                                             1

            Total Data Storage/Database Size                                  0.01

            Start of Database Load                                            yyyy-mm-dd hh:mm:ss

            End of Database Load                                              yyyy-mm-dd hh:mm:ss

            Database Load Time                                                hh:mm:ss

            Query Streams for Throughput Test                                 1

            TPC-H Power                                                       0.1

            TPC-H Throughput                                                  0.1

            TPC-H Composite Query-per-Hour Metric (QphH@Size)                 0.1



        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 118
                                    Item Title                                         Precision                    注

          Total System Price Over 3 Years                                   $1                                (1)

          TPC-H Price Performance Metric ($/kQphH@Size)                     $0.01                             (1)

        (1) depending on the currency used for publication this sign has to be exchanged with the ISO currency symbol

8.4.4.2 The second 节 contains 查询 and 查询 stream timing information.
        Section Title: Measurement Intervals

                                    Item Title                                         Precision                    注

          Measurement Interval in Throughput Test (Ts)                      0.01 second

          Duration of Stream Execution                                      0.01 second                       (1)

          Stream                                                            1

          Seed                                                              1

          Start Date/Time                                                   mm/dd/yy hh:mm:ss.ss

          End Date/Time                                                     mm/dd/yy hh:mm:ss.ss

          Total Time                                                        hh:mm:ss

          Refresh Start Date/Time                                           mm/dd/yy hh:mm:ss.ss

          Refresh End Date/Time                                             mm/dd/yy hh:mm:ss.ss

         (1) The remaining items in this 节 应 be reported as a sub-表, with one entry for each stream executed
        during the 性能 test.

8.4.4.3 The final 节, titled Timing Intervals (in Sec.) contains individual 查询 and 刷新函数 timings. The data
        应 be presented as a 表 with one entry for each 查询 stream executed during the Performance Test. For each
        stream entry, the total 耗时 for each 查询 in the stream and for its associated 刷新 functions 应 be
        reported separately to a resolution of 0.01 seconds. In addition, the minimum, maximum and average 执行 time
        for each 查询 and 刷新函数 必须 reported to a resolution of 0.01 seconds.

8.5     Availability of the Full Disclosure Report and Supporting Files Archive

8.5.1   The full disclosure report and supporting files archive 必须 readily available to the public at a reasonable charge,
        similar to charges for comparable documents by that test sponsor. The report and supporting files archive 必须
        made available when results are made public. In 订单 to use the phrase “TPC Benchmark H”, the full disclosure
        report and supporting files archive must have been submitted electronically to the TPC using the procedure
        described in the TPC Policies and Guidelines document.
8.5.2   The official full disclosure report 必须 available in English but 可 be translated to additional languages.

8.6     Revisions to the Full Disclosure Report and Supporting Files Archive

        Revisions to the full disclosure documentation and supporting files archive 应 be handled as follows:



        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 119
8.6.1   Substitutions will be open to challenge for a 60 day period. No other portion of the FDR and supporting files archive
        are challengeable.
8.6.2   During the normal product life cycle, problems will be uncovered that require changes, sometimes referred to as
        ECOs, FCOs, patches, updates, etc. When the cumulative 结果 of applied changes causes the QphH rating of the
        系统 to decrease by more than 2% from the initially reported QphH, then the test sponsor is required to re-validate
        the 基准测试 results. The complete revision history is maintained following the 查询 timing interval 节
        showing the revision 日期 and 说明.
8.6.3   Full disclosure report and supporting files archive revisions 可 be required for other reasons according to TPC
        policies (see TPC Policy Document)




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 120
                                                         9: AUDIT
         Rules for auditing 定价 information are included in the current revision of the TPC Pricing Specification located
         at www.tpc.org. When the TPC-Energy optional reporting is selected by the test sponsor, the 规则 for auditing of
         TPC-Energy related items are included in the current revision of the TPC Energy Specification located at
         www.tpc.org.


9.1      General Rules

9.1.1    An independent 审计 of the 基准测试 results by a TPC certified auditor is required. The term independent is
         defined as “the outcome of the 基准测试 carries no financial benefit to the auditing agency other than fees earned
         directly related to the 审计.” In addition, the auditing agency cannot have supplied any 性能 consulting
         under contract for the 基准测试.

         In addition, the following conditions 必须 met:

          a)    The auditing agency cannot be financially related to the sponsor. For 示例, the auditing agency is finan-
                cially related if it is a dependent division of the sponsor, the majority of its stock is owned by the sponsor,
                etc.

          b)    The auditing agency cannot be financially related to any one of the suppliers of the measured/priced configu-
                ration, e.g., the DBMS 供应商, the disk 供应商, etc.
9.1.2    The auditor's attestation letter is to be made readily available to the public as 零件 of the full disclosure report. A
         detailed report from the auditor is not required.
9.1.3    TPC-H results can be used as the basis for new TPC-H results if and only if:

          a)    The auditor ensures that the 硬件 and 软件 products are the same as those used in the prior 结果;

          b)    The auditor reviews the FDR of the new results and ensures that they match what is contained in the original
                sponsor's FDR;

          c)    The auditor can attest to the validity of the 定价 used in the new FDR.

         Comment 1: The intent of this 子句 is to allow a reseller of equipment from a given 供应商 to publish under the
         re-seller's name a TPC-H 结果 already published by the 供应商.

         Comment 2: In the event that all conditions listed in Clause 9.1.3 are met, the auditor is not required to follow the
         remaining auditor's check list items from Clause 9.2.
9.1.4    Ensure that any auxiliary data structures satisfy the 要求 of Clause 1.5.6.
9.1.5    In the event that a remote 审计 procedure is used in the context of a change-based 审计, a remote connection to the
         SUT 必须 available for the auditor to verify selected 审计 items from Clause 9.2.

9.2      Auditor's Check List

9.2.1    Clause 1 Related Items

9.2.1.1 Verify that the data types used for each 列 are conformant. For 示例, verify that decimal 列 can be
        incremented by 0.01 from -9,999,999,999.99.

9.2.1.2 Verify that the 表 have the required list of 列.

9.2.1.3 Verify that the 实现 规则 are met by the test 数据库.

9.2.1.4 Verify that the test 数据库 meets the data access transparency 要求.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 121
9.2.1.5 Verify that conforming arbitrary data 值 can be inserted into any of the 表. Examples of verification tests
        include:
         •        Inserting a 行 that is a complete duplicate of an existing 行 except for a distinct ‘Primary Key’ 值 ;
         •        Inserting a 行 with 列 值 within the domain of the data type and check constraints but beyond the
                  range of existing 值.

9.2.1.6 Verify that the set of auxiliary data structures (as defined in Clause 1.5.7) that exist at the end of the load test are the
        same as those which exist at the end of the 性能 test. A similar check 可 be performed at any point during
        the 性能 test at the discretion of the auditor.

         Comment: The purpose of this check is to verify that no auxiliary data structures automatically generated during the
         性能 test 可 be accessed by more than one 查询 执行.

9.2.2    Clause 2 Related Items

9.2.2.1 Verify that the basis for the SQL used for each 查询 is either the functional 查询 定义 or an approved variant.

9.2.2.2 Verify that all SQL features used for each 查询, 刷新 functions, 数据库 loading, indexing and verification
        scripts are externally documented.

9.2.2.3 Verify that any deviation in the SQL from either the functional 查询 定义 or an approved variant is compliant
        with the specified minor 查询 modifications. Verify that minor 查询 modifications have been applied consistently
        to the set of functional 查询 definitions or approved variants used.

9.2.2.4 Verify that the executable 查询 text produces the required 输出 when executed against the qualification 数据库
        using the validation 值 for substitution parameters.

9.2.2.5 Note the version number, release number, modification number and patch level of QGen. Verify that the version
        and release numbers match the 基准测试 规范.

9.2.2.6 Verify that the generated substitution parameters are reasonably diverse among the streams.

9.2.2.7 Verify that no aspect of the 系统 under test, except for the 数据库 size, has changed between the demonstration
        of 合规 against the qualification 数据库 and the 执行 of the reported measurements.

9.2.2.8 Verify that the 刷新 functions are implemented according to their 定义.

9.2.2.9 Verify that the 事务 要求 are met by the 实现 of the 刷新 functions.

9.2.2.10 Note the method used to execute 数据库 维护 operations

9.2.2.11 Verify that the 输出 of the validation run (Clause 2.3.1) matches the 输出 supplied in Appendix C.


9.2.3    Clause 3 Related Items

9.2.3.1 Verify that the required ACID properties are supported by the 系统 under test as configured for the 执行 of
        the reported measurements.

9.2.3.2 If one or more of the ACID tests defined in Clause 3:           were not executed, 注 the rationale for waiving such
        demonstration of support of the related ACID property.

9.2.3.3 Verify that SUT Power Failure has been tested as required by Clause 3.5.3 .


9.2.4    Clause 4 Related Items


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                          Page 122
9.2.4.1 Verify that the qualification 数据库 is properly scaled and populated.

9.2.4.2 Verify that the test 数据库 is properly scaled.

9.2.4.3 Verify that the 行 in the loaded 数据库 after the 性能 test are correct by comparing any two files of the
        corresponding Base, Insert and Delete reference data set files for each 表 against the corresponding 行 of the
        数据库.
        Comment: Due to a known anomaly in the data generator dbgen, at scale factors 30000
        and 100000, the content of 列 L_PARTKEY, L_SUPPKEY and L_EXTENDEDPRICE do
        not need to match those in the reference data set.

9.2.4.4 Verify that the DBGen (using the command lines provided in Appendix F) used in the 基准测试 generates a data
        set which matches the reference data set provided in Appendix F corresponding to the 规模因子 used in this
        基准测试.

9.2.4.5 Verify referential integrity in the 数据库 after the initial load.

9.2.4.6 Verify that the qualification and test databases were constructed in the same manner so that correct behavior on the
        qualification 数据库 is indicative of correct behavior on the test 数据库.

9.2.4.7 Note the version number, release number, modification number and patch level of DBGen. Verify that the version
        and the release numbers match the 基准测试 规范.

9.2.4.8 Verify that storage and processing elements that are not included in the priced 配置 are physically removed
        or made inaccessible during the 性能 test.

9.2.4.9 Verify that the 数据库 load time is measured according to the 要求.
9.2.5    Clause 5 Related Items

9.2.5.1 Verify that the driver meets the 要求 of Clause 5.2 and Clause 6.3.

9.2.5.2 Verify that the 执行 规则 are followed for the power test.

9.2.5.3 Verify that the queries are executed against the test 数据库.

9.2.5.4 Verify that the 执行 规则 are followed for the 吞吐量 test.

9.2.5.5 Verify that a single stream is used for 刷新 functions in the 吞吐量 test and that the required number of 刷新
        function pairs is executed according to the 执行 规则.

9.2.5.6 Verify that the 查询 sequencing 规则 are followed.

9.2.5.7 Verify that the measurement interval for the 吞吐量 test is measured as required.

9.2.5.8 Verify that the method used to measure the timing intervals is compliant.

9.2.5.9 Verify that the metrics are computed as required. Note whether Clause 5.4.1.4 concerning the ratio between the lon-
        gest and the shortest timing intervals had to be applied.

9.2.5.10 Verify that the reported metrics are repeatable.
9.2.6    Clause 6 Related Items

9.2.6.1 Verify that the composition of the SUT is compliant and that its components will be commercially available soft-
        ware or 硬件 products according to 子句 7 of the Pricing Specification.

9.2.6.2 Note whether an 实现 specific layer is used and verify its 合规 with Clause 6.2.4.


         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 123
9.2.6.3 Verify that the driver's 实现 is compliant.

9.2.6.4 Verify that any profile-directed 优化 performed by the test sponsor conforms to the 要求 of Clause
        5.2.9.
9.2.7    Clause 8 Related Items

9.2.7.1 Verify that major portions of the full disclosure report are accurate and comply with the reporting 要求. This
        includes:
         •        The executive summary;
         •        The numerical 数量 summary;
         •        The diagrams of both measured and priced configurations;
         •        The block diagram illustrating the 数据库 load process.




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 124
                                          10: GLOBAL DEFINITIONS
E ___________________________
Externally Documented means that the documentation is available to any 客户 who has purchased the SUT, i.e. no
additional condition such as a Non Disclosure Agreement (NDA) is required.

F ___________________________

Foreign Key

A Foreign Key (Foreign Key Constraint) is a 列 or combination of 列 used to establish and enforce a link
between the data in two 表. A link is created between two 表 by adding the 列 or 列 that hold one 表's
Primary Key 值 to the other 表. This 列 becomes a Foreign Key in the second 表. May also be referred to as
a 外键 约束.


P____________________________

Primary Key
A Primary Key (Primary Key Constraint) is one or more 列 that uniquely identifies a 行. None of the 列 that
are 零件 of the Primary Key 可 be nullable. A 表 must have no more than one Primary Key.



R ___________________________

Referential Integrity
Referential Integrity is a data property whereby a Foreign Key in one 表 has a corresponding Primary key in a different
表.

round(x,m)
Rounding a number x to a decimal precision of m is defined as:
    1)     x+5*power(10,-m-1), call it y
    2)     y*power(10,m), call it z
    3)     truncate z to an integer 值, call it q;
    4)     q/power(10,m) to obtain the rounded 值.

 Rounding Examples
   •     round(45.897,1)
         y=45.897+0.05=45.947
         z=459.47
         q=459
         z=45.9

    •      round(45.213,1)
           y=45.213+0.05=45.263
           z=452.63
           q=452
           z=45.2

    •      round(45.897,0)
           y=45.897+0.5=46.397
           z=46.397
           q=46
           z=46



        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                  Page 125
                                Appendix A: ORDERED SETS
Following are the ordered sets that 必须 used for sequencing 查询 执行 as described in Clause 5.3.5. They
are adapted from Moses and Oakford, Tables of Random Permutations, Stanford University Press, 1963. pp. 52-53.
         1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
  Power Test
  0      14 2 9 20 6 17 18 8 21 13 3 22 16 4 11 15 1 10 19 5 7 12
  Throughput Test
  1      21 3 18 5 11 7 6 20 17 12 16 15 13 10 2 8 14 19 9 22 1 4
  2      6 17 14 16 19 10 9 2 15 8 5 22 12 7 13 18 1 4 20 3 11 21
  3      8 5 4 6 17 7 1 18 22 14 9 10 15 11 20 2 21 19 13 16 12 3
  4      5 21 14 19 15 17 12 6 4 9 8 16 11 2 10 18 1 13 7 22 3 20
  5      21 15 4 6 7 16 19 18 14 22 11 13 3 1 2 5 8 20 12 17 10 9
  6      10 3 15 13 6 8 9 7 4 11 22 18 12 1 5 16 2 14 19 20 17 21
  7      18 8 20 21 2 4 22 17 1 11 9 19 3 13 5 7 10 16 6 14 15 12
  8      19 1 15 17 5 8 9 12 14 7 4 3 20 16 6 22 10 13 2 21 18 11
  9      8 13 2 20 17 3 6 21 18 11 19 10 15 4 22 1 7 12 9 14 5 16
  10     6 15 18 17 12 1 7 2 22 13 21 10 14 9 3 16 20 19 11 4 8 5
  11     15 14 18 17 10 20 16 11 1 8 4 22 5 12 3 9 21 2 13 6 19 7
  12     1 7 16 17 18 22 12 6 8 9 11 4 2 5 20 21 13 10 19 3 14 15
  13     21 17 7 3 1 10 12 22 9 16 6 11 2 4 5 14 8 20 13 18 15 19
  14     2 9 5 4 18 1 20 15 16 17 7 21 13 14 19 8 22 11 10 3 12 6
  15     16 9 17 8 14 11 10 12 6 21 7 3 15 5 22 20 1 13 19 2 4 18
  16     1 3 6 5 2 16 14 22 17 20 4 9 10 11 15 8 12 19 18 13 7 21
  17     3 16 5 11 21 9 2 15 10 18 17 7 8 19 14 13 1 4 22 20 6 12
  18     14 4 13 5 21 11 8 6 3 17 2 20 1 19 10 9 12 18 15 7 22 16
  19     4 12 22 14 5 15 16 2 8 10 17 9 21 7 3 6 13 18 11 20 19 1
  20     16 15 14 13 4 22 18 19 7 1 12 17 5 10 20 3 9 21 11 2 6 8
  21     20 14 21 12 15 17 4 19 13 10 11 1 16 5 18 7 8 22 9 6 3 2
  22     16 14 13 2 21 10 11 4 1 22 18 12 19 5 7 8 6 3 15 20 9 17
  23     18 15 9 14 12 2 8 11 22 21 16 1 6 17 5 10 19 4 20 13 3 7
  24     7 3 10 14 13 21 18 6 20 4 9 8 22 15 2 1 5 12 19 17 11 16
  25     18 1 13 7 16 10 14 2 19 5 21 11 22 15 8 17 20 3 4 12 6 9
  26     13 2 22 5 11 21 20 14 7 10 4 9 19 18 6 3 1 8 15 12 17 16
  27     14 17 21 8 2 9 6 4 5 13 22 7 15 3 1 18 16 11 10 12 20 19
  28     10 22 1 12 13 18 21 20 2 14 16 7 15 3 4 17 5 19 6 8 9 11
  29     10 8 9 18 12 6 1 5 20 11 17 22 16 3 13 2 15 21 14 19 7 4
  30     7 17 22 5 3 10 13 18 9 1 14 15 21 19 16 12 8 6 11 20 4 2
  31     2 9 21 3 4 7 1 11 16 5 20 19 18 8 17 13 10 12 15 6 14 22
  32     15 12 8 4 22 13 16 17 18 3 7 5 6 1 9 11 21 10 14 20 19 2
  33     15 16 2 11 17 7 5 14 20 4 21 3 10 9 12 8 13 6 18 19 22 1
  34     1 13 11 3 4 21 6 14 15 22 18 9 7 5 10 20 12 16 17 8 19 2
  35     14 17 22 20 8 16 5 10 1 13 2 21 12 9 4 18 3 7 6 19 15 11
  36     9 17 7 4 5 13 21 18 11 3 22 1 6 16 20 14 15 10 8 2 12 19
  37     13 14 5 22 19 11 9 6 18 15 8 10 7 4 17 16 3 1 12 2 21 20
  38     20 5 4 14 11 1 6 16 8 22 7 3 2 12 21 19 17 13 10 15 18 9
  39     3 7 14 15 6 5 21 20 18 10 4 16 19 1 13 9 8 17 11 12 22 2
  40     13 15 17 1 22 11 3 4 7 20 14 21 9 8 2 18 16 6 10 12 5 19




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                 Page 126
                           Appendix B: APPROVED QUERY VARIANTS

     Following are the approved TPC-H 查询 variants as of the publication 日期 of this version of the 规范. As
     new 查询 variants 可 be approved on an on-going basis, implementers are encouraged to obtain a copy of the lat-
     est list of approved 查询 variants from the TPC office (see cover page for coordinates).

     Some 查询 variants include statements that create temporary 表. In these statements, 列 data types are des-
     ignated in angle brackets (e.g., <Integer>) and refer to the list of data types specified in Clause 1.3.1.

     - This appendix is also available in machine readable format -

     To obtain a copy of the machine-readable appendices, please contact the TPC (see cover page).


Q8
     Variant A (approved 11-Feb-1998)
     This variant replaces the CASE statement from the Functional Query Definition with equivalent DECODE() syntax.
     The justification for this variant was Clause 2.2.4.3 (d)), which allows for vendor-specific syntax that, while not
     SQL-92, provides a simple and direct mapping to approved SQL-92 syntax.

     select
              o_year,
              sum(decode(国家, ‘[NATION]’, volume, 0)) / sum(volume) as mkt_share
     from
              (
                       select
                                extract(year from o_orderdate) as o_year,
                                l_extendedprice * (1 - l_折扣) as volume,
                                n2.n_name as 国家
                       from
                                零件,
                                供应商,
                                行项,
                                orders,
                                客户,
                                国家 n1,
                                国家 n2,
                                地区
                       where
                                p_partkey = l_partkey
                                and s_suppkey = l_suppkey
                                and l_orderkey = o_orderkey
                                and o_custkey = c_custkey
                                and c_nationkey = n1.n_nationkey
                                and n1.n_regionkey = r_regionkey
                                and r_name = '[REGION]'
                                and s_nationkey = n2.n_nationkey
                                and o_orderdate between 日期 '1995-01-01' and 日期 '1996-12-31'
                                and p_type = '[TYPE]’




     TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                   Page 127
                 ) all_nations
      group by
                 o_year
      订单 by
                 o_year;


Q12
      Variant A (approved 11-Feb-1998)
      This variant replaces the CASE statement from the Functional Query Definition with equivalent DECODE() syntax.
      The justification for this variant was Clause 2.2.4.3 (d), which allows for vendor-specific syntax that, while not
      SQL-92, provides a simple and direct mapping to approved SQL-92 syntax.

      select
                 l_shipmode,
                 sum(decode(o_orderpriority, '1-URGENT', 1, '2-HIGH', 1, 0)) as
                         high_line_count,
                 sum(decode(o_orderpriority, '1-URGENT', 0, '2-HIGH', 0, 1)) as
                         low_line_count
      from
                 orders,
                 行项
      where
                 o_orderkey = l_orderkey
                 and l_shipmode in ('[SHIPMODE1]', '[SHIPMODE2]')
                 and l_commitdate < l_receiptdate
                 and l_shipdate < l_commitdate
                 and l_receiptdate >= 日期 '[DATE]'
                 and l_receiptdate < 日期 '[DATE]' + interval '1' year
      group by
                 l_shipmode
      订单 by
                 l_shipmode;


Q13
      Variant A (approved 5 March 1998)

      This variant was required by a vendor which did not support two aggregates in a nested 表 expression.

      create view orders_per_cust[STREAM_ID] (custkey, ordercount) as
               select
                        c_custkey,
                        count(o_orderkey)
               from
                        客户 left outer 连接 orders on
                                c_custkey = o_custkey
                        and o_comment not like '%[WORD1]%[WORD2]%'
               group by
                        c_custkey;

      select




      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                    Page 128
                 ordercount,
                 count(*) as custdist
      from
                 orders_per_cust[STREAM_ID]
      group by
                 ordercount
      订单 by
                 custdist desc,
                 ordercount desc;

      drop view orders_per_cust[STREAM_ID];


Q14
      Variant A (approved 5 March 1998)

      This variant replaces the CASE statement with the equivalent DECODE() syntax.

      select
                 100.00 * sum(decode(substring(p_type from 1 for 5), 'PROMO',
                         l_extendedprice * (1-l_折扣), 0)) /
                                 sum(l_extendedprice * (1-l_折扣)) as promo_收入
      from
                 行项,
                 零件
      where
                 l_partkey = p_partkey
                 and l_shipdate >= 日期 '[DATE]'
                 and l_shipdate < 日期 '[DATE]' + interval '1' month;


Q15
      Variant A (approved 11-Feb-1998)
      This variant was approved because it contains new SQL syntax that is relevant to the 基准测试. The SQL3 stan-
      dard, which was moved to an Approved Committee Draft in May 1996, contains the 定义 of common 表
      expressions. TPC-H already makes extensive use of nested 表 expressions. Common 表 expressions can be
      thought of as shared 表 expressions or "inline views" that last only for the duration of the 查询.

      with 收入 (供应商_no, total_收入) as (
               select
                        l_suppkey,
                        sum(l_extendedprice * (1-l_折扣))
               from
                        行项
               where
                        l_shipdate >= 日期 '[DATE]'
                        and l_shipdate < 日期 '[DATE]' + interval '3' month
               group by
                        l_suppkey




      TPC BenchmarkTM H Standard Specification Revision 3.0.1                                              Page 129
)
select
           s_suppkey,
           s_name,
           s_address,
           s_phone,
           total_收入
from
           供应商,
           收入
where
           s_suppkey = 供应商_no
           and total_收入 = (
                    select
                            max(total_收入)
                    from
                            收入
           )
订单 by
           s_suppkey;




TPC BenchmarkTM H Standard Specification Revision 3.0.1   Page 130
                             Appendix C: QUERY VALIDATION

This appendix contains the 输出 data for validation of executable 查询 text against the qualification 数据库.

- This appendix is available in machine-readable format only -

To obtain a copy of the machine-readable appendices, please contact the TPC (see Cover page).




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                      Page 131
           Appendix D: DATA AND QUERY GENERATION PROGRAMS

The QGEN (see Clause 2.1.4) and DBGEN (see Clause 4.2.1) programs 应 be used to generate the executable
查询 text and the data that populate the TPC-H Databases. These programs produce flat files that can be used by the
test sponsor to 实现 the 基准测试.

- This appendix is available in machine readable format only -

To obtain a copy of the machine readable appendices, please contact the TPC (see Cover page).




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                   Page 132
                     Appendix E: SAMPLE EXECUTIVE SUMMARY

This appendix includes a sample Executive Summary.

See Clause 8.4 for a detailed 说明 of the required format of the Executive Summary. This sample is
provided only as an illustration of the 要求 set forth in Clause 8.4 of the 规范. In the event of a
conflict between this 示例 and the 规范, the 规范 应 prevail.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 133
                                                                                                                 TPC-H Rev. 2.14.3
                                                                                                                TPC-H
                                                                                                               TPC      Rev.Rev.
                                                                                                                    Pricing  2.18.0
                                                                                                                                  1.6.0
           My Logo                                      My System                                             TPC Pricing  Rev.  1.6.0
    My Logo                                        My System                                                 Report
                                                                                                                    Report Date:
                                                                                                                     Date: 11-Nov-18
                                                                                                                November     11, 2011
         Total System Cost                     Composite Query perHour Metric                                  Revised:   24-Dec-18
                                                                                                                Price/Performance
     Total System Cost                       Composite Query per Hour Metric                                      Price/Performance

    $31,322 USD                                        123,543.20                                                $0.26 USD
                                                                                                                         USD
  $31,322 USD                                        123,543.20
                                                       QphH@1000GB
                                                                                                                $0.26
                                                                                                               Price/QphH@1000GB
                                                 QphH@1000GB                                               Price/kQphH@1000GB
           Database Size               Database Manager    Operating System                            Other Software Availability Date
       Database Size                  Database Manager                Operating System             Other Software           Availability Date

        1000
      1000   GB*
           GB*                      MyDatabase
                                    My Database                           My
                                                                         My OSOS                        n/a n/a             4/11/2012
                                                                                                                            4/11/2018




Database Load Time:
                            Load Includes Backup: N           Memory Ratio: 60%                Total Data Storage/Database Size: 4
     02:34:12Load Time: 02:34:12
     Database                        Load Includes Backup: N        Memory Ratio: 60%            Total Data Storage/Database Size: 4
   StorageStorage
           Redundancy   Level:Level:
                  Redundancy    3 3         Base Base
                                                  Table: RAID-10
                                                      Table: RAID-10 Auxiliary Data Structures:
                                                                            Auxiliary             RAID-10
                                                                                      Data Structures: RAID-10      Other:
                                                                                                                     Other: RAID-10
                                                                                                                            RAID-10
     System
System       Configuration
       Configuration
    NumberNumber  of Nodes:
             of Nodes:                       11
          Processor/Cores/Treads/Type:
    Processor/Cores/Treads/Type:              4/16/32myCPU
                                             4/16/32   myCPU2.0GHz,
                                                               2.0GHz,3MB
                                                                       3MBL3L3cache
                                                                               cacheper
                                                                                     percore
                                                                                         core
          Memory:                             384 GB
    Memory:                                  384 GB
          Disk Drives:                        2 Storage Arrays, each with 10 x 180GB 15Krpm SATA Disks
    Disk Drives:                             24Storage
                                                x 100GBArrays, each
                                                         Internal   with 10
                                                                  15Krpm    x 180GB
                                                                          SAS Disks 15Krpm SATA Disks
          Total Disk Storage:                44,000GB
                                               x 100GB Internal 15Krpm SAS Disks
    Total Lan
          DiskControllers
               Storage:                       1 x 100Mb PCI LAN card
                                             4,000GB
    LAN Controllers                          1 x 100Mb PCI LAN card
                             * Database Size includes only raw data (e.g., no temp, 索引, redundant storage space, etc.)
                          * Database Size includes only raw data (e.g., no temp, 索引, redundant storage space, etc.)




         TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                                          Page 134
                                                                                                                  TPC-H Rev. 2.18.0
                                                                                                                TPC Pricing Rev. 2.4.0
    My Logo                                              My System                                             Report Date: 11-Nov-18
                                                                                                                 Revised: 24-Dec-18
                                                                 Part                       Unit                   Extended     3 yr Maint.
   Description                                                                   Source                  Qty
                                                                Number                      Price                    Price         Price

  Server Hardware
    MyCo Server                                               abcd123456             1      12,000        1           12,000
    MyCo 4GB Reg PC3200 2X2GB Memory                          abcd123457             1         300        2              300
    100GB 15Krpm U320 SAS HDD                                 abcd123458             1         210        4              210
    MyCo Fiber Channel Adapter                                abcd123459             1         584        1              584
    MyCo Care Pack 3-year, 4-hour, 7x24                       abcd123410             1       1,234        1                               1,234
    MyCo rack                                                 abcd123411             1         500        1              500
    DiscntCo KB & Mouse                                         Dis2345              3          70        1              210
    DiscntCo 17in LCD                                           Dis2347              3         200        1              600
                                                                                                        Subtotal      14,404              1,234

  Server Software
    MyDB FastDBMS Core License                                   xyz432              2       4,100        16           8,200
    MyDB FastDBMS Support 4-hour, 7x24                           xyz433              2       1,700         3                              5,100
    MyDB MyUNIX Server                                           xyz123              2       1,500         1           3,000
                                                                                                        Subtotal      11,200              5,100

  Storage
    MyCo Storage Array                                          stqw876              1       3,000         1           3,000
    180GB 15Krpm SF SATA HDD                                    stqw871              1         410        20             410
    MyCo Array Care 3-year, 4-hour, 7x24                        stqw872              1         732         1                                732
    MyCo SAN Switch (inc. spare)                                stqw875              1       3,000         3           3,000
    MyCo Fiber Channel Cable (5m) (inc. spares)                 stqw873              1          72         3              72
                                                                                                        Subtotal       6,482                732

                                                                                                           Total      32,086               7,066
  Discount *                                                                                                          (6,417)            (1,413)

                                                                                                     Grand Total      25,669              5,653

* All discounts are based on US list prices and for similar quantities and configurations       3-year Cost of Ownership:          31,321.60
  Source: 1=MyCo, 2=MyDB, 3=DiscntCo                                                                     QphH@1000GB:             123,543.20
                                                                                                      $/kQphH@1000GB:                 253.53
  Audited by: John Smith for AuditorCo

        Prices used in TPC benchmarks reflect the actual prices a 客户 would pay for a one-time purchase of the stated
        components. Individually negotiated discounts are not permitted. Special prices based on assumptions about past or
        future purchases are not permitted. All discounts reflect standard 定价 policies for the listed components. For
        complete details, see the 定价 节 of the TPC 基准测试 specifications. If you find that the stated prices are not
        available according to these terms, please inform the TPC at 定价@tpc.org. Thank you.




             TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                                 Page 135
                                                                                             TPC-H Rev. 2.18.0
                                                                                           TPC Pricing Rev. 2.4.0
My Logo                                   My System                                       Report Date: 11-Nov-18
                                                                                            Revised: 24-Dec-18

Measurement Results
             Database Scaling (SF/Size)                                                                         1,000
             Total Data Storage/Database Size                                                                    8.78
             Percentage Memory/Database Size                                                                    102%
             Start of Database Load Time                                                          14/08/11 19:36:22
             End of Database Load Time                                                            15/08/11 16:40:41
             Database Load Time                                                                            21:04:19
             Query Streams for Throughput Test (S)                                                                  7
             TPC-H Power                                                                                  156,157.2
             TPC-H Throughput                                                                             115,188.0
             TPC-H Composite                                                                              123,543.2
             Total System Price Over 3 Years                                                              31,321.60
             TPC-H Price/Performance Metric ($/kQphH@1000GB)                                                 253.53

Measurement Interval
             Measurement Interval in Throughput Test (Ts)                                                  4,813.17

Duration of stream 执行:
                                Query Start Time      Duration       RF1 Start Time             RF2 Start Time
                 Seed
  Power                           Query End Time       (sec)         RF1 End Time                RF2 End Time
   Run                      08/15/2018 19:43:29.03               08/15/2018 19:42:48.04     08/15/2018 20:01:12.09
             0815164040                               1,063.01
                            08/15/2018 20:01:12.04               08/15/2018 19:43:29.01     08/15/2018 20:01:42.89


Throughput                      Query Start Time      Duration       RF1 Start Time             RF2 Start Time
                 Seed
  Stream                          Query End Time       (sec)         RF1 End Time                RF2 End Time
                            08/15/2018 20:01:43.01               08/15/2018 21:12:55.03     08/15/2018 21:13:51.58
    1        0815164041                               3,905.01
                            08/15/2018 21:06:47.02               08/15/2018 21:13:51.56     08/15/2018 21:14:22.12
                            08/15/2018 20:01:43.02               08/15/2018 21:14:22.15     08/15/2018 21:15:08.01
    2        0815164042                               4,119.07
                            08/15/2018 21:10:21.09               08/15/2018 21:15:07.98     08/15/2018 21:15:36.18
                            08/15/2018 20:01:43.02               08/15/2018 21:15:36.21     08/15/2018 21:16:18.92
    3        0815164043                               3,882.01
                            08/15/2018 21:06:25.03               08/15/2018 21:16:18.89     08/15/2018 21:16:47.99
                            08/15/2018 20:01:43.03               08/15/2018 21:16:48.02     08/15/2018 21:17:30.01
    4        0815164044                               4,135.00
                            08/15/2018 21:10:38.03               08/15/2018 21:17:29.92     08/15/2018 21:18:00.21
                            08/15/2018 20:01:43.03               08/15/2018 21:18:00.23     08/15/2018 21:18:40.57
    5        0815164045                               3,864.01
                            08/15/2018 21:06:07.04               08/15/2018 21:18:40.54     08/15/2018 21:19:12.93
                            08/15/2018 20:01:43.09               08/15/2018 21:19:13.02     08/15/2018 21:20:00.37
    6        0815164046                               4,271.80
                            08/15/2018 21:12:54.89               08/15/2018 21:20:00.34     08/15/2018 21:20:35.45
                            08/15/2018 20:01:43.10               08/15/2018 21:20:35.48     08/15/2018 21:21:22.36
    7        0815164047                               3,787.02
                            08/15/2018 21:04:50.12               08/15/2018 21:21:22.32     08/15/2018 21:21:55.22



                                                                                             TPC-H Rev. 2.18.0
My Logo                                   My System                                        TPC Pricing Rev. 2.4.0



    TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                         Page 136
                                                                                       Report Date: 11-Nov-18
                                                                                         Revised: 24-Dec-18



                                    TPC-H Timing Intervals (in seconds)

Duration of 查询 执行:
Stream ID      Q1      Q2     Q3        Q4      Q5     Q6      Q7        Q8      Q9      Q10      Q11     Q12
    0          69.14   1.91   15.69      8.07   9.28    1.08      1.45    1.88   16.22     1.18    9.38    5.19
    1          45.23   8.21   12.70     30.97   7.86    2.13      6.69   16.35   38.79     6.35   24.09   12.91
    2          60.74   7.26   11.82     45.27   9.42    2.37      5.61    9.08   40.41     6.67   19.48   42.78
    3          58.93   4.16   10.04     48.25   9.29    6.28   12.52      8.79   39.08     6.09   12.95   13.50
    4          51.93   9.16   14.32     37.25   8.67    7.73      6.36   12.12   65.42     7.84    3.98   10.38
    5          57.94   2.19   17.90     59.31   7.96    4.27   10.12      8.03   37.97     5.66   13.67   15.70
    6          97.31   2.35   10.31     36.49   8.03    2.62   15.00     10.31   49.06     5.27   46.69   17.81
    7          53.91   9.11   10.82     38.34   8.87    2.07      9.00    8.19   42.84     6.10   10.78    9.15
Minimum        45.23   1.91   10.04      8.30   1.88    1.08      1.45    1.88   16.22     1.18    3.98    5.19
Maximum        69.14   9.10   17.90     59.31   9.42    7.73   15.00     16.35   65.42     7.84   46.69   42.78
 Average      485.51   6.16   13.60     38.20   7.75    3.57      9.22    9.34   41.22     5.68   17.63   15.93


Stream ID      Q13     Q14    Q15      Q16      Q17    Q18     Q19       Q20     Q21     Q22      RF1     RF2
    0           4.67    .52     .52      1.85   1.20   15.17      1.85    1.19   27.43     1.34    4.12    2.96
    1          11.95   2.34    2.88      7.61   3.90   78.09   13.37      7.92   63.60     7.52    5.61    3.06
    2          19.39   3.72    3.51      9.50   8.21   77.46   13.34     10.29   36.32    15.54    4.50    2.84
    3          20.60   2.23    3.86      9.34   6.46   70.80      6.86   16.41   67.46     5.71    4.16    2.87
    4          19.83   2.20    4.34      7.98   5.82   91.97   12.47      7.47   67.86     6.51    4.17    2.99
    5          21.31   2.64    3.40      8.65   4.08   75.95      9.87   10.42   63.93    13.27    3.94    3.23
    6          27.95   2.14    4.20      9.17   7.45   87.26      8.14   11.24   32.06     6.88    4.68    3.49
    7          22.49   1.77    5.69     10.27   4.40   88.76      9.77   10.81   46.42     5.55    4.64    3.30
Minimum         4.67   0.52    0.52      1.85   1.20   15.17      1.85    1.19   27.43     1.34    3.94    2.84
Maximum        27.95   3.72    5.69     10.27   8.21   91.97   13.37     16.41   67.86    15.54    5.61    3.49
 Average       18.52   2.19    3.55      8.05   5.19   73.18      9.46    9.47   50.63     7.79    4.48    3.09




        TPC BenchmarkTM H Standard Specification Revision 3.0.1                                             Page 137
                            Appendix F: REFERENCE DATA SET

The content for this appendix is not included here. It can be obtained from the download 节 of the TPC web
site. It contains sample dbgen and qgen data (reference data set) and the command lines/scripts used to generate this
data by the TPC. The appendix contains the following datasets:

Base Data Set
The base data set contains sample data for all 表 at all scale factors. For each 规模因子 5 files of 表
行项, orders, 零件, partsupp, 客户 and 供应商 are included. For 表 国家 and 地区 all data is included
due to their limited size.

Insert Data Set
The insert data set contains sample data for 表 行项 and orders at all scale factors. For all scale factors and
each of the update sets 1, 75 and 150 100 files for 行项 and 100 files for orders are included.

Delete Data Set
The delete data set contains sample data for 表 行项 and orders at all scale factors. For each 规模因子 100,
300, 1000, 3000, 10000, 30000, 100000 and each of the update sets 1, 75 and 150 100 files are included. For scale
factor 1 and each of the update sets 1, 75 and 150 94 files are included.

Qgen Data Set
The qgen data set contains 150 files with 查询 substitutions 值 for all 22 queries for each 规模因子 as
generated with qgen. Each file uses a different seed.




TPC BenchmarkTM H Standard Specification Revision 3.0.1                                                       Page 138

