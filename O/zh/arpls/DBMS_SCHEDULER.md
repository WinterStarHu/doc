# DBMS_SCHEDULER

The `DBMS_SCHEDULER` package provides a collection of scheduling functions and procedures that can be called from any PL/SQL program.

> ⚠️ 机器翻译草稿：签名/代码保留原文，散文为短语级粗译，可能生硬。如需精译某过程请告知。

This chapter contains the following topics:
- Deprecated Subprograms
- Security Model
- Rules and Limits
- Operational Notes
- Data Structures
- Summary of DBMS_SCHEDULER Subprograms
参见：
Oracle Database Administrator's Guide for more information regarding how to use `DBMS_SCHEDULER`
### DBMS_SCHEDULER 已弃用的子程序
Oracle recommends that you do not use deprecated subprograms in new applications. Support for deprecated features is for backward compatibility only
The following subprograms are deprecated with Oracle Database 12c Release 1 (12.1):
- CREATE_CREDENTIAL Procedure
- DROP_CREDENTIAL Procedure
### DBMS_SCHEDULER 安全模型
The `DBMS_SCHEDULER` package ignores privileges granted on scheduler objects, such as jobs or chains, through roles. Object privileges must be granted directly to the user.
### DBMS_SCHEDULER 规则与限制
These rules apply when using the `DBMS_SCHEDULER` package.

- Only SYS can perform actions on objects in the SYS schema.

- Several of the procedures accept comma-delimited lists of object names. If you provide a list of names, then 调度器 stops executing the list at the first object that returns an error. Therefore, 调度器 does not perform the tasks needed for the remaining objects on the list. For example, consider the statement DBMS_SCHEDULER.STOP_JOB ('job1, job2, job3, sys.jobclass1, sys.jobclass2, sys.jobclass3'); If job3 cannot be stopped, then the jobs that follow it, jobclass1, jobclass2, and jobclass3 cannot be stopped. The jobs that preceded job3, job1 and job2, are stopped.
- Performing an action on an object that does not exist returns a PL/SQL exception stating that the object does not exist.
### DBMS_SCHEDULER 操作说明
调度器 uses a rich calendaring syntax to enable you to define repeating schedules, such as "every Tuesday and Friday at 4:00 p.m." or "the second Wednesday of every month." This calendaring syntax is used in 日历表达式s in the `repeat_interval` 参数 of a number of package subprograms. Evaluating a 日历表达式 results in a set of discrete timestamps.
See Oracle Database Administrator's Guide for examples of the calendaring syntax.
Calendaring Syntax
This section starts with the calendaring syntax. It is followed by descriptions of various parts of the syntax.
In the calendaring syntax, * means 0 or more.

repeat_interval = regular_schedule | combined_schedule
regular_schedule = frequency_clause
[";" interval_clause] [";" bymonth_clause] [";" byweekno_clause]
[";" byyearday_clause] [";" bydate_clause] [";" bymonthday_clause]
[";" byday_clause] [";" byhour_clause] [";" byminute_clause]
[";" bysecond_clause] [";" bysetpos_clause] [";" include_clause]
[";" exclude_clause] [";" intersect_clause][";" periods_clause]
[";" byperiod_clause]

frequency_clause = "FREQ" "=" ( predefined_frequency | user_defined_frequency )
predefined_frequency = "YEARLY" | "MONTHLY" | "WEEKLY" | "DAILY" |
   "HOURLY" | "MINUTELY" | "SECONDLY"
user_defined_frequency = named_schedule
interval_clause = "INTERVAL" "=" intervalnum
   intervalnum = 1 through 99
bymonth_clause = "BYMONTH" "=" monthlist
   monthlist = month ( "," month)*
   month = numeric_month | char_month
   numeric_month = 1 | 2 | 3 ...  12
   char_month = "JAN" | "FEB" | "MAR" | "APR" | "MAY" | "JUN" |
   "JUL" | "AUG" | "SEP" | "OCT" | "NOV" | "DEC"
byweekno_clause = "BYWEEKNO" "=" weeknumber_list
   weeknumber_list = weeknumber ( "," weeknumber)*
   weeknumber = [minus] weekno
   weekno = 1 through 53
byyearday_clause = "BYYEARDAY" "=" yearday_list
   yearday_list = yearday ( "," yearday)*
   yearday = [minus] yeardaynum
   yeardaynum = 1 through 366
bydate_clause = "BYDATE" "=" date_list
   date_list = date ( "," date)*
   date = [YYYY]MMDD [ offset | span ]
bymonthday_clause = "BYMONTHDAY" "=" monthday_list
   monthday_list = monthday ( "," monthday)*
   monthday = [minus] monthdaynum
   monthdaynum = 1 through 31
byday_clause = "BYDAY" "=" byday_list
   byday_list = byday ( "," byday)*
   byday = [weekdaynum] day
   weekdaynum = [minus] daynum
   daynum = 1 through 53 /* if frequency is yearly */
   daynum = 1 through 5  /* if frequency is monthly */
   day = "MON" | "TUE" | "WED" | "THU" | "FRI" | "SAT" | "SUN"
BYTIME clause:  BYTIME=[hour_minute_second_list|minute_second_list]
   hour_minute_second_list: hh24mmss, .., hh24mmss
   minute_second_list: mmss, .. mmss
byhour_clause = "BYHOUR" "=" hour_list
   hour_list = hour ( "," hour)*
   hour = 0 through 23
byminute_clause = "BYMINUTE" "=" minute_list
   minute_list = minute ( "," minute)*
   minute = 0 through 59
bysecond_clause = "BYSECOND" "=" second_list
   second_list = second ( "," second)*
   second = 0 through 59
bysetpos_clause = "BYSETPOS" "=" setpos_list
   setpos_list = setpos ("," setpos)*
   setpos = [minus] setpos_num
   setpos_num = 1 through 9999
include_clause = "INCLUDE" "=" schedule_list
exclude_clause = "EXCLUDE" "=" schedule_list
intersect_clause = "INTERSECT" "=" schedule_list
schedule_list = schedule_clause ("," schedule_clause)*
schedule_clause = named_schedule [ offset ]
named_schedule = [schema "."] schedule
periods_clause = "PERIODS" "=" periodnum
byperiod_clause = "BYPERIOD" "=" period_list
period_list = periodnum ("," periodnum)*
periodnum = 1 through 100
offset = ("+" | "-") ["OFFSET:"] duration_val
span = ("+" | "-" | "^") "SPAN:" duration_val
duration_val = dur-weeks | dur_days
dur_weeks = numofweeks "W"
dur_days = numofdays "D"
numofweeks = 1 through 53
numofdays = 1 through 376
minus = "-"
combined_schedule = schedule_list

Table 159-1 Values for repeat_interval
| Name | Description |
|---|---|
| FREQ | This specifies the type of recurrence. It must be specified. The possible predefined frequency values are YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, and SECONDLY. Alternatively, specifies an existing schedule to use as a user-defined frequency. |
| INTERVAL | This specifies a positive integer representing how often the recurrence repeats. 默认为 1, which means every second for secondly, every day for daily, and so on. The maximum value is 99. |
| BYMONTH | This specifies which month or months you want the job to execute in. You can use numbers such as 1 for January and 3 for March, as well as three-letter abbreviations such as FEB for February and JUL for July. |
| BYWEEKNO | This specifies the week of the year as a number. It follows ISO-8601, which defines the week as starting with Monday and ending with Sunday; and the first week of a year as the first week, which is mostly within the Gregorian year. The first week is equivalent to the following two variants: the week that contains the first Thursday of the Gregorian year; and the week containing January 4th. The ISO-8601 week numbers are integers from 1 to 52 or 53; parts of week 1 may be in the previous calendar year; parts of week 52 may be in the following calendar year; and if a year has a week 53, parts of it must be in the following calendar year. As an example, in the year 1998, the ISO week 1 began on Monday December 29th, 1997; and the last ISO week (week 53) ended on Sunday January 3rd, 1999. So December 29th, 1997, is in the ISO week 1998-01, and January 1st, 1999, is in the ISO week 1998-53. byweekno is only valid for YEARLY. Examples of invalid specifications are "FREQ=YEARLY; BYWEEKNO=1; BYMONTH=12" and "FREQ=YEARLY;BYWEEKNO=53;BYMONTH=1". |
| BYYEARDAY | This specifies the day of the year as a number. Valid values are 1 to 366. An example is 69, which is March 10 (31 for January, 28 for February, and 10 for March). 69 evaluates to March 10 for non-leap years and March 9 in leap years. -2 will always evaluate to December 30th independent of whether it is a leap year. |
| BYDATE | This specifies a list of dates, where each date is of the form [YYYY]MMDD. A list of consecutive dates can be generated by using the SPAN modifier, and a date can be adjusted with the OFFSET modifier. An example of a simple BYDATE clause follows: BYDATE=0115,0315,0615,0915,1215,20060115 The following SPAN example is equivalent to BYDATE=0110,0111,0112,0113,0114, which is a span of 5 days starting at 1/10: BYDATE=0110+SPAN:5D The plus sign in front of the SPAN keyword indicates a span starting at the supplied date. The minus sign indicates a span ending at the supplied date, and the "^" sign indicates a span of n days or weeks centered around the supplied date. If n is an even number, it is adjusted up to the next odd number. Offsets adjust the supplied date by adding or subtracting n days or weeks. BYDATE=0205-OFFSET:2W is equivalent to BYDATE=0205-14D (the OFFSET: keyword is optional), which is also equivalent to BYDATE=0122. |
| BYMONTHDAY | This specifies the day of the month as a number. Valid values are 1 to 31. An example is 10, which means the 10th day of the selected month. You can use the minus sign (-) to count backward from the last day, so, for example, BYMONTHDAY=-1 means the last day of the month and BYMONTHDAY=-2 means the next to last day of the month. |
| BYDAY | This specifies the day of the week from Monday to Sunday in the form MON, TUE, and so on. Using numbers, you can specify the 26th Friday of the year, if using a YEARLY frequency, or the 4th THU of the month, using a MONTHLY frequency. Using the minus sign, you can say the second to last Friday of the month. For example, -1 FRI is the last Friday of the month. |
| BYHOUR | This specifies the hour on which the job is to run. Valid values are 0 to 23. As an example, 10 means 10 a.m. |
| BYMINUTE | This specifies the minute on which the job is to run. Valid values are 0 to 59. As an example, 45 means 45 minutes past the chosen hour. |
| BYSECOND | This specifies the second on which the job is to run. Valid values are 0 to 59. As an example, 30 means 30 seconds past the chosen minute. |
| BYSETPOS | This selects one or more items, by position, in the list of timestamps that result after the whole 日历表达式 is evaluated. It is useful for requirements such as running a job on the last workday of the month. Rather than attempting to express this with the other BY clauses, you can code the 日历表达式 to evaluate to a list of every workday of the month, and then add the BYSETPOS clause to select only the last item of that list. Assuming that workdays are Monday through Friday, the syntax would then be: FREQ=MONTHLY; BYDAY=MON,TUE,WED,THU,FRI; BYSETPOS=-1Valid values are 1 through 9999. A negative number selects an item from the end of the list (-1 is the last item, -2 is the next to last item, and so on) and a positive number selects from the front of the list. The BYSETPOS clause is always evaluated last. BYSETPOS is only supported with the MONTHLY and YEARLY frequencies. The BYSETPOS clause is applied to the list of timestamps once per frequency period. For example, when the frequency is defined as MONTHLY, 调度器 determines all valid timestamps for the month, orders that list, and then applies the BYSETPOS clause. 调度器 then moves on to the next month and repeats the procedure. Assuming a start date of Jun 10, 2004, the example evaluates to: Jun 30, Jul 30, Aug 31, Sep 30, Oct 29, and so on. |
| INCLUDE | This includes one or more named schedules in the 日历表达式. That is, the set of timestamps defined by each included named schedule is added to the results of the 日历表达式. If an identical timestamp is contributed by both an included schedule and the 日历表达式, it is included in the resulting set of timestamps only once. The named schedules must have been defined with the CREATE_SCHEDULE procedure. This clause only works on a full day and therefore cannot be used with BYHOUR, BYMIN, and BYSECOND. |
| EXCLUDE | This excludes one or more named schedules from the 日历表达式. That is, the set of timestamps defined by each excluded named schedule is removed from the results of the 日历表达式. The named schedules must have been defined with the CREATE_SCHEDULE procedure. This clause only works on a full day and therefore cannot be used with BYHOUR, BYMIN, and BYSECOND. |
| INTERSECT | This specifies an intersection between the 日历表达式 results and the set of timestamps defined by one or more named schedules. Only the timestamps that appear both in the 日历表达式 and in one of the named schedules are included in the resulting set of timestamps. For example, assume that the named schedule last_sat indicates the last Saturday in every month, and that for the year 2005, the only months where the last day of the month is also a Saturday are April and December. Assume also that the named schedule end_qtr indicates the last day of each quarter in 2005: 3/31/2005, 6/30/2005, 9/30/2005, 12/31/2005 These 日历表达式s result in the dates that follow:3/31/2005, 4/30/2005, 6/30/2005, 9/30/2005, 12/31/2005 FREQ=MONTHLY; BYMONTHDAY=-1; INTERSECT=last_sat,end_qtrIn this example, the terms FREQ=MONTHLY; BYMONTHDAY=-1 indicate the last day of each month. This clause only works on a full day and therefore cannot be used with BYHOUR, BYMIN, and BYSECOND. |
| PERIODS | This identifies the number of periods that together form one cycle of a user-defined frequency. It is used in the repeat_interval expression of the schedule that defines the user-defined frequency. It is mandatory when the repeat_interval expression in the main schedule contains a BYPERIOD clause. The following example defines the quarters of a fiscal year. FREQ=YEARLY;BYDATE=0301,0601,0901,1201;PERIODS=4 |
| BYPERIOD | This selects periods from a user-defined frequency. For example, if a main schedule names a user-defined frequency schedule that defines the fiscal quarters shown in the previous example, the clause BYPERIOD=2,4 in the main schedule selects the 2nd and 4th fiscal quarters. |
Combining Schedules
There are two ways to combine schedules:
- Using a combined schedule expression, which is a list of individual schedules For example, to create a schedule for all company holidays, you provide a list of individual schedules, where each schedule in the list defines a single holiday. 调度器 evaluates each individual schedule, and then returns a union of the timestamps returned by each individual schedule.

  - Timestamps generated by the INCLUDE clause that fall into periods that are skipped by the main schedule are ignored. This is the case when the main schedule skips periods due to the INTERVAL clause, the BYPERIOD clause, or the BYMONTH clause for freq=monthly.
  - Days that are added by the INCLUDE clause follow the hourly/minutely/secondly execution pattern of the main schedule.

  - When the INCLUDE clause is present, no date-specific defaults are retrieved from the start date (but time-specific defaults can be). (See "Start Dates and Repeat Intervals", later in this section.) For example, a repeat_interval of FREQ=MONTHLY;INCLUDE=HOLIDAY executes only on holidays and not on the month/day defaults retrieved from the start date.
The following is an example:

BEGIN
dbms_scheduler.create_schedule('embed_sched', repeat_interval =>
  'FREQ=YEARLY;BYDATE=0130,0220,0725');
dbms_scheduler.create_schedule('main_sched', repeat_interval =>
  'FREQ=MONTHLY;INTERVAL=2;BYMONTHDAY=15;BYHOUR=9,17;INCLUDE=embed_sched');
END;
/

In this example, the dates 1/30, 2/20, and 7/25 are added to the main schedule. However, 调度器 does not include dates that fall in months that are skipped by the `INTERVAL` clause. If the start date of the main schedule is 1/1/2005, then 2/20 is not added. On the dates that are added, the embedded schedule follows the execution pattern of the main schedule: jobs are executed at 9:00 a.m. and 5:00 p.m. on 1/30 and 7/25. If the embedded schedule does not itself have a start date, it inherits the start date from the main schedule.
User-Defined Frequencies
Instead of using predefined frequencies like `DAILY`, `WEEKLY`, `MONTHLY`, and so on, you can create your own frequencies by creating a schedule that returns the start date of each period. For example, the following `repeat_interval` expression is used in a schedule named `fiscal_year` that defines the start of each quarter in a fiscal year:

FREQ=YEARLY;BYDATE=0301,0601,0901,1201;PERIODS=4

To return the last Wednesday of every quarter, you create a schedule (the "main schedule") that uses the `fiscal_year` schedule as a user-defined frequency:

FREQ=fiscal_year;BYDAY=-1WED

Periods in a user-defined frequency do not have to be equal in length. In the main schedule, the `BYSETPOS` clause and numbered weekdays are recalculated based on the size of each period. To select dates in specific periods, you must use the `BYPERIOD` clause in the main schedule. To enable this, the schedule that is used as the user-defined frequency must include a `PERIODS` clause, and it must set its start date appropriately. The first date returned by this schedule is used as the starting point of period 1.
As another example, assuming work days are Monday through Friday, to get the last work day of the 2nd and 4th quarters of the fiscal year, the `repeat_interval` clause in the main schedule is the following:

FREQ=fiscal_year;BYDAY=MON,TUE,WED,THU,FRI;BYPERIOD=2,4;BYSETPOS=-1

Start Dates and Repeat Intervals
调度器 retrieves the date and time from the job or schedule start date and incorporates them as defaults into the `repeat_interval`. For example, if the specified frequency is yearly and there is no `BYMONTH` or `BYMONTHDAY` clause in the 重复间隔, then the month and day that the 作业运行s on are retrieved from the start date. Similarly, if frequency is monthly but there is no `BYMONTHDAY` clause in the 重复间隔, then the day of the month that the 作业运行s on is retrieved from the start date. If present, `BYHOUR`, `BYMINUTE`, and `BYSECOND` defaults are also retrieved from the start date, and used if those clauses are not specified. Note that if the `INCLUDE`, `EXCLUDE`, or `INTERSECT` clauses are present, no date-related defaults are retrieved from the start date, but time-related defaults are.The following are some examples:

start_date:      4/15/05 9:00:00
repeat_interval: freq=yearly

is expanded internally to:

freq=yearly;bymonth=4;bymonthday=15;byhour=9;byminute=0;bysecond=0

The preceding schedule executes on 04/15/05 9:00:00, 04/15/06 9:00:00, 04/15/07 9:00:00, and so on.
For the next example, assume that schedule `S1` has a `repeat_interval` of `FREQ=YEARLY;BYDATE=0701`.

start_date:      01/20/05 9:00:00
repeat_interval: freq=yearly;include=S1

is expanded internally to:

freq=yearly;byhour=9;byminute=0;bysecond=0;include=S1

Because an `INCLUDE` clause is present, date-related information is not retrieved from the start date. However, time-specific information is, so the preceding schedule executes on 07/01/05 9:00:00, 07/01/06 9:00:00, 07/01/08 9:00:00, and so on.
General Rules
When using a 日历表达式, consider the following rules:
- For a regular schedule (as opposed to a combined schedule), the 日历字符串 must start with the frequency clause. All other clauses are optional and can be put in any order.

- All clauses are separated by a semicolon, and each clause can be present at most once, with the exception of the include, exclude, and intersect clauses.
- Spaces are allowed between syntax elements and the strings are case-insensitive.
- The list of values for a specific BY clause do not need to be ordered.

- When not enough BY clauses are present to determine what the next date is, this information is retrieved from the start date. For example, "FREQ=YEARLY" with a start date of 02/15/2003 becomes "FREQ=YEARLY;BYMONTH=FEB; BYMONTHDAY=15", which means every year on the 15th of February. "FREQ=YEARLY;BYMONTH=JAN,JUL" with start date 01/21/2003 becomes "FREQ=YEARLY;BYMONTH=JAN,JUL;BYMONTHDAY=21", which means every year on January 21 and July 21.

01/06/2003, 01/07/2003, 01/08/2003, 01/09/2003, 01/10/2003, 01/11/2003, 01/12/2003, 01/05/2004, 01/06/2004, 01/07/2004, .... and so on.

12/29/03, 12/30/03, 12/31/03, 01/01/04, 01/02/04, 01/03/04, 01/04/04, 12/27/04, 12/28/04, 12/29/04, 12/30/04, 12/31/04, 01/01/05, 01/02/05

- The byweekno clause is only allowed if the frequency is YEARLY. It cannot be used with other frequencies. When it is present, it will return all days in that week number. If you want to limit it to specific days within the week, you have to add a BYDAY clause. For example, "FREQ=YEARLY;BYWEEKNO=2" with a start date of 01/01/2003 will return: Note that when the byweekno clause is used, it is possible that the dates returned are from a year other than the current year. For example, if returning dates for the year 2004 and the 日历字符串 is "FREQ=YEARLY;BYWEEKNO=1,53" for the specified week numbers in 2004, it will return the dates:

- For those BY clauses that do not have a consistent range of values, you can count backward by putting a "-" in front of the numeric value. For example, specifying BYMONTHDAY=31 will not give you the last day of every month, because not every month has 31 days. Instead, BYMONTHDAY=-1 will give you the last day of the month. This is not supported for BY clauses that are fixed in size. In other words, BYMONTH, BYHOUR, BYMINUTE, and BYSECOND are not supported.

- The basic values for the BYDAY clause are the days of the week. When the frequency is YEARLY, or MONTHLY, you are allowed to specify a positive or negative number in front of each day of the week. In the case of YEARLY, BYDAY=40MON, indicates the 40th Monday of the year. In the case of MONTHLY, BYDAY=-2SAT, indicates the second to last Saturday of the month. Note that positive or negative numbers in front of the weekdays are not supported for other frequencies and that in the case of yearly, the number ranges from -53 ... -1, 1 ... 53, whereas for the monthly frequency it is limited to -5 ... -1, 1... 5. If no number is present in front of the weekday it specifies, every occurrence of that weekday in the specified frequency.
- The first day of the week is Monday.
- Repeating jobs with frequencies smaller than daily follow their frequencies exactly across daylight savings adjustments. For example, suppose that a job is scheduled to repeat every 3 hours, the clock is moved forward from 1:00 a.m. to 2:00 a.m., and the last time the job ran was midnight. Its next scheduled time will be 4:00 a.m. Thus, the 3 hour period between subsequent 作业运行s is retained. The same applies when the clock is moved back. This behavior is not the case for repeating jobs that have frequencies of daily or larger. For example, if a repeating job is supposed to be executed on a daily basis at midnight, it will continue to run at midnight if the clock is moved forward or backward. When the execution time of such a daily (or larger frequency) job happens to fall inside a window where the clock is moved forward, the job executes at the end of the window.

- The calendaring syntax does not allow you to specify a time zone. Instead 调度器 retrieves the time zone from the start_date 参数. If jobs must follow daylight savings adjustments, then you must specify a region name for the time zone of the start_date. For example specifying the start_date time zone as 'US/Eastern' in New York ensures that daylight saving adjustments are automatically applied. If instead, the time zone of the start_date is set to an absolute offset, such as '-5:00', then daylight savings adjustments are not followed and your job execution is off by an hour for half the year.

SQL> ALTER SESSION SET time_zone = 'Asia/Shanghai';

    - Issuing an ALTER SESSION statement, for example:
    - Setting the ORA_SDTZ environment variable.
  - If the session time zone is an absolute offset instead of a region name, 调度器 uses the value of the DEFAULT_TIMEZONE Scheduler 属性. For more information, see the SET_SCHEDULER_ATTRIBUTE Procedure.

  - If the DEFAULT_TIMEZONE 属性 is NULL, 调度器 uses the time zone of systimestamp when the job or window is 已启用.
BYSETPOS Clause Rules
The following are rules for the `BYSETPOS` clause.

- The BYSETPOS clause is the last clause to be evaluated. It is processed after all other BY clauses and the INCLUDE, EXCLUDE and INTERSECT clauses have been evaluated.

FREQ=MONTHLY;INTERVAL=3;BYDAY=MON,TUE,WED,THU,FRI;BYSETPOS=-2

- The INTERVAL clause does not change the size of the period to which the BYSETPOS clause is applied. For example, when the frequency is set to monthly and interval is set to 3, the list of timestamps to which BYSETPOS is applied is generated from a month, not a quarter. The only impact of the INTERVAL clause is to cause months to be skipped. However, you can still select the second to last workday of the quarter like this: provided that you set the start date in the right month. This example returns the next to last workday of a month, and repeats once a quarter.

FREQ=MONTHLY;BYDAY=MON,TUE,FRI;BYSETPOS=1,3

- To get consistent results, the set to which BYSETPOS is applied is determined from the beginning of the frequency period independently of when the evaluation occurs. Whether 调度器 evaluates on 01/01/2004 or 01/15/2004, in both cases the expression evaluates to Friday 01/02/2004, and Tuesday 01/06/2004. The only difference is that when the expression is evaluated on 01/15/2004, 调度器 determines that there are no matches in January because the timestamps found are in the past, and it moves on to the matches in the next month, February.
BYDATE Clause Rules
The following are rules for the `BYDATE` clause.
- If dates in the BYDATE clause do not have their optional year component, the 作业运行s on those dates every year.

freq=daily;byhour=8,13,18;byminute=0;bysecond=0;bydate=0502,0922

- The job execution times on the included dates are derived from the BY clauses in the 日历表达式. For example, if repeat_interval is defined as then the execution times on 05/02 and 09/22 are 8:00 a.m., 1:00 p.m., and 6:00 p.m.
EXCLUDE Clause Rules
Excluded dates without a time component are 24 hour periods. All timestamps that fall on an excluded date are removed. In the following example, `jan_fifteen` is a named schedule that resolves to the single date of 01/15:

freq=monthly;bymonthday=15,30;byhour=8,13,18;byminute=0;bysecond=0;
     exclude=jan_fifteenth

In this case, all three instances of the job are removed for 01/15.
OFFSET Rules
You can adjust the dates of individual named schedules by adding positive offsets to them. For example, to execute `JOB2` exactly 15 days after every occurrence of `JOB1`, add `+OFFSET:15D` to the schedule of `JOB1`, as follows:

BEGIN
dbms_scheduler.create_schedule('job2_schedule', repeat_interval =>
  'job1_schedule+OFFSET:15D');
END;
/

Note that negative offsets to named schedules are not supported.
Example 159-1 Putting It All Together
This example demonstrates the use of user-defined frequencies, spans, offsets, and the `BYSETPOS` and `INCLUDE` clauses. (Note that the `OFFSET:` keyword is optional in an offset clause.)
Many companies in the retail industry share the same fiscal year. The fiscal year starts on the Sunday closest to February 1st, and subsequent quarters start exactly 13 weeks later. The fiscal year schedule for the retail industry can be defined as the following:

begin
 dbms_scheduler.create_schedule('year_start', repeat_interval=>
       'FREQ=YEARLY;BYDATE=0201^SPAN:1W;BYDAY=SUN');
 dbms_scheduler.create_schedule('retail_fiscal_year',
        to_timestamp_tz('15-JAN-2005 12:00:00','DD-MON-YYYY HH24:MI:SS'),
         'year_start,year_start+13w,year_start+26w,year_start+39w;periods=4');
end;
/

The following schedule can be used to execute a job on the 5th day off in the 2nd and the 4th quarters of the retail industry. This assumes that Saturday and Sunday are off days as well as the days in the existing `holiday` schedule.

begin
 dbms_scheduler.create_schedule('fifth_day_off', repeat_interval=>
  'FREQ=retail_fiscal_year;BYDAY=SAT,SUN;INCLUDE=holiday;
    BYPERIOD=2,4;BYSETPOS=5');
end;
/

### DBMS_SCHEDULER 数据结构
The `DBMS_SCHEDULER` package defines `OBJECT` types and `TABLE` types.
OBJECT Types
- JOBARG Object Type
- JOB_DEFINITION Object Type
- JOBATTR Object Type
- SCHEDULER$_STEP_TYPE Object Type
- SCHEDULER$_EVENT_INFO Object Type
- SCHEDULER_FILEWATCHER_RESULT Object Type
- SCHEDULER_FILEWATCHER_REQUEST Object Type
TABLE Types
- JOBARG_ARRAY Table Type
- JOB_DEFINITION_ARRAY Table Type
- JOBATTR_ARRAY Table Type
- SCHEDULER$_STEP_TYPE_LIST Table Type
#### DBMS_SCHEDULER JOBARG Object Type
This type is used by the `JOB` and `JOBATTR` object types. It represents a job 参数 in a batch of 作业参数.
语法

TYPE jobarg IS OBJECT (
   arg_position         NUMBER,
   arg_text_value       VARCHAR2(4000),
   arg_anydata_value    ANYDATA,
   arg_operation        VARCHAR2(5));

Attributes
Table 159-2 JOBARG Object Type Attributes
| Attribute | Description |
|---|---|
| arg_position | Position of the 参数 |
| arg_text_value | Value of the 参数 if the type is VARCHAR2 |
| arg_anydata_value | Value of the 参数 if the type is AnyData |
| arg_operation | Type of the operation: SET RESET |
JOBARG Constructor Function
This constructor function constructs a job 参数. It is overloaded to construct 作业参数 with different types of values.
语法
Constructs a job 参数 with a text value.

constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN VARCHAR2)
   RETURN SELF AS RESULT;

Constructs a job 参数 with an `AnyData` value.

constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN ANYDATA)
   RETURN SELF AS RESULT;

Constructs a job 参数 with a `NULL` value.

constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_reset           IN BOOLEAN DEFAULT FALSE)
   RETURN SELF AS RESULT;

参数
Table 159-3 JOBARG Constructor Function Parameters
| Parameter | Description |
|---|---|
| arg_position | Position of the 参数 |
| arg_value | Value of the 参数 |
| arg_reset | If arg_reset is TRUE, then the 参数 at that position is reset. Setting arg_reset to FALSE (which is the default) will create an 参数 with a NULL value. |
JOBARG_ARRAY Table Type
语法

TYPE jobarg_array IS TABLE OF jobarg;

#### JOBARG_ARRAY Table Type
The `jobarg_array` type is a table of `jobarg`.
语法

TYPE jobarg_array IS TABLE OF jobarg;

#### DBMS_SCHEDULER JOB_DEFINITION Object Type
This type is used by the `CREATE_JOBS` procedure and represents a job in a batch of jobs.
语法

TYPE job_definition IS OBJECT (
  job_name                       VARCHAR2(100),
  job_class                      VARCHAR2(32),
  job_style                      VARCHAR2(11),
  program_name                   VARCHAR2(100),
  job_action                     VARCHAR2(4000),
  job_type                       VARCHAR2(20),
  schedule_name                  VARCHAR2(65),
  repeat_interval                VARCHAR2(4000),
  schedule_limit                 INTERVAL DAY TO SECOND,
  start_date                     TIMESTAMP WITH TIME ZONE,
  end_date                       TIMESTAMP WITH TIME ZONE,
  event_condition                VARCHAR2(4000),
  queue_spec                     VARCHAR2(100),
  number_of_arguments            NUMBER,
  参数s                      SYS.JOBARG_ARRAY,
  job_priority                   NUMBER,
  job_weight                     NUMBER,
  max_run_duration               INTERVAL DAY TO SECOND,
  max_runs                       NUMBER,
  max_failures                   NUMBER,
  logging_level                  NUMBER,
  restartable                    VARCHAR2(5),
  stop_on_window_close           VARCHAR2(5),
  raise_events                   NUMBER,
  comments                       VARCHAR2(240),
  auto_drop                      VARCHAR2(5),
  已启用                        VARCHAR2(5),
  follow_default_timezone        VARCHAR2(5),
  parallel_instances             VARCHAR2(5),
  aq_job                         VARCHAR2(5),
  instance_id                    NUMBER,
  credential_name                VARCHAR2(65),
  目标                    VARCHAR2(4000),
  database_role                  VARCHAR2(20),
  allow_runs_in_restricted_mode  VARCHAR2(5);
  restart_on_recovery            BOOLEAN;
  restart_on_failure             BOOLEAN;)

Object Attributes
Table 159-4 provides brief descriptions of the 属性s of the `JOB_DEFINITION` object type. For more complete information about these 属性s, see the "CREATE_JOB Procedure" and the "SET_ATTRIBUTE Procedure".
Table 159-4 JOB_DEFINITION Object Types
| Attribute | Description |
|---|---|
| job_name | Name of the job |
| job_class | Name of the 作业类 |
| job_style | Style of the job: REGULAR LIGHTWEIGHT IN_MEMORY_RUNTIME IN_MEMORY_FULL |
| program_name | Name of the program that the 作业运行s |
| job_action | Inline action of the job. This is either the code for an anonymous PL/SQL block or the name of a stored procedure, external executable, or chain. |
| job_type | Job action type ('PLSQL_BLOCK', 'STORED_PROCEDURE', 'EXECUTABLE', 'CHAIN', 'EXTERNAL_SCRIPT', 'SQL_SCRIPT', and 'BACKUP_SCRIPT') |
| schedule_name | Name of the schedule that specifies when the job has to execute |
| repeat_interval | Inline time-based schedule |
| schedule_limit | Maximum delay time between scheduled and actual job start before a 作业运行 is canceled |
| start_date | Start date and time of the job |
| end_date | End date and time of the job |
| event_condition | Event condition for event-based jobs |
| queue_spec | File watcher name or queue specification for event-based jobs |
| number_of_arguments | Number of 作业参数 |
| arguments | Array of 作业参数 |
| job priority | Job priority |
| job_weight | *** Deprecated in Oracle Database 11gR2. Do not change the value of this 属性 from the default, which is 1. Weight of the job for parallel execution. |
| max_run_duration | Maximum run duration of the job |
| max_runs | Maximum number of runs before the job is marked as completed |
| max_failures | Maximum number of failures tolerated before the job is marked as broken |
| logging_level | Job logging level |
| restartable | Indicates whether the job is restartable (TRUE) or not (FALSE) |
| stop_on_window_close | Indicates whether the job is stopped when the window that it runs in ends (TRUE) or not (FALSE). Equivalent to the stop_on_window_close job 属性 described in the SET_ATTRIBUTE Procedure. |
| raise_events | State changes that raise events |
| comments | Comments on the job |
| auto_drop | If TRUE (the default), indicates that the job should be dropped once completed |
| enabled | Indicates whether the job should be 已启用 immediately after creating it (TRUE) or not (FALSE) |
| follow_default_timezone | If TRUE and if the job start_date is null, then when the default_timezone scheduler 属性 is changed, 调度器 recomputes the next run date and time for this job so that it is in accordance with the new time zone. |
| parallel_instances | For event-based jobs only. If TRUE, on the arrival of the specified event, 调度器 creates a new 轻量级作业 to handle that event, so multiple instances of the same event-based job can run in parallel. If FALSE, then an event is discarded if it is raised while the job that handles it is already running, |
| aq_job | For internal use only |
| instance_id | The instance ID of the instance that the job must run on For in-memory full jobs, the instance_id value determines in which instance to stop the job; if left NULL, the job is stopped in all instances. |
| credential_name | The 凭据 to use for a single 目标 or the default 凭据 for a group of 目标s |
| destination | The name of a single external 目标 or database 目标, or a group name of type external 目标 or database 目标 |
| database_role | In an Oracle Data Guard environment, the database role ('PRIMARY' or 'LOGICAL STANDBY') for which the 作业运行s |
| allow_runs_in_restricted_mode | If TRUE, the job is permitted to run when the database is in restricted mode, provided that the job owner is permitted to log in during this mode |
| restart_on_recovery | If set to TRUE for a job and the job is stopped by a database shutdown, then the job is restarted when the database is recovered. If set to FALSE, and the job is stopped by a database shutdown, then the job is marked as stopped when the database is recovered. |
| restart_on_failure | If set to TRUE for a job and the job fails due to an application error, then the job is retried using the normal Scheduler retry mechanism (after 1 second, after 10 seconds, after 100 seconds, and so on, up to a maximum of 6 times). If all 6 retries fail (after about 30 hours), then the job is marked FAILED. If set to FALSE (the default), a failed job is immediately marked FAILED. |
JOB_DEFINITION Constructor Function
This constructor function constructs a `job_definition` object.
语法

constructor function job_definition (
    job_name                IN     VARCHAR2,
    job_style               IN     VARCHAR2 DEFAULT 'REGULAR',
    program_name            IN     VARCHAR2 DEFAULT NULL,
    job_action              IN     VARCHAR2 DEFAULT NULL,
    job_type                IN     VARCHAR2 DEFAULT NULL,
    schedule_name           IN     VARCHAR2 DEFAULT NULL,
    repeat_interval         IN     VARCHAR2 DEFAULT NULL,
    event_condition         IN     VARCHAR2 DEFAULT NULL,
    queue_spec              IN     VARCHAR2 DEFAULT NULL,
    start_date              IN     TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    end_date                IN     TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    number_of_arguments     IN     NATURAL DEFAULT NULL,
    arguments               IN     SYS.JOBARG_ARRAY DEFAULT NULL,
    job_class               IN     VARCHAR2 DEFAULT 'DEFAULT_JOB_CLASS',
    schedule_limit          IN     INTERVAL DAY TO SECOND DEFAULT NULL,
    job_priority            IN     NATURAL DEFAULT NULL,
    job_weight              IN     NATURAL DEFAULT NULL,
    max_run_duration        IN     INTERVAL DAY TO SECOND DEFAULT NULL,
    max_runs                IN     NATURAL DEFAULT NULL,
    max_failures            IN     NATURAL DEFAULT NULL,
    logging_level           IN     NATURALN DEFAULT 64,
    restartable             IN     BOOLEAN DEFAULT FALSE,
    stop_on_window_close    IN     BOOLEAN DEFAULT FALSE,
    raise_events            IN     NATURAL DEFAULT NULL,
    comments                IN     VARCHAR2 DEFAULT NULL,
    auto_drop               IN     BOOLEAN DEFAULT TRUE,
    enabled                 IN     BOOLEAN DEFAULT FALSE,
    follow_default_timezone IN     BOOLEAN DEFAULT FALSE,
    parallel_instances      IN     BOOLEAN DEFAULT FALSE,
    aq_job                  IN     BOOLEAN DEFAULT FALSE,
    instance_id             IN     NATURAL DEFAULT NULL,
    credential_name         IN     VARCHAR2 DEFAULT NULL,
    destination             IN     VARCHAR2 DEFAULT NULL,
    database_role           IN     VARCHAR2 DEFAULT NULL,
    allow_runs_in_restricted_mode IN BOOLEAN DEFAULT FALSE)
    RETURN SELF AS RESULT;

JOB_DEFINITION_ARRAY Table Type
语法

TYPE job_definition_array IS TABLE OF job_definition;

#### JOB_DEFINITION_ARRAY Table Type
The type `job_definition_array` is a table of `job_definition`.
语法

TYPE job_definition_array IS TABLE OF job_definition;

#### JOBATTR Object Type
This type is used by the `SET_JOB_ATTRIBUTES` procedure and represents a job 属性 in a batch of job 属性s.
语法

TYPE jobattr IS OBJECT (
   job_name             VARCHAR2(100),
   attr_name            VARCHAR2(30),
   char_value           VARCHAR2(4000),
   char_value2          VARCHAR2(4000),
   args_value           JOBARG_ARRAY,
   num_value            NUMBER,
   timestamp_value      TIMESTAMP(6) WITH TIME ZONE,
   interval_value       INTERVAL DAY(2) TO SECOND(6));

Attributes
Table 159-5 JOBATTR Object Type Attributes
| Attribute | Description |
|---|---|
| job_name | Name of the job |
| attr_name | Name of the 属性 |
| char_value | Value of the 参数 if the type is VARCHAR2 |
| char_value2 | Second VARCHAR2 属性 value |
| args_value | Value of the 参数 if the type is a JOBARG array |
| num_value | Value of the 参数 if the type is NUMBER |
| timestamp_value | Value of the 参数 if the type is TIMESTAMP WITH TIME ZONE |
| interval_value | Value of the 参数 if the type is INTERVAL DAY TO SECOND |
JOBATTR Constructor Function
This constructor function constructs a job 属性. It is overloaded to create 属性 values of the following types: `VARCHAR2`, `NUMBER`, `TIMESTAMP WITH TIME ZONE`, `INTERVAL DAY TO SECOND`, and an array of `JOBARG` types.
语法

constructor function jobattr (
   job_name            IN VARCHAR2,
   attr_name           IN VARCHAR2,
   attr_value          IN VARCHAR2,
   attr_value2         IN VARCHAR2 DEFAULT NULL)
   RETURN SELF AS RESULT;

constructor function jobattr (
   job_name            IN VARCHAR2,
   attr_name           IN VARCHAR2,
   attr_value          IN [NUMBER, BOOLEAN,
                           TIMESTAMP WITH TIME ZONE,
                           INTERVAL DAY TO SECOND, JOBARG_ARRAY])
   RETURN SELF AS RESULT;

constructor function jobattr (
   job_name            IN VARCHAR2,
   attr_name           IN VARCHAR2)
   RETURN SELF AS RESULT;

参数
Table 159-6 JOBATTR Constructor Function Parameters
| Parameter | Description |
|---|---|
| job_name | Name of the job |
| attr_name | Name of the 参数 |
| attr_value | Value of the 参数 |
| attr_value2 | Most 属性s have only one value associated with them, but some can have two. The attr_value2 参数 is for this optional second value. |
JOBATTR Table Type
语法

TYPE jobattr_array IS TABLE OF jobattr;

#### JOBATTR_ARRAY Table Type
The type `jobattr_array` is a table of `jobattr`.
语法

TYPE jobattr_array IS TABLE OF jobattr;

#### SCHEDULER$_STEP_TYPE Object Type
This type is used by `RUN_CHAIN` to return a list of 链步骤s with an initial state.
语法

TYPE scheduler$_step_type IS OBJECT (
   step_name  VARCHAR2(32),
   step_type  VARCHAR2(32));

Attributes
Table 159-7 SCHEDULER$_STEP_TYPE Object Type Attributes
| Attribute | Description |
|---|---|
| step_name | Name of the step |
| step_type | State of the step |
#### SCHEDULER$_STEP_TYPE_LIST Table Type
This type is a table of `scheduler$_step_type`.
语法

TYPE scheduler$_step_type_list IS TABLE OF scheduler$_step_type;

#### SCHEDULER$_EVENT_INFO Object Type
This the datatype of 调度器 事件队列 `SYS.SCHEDULER$_EVENT_QUEUE`, from which your application consumes job state events raised by 调度器.
It is a secure queue owned by `SYS`.
语法

TYPE SCHEDULER$_EVENT_INFO IS OBJECT (
  event_type         VARCHAR2(4000),
  object_owner       VARCHAR2(4000),
  object_name        VARCHAR2(4000),
  event_timestamp    TIMESTAMP WITH TIME ZONE,
  error_code         NUMBER,
  error_msg          VARCHAR2(4000),
  event_status       NUMBER,
  log_id             NUMBER,
  run_count          NUMBER,
  failure_count      NUMBER,
  retry_count        NUMBER,
  spare1             NUMBER,
  spare2             NUMBER,
  spare3             VARCHAR2(4000),
  spare4             VARCHAR2(4000),
  spare5             TIMESTAMP WITH TIME ZONE,
  spare6             TIMESTAMP WITH TIME ZONE,
  spare7             RAW(2000),
  spare8             RAW(2000));

Attributes
Table 159-8 SCHEDULER_EVENT_INFO Object Type Attributes
| Attribute | Description |
|---|---|
| event_type | One of "JOB_STARTED", "JOB_SUCCEEDED", "JOB_FAILED", "JOB_BROKEN", "JOB_COMPLETED", "JOB_STOPPED", "JOB_SCH_LIM_REACHED", "JOB_DISABLED", "JOB_CHAIN_STALLED", "JOB_OVER_MAX_DUR". For descriptions of these event types, see Table 159-84. |
| object_owner | Owner of the job that raised the event |
| object_name | Name of the job that raised the event |
| event_timestamp | Time at which the event occurred |
| error_code | Applicable only when an error is thrown during job execution. Contains the top-level error code. |
| error_msg | Applicable only when an error is thrown during job execution. Contains the entire error stack. |
| event_status | Adds further qualification to the event type. If event_type is "JOB_STARTED," status 1 indicates that it is a normal start, and status 2 indicates that it is a retry. If event_type is "JOB_FAILED," status 4 indicates that it was a failure due to an error that was thrown during job execution, and status 8 indicates that it was an abnormal termination of some kind. If event_type is "JOB_STOPPED," status 16 indicates that it was a normal stop, and status 32 indicates that it was a stop with the FORCE option set to TRUE. |
| log_id | Points to the ID in the scheduler 作业日志 from which additional information can be obtained. Note that there need not always be a log entry corresponding to an event. In such cases, log_id is NULL. |
| run_count | Run count for the job when the event was raised. |
| failure_count | Failure count for the job when the event was raised. |
| retry_count | Retry count for the job when the event was raised. |
| spare1 – spare8 | Not currently in use. |
#### SCHEDULER_FILEWATCHER_RESULT Object Type
This is the datatype of a file arrival event message.
You access the event message as a parameter of an event-based job (or a parameter of a program referenced by an event-based job). The message contains information needed to locate and process a file that arrived on a local or remote system.
语法

TYPE scheduler_filewatcher_result IS OBJECT (
  目标         VARCHAR2(4000),
  directory_path      VARCHAR2(4000),
  actual_file_name    VARCHAR2(4000),
  file_size           NUMBER,
  file_timestamp      TIMESTAMP WITH TIME ZONE,
  ts_ms_from_epoch    NUMBER,
  matching_requests   SYS.SCHEDULER_FILEWATCHER_REQ_LIST);

Attributes
Table 159-9 SCHEDULER_FILEWATCHER_RESULT Object Type Attributes
| Attribute | Description |
|---|---|
| destination | Destination at which the file was found, expressed as a host name or IP address. |
| directory_path | Absolute path of directory in which the file was found. |
| actual_file_name | Actual name of the file that was found. If the file name specified in the 文件监视器 did not contain wildcards, then this is the same as the name specified in the 文件监视器. |
| file_size | Size of the file that was found, in bytes. |
| file_timestamp | Timestamp assigned to the file when the 文件监视器 considered the file found, based on the minimum file size and steady state duration 属性s. |
| ts_ms_from_epoch | For internal use only. |
| matching_requests | List of matching requests. This is a TABLE of type objects SCHEDULER_FILEWATCHER_REQUEST. Each matching request corresponds to a 文件监视器 whose 目标, directory_path, and file_name 属性s matched the arrived file. See "SCHEDULER_FILEWATCHER_REQUEST Object Type". |
#### SCHEDULER_FILEWATCHER_REQUEST Object Type
This type is returned in the `matching_requests` 属性 of the SCHEDULER_FILEWATCHER_RESULT Object Type. Its 属性s are similar to the 属性s of a 文件监视器.
语法

TYPE scheduler_filewatcher_request IS OBJECT (
  owner                 VARCHAR2(4000),
  name                  VARCHAR2(4000),
  requested_path_name   VARCHAR2(4000),
  requested_file_name   VARCHAR2(4000),
  credential_owner      VARCHAR2(4000),
  credential_name       VARCHAR2(4000),
  min_file_size         NUMBER,
  steady_state_dur      NUMBER);

Attributes
Table 159-10 SCHEDULER_FILEWATCHER_REQUEST Object Type Attributes
| Attribute | Description |
|---|---|
| owner | Owner of the matched 文件监视器. |
| name | Name of the matched 文件监视器. |
| requested_path_name | Value of the directory_path 属性 of the matched 文件监视器. |
| requested_file_name | Value of the file_name 属性 of the matched 文件监视器. |
| credential_owner | Owner of the 凭据 referenced by the matched 文件监视器. |
| credential_name | Name of the 凭据 referenced by the matched 文件监视器. |
| min_file_size | Value of the min_file_size 属性 of the matched 文件监视器. |
| steady_state_dur | Value of the steady_state_duration 属性 of the matched 文件监视器. |
**Related Topics**
                           - SCHEDULER_FILEWATCHER_RESULT Object Type
### DBMS_SCHEDULER 子程序概览
This table lists the `DBMS_SCHEDULER` subprograms and briefly describes them.
Table 159-11 DBMS_SCHEDULER Package Subprograms
| Subprogram | Description |
|---|---|
| ADD_EVENT_QUEUE_SUBSCRIBER Procedure | Adds a user as a subscriber to 调度器 事件队列 SYS.SCHEDULER$_EVENT_QUEUE |
| ADD_GROUP_MEMBER Procedure | Adds one or more members to an existing group |
| ADD_JOB_EMAIL_NOTIFICATION Procedure | Adds e-mail 通知s for a job for a list of recipients and a list of job state events |
| ADD_TO_INCOMPATIBILITY Procedure | Adds jobs or programs to an existing incompatibility definition |
| ALTER_CHAIN Procedure | Alters specified steps of a chain |
| ALTER_RUNNING_CHAIN Procedure | Alters specified steps of a running chain |
| CLOSE_WINDOW Procedure | Closes an open window prematurely |
| COPY_JOB Procedure | Copies an existing job |
| CREATE_CHAIN Procedure | Creates a chain, which is a named series of programs that are linked together for a combined objective |
| CREATE_CREDENTIAL Procedure | Creates a 凭据 |
| CREATE_DATABASE_DESTINATION Procedure | Creates a database 目标 for use with remote database jobs |
| CREATE_EVENT_SCHEDULE Procedure | Creates an 事件计划, which is a schedule that starts a job based on the detection of an event |
| CREATE_FILE_WATCHER Procedure | Creates a 文件监视器, which is a Scheduler object that defines the location, name, and other properties of a file whose arrival on a system causes 调度器 to start a job |
| CREATE_GROUP Procedure | Creates a group |
| CREATE_INCOMPATIBILITY Procedure | Creates an incompatibility definition |
| CREATE_JOB Procedure | Creates a single job |
| CREATE_JOB_CLASS Procedure | Creates a 作业类, which provides a way to group jobs for 资源 allocation and prioritization |
| CREATE_JOBS Procedure | Creates multiple jobs |
| CREATE_PROGRAM Procedure | Creates a program |
| CREATE_RESOURCE Procedure | Specifies 资源s used by jobs or creates a new 资源 |
| CREATE_SCHEDULE Procedure | Creates a schedule |
| CREATE_WINDOW Procedure | Creates a window, which provides a way to automatically activate different 资源计划s at different times |
| DEFINE_ANYDATA_ARGUMENT Procedure | Defines a program 参数 whose value is of a complex type and must be passed encapsulated in an AnyData object |
| DEFINE_CHAIN_EVENT_STEP Procedure | Adds or replaces a 链步骤 and associates it with an 事件计划 or inline event. See also: DEFINE_CHAIN_STEP. |
| DEFINE_CHAIN_RULE Procedure | Adds a rule to an existing chain |
| DEFINE_CHAIN_STEP Procedure | Defines a 链步骤, which can be a program or another (nested) chain. See also: DEFINE_CHAIN_EVENT_STEP. |
| DEFINE_METADATA_ARGUMENT Procedure | Defines a special metadata 参数 for the program. You can retrieve specific metadata through this 参数. |
| DEFINE_PROGRAM_ARGUMENT Procedure | Defines a program 参数 whose value can be passed as a string literal to the program |
| DISABLE Procedure | Disables a program, job, chain, window, database 目标, external 目标, 文件监视器, group, or incompatibilty |
| DROP_AGENT_DESTINATION Procedure | Drops one or more external 目标s. Use only when the preferred method of dropping external 目标s—unregistering 调度器 agent with the database—fails. |
| DROP_CHAIN Procedure | Drops an existing chain |
| DROP_CHAIN_RULE Procedure | Removes a rule from an existing chain |
| DROP_CHAIN_STEP Procedure | Drops a 链步骤 |
| DROP_CREDENTIAL Procedure | Drops a 凭据 |
| DROP_DATABASE_DESTINATION Procedure | Drops one or more database 目标s |
| DROP_FILE_WATCHER Procedure | Drops one or more 文件监视器s |
| DROP_GROUP Procedure | Drops one or more groups |
| DROP_INCOMPATIBILITY Procedure | Drops an existing incompatibility definition |
| DROP_JOB Procedure | Drops a job or all jobs in a 作业类 |
| DROP_JOB_CLASS Procedure | Drops a 作业类 |
| DROP_PROGRAM Procedure | Drops a program |
| DROP_PROGRAM_ARGUMENT Procedure | Drops a program 参数 |
| DROP_SCHEDULE Procedure | Drops a schedule |
| DROP_WINDOW Procedure | Drops a window |
| ENABLE Procedure | Enables a program, job, chain, window, database 目标, external 目标, 文件监视器, or group |
| END_DETACHED_JOB_RUN Procedure | Ends a running detached job |
| EVALUATE_CALENDAR_STRING Procedure | Evaluates the 日历字符串 and tells you what the next execution date of a job or window will be |
| EVALUATE_RUNNING_CHAIN Procedure | Forces reevaluation of the rules of a running chain to trigger any rules for conditions that have been satisfied |
| GENERATE_JOB_NAME Function | Generates a unique name for a job. This enables you to identify jobs by adding a prefix, so, for example, Sally's jobs would be named sally1, sally2, and so on |
| GET_AGENT_INFO Function | Returns job information specific to an agent, such as how many are running and so on, depending on the 属性 selected |
| GET_AGENT_VERSION Function | Returns the version string of a Scheduler agent that is registered with the database and is currently running |
| GET_ATTRIBUTE Procedure | Retrieves the value of an 属性 of an object |
| GET_FILE Procedure | Retrieves a file from a host |
| GET_SCHEDULER_ATTRIBUTE Procedure | Retrieves the value of a Scheduler 属性 |
| OPEN_WINDOW Procedure | Opens a window prematurely. The window is opened immediately for the duration |
| PURGE_LOG Procedure | Purges specific rows from the job and 窗口日志s |
| PUT_FILE Procedure | Saves a file to one or more hosts |
| REMOVE_EVENT_QUEUE_SUBSCRIBER Procedure | Unsubscribes a user from 调度器 事件队列 SYS.SCHEDULER$_EVENT_QUEUE |
| REMOVE_FROM_INCOMPATIBILITY Procedure | Removes jobs or programs from an incompatibility definition |
| REMOVE_GROUP_MEMBER Procedure | Removes one or more members from a group |
| REMOVE_JOB_EMAIL_NOTIFICATION Procedure | Removes e-mail 通知s for a job |
| RESET_JOB_ARGUMENT_VALUE Procedure | Resets the current value assigned to an 参数 defined with the associated program |
| RUN_CHAIN Procedure | Immediately runs a chain by creating a run-once job |
| RUN_JOB Procedure | Runs a job immediately |
| SET_AGENT_REGISTRATION_PASS Procedure | Sets the agent registration password for a database |
| SET_ATTRIBUTE Procedure | Changes an 属性 of a job, schedule, or other Scheduler object |
| SET_ATTRIBUTE_NULL Procedure | Changes an 属性 of an object to NULL |
| SET_JOB_ANYDATA_VALUE Procedure | Sets the value of a job 参数 encapsulated in an AnyData object |
| SET_JOB_ARGUMENT_VALUE Procedure | Sets the value of a job 参数 |
| SET_JOB_ATTRIBUTES Procedure | Sets the value of a job 属性 |
| SET_RESOURCE_CONSTRAINT Procedure | Specifies the 资源s used by jobs |
| SET_SCHEDULER_ATTRIBUTE Procedure | Sets the value of a Scheduler 属性 |
| STOP_JOB Procedure | Stops a currently running job or all jobs in a 作业类 |
#### ADD_EVENT_QUEUE_SUBSCRIBER Procedure
此过程 adds a user as a subscriber to 调度器 事件队列 `SYS.SCHEDULER$_EVENT_QUEUE`, and grants the user permission to dequeue from this queue using the designated agent.
语法

DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER (
   subscriber_name         IN VARCHAR2 DEFAULT NULL);

参数
Table 159-12 ADD_EVENT_QUEUE_SUBSCRIBER Procedure Parameters
| Parameter | Description |
|---|---|
| subscriber_name | Name of the Oracle Advanced Queuing (AQ) agent to be used to subscribe to 调度器 事件队列. If NULL, an agent is created and assigned the user name of the calling user. |
使用说明
The subscription is rule-based. The rule permits the user to see only events raised by jobs that the user owns, and filters out all other messages. If an AQ agent with the same name already exists, an error is raised.
#### ADD_GROUP_MEMBER Procedure
此过程 adds one or more members to an existing group.
语法

DBMS_SCHEDULER.ADD_GROUP_MEMBER (
   group_name              IN VARCHAR2,
   member                  IN VARCHAR2);

参数
Table 159-13 ADD_GROUP_MEMBER Procedure Parameters
| Parameter | Description |
|---|---|
| group_name | The name of the group. |
| member | A comma-separated list of members to add to the group. Members must match the group type. A group of the same type can be a member. 调度器 immediately expands the included group name into its list of members. An error is returned if any of the members do not exist. A member that is already in the group is skipped, and no error is generated. The keyword LOCAL can be included as a member for database 目标 or external 目标 groups. See the "CREATE_GROUP Procedure" for information about this keyword. |
使用说明
The following users may add members to a group:
- The group owner
- A user that has been granted the ALTER object privilege on the group
- A user with the CREATE ANY JOB system privilege
You must have the `MANAGE` `SCHEDULER` privilege to add a member to a group of type `WINDOW`.
参见：
"CREATE_GROUP Procedure"
#### ADD_JOB_EMAIL_NOTIFICATION Procedure
此过程 adds e-mail 通知s for a job. E-mails are then sent to the specified list of recipients whenever any of the specified job state events is raised.
语法

DBMS_SCHEDULER.ADD_JOB_EMAIL_NOTIFICATION (
    job_name             IN VARCHAR2,
    recipients           IN VARCHAR2,
    sender               IN VARCHAR2 DEFAULT NULL,
    subject              IN VARCHAR2 DEFAULT DBMS_SCHEDULER.DEFAULT_NOTIFICATION_SUBJECT,
    body                 IN VARCHAR2 DEFAULT DBMS_SCHEDULER.DEFAULT_NOTIFICATION_BODY,
    events               IN VARCHAR2 DEFAULT 'JOB_FAILED,JOB_BROKEN,JOB_SCH_LIM_REACHED,
                             JOB_CHAIN_STALLED,JOB_OVER_MAX_DUR',
    filter_condition     IN VARCHAR2 DEFAULT NULL);

参数
Table 159-14 ADD_JOB_EMAIL_NOTIFICATION Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | Name of the job that e-mail 通知s are added for. Cannot be NULL. |
| recipients | Comma-separated list of e-mail addresses to send 通知s to. E-mail 通知s for all listed events are sent to all recipients. Cannot be NULL. |
| sender | e-mail address to use as the sender address (the From: address) in the e-mail header. If NULL or omitted, the e-mail address specified in 调度器 属性 email_sender is used. See Oracle Database Administrator's Guide for more information on this Scheduler 属性. |
| subject | The subject to use in the e-mail header. Table 159-15 describes the variables that you can include within this parameter. 调度器 assigns values to these variables before sending the 通知. If subject is omitted, the default subject is used. The default subject is the following text, where text enclosed in the '%' character represents a variable: 'Oracle Scheduler Job Notification - %job_owner%.%job_name%.%job_subname% %event_type%' |
| body | The body of the e-mail message. Table 159-15 describes the variables that you can include within this parameter. 调度器 assigns values to these variables before sending the 通知. If body is omitted, the default body is used. The default body is the following text, where text enclosed in the '%' character represents a variable: 'Job: %job_owner%.%job_name%.%job_subname% Event: %event_type% Date: %event_timestamp% Log id: %log_id% Job class: %job_class_name% Run count: %run_count% Failure count: %failure_count% Retry count: %retry_count% Error code: %error_code% Error message: %error_message%' |
| events | Comma-separate list of job state events to send e-mail 通知s for. Cannot be NULL. A 通知 is sent to all recipients if any of the listed events is raised. Table 159-84 lists the valid events for this parameter. If events is omitted, 通知s are sent for the following default events: JOB_FAILED,JOB_BROKEN,JOB_SCH_LIM_REACHED,JOB_CHAIN_STALLED,JOB_OVER_MAX_DUR |
| filter_condition | Used to filter events to send e-mail 通知s for. If NULL, all occurrences of the specified events cause e-mail 通知s to be sent. filter_condition must be a boolean SQL WHERE clause that may refer to the :event bind variable. This bind variable is automatically bound to an object of type SCHEDULER$_EVENT_INFO that represents the raised event. For example, to send an e-mail 通知 only when the error number in an event is 600 or 700, use the following filter_condition: :event.error_code=600 or :event.error_code=700See "SCHEDULER$_EVENT_INFO Object Type". |
Table 159-15 lists the variables that you can use in the subject and body 参数s.
Table 159-15 Variables Used in the SUBJECT and BODY Parameters
| Variable | Comment |
|---|---|
| %job_owner% | Schema in which job was created |
| %job_name% | Name of the job that e-mail 通知s are added for |
| %job_subname% | Present for event-based jobs with the parallel_instances 属性 set and for 链步骤s |
| %event_type% | Valid values are listed in Table 159-84 |
| %event_timestamp% | Time at which the event occurred |
| %log_id% | Refers to the LOG_ID column in views *_SCHEDULER_JOB_LOG and *_SCHEDULER_JOB_RUN_DETAILS |
| %error_code% | Number of the error code. |
| %error_message% | The text of the error message |
| %run_count% | Run count for the job when the event was raised |
| %failure_count% | Failure count for the job when the event was raised |
| %retry_count% | Retry count for the job when the event was raised |
使用说明
You can call `ADD_JOB_EMAIL_NOTIFICATION` once for each different set of 通知s that you want to configure for a particular job. For example, you may want to send 通知s for the `JOB_FAILED`, `JOB_BROKEN`, `JOB_SCH_LIM_REACHED`, and `JOB_CHAIN_STALLED` events to the principle DBA and all senior DBAs, but send a 通知 for the `JOB_OVER_MAX_DUR` event only to the principle DBA.
此过程 succeeds only if 调度器 属性 `email_server` is set to a valid SMTP server. See Oracle Database Administrator's Guide for more information.
To call this procedure, you must be the job owner or have the `CREATE` `ANY` `JOB` system privilege or have the `ALTER` object privilege on the job.
#### ADD_TO_INCOMPATIBILITY Procedure
此过程 adds jobs or programs to an existing incompatibility definition.
语法

DBMS_SCHEDULER.ADD_TO_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2);

参数
Table 159-16 ADD_TO_INCOMPATIBILITY Procedure Parameters
| Parameter | Description |
|---|---|
| incompatibility_name | The name of the incompatibility definition. |
| object_name | One or more (comma-separated) programs or jobs |
使用说明
此过程 does not raise an error if any specified objects already exist in the incompatibility definition.
参见：
Using Incompatibility Definitions in Oracle Database Administrator’s Guide
#### ALTER_CHAIN Procedure
此过程 alters an 属性 of the specified steps of a chain. This affects all future runs of the specified steps, both in the currently running chain job and in future runs of the same chain job or other chain jobs that point to the chain.
语法
Alters the value of a boolean 属性 of one or more steps:

DBMS_SCHEDULER.ALTER_CHAIN (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   attribute               IN VARCHAR2,
   value                   IN BOOLEAN);

Alters the value of a character 属性 of one or more steps:

DBMS_SCHEDULER.ALTER_CHAIN (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   attribute               IN VARCHAR2,
   char_value              IN VARCHAR2);

参数
Table 159-17 ALTER_CHAIN Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to alter |
| step_name | The name of the step or a comma-separated list of steps to alter. This cannot be NULL. |
| attribute | The 属性 of the steps to change. Must be one of the following: 'PAUSE' If set to TRUE for a step, after the step has run, its state changes to PAUSED (and the completed 属性 remains FALSE). If PAUSE is reset to FALSE for a paused 链步骤 (using ALTER_RUNNING_CHAIN), the state is set to its completion state (SUCCEEDED, FAILED, or STOPPED) and the completed 属性 is set to TRUE. Setting PAUSE has no effect on steps that have already run. This allows execution of a chain to be suspended after the execution of certain steps. 'PAUSED_BEFORE' If set to TRUE for a step and if any of the rule conditions that start the step are true, then its state changes to PAUSED and the step does not run. If PAUSE_BEFORE is reset to FALSE for a 链步骤 that has paused before starting (using ALTER_RUNNING_CHAIN), then the step starts running if any of the rule conditions that start the step are true. Setting PAUSE_BEFORE has no effect on steps that are running or have already run. This allows execution of a chain to be suspended before the execution of certain steps. 'SKIP' If set to TRUE for a step, when the step condition is met, instead of being run, the step is treated as if it has immediately succeeded. Setting SKIP to TRUE has no effect for a step that is running, scheduled to run after a delay, or has already run. If SKIP is set TRUE for a step that PAUSE is also set for, when the step condition is met, the step immediately changes to state PAUSED. 'RESTART_ON_FAILURE' If set to TRUE for a step and the step fails due to an application error, then the step is retried using the normal Scheduler retry mechanism (after 1 second, after 10 seconds, after 100 seconds, and so on, up to a maximum of 6 times). If all 6 retries fail (after about 30 hours), then the 链步骤 is marked FAILED. If set to FALSE (the default), a failed 链步骤 is immediately marked FAILED. 'RESTART_ON_RECOVERY' If set to TRUE for a step and the step is stopped by a database shutdown, then the step is restarted when the database is recovered. If set to FALSE, and the step is stopped by a database shutdown, then the step is marked as stopped when the database is recovered and the chain continues. 'DESTINATION_NAME' The name of an existing database 目标 or external 目标. You can view external 目标 names in the view ALL_SCHEDULER_EXTERNAL_DESTS, and database 目标 names in the views *_SCHEDULER_DB_DESTS. You cannot specify a 目标 group for this 属性. This parameter is NULL by default. 'CREDENTIAL_NAME' The 凭据 to use when running this step. NULL by default. |
| value | The value to set for the 属性 (for a boolean 属性). |
| char_value | The value to set for the 属性 (for a character 属性). |
使用说明
Altering a chain requires `ALTER` privileges on the chain either by being the owner of the chain, or by having the `ALTER` object privilege on the chain or by having the `CREATE` `ANY` `JOB` system privilege.
#### ALTER_RUNNING_CHAIN Procedure
此过程 alters an 属性 of the specified steps of a chain. This affects only steps of the instance of the chain for the specified running chain job.
语法

DBMS_SCHEDULER.ALTER_RUNNING_CHAIN (
   job_name                IN VARCHAR2,
   step_name               IN VARCHAR2,
   attribute               IN VARCHAR2,
   value                   IN {BOOLEAN|VARCHAR2});

参数
Table 159-18 ALTER_RUNNING_CHAIN Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of the job that is running the chain |
| step_name | The name of the step or a comma-separated list of steps to alter. If this is set to NULL and 属性 is PAUSE or SKIP, then all steps of the running chain are altered. |
| attribute | The 属性 of the steps to change. Valid values are: 'PAUSE' If the PAUSE 属性 is set TRUE for a step, then after the step runs, its state changes to PAUSED (and the completed 属性 remains false). If PAUSE is reset to FALSE for a paused 链步骤 (using ALTER_RUNNING_CHAIN), the state is set to completion (SUCCEEDED, FAILED, or STOPPED) and the completed 属性 is set to TRUE. Setting PAUSE has no effect on steps that have already run. This allows execution of a chain to be suspended after the execution of certain steps. If step_name is set to NULL, PAUSE is set to TRUE for all steps of this running chain. 'PAUSE_BEFORE' If set to TRUE for a step that has not yet run and if any of the rule conditions that start the step are true, then its state changes to PAUSED and the step does not run. If PAUSE_BEFORE is reset to FALSE for a 链步骤 that has paused before starting, then the step starts running if any of the rule conditions that start the step are true. Setting PAUSE_BEFORE has no effect on steps that are running or have already run. This allows execution of a chain to be suspended before the execution of certain steps. If step_name is set to NULL, then PAUSE_BEFORE is set to the specified value for all steps of this running chain. |
| attribute CONTINUED | 'SKIP' If the SKIP 属性 is set to TRUE for a step, when the step condition is met, instead of being run, the step is treated as if it has immediately succeeded. Setting SKIP to TRUE has no effect for a step that is running, scheduled to run after a delay, or has already run. If step_name is set to NULL, SKIP is set TRUE for all steps of this running chain. If SKIP is set TRUE for a step that PAUSE is also set for, when the step condition is met the step immediately changes to state PAUSED. 'RESTART_ON_FAILURE' If set to TRUE for a step and the step fails due to an application error, then the step is retried using the normal Scheduler retry mechanism (after 1 second, after 10 seconds, after 100 seconds, and so on, up to a maximum of 6 times). If all 6 retries fail (after about 30 hours), then the 链步骤 is marked FAILED. If set to FALSE (the default), a failed 链步骤 is immediately marked FAILED. 'RESTART_ON_RECOVERY' If the RESTART_ON_RECOVERY 属性 is set to TRUE for a step, then if the step is stopped by a database shutdown, it is restarted when the database is recovered. If set to FALSE, then if the step is stopped by a database shutdown, the step is marked as stopped when the database is recovered and the chain continues. 'STATE' This changes the state of the steps. The state can only be changed if the step is not running. The state can only be changed to one of the following:'NOT_STARTED', 'SUCCEEDED', 'FAILED error_code'If the state is being changed to FAILED, an error code must be included (this must be a positive integer). |
| value | The value to set for the 属性. Valid values are: TRUE, FALSE, 'NOT_STARTED', 'SUCCEEDED', or 'FAILED error_code' |
使用说明
Altering a running chain requires you to have alter privileges on the job that is running (either as the owner, or as a user with `ALTER` privileges on the job or the `CREATE` `ANY` `JOB` system privilege).
When trying to update a step defined with a nested chain, it is necessary to specify the `job_name` as `<SCHEMA>.<JOB_NAME>.<STEP_NAME_IN_TOP_LEVEL_CHAIN>` to be able to make reference to the steps inside the subchain.
#### CLOSE_WINDOW Procedure
此过程 closes an open window prematurely. A closed window means that it is no longer in effect. When a window is closed, 调度器 switches the 资源计划 to the one that is in effect outside the window, or in the case of overlapping windows, to another window.
语法

DBMS_SCHEDULER.CLOSE_WINDOW (
   window_name             IN VARCHAR2);

参数
Table 159-19 CLOSE_WINDOW Procedure Parameters
| Parameter | Description |
|---|---|
| window_name | The name of the window |
使用说明
If you try to close a window that does not exist or is not open, an error is generated.
A job that is running does not stop when the window it is running in closes, unless the 属性 `stop_on_window_close` is set to `TRUE` for the job. However, the 资源s allocated to the job can change if the 资源计划 changes.
When a running job has a group of type `WINDOW` as its schedule, the job is not stopped when its window is closed if another window in the same 窗口组 becomes active. This is the case even if the job has the 属性 `stop_on_window_close` set to `TRUE`.
Closing a window requires the `MANAGE` `SCHEDULER` privilege.
#### COPY_JOB Procedure
此过程 copies all 属性s of an existing job to a new job. The new job is created 已禁用, while the state of the existing job is unaltered.
语法

DBMS_SCHEDULER.COPY_JOB (
   old_job                IN VARCHAR2,
   new_job                IN VARCHAR2);

参数
Table 159-20 COPY_JOB Procedure Parameters
| Parameter | Description |
|---|---|
| old_job | The name of the existing job |
| new_job | The name of the new job |
使用说明
To copy a job, you must have privileges to create a job in the schema of the new job (the `CREATE` `JOB` system privilege if it is in your own schema, otherwise, the `CREATE` `ANY` `JOB` system privilege). If the old job is not in the your own schema, then you must also have `ALTER` privileges on the old job or the `CREATE` `ANY` `JOB` system privilege.
#### CREATE_CHAIN Procedure
此过程 creates a new chain. The chain name can be optionally qualified with a schema name (for example, `myschema.myname`).
A chain is always created as 已禁用 and must be 已启用 with the ENABLE Procedure before it can be used.
语法

DBMS_SCHEDULER.CREATE_CHAIN (
   chain_name              IN VARCHAR2,
   rule_set_name           IN VARCHAR2 DEFAULT NULL,
   evaluation_interval     IN INTERVAL DAY TO SECOND DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-21 CREATE_CHAIN Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name to assign to the new chain, which can optionally be qualified with a schema. This must be unique in the SQL namespace, therefore, there cannot already be a table or other object with this name and schema. |
| rule_set_name | In the normal case, no 规则集 should be passed in. 调度器 automatically creates a 规则集 and associated empty evaluation context. You then use DEFINE_CHAIN_RULE to add rules and DROP_CHAIN_RULE to remove them. Advanced users can create a 规则集 that describes their chain dependencies and pass it in here. This allows greater flexibility in defining rules. For example, conditions can refer to external variables, and tables can be exposed through the evaluation context. If you pass in a 规则集, you must ensure that it is in the format of a chain 规则集. (For example, all steps must be listed as variables in the evaluation context). If no 规则集 is passed in, the 规则集 created is of the form SCHED_RULESET${N} and the evaluation context created is of the form SCHED_EVCTX${N} |
| evaluation_interval | If this is NULL, reevaluation of the rules of a running chain are performed only when the job starts and when a step completes. A non-NULL value causes rule evaluations to also occur periodically at the specified interval. Because evaluation may be CPU-intensive, this should be conservatively set to the highest possible value or left at NULL if possible. evaluation_interval cannot be less than a minute or greater than a day. |
| comments | An optional comment describing the purpose of the chain |
使用说明
To create a chain in your own schema, you must have the `CREATE` `JOB` system privilege. To create a chain in a different schema you must have the `CREATE` `ANY` `JOB` system privilege. If you do not provide a `rule_set_name`, a 规则集 and evaluation context is created in the schema that the chain is being created in, so you must have the privileges required to create these objects. See the `DBMS_RULE_ADM.CREATE_RULE_SET` and `DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT` procedures for more information.
#### CREATE_CREDENTIAL Procedure
This deprecated procedure creates a stored username/password pair. Credentials are assigned to jobs so that they can authenticate with a local or remote host operating system or a remote Oracle database.
Note:
此过程 is deprecated with Oracle Database 12c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the  DBMS_CREDENTIAL  package, specifically the CREATE_CREDENTIAL Procedure.
语法

DBMS_SCHEDULER.CREATE_CREDENTIAL (
   credential_name         IN VARCHAR2,
   username                IN VARCHAR2,
   password                IN VARCHAR2,
   database_role           IN VARCHAR2 DEFAULT NULL,
   windows_domain          IN VARCHAR2 DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-22 CREATE_CREDENTIAL Procedure Parameters
| Parameter | Description |
|---|---|
| credential_name | The name to assign to the 凭据. It can optionally be prefixed with a schema name. It cannot be set to NULL. It is converted to uppercase unless enclosed in double quotation marks. |
| username | The user name for logging into to the host operating system or remote Oracle database. This cannot be set to NULL and is case-sensitive. It cannot contain double quotes or spaces. Maximum length is 64. |
| password | The password for the user name. This cannot be set to NULL and is case sensitive. The password is stored obfuscated and is not displayed in 调度器 dictionary views. Maximum length is 128. |
| database_role | The value of the database_role 属性 is used as the system privilege for logging into a remote database to run a remote database job. Valid values are: SYSDBA and SYSOPER |
| windows_domain | For a Windows remote executable target, this is the domain that the specified user belongs to. The domain is converted to uppercase automatically. Maximum length is 64. |
| comments | A text string that can be used to describe the 凭据. Scheduler does not use this parameter. Maximum length is 240. |
使用说明
Credentials reside in a particular schema and can be created by any user with the `CREATE JOB` system privilege. To create a 凭据 in a schema other than your own, you must have the `CREATE ANY JOB` privilege.
#### CREATE_DATABASE_DESTINATION Procedure
此过程 creates a database 目标. A database 目标 represents an Oracle database on which remote database jobs run.
The host that the remote database resides on must have a running Scheduler agent that is registered with the database that this procedure is called from.
语法

DBMS_SCHEDULER.CREATE_DATABASE_DESTINATION (
   destination_name        IN VARCHAR2,
   agent                   IN VARCHAR2,
   tns_name                IN VARCHAR2,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-23 CREATE_DATABASE_DESTINATION Procedure Parameters
| Parameter | Description |
|---|---|
| destination_name | The name to assign to the database 目标. It can optionally be prefixed with a schema name. Cannot be NULL. It is converted to uppercase unless enclosed in double quotation marks. |
| agent | The external 目标 name of 调度器 agent to connect. Equivalent to an agent name. The external 目标 must already exist. The external 目标 representing an agent is created automatically on a database instance when the agent registers with that instance. An agent's name is specified in its agent configuration file. If it is not specified, it defaults to the first part (before the first period) of the name of the host it resides on. |
| tns_name | An Oracle Net connect identifier that is resolved to the Oracle database instance being connected to. The exact syntax depends on the Oracle Net configuration.The connect identifier can be a complete Oracle Net connect descriptor (network address and database service name) or a net service name, which is an alias for a connect descriptor. The alias must be resolved in the tnsnames.ora file on the local computer. The maximum size for tns_name is 2000 characters. If tns_name is NULL, the agent connects to the default Oracle database on its host. You specify the default database by assigning values to the ORACLE_HOME and ORACLE_SID parameters in the agent configuration file, schagent.conf, located in the agent home directory. See Oracle Database Net Services Administrator's Guide for more information on connect identifiers. |
| comments | A text string that describes the database 目标. Scheduler does not use this 参数. |
使用说明
Database 目标s reside in a particular schema and can be created by any user with the `CREATE JOB` system privilege. To create a database 目标 in a schema other than your own, you must have the `CREATE ANY JOB` privilege.
#### CREATE_EVENT_SCHEDULE Procedure
此过程 creates an 事件计划, which is used to start a job when a particular event is raised.
语法

DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE (
   schedule_name           IN VARCHAR2,
   start_date              IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   event_condition         IN VARCHAR2 DEFAULT NULL,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-24 CREATE_EVENT_SCHEDULE Parameters
| Parameter | Description |
|---|---|
| schedule_name | The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. |
| start_date | This 属性 specifies the date and time that this schedule becomes valid. Occurrences of the event before this date and time are ignored in the context of this schedule. |
| event_condition | This is a conditional expression based on the columns of the event 源队列 table. The expression must have the syntax of an Advanced Queuing rule. Accordingly, you can include user data properties in the expression, provided that the message payload is an object type, and that you prefix object 属性s in the expression with tab.user_data. For more information on rules, see the DBMS_AQADM.ADD_SUBSCRIBER procedure. |
| queue_spec | This 参数 specifies either a 文件监视器 name or the queue into which events that start this particular job are enqueued (the 源队列). If the 源队列 is a secure queue, the queue_spec 参数 is a string containing a pair of values of the form queue_name, agent name. For non-secure queues, only the queue name need be provided. If a fully qualified queue name is not provided, the queue is assumed to be in the job owner's schema. In the case of secure queues, the agent name provided should belong to a valid agent that is currently subscribed to the queue. |
| end_date | The date and time after which jobs do not run and windows do not open. An 事件计划 that has no end_date is valid forever. end_date must be after the start_date. If it is not, then an error is generated when the schedule is created. |
| comments | This 属性 specifies an optional comment about the schedule. By default, this 属性 is NULL. |
使用说明
You must have the `CREATE` `JOB` privilege to create a schedule in your own schema or the `CREATE` `ANY` `JOB` privilege to create a schedule in someone else's schema by specifying `schema.schedule_name`. Once a schedule has been created, it can be used by other users. The schedule is created with access to `PUBLIC`. Therefore, there is no need to explicitly grant access to the schedule.
参见：
"CREATE_FILE_WATCHER Procedure"
#### CREATE_FILE_WATCHER Procedure
此过程 creates a 文件监视器, which is a Scheduler object that defines the location, name, and other properties of a file whose arrival on a system causes 调度器 to start a job. After you create a 文件监视器, you reference it in an event-based job or 事件计划.
语法

DBMS_SCHEDULER.CREATE_FILE_WATCHER (
   file_watcher_name            IN VARCHAR2,
   directory_path               IN VARCHAR2,
   file_name                    IN VARCHAR2,
   credential_name              IN VARCHAR2,
   destination                  IN VARCHAR2  DEFAULT NULL,
   min_file_size                IN PLS_INTEGER DEFAULT 0,
   steady_state_duration        IN INTERVAL DAY TO SECOND DEFAULT NULL,
   comments                     IN VARCHAR2 DEFAULT NULL,
   enabled                      IN BOOLEAN DEFAULT TRUE);

参数
Table 159-25 CREATE_FILE_WATCHER Parameters
| Parameter | Description |
|---|---|
| file_watcher_name | The name to assign to the 文件监视器. The name must be unique in the SQL namespace. For example, a 文件监视器 cannot have the same name as a table in a schema. This can optionally be prefixed with a schema name. Cannot be NULL. |
| directory_path | Directory in which the file is expected to arrive. The single wildcard '?' at the beginning of the path denotes the Oracle home path. For example, '?/rdbms/log' denotes the rdbms/log subdirectory of the Oracle home directory. |
| file_name | Name of the file to look for. Two wildcards are permitted anywhere in the file name: '?' denotes any single character, and '*' denotes zero or more characters. This 属性 cannot be NULL. |
| credential_name | Name of a valid 凭据 object. The 文件监视器 uses the 凭据 to authenticate itself with the host operating system to access the watched-for file. The 文件监视器 owner must have EXECUTE privileges on the 凭据. Cannot be NULL. |
| destination | Name of an external 目标. You create an external 目标 by registering a remote Scheduler agent with the database. See the view ALL_SCHEDULER_EXTERNAL_DESTS for valid external 目标 names. If this parameter is NULL, the 文件监视器 is created on the local host. |
| min_file_size | Minimum size in bytes that the file must be before the 文件监视器 considers the file found. 默认为 0. |
| steady_state_duration | Minimum time interval that the file must remain unchanged before the 文件监视器 considers the file found. Cannot exceed one hour. If NULL, an internal value is used. The minimum value is 10 seconds. Oracle recommends similar steady_state_duration values for all 文件监视器s for efficient 文件监视器 job operation. Also, the 重复间隔 of the 文件监视器 schedule must be equal or greater than the steady_state_duration value. |
| comments | Optional comment. |
| enabled | If TRUE (the default), the 文件监视器 is 已启用. |
使用说明
You must have the `CREATE` `JOB` system privilege to create a 文件监视器 in your own schema. You require the `CREATE` `ANY` `JOB` system privilege to create a 文件监视器 in a schema different from your own (except the `SYS` schema, which is disallowed).
#### CREATE_GROUP Procedure
此过程 creates a group. Groups contain members, which you can specify when you create the group or at a later time. There are three types of groups: 窗口组, database 目标 groups, and external 目标 groups.
You can use a group name in other `DBMS_SCHEDULER` package procedures to specify a list of objects. For example, to specify multiple 目标s for a remote database job, you provide a group name for the `DESTINATION_NAME` parameter of the job.
语法

DBMS_SCHEDULER.CREATE_GROUP (
   group_name           IN VARCHAR2,
   group_type           IN VARCHAR2,
   member               IN VARCHAR2 DEFAULT NULL,
   comments             IN VARCHAR2 DEFAULT NULL);

参数
Table 159-26 CREATE_GROUP Procedure Parameters
| Parameter | Description |
|---|---|
| group_name | The name to assign to the group. It can optionally be prefixed with a schema name. It cannot be NULL. It is converted to uppercase unless enclosed in double quotation marks. |
| group_type | The type of members in the group. All members must be of the same type. Possible types are: 'DB_DEST' Database 目标: Members are database 目标s, for running remote database jobs. 'EXTERNAL_DEST External 目标: Members are external 目标s, for running remote 外部作业s. 'WINDOW' Members are Scheduler 窗口. You must have the MANAGE SCHEDULER privilege to create a group of this type. Members in database 目标 and external 目标 groups have the following format:[[schema.]凭据@][schema.]目标where: 凭据 is the name of an existing 凭据. 目标 is the name of an existing database 目标 or external 目标. The 凭据 portion of a 目标 member is optional. If omitted, the job using this 目标 member uses its default 凭据. Members in 窗口组 are window names. Because all Scheduler 窗口 reside in the SYS schema, you do not specify a schema name for windows. |
| member | Optional comma-separated list of group members. 默认为 NULL. If NULL, use the ADD_GROUP_MEMBER procedure to add members. You can also use ADD_GROUP_MEMBER to add additional members at a later time. The keyword LOCAL can be used as a member in database 目标 groups and external 目标 groups. In database 目标 groups, LOCAL represents the source database on which the job is created. It cannot be preceded with a 凭据. In external 目标 groups, LOCAL represents the host on which the source database resides. It can be optionally preceded with a 凭据 name. If no 凭据 is provided, jobs that use this group as their 目标 must have a default 凭据. |
| comments | A text string that describes the group. Scheduler does not use this 参数. |
使用说明
Groups reside in a particular schema and can be created by any user with the `CREATE JOB` system privilege. To create a group in a schema other than your own, you must have the `CREATE ANY JOB` privilege. The group name must be unique among all Scheduler objects.
You can grant the `SELECT` or `READ` privilege on a group so that other users can reference the group when creating jobs or schedules. To enable other users to modify a group, you can grant the `ALTER` privilege on the group.
Each group member must be unique within the group. For 目标 groups, the 凭据/目标 name pairs must be unique within the group. An error is generated if any of the group members do not exist. For 目标 groups, both the 凭据 and 目标 portions of a member must exist.
Another group of the same type can be a group member. 调度器 immediately expands the included group name into its list of members.
Groups are created 已启用, but you can disable them.
示例
The following PL/SQL block creates a group named `production_dest1`, whose members are database 目标s for a collection of production databases.

BEGIN
  DBMS_SCHEDULER.CREATE_GROUP(
    GROUP_NAME    => 'production_dest1',
    GROUP_TYPE    => 'DB_DEST',
    MEMBER        => 'LOCAL, oracle_cred@prodhost1, prodhost2',
    COMMENTS      => 'All sector1 production machines');
END;

#### CREATE_INCOMPATIBILITY Procedure
此过程 creates an incompatibility definition.
语法

DBMS_SCHEDULER.CREATE_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2,
   constraint_level        IN VARCHAR2 DEFAULT 'JOB_LEVEL',
   enabled                 IN BOOLEAN DEFAULT TRUE,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-27 CREATE_INCOMPATIBILITY Procedure Parameters
| Parameter | Description |
|---|---|
| incompatibility_name | The name of the incompatibility definition. |
| object_name | One or more (comma-separated) programs or jobs. |
| constraint_level | One or more (comma-separated) programs or jobs. |
| enabled | Specifies whether the constraint is initially 已启用 (true) or not 已启用 (false). |
| comments | Optional descriptive comment. |
使用说明
If `object_name` contains multiple (comma-separated) values, they must be either all programs or all jobs that are incompatible with each other (that is, they cannot be run at the same time). For jobs, the list must consist of two or more jobs, and `constraint_level` must be ‘JOB_LEVEL’. For programs, `constraint_level` can be either `'JOB_LEVEL'` or '`PROGRAM_LEVEL'`. When set to the default value `'JOB_LEVEL’`, only a single job that is based on the program (or programs) mentioned in `object_name` can run at the same time. When `constraint_level` is set to `'PROGRAM_LEVEL'`, the programs are incompatible, but the jobs based on the same program are not incompatible.
For example, if the value of `object_name` is `'P1,P2,P3'` and `constraint_level` is `'PROGRAM_LEVEL’`, many jobs based on P1 can be running at the same time, but if any P1 based job is running, none based on P2 or P3 can be running. Or, similarly, many jobs based on P3 can be running at the same time, but none based on P1 or P2. If `constraint_level` is set to `'JOB_LEVEL'`, then only a single job out of all the jobs based on programs P1, P2 and P3 can be running at a time.
参见：
Using Incompatibility Definitionsin Oracle Database Administrator’s Guide
#### CREATE_JOB Procedure
此过程 creates a single job.
If you create the job as 已启用 by setting the `已启用` 属性 to `TRUE`, 调度器 automatically runs the job according to its schedule. If you create the job 已禁用, the job does not run until you enable it with the SET_ATTRIBUTE Procedure.
The procedure is overloaded. The different functionality of each form of syntax is presented along with the syntax declaration.
语法
Creates a job in a single call without using an existing program or schedule:

DBMS_SCHEDULER.CREATE_JOB (
   job_name             IN VARCHAR2,
   job_type             IN VARCHAR2,
   job_action           IN VARCHAR2,
   number_of_arguments  IN PLS_INTEGER              DEFAULT 0,
   start_date           IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   repeat_interval      IN VARCHAR2                 DEFAULT NULL,
   end_date             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class            IN VARCHAR2                 DEFAULT 'DEFAULT_JOB_CLASS',
   enabled              IN BOOLEAN                  DEFAULT FALSE,
   auto_drop            IN BOOLEAN                  DEFAULT TRUE,
   comments             IN VARCHAR2                 DEFAULT NULL,
   credential_name      IN VARCHAR2                 DEFAULT NULL,
   destination_name     IN VARCHAR2                 DEFAULT NULL);

Creates a job using a named schedule object and a named program object:

DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   program_name            IN VARCHAR2,
   schedule_name           IN VARCHAR2,
   job_class               IN VARCHAR2              DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN               DEFAULT FALSE,
   auto_drop               IN BOOLEAN               DEFAULT TRUE,
   comments                IN VARCHAR2              DEFAULT NULL,
   job_style               IN VARCHAR2              DEFAULT 'REGULAR',
   credential_name         IN VARCHAR2              DEFAULT NULL,
   destination_name        IN VARCHAR2              DEFAULT NULL);

Creates a job using a named program object and an inlined schedule:

DBMS_SCHEDULER.CREATE_JOB (
   job_name             IN VARCHAR2,
   program_name         IN VARCHAR2,
   start_date           IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   repeat_interval      IN VARCHAR2                 DEFAULT NULL,
   end_date             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class            IN VARCHAR2                 DEFAULT 'DEFAULT_JOB_CLASS',
   enabled              IN BOOLEAN                  DEFAULT FALSE,
   auto_drop            IN BOOLEAN                  DEFAULT TRUE,
   comments             IN VARCHAR2                 DEFAULT NULL,
   job_style            IN VARCHAR2                 DEFAULT 'REGULAR',
   credential_name      IN VARCHAR2                 DEFAULT NULL,
   destination_name     IN VARCHAR2                 DEFAULT NULL);

Creates a job using a named schedule object and an inlined program:

DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   schedule_name           IN VARCHAR2,
   job_type                IN VARCHAR2,
   job_action              IN VARCHAR2,
   number_of_arguments     IN PLS_INTEGER       DEFAULT 0,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);

Creates a job using an inlined program and an event:

DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   job_type                IN VARCHAR2,
   job_action              IN VARCHAR2,
   number_of_arguments     IN PLS_INTEGER       DEFAULT 0,
   start_date              IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   event_condition         IN VARCHAR2          DEFAULT NULL,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);

Creates a job using a named program object and an event:

DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   program_name            IN VARCHAR2,
   start_date              IN TIMESTAMP WITH TIME ZONE,
   event_condition         IN VARCHAR2,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   job_style               IN VARCHAR2          DEFAULT 'REGULAR',
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);

参数
Table 159-28 CREATE_JOB Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name to assign to the job. The name must be unique in the SQL namespace. For example, a job cannot have the same name as a table in a schema. If the job being created will reside in another schema, it must be qualified with the schema name. If job_name is not specified, an error is generated. If you want to have a name generated by 调度器, you can use the GENERATE_JOB_NAME procedure to generate a name and then use the output in the CREATE_JOB procedure. The GENERATE_JOB_NAME procedure generates a number from a sequence, which is the job name. You can prefix the number with a string. The job name will then be the string with the number from the sequence appended to it. See "GENERATE_JOB_NAME Function" for more information. |
| job_type | This 属性 specifies the type of job that you are creating. If it is not specified, an error is generated. See job_action in the next row for related information. The supported values are: 'PLSQL_BLOCK' This specifies that the job is an anonymous PL/SQL block. Job or 程序参数 are not supported when the job or program type is PLSQL_BLOCK. In this case, the number of 参数s must be 0. 'STORED_PROCEDURE' This specifies that the job is a PL/SQL or Java stored procedure, or an external C subprogram. Only procedures, not functions with return values, are supported. 'EXECUTABLE' This specifies that the job is going to be run outside the database using an external executable. External jobs are anything that can be executed from the command line of the operating system. Anydata 参数s are not supported with a job or program type of EXECUTABLE. The job owner must have the CREATE EXTERNAL JOB system privilege before the job can be 已启用 or run. 'CHAIN' This specifies that the job is a chain. Arguments are not supported for a chain, so number_of_arguments must be 0. 'EXTERNAL_SCRIPT' This specifies that the job is an external script that uses the command shell of the computer running the job. For Windows this is cmd.exe and for UNIX based systems the sh shell, unless a different interpreter is specified by prefixing the first line of the script with #!. 'SQL_SCRIPT' This specifies that the job is a SQL*Plus script. The job must point to a 凭据 that contains a valid operating system username and password. The SQL*Plus script is run by the SQL*Plus executable. The job may point to a connect 凭据 that contains a database 凭据. If so, this 凭据 is used to connect to the database before running the SQL*Plus script. Note that if you choose to use connect 凭据, you must use set_attribute to specify the Connect_Credential_Name 属性. If you do not have connect 凭据, you must include an explicit SQL*Plus connect statement providing a valid database userid / password. The job owner must have the CREATE EXTERNAL JOB system privilege. 'BACKUP_SCRIPT' This specifies that the job is an RMAN backup script. The script runs a connect statement that uses either a password or OS authentication before it executes any target commands. The job points to a 凭据 that contains a valid operating system username and password. The RMAN session runs under this operating system user. 调度器 uses the RMAN executable from the current Oracle home to run the script and throws an error if this is missing. The job owner must have the CREATE EXTERNAL JOB system privilege. |
| job_action | This attribute specifies the action of the job. If job_action is not specified for an inline program, then an error is generated when creating the job. The job action is executed inside an autonomous transaction, and all autonomous transaction guidelines and restrictions apply. For example, online DDL operations are not allowed inside an autonomous transaction, and therefore cannot be used in the job action. The following actions are possible: For a PL/SQL block: The action is to execute PL/SQL code. These blocks must end with a semicolon. For example, my_proc(); or BEGIN my_proc(); END; or DECLARE arg pls_integer:= 10; BEGIN my_proc2(arg); END;. Note that the Scheduler wraps job_action in its own block and passes the following to PL/SQL for execution: DECLARE ... BEGIN job_action END; This is done to declare some internal Scheduler variables. You can include any Scheduler metadata attribute except event_message in your PL/SQL code. You use the attribute name as you use any other PL/SQL identifier, and the Scheduler assigns it a value. See Table 159-40 for details on available metadata attributes. For a stored procedure: The action is the name of the stored procedure. You have to specify the schema if the procedure resides in another schema than the job. If case sensitivity is needed, enclose the schema name and the store procedure name in double quotes. For example, job_action=>'"Schema"."Procedure"'. PL/SQL procedures with INOUT or OUT arguments are not supported as job_action when the job or program type is STORED_PROCEDURE. For an executable: The action is the name of the external executable, including the full path name, but excluding any command-line arguments. If the action starts with a single question mark ('?'), the question mark is replaced by the path to the Oracle home directory for a local job or to the Scheduler agent home for a remote job. If the action contains an at-sign ('@') and the job is local, the at-sign is replaced with the SID of the current Oracle instance. NOTE: Shell script syntax is not supported, only syntax for the name of and path to an executable is supported. For a chain: The action is the name of a Scheduler chain object. You must specify the schema of the chain if it resides in a different schema than the job. For an external script: The job_action must be either the path to an operating system script or an inline operating system script. If the job_action is a path to a script, then the script must reside on every computer that the job runs on. The job_action may contain calls to SQL*Plus or RMAN executables directly, without having to specify its full path, given that they are stored on their default location for every computer that runs the job. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. The job must point to a credential that contains a valid operating system username and password. For a SQL script: The job_action must be either the path to a SQL*Plus script or an inline SQL*Plus script. If the job_action is a path to a script, then the script must reside on every computer that the job runs on. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. If the arguments are named, they are also bound to named variables in the SQL*Plus session. For a backup script: The job_action is either the path to a RMAN script or an inline RMAN script. If the program_action is a path to a script, then the script must reside on every computer that the program runs on. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. |
| number_of_arguments | This 属性 specifies the number of 参数s that the job expects. The range is 0-255, with the default being 0. |
| program_name | The name of the program associated with this job. If the program is of type EXECUTABLE, the job owner must have the CREATE EXTERNAL JOB system privilege before the job can be 已启用 or run. |
| start_date | This 属性 specifies the first date and time on which this job is scheduled to start. If start_date and repeat_interval are left null, then the job is scheduled to run as soon as the job is 已启用. For repeating jobs that use a 日历表达式 to specify the 重复间隔, start_date is used as a reference date. The first time the 作业运行s is the first match of the 日历表达式 that is on or after the current date and time. 调度器 cannot guarantee that a job executes on an exact time because the system may be overloaded and thus 资源s unavailable. |
| event_condition | This is a conditional expression based on the columns of the event 源队列 table. The expression must have the syntax of an Advanced Queuing rule. Accordingly, you can include user data properties in the expression provided that the message payload is an object type, and that you prefix object 属性s in the expression with tab.user_data. For more information on rules, see the DBMS_AQADM.ADD_SUBSCRIBER procedure. |
| queue_spec | This 参数 specifies either of the following: The 源队列 where events that start this particular job are enqueued. If it is secure, then the queue_spec 参数 is a pair of values of the form queue_name, agent name. If it is not secure, then only the queue name need be provided. If a fully qualified queue name is not provided, the queue is assumed to be in the job owner's schema. In the case of secure queues, the agent name provided should belong to a valid agent that is currently subscribed to the queue. A 文件监视器 name. For more information on this option, see Oracle Database Administrator's Guide. |
| repeat_interval | This 属性 specifies how often the job repeats. You can specify the 重复间隔 by using calendaring or PL/SQL expressions. The expression specified is evaluated to determine the next time the job should run. If repeat_interval is not specified, the 作业运行s only once at the specified start date. See "Calendaring Syntax" for further information. |
| schedule_name | The name of the schedule, window, or 窗口组 associated with this job. |
| job_class | The class this job is associated with. |
| end_date | This 属性 specifies the date and time after which the job expires and is no longer run. After the end_date, if auto_drop is TRUE, the job is dropped. If auto_drop is FALSE, the job is 已禁用 and the STATE of the job is set to COMPLETED. If no value for end_date is specified, the job repeats forever unless max_runs or max_failures is set, in which case the job stops when either value is reached. The value for end_date must be after the value for start_date. If end_date is less than start_date, then an error will be generated. If end_date is the same as start_date, then the job will not execute and no error will be generated. |
| comments | This 属性 specifies a comment about the job. By default, this 属性 is NULL. |
| job_style | Style of the job being created. This 参数 can have one of the following values: 'REGULAR' creates a regular job. This is the default. 'LIGHTWEIGHT' creates a 轻量级作业. This value is permitted only when the job references a program object. Use 轻量级作业s when you have many short-duration jobs that run frequently. Under certain circumstances, using 轻量级作业s can deliver a small performance gain. 'IN_MEMORY_RUNTIME' creates an in-memory runtime job. These jobs are based on 轻量级作业 structures, so the same rules and restrictions apply; however, they further boost performance by keeping an in-memory cache, so they minimize disk access for pre-run and post-run actions. 'IN_MEMORY_FULL' creates an in-memory full job. In-memory full jobs require a program and cannot have a schedule or 重复间隔. They run automatically when the job is 已启用, and after running they are discarded. They keep all the job information in memory and are not backed up on disk, meaning that they are lost when the instance is rebooted. They are designed to run actions that must be performed immediately with the least amount of overhead possible. |
| credential_name | The default 凭据 to use with the job. Applicable only to remote database jobs, remote 外部作业s, local 外部作业s, script jobs, and event-based jobs that process file arrival events. The 凭据 must exist. For local database jobs, it must be NULL. For local 外部作业s only, if this 属性 is NULL (the default), then a preferred (default) 凭据 is selected. See Oracle Database Administrator's Guide for information about preferred 凭据s for local 外部作业s. See also: "CREATE_CREDENTIAL Procedure" |
| destination_name | The database 目标 or external 目标 for the job. Use for remote database jobs and remote 外部作业s only. Must be NULL for jobs running on the local database or for local 外部作业s (executables). This 属性 can be a single 目标 name or the name of a group of type 'EXTERNAL_DEST' or 'DB_DEST'. The single 目标 or group must already exist. The following applies to this 属性: If it is a database 目标, it must have been created by the CREATE_DATABASE_DESTINATION Procedure. If it is an external 目标, it must have been implicitly created by registering a remote Scheduler agent with the local database. If it is a group, each member of the group must exist, and the job must run on all 目标s named in the group. See "CREATE_GROUP Procedure". destination_name cannot reference a 目标 group when: The job type is 'CHAIN' The job style is 'LIGHTWEIGHT', 'IN_MEMORY_RUNTIME', or 'IN_MEMORY_FULL', If the credential_name 参数 of CREATE_JOB is NULL, each 目标 must be preceded by a 凭据, in the following format: 凭据.destinationThe 凭据 must already exist. If the credential_name 参数 is provided, then it serves as the default 凭据 for every 目标 that is not preceded by a 凭据. You can query the views *_SCHEDULER_DB_DESTS and ALL_SCHEDULER_EXTERNAL DESTS for existing 目标s and *_SCHEDULER_GROUP_MEMBERS for existing groups and their members. *** 目标 job 属性 is deprecated in Oracle Database 11gR2 and superseded by destination_name. |
| enabled | This 属性 specifies whether the job is created 已启用 or not. The possible settings are TRUE or FALSE. By default, this 属性 is set to FALSE and, therefore, the job is created as 已禁用. A 已禁用 job means that the metadata about the job has been captured, and the job exists as a database object. However, 调度器 ignores the job and the job coordinator does not pick it for processing. In order for the job coordinator to process the job, the job must be 已启用. You can enable a job by setting this 参数 to TRUE or by using the ENABLE procedure. |
| auto_drop | This flag, if TRUE, causes a job to be automatically dropped after it has completed or has been automatically 已禁用. A job is considered completed if: Its end date (or the end date of the job schedule) has passed. Note that a job with a Window schedule will not be auto-dropped when the window closes, because this is not considered to be the end of the Window. It has run max_runs number of times. max_runs must be set with SET_ATTRIBUTE. It is not a repeating job and has run once. A job is 已禁用 when it has failed max_failures times. max_failures is also set with SET_ATTRIBUTE. If this flag is set to FALSE, the jobs are not dropped and their metadata is kept until the job is explicitly dropped with the DROP_JOB procedure. By default, jobs are created with auto_drop set to TRUE. |
使用说明
Jobs are created as 已禁用 by default. You must explicitly enable them so that they will become active and scheduled. Before enabling a job, ensure that all 程序参数, if any, are defined, either by defining default values in the program object or by supplying values with the job.
The `JOB_QUEUE_PROCESSES` initialization parameter specifies the maximum number of processes that can be created for the execution of jobs. Beginning with Oracle Database 11g Release 2, `JOB_QUEUE_PROCESSES` applies to `DBMS_SCHEDULER` jobs. Setting this parameter to 0 disables `DBMS_SCHEDULER` jobs.
To create a job in your own schema, you need to have the `CREATE` `JOB` privilege. A user with the `CREATE` `ANY` `JOB` privilege can create a job in any schema. If the job being created will reside in another schema, the job name must be qualified with the schema name. For a job of type `EXECUTABLE` (or for a job that points to a program of type `EXECUTABLE`), the job owner must have the `CREATE EXTERNAL JOB` system privilege before the job can be 已启用 or run.
Associating a job with a particular class or program requires `EXECUTE` privileges for that class or program.
Not all possible job 属性s can be set with `CREATE_JOB`. Some must be set after the job is created. For example, 作业参数 must be set with the SET_JOB_ARGUMENT_VALUE Procedure or the SET_JOB_ANYDATA_VALUE Procedure. Other job 属性s, such as `job_priority` and `max_runs`, are set with the SET_ATTRIBUTE Procedure.
To create multiple jobs efficiently, use the `CREATE_JOBS` procedure.
Note:
调度器 runs event-based jobs for each occurrence of an event that matches the event condition of the job. However, events that occur while the job is already running are ignored; the event gets consumed, but does not trigger another run of the job.
#### CREATE_JOB_CLASS Procedure
此过程 creates a 作业类. Job classes are created in the `SYS` schema.
语法

DBMS_SCHEDULER.CREATE_JOB_CLASS (
   job_class_name            IN VARCHAR2,
   resource_consumer_group   IN VARCHAR2 DEFAULT NULL,
   service                   IN VARCHAR2 DEFAULT NULL,
   logging_level             IN PLS_INTEGER
                                DEFAULT DBMS_SCHEDULER.LOGGING_RUNS,
   log_history               IN PLS_INTEGER DEFAULT NULL,
   comments                  IN VARCHAR2 DEFAULT NULL);

参数
Table 159-29 CREATE_JOB_CLASS Procedure Parameters
| Parameter | Description |
|---|---|
| job_class_name | The name to assign to the 作业类. Job classes can only be created in the SYS schema. This 属性 specifies the name of the 作业类 and uniquely identifies the 作业类. The name must be unique in the SQL namespace. For example, a 作业类 cannot have the same name as a table in a schema. |
| resource_consumer_group | This 属性 specifies the 资源使用者组 that his class is associated with. A 资源使用者组 is a set of synchronous or asynchronous sessions that are grouped together based on their processing needs. A 作业类 has a many-to-one relationship with a 资源使用者组. The 资源使用者组 that the 作业类 associates with determines the 资源s that are allocated to the 作业类. If a 资源使用者组 is dropped, 作业类es associated with it are then associated with the default 资源使用者组. If no 资源使用者组 is specified, 作业类es are associated with the default 资源使用者组. If the specified 资源使用者组 does not exist when creating the 作业类, an error occurs. |
| service | This 属性 specifies the database service that the jobs in this class have affinity to. In an Oracle RAC environment, this means that the jobs in this class only run on those database instances that are assigned to the specific service. Note that a service can be mapped to a 资源使用者组, so you can also control 资源s allocated to jobs by specifying a service. See DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING for details. If both the resource_consumer_group and service 属性s are specified, and if the service is mapped to a 资源使用者组, the resource_consumer_group 属性 takes precedence. If no service is specified, the 作业类 belongs to the default service, which means it has no service affinity and any one of the database instances within the cluster might run the job. If the service that a 作业类 belongs to is dropped, the 作业类 will then belong to the default service. If the specified service does not exist when creating the 作业类, then an error occurs. |
| logging_level | This 属性 specifies how much information is logged. The possible options are: DBMS_SCHEDULER.LOGGING_OFF No logging is performed for any jobs in this class. DBMS_SCHEDULER.LOGGING_RUNS 调度器 writes detailed information to the 作业日志 for all runs of each job in this class. This is the default. DBMS_SCHEDULER.LOGGING_FAILED_RUNS 调度器 logs only jobs that failed in this class. DBMS_SCHEDULER.LOGGING_FULL In addition to recording every run of a job, 调度器 records all operations performed on all jobs in this class. Every time a job is created, 已启用, 已禁用, altered (with SET_ATTRIBUTE), stopped, and so, an entry is recorded in the log. |
| log_history | This 属性 controls the number of days that 作业日志 entries for jobs in this class are retained. It helps prevent the 作业日志 from growing indiscriminately. The range of valid values is 0 through1000000. If set to 0, no history is kept. If NULL (the default), retention days are set by the log_history Scheduler 属性 (set with SET_SCHEDULER_ATTRIBUTE). |
| comments | This 属性 is for an optional comment about the 作业类. By default, this 属性 is NULL. |
使用说明
For users to create jobs that belong to a 作业类, the job owner must have `EXECUTE` privileges on the 作业类. Therefore, after the 作业类 has been created, `EXECUTE` privileges must be granted on the 作业类 so that users create jobs belonging to that class. You can also grant the `EXECUTE` privilege to a role.
Creating a 作业类 requires the `MANAGE` `SCHEDULER` system privilege.
#### CREATE_JOBS Procedure
此过程 creates multiple jobs and sets the values of their 参数s in a single call.
语法

DBMS_SCHEDULER.CREATE_JOBS (
   jobdef_array      IN SYS.JOB_DEFINITION_ARRAY,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-30 CREATE_JOBS Procedure Parameters
| Parameter | Description |
|---|---|
| jobdef_array | The array of job definitions. See "Data Structures" for a description of the JOB_DEFINITION_ARRAY and JOB_DEFINITION datatypes. |
| commit_semantics | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error. Previous successfully created jobs are committed to disk. This is the default. TRANSACTIONAL returns on the first error and everything that happened before that error is rolled back. ABSORB_ERRORS tries to absorb any errors and attempts to create the rest of the jobs on the list. It commits all successfully created jobs. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |
使用说明
此过程 creates many jobs in the context of a single transaction. To realize the desired performance gains, the jobs being created must be grouped in batches of sufficient size. Calling `CREATE_JOBS` with a small array size may not be much faster than calling `CREATE_JOB` once for each job.
You cannot use this procedure to create multiple-目标 jobs. That is, the `目标` 属性 of the `job_definition` object cannot reference a 目标 group.
示例
See Oracle Database Administrator's Guide.
#### CREATE_PROGRAM Procedure
此过程 creates a program.
语法

DBMS_SCHEDULER.CREATE_PROGRAM (
   program_name             IN VARCHAR2,
   program_type             IN VARCHAR2,
   program_action           IN VARCHAR2,
   number_of_arguments      IN PLS_INTEGER DEFAULT 0,
   enabled                  IN BOOLEAN DEFAULT FALSE,
   comments                 IN VARCHAR2 DEFAULT NULL);

参数
Table 159-31 CREATE_PROGRAM Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name to assign to the program. The name must be unique in the SQL namespace. For example, a program cannot have the same name as a table in a schema. If no name is specified, then an error occurs. |
| program_type | This 属性 specifies the type of program you are creating. If it is not specified then you get an error. These are the supported values for program_type: 'PLSQL_BLOCK' This specifies that the program is a PL/SQL block. Job or 程序参数 are not supported when the job or program type is PLSQL_BLOCK. In this case, the number of 参数s must be 0. 'STORED_PROCEDURE' This specifies that the program is a PL/SQL or Java stored procedure, or an external C subprogram. Only procedures, not functions with return values, are supported. PL/SQL procedures with INOUT or OUT 参数s are not supported. 'EXECUTABLE' This specifies that the job is going to be run outside the database using an external executable. External programs imply anything that can be executed from the operating system command line. AnyData 参数s are not supported with job or program type EXECUTABLE. 'EXTERNAL_SCRIPT' This specifies that the job is an external script that uses the command shell of the computer running the job. For Windows this is cmd.exe and for UNIX based systems the sh shell, unless a different interpreter is specified by prefixing the first line of the script with #!. 'SQL_SCRIPT' This specifies that the program is a SQL*Plus script. A job using this program must point to a 凭据 that contains a valid operating system username and password. The SQL*Plus script is run by SQL*Plus executable. The job using this program may point to a connect 凭据 that contains a database 凭据. If so, this 凭据 is used to connect to the database before running the SQL*Plus script. Note that if you choose to use connect 凭据, you must use set_attribute to specify the Connect_Credential_Name 属性. If you do not have connect 凭据, you must include an explicit SQL*Plus connect statement providing a valid database userid / password. 'BACKUP_SCRIPT' This specifies that the program is an RMAN backup script. The script runs a connect statement that uses either a password or OS authentication before it executes any target commands. 调度器 uses the RMAN executable from the current Oracle home to run the script and throws an error if this is missing. |
| program_action | This attribute specifies the action of the program. If program_action is not specified, an error is generated. The following actions are possible: For a PL/SQL block, the action is to execute PL/SQL code. These blocks must end with a semicolon. For example, my_proc(); or BEGIN my_proc(); END; or DECLARE arg pls_integer:= 10; BEGIN my_proc2(arg); END;. Note that the Scheduler wraps job_action in its own block and passes the following to PL/SQL for execution: DECLARE ... BEGIN job_action END; This is done to declare some internal Scheduler variables. You can include any Scheduler metadata attribute except event_message in your PL/SQL code. You use the attribute name as you use any other PL/SQL identifier, and the Scheduler assigns it a value. See Table 159-40 for details on available metadata attributes. If it is an anonymous block, special Scheduler metadata may be accessed using the following variable names: job_name, job_owner, job_start, window_start, window_end. For more information, see the "DEFINE_METADATA_ARGUMENT Procedure". For a stored procedure, the action is the name of the stored procedure. You have to specify the schema if the procedure resides in a schema other than the job. If case sensitivity is needed, enclose the schema name and the store procedure name in double quotes. For example, program_action=>'"Schema"."Procedure"'. For an executable, the action is the name of the external executable, including the full path name, but excluding any command-line arguments. If the action starts with a single question mark ('?'), the question mark is replaced by the path to the Oracle home directory for a local job or to the Scheduler agent home for a remote job. If the action contains an at sign ('@') and the job is local, the at sign is replaced with the SID of the current Oracle instance. For an external script, the action must be either the path to an operating system script or an inline operating system script. If the program_action is a path to a script, then the script must reside on every computer that the program runs on. The program_action may contain calls to SQL*Plus or RMAN executables directly, without having to specify its full path, given that they are stored on their default location for every computer that runs the job. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. The program points to a credential that contains a valid operating system username and password. For a SQL script, the action must be either the path to a SQL*Plus script or an inline SQL*Plus script. If the program_action is a path to a script, then the script must reside on every computer that the program runs on. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. If the arguments are named, they are also bound to named variables in the SQL*Plus session. For a backup script, the action must be either the path to a RMAN script or an inline RMAN script. If the program_action is a path to a script, then the script must reside on every computer that the program runs on. The job can only have arguments that are strings or that can be cast to strings. These arguments are passed positionally when the script is called. |
| number_of_arguments | This 属性 specifies the number of 参数s the program takes. If this parameter is not specified, then the default is 0. A program can have a maximum of 255 参数s. If the program_type is PLSQL_BLOCK, then this parameter is ignored. |
| enabled | This flag specifies whether the program should be created as 已启用 or not. If the flag is set to TRUE, then validity checks are made and the program is created as ENABLED if all the checks be successful. By default, this flag is set to FALSE, meaning not created 已启用. You can also call the ENABLE procedure to enable the program before it can be used. |
| comments | A comment about the program. By default, this 属性 is NULL. |
使用说明
To create a program in their own schema, users need the `CREATE` `JOB` privilege. A user with the `CREATE` `ANY` `JOB` privilege can create a program in any schema. A program is created in a 已禁用 state by default (unless the 已启用 parameter is set to `TRUE`). It cannot be executed by a job until it is 已启用.
To use your programs, other users must have `EXECUTE` privileges, therefore once a program has been created, you have to grant `EXECUTE` privileges on it.
参见：
"DEFINE_PROGRAM_ARGUMENT Procedure"
#### CREATE_RESOURCE Procedure
此过程 allows users to specify the 资源s used by jobs or to create a new 资源.
语法

DBMS_SCHEDULER.CREATE_RESOURCE (
  resource_name    IN VARCHAR2,
  units            IN PLS_INTEGER,
  status           IN VARCHAR2 DEFAULT 'ENFORCE_CONSTRAINTS',
  constraint_level IN VARCHAR2 DEFAULT 'JOB_LEVEL',
  comments         IN VARCHAR2 DEFAULT NULL);

参数
Table 159-32 CREATE_RESOURCE Procedure Parameters
| Parameter | Description |
|---|---|
| resource_name | The name of the 资源. |
| units | The number of units of this 资源 that the job or program uses. |
| status | The status of the 资源. ‘ENFORCE_CONSTRAINTS’. This is the default value, and when set, will force the scheduler to enforce 资源 limits. When the maximum number of units of this 资源 has been reached no additional jobs using this 资源 will get started. ‘IGNORE_CONSTRAINTS’. When set, the scheduler will ignore any constraints on this 资源. ‘BLOCKED_ALL_JOBS’. No jobs having a constraint on this 资源 will be allowed to run. The 资源 is considered to be permanently blocking until switched to one of the other two states. |
| constraint_level | Level of the constraint: JOB_LEVEL or PROGRAM_LEVEL. For incompatibilities, for JOB_LEVEL, the incompatibility members must be jobs; for PROGRAM_LEVEL the incompatibility members must be programs. |
| comments | Descriptive comment about the 资源. |
使用说明
The following example creates a new 资源.

BEGIN
   DBMS_SCHEDULER.CREATE_RESOURCE(
      resource_name => 'my_resource',
      units => 3,
      state => 'ENFORCE_CONSTRAINTS',
      comments => 'Resource1'
   )
END;
/

参见：
- Creating or Dropping a Resource in Oracle Database Administrator’s Guide
- SET_RESOURCE_CONSTRAINT Procedure
#### CREATE_SCHEDULE Procedure
此过程 creates a schedule.
语法

DBMS_SCHEDULER.CREATE_SCHEDULE (
   schedule_name          IN VARCHAR2,
   start_date             IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   repeat_interval        IN VARCHAR2,
   end_date               IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   comments               IN VARCHAR2 DEFAULT NULL);

参数
Table 159-33 CREATE_SCHEDULE Procedure Parameters
| Parameter | Description |
|---|---|
| schedule_name | The name to assign to the schedule. The name must be unique in the SQL namespace. For example, a schedule cannot have the same name as a table in a schema. If no name is specified, then an error occurs. |
| start_date | This 属性 specifies the first date and time on which this schedule becomes valid. For a repeating schedule, the value for start_date is a reference date. In this case, the start of the schedule is not the start_date; it depends on the 重复间隔 specified. start_date is used to determine the first instance of the schedule. If start_date is specified in the past and no value for repeat_interval is specified, the schedule is invalid. For a repeating job or window, start_date can be derived from the repeat_interval if it is not specified. If start_date is null, then the date that the job or window is 已启用 is used. start_date and repeat_interval cannot both be null. |
| repeat_interval | This 属性 specifies how often the schedule repeats. It is expressed using calendaring syntax. See "Calendaring Syntax" for further information. PL/SQL expressions are not allowed as 重复间隔s for named schedules. |
| end_date | The date and time after which jobs will not run and windows will not open. A non-repeating schedule that has no end_date is valid forever. end_date has to be after the start_date. If this is not the case, then an error is generated when the schedule is created. |
| comments | This 属性 specifies an optional comment about the schedule. By default, this 属性 is NULL. |
使用说明
此过程 requires the `CREATE` `JOB` privilege to create a schedule in your own schema or the `CREATE` `ANY` `JOB` privilege to create a schedule in someone else's schema by specifying `schema.schedule_name`. Once a schedule has been created, it can be used by other users. The schedule is created with access to `PUBLIC`. Therefore, there is no need to explicitly grant access to the schedule.
#### CREATE_WINDOW Procedure
此过程 creates a recurring time window and associates it with a 资源计划. You can then use the window to schedule jobs that run under the associated 资源计划. Windows are created in the `SYS` schema.
The procedure is overloaded.
语法
Creates a window using a named schedule object:

DBMS_SCHEDULER.CREATE_WINDOW (
   window_name             IN VARCHAR2,
   resource_plan           IN VARCHAR2,
   schedule_name           IN VARCHAR2,
   duration                IN INTERVAL DAY TO SECOND,
   window_priority         IN VARCHAR2 DEFAULT 'LOW',
   comments                IN VARCHAR2 DEFAULT NULL);

Creates a window using an inlined schedule:

DBMS_SCHEDULER.CREATE_WINDOW (
   window_name             IN VARCHAR2,
   resource_plan           IN VARCHAR2,
   start_date              IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   repeat_interval         IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   duration                IN INTERVAL DAY TO SECOND,
   window_priority         IN VARCHAR2 DEFAULT 'LOW',
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-34 CREATE_WINDOW Procedure Parameters
| Parameter | Description |
|---|---|
| window_name | The name to assign to the window. The name must be unique in the SQL namespace. All windows are in the SYS schema, so the preface 'SYS' is optional. |
| resource_plan | This 属性 specifies the 资源计划 that automatically activates when the window opens. When the window closes, the system switches to the appropriate 资源计划, which is usually the plan that was in effect before the window opened, but can also be the plan of a different window. Only one 资源计划 can be associated with a window. It may be NULL or the empty string (""). When it is NULL, the 资源计划 in effect when the window opens stays in effect for the duration of the window. When it is the empty string, the 资源 manager is 已禁用 for the duration of the window. If the window is open and the 资源计划 is dropped, then the 资源 allocation for the duration of the window is not affected. |
| start_date | This 属性 specifies the first date and time on which this window is scheduled to open. If the value for start_date specified is in the past or is not specified, the window opens as soon as it is created. For repeating windows that use a 日历表达式 to specify the 重复间隔, the value for start_date is a reference date. The first time the window opens depends on the 重复间隔 specified and the value for start_date. |
| duration | This 属性 specifies how long the window stays open. For example, 'interval '5' hour' for five hours. There is no default value for this 属性. Therefore, if no value is specified when the window is created, an error occurs. The duration is of type interval day to seconds and ranges from one minute to 99 days. |
| schedule_name | This 属性 specifies the name of the schedule associated with the window. |
| repeat_interval | This 属性 specifies how often the window repeats. It is expressed using 调度器 calendaring syntax. See "Calendaring Syntax" for more information. A PL/SQL expression cannot be used to specify the 重复间隔 for a window. The expression specified is evaluated to determine the next time the window opens. If no repeat_interval is specified, the window opens only once at the specified start date. |
| end_date | This 属性 specifies the date and time after which the window no longer opens. When the value for end_date is reached, the window is 已禁用. In the *_SCHEDULER_WINDOWS views, the 已启用 flag of the window is set to FALSE. A non-repeating window that has no value for end_date opens only once for the duration of the window. For a repeating window, if no end_date is specified, then the window keeps repeating forever. The end_date must be after the start_date. If it is not, then an error is generated when the window is created. |
| window_priority | This 属性 is only relevant when two windows overlap. Because only one window can be in effect at one time, the window priority determines which window opens. The two possible values for this 属性 are 'HIGH' and 'LOW'. A high priority window has precedence over a low priority window, therefore, the low priority window does not open if it overlaps a high priority window. By default, windows are created with priority 'LOW'. |
| comments | This 属性 specifies an optional comment about the window. By default, this 属性 is NULL. |
使用说明
Creating a window requires the `MANAGE` `SCHEDULER` privilege.
Scheduler 窗口 are the principal mechanism used to automatically switch 资源计划s according to a schedule. You can also manually activate a 资源计划 by using the `ALTER SYSTEM SET RESOURCE_MANAGER_PLAN` statement or the `DBMS_RESOURCE_MANAGER.SWITCH_PLAN` package procedure. Note that either of these manual methods can also disable 资源计划 switching by Scheduler 窗口. For more information, see Oracle Database Administrator's Guide and "SWITCH_PLAN Procedure".
#### DEFINE_ANYDATA_ARGUMENT Procedure
此过程 defines a name or default value for a program 参数 that is of a complex type and must be encapsulated within an `ANYDATA` object. A job that references the program can override the default value.
语法

DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT (
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   default_value           IN SYS.ANYDATA,
   out_argument            IN BOOLEAN DEFAULT FALSE);

参数
Table 159-35 DEFINE_ANYDATA_ARGUMENT Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name of the program to be altered. A program with this name must exist. |
| argument_position | The position of the 参数 as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique, so it can replace any 参数 already defined at this position. |
| argument_name | The name to assign to the 参数. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ANYDATA_VALUE Procedure. |
| argument_type | The datatype of the 参数 being defined. This is not verified or used by 调度器. It is only used by the user of the program when deciding what value to assign to the 参数. |
| default_value | The default value to be assigned to the 参数 encapsulated within an AnyData object. This is optional. |
| out_argument | This parameter is reserved for future use. It must be set to FALSE. |
使用说明
All 程序参数 from one to the `number_of_arguments` value must be defined before a program can be 已启用. If a default value for an 参数 is not defined with this procedure, a value must be defined in the job.
Defining a program 参数 requires that you be the owner of the program or have `ALTER` privileges on that program. You can also define a program 参数 if you have the `CREATE` `ANY` `JOB` privilege.
参见：
- "DEFINE_PROGRAM_ARGUMENT Procedure"
- "SET_JOB_ANYDATA_VALUE Procedure"
#### DEFINE_CHAIN_EVENT_STEP Procedure
此过程 adds or replaces a 链步骤 and associates it with an 事件计划 or an inline event.
Once started in a running chain, this step does not complete until the specified event has occurred. Every step in a chain must be defined before the chain can be 已启用 and used. Defining a step gives it a name and specifies what happens during the step. If a step already exists with this name, the new step replaces the old one.
语法

DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   event_schedule_name     IN VARCHAR2,
   timeout                 IN INTERVAL DAY TO SECOND DEFAULT NULL);
DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   event_condition         IN VARCHAR2,
   queue_spec              IN VARCHAR2,
   timeout                 IN INTERVAL DAY TO SECOND DEFAULT NULL);

参数
Table 159-36 DEFINE_CHAIN_EVENT_STEP Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain that the step is in |
| step_name | The name of the step |
| event_schedule_name | The name of the 事件计划 that the step waits for |
| timeout | This parameter is reserved for future use |
| event_condition | See the CREATE_EVENT_SCHEDULE Procedure |
| queue_spec | See the CREATE_EVENT_SCHEDULE Procedure |
使用说明
Defining a 链步骤 requires `ALTER` privileges on the chain either as the owner of the chain, or as a user with the `ALTER` object privilege on the chain or the `CREATE` `ANY` `JOB` system privilege.
You can base a 链步骤 on a 文件监视器 as well. To do this, provide the 文件监视器 name directly in the `queue_spec` parameter, or use a 文件监视器 schedule for the `event_schedule_name` parameter.
参见：
"DEFINE_CHAIN_STEP Procedure"
#### DEFINE_CHAIN_RULE Procedure
此过程 adds a new rule to an existing chain, specified as a condition-action pair. The condition is expressed using either SQL or 调度器 链 condition syntax and indicates the prerequisites for the action to occur. The action is a result of the condition being met.
An actual rule object is created to store the rule in the schema where the chain resides. If a rule name is given, this name is used for the rule object. If an existing rule name in the schema of the chain is given, the existing rule is altered. (A schema different than the schema of the chain cannot be specified). If no rule name is given, one is generated in the form `SCHED_RULE${N}`.
语法

DBMS_SCHEDULER.DEFINE_CHAIN_RULE (
   chain_name              IN VARCHAR2,
   condition               IN VARCHAR2,
   action                  IN VARCHAR2,
   rule_name               IN VARCHAR2 DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);

参数
Table 159-37 DEFINE_CHAIN_RULE Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to alter |
| condition | A boolean expression which must evaluate to TRUE for the action to be performed. Every chain must have a rule that evaluates to TRUE to start the chain. For this purpose, you can use a rule that has 'TRUE' as its condition if you are using Scheduler 链 condition syntax, or '1=1' as its condition if you are using SQL syntax. Scheduler Chain Condition Syntax See "Scheduler Chain Condition Syntax" and Oracle Database Administrator’s Guide for details SQL WHERE Clause Syntax Conditions expressed with SQL must use the syntax of a SELECT statement WHERE clause. You can refer to 链步骤 属性s by using the 链步骤 name as a bind variable. The bind variable syntax is :step_name.属性. (step_name refers to a typed object.) Possible 属性s are: completed, state, start_date, end_date, error_code, and duration. Possible values for the state 属性 include: 'NOT_STARTED', 'SCHEDULED', 'RUNNING', 'PAUSED', 'STALLED', 'SUCCEEDED', 'FAILED', and 'STOPPED'. If a step is in the state 'SUCCEEDED', 'FAILED', or 'STOPPED', its completed 属性 is set to 'TRUE', otherwise completed is 'FALSE'. |
| action | The action to be performed when the rule evaluates to TRUE. The action must consist of at least one keyword with an optional value and an optional delay clause. Possible actions include: [AFTER delay_interval] START step_1[,step_2 ...] STOP step_1[,step_2 ...] END [{end_value\| step_name.error_code}] At the beginning of the START action, a delay clause can specify a delay interval before performing the action. delay_interval is a formatted datetime interval of the form HH:MM:SS. The END action ends the chain with an error code equal to either the supplied end_value or the error code that step_name completes with. The default error code is 0, indicating a successful chain run. |
| rule_name | The name of the rule being created. If no rule_name is given, one is generated in the form SCHED_RULE$_{N}. |
| comments | An optional comment describing the rule. This is stored in the rule object created. |
Scheduler Chain Condition Syntax
调度器 链 condition syntax provides an easy way to construct a condition using the states and error codes of steps in the current chain.
Chain Condition Syntax
The following are the available constructs for Scheduler 链 condition syntax, which are all boolean expressions:

TRUE
FALSE
stepname [NOT] SUCCEEDED
stepname [NOT] FAILED
stepname [NOT] STOPPED
stepname [NOT] COMPLETED
stepname ERROR_CODE IN (integer, integer, integer ...)
stepname ERROR_CODE NOT IN (integer, integer, integer ...)
stepname ERROR_CODE = integer
stepname ERROR_CODE != integer
stepname ERROR_CODE <> integer
stepname ERROR_CODE > integer
stepname ERROR_CODE >= integer
stepname ERROR_CODE < integer
stepname ERROR_CODE <= integer

These boolean operators are available to create more complex conditions:

expression AND expression
expression OR expression
NOT (expression)

`integer` can be positive or negative. Parentheses may be used for clarity or to enforce ordering. You must use parentheses with the `NOT` operator.
PL/SQL code that runs as part of a step can set the value of `ERROR_CODE` for that step with the `RAISE_APPLICATION_ERROR` statement.
使用说明
Defining a chain rule requires `ALTER` privileges on the chain (either as the owner, or as a user with `ALTER` privileges on the chain or the `CREATE` `ANY` `JOB` system privilege).
You must define at least one rule that starts the chain and at least one that ends it. See the section "Adding Rules to a Chain" in Oracle Database Administrator's Guide for more information.
示例
The following are examples of using rule conditions and rule actions.
Rule Conditions Using Scheduler Chain Condition Syntax

'step1 completed'
-- satisfied when step step1 has completed. (step1 completed is also TRUE when any
-- of the following are TRUE: step1 succeeded, step1 failed, step1 stopped.)
'step1 succeeded and step2 succeeded'
-- satisfied when steps step1 and step2 have both succeeded
'step1 error_code > 100'
-- satisfied when step step1 has failed with an error_code greater than 100
'step1 error_code IN (1, 3, 5, 7)'
-- satisfied when step step1 has failed with an error_code of 1, 3, 5, or 7

Rule Conditions Using SQL Syntax

':step1.completed = ''TRUE'' AND :step1.end_date >SYSDATE-1/24'
--satisfied when step step1 completed less than an hour ago
':step1.duration > interval ''5'' minute'
-- satisfied when step step1 has completed and took longer than 5 minutes to complete

Rule Actions

'AFTER 01:00:00 START step1, step2'
--After an hour start steps step1 and step2
'STOP step1'
--Stop step step1
END step4.error_code'
--End the chain with the error code that step step4 finished with. If step4 has not completed, the chain will be ended unsuccessfully with error code 27435.
'END' or 'END 0'
--End the chain successfully (with error_code 0)
'END 100'
--End the chain unsuccessfully with error code 100.

#### DEFINE_CHAIN_STEP Procedure
此过程 adds or replaces a 链步骤 and associates it with a program or a nested chain. When the 链步骤 is started, the specified program or chain is run. If a step already exists with the name supplied in the `chain_name` 参数, the new step replaces the old one.
The chain owner must have `EXECUTE` privileges on the program or chain associated with the step. Only one program or chain can run during a step.
You cannot set all possible step 属性s with this procedure. Use the `ALTER_CHAIN` procedure to set additional 链步骤 属性s, such as `credential_name` and `destination_name`.
语法

DBMS_SCHEDULER.DEFINE_CHAIN_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   program_name            IN VARCHAR2);

参数
Table 159-38 DEFINE_CHAIN_STEP Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to alter. |
| step_name | The name of the step being defined. If a step already exists with this name, the new step replaces the old one. |
| program_name | The name of a program or chain to run during this step. The chain owner must have EXECUTE privileges on this program or chain. |
使用说明
Defining a 链步骤 requires `ALTER` privileges on the chain (either as the owner, or a user with `ALTER` privileges on the chain or the `CREATE` `ANY` `JOB` system privilege).
参见：
- "ALTER_CHAIN Procedure"
- "DEFINE_CHAIN_EVENT_STEP Procedure"
#### DEFINE_METADATA_ARGUMENT Procedure
此过程 defines a special metadata 参数 for the program. 调度器 can pass Scheduler metadata through this 参数 to your stored procedure or other executable. You cannot set values for jobs using this 参数.
语法

DBMS_SCHEDULER.DEFINE_METADATA_ARGUMENT (
  program_name            IN VARCHAR2,
  metadata_attribute      IN VARCHAR2,
  argument_position       IN PLS_INTEGER,
  argument_name           IN VARCHAR2 DEFAULT NULL);

参数
Table 159-39 DEFINE_METADATA_ARGUMENT Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name of the program to be altered |
| metadata_attribute | The metadata to be passed. Valid metadata 属性s are: 'job_name', 'job_subname', 'job_owner', 'job_start', 'window_start', 'window_end', and 'event_message'. Table 159-40 describes these 属性s in detail. |
| argument_position | The position of the 参数 as it is passed to the executable. The position cannot be greater than the number_of_arguments specified for the program. It must be unique, so it replaces any 参数 already defined at this position. |
| argument_name | The name to assign to the 参数. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures. |
Table 159-40 Metadata Attributes
| Metadata Attribute | Datatype | Description |
|---|---|---|
| job_name | VARCHAR2 | Name of the currently running job |
| job_subname | VARCHAR2 | Subname of the currently running job. The name + subname form a unique identifier for a job that is running a 链步骤. NULL if the job is not part of a chain. |
| job_owner | VARCHAR2 | Owner of the currently running job |
| job_scheduled_start | TIMESTAMP WITH TIME ZONE | When the currently running job was scheduled to start |
| job_start | TIMESTAMP WITH TIME ZONE | When the currently running job started |
| window_start | TIMESTAMP WITH TIME ZONE | If the job was started by a window, the time that the window opened |
| window_end | TIMESTAMP WITH TIME ZONE | If the job was started by a window, the time that the window is scheduled to close |
| event_message | (See Description) | For an event-based job, the message content of the event that started the job. The datatype of this 属性 depends on the queue used for the event. It has the same type as the USER_DATA column of the queue table. In the case of a file arrival event, event_message is of type SYS.SCHEDULER_FILEWATCHER_RESULT. See "SCHEDULER_FILEWATCHER_RESULT Object Type". |
使用说明
Defining a program 参数 requires that you be the owner of the program or have `ALTER` privileges on that program. You can also define a program 参数 if you have the `CREATE` `ANY` `JOB` privilege.
All metadata 属性s except `event_message` can be used in PL/SQL blocks that you enter into the `job_action` or `program_action` 属性s of jobs or programs, respectively. You use the 属性 name as you use any other PL/SQL identifier, and 调度器 assigns it a value.
#### DEFINE_PROGRAM_ARGUMENT Procedure
此过程 defines a name or default value for a program 参数. If no default value is defined for a program 参数, the job that references the program must supply an 参数 value. (The job can also override a default value.)
此过程 is overloaded.
语法
Defines a program 参数 without a default value:

PROCEDURE define_program_argument(
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   out_argument            IN BOOLEAN DEFAULT FALSE);

Defines a program 参数 with a default value:

PROCEDURE define_program_argument(
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   default_value           IN VARCHAR2,
   out_argument            IN BOOLEAN DEFAULT FALSE);

参数
Table 159-41 DEFINE_PROGRAM_ARGUMENT Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name of the program to be altered. A program with this name must exist. |
| argument_position | The position of the 参数 as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique so it replaces any 参数 already defined at this position. |
| argument_name | The name to assign to the 参数. It is optional, but must be unique for the program if specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ARGUMENT_VALUE Procedure. |
| argument_type | The datatype of the 参数 being defined. This is not verified or used by 调度器. The program user uses argument_type when deciding what value to assign to the 参数. Any valid SQL datatype is allowed. |
| default_value | The default value to be assigned to the 参数 if none is specified by the job. |
| out_argument | This parameter is reserved for future use. It must be set to FALSE. |
使用说明
All 程序参数 from 1 to the `number_of_arguments` value must be defined before a program can be 已启用. If a default value for an 参数 is not defined with this procedure, a value must be defined in the job.
Defining a program 参数 requires that you be the owner of the program or have `ALTER` privileges on that program. You can also define a program 参数 if you have the `CREATE` `ANY` `JOB` privilege.
`DEFINE_PROGRAM_ARGUMENT` only supports 参数s of SQL type. Therefore, 参数 values that are not of SQL type, such as booleans, are not supported as program or 作业参数.
参见：
- "DEFINE_ANYDATA_ARGUMENT Procedure"
- "SET_JOB_ARGUMENT_VALUE Procedure"
#### DISABLE Procedure
此过程 disables a program, job, chain, window, database 目标, external 目标, 文件监视器, or group. When an object is 已禁用, its `已启用` 属性 is set to `FALSE`.
语法

DBMS_SCHEDULER.DISABLE (
   name              IN VARCHAR2,
   force             IN BOOLEAN DEFAULT FALSE,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-42 DISABLE Procedure Parameters
| Parameter | Description |
|---|---|
| name | The name of the object being 已禁用. Can be a comma-delimited list. If a 作业类 name is specified, then all the jobs in the 作业类 are 已禁用. The 作业类 is not 已禁用. If a group name is specified, then the group is 已禁用, but the 已启用 state of the group members is unaffected. |
| force | If TRUE, objects are 已禁用 even if other objects depend on them. See the usage notes for more information. |
| commit_semantics | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR: The procedure returns on the first error and the previous disable operations that were successful are committed to disk. This is the default. TRANSACTIONAL: The procedure returns on the first error and everything that happened before that error is rolled back. This type is only supported when disabling a job or a list of jobs. In addition, this type is not supported when force is set to TRUE. ABSORB_ERRORS: The procedure tries to absorb any errors and disable the rest of the jobs and commits all the disable operations that were successful. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. This type is only supported when disabling a job or a list of jobs. |
使用说明
Windows must be preceded by `SYS`.
Disabling an object that is already 已禁用 does not generate an error.
The purpose of the `force` option is to point out dependencies. No dependent objects are altered.
To run `DISABLE` for a window or a group of type `WINDOW`, you must have the `MANAGE` `SCHEDULER` privilege.
You can use `DISABLE` with any schema except the `SYS` schema.
Jobs
Disabling a job means that, although the metadata of the job is there, it should not run and the job coordinator will not pick up these jobs for processing. When a job is 已禁用, its `state` in the job queue is changed to `已禁用`.
If `force` is set to `FALSE` and the job is currently running, an error is returned.
If `force` is set to `TRUE`, the job is 已禁用, but the currently running instance is allowed to finish.
For jobs with multiple 目标s, you cannot disable a child job at a specific 目标. Instead, you can disable the 目标.
Programs
When a program is 已禁用, the status is changed to 已禁用. A 已禁用 program implies that, although the metadata is still there, jobs that point to this program cannot run.
If `force` is set to `FALSE`, the program must not be referenced by any job, otherwise an error will occur.
If `force` is set to `TRUE`, those jobs that point to the program will not be 已禁用, however, they will fail at runtime because their program will not be valid.
Running jobs that point to the program are not affected by the `DISABLE` call and are allowed to continue
No 参数s that pertain to the program are affected when the program is 已禁用.
File Watchers
If `force` is set to `FALSE`, the 文件监视器 must not be referenced by any job, otherwise an error will occur. If you force disabling a 文件监视器, jobs that depend on it become 已禁用.
Windows
This means that the window will not open, however, the metadata of the window is still there, so it can be re已启用.
If `force` is set to `FALSE`, the window must not be open or referenced by any job otherwise an error occurs.
If `force` is set to `TRUE`, disabling a window that is open will succeed but the window will not be closed. It will prevent the window from opening in the future until it is re已启用.
When the window is 已禁用, those jobs that have the window as their schedule will not be 已禁用.
Window Groups
When a group of type `WINDOW` is 已禁用, jobs (other than a running job) that have the 窗口组 as their schedule will not run when the member windows open. However, a job that has one of the 窗口组 members as its schedule still runs.
The metadata of the 窗口组 is still there, so it can be re已启用. Note that the members of the 窗口组 will still open.
If `force` is set to `FALSE`, the 窗口组 must not have any members that are open or referenced by any job, otherwise an error will occur.
If `force` is set to `TRUE`:
- The 窗口组 is 已禁用 and the open window will be not closed or 已禁用. It will be allowed to continue to its end.
- The 窗口组 is 已禁用 but those jobs that have the 窗口组 as their schedule will not be 已禁用.
Job Chains
When a chain is 已禁用, the metadata for the chain is still there, but jobs that point to it will not be able to be run. This allows changes to the chain to be made safely without the risk of having an incompletely specified chain run.If `force` is set to `FALSE`, the chain must not be referenced by any job, otherwise an error will occur.If `force` is set to `TRUE`, those jobs that point to the chain will not be 已禁用, however, they will fail at runtime.Running jobs that point to this chain are not affected by the `DISABLE` call and are allowed to complete.
Database Destinations
When you disable a database 目标:
- The 目标 is skipped when a multiple 目标 作业运行s.
- If all 目标s are 已禁用 for a job, 调度器 generates an error when it attempts to run the job.

- The REFS_ENABLED column in *_SCHEDULER_JOB_DESTS is set to FALSE for all jobs that reference the database 目标.
External Destinations
When you disable an external 目标:
- Dependent database 目标s remain 已启用, but 调度器 generates an error when it attempts to run a job with a database 目标 that depends on the external 目标.

- The REFS_ENABLED column in *_SCHEDULER_JOB_DESTS is set to FALSE for all 外部作业s that reference the external 目标 and for all database jobs with a database 目标 that depends on the external 目标.
Groups
If you disable an external 目标 group or database 目标 group, 调度器 generates an error when it attempts to run a job that names the group as its 目标.
#### DROP_AGENT_DESTINATION Procedure
此过程 drops one or more external 目标s, also known as agent 目标s. It should be used only when the preferred method of dropping an external 目标, using the `schagent` utility to unregister a Scheduler agent with a database, is unavailable due to failures.
此过程 can be called only by the `SYS` user or a user with the `MANAGE` `SCHEDULER` privilege.
Note:
External 目标s are created on a source database only implicitly by registering an agent with the database. There is no user-callable `CREATE_AGENT_DESTINATION` procedure.
语法

DBMS_SCHEDULER.DROP_AGENT_DESTINATION (
   destination_name        IN VARCHAR2);

参数
Table 159-43 DROP_AGENT_DESTINATION Procedure Parameters
| Parameter | Description |
|---|---|
| destination_name | A comma-separated list of external 目标s to drop. Because user SYS owns all external 目标s, do not prefix them with a schema name. The procedure stops processing if it encounters an external 目标 that does not exist. All external 目标s processed before the error are dropped. Cannot be NULL. |
使用说明
When an external 目标 is dropped:

- All database 目标s that refer to the external 目标 are 已禁用 and their agent 属性 is set to NULL.
- Members of external 目标 groups that refer to the 目标 are removed from the group.
- All job instances in the *_SCHEDULER_JOB_DESTS views that refer to the external 目标 are also dropped.
- Jobs running against the 目标 are stopped.
#### DROP_CHAIN Procedure
此过程 drops an existing chain.
语法

DBMS_SCHEDULER.DROP_CHAIN (
   chain_name              IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-44 DROP_CHAIN Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to drop. Can also be a comma-delimited list of chains. |
| force | If force is set to FALSE, the chain must not be referenced by any job, otherwise an error will occur. If force is set to TRUE, all jobs pointing to the chain are 已禁用 before the chain is dropped.Running jobs that point to this chain are stopped before the chain is dropped. |
使用说明
Dropping a chain requires alter privileges on the chain (either as the owner, or a user with `ALTER` privileges on the chain or the `CREATE` `ANY` `JOB` system privilege).
All steps associated with the chain are dropped. If no 规则集 was specified when the chain was created, then the automatically created 规则集 and evaluation context associated with the chain are also dropped, so the user must have the privileges required to do this. See the `DBMS_RULE_ADM.DROP_RULE_SET` and `DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT` procedures for more information.
If `force` is `FALSE`, no jobs may be using this chain. If `force` is `TRUE`, any jobs that use this chain are 已禁用 before the chain is dropped (and any of these jobs that are running will be stopped).
#### DROP_CHAIN_RULE Procedure
此过程 removes a rule from an existing chain. The rule object corresponding to this rule will also be dropped. The chain will not be 已禁用. If dropping this rule makes the chain invalid, the user should first disable the chain to ensure that it does not run.
语法

DBMS_SCHEDULER.DROP_CHAIN_RULE (
   chain_name              IN VARCHAR2,
   rule_name               IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-45 DROP_CHAIN_RULE Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to alter |
| rule_name | The name of the rule to drop |
| force | If force is set to TRUE, the drop operation proceeds even if the chain is currently running. The running chain is not stopped or interrupted. If force is set to FALSE and the chain is running, an error is generated. |
使用说明
Dropping a chain rule requires alter privileges on the chain (either as the owner or as a user with `ALTER` privileges on the chain or the `CREATE` `ANY` `JOB` system privilege).
Dropping a chain rule also drops the underlying rule database object so you must have the privileges to drop this rule object. See the `DBMS_RULE_ADM.DROP_RULE` procedure for more information.
#### DROP_CHAIN_STEP Procedure
此过程 drops a 链步骤. If this 链步骤 is still used in the chain rules, the chain will be 已禁用.
语法

DBMS_SCHEDULER.DROP_CHAIN_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-46 DROP_CHAIN_STEP Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to alter |
| step_name | The name of the step being dropped. Can be a comma-separated list. |
| force | If force is set to TRUE, this succeeds even if this chain is currently running. The running chain will not be stopped or interrupted.If force is set to FALSE and this chain is currently running, an error is thrown. |
使用说明
Dropping a 链步骤 requires `ALTER` privileges on the chain (either as the owner or as a user with `ALTER` privileges on the chain or the `CREATE` `ANY` `JOB` system privilege).
#### DROP_CREDENTIAL Procedure
This deprecated procedure drops a 凭据.
Note:
此过程 is deprecated with Oracle Database 12c Release 1 (12.1). While the procedure remains available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the  DBMS_CREDENTIAL  package, specifically the DROP_CREDENTIAL Procedure.
语法

DBMS_SCHEDULER.DROP_CREDENTIAL (
   credential_name         IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-47 DROP_CREDENTIAL Procedure Parameters
| Parameter | Description |
|---|---|
| credential_name | The name of the 凭据 being dropped. This can optionally be prefixed with a schema name. This cannot be set to NULL. |
| force | If set to FALSE, the 凭据 must not be referenced by any job, or an error will occur. If set to TRUE, the 凭据 is dropped whether or not there are jobs referencing it. Jobs that reference the 凭据 will continue to point to a nonexistent 凭据 and throw an error at runtime. |
使用说明
Only the owner of a 凭据 or a user with the `CREATE ANY JOB` system privilege may drop the 凭据.
Running jobs that point to the 凭据 are not affected by this procedure and are allowed to continue.
#### DROP_DATABASE_DESTINATION Procedure
此过程 drops one or more database 目标s.
语法

DBMS_SCHEDULER.DROP_DATABASE_DESTINATION (
   destination_name        IN VARCHAR2);

参数
Table 159-48 DROP_DATABASE_DESTINATION Procedure Parameters
| Parameter | Description |
|---|---|
| destination_name | The name of the 目标 to drop. Can be a comma-separated list of database 目标s to drop. Each database 目标 can optionally be prefixed with a schema name. The procedure stops processing if it encounters a database 目标 that does not exist. All database 目标s processed before the error are dropped. Cannot be NULL. |
使用说明
Only the owner or a user with the `CREATE ANY JOB` system privilege may drop the database 目标.
When a database 目标 is dropped:
- All job instances that refer to the 目标 in the *_SCHEDULER_JOB_DESTS views are also dropped.
- Jobs running against the 目标 are stopped.
- Members of database 目标 groups that refer to the 目标 are removed from the group.
参见：
CREATE_DATABASE_DESTINATION Procedure
#### DROP_FILE_WATCHER Procedure
此过程 drops one or more 文件监视器s.
语法

DBMS_SCHEDULER.DROP_FILE_WATCHER (
   file_watcher_name       IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-49 DROP_FILE_WATCHER Procedure Parameters
| Parameter | Description |
|---|---|
| file_watcher_name | The 文件监视器 to drop. Can be a comma-separated list of 文件监视器s. Each 文件监视器 name can optionally be prefixed with a schema name. Cannot be NULL. |
| force | If set to FALSE, the 文件监视器 must not be referenced by any job, or an error occurs. If set to TRUE, the 文件监视器 is dropped whether or not there are jobs referencing it. In this case, jobs that reference the dropped 文件监视器 are 已禁用. |
使用说明
Only the owner of a 文件监视器 or a user with the `CREATE ANY JOB` system privilege may drop the 文件监视器.
Running jobs that point to the 文件监视器 are not affected by this procedure and are allowed to continue.
参见：
"CREATE_FILE_WATCHER Procedure"
#### DROP_GROUP Procedure
此过程 drops one or more groups.
语法

DBMS_SCHEDULER.DROP_GROUP (
   group_name       IN VARCHAR2,
   force            IN BOOLEAN DEFAULT FALSE);

参数
Table 159-50 DROP_GROUP Procedure Parameters
| Parameter | Description |
|---|---|
| group_name | A group to drop. Can be a comma-separated list of group names. Each group name can optionally be prefixed with a schema name. The procedure stops processing if it encounters a group that does not exist. All groups processed before the error are dropped. Cannot be NULL. |
| force | If FALSE, the group must not be referenced by any job, otherwise an error occurs. If TRUE, the group is dropped whether or not there are jobs referencing it. In this case, all jobs referencing the group are 已禁用 and all job instances that reference the group are removed from the *_SCHEDULER_JOB_DESTS views. |
使用说明
Only the owner or a user with the `CREATE ANY JOB` system privilege may drop a group. You must have the `MANAGE` `SCHEDULER` privilege to drop a group of type `WINDOW`.
参见：
"CREATE_FILE_WATCHER Procedure"
#### DROP_INCOMPATIBILITY Procedure
此过程 drops an existing incompatibility definition.
语法

DBMS_SCHEDULER.DROP_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2);

参数
Table 159-51 DROP_INCOMPATIBILITY Procedure Parameters
| Parameter | Description |
|---|---|
| incompatibility_name | The name of the incompatibility definition. |
使用说明
参见：
Using Incompatibility Definitions in Oracle Database Administrator’s Guide
#### DROP_JOB Procedure
此过程 drops one or more jobs or all jobs in one or more 作业类es. Dropping a job also drops all 参数 values set for that job.
语法

DBMS_SCHEDULER.DROP_JOB (
   job_name                IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE,
   defer                   IN BOOLEAN DEFAULT FALSE,
   commit_semantics        IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-52 DROP_JOB Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of a job or 作业类. Can be a comma-delimited list. For a 作业类, the SYS schema should be specified. If the name of a 作业类 is specified, the jobs that belong to that 作业类 are dropped, but the 作业类 itself is not dropped. |
| force | If force is set to TRUE, 调度器 first attempts to stop the running job instances (by issuing the STOP_JOB call with the force flag set to false), and then drops the jobs. |
| defer | If defer is set to TRUE, 调度器 allows the running jobs to complete and then drops the jobs. |
| commit_semantics | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and previous successful drop operations are committed to disk. This is the default. TRANSACTIONAL returns on the first error. Everything that happened before that error is rolled back. This type is not supported when force is set to TRUE. ABSORB_ERRORS tries to absorb any errors and drop the rest of the jobs, and commits all the successful drops. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Only STOP_ON_FIRST_ERROR is permitted when 作业类es are included in the job_name list. |
使用说明
If both `force` and `defer` are set to `FALSE` and a job is running at the time of the call, the attempt to drop that job fails. The entire call to `DROP_JOB` may then fail, depending on the setting of `commit_semantics`.
Setting both `force` and `defer` to `TRUE` results in an error.
Dropping a job requires `ALTER` privileges on the job either as the owner of the job or as a user with the `ALTER` object privilege on the job or the `CREATE` `ANY` `JOB` system privilege.
#### DROP_JOB_CLASS Procedure
此过程 drops a 作业类. Dropping a 作业类 means that all the metadata about the 作业类 is removed from the database.
语法

DBMS_SCHEDULER.DROP_JOB_CLASS (
   job_class_name          IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-53 DROP_JOB_CLASS Procedure Parameters
| Parameter | Description |
|---|---|
| job_class_name | The name of the 作业类. Can be a comma-delimited list. |
| force | If force is set to FALSE, a class being dropped must not be referenced by any jobs, otherwise an error occurs. If force is set to TRUE, jobs belonging to the class are 已禁用 and their class is set to the default class. Only if this is successful is the class dropped. Running jobs that belong to the 作业类 are not affected. |
使用说明
Dropping a 作业类 requires the `MANAGE` `SCHEDULER` system privilege.
#### DROP_PROGRAM Procedure
此过程 drops a program. Any 参数s that pertain to the program are also dropped when the program is dropped.
语法

DBMS_SCHEDULER.DROP_PROGRAM (
   program_name            IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-54 DROP_PROGRAM Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name of the program to be dropped. Can be a comma-delimited list. |
| force | If force is set to FALSE, the program must not be referenced by any job, otherwise an error occurs. If force is set to TRUE, all jobs referencing the program are 已禁用 before the program is dropped. Running jobs that point to the program are not affected by the DROP_PROGRAM call and are allowed to continue. |
使用说明
Dropping a program requires that you be the owner of the program or have `ALTER` privileges on that program. You can also drop a program if you have the `CREATE` `ANY` `JOB` privilege.
#### DROP_PROGRAM_ARGUMENT Procedure
此过程 drops a program 参数. An 参数 can be specified by either name (if one has been given) or position.
The procedure is overloaded.
语法
Drops a program 参数 by position:

DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT (
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER);

Drops a program 参数 by name:

DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT (
   program_name            IN VARCHAR2,
   argument_name           IN VARCHAR2);

参数
Table 159-55 DROP_PROGRAM_ARGUMENT Procedure Parameters
| Parameter | Description |
|---|---|
| program_name | The name of the program to be altered. A program with this name must exist. |
| argument_name | The name of the 参数 being dropped |
| argument_position | The position of the 参数 to be dropped |
使用说明
Dropping a program 参数 requires that you be the owner of the program or have `ALTER` privileges on that program. You can also drop a program 参数 if you have the `CREATE` `ANY` `JOB` privilege.
#### DROP_RESOURCE Procedure
此过程 drops a 资源.
语法

DBMS_SCHEDULER.DROP_RESOURCE (
   resource_name  IN VARCHAR2,
   force          IN BOOLEAN DEFAULT FALSE);

参数
Table 159-56 DROP_RESOURCE Procedure Parameters
| Parameter | Description |
|---|---|
| resource_name | The name of the 资源 to be dropped. Can be a comma-delimited list. |
| force | If force is set to FALSE, the 资源 must not have any existing constraints, otherwise an error occurs. If force is set to TRUE, the 资源 will be dropped and any constraints defined on this 资源 will also be dropped. |
使用说明
Only the owner or a user with the CREATE ANY JOB system privilege may drop the 资源.
参见：
Creating or Dropping a Resource in Oracle Database Administrator’s Guide
#### DROP_SCHEDULE Procedure
此过程 drops a schedule.
语法

DBMS_SCHEDULER.DROP_SCHEDULE (
   schedule_name    IN VARCHAR2,
   force            IN BOOLEAN DEFAULT FALSE);

参数
Table 159-57 DROP_SCHEDULE Procedure Parameters
| Parameter | Description |
|---|---|
| schedule_name | The name of the schedule. Can be a comma-delimited list. |
| force | If force is set to FALSE, the schedule must not be referenced by any job or window, otherwise an error will occur. If force is set to TRUE, any jobs or windows that use this schedule are 已禁用 before the schedule is dropped Running jobs and open windows that point to the schedule are not affected. |
使用说明
You must be the owner of the schedule being dropped or have `ALTER` privileges for the schedule or the `CREATE` `ANY` `JOB` privilege.
#### DROP_WINDOW Procedure
此过程 drops a window. All metadata about the window is removed from the database. The window is removed from any groups that reference it.
语法

DBMS_SCHEDULER.DROP_WINDOW (
   window_name             IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-58 DROP_WINDOW Procedure Parameters
| Parameter | Description |
|---|---|
| window_name | The name of the window. Can be a comma-delimited list. |
| force | If force is set to FALSE, the window must be not be open or referenced by any job, otherwise an error occurs. If force is set to TRUE, the window is dropped and those jobs that have the window as their schedule are 已禁用. However, jobs that have a 窗口组, of which the dropped window is a member, as their schedule, are not 已禁用. If the window is open then, 调度器 attempts to first close the window and then drop it. When the window is closed, normal close window rules apply. Running jobs that have the window as their schedule is allowed to continue, unless the stop_on_window_close flag is set to TRUE for the job. If this is the case, the job is stopped when the window is dropped. |
使用说明
Dropping a window requires the `MANAGE` `SCHEDULER` privilege.
#### ENABLE Procedure
此过程 enables a program, job, chain, window, database 目标, external 目标, 文件监视器, or group.
When an object is 已启用, its `已启用` 属性 is set to `TRUE`. By default, jobs, chains, and programs are created 已禁用 and database 目标s, external 目标s, 文件监视器s, windows, and groups are created 已启用.
If a job was 已禁用 and you enable it, 调度器 begins to automatically run the job according to its schedule. Enabling a 已禁用 job also resets the job `RUN_COUNT`, `FAILURE_COUNT` and `RETRY_COUNT` columns in the `*_SCHEDULER_JOBS` data dictionary views.
Validity checks are performed before enabling an object. If the check fails, the object is not 已启用, and an appropriate error is returned. 此过程 does not return an error if the object was already 已启用.
语法

DBMS_SCHEDULER.ENABLE (
   name              IN VARCHAR2,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-59 ENABLE Procedure Parameters
| Parameter | Description |
|---|---|
| name | The name of 调度器 object being 已启用. Can be a comma-delimited list of names. If a 作业类 name is specified, then all the jobs in the 作业类 are 已启用. If a group name is specified, then the group is 已启用, but the 已启用 state of the group members is unaffected. |
| commit_semantics | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR - The procedure returns on the first error and previous successful enable operations are committed to disk. This is the default. TRANSACTIONAL - The procedure returns on the first error and everything that happened before that error is rolled back. This type is only supported when enabling a job or a list of jobs. ABSORB_ERRORS - The procedure tries to absorb any errors and enable the rest of the jobs. It commits all the enable operations that were successful. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. This type is only supported when enabling a job or a list of jobs. |
使用说明
Window names must be preceded by `SYS`.
To run `ENABLE` for a window or group of type `WINDOW`, you must have the `MANAGE` `SCHEDULER` privilege. For a job of type `EXECUTABLE` (or for a job that points to a program of type `EXECUTABLE`), the job owner must have the `CREATE EXTERNAL JOB` system privilege before the job can be 已启用 or run.
To enable a 文件监视器, the 文件监视器 owner must have the `EXECUTE` privilege on the designated 凭据.
You can use `ENABLE` with any schema except the `SYS` schema.
#### END_DETACHED_JOB_RUN Procedure
此过程 ends a detached 作业运行. A detached job points to a detached program, which is a program with the `detached` 属性 set to `TRUE`.
A detached 作业运行 does not end until this procedure or the STOP_JOB Procedure is called.
语法

DBMS_SCHEDULER.END_DETACHED_JOB_RUN (
   job_name          IN VARCHAR2,
   error_number      IN PLS_INTEGER DEFAULT 0,
   additional_info   IN VARCHAR2 DEFAULT NULL);

参数
Table 159-60 END_DETACHED_JOB_RUN Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of the job to end. Must be a detached job that is running. |
| error_number | If zero, then the 作业运行 is logged as succeeded. If -1013, then the 作业运行 is logged as stopped. If any other number, then the 作业运行 is logged as failed with that error number. |
| additional_info | This text is stored in the additional_info column of the *_scheduler_job_run_details views for this 作业运行. |
使用说明
此过程 requires that you either own the job or have `ALTER` privileges on it. You can also end any detached 作业运行 if you have the `CREATE` `ANY` `JOB` privilege.
参见：
Oracle Database Administrator's Guide for information about detached jobs.
#### EVALUATE_CALENDAR_STRING Procedure
You can define 重复间隔s of jobs, windows or schedules using 调度器 calendaring syntax. 此过程 evaluates the 日历表达式 and tells you the next execution date and time of a job or window. This is very useful for testing the correct definition of the 日历字符串 without actually scheduling the job or window.
此过程 can also get multiple steps of the 重复间隔 by passing the `next_run_date` returned by one invocation as the `return_date_after` 参数 of the next invocation.
See the calendaring syntax described in "Operational Notes".
语法

DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING (
   calendar_string    IN  VARCHAR2,
   start_date         IN  TIMESTAMP WITH TIME ZONE,
   return_date_after  IN  TIMESTAMP WITH TIME ZONE,
   next_run_date      OUT TIMESTAMP WITH TIME ZONE);

参数
Table 159-61 EVALUATE_CALENDAR_STRING Procedure Parameters
| Parameter | Description |
|---|---|
| calendar_string | The 日历表达式 to be evaluated. The string must be in the calendaring syntax described in "Operational Notes". |
| start_date | The date and time after which the 重复间隔 becomes valid. It can also be used to fill in specific items that are missing from the 日历字符串. Can optionally be NULL. |
| return_date_after | The return_date_after 参数 helps 调度器 determine which one of all possible matches (all valid execution dates) to return from those determined by the start_date and the 日历字符串. When a NULL value is passed for this 参数, 调度器 automatically fills in systimestamp as its value. |
| next_run_date | The first timestamp that matches the 日历字符串 and start date that occur after the value passed in for the return_date_after 参数. |
示例
The following code fragment can be used to determine the next five dates a job will run given a specific 日历字符串.

SET SERVEROUTPUT ON;
ALTER SESSION set NLS_DATE_FORMAT = 'DD-MON-YYYY HH24:MI:SS';
Session altered.
DECLARE
start_date        TIMESTAMP;
return_date_after TIMESTAMP;
next_run_date     TIMESTAMP;
BEGIN
start_date :=
  to_timestamp_tz('01-JAN-2003 10:00:00','DD-MON-YYYY HH24:MI:SS');
return_date_after := start_date;
FOR i IN 1..5 LOOP
  DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING(
    'FREQ=DAILY;BYHOUR=9;BYMINUTE=30;BYDAY=MON,TUE,WED,THU,FRI',
    start_date, return_date_after, next_run_date);
DBMS_OUTPUT.PUT_LINE('next_run_date: ' || next_run_date);
return_date_after := next_run_date;
END LOOP;
END;
/
next_run_date: 02-JAN-03 09.30.00.000000 AM
next_run_date: 03-JAN-03 09.30.00.000000 AM
next_run_date: 06-JAN-03 09.30.00.000000 AM
next_run_date: 07-JAN-03 09.30.00.000000 AM
next_run_date: 08-JAN-03 09.30.00.000000 AM
PL/SQL procedure successfully completed.

使用说明
No specific Scheduler privileges are required.
#### EVALUATE_RUNNING_CHAIN Procedure
此过程 forces reevaluation of the rules of a running chain to trigger any rules for which the conditions have been satisfied. The job passed as an 参数 must point to a chain and must be running. If the job is not running, an error is thrown. (`RUN_JOB` can be used to start the job.)
If any of the steps of the chain are themselves running chains, another `EVALUATE_RUNNING_CHAIN` is performed on each of the nested running chains.
语法

DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN (
   job_name              IN VARCHAR2);

参数
Table 159-62 EVALUATE_RUNNING_CHAIN Procedure Parameter
| Parameter | Description |
|---|---|
| job_name | The name of the running job (pointing to a chain) to reevaluate the rules for |
使用说明
Running `EVALUATE_RUNNING_CHAIN` on a job requires alter privileges on the job (either as the owner, or as a user with `ALTER` privileges on the job or the `CREATE` `ANY` `JOB` system privilege).
Note:
调度器 automatically evaluates a chain:
- At the start of the chain job
- When a 链步骤 completes
- When an event occurs that is associated with an event step in the chain
For most chains, this is sufficient. `EVALUATE_RUNNING_CHAIN` should be used only under the following circumstances:
- After manual intervention of a running chain with the ALTER_RUNNING_CHAIN procedure
- When chain rules use SQL syntax and the rule conditions contain elements that are not under the control of 调度器.
In these cases, `EVALUATE_RUNNING_CHAIN` may not be needed if you set the `evaluation_interval` 属性 when you created the chain.
#### GENERATE_JOB_NAME Function
此函数 returns a unique name for a job.
The name will be of the form `{prefix}N` where `N` is a number from a sequence. If no prefix is specified, the generated name will, by default, be `JOB$_1`, `JOB$_2`, `JOB$_3`, and so on. If `'SCOTT'` is specified as the prefix, the name will be `SCOTT1`, `SCOTT2`, and so on.
语法

DBMS_SCHEDULER.GENERATE_JOB_NAME (
   prefix        IN VARCHAR2 DEFAULT 'JOB$_') RETURN VARCHAR2;

参数
Table 159-63 GENERATE_JOB_NAME Function Parameter
| Parameter | Description |
|---|---|
| prefix | The prefix to use when generating the job name |
使用说明
If the prefix is explicitly set to `NULL`, the name is just the sequence number. In order to successfully use such numeric names, they must be surrounded by double quotes throughout the `DBMS_SCHEDULER` calls. A prefix cannot be longer than 18 characters and cannot end with a digit.
Note that, even though the `GENERATE_JOB_NAME` function never returns the same job name twice, there is a small chance that the returned name matches an already existing database object.
No specific Scheduler privileges are required to use this function.
#### GET_AGENT_INFO Function
此函数 can return job information specific to an agent, such as how many are running and so on, depending on the 属性 selected.
语法

DBMS_SCHEDULER.GET_AGENT_INFO (
   agent_name        IN VARCHAR2,
   attribute         IN VARCHAR2) RETURN VARCHAR2;

参数
Table 159-64 GET_AGENT_INFO Function Parameter
| Parameter | Description |
|---|---|
| agent_name | The name of an external 目标 where the agent is running |
| attribute | Possible Attributes values VERSION:. Returns the agent version number. Requires the CREATE JOB system privilege. UPTIME: Returns the time the agent has been up and running. Requires the CREATE JOB system privilege. NUMBER_OF_RUNNING_JOBS: Returns the number of jobs that the agent is currently running. Requires the CREATE JOB system privilege. TOTAL_JOBS_RUN: Returns the number of jobs run by the agent since it was started. Requires the CREATE JOB system privilege. RUNNING_JOBS: Returns a comma-separated list of the names of the jobs running currently. Requires the MANAGE SCHEDULER system privilege. ALL: Returns all the information the previous options return. It requires the MANAGE SCHEDULER system privilege. |
使用说明
此函数 returns the same information as the `schagent` utility status option. See Oracle Database Administrator's Guide.
#### GET_AGENT_VERSION Function
此函数 returns the version string of a Scheduler agent that is registered with the database and is currently running. `GET_AGENT_VERSION` throws an error if the agent is not registered with the database or if the agent is not currently running.
语法

DBMS_SCHEDULER.GET_AGENT_VERSION (
   agent_host        IN VARCHAR2) RETURN VARCHAR2;

参数
Table 159-65 GET_AGENT_VERSION Function Parameter
| Parameter | Description |
|---|---|
| agent_host | Either the hostname and port on which the agent is running in the form hostname:port or the name of the agent as shown in the destination_name column of the ALL_SCHEDULER_EXTERNAL_DESTS view which lists all Scheduler agents registered with the database. |
使用说明
此函数 requires the `CREATE` `EXTERNAL` `JOB` system privilege.
#### GET_ATTRIBUTE Procedure
此过程 retrieves the value of an 属性 of a Scheduler object. It is overloaded to retrieve values of various types.
语法

DBMS_SCHEDULER.GET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          OUT {VARCHAR2|PLS_INTEGER|BOOLEAN|DATE|TIMESTAMP|
                        TIMESTAMP WITH TIME ZONE|TIMESTAMP WITH LOCAL TIME ZONE|
                        INTERVAL DAY TO SECOND});
DBMS_SCHEDULER.GET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          OUT VARCHAR2,
   value2         OUT VARCHAR2);

参数
Table 159-66 GET_ATTRIBUTE Procedure Parameters
| Parameter | Description |
|---|---|
| name | The name of the object |
| attribute | The 属性 being retrieved. See the SET_ATTRIBUTE Procedure for tables of 属性 values. |
| value | The existing value of the 属性 |
| value2 | The value2 参数 is for an optional second value. Most 属性s have only one value associated with them, but some can have two. |
使用说明
To run `GET_ATTRIBUTE` for a 作业类, you must have the `MANAGE` `SCHEDULER` privilege or have `EXECUTE` privileges on the class. For a schedule, window, or group, no privileges are necessary. Otherwise, you must be the owner of the object or have `ALTER` or `EXECUTE` privileges on that object or have the `CREATE ANY JOB` privilege.
See the SET_ATTRIBUTE Procedure for tables of 属性 values that you can retrieve for the various Scheduler object types.
#### GET_FILE Procedure
此过程 retrieves a file from the operating system file system of a specified host. The file is copied to a 目标, or its contents are returned in a procedure output parameter.
You can also use this procedure to retrieve the standard output or error text for a run of an 外部作业 that has an associated 凭据.
此过程s differs from the equivalent `UTL_FILE` procedure in that it uses a 凭据 and can retrieve files from remote hosts that have only a Scheduler agent (and not an Oracle database) installed.
语法

DBMS_SCHEDULER.GET_FILE (
   source_file                  IN VARCHAR2,
   source_host                  IN VARCHAR2,
   credential_name              IN VARCHAR2,
   file_contents                IN OUT NOCOPY {BLOB|CLOB});

DBMS_SCHEDULER.GET_FILE (
   source_file                  IN VARCHAR2,
   source_host                  IN VARCHAR2,
   credential_name              IN VARCHAR2,
   destination_file_name        IN VARCHAR2,
   destination_directory_object IN VARCHAR2,
   destination_permissions      IN VARCHAR2 DEFAULT NULL);

参数
Table 159-67 GET_FILE Procedure Parameters
| Parameter | Description |
|---|---|
| source_file | Fully qualified path name of the file to retrieve from the operating system. The file name is case-sensitive and is not converted to uppercase. If the file name starts with a question mark ('?'), the question mark is replaced by the path to the Oracle home if getting a file from the local host, or to 调度器 agent home if getting a file from a remote host. If the format of this parameter is external_log_id_stdout, then the stdout from the designated 外部作业 run is returned. If the format of this parameter is external_log_id_stderr, the error text from the designated 外部作业 run is returned. You obtain the value of external_log_id from the ADDITIONAL_INFO column of the *_SCHEDULER_JOB_RUN_DETAILS views. This column contains a set of name/value pairs in an indeterminate order, so you must parse this column for the external_log_id name/value pair, and then append either "_stdout" or "_stderr" to its value. The 外部作业 must have an associated 凭据. The credential_name parameter of GET_FILE must name the same 凭据 that is used by the job, and the source_host parameter must be the same as the 目标 属性 of the job. |
| source_host | If the file is to be retrieved from a remote host, then this parameter must be a valid an external 目标 name. (An external 目标 is created when you register a remote Scheduler agent with the database. You can view external 目标 names in the views *_SCHEDULER_EXTERNAL_DESTS.) If source_host is NULL or set to 'localhost', then the file is retrieved from the file system of the local host. To determine the port number of a Scheduler agent, view the schagent.conf file, which is located in 调度器 agent home directory on the remote host. |
| credential_name | The name of the 凭据 to use for accessing the file system. |
| file_contents | The variable into which the file contents is read. |
| destination_file_name | The file to which the file contents is written. |
| destination_directory_object | The directory object that specifies the path to the 目标 file, when destination_file_name is used. The caller must have the necessary privileges on the directory object. |
| destination_permissions | 保留供将来使用 |
使用说明
The caller must have the `CREATE EXTERNAL JOB` system privilege and have `EXECUTE` privileges on the 凭据.
#### GET_SCHEDULER_ATTRIBUTE Procedure
此过程 retrieves the value of a Scheduler 属性.
语法

DBMS_SCHEDULER.GET_SCHEDULER_ATTRIBUTE (
   attribute      IN VARCHAR2,
   value          OUT VARCHAR2);

参数
Table 159-68 GET_SCHEDULER_ATTRIBUTE Procedure Parameters
| Parameter | Description |
|---|---|
| attribute | The name of the 属性 |
| value | The existing value of the 属性 |
使用说明
To run `GET_SCHEDULER_ATTRIBUTE`, you must have the `MANAGE` `SCHEDULER` privilege.
Table 159-69 lists 调度器 属性s that you can retrieve. For more detail on these 属性s, see Table 159-101 and the section "Configuring 调度器" in Oracle Database Administrator's Guide.
Table 159-69 Scheduler Attributes Retrievable with GET_SCHEDULER_ATTRIBUTE
| Scheduler Attribute | Description |
|---|---|
| current_open_window | Name of the currently open window |
| default_timezone | Default time zone used by 调度器 for 重复间隔s and windows |
| email_sender | The default e-mail address of the sender for job state e-mail 通知s |
| email_server | The SMTP server address that 调度器 uses to send e-mail 通知s for job state events. E-mail 通知s cannot be sent if this 属性 is NULL. |
| event_expiry_time | Time in seconds before an event generated by 调度器 and enqueued onto 调度器 事件队列 expires. May be NULL. |
| log_history | Retention period in days for job and 窗口日志s. The range of valid values is 0 through 1000000. |
| max_job_slave_processes | This Scheduler 属性 is not used. |
#### OPEN_WINDOW Procedure
此过程 manually opens a window, unrelated to its schedule.
The window opens and the 资源计划 associated with it takes effect immediately, for the duration specified or for the normal duration of the window, if no duration is given. Only an 已启用 window can be manually opened.
语法

DBMS_SCHEDULER.OPEN_WINDOW (
   window_name             IN VARCHAR2,
   duration                IN INTERVAL DAY TO SECOND,
   force                   IN BOOLEAN DEFAULT FALSE);

参数
Table 159-70 OPEN_WINDOW Procedure Parameters
| Parameter | Description |
|---|---|
| window_name | The name of the window |
| duration | The duration of the window. It is of type interval day to second. If it is NULL, then the window opens for the regular duration as specified in the window metadata. |
| force | If force is set to FALSE, then opening an already open window generates an error. If force is set to TRUE: You can open a window that is already open. The window stays open for the duration specified in the call, from the time the OPEN_WINDOW command was issued. For example: window1 was created with a duration of four hours. It has how been open for two hours. If, at this point, you reopen window1 using the OPEN_WINDOW call and do not specify a duration, then window1 stays open for four hours because it was created with that duration. If you specified a duration of 30 minutes, the window will close in 30 minutes. 调度器 automatically closes any window that is open at that time, even if it has a higher priority. For the duration of this manually opened window, 调度器 does not open any other scheduled windows even if they have a higher priority. |
使用说明
Opening a window manually has no impact on regular scheduled runs of the window. The next open time of the window is not updated and is determined by the regular scheduled opening.
When a window that was manually opened closes, the rules about overlapping windows are applied to determine which other window should be opened at that time if any at all.
If there are jobs running when the window opens, the 资源s allocated to them might change if there is a switch in 资源计划.
If a window fails to switch 资源计划s because the designated 资源计划 no longer exists or because 资源计划 switching by windows is 已禁用 (for example, by using the `ALTER` `SYSTEM` statement with the `force` option), the failure to switch 资源计划s is recorded in the 窗口日志.
Opening a window requires the `MANAGE` `SCHEDULER` privilege.
#### PURGE_LOG Procedure
The `PURGE_LOG` procedure purges rows from the job and 窗口日志 that were not purged automatically by the scheduler.
By default, 调度器 automatically purges all rows in the 作业日志 and 窗口日志 that are older than 30 days. The `PURGE_LOG` procedure can be used to purge additional rows from the job and 窗口日志.
Rows in the 作业日志 table pertaining to the steps of a chain are purged only when the entry for the main chain job is purged (either manually or automatically).
语法

DBMS_SCHEDULER.PURGE_LOG (
   log_history             IN PLS_INTEGER  DEFAULT 0,
   which_log               IN VARCHAR2     DEFAULT 'JOB_AND_WINDOW_LOG',
   job_name                IN VARCHAR2     DEFAULT NULL);

参数
Table 159-71 PURGE_LOG Procedure Parameters
| Parameter | Description |
|---|---|
| log_history | This specifies how much history (in days) to keep. The valid range is 0 - 1000000. If set to 0, no history is kept. |
| which_log | This specifies the log type. Valid values are: job_log, window_log, and job_and_window_log. |
| job_name | This specifies which job-specific entries must be purged from the jog log. This can be a comma-delimited list of job names and 作业类es. Whenever job_name has a value other than NULL, the which_log 参数 implicitly includes the 作业日志. |
使用说明
此过程 requires the `MANAGE` `SCHEDULER` privilege.
示例
The following completely purges all rows from both the 作业日志 and the 窗口日志:

DBMS_SCHEDULER.PURGE_LOG();

The following purges all rows from the 窗口日志 that are older than 5 days:

DBMS_SCHEDULER.PURGE_LOG(5, 'window_log');

The following purges all rows from the 窗口日志 that are older than 1 day and all rows from the 作业日志 that are related to jobs in `jobclass1` and older than 1 day:

DBMS_SCHEDULER.PURGE_LOG(1, 'job_and_window_log', 'sys.jobclass1');

#### PUT_FILE Procedure
此过程 saves a file to the operating system file system of a specified remote host or of the local computer.
It differs from the equivalent `UTL_FILE` procedure in that it uses a 凭据 and can save files to a remote host that has only a Scheduler agent (and not an Oracle Database) installed.
语法

DBMS_SCHEDULER.PUT_FILE (
   destination_file         IN VARCHAR2,
   destination_host         IN VARCHAR2,
   credential_name          IN VARCHAR2,
   file_contents            IN {BLOB|CLOB},
   destination_permissions  IN VARCHAR2 DEFAULT NULL);

DBMS_SCHEDULER.PUT_FILE (
   destination_file         IN VARCHAR2,
   destination_host         IN VARCHAR2,
   credential_name          IN VARCHAR2,
   source_file_name         IN VARCHAR2,
   source_directory_object  IN VARCHAR2,
   destination_permissions  IN VARCHAR2 DEFAULT NULL);

参数
Table 159-72 PUT_FILE Procedure Parameters
| Parameter | Description |
|---|---|
| destination_file | Fully qualified path name of the file to save to the operating system file system. The file name is case-sensitive. If the file name starts with a question mark ('?'), the question mark is replaced by the path to the Oracle home if saving to the local host, or to 调度器 agent home if saving to a remote host. |
| destination_host | If NULL or set to 'localhost', the file is saved to the file system of the local computer. To save to a remote host, this parameter must be a valid external 目标 name. (An external 目标 is created when you register a remote Scheduler agent with the database. You can view external 目标 names in the views *_SCHEDULER_EXTERNAL_DESTS.) |
| credential_name | The name of the 凭据 to use for accessing the 目标 file system. |
| file_contents | The variable from which the file contents is read. |
| source_file_name | The file from which the file contents is written |
| source_directory_object | The directory object that specifies the path to the source file, when source_file_name is used. The caller must have the necessary privileges on the directory object. |
| destination_permissions | 保留供将来使用 |
使用说明
The caller must have the `CREATE EXTERNAL JOB` system privilege and have `EXECUTE` privileges on the 凭据.
#### REMOVE_EVENT_QUEUE_SUBSCRIBER Procedure
此过程 unsubscribes a user from 调度器 事件队列 `SYS.SCHEDULER$_EVENT_QUEUE`.
语法

DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER (
   subscriber_name         IN VARCHAR2 DEFAULT NULL);

参数
Table 159-73 REMOVE_EVENT_QUEUE_SUBSCRIBER Procedure Parameters
| Parameter | Description |
|---|---|
| subscriber_name | Name of the Oracle Advanced Queuing (AQ) agent to remove the subscription from. If NULL, the user name of the calling user is used. |
使用说明
After the agent is unsubscribed, it is deleted. If the agent does not exist or is not currently subscribed to 调度器 事件队列, an error is raised.
#### REMOVE_FROM_INCOMPATIBILITY Procedure
此过程 removes jobs or programs from an existing incompatibility definition.
语法

DBMS_SCHEDULER.REMOVE_FROM_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2);

参数
Table 159-74 REMOVE_FROM_INCOMPATIBILITY Procedure Parameters
| Parameter | Description |
|---|---|
| incompatibility_name | The name of the incompatibility definition. |
| object_name | One or more (comma-separated) programs or jobs |
使用说明
此过程 does not raise an error if any specified objects do not already exist in the incompatibility definition.
参见：
Using Incompatibility Definitions in Oracle Database Administrator’s Guide
#### REMOVE_GROUP_MEMBER Procedure
此过程 removes one or more members from an existing group.
语法

DBMS_SCHEDULER.REMOVE_GROUP_MEMBER (
   group_name              IN VARCHAR2,
   member                  IN VARCHAR2);

参数
Table 159-75 REMOVE_GROUP_MEMBER Procedure Parameters
| Parameter | Description |
|---|---|
| group_name | The name of the group. |
| member_name | The name of the member to remove from group. Comma-separated list of members to remove. An error is returned if any of the members is not part of the group. A group of the same type can be named as a member. 调度器 immediately expands the included group name into its list of members. If the member is a 目标, any job instances that run on this 目标 are removed from the *_SCHEDULER_JOB_DESTS views. |
使用说明
The following users may remove members from a group:
- The group owner
- A user that has been granted the ALTER object privilege on the group
- A user with the CREATE ANY JOB system privilege
You must have the `MANAGE` `SCHEDULER` privilege to remove a member from a group of type `WINDOW`.
参见：
"CREATE_GROUP Procedure"
#### REMOVE_JOB_EMAIL_NOTIFICATION Procedure
此过程 removes e-mail 通知s for a job. You can remove all e-mail 通知s or remove 通知s only for specified recipients or specified events.
语法

DBMS_SCHEDULER.REMOVE_JOB_EMAIL_NOTIFICATION (
    job_name             IN VARCHAR2,
    recipients           IN VARCHAR2 DEFAULT NULL,
    events               IN VARCHAR2 DEFAULT NULL);

参数
Table 159-76 ADD_JOB_EMAIL_NOTIFICATION Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | Name of the job to remove e-mail 通知s for. Cannot be NULL. |
| recipients | E-mail address to remove e-mail 通知 for. Comma-separated list of e-mail addresses. |
| events | Job state event to remove e-mail 通知 for. Comma-separate list of job state events. |
使用说明
When you specify multiple recipients and multiple events, the 通知 for each specified event is removed for each specified recipient. The procedure ignores any recipients or events that are specified but that were not previously added.
If `recipients` is `NULL`, e-mail 通知s for the specified events are removed for all existing recipients. If `events` is `NULL`, 通知s for all events are removed for the specified recipients. If both `recipients` and `events` are `NULL`, all e-mail 通知s are removed for the job.
For example, if `recipients` is '`jsmith@example.com,rjones@example.com`' and `events` is '`JOB_FAILED,JOB_BROKEN`', then 通知s for both the `JOB_FAILED` and `JOB_BROKEN` events are removed for both jsmith and rjones. If `recipients` is `NULL`, then 通知s for both the `JOB_FAILED` and `JOB_BROKEN` events are removed for jsmith, rjones, and any other previously defined recipients for these events.
To call this procedure, you must be the job owner or a user with the `CREATE` `ANY` `JOB` system privilege or `ALTER` object privilege on the job.
参见：
"ADD_JOB_EMAIL_NOTIFICATION Procedure"
#### RESET_JOB_ARGUMENT_VALUE Procedure
此过程 resets (clears) the value previously set to an 参数 for a job.
`RESET_JOB_ARGUMENT_VALUE` is overloaded.
语法
Clears a previously set job 参数 value by 参数 position:

DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER);

Clears a previously set job 参数 value by 参数 name:

DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_name           IN VARCHAR2);

参数
Table 159-77 RESET_JOB_ARGUMENT_VALUE Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of the job being altered |
| argument_position | The position of the program 参数 being reset |
| argument_name | The name of the program 参数 being reset |
使用说明
If the corresponding program 参数 has no default value, the job is 已禁用. Resetting a program 参数 of a job belonging to another user requires `ALTER` privileges on that job. Arguments can be specified by position or by name.
`RESET_JOB_ARGUMENT_VALUE` requires that you be the owner of the job or have `ALTER` privileges on that job. You can also reset a job 参数 value if you have the `CREATE` `ANY` `JOB` privilege.
`RESET_JOB_ARGUMENT_VALUE` only supports 参数s of SQL type. Therefore, 参数 values that are not of SQL type, such as booleans, are not supported as program or 作业参数.
#### RUN_CHAIN Procedure
此过程 immediately runs a chain or part of a chain by creating a run-once job with the job name given.
If no `job_name` is given, one is generated of the form `RUN_CHAIN$_chainnameN`, where `chainname` is the first 8 characters of the chain name and N is an integer.
If a list of start steps is given, only those steps are started when the chain begins running. Steps not in the list that would normally have started are skipped and paused (so that they or the steps after them do not run).
If `start_steps` is `NULL`, then the chain starts normally—that is, it performs an initial evaluation to see which steps to start running).
If a list of initial step states is given, the newly created chain job sets every listed step to the state specified for that step before evaluating the chain rules to see which steps to start. (Steps in the list are not started.)
语法
Runs a chain, with a list of start steps.

DBMS_SCHEDULER.RUN_CHAIN (
   chain_name                IN VARCHAR2,
   start_steps               IN VARCHAR2,
   job_name                  IN VARCHAR2 DEFAULT NULL);

Runs a chain, with a list of initial step states.

DBMS_SCHEDULER.RUN_CHAIN (
   chain_name               IN VARCHAR2,
   step_state_list          IN SYS.SCHEDULER$_STEP_TYPE_LIST,
   job_name                 IN VARCHAR2 DEFAULT NULL);

参数
Table 159-78 RUN_CHAIN Procedure Parameters
| Parameter | Description |
|---|---|
| chain_name | The name of the chain to run |
| job_name | The name of the job to create to run the chain |
| start_steps | Comma-separated list of the steps to start when the chain starts running |
| step_state_list | List of 链步骤s with an initial state (SUCCEEDED or FAILED) to set for each. Set the 属性s of sys.scheduler$_step_type as follows: step_name The name of the stepstep_type 'SUCCEEDED' or 'FAILED error_number' where error_number is a positive or negative integer. |
使用说明
Running a chain requires `CREATE` `JOB` if the job is being created in the user's schema, or `CREATE` `ANY` `JOB` otherwise. In addition, the owner of the job being created needs execute privileges on the chain (as the owner of the chain, or as a user with the `EXECUTE` privilege on the chain or the `EXECUTE` `ANY` `PROGRAM` system privilege).
示例
The following example illustrates how to start a chain in the middle by providing the initial state of some 链步骤s.

declare
  initial_step_states sys.scheduler$_step_type_list;
begin
  initial_step_states := sys.scheduler$_step_type_list(
    sys.scheduler$_step_type('step1', 'SUCCEEDED'),
    sys.scheduler$_step_type('step2', 'FAILED 27486'),
    sys.scheduler$_step_type('step3', 'SUCCEEDED'),
    sys.scheduler$_step_type('step5', 'SUCCEEDED'));
  dbms_scheduler.run_chain('my_chain', initial_step_states);
end;
/

#### RUN_JOB Procedure
此过程 runs a job immediately.
If a job is 已启用, 调度器 runs it automatically. It is not necessary to call `RUN_JOB` to run a job according to its schedule. Use `RUN_JOB` to run a job outside of its normal schedule.
语法

DBMS_SCHEDULER.RUN_JOB (
   job_name                IN VARCHAR2,
   use_current_session     IN BOOLEAN DEFAULT TRUE);

参数
Table 159-79 RUN_JOB Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | A job name or a comma-separate list of entries, where each is the name of an existing job, optionally preceded by a schema name and dot separator. If you specify a multiple-目标 job, the 作业运行s on all 目标s. In this case, the use_current_session 参数 must be FALSE. |
| use_current_session | This specifies whether or not the 作业运行 should occur in the same session that the procedure was invoked from.The job always runs as the job owner, in the job owner's schema, unless it has 凭据 specified, then the 作业运行s using the user named in the 凭据. When use_current_session is set to TRUE: You can test a job and see any possible errors on the command line. state, run_count, last_start_date, last_run_duration, and failure_count of *_scheduler_jobs are not updated. RUN_JOB can be run in parallel with a regularly scheduled 作业运行. When use_current_session is set to FALSE: You need to check the 作业日志 to find error information. All relevant fields in *_scheduler_jobs are updated. RUN_JOB fails if a regularly scheduled job is running. For jobs that have a specified 目标 or 目标 group, or point to chains or programs with the detached 属性 set to TRUE, use_current_session must be FALSE. |
使用说明
Jobs do not have to be 已启用. If a job is 已禁用, the following validity checks are performed before running it:
- The job points to a valid 作业类.
- The job owner has EXECUTE privileges on the 作业类.
- If a program or chain is referenced, the program/chain exists.
- If a program or chain is referenced, the job owner has privileges to execute the program/chain.
- All 参数 values have been set (or have defaults).
- The job owner has the CREATE EXTERNAL JOB privilege if this is an 外部作业.
A `TRUE` value for `use_current_session` is not permitted for the following types of jobs:
- Jobs that specify a 目标 or 目标 group in the destination_name 属性
- Jobs that point to chains (chain jobs)
- Jobs that make use of detached programs (detached jobs). above bug fix 1261887 6.12.11
When `use_current_session` is `TRUE`, the call to `RUN_JOB` blocks until the job completes. Any errors that occur during the execution of the job are returned as errors to the `RUN_JOB` procedure.
Using `RUN_JOB` with `use_current_session=TRUE` does not update the job state and the job will not appear in `*_SCHEDULER_RUNNING_JOBS` views.
above bug fix 19185117  9.15.14
When `use_current_session` is `FALSE`, `RUN_JOB` returns immediately and the job is picked up by the job coordinator and passed on to a job slave for execution. 调度器 views and logs must be queried for the outcome of the job.
Multiple user sessions can use `RUN_JOB` in their sessions simultaneously when `use_current_session` is set to `TRUE`.
`RUN_JOB` requires that you own the job or have `ALTER` privileges on that job. You can also run a job if you have the `CREATE` `ANY` `JOB` privilege.
示例
The following is an example of using `RUN_JOB`.

BEGIN
  DBMS_SCHEDULER.RUN_JOB(
    JOB_NAME            => 'EODJOB, DSS.ETLJOB',
    USE_CURRENT_SESSION => FALSE);
END;

#### SET_AGENT_REGISTRATION_PASS Procedure
此过程 sets the agent registration password for a database.
A Scheduler agent must register with the database before the database can submit jobs to the agent. The agent must provide this password when registering.
语法

DBMS_SCHEDULER.SET_AGENT_REGISTRATION_PASS (
   registration_password   IN VARCHAR2,
   expiration_date         IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   max_uses                IN NUMBER DEFAULT NULL);

参数
Table 159-80 SET_AGENT_REGISTRATION_PASS Procedure Parameters
| Parameter | Description |
|---|---|
| registration_password | This is the password that remote agents must specify in order to successfully register with the database. If this is NULL, then no agents will be able to register with the database. |
| expiration_date | If this is set to a non-NULL value, then the registration_password is not valid after this date. After this date, no agents can register with the database. This cannot be set to a date in the past. |
| max_uses | This is the maximum number of successful registrations that can be performed with this password. After the number of successful registrations has been performed with this password, then no agents can register with the database. This cannot be set to 0 or a negative value. If this is set to NULL, then there will be no limit on the number of successful registrations. |
使用说明
To prevent abuse, this password can be set to expire after a given date or a maximum number of successful registrations. 此过程 will overwrite any password already set. This requires the `MANAGE SCHEDULER` system privilege.
By default, `max_uses` is set to `NULL`, which means that there is no limit to the number of successful registrations.
Oracle recommends that an agent registration password be reset after every agent registration or every known set of agent registrations. Furthermore, Oracle recommends that this password be set to `NULL` if no new agents are being registered.
#### SET_ATTRIBUTE Procedure
此过程 modifies an 属性 of a Scheduler object. It is overloaded to accept values of various types.
To set an 属性 to `NULL`, use the `SET_ATTRIBUTE_NULL` procedure. The 属性s that can be set depend on the object being altered. All object 属性s can be changed, except the object name.
语法

DBMS_SCHEDULER.SET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          IN {BOOLEAN|DATE|TIMESTAMP|
                        TIMESTAMP WITH TIME ZONE|TIMESTAMP WITH LOCAL TIME ZONE|
                        INTERVAL DAY TO SECOND});
DBMS_SCHEDULER.SET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          IN VARCHAR2,
   value2         IN VARCHAR2 DEFAULT NULL);

参数
Table 159-81 SET_ATTRIBUTE Procedure Parameters
| Parameter | Description |
|---|---|
| name | The name of the object. |
| attribute | See Table 159-83 through Table 159-93. |
| value | The new value being set for the 属性. This cannot be NULL. To set an 属性 value to NULL, use the SET_ATTRIBUTE_NULL procedure. |
| value2 | The value2 参数 is for an optional second value. Most 属性s have only one value associated with them, but some can have two. |
Table 159-82 is a directory of Scheduler object types and tables of 属性s for the object types.
These object types can be viewed with Scheduler Data Dictionary Views, listed in Oracle Database Administrator's Guide.
Table 159-82 Attribute Tables for Scheduler Object Types
| Scheduler Object Type | Table of Attributes |
|---|---|
| Job | Table 159-83 |
| Program | Table 159-85 |
| Schedule | Table 159-86 |
| File Watcher | Table 159-87 |
| Job Class | Table 159-88 |
| Window | Table 159-89 |
| Chain | Table 159-90 |
| Database Destination | Table 159-91 |
| External Destination | Table 159-92 |
| Group | Table 159-93 |
| Credential | Table 159-94 |
| Resource | Table 159-95 |
使用说明
If an object is altered and it was in the 已启用 state, 调度器 first disables it, then makes the change and reenables it. If any errors are encountered during the enable process, the object is not re已启用 and an error is generated.
If an object is altered and it was in the 已禁用 state, it remains 已禁用 after it is altered.
To run `SET_ATTRIBUTE` for a window, a group of type `WINDOW`, or 作业类, you must have the `MANAGE` `SCHEDULER` privilege. Otherwise, you must be the owner of the object being altered or have `ALTER` privileges on that object or have the `CREATE` `ANY` `JOB` privilege.
Job
If there is a running instance of the job when the `SET_ATTRIBUTE` call is made, it is not affected by the call. The change is only affects future runs of the job.
If any of the schedule 属性s of a job are altered while the job is running, the time of the next 作业运行 is scheduled using the new schedule 属性s. Schedule 属性s of a job include `schedule_name`, `start_date`, `end_date`, and `repeat_interval`.
If any of the program 属性s of a job are altered while the job is running, the new program 属性s take effect the next time the 作业运行s. Program 属性s of a job include `program_name`, `job_action`, `job_type`, and `number_of_arguments`.
If any job 参数 values are altered while the job is running, the new values take effect the next time the 作业运行s.
Granting the `ALTER` privilege on a job lets a user alter all 属性s of that job except its program 属性s (`program_name`, `job_type`, `job_action`, `program_action`, and `number_of_arguments`) and does not allow a user to use a PL/SQL expression to specify the schedule for a job.
Oracle recommends that you not alter a job that was automatically created for you by the database. Jobs that were created by the database have the column `SYSTEM` set to `TRUE` in job views.
Program
If any currently running jobs use the program that was altered, they continue to run with the program definition prior to the alter. The 作业运行s with the new program definition the next time the job executes.
Schedule
If a schedule is altered, the change does not affect running jobs and open windows that use this schedule. The change only goes into effect the next time the jobs runs or the window opens.
File Watcher
If a 文件监视器 is altered, any currently running event-based jobs started by the file arrival event are not affected. On the local system, the new 文件监视器 属性s take effect the next time that the 文件监视器 checks for the arrival of the file (every ten minutes by default). On remote systems, there may be an additional delay before the new 文件监视器 属性s take effect.
Job Class
With the exception of the default 作业类, all 作业类es can be altered. To alter a 作业类, you must have the `MANAGE` `SCHEDULER` privilege.
When a 作业类 is altered, running jobs that belong to the class are not affected. The change only takes effect for jobs that have not started running yet. Job Class names must be preceded by `SYS`.
Window
When a window is altered, it does not affect an active window. The changes only take effect the next time the window opens.
If there is no current 资源计划, when a window with a designated 资源计划 opens, the Resource Manager activates with that plan. Window names must be preceded by `SYS`.
Job Attribute Values
Table 159-83 lists 属性 values for jobs.
Note:
See the `CREATE_JOB` procedure and the `CREATE_JOBS` procedure for more complete descriptions of the 属性s in this table.
Table 159-83 Job Attribute Values
| Name | Description |
|---|---|
| allow_runs_in_restricted_mode | If TRUE, the job is permitted to run when the database is in restricted mode, provided that the job owner is permitted to log in during this mode. FALSE by default. |
| auto_drop | This 属性, if TRUE, causes a job to be automatically dropped after it completes or is automatically 已禁用. A job is considered completed if: Its end date (or the end date of the schedule) has passed. It has run max_runs number of times. max_runs must be set with SET_ATTRIBUTE. It is not a repeating job and has run once. A job is automatically 已禁用 when it has failed max_failures times. max_failures is also set with SET_ATTRIBUTE. If this 属性 is set to FALSE, the jobs are not dropped and their metadata is kept until the job is explicitly dropped with the DROP_JOB procedure. By default, jobs are created with auto_drop set to TRUE. |
| comments | An optional comment. |
| connect_credential_name | This 属性 may be set to point to a database 凭据. For a SQL*Plus or backup script job, the 凭据 connects to the database before running the script. For other job types, it is ignored. The job owner must have execute privileges on the 凭据, otherwise the job fails. Using a connect_credential_name is recommended since it allows the password to be stored securely in a 凭据 in the database rather than in plain view in the job, program action, or script. |
| credential_name | This 属性 specifies the name of the 凭据 object (凭据) to use for a remote database job, a remote 外部作业, a local 外部作业, or an event-based job that processes a file arrival event. For local 外部作业s only, if this 属性 is NULL (the default), then a preferred (default) 凭据 is selected. See Oracle Database Administrator's Guide for information about preferred 凭据s for local 外部作业s. |
| database_role | This 属性 applies when the database participates in an Oracle Data Guard environment. If this 属性 is set to 'PRIMARY', the 作业运行s only when the database is in the role of the primary database. If set to 'LOGICAL STANDBY', the 作业运行s only when the database is in the role of a logical standby. 默认为 'PRIMARY' when the database is the primary database, and 'LOGICAL STANDBY' when the database is a logical standby. Note: If you want a job to run for all database roles on a particular host, you must create two copies of the job on that host: one with a database_role of 'PRIMARY', and the other with a database_role of 'LOGICAL STANDBY'. |
| destination | *** Deprecated in Oracle Database 11g Release 2. Use destination_name instead. This 属性 specifies a host on which to run a remote 外部作业. It must be set to the host name or IP address of the 目标 host. It can optionally be followed by a port number, in the following format:hostname:portThis 属性 is set to NULL by default. |
| destination_name | The database 目标 or external 目标 for the job. Use for remote database jobs and remote 外部作业s only. For jobs running on the local database or for local 外部作业s (executables), must be NULL. See Table 159-28 for details about this 属性. |
| end_date | Specifies the date and time after which the job expires and is no longer run. After the end_date, if is TRUE, the job is dropped. If auto_drop is FALSE, the job is 已禁用 and the STATE of the job is set to COMPLETED. If no value for end_date is specified, the job repeats forever unless max_runs or max_failures is set, in which case the job stops when either value is reached. The value for end_date must be after the value for start_date. If end_date is less than start_date, then an error will be generated. If end_date is the same as start_date, then the job will not execute and no error will be generated. |
| event_spec | This 属性 takes two values: the value 参数 specifies the event condition and the value2 参数 specifies the queue specification. For more details, see the descriptions for the event_condition and queue_spec 参数s in the "CREATE_JOB Procedure". |
| follow_default_timezone | If TRUE and if the job start_date is null, then when the default_timezone scheduler 属性 is changed, 调度器 recomputes the next run date and time for this job so that it is in accordance with the new time zone. For example, if the job was set to run at 02:00 in the previous time zone, it will run at 02:00 in the new time zone. If the job start_date is not null, then the time zone for the run date and time for the job is always specified by the time zone of the start_date. If FALSE, the next start date and time for the job is not recomputed when the default_timezone scheduler 属性 is changed. In this case, if the old time zone is three hours earlier than the new time zone, then a job scheduled to run at 02:00 in the old time zone runs at 05:00 in the new time zone. Summer and winter transitions do not change the default time zone name. |
| instance_id | Valid only in an Oracle Real Application Clusters environment. Indicates the instance on which the job is to be run. |
| instance_stickiness | This 属性 should only be used for a database running in an Oracle Real Application Clusters (Oracle RAC) environment. By default, it is set to TRUE. If you set instance_stickiness to TRUE, jobs start running on the instance with the lightest load and 调度器 thereafter attempts to run on the instance that it last ran on. If that instance is either down or so overloaded that it does not start new jobs for a significant period of time, another instance runs the job. If the interval between runs is large, instance_stickiness is ignored and the job is handled as if it were a non-sticky job. If instance_stickiness is set to FALSE, each instance of the 作业运行s on the first instance available. For environments other than Oracle RAC, this 属性 is not useful because there is only one instance. |
| job_action | The action that the job performs, depending on the job_type 属性. For example, if job_type is 'STORED_PROCEDURE', job_action contains the name of the stored procedure. |
| job_class | The class this job is associated with. |
| job_priority | This 属性 specifies the priority of this job relative to other jobs in the same class as this job. If multiple jobs within a class are scheduled to be executed at the same time, the job priority determines the order in which jobs from that class are picked up for execution by the job coordinator. It can be a value from 1 through 5, with 1 being the first to be picked up for job execution. If no job priority is specified when creating a job, the default priority of 3 is assigned to it. |
| job_type | The type of this job.Valid values are: 'PLSQL_BLOCK', 'STORED_PROCEDURE', 'EXECUTABLE', CHAIN', 'EXTERNAL_SCRIPT', 'SQL_SCRIPT', and 'BACKUP_SCRIPT'. If this is set, program_name must be NULL. |
| job_weight | *** Deprecated in Oracle Database 11gR2. Do not change the value of this 属性 from the default, which is 1. Weight of the job for parallel execution. |
| logging_level | This 属性 specifies how much information is logged. The possible options are: DBMS_SCHEDULER.LOGGING_OFF (The default) No logging is performed for this job. However, the logging level of the 作业类 takes precedence and 作业日志ging may occur. DBMS_SCHEDULER.LOGGING_FAILED_RUNS 调度器 logs only jobs that failed, with the reason for failure. If the 作业类 has a higher logging level, then the higher logging level takes precedence. DBMS_SCHEDULER.LOGGING_RUNS 调度器 writes detailed information to the 作业日志 for all runs of each job in this class. If the 作业类 has a higher logging level, then the higher logging level takes precedence. DBMS_SCHEDULER.LOGGING_FULL In addition to recording every run of a job, 调度器 records all operations performed on the job, including create, enable, disable, alter (with SET_ATTRIBUTE), stop, and so on. |
| max_failures | This 属性 specifies the number of times a job can fail on consecutive scheduled runs before it is automatically 已禁用. Once a job is 已禁用, it is no longer executed and its STATE is set to BROKEN in the *_SCHEDULER_JOB views. max_failures can be an integer between 1 to 1,000,000. By default, it is set to NULL, which indicates that new instances of the job are started regardless of how many previous instances have failed. |
| max_run_duration | This 属性 specifies the maximum amount of time that the job should be allowed to run. Its datatype is INTERVAL DAY TO SECOND. If this 属性 is set to a non-zero and non-NULL value, and job duration exceeds this value, 调度器 raises an event of type JOB_OVER_MAX_DUR. It is then up to your event handler to decide whether or not to allow the job to continue. |
| max_runs | This 属性 specifies the maximum number of consecutive scheduled runs of the job. Once max_runs is reached, the job is 已禁用 and its state is changed to COMPLETED. max_runs can be an integer between 1 and 1,000,000. By default, it is set to NULL, which means that it repeats forever or until end_date or max_failures is reached. |
| number_of_arguments | The number of 参数s if the program is inlined. If this is set, program_name should be NULL. |
| parallel_instances | This is a boolean 属性 that can be set only for event-based jobs. If FALSE (the default), then if an event is raised and the event-based job that processes that event is already running, the new event is ignored. If TRUE, then an instance of the job is started for every instance of the event, and each job instance is a 轻量级作业 so multiple instances of the same event-based job can run in parallel. Each 轻量级作业 takes its 属性s (such as action, maximum run duration, and so on) from the definition of the event-based job (its parent job). After the 轻量级作业 completes, it is dropped. There is no explicit limit to the number of 轻量级作业s that can run simultaneously to process multiple instances of the event. However, limitations may be imposed by available system 资源s. The 轻量级作业s are not visible in any of the *_SCHEDULER_JOBS views. However, they are visible in the *_SCHEDULER_RUNNING_JOBS views. The name of each 轻量级作业 is the same as that of the parent job, and a subname is automatically generated to distinguish each 轻量级作业 from its parent and from its siblings. |
| program_name | The name of a program object to use with this job. If this is set, job_action, job_type and number_of_arguments should be NULL. |
| raise_events | This attribute tells the Scheduler at what stages of the job execution to raise events. It is a bit vector in which zero or more of the following bits can be set. Each bit has a package constant corresponding to it. job_started CONSTANT PLS_INTEGER := 1 job_succeeded CONSTANT PLS_INTEGER := 2 job_failed CONSTANT PLS_INTEGER :=4 job_broken CONSTANT PLS_INTEGER :=8 job_completed CONSTANT PLS_INTEGER :=16 job_stopped CONSTANT PLS_INTEGER :=32 job_sch_lim_reached CONSTANT PLS_INTEGER :=64 job_disabled CONSTANT PLS_INTEGER :=128 job_chain_stalled CONSTANT PLS_INTEGER :=256 job_all_events CONSTANT PLS_INTEGER := 511 job_run_completed CONSTANT PLS_INTEGER := job_succeeded + job_failed + job_stopped Table 159-84 describes these event types in detail. |
| repeat_interval | Either a PL/SQL function returning the next date and time on which to run, or calendaring syntax expression. If this is set, schedule_name should be NULL. See "Calendaring Syntax" for more information. |
| restartable | This 属性 specifies whether or not a job can be restarted in case of failure. By default, jobs are not restartable and this 属性 is set to FALSE. Setting this to TRUE means that if a job fails while running, it is restarted from the beginning point of the job. In the case of a chain job, if this 属性 is TRUE, the chain is restarted from the beginning after an 应用失败. If this 属性 is FALSE, or if there has been a database failure, the chain is restarted at the last running step. The restart_on_recovery 属性 of that step then determines if the step is restarted or marked as stopped. (If marked as stopped, the chain evaluates rules and continues.) Note that setting this 属性 to TRUE might lead to data inconsistencies in some situations, for example, if data is committed within a job. Retries on errors are not counted as regular runs. The run count or failure count is not incremented until the job succeeds or has failed all its six retries. The restartable 属性 is used by 调度器 to determine whether to retry the job not only on regular application errors, but after a database malfunction as well. 调度器 retries the job a maximum of six times. The first time, it waits for one second and multiplies this wait time with a factor of 10 each time thereafter. Both the run count and failure count are incremented by 1 if the job has failed all its six retries. If the job immediately succeeds, or it succeeds on one of its retries, run count is incremented by 1. 调度器 stops retrying a job when: One of the retries succeeds. All of its six retries have failed. The next retry would occur after the next regularly scheduled run of the job. 调度器 no longer retries the job if the next scheduled retry is past the next regularly scheduled run for repeating jobs. |
| schedule_limit | In heavily loaded systems, jobs are not always started at their scheduled time. This 属性 enables you to have 调度器 not start a job at all if the delay in starting the job is larger than the interval specified. It can be a value of 1 minute to 99 days. For example, if a job was supposed to start at noon and the schedule limit is set to 60 minutes, the job will not be run if it has not started to run by 1:00 p.m. If schedule_limit is not specified, the job is executed at some later date as soon as there are 资源s available to run it. By default, this 属性 is set to null, which indicates that the job can be run at any time after its scheduled time. A scheduled 作业运行 that is skipped because of this 属性 does not count against the number of runs and failures of the job. An entry in the 作业日志 reflects the skipped run. |
| schedule_name | The name of a schedule, window, or group of type WINDOW to use as the schedule for this job. If this is set, end_date, start_date and repeat_interval should all be NULL. |
| start_date | The original date and time on which this job started or is scheduled to start. If this is set, schedule_name should be NULL. |
| stop_on_window_close | This 属性 only applies if the schedule of a job is a window or a 窗口组. Setting this 属性 to TRUE implies that the job should stop once the associated window is closed. The job is stopped using the stop_job procedure with force set to FALSE. By default, stop_on_window_close is set to FALSE. Therefore, if you do not set this 属性, the job continues after the window closes. Note that, although the job is allowed to continue, its 资源 allocation will probably change because closing a window generally also implies a change in 资源计划s. |
| store_output | This is a boolean 属性. If set to TRUE, then for 作业运行s that are logged, all job output and error messages are stored in the *_JOB_RUN_DETAILS views. If set to FALSE, then the output and messages are not stored. For new jobs, this is set, by default, to TRUE. |
The following event types are valid values for the `raise_events` 属性 in Table 159-83.
Table 159-84 Event Types Raised by 调度器
| Event Type | Description |
|---|---|
| job_all_events | Not an event, but a constant that provides an easy way for you to enable all events |
| job_broken | The job has been 已禁用 and has changed to the BROKEN state because it exceeded the number of failures defined by the max_failures job 属性 |
| job_chain_stalled | A 作业运行ning a chain is in the CHAIN_STALLED state. A running chain becomes stalled if there are no steps running or scheduled to run and the chain evaluation_interval is set to NULL. No progress is made in the chain unless there is manual intervention. |
| job_completed | The job completed because it reached its max_runs or end_date |
| job_disabled | The job was 已禁用 by 调度器 or by a call to SET_ATTRIBUTE |
| job_failed | The job failed, either due to an error or an unusual termination. |
| job_over_max_dur | The job exceeded the maximum run duration specified by its max_run_duration 属性. (Note: you do not need to enable this event with the raise_events job 属性; it is always 已启用.) |
| job_run_completed | A 作业运行 either failed, succeeded, or was stopped |
| job_sch_lim_reached | The schedule limit of the job was reached. The job was not started because the delay in starting the job exceeded the value of the schedule_limit job 属性. |
| job_started | The job started |
| job_stopped | The job was stopped by a call to STOP_JOB |
| job_succeeded | The job completed successfully |
Program Attribute Values
Table 159-85 lists program 属性 values.
Note:
See the "CREATE_PROGRAM Procedure" for more complete descriptions of the 属性s in this table.
Table 159-85 Program Attribute Values
| Name | Description |
|---|---|
| comments | An optional comment. This can describe what the program does or give usage details. |
| detached | If TRUE, the program is a detached program. See Oracle Database Administrator's Guide for information about detached jobs and detached programs. |
| number_of_arguments | The number of 参数s required by the stored procedure or other executable that the program invokes |
| program_action | The action that the program performs, indicated by the program_type 属性. For example, if program_type is 'STORED_PROCEDURE', program_action contains the name of the stored procedure. |
| program_type | The type of program. This must be one of these supported program types: 'PLSQL_BLOCK', 'STORED_PROCEDURE', and 'EXECUTABLE'. |
Schedule Attribute Values
Table 159-86 lists schedule 属性 values.
Note:
See `"CREATE_SCHEDULE Procedure"` for more complete descriptions of the 属性s in this table.
Table 159-86 Schedule Attribute Values
| Name | Description |
|---|---|
| comments | An optional comment. |
| end_date | The cutoff date and time after which the schedule does not specify any dates. |
| event_spec | This 属性 takes two values: the value 参数 should contain the event condition and the value2 参数 should contain the queue specification. For more details, see the descriptions for the event_condition and queue_spec 参数s to the "CREATE_JOB Procedure". |
| repeat_interval | An 属性 specifying how often the schedule should repeat, using the calendaring syntax. See "Calendaring Syntax" for more information. |
| start_date | The start or reference date and time used by the calendaring syntax. |
File Watcher Attribute Values
Table 159-87 lists 文件监视器 属性 values.
Table 159-87 File Watcher Attribute Values
| Parameter | Description |
|---|---|
| destination | Remote host name or IP address where the file is expected to arrive. If NULL, 目标 is the local host. |
| directory_path | Directory in which the file is expected to arrive. The single wildcard '?' at the beginning of the path denotes the Oracle home path. For example, '?/rdbms/log' denotes the rdbms/log subdirectory of the Oracle home directory. |
| file_name | Name of the file being looked for. Two wildcards are permitted anywhere in the file name: '?' denotes any single character, and '*' denotes zero or more characters. This 属性 cannot be NULL. |
| credential_name | Name of a valid 凭据 object. The 文件监视器 uses the 凭据 to authenticate itself with the host operating system to access the watched-for file. The 文件监视器 owner must have the EXECUTE privilege on the 凭据. Cannot be NULL. |
| min_file_size | Minimum file size in bytes before the 文件监视器 considers the file found. 默认为 0. |
| steady_state_duration | Minimum time interval that the file must remain unchanged before the 文件监视器 considers the file found. If NULL, an internal value is used. The lower limit for this 属性 is 10 seconds. |
| comments | Optional comment. |
Job Class Attribute Values
Table 159-88 lists 作业类 属性 values.
Note:
See the "CREATE_JOB_CLASS Procedure" for more complete descriptions of the 属性s in this table.
Table 159-88 Job Class Attribute Values
| Name | Description |
|---|---|
| comments | An optional comment about the class. |
| log_history | This 属性 controls the number of days that 作业日志 entries for jobs in this class are retained. It helps prevent the 作业日志 from growing indiscriminately. The range of valid values is 0 through 1000000. If set to 0, no history is kept. If NULL, retention days are set by the log_history Scheduler 属性 (set with SET_SCHEDULER_ATTRIBUTE). |
| logging_level | This 属性 specifies how much information is logged. The valid values are: DBMS_SCHEDULER.LOGGING_OFF No logging is performed for any jobs in this class. DBMS_SCHEDULER.LOGGING_FAILED_RUNS 调度器 logs only jobs in the class that failed, with the reason for failure. DBMS_SCHEDULER.LOGGING_RUNS 调度器 writes detailed information to the 作业日志 for all runs of each job in this class. This is the default. DBMS_SCHEDULER.LOGGING_FULL 调度器 records all operations performed on all jobs in this class, in addition to recording every run of a job. Every time a job is created, 已启用, 已禁用, altered (with SET_ATTRIBUTE), stopped, and so on, an entry is recorded in the log. |
| resource_consumer_group | The 资源使用者组 that a class is associated with. All jobs in the class run under this 资源使用者组. See Oracle Database Administrator's Guide for a description of 资源使用者组s and the Database Resource Manager. |
| service | The database service that the jobs in the 作业类 have affinity to. If both the resource_consumer_group and service 属性s are set for a 作业类, and if the service is mapped to a 资源使用者组, the resource_consumer_group 属性 takes precedence. |
Window Attribute Values
Table 159-89 lists window 属性 values.
Note:
See the "CREATE_WINDOW Procedure" for more complete descriptions of the 属性s in this table.
Table 159-89 Window Attribute Values
| Name | Description |
|---|---|
| comments | An optional comment about the window. |
| duration | The duration of the window. |
| end_date | The date after which the window no longer opens. If this is set, schedule_name must be NULL. |
| repeat_interval | An 属性 specifying how often the schedule should repeat, using the calendaring syntax. PL/SQL date functions are not allowed. If this is set, schedule_name must be NULL. See "Calendaring Syntax" for more information. |
| resource_plan | The 资源计划 to be associated with a window. When the window opens, the system switches to this 资源计划. When the window closes, the original 资源计划 is restored. If a 资源计划 has been made active with the force option, no 资源计划 switch occurs. Only one 资源计划 can be associated with a window. It may be NULL or the empty string (""). When it is NULL, the 资源计划 that is in effect when the window opens stays in effect for the duration of the window. When it is the empty string, the 资源 manager is 已禁用 for the duration of the window. |
| schedule_name | The name of a schedule to use with this window. If this is set, start_date, end_date, and repeat_interval must all be NULL. |
| start_date | The next date and time on which this window is scheduled to open. If this is set, schedule_name must be NULL. |
| window_priority | The priority of the window. Must be either 'LOW' (default) or 'HIGH'. |
Chain Attribute Values
Table 159-90 lists chain 属性 values.
Note:
See the "CREATE_CHAIN Procedure" for more complete descriptions of the 属性s in this table.
Table 159-90 Chain Attribute Values
| Name | Description |
|---|---|
| comments | An optional comment describing the purpose of the chain. |
| evaluation_interval | If not NULL, provides an additional evaluation of the chain at this interval, as well as at normal evaluation times (when the job starts, when a step completes, or when an event that is associated with an event step arrives) This 属性 should only to be used when chain rules use SQL syntax and the rule conditions contain elements that are not under the control of 调度器, because the extra interval is CPU intensive. For most chains, the normal evaluation times are sufficient. |
| rule_set_name | In the normal case, no 规则集 should be passed in. 调度器 automatically creates a 规则集 and associated empty evaluation context. You then use DEFINE_CHAIN_RULE to add rules and DROP_CHAIN_RULE to remove them. Advanced users can create a 规则集 that describes their chain dependencies and pass it in here. This allows greater flexibility in defining rules. For example, conditions can refer to external variables, and tables can be exposed through the evaluation context. If you pass in a 规则集, you must ensure that it is in the format of a chain 规则集. (For example, all steps must be listed as variables in the evaluation context). If no 规则集 is passed in, the 规则集 created is of the form SCHED_RULESET${N} and the evaluation context created is of the form SCHED_EVCTX${N} |
Database Destination Attribute Values
Table 159-91 lists database 目标 属性 values.
Note:
See the "CREATE_DATABASE_DESTINATION Procedure" for more complete descriptions of the 属性s in this table.
Table 159-91 Database Destination Attribute Values
| Name | Description |
|---|---|
| agent | The name of the external 目标 (also known as agent 目标) that is used to connect to the remote database. You can obtain valid external 目标 names from the view ALL_SCHEDULER_EXTERNAL_DESTS. |
| connect_info | The TNS connect descriptor that identifies the remote database to connect to, or the net service name (alias) in tnsnames.ora that resolves to the connect descriptor. Note: This corresponds to the tns_name 参数 of CREATE_DATABASE_DESTINATION. |
| enabled | If TRUE, the database 目标 is 已启用. |
| comments | An optional comment about the database 目标. |
External Destination Attribute Values
Table 159-92 lists external 目标 属性 values.
Note:
External 目标s are created only implicitly by registering a remote Scheduler agent with the local database.
Table 159-92 External Destination Attribute Values
| Name | Description |
|---|---|
| hostname | (GET_ATTRIBUTE only) The fully qualified host name (including domain) or IP address of the computer on which 调度器 agent resides. |
| port | (GET_ATTRIBUTE only) The TCP port number on which the agent listens. |
| ip_address | (GET_ATTRIBUTE only) The IP address of the host on which the agent resides. |
| enabled | If TRUE, the external 目标 is 已启用. |
| comments | An optional comment about the external 目标. |
Group Attribute Values
Table 159-93 lists group 属性 values.
Note:
See the "CREATE_GROUP Procedure" for more complete descriptions of the 属性s in this table.
Table 159-93 Group Attribute Values
| Name | Description |
|---|---|
| group_type | (GET_ATTRIBUTE only) The group type (either WINDOW, DB_DEST, or EXTERNAL_DEST). |
| member_name | Comma-separated list of members. Replaces the existing list of members. To add one or more members to the existing list, use ADD_GROUP_MEMBER. Note: this 属性 corresponds to the member 参数 of CREATE_GROUP. |
| enabled | If TRUE, the group is 已启用. |
| comments | An optional comment about the group. |
| number_of_members | (GET_ATTRIBUTE only) The number of members in the group. |
Credential Attribute Values
Table 159-94 lists 凭据 属性 values.
Note:
Credential 属性 values for the `SET_ATTRIBUTE` and `GET_ATTRIBUTE` procedures are deprecated with Oracle Database Release 12c Release 1 (12.1). While these 属性 values remain available in this package, for reasons of backward compatibility, Oracle recommends using the alternative enhanced functionality provided in the  DBMS_CREDENTIAL  package, specifically the 属性 parameter in the UPDATE_CREDENTIAL Procedure.
Table 159-94 Credential Attribute Values
| Name | Description |
|---|---|
| username | The user name for logging into to the host operating system or remote Oracle database. Maximum length is 64. |
| password | The password for the user name. Maximum length is 128. |
| comments | A description of the 凭据. Maximum length is 240. |
| windows_domain | For a Windows remote executable target, this is the domain that the specified user belongs to. Maximum length is 64. |
| database_role | The value of the database_role 属性 is used as the system privilege for logging into a remote database to run a remote database job. Valid values are: SYSDBA and SYSOPER. |
Resource Attribute Values
Table 159-95 lists 资源 属性 values.
Table 159-95 Resource Attribute Values
| Name | Description |
|---|---|
| resource_name | The name of the 资源 |
| units | The number of units of this 资源 that the job or program uses. |
| status | The status of the 资源. ENFORCE_CONSTRAINTS. This is the default value, and when set, will force the scheduler to enforce 资源 limits. When the maximum number of units of this 资源 has been reached, no additional jobs using this 资源 will get started. IGNORE_CONSTRAINTS. When set, the scheduler will ignore any constraints on this 资源. BLOCKED_ALL_JOBS. No jobs having a constraint on this 资源 will be allowed to run. The 资源 is considered to be permanently blocking until switched to one of the other two states. |
| constraint_level | Level of the constraint: JOB_LEVEL or PROGRAM_LEVEL For incompatibilities, for JOB_LEVEL, the incompatibility members must be jobs; for PROGRAM_LEVEL the incompatibility members must be programs. |
| comments | Descriptive comment about the 资源. |
#### SET_ATTRIBUTE_NULL Procedure
此过程 sets an 属性 of an object to `NULL`.
The 属性s that can be set depend on the object being altered. If the object is 已启用, it is 已禁用 before being altered and re已启用 afterward. If the object cannot be re已启用, an error is generated and the object is left in a 已禁用 state.
语法

DBMS_SCHEDULER.SET_ATTRIBUTE_NULL (
   name              IN VARCHAR2,
   attribute         IN VARCHAR2);

参数
Table 159-96 SET_ATTRIBUTE_NULL Procedure Parameters
| Parameter | Description |
|---|---|
| name | The name of the object |
| attribute | The 属性 being changed |
使用说明
To run `SET_ATTRIBUTE_NULL` for a window, group of type `WINDOW`, or 作业类, you must have the `MANAGE` `SCHEDULER` privilege. Otherwise, you must be the owner of the object being altered or have `ALTER` privileges on that object or have the `CREATE` `ANY` `JOB` privilege.
#### SET_JOB_ANYDATA_VALUE Procedure
此过程 sets the value for an 参数 of the associated program for a job, encapsulated in an `AnyData` object.
It overrides any default value set for the program 参数. `NULL` is a valid assignment for a program 参数.
The 参数 can be specified by position or by name. You can specify by name only when:
- The job points to a saved program object
- The 参数 was assigned a name with the DEFINE_ANYDATA_ARGUMENT Procedure
Scheduler does no type checking of the 参数 at any time.
`SET_JOB_ANYDATA_VALUE` is overloaded.
语法
Sets a program 参数 by its position.

DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_value          IN SYS.ANYDATA);

Sets a program 参数 by its name.

DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE (
   job_name                IN VARCHAR2,
   argument_name           IN VARCHAR2,
   argument_value          IN SYS.ANYDATA);

参数
Table 159-97 SET_JOB_ANYDATA_VALUE Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of the job to be altered |
| argument_name | The name of the program 参数 being set |
| argument_position | The position of the program 参数 being set |
| argument_value | The new value to be assigned to the program 参数, encapsulated in an AnyData object |
使用说明
`SET_JOB_ANYDATA_VALUE` requires that you own the job or have `ALTER` privileges on that job. You can also set a job 参数 value if you have the `CREATE` `ANY` `JOB` privilege.
`SET_JOB_ANYDATA_VALUE` does not apply to 轻量级作业s because 轻量级作业s cannot take `AnyData` 参数s.
参见：
- "SET_JOB_ARGUMENT_VALUE Procedure"
- "DEFINE_ANYDATA_ARGUMENT Procedure"
#### SET_JOB_ARGUMENT_VALUE Procedure
此过程 sets the value of an 参数 for a job.
It overrides any default value set for the corresponding program or stored procedure 参数. The 参数 can be specified by position or by name. You can specify by name only when:
- The job points to a saved program object
- The 参数 was assigned a name with the DEFINE_PROGRAM_ARGUMENT Procedure or the DEFINE_METADATA_ARGUMENT Procedure
Scheduler does no type checking of the 参数 at any time.
`SET_JOB_ARGUMENT_VALUE` is overloaded.
语法
Sets an 参数 value by position:

DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_value          IN VARCHAR2);

Sets an 参数 value by name:

DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_name           IN VARCHAR2,
   argument_value          IN VARCHAR2);

参数
Table 159-98 SET_JOB_ARGUMENT_VALUE Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | The name of the job to be altered |
| argument_name | The name of the program 参数 being set |
| argument_position | The position of the program 参数 being set |
| argument_value | The new value to be set for the program 参数. To set a non-VARCHAR value, use the SET_JOB_ANYDATA_VALUE procedure. |
使用说明
`SET_JOB_ARGUMENT_VALUE` requires that you be the owner of the job or have `ALTER` privileges on that job. You can also set a job 参数 value if you have the `CREATE` `ANY` `JOB` privilege.
`SET_JOB_ARGUMENT_VALUE` only supports 参数s of SQL type. Therefore, 参数 values that are not of SQL type, such as booleans, are not supported as program or 作业参数.
`SET_JOB_ARGUMENT_VALUE` can be used to set 参数s of 轻量级作业s but only if the 参数 is of type `VARCHAR2`.
参见：
- "SET_JOB_ANYDATA_VALUE Procedure"
- "DEFINE_PROGRAM_ARGUMENT Procedure"
#### SET_JOB_ATTRIBUTES Procedure
此过程 changes an 属性 of a job.
语法

DBMS_SCHEDULER.SET_JOB_ATTRIBUTES (
   jobattr_array     IN JOBATTR_ARRAY,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-99 SET_JOB_ATTRIBUTES Procedure Parameters
| Parameter | Description |
|---|---|
| jobattr_array | The array of job 属性 changes. |
| commit_semantics | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and commits previous successful 属性 changes to disk. This is the default. TRANSACTIONAL returns on the first error and rolls back everything that happened before that error. ABSORB_ERRORS tries to absorb any errors and complete the rest of the job 属性 changes on the list. It commits all the successful changes. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |
使用说明
Calling `SET_ATTRIBUTE` on an 已启用 job disables the job, changes the 属性 value, and reenables the job. `SET_JOB_ATTRIBUTES` changes the 属性 values in the context of a single transaction.
#### SET_RESOURCE_CONSTRAINT Procedure
此过程 allows users to specify the 资源s used by jobs.
语法

DBMS_SCHEDULER.SET_RESOURCE_CONSTRAINT (
   object_name       IN VARCHAR2,
   resource_name     IN VARCHAR2,
   units             IN NUMBER DEFAULT 1);

参数
Table 159-100 SET_RESOURCE_CONSTRAINT Procedure Parameters
| Parameter | Description |
|---|---|
| object_name | The name of a program or a job, or a comma separated list of these objects. |
| resource_name | The name of the 资源. |
| units | The number of units of this 资源 that the job or program uses. |
Usages Notes
`object_name` can be the name or comma-separated list of names of either programs or jobs. This creates a constraint on the named 资源 for these programs or jobs.
`units` specifies the number of units of the 资源 that the program or job can use. If `units` is set to `0,`then the program or job does not use this 资源 anymore, and the resulting constraint is deleted. Setting `units` to `0` on a 资源 with no previous constraint results in an error.
When multiple constraints are defined on the same 资源, the object types must match. When one or more existing constraints for a 资源 are based on jobs and a new constraint is added for the same 资源 that is based on a program (or vice versa) an error will be raised.
#### SET_SCHEDULER_ATTRIBUTE Procedure
此过程 sets the value of a Scheduler 属性. This takes effect immediately but the resulting changes may not be seen immediately, depending on the 属性 affected.
Table 159-101 provides short 属性 descriptions for the `SET_SCHEDULER_ATTRIBUTE` procedure. For complete descriptions, see section "Setting Scheduler Preferences" in Oracle Database Administrator's Guide.
语法

DBMS_SCHEDULER.SET_SCHEDULER_ATTRIBUTE (
   attribute      IN VARCHAR2,
   value          IN VARCHAR2);

参数
Table 159-101 SET_SCHEDULER_ATTRIBUTE Procedure Parameters
| Parameter | Description |
|---|---|
| attribute | The name of 调度器 属性. Possible values are: 'default_timezone': Repeating jobs and windows that use the calendaring syntax retrieve the time zone from this 属性 when start_date is not specified. See "Calendaring Syntax" for more information. 'email_server': The SMTP server address that 调度器 uses to send e-mail 通知s for job state events. E-mail 通知s cannot be sent if this 属性 is NULL. 'email_sender': The default e-mail address of the sender of job state e-mail 通知s. 'email_server_credential': The schema and name of an existing 凭据 object that SYS has execute object privileges on. 默认为 NULL. The username and password stored in this 凭据 are used to authenticate with the e-mail server when sending e-mail 通知s. 'email_server_encryption': This 属性 indicates whether or not encryption is 已启用 for this email server connection, and if so, at what point encryption starts, and with which protocol. Values are: NONE: the default, indicating no encryption used SSL_TLS: indicating that either SSL or TLS are used, from the beginning of the connection STARTTLS:indicating that the connection starts unencrypted, but the command STARTTLS is sent to the e-mail server and starts encryption 'event_expiry_time': The time, in seconds, before a job state event generated by 调度器 expires from 调度器 事件队列. If NULL, job state events expire after 24 hours. 'log_history': The number of days that log entries for both the 作业日志 and the 窗口日志 are retained. 默认为 30 and the range of valid values is 0 through 1000000. 'max_job_slave_processes': This Scheduler 属性 is not used. |
| value | The new value of the 属性 |
使用说明
To run `SET_SCHEDULER_ATTRIBUTE`, you must have the `MANAGE` `SCHEDULER` privilege.
参见：
Oracle Database Administrator's Guide for more detailed descriptions of Scheduler 属性s
#### STOP_JOB Procedure
此过程 stops currently running jobs or all jobs in a 作业类.
After stopping the job, the state of a one-time job is set to `STOPPED`, whereas the state of a repeating job is set to `SCHEDULED` or `COMPLETED`, depending on whether the next run of the job is scheduled.
If a job pointing to a chain is stopped, all running steps of the running chain are stopped.
If a job has multiple 目标s, the database attempts to stop the job at all 目标s.
For 外部作业s, `STOP_JOB` stops only the external process that was directly started by the job action. It does not stop child processes of 外部作业s.
For in-memory full jobs in an Oracle Real Application Clusters environment, `STOP_JOB` uses the `instance_id` 属性 of the job definition to determine in which instance (or all of them if the 属性 is left null) to stop the in-memory full job. (In-memory full jobs are kept cached in memory, and as such are limited to the instance currently caching them. Because of this, the same `job_name` can in some conditions be used for different jobs on different instances.)
语法

DBMS_SCHEDULER.STOP_JOB (
   job_name         IN VARCHAR2
   force            IN BOOLEAN DEFAULT FALSE
   commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');

参数
Table 159-102 STOP_JOB Procedure Parameters
| Parameter | Description |
|---|---|
| job_name | Name of a job to stop. Can be a comma-separate list of jobs, where each entry can be one of the following: Job name: the name of an existing job, optionally preceded by a schema name and dot separator. Job 目标 ID: a number, obtained from the JOB_DEST_ID column of the *_SCHEDULER_JOB_DESTS views, that represents the unique combination of a job, a 凭据, and a 目标. Job class: the name of a 作业类. Must be preceded by the SYS schema name and a dot separator. If you specify a 作业类, all jobs that belong to that 作业类 are stopped. If you specify a job that was created with a 目标 group as its destination_name 属性, all job instances on all 目标s are stopped. |
| force | If force is set to FALSE, 调度器 tries to gracefully stop the job using an interrupt mechanism. This method gives control back to the slave process, which can update the status of the job in the job queue to stopped. If this fails, an error is returned. If force is set to TRUE, 调度器 immediately terminates the job slave. Oracle recommends that STOP_JOB with force set to TRUE be used only after a STOP_JOB with force set to FALSE has failed. Use of the force option requires the MANAGE SCHEDULER system privilege. |
| commit_semantics | The commit semantics. The following two types are supported: STOP_ON_FIRST_ERROR: The procedure returns on the first error and commits previous successful stop operations to disk. This is the default. ABSORB_ERRORS: The procedure tries to absorb any errors, stops the rest of the jobs, and commits all the successful stop operations. This type is available only if no 作业类es are specified in the job_name list. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |
使用说明
`STOP_JOB` without the `force` option requires that you be the owner of the job or have `ALTER` privileges on that job. You can also stop a job if you have the `CREATE` `ANY` `JOB` or `MANAGE` `SCHEDULER` privilege.
`STOP_JOB` with the `force` option requires that you have the `MANAGE` `SCHEDULER` privilege.
示例
The following is an example of using `STOP_JOB`.

BEGIN
  DBMS_SCHEDULER.STOP_JOB('DSS.ETLJOB, 984, 1223, SYS.ETL_JOBCLASS');
END;

---

#### CREATE_PROGRAM Procedure

此过程创建一个程序（program）。

语法：

```
DBMS_SCHEDULER.CREATE_PROGRAM (
   program_name             IN VARCHAR2,
   program_type             IN VARCHAR2,
   program_action           IN VARCHAR2,
   number_of_arguments      IN PLS_INTEGER DEFAULT 0,
   enabled                  IN BOOLEAN DEFAULT FALSE,
   comments                 IN VARCHAR2 DEFAULT NULL);
```

参数（表 159-31 CREATE_PROGRAM Procedure Parameters）：

| 参数 | 说明 |
|---|---|
| program_name | 赋予该程序的名称。名称在 SQL 命名空间内必须唯一（例如不能与某 schema 中的表同名）。未指定名称会报错。 |
| program_type | 指定所创建程序的类型，未指定会报错。支持的取值：'PLSQL_BLOCK'——程序为 PL/SQL 块，此时作业/程序参数不支持，参数个数必须为 0；'STORED_PROCEDURE'——程序为 PL/SQL 或 Java 存储过程，或外部 C 子程序，仅支持过程（不支持有返回值的函数），不支持带 INOUT/OUT 参数的 PL/SQL 过程；'EXECUTABLE'——作业在数据库外用外部可执行文件运行（任何可从操作系统命令行执行的程序），不支持 AnyData 参数；'EXTERNAL_SCRIPT'——作业为外部脚本，使用运行作业机器的命令 shell（Windows 为 cmd.exe，UNIX 系为 sh，除非脚本首行用 `#!` 指定其它解释器）；'SQL_SCRIPT'——程序为 SQL*Plus 脚本，使用该程序的作业须指向含有效操作系统用户名/口令的凭据，脚本由 SQL*Plus 可执行文件运行；作业可指向含数据库凭据的连接凭据，若有则运行脚本前用它连接数据库（用连接凭据时须用 set_attribute 设置 Connect_Credential_Name 属性；若无则须在脚本中包含显式 SQL*Plus connect 语句并提供有效数据库用户/口令）；'BACKUP_SCRIPT'——程序为 RMAN 备份脚本，脚本执行目标命令前先运行一条使用口令或 OS 认证的 connect 语句，调度器用当前 Oracle home 的 RMAN 可执行文件运行脚本，缺失则报错。 |
| program_action | 指定程序的动作，未指定会报错。可能动作：PL/SQL 块——动作为执行 PL/SQL 代码，块须以分号结尾（如 `my_proc();` 或 `BEGIN my_proc(); END;` 或 `DECLARE arg pls_integer:=10; BEGIN my_proc2(arg); END;`），调度器会把 job_action 包在自己的块中（`DECLARE ... BEGIN job_action END;`）以声明内部调度器变量；可在 PL/SQL 代码中使用除 event_message 外的任何调度器元数据属性（用属性名作 PL/SQL 标识符，调度器赋值），匿名块还可用变量名 job_name、job_owner、job_start、window_start、window_end 访问特殊调度器元数据（见 DEFINE_METADATA_ARGUMENT）；存储过程——动作为存储过程名，过程所在 schema 与作业不同时须指定 schema，需大小写敏感时用双引号括起 schema 名与过程名（如 `program_action=>'"Schema"."Procedure"'`）；可执行文件——动作为外部可执行文件名（含全路径，不含命令行参数），以 `?` 开头时替换为本地作业的 Oracle home 或远程作业的调度器代理 home，含 `@` 且为本地作业时替换为当前 Oracle 实例的 SID；外部脚本——动作为操作系统脚本路径或内联脚本，脚本须存在于每台运行该程序的机器上，可调用 SQL*Plus/RMAN 可执行文件（无需全路径，前提是各机器默认位置有），作业参数只能为字符串或可转为字符串者，按位置传入；SQL 脚本——动作为 SQL*Plus 脚本路径或内联脚本，参数同上，若为命名参数还会绑定到 SQL*Plus 会话的命名变量；备份脚本——动作为 RMAN 脚本路径或内联脚本，参数同上。 |
| number_of_arguments | 程序接受的参数个数，未指定默认 0，最多 255。program_type 为 PLSQL_BLOCK 时忽略此参数。 |
| enabled | 是否创建为已启用。设为 TRUE 时做有效性检查并通过则创建为 ENABLED；默认 FALSE（未启用），也可之后调用 ENABLE 过程启用。 |
| comments | 关于此程序的注释，默认 NULL。 |

使用说明：
要在自己的 schema 中创建程序，需要 `CREATE JOB` 权限；拥有 `CREATE ANY JOB` 权限者可在任意 schema 创建。程序默认以禁用状态创建（除非 enabled 参数为 TRUE），启用前不能被作业执行。他人要使用你的程序须有 `EXECUTE` 权限，故创建程序后须授予 `EXECUTE` 权限。

参见："DEFINE_PROGRAM_ARGUMENT Procedure"。

---

#### CREATE_SCHEDULE Procedure

此过程创建一个调度（schedule）。

语法：

```
DBMS_SCHEDULER.CREATE_SCHEDULE (
   schedule_name          IN VARCHAR2,
   start_date             IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   repeat_interval        IN VARCHAR2,
   end_date               IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   comments               IN VARCHAR2 DEFAULT NULL);
```

参数（表 159-33）：

| 参数 | 说明 |
|---|---|
| schedule_name | 赋予该调度的名称，在 SQL 命名空间内唯一（不能与某 schema 中表同名），未指定会报错。 |
| start_date | 调度生效的第一个日期与时间。对重复调度，start_date 是参考日期——调度起始不一定是 start_date，而取决于 repeat_interval；start_date 用于确定调度的第一个实例。若 start_date 在过去且未指定 repeat_interval，则调度无效。对重复作业或窗口，未指定 start_date 时可从 repeat_interval 推导。start_date 为 null 时用作业/窗口启用时的日期。start_date 与 repeat_interval 不能同时为 null。 |
| repeat_interval | 调度重复的频率，用日历语法表达（见"日历语法"）。命名调度不允许用 PL/SQL 表达式作为重复间隔。 |
| end_date | 此日期时间之后作业不再运行、窗口不再打开。无 end_date 的非重复调度永久有效。end_date 须晚于 start_date，否则创建调度时报错。 |
| comments | 关于调度的可选注释，默认 NULL。 |

使用说明：
在自己 schema 创建调度需 `CREATE JOB` 权限，在他人 schema 创建（用 `schema.schedule_name`）需 `CREATE ANY JOB` 权限。调度创建后可被其他用户使用，并以对 PUBLIC 的访问创建，因此无需显式授权。

---

#### DEFINE_PROGRAM_ARGUMENT Procedure

此过程为程序参数定义名称或默认值。若程序参数未定义默认值，引用该程序的作业须提供参数值（作业也可覆盖默认值）。此过程有重载。

语法：

定义不带默认值的程序参数：
```
PROCEDURE define_program_argument(
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   out_argument            IN BOOLEAN DEFAULT FALSE);
```
定义带默认值的程序参数：
```
PROCEDURE define_program_argument(
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   default_value           IN VARCHAR2,
   out_argument            IN BOOLEAN DEFAULT FALSE);
```

参数（表 159-41）：

| 参数 | 说明 |
|---|---|
| program_name | 要修改的程序名，该程序必须存在。 |
| argument_position | 参数传给可执行文件时的位置。参数编号从 1 到程序的 number_of_arguments。必须唯一，会替换该位置已定义的参数。 |
| argument_name | 赋予参数的名称，可选但指定时须在该程序内唯一。赋名后可被其它包子程序使用（含 SET_JOB_ARGUMENT_VALUE）。 |
| argument_type | 所定义参数的数据类型。调度器不校验也不使用它，由程序用户决定赋值时使用。允许任意有效 SQL 数据类型。 |
| default_value | 作业未指定时赋予参数的默认值。 |
| out_argument | 保留供将来使用，必须设为 FALSE。 |

使用说明：
程序启用前，从 1 到 number_of_arguments 的所有参数都须已定义。若某参数未用此过程定义默认值，则作业中必须定义其值。定义程序参数要求你是程序属主或对其有 `ALTER` 权限，或拥有 `CREATE ANY JOB` 权限。`DEFINE_PROGRAM_ARGUMENT` 仅支持 SQL 类型参数，故布尔等非 SQL 类型的值不能作为程序/作业参数。

参见：DEFINE_ANYDATA_ARGUMENT、SET_JOB_ARGUMENT_VALUE。

---

#### DISABLE Procedure

此过程禁用程序、作业、链、窗口、数据库目标、外部目标、文件监视器或组。对象被禁用时其 `enabled` 属性设为 FALSE。

语法：

```
DBMS_SCHEDULER.DISABLE (
   name              IN VARCHAR2,
   force             IN BOOLEAN DEFAULT FALSE,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

参数（表 159-42）：

| 参数 | 说明 |
|---|---|
| name | 被禁用对象名，可为逗号分隔列表。指定作业类名时该类下所有作业被禁用（作业类本身不禁用）。指定组名时组被禁用，组成员的启用状态不受影响。 |
| force | 为 TRUE 时即使有其它对象依赖也禁用。详见使用说明。 |
| commit_semantics | 提交语义，支持：STOP_ON_FIRST_ERROR（默认）——遇第一个错误即返回，之前成功的禁用操作已提交；TRANSACTIONAL——遇第一个错误返回，此前所有操作回滚，仅禁用作业或作业列表时支持，且 force=TRUE 时不支持；ABSORB_ERRORS——尽量吸收错误并禁用其余作业，提交所有成功的禁用操作，出错时可查 SCHEDULER_BATCH_ERRORS 视图，仅禁用作业/作业列表时支持。 |

使用说明：
窗口名前须加 `SYS`。禁用已禁用的对象不报错。`force` 选项意在指出依赖，不改动被依赖对象。对窗口或 WINDOW 类型组执行 DISABLE 须有 `MANAGE SCHEDULER` 权限。除 SYS schema 外可在任意 schema 使用 DISABLE。

作业：禁用作业意味着虽有元数据但不运行，作业协调器不再拾取处理；作业在队列中的 state 改为 disabled。force=FALSE 且作业正在运行则报错；force=TRUE 则禁用但允许当前运行实例完成。多目标作业不能在特定目标禁用子作业，但可禁用目标。

程序：禁用后状态改为 disabled，虽有元数据但指向它的作业不能运行。force=FALSE 时程序须未被任何作业引用，否则报错；force=TRUE 时指向它的作业不禁用，但运行时会因程序无效而失败。正在运行、指向该程序的作业不受影响、可继续。程序禁用不影响其相关参数。

文件监视器：force=FALSE 时须未被任何作业引用，否则报错；强制禁用则依赖它的作业被禁用。

窗口：禁用后窗口不再打开但元数据仍在，可重新启用。force=FALSE 时窗口须未打开且未被作业引用，否则报错；force=TRUE 时禁用打开中的窗口会成功但不会关闭它，仅阻止其未来打开直到重新启用。窗口禁用时以其为调度的作业不会被禁用。

窗口组：禁用 WINDOW 类型组后，以该窗口组为调度的作业（运行中除外）在成员窗口打开时不再运行；但以组中某成员窗口为调度的作业仍运行。组元数据仍在可重新启用，注意组成员窗口仍会打开。force=FALSE 时组中成员须无打开或被作业引用，否则报错；force=TRUE 时组被禁用，打开的窗口不关闭不禁用、允许运行至结束，以该组为调度的作业不禁用。

作业链：禁用链后元数据仍在但指向它的作业不能运行，便于安全改动链而不至于运行不完整定义的链。force=FALSE 时链须未被作业引用，否则报错；force=TRUE 时指向它的作业不禁用但运行时失败。正在运行、指向该链的作业不受影响、可完成。

数据库目标：禁用时——多目标作业运行时跳过该目标；若某作业所有目标都被禁用，调度器尝试运行时报错；*_SCHEDULER_JOB_DESTS 中引用该数据库目标的作业的 REFS_ENABLED 列设为 FALSE。

外部目标：禁用时——依赖它的数据库目标保持启用，但调度器运行引用该外部目标的数据库目标的作业时报错；所有引用该外部目标的外部作业、以及数据库目标依赖该外部目标的所有数据库作业，在 *_SCHEDULER_JOB_DESTS 中 REFS_ENABLED 设为 FALSE。

组：禁用外部目标组或数据库目标组时，调度器运行以该组为目标名的作业时报错。

---

#### DROP_JOB Procedure

此过程删除一个或多个作业，或删除一个或多个作业类中的全部作业。删除作业也会删除该作业设置的所有参数值。

语法：

```
DBMS_SCHEDULER.DROP_JOB (
   job_name                IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE,
   defer                   IN BOOLEAN DEFAULT FALSE,
   commit_semantics        IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

参数（表 159-52）：

| 参数 | 说明 |
|---|---|
| job_name | 作业名或作业类名，可为逗号分隔列表。作业类须指定 SYS schema。指定作业类名时删除该类中所有作业（作业类本身不删）。 |
| force | 为 TRUE 时调度器先尝试停止运行中的作业实例（以 force=false 调 STOP_JOB），再删除作业。 |
| defer | 为 TRUE 时调度器允许运行中作业完成后再删除。 |
| commit_semantics | 提交语义：STOP_ON_FIRST_ERROR（默认）——遇第一个错误返回，之前成功的删除已提交；TRANSACTIONAL——遇第一个错误返回并回滚此前操作，force=TRUE 时不支持；ABSORB_ERRORS——尽量吸收错误删除其余作业并提交所有成功删除，出错可查 SCHEDULER_BATCH_ERRORS。job_name 列表含作业类时仅允许 STOP_ON_FIRST_ERROR。 |

使用说明：
force 与 defer 都为 FALSE 且调用时作业正在运行，删除该作业失败；整个 DROP_JOB 调用是否失败取决于 commit_semantics。force 与 defer 同时为 TRUE 报错。删除作业要求你是作业属主、或对其有 `ALTER` 对象权限、或拥有 `CREATE ANY JOB` 系统权限。

---

#### DROP_PROGRAM Procedure

此过程删除一个程序。删除程序时其相关参数也一并删除。

语法：

```
DBMS_SCHEDULER.DROP_PROGRAM (
   program_name            IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

参数（表 159-54）：

| 参数 | 说明 |
|---|---|
| program_name | 要删除的程序名，可为逗号分隔列表。 |
| force | 为 FALSE 时程序须未被任何作业引用，否则报错；为 TRUE 时引用该程序的所有作业在程序删除前先被禁用，正在运行、指向该程序的作业不受影响、可继续。 |

使用说明：
删除程序要求你是程序属主、或对其有 `ALTER` 权限、或拥有 `CREATE ANY JOB` 权限。

---

#### ENABLE Procedure

此过程启用程序、作业、链、窗口、数据库目标、外部目标、文件监视器或组。对象启用时 `enabled` 属性设为 TRUE。作业、链、程序默认创建为禁用；数据库目标、外部目标、文件监视器、窗口、组默认创建为启用。若作业原被禁用，启用后调度器按其调度自动运行。启用被禁用的作业还会重置 `*_SCHEDULER_JOBS` 视图中的 RUN_COUNT、FAILURE_COUNT、RETRY_COUNT。启用前做有效性检查，失败则不启用并返回相应错误。对象已启用时此过程不报错。

语法：

```
DBMS_SCHEDULER.ENABLE (
   name              IN VARCHAR2,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

参数（表 159-59）：

| 参数 | 说明 |
|---|---|
| name | 被启用的调度器对象名，可为逗号分隔列表。指定作业类名时该类下所有作业被启用；指定组名时组被启用，组成员启用状态不受影响。 |
| commit_semantics | 提交语义：STOP_ON_FIRST_ERROR（默认）——遇第一个错误返回，之前成功的启用已提交；TRANSACTIONAL——遇第一个错误返回并回滚此前操作，仅启用作业/作业列表时支持；ABSORB_ERRORS——尽量吸收错误并启用其余作业，提交所有成功启用，出错可查 SCHEDULER_BATCH_ERRORS，仅启用作业/作业列表时支持。 |

使用说明：
窗口名前须加 `SYS`。对窗口或 WINDOW 类型组执行 ENABLE 须有 `MANAGE SCHEDULER` 权限。对 EXECUTABLE 类型作业（或指向 EXECUTABLE 程序的作业），作业属主须有 `CREATE EXTERNAL JOB` 系统权限才能启用/运行。启用文件监视器时，文件监视器属主须对指定凭据有 `EXECUTE` 权限。除 SYS schema 外可在任意 schema 使用 ENABLE。

---

#### RUN_JOB Procedure

此过程立即运行作业。作业已启用时调度器自动运行，无需调用 RUN_JOB；RUN_JOB 用于在正常调度之外运行作业。

语法：

```
DBMS_SCHEDULER.RUN_JOB (
   job_name                IN VARCHAR2,
   use_current_session     IN BOOLEAN DEFAULT TRUE);
```

参数（表 159-79）：

| 参数 | 说明 |
|---|---|
| job_name | 作业名或逗号分隔列表，每项为已存在作业名（可前缀 schema 名加点）。指定多目标作业时在所有目标运行，此时 use_current_session 须为 FALSE。 |
| use_current_session | 作业运行是否在与调用过程相同的会话中进行。作业总是以作业属主身份、在属主 schema 运行，除非指定了凭据则用凭据中用户运行。为 TRUE 时：可在命令行测试作业并看到错误；*_scheduler_jobs 的 state/run_count/last_start_date/last_run_duration/failure_count 不更新；RUN_JOB 可与正常调度的作业并行运行。为 FALSE 时：须查作业日志找错误；*_scheduler_jobs 相关字段都更新；若正常调度的作业正在运行则 RUN_JOB 失败。对指定了目标/目标组、或指向 detached 属性为 TRUE 的链/程序的作业，use_current_session 必须为 FALSE。 |

使用说明：
作业不必已启用。禁用作业运行前做有效性检查：指向有效作业类；作业属主对作业类有 EXECUTE 权限；引用的程序/链存在且属主有权执行；所有参数值已设（或有默认）；外部作业的属主有 CREATE EXTERNAL JOB 权限。

use_current_session 为 TRUE 不允许用于：destination_name 属性指定目标/目标组的作业、链作业、使用 detached 程序的作业。

use_current_session=TRUE 时 RUN_JOB 阻塞至作业完成，执行中错误作为错误返回给 RUN_JOB，不更新作业状态、不出现在 *_SCHEDULER_RUNNING_JOBS。use_current_session=FALSE 时 RUN_JOB 立即返回，作业由协调器拾取并交作业从属执行，须查视图与日志获知结果。多个用户会话可在 use_current_session=TRUE 时同时各自 RUN_JOB。RUN_JOB 要求你拥有该作业或对其有 `ALTER` 权限，或拥有 `CREATE ANY JOB` 权限。

示例：
```
BEGIN
  DBMS_SCHEDULER.RUN_JOB(
    JOB_NAME            => 'EODJOB, DSS.ETLJOB',
    USE_CURRENT_SESSION => FALSE);
END;
```

---

#### SET_JOB_ARGUMENT_VALUE Procedure

此过程设置作业参数的值。它会覆盖对应程序或存储过程参数的默认值。参数可按位置或按名指定，按名指定仅当：作业指向已保存的程序对象，且参数已由 DEFINE_PROGRAM_ARGUMENT 或 DEFINE_METADATA_ARGUMENT 赋名。调度器任何时刻都不做参数类型检查。此过程有重载。

语法：

按位置设置：
```
DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_value          IN VARCHAR2);
```
按名设置：
```
DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_name           IN VARCHAR2,
   argument_value          IN VARCHAR2);
```

参数（表 159-98）：

| 参数 | 说明 |
|---|---|
| job_name | 要修改的作业名。 |
| argument_name | 所设程序参数的名。 |
| argument_position | 所设程序参数的位置。 |
| argument_value | 为程序参数设置的新值。设置非 VARCHAR 值须用 SET_JOB_ANYDATA_VALUE 过程。 |

使用说明：
要求你是作业属主或对其有 `ALTER` 权限，或拥有 `CREATE ANY JOB` 权限。仅支持 SQL 类型参数，布尔等非 SQL 类型不支持。可用于设置轻量级作业参数，但仅当参数类型为 VARCHAR2。

参见：SET_JOB_ANYDATA_VALUE、DEFINE_PROGRAM_ARGUMENT。

---

#### STOP_JOB Procedure

此过程停止正在运行的作业或某作业类中的所有作业。停止后，一次性作业的 state 设为 STOPPED，重复作业的 state 设为 SCHEDULED 或 COMPLETED（取决于下次运行是否已调度）。指向链的作业被停止时，运行中链的所有运行步骤被停止。多目标作业时，数据库尝试在所有目标停止该作业。对外部作业，STOP_JOB 仅停止由作业动作直接启动的外部进程，不停止外部作业的子进程。对 RAC 环境中的 in-memory full 作业，STOP_JOB 用作业定义的 instance_id 属性确定在哪个实例停止（属性为 null 则所有实例）。

语法：
```
DBMS_SCHEDULER.STOP_JOB (
   job_name         IN VARCHAR2
   force            IN BOOLEAN DEFAULT FALSE
   commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

参数（表 159-102）：

| 参数 | 说明 |
|---|---|
| job_name | 要停止的作业名，可为逗号分隔列表，每项可为：作业名（可前缀 schema 加点）；作业目标 ID（*_SCHEDULER_JOB_DESTS 的 JOB_DEST_ID 列所得，代表作业+凭据+目标的唯一组合）；作业类（须前缀 SYS schema 加点，指定时该类所有作业被停止）。指定以目标组为 destination_name 的作业时，所有目标上所有作业实例被停止。 |
| force | 为 FALSE 时调度器尝试用中断机制优雅停止（让从属进程拿回控制以更新队列为 stopped），失败则报错；为 TRUE 时调度器立即终止作业从属，建议仅在 force=FALSE 失败后再用 force=TRUE，使用 force 选项须有 MANAGE SCHEDULER 系统权限。 |
| commit_semantics | 提交语义：STOP_ON_FIRST_ERROR（默认）——遇第一个错误返回并提交之前成功的停止；ABSORB_ERRORS——尽量吸收错误停止其余作业并提交所有成功停止，仅当 job_name 列表不含作业类时可用，出错可查 SCHEDULER_BATCH_ERRORS。 |

使用说明：
不带 force 的 STOP_JOB 要求你是作业属主或对其有 `ALTER` 权限，或拥有 `CREATE ANY JOB` 或 `MANAGE SCHEDULER` 权限。带 force 的 STOP_JOB 要求有 `MANAGE SCHEDULER` 权限。

示例：
```
BEGIN
  DBMS_SCHEDULER.STOP_JOB('DSS.ETLJOB, 984, 1223, SYS.ETL_JOBCLASS');
END;
```

---

#### EVALUATE_CALENDAR_STRING Procedure

可用调度器日历语法定义作业、窗口或调度的重复间隔。此过程对日历表达式求值，告诉你作业或窗口的下一次执行日期时间。便于在不实际调度作业/窗口的情况下测试日历串定义是否正确。通过把一次调用返回的 next_run_date 作为下次调用的 return_date_after 参数，可获取重复间隔的多个步骤。日历语法见"操作说明"。

语法：
```
DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING (
   calendar_string    IN  VARCHAR2,
   start_date         IN  TIMESTAMP WITH TIME ZONE,
   return_date_after  IN  TIMESTAMP WITH TIME ZONE,
   next_run_date      OUT TIMESTAMP WITH TIME ZONE);
```

参数（表 159-61）：

| 参数 | 说明 |
|---|---|
| calendar_string | 要求值的日历表达式，须为"操作说明"中所述日历语法。 |
| start_date | 重复间隔生效的日期时间，也可用于填充日历串中缺失的特定项，可为 NULL。 |
| return_date_after | 帮助调度器从 start_date 与日历串确定的所有可能匹配（所有有效执行日期）中决定返回哪一个。传 NULL 时调度器自动填入 systimestamp。 |
| next_run_date | 在 return_date_after 值之后、与日历串和 start_date 匹配的第一个时间戳。 |

示例：以下代码片段可用于确定给定日历串下作业将运行的下五个日期。
```
SET SERVEROUTPUT ON;
ALTER SESSION set NLS_DATE_FORMAT = 'DD-MON-YYYY HH24:MI:SS';

DECLARE
start_date        TIMESTAMP;
return_date_after TIMESTAMP;
next_run_date     TIMESTAMP;
BEGIN
start_date :=
  to_timestamp_tz('01-JAN-2003 10:00:00','DD-MON-YYYY HH24:MI:SS');
return_date_after := start_date;
FOR i IN 1..5 LOOP
  DBMS_SCHEDULER.EVALUATE_CALENDAR_STRING(
    'FREQ=DAILY;BYHOUR=9;BYMINUTE=30;BYDAY=MON,TUE,WED,THU,FRI',
    start_date, return_date_after, next_run_date);
DBMS_OUTPUT.PUT_LINE('next_run_date: ' || next_run_date);
return_date_after := next_run_date;
END LOOP;
END;
/
```
输出：
```
next_run_date: 02-JAN-03 09.30.00.000000 AM
next_run_date: 03-JAN-03 09.30.00.000000 AM
next_run_date: 06-JAN-03 09.30.00.000000 AM
next_run_date: 07-JAN-03 09.30.00.000000 AM
next_run_date: 08-JAN-03 09.30.00.000000 AM
PL/SQL procedure successfully completed.
```

使用说明：无需特定调度器权限。

---

#### CREATE_JOB Procedure

此过程创建单个作业。若通过把 `enabled` 属性设为 TRUE 创建为已启用，调度器会按其调度自动运行作业；若创建为禁用，则作业直到用 SET_ATTRIBUTE 启用后才运行。此过程有重载，各语法形式的功能随语法声明给出。

语法：

（1）单次调用创建作业，不使用已存在的程序或调度：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name             IN VARCHAR2,
   job_type             IN VARCHAR2,
   job_action           IN VARCHAR2,
   number_of_arguments  IN PLS_INTEGER              DEFAULT 0,
   start_date           IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   repeat_interval      IN VARCHAR2                 DEFAULT NULL,
   end_date             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class            IN VARCHAR2                 DEFAULT 'DEFAULT_JOB_CLASS',
   enabled              IN BOOLEAN                  DEFAULT FALSE,
   auto_drop            IN BOOLEAN                  DEFAULT TRUE,
   comments             IN VARCHAR2                 DEFAULT NULL,
   credential_name      IN VARCHAR2                 DEFAULT NULL,
   destination_name     IN VARCHAR2                 DEFAULT NULL);
```
（2）使用命名调度对象与命名程序对象：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   program_name            IN VARCHAR2,
   schedule_name           IN VARCHAR2,
   job_class               IN VARCHAR2              DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN               DEFAULT FALSE,
   auto_drop               IN BOOLEAN               DEFAULT TRUE,
   comments                IN VARCHAR2              DEFAULT NULL,
   job_style               IN VARCHAR2              DEFAULT 'REGULAR',
   credential_name         IN VARCHAR2              DEFAULT NULL,
   destination_name        IN VARCHAR2              DEFAULT NULL);
```
（3）使用命名程序对象 + 内联调度：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name             IN VARCHAR2,
   program_name         IN VARCHAR2,
   start_date           IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   repeat_interval      IN VARCHAR2                 DEFAULT NULL,
   end_date             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class            IN VARCHAR2                 DEFAULT 'DEFAULT_JOB_CLASS',
   enabled              IN BOOLEAN                  DEFAULT FALSE,
   auto_drop            IN BOOLEAN                  DEFAULT TRUE,
   comments             IN VARCHAR2                 DEFAULT NULL,
   job_style            IN VARCHAR2                 DEFAULT 'REGULAR',
   credential_name      IN VARCHAR2                 DEFAULT NULL,
   destination_name     IN VARCHAR2                 DEFAULT NULL);
```
（4）使用命名调度对象 + 内联程序：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   schedule_name           IN VARCHAR2,
   job_type                IN VARCHAR2,
   job_action              IN VARCHAR2,
   number_of_arguments     IN PLS_INTEGER       DEFAULT 0,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);
```
（5）使用内联程序 + 事件：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   job_type                IN VARCHAR2,
   job_action              IN VARCHAR2,
   number_of_arguments     IN PLS_INTEGER       DEFAULT 0,
   start_date              IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   event_condition         IN VARCHAR2          DEFAULT NULL,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);
```
（6）使用命名程序对象 + 事件：
```
DBMS_SCHEDULER.CREATE_JOB (
   job_name                IN VARCHAR2,
   program_name            IN VARCHAR2,
   start_date              IN TIMESTAMP WITH TIME ZONE,
   event_condition         IN VARCHAR2,
   queue_spec              IN VARCHAR2,
   end_date                IN TIMESTAMP WITH TIME ZONE,
   job_class               IN VARCHAR2          DEFAULT 'DEFAULT_JOB_CLASS',
   enabled                 IN BOOLEAN           DEFAULT FALSE,
   auto_drop               IN BOOLEAN           DEFAULT TRUE,
   comments                IN VARCHAR2          DEFAULT NULL,
   job_style               IN VARCHAR2          DEFAULT 'REGULAR',
   credential_name         IN VARCHAR2          DEFAULT NULL,
   destination_name        IN VARCHAR2          DEFAULT NULL);
```

参数（表 159-28 CREATE_JOB Procedure Parameters）：

| 参数 | 说明 |
|---|---|
| job_name | 赋予作业的名称，在 SQL 命名空间内唯一（不能与某 schema 中表同名）。作业如在其它 schema 须加 schema 名限定。未指定会报错。若想由调度器生成名称，可用 GENERATE_JOB_NAME 过程生成名称再用于 CREATE_JOB（它从序列生成数字作为作业名，可加字符串前缀，作业名即该字符串+序列数字，见"GENERATE_JOB_NAME Function"）。 |
| job_type | 指定所创建作业类型，未指定报错（详见下一行 job_action）。取值：'PLSQL_BLOCK'——作业为匿名 PL/SQL 块，不支持参数，number_of_arguments 必须为 0；'STORED_PROCEDURE'——作业为 PL/SQL 或 Java 存储过程或外部 C 子程序，仅支持过程、不支持有返回值的函数；'EXECUTABLE'——作业在数据库外用外部可执行文件运行（任何可从命令行执行者），不支持 AnyData 参数，作业属主须有 CREATE EXTERNAL JOB 系统权限才能启用/运行；'CHAIN'——作业为链，不支持参数，number_of_arguments 须为 0；'EXTERNAL_SCRIPT'——作业为外部脚本，用运行作业机器的命令 shell（Windows=cmd.exe，UNIX=sh，除非首行 `#!` 指定）；'SQL_SCRIPT'——作业为 SQL*Plus 脚本，作业须指向含有效 OS 用户名/口令的凭据，由 SQL*Plus 可执行文件运行；可指向含数据库凭据的连接凭据（若有则运行脚本前用它连接数据库；用连接凭据须用 set_attribute 设 Connect_Credential_Name；无则须在脚本中含显式 SQL*Plus connect 语句并提供有效数据库用户/口令），作业属主须有 CREATE EXTERNAL JOB 权限；'BACKUP_SCRIPT'——作业为 RMAN 备份脚本，脚本执行目标命令前先运行用口令或 OS 认证的 connect 语句，作业指向含有效 OS 用户名/口令的凭据，RMAN 会话在该 OS 用户下运行，调度器用当前 Oracle home 的 RMAN 可执行文件运行脚本（缺失报错），作业属主须有 CREATE EXTERNAL JOB 权限。 |
| job_action | 指定作业动作，内联程序未指定会在创建时报错。作业动作在自治事务中执行，适用所有自治事务指南与限制（如自治事务中不允许 online DDL，故不能用于作业动作）。可能动作：PL/SQL 块——动作为执行 PL/SQL 代码，块须以分号结尾（如 `my_proc();`/`BEGIN my_proc(); END;`/`DECLARE arg pls_integer:=10; BEGIN my_proc2(arg); END;`），调度器把 job_action 包在自己块中（`DECLARE ... BEGIN job_action END;`）以声明内部变量；可在代码中用除 event_message 外的任何调度器元数据属性（属性名作标识符，调度器赋值，见 Table 159-40）；存储过程——动作为存储过程名，过程在其它 schema 须指定 schema，大小写敏感时用双引号括起（`job_action=>'"Schema"."Procedure"'`），STORED_PROCEDURE 类型不支持带 INOUT/OUT 参数的 PL/SQL 过程作 job_action；可执行文件——动作为外部可执行文件名（含全路径，不含命令行参数），以 `?` 开头时替换为本地作业 Oracle home 或远程作业调度器代理 home，含 `@` 且本地作业时替换为当前实例 SID，注意不支持 shell 脚本语法、只支持可执行文件名与路径；链——动作为调度器链对象名，链在其它 schema 须指定 schema；外部脚本——job_action 为 OS 脚本路径或内联脚本，路径须存在于每台运行机器上，可调用 SQL*Plus/RMAN（无需全路径），参数只能为字符串或可转字符串者、按位置传入，作业须指向含有效 OS 用户名/口令的凭据；SQL 脚本——job_action 为 SQL*Plus 脚本路径或内联脚本，参数同上，命名参数还会绑定到 SQL*Plus 会话命名变量；备份脚本——job_action 为 RMAN 脚本路径或内联脚本，参数同上。 |
| number_of_arguments | 作业期望的参数个数，范围 0–255，默认 0。 |
| program_name | 与该作业关联的程序名。程序类型为 EXECUTABLE 时作业属主须有 CREATE EXTERNAL JOB 系统权限才能启用/运行。 |
| start_date | 作业计划首次开始的日期时间。start_date 与 repeat_interval 都为 null 时作业在启用后尽快运行。对用日历表达式指定重复间隔的重复作业，start_date 作参考日期，作业首次运行为当前日期时间起（含）日历表达式的第一个匹配。系统过载时调度器不能保证精确时间执行。 |
| event_condition | 基于事件源队列表列的条件表达式，须为高级队列（AQ）规则语法。消息载荷为对象类型时可在表达式中包含用户数据属性，对象属性前须加 `tab.user_data`。规则详见 DBMS_AQADM.ADD_SUBSCRIBER。 |
| queue_spec | 指定以下之一： enqueue 此作业启动事件的源队列——安全队列时 queue_spec 为 `queue_name, agent name` 对，非安全队列只需队列名；未提供全限定队列名则认为在作业属主 schema 中，安全队列的 agent 名须属于当前订阅该队列的有效 agent。或一个文件监视器名（见《Administrator's Guide》）。 |
| repeat_interval | 作业重复频率，可用日历或 PL/SQL 表达式。表达式求值以确定下次运行时间。未指定则作业在指定 start_date 只运行一次。见"日历语法"。 |
| schedule_name | 与该作业关联的调度、窗口或窗口组名。 |
| job_class | 该作业关联的作业类。 |
| end_date | 作业过期、不再运行的日期时间。超过后若 auto_drop 为 TRUE 则作业被删除；若 auto_drop 为 FALSE 则作业被禁用且 STATE 设为 COMPLETED。未指定则永久重复，除非设了 max_runs 或 max_failures（达到时停止）。end_date 须晚于 start_date，否则报错；二者相同则作业不执行且不报错。 |
| comments | 关于作业的注释，默认 NULL。 |
| job_style | 所创建作业样式，取值：'REGULAR'（默认，常规作业）；'LIGHTWEIGHT'（轻量级作业，仅当作业引用程序对象时允许，适用于频繁运行的短作业，特定场景有小幅性能提升）；'IN_MEMORY_RUNTIME'（内存中运行时作业，基于轻量级结构、规则限制相同，但保留内存缓存以最小化运行前后磁盘访问、进一步提升性能）；'IN_MEMORY_FULL'（内存中完整作业，须有程序、不能有调度或重复间隔，启用时自动运行、运行后丢弃，所有信息在内存、不落盘，实例重启即丢失，用于须以最低开销立即执行的动作）。 |
| credential_name | 作业默认凭据，仅适用于远程数据库作业、远程外部作业、本地外部作业、脚本作业及处理文件到达事件的事件作业，凭据必须存在。本地数据库作业须为 NULL。仅本地外部作业：此属性为 NULL（默认）时选用首选（默认）凭据（见《Administrator's Guide》）。参见 CREATE_CREDENTIAL。 |
| destination_name | 作业的数据库目标或外部目标，仅用于远程数据库作业与远程外部作业；本地数据库或本地外部（可执行）作业须为 NULL。可为单个目标名或 'EXTERNAL_DEST'/'DB_DEST' 类型组名。单个目标或组须已存在：数据库目标须由 CREATE_DATABASE_DESTINATION 创建；外部目标由向本地数据库注册远程调度器代理时隐式创建；组则每个成员须存在、作业在组中所有目标上运行（见 CREATE_GROUP）。destination_name 不能引用目标组当：作业类型为 'CHAIN'；作业样式为 'LIGHTWEIGHT'/'IN_MEMORY_RUNTIME'/'IN_MEMORY_FULL'。若 CREATE_JOB 的 credential_name 参数为 NULL，每个目标前须带凭据，格式 `credential.destination`，凭据须已存在；若提供 credential_name 则作为未带凭据目标的默认凭据。可查 *_SCHEDULER_DB_DESTS、ALL_SCHEDULER_EXTERNAL_DESTS、*_SCHEDULER_GROUP_MEMBERS。注：destination 作业属性在 11gR2 已弃用，由 destination_name 取代。 |
| enabled | 是否创建为已启用（TRUE/FALSE），默认 FALSE 即创建为禁用。禁用作业意味着元数据已捕获、作为数据库对象存在，但调度器忽略它、协调器不拾取；要运行须启用——置此参数为 TRUE 或用 ENABLE 过程。 |
| auto_drop | 为 TRUE 时作业完成或被自动禁用后自动删除。作业完成指：end_date（或调度 end_date）已过（注意以窗口为调度的作业窗口关闭时不视为窗口结束、不自动删除）；已运行 max_runs 次（max_runs 须用 SET_ATTRIBUTE 设）；非重复作业且已运行一次。作业失败 max_failures 次时被禁用（max_failures 亦用 SET_ATTRIBUTE 设）。为 FALSE 时不删除、元数据保留至显式 DROP_JOB。默认 TRUE。 |

使用说明：
作业默认创建为禁用，须显式启用才活动、调度。启用前确保所有程序参数（若有）已定义——在程序对象中定义默认值或随作业提供值。初始化参数 `JOB_QUEUE_PROCESSES` 指定作业执行可创建的最大进程数；自 11gR2 起对 `DBMS_SCHEDULER` 作业生效，设为 0 则禁用 `DBMS_SCHEDULER` 作业。在自己 schema 创建作业需 `CREATE JOB` 权限；`CREATE ANY JOB` 可在任意 schema 创建；作业在其它 schema 须加 schema 名限定。EXECUTABLE 类型作业（或指向 EXECUTABLE 程序）的属主须有 `CREATE EXTERNAL JOB` 系统权限。作业关联特定类或程序需对其有 `EXECUTE` 权限。并非所有作业属性都可用 CREATE_JOB 设，部分须创建后设（如作业参数用 SET_JOB_ARGUMENT_VALUE/SET_JOB_ANYDATA_VALUE，job_priority、max_runs 等用 SET_ATTRIBUTE）。高效创建多作业用 CREATE_JOBS。注意：事件作业对每个匹配事件条件的事件运行一次，但作业正在运行期间发生的事件被忽略——事件被消费但不触发再次运行。

---

#### SET_ATTRIBUTE Procedure

此过程修改调度器对象的某个属性。有重载，可接受多种类型的值。要把属性设为 `NULL` 用 `SET_ATTRIBUTE_NULL` 过程。可设的属性取决于被改对象。除对象名外，所有对象属性都可改。

语法：
```
DBMS_SCHEDULER.SET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          IN {BOOLEAN|DATE|TIMESTAMP|
                        TIMESTAMP WITH TIME ZONE|TIMESTAMP WITH LOCAL TIME ZONE|
                        INTERVAL DAY TO SECOND});
DBMS_SCHEDULER.SET_ATTRIBUTE (
   name           IN VARCHAR2,
   attribute      IN VARCHAR2,
   value          IN VARCHAR2,
   value2         IN VARCHAR2 DEFAULT NULL);
```

参数（表 159-81）：

| 参数 | 说明 |
|---|---|
| name | 对象名。 |
| attribute | 见表 159-83 至 159-93。 |
| value | 为属性设的新值，不能为 NULL（设 NULL 用 SET_ATTRIBUTE_NULL）。 |
| value2 | 可选第二个值。多数属性仅一个值，部分可有两个。 |

表 159-82 是调度器对象类型及其属性表的目录，这些对象类型可用调度器数据字典视图查看（见《Administrator's Guide》）。

表 159-82 调度器对象类型的属性表

| 调度器对象类型 | 属性表 |
|---|---|
| Job | 159-83 |
| Program | 159-85 |
| Schedule | 159-86 |
| File Watcher | 159-87 |
| Job Class | 159-88 |
| Window | 159-89 |
| Chain | 159-90 |
| Database Destination | 159-91 |
| External Destination | 159-92 |
| Group | 159-93 |
| Credential | 159-94 |
| Resource | 159-95 |

使用说明：
若对象被改且原为启用状态，调度器先禁用它、再改、再重新启用；重新启用过程中出错则不重新启用并报错。若对象被改且原为禁用状态，改后仍禁用。对窗口、WINDOW 类型组或作业类执行 SET_ATTRIBUTE 须有 `MANAGE SCHEDULER` 权限；否则须是对象属主或对其有 `ALTER` 权限或拥有 `CREATE ANY JOB` 权限。

作业：调用 SET_ATTRIBUTE 时若作业有运行中实例，不受影响，改动仅影响后续运行。作业运行时改调度属性（schedule_name、start_date、end_date、repeat_interval），下次运行用新调度属性。运行时改程序属性（program_name、job_action、job_type、number_of_arguments），下次运行生效。运行时改作业参数值，下次运行生效。授予作业的 `ALTER` 权限允许用户改除程序属性（program_name、job_type、job_action、program_action、number_of_arguments）外的所有属性，且不允许用 PL/SQL 表达式指定作业调度。Oracle 建议不要改动数据库自动创建的作业（作业视图中 SYSTEM 列为 TRUE 者）。

程序：若当前运行中作业使用了被改的程序，它们继续用改动前的程序定义；下次执行时用新定义。调度：改调度不影响使用它的运行中作业和已打开窗口，改动在下次作业运行/窗口打开时生效。文件监视器：改文件监视器不影响当前由文件到达事件启动的运行中事件作业；本地系统上，新属性在下次文件监视器检查文件到达时生效（默认每 10 分钟），远程系统可能有额外延迟。作业类：除默认作业类外都可改，改作业类须有 `MANAGE SCHEDULER` 权限；改动不影响类中运行中作业，仅对未开始运行的作业生效，作业类名前须加 `SYS`。窗口：改窗口不影响活动窗口，改动下次打开时生效；无当前资源计划时，带指定资源计划的窗口打开时资源管理器以该计划激活；窗口名前须加 `SYS`。

**作业属性值**（表 159-83，详见 CREATE_JOB/CREATE_JOBS）：

| 名称 | 说明 |
|---|---|
| allow_runs_in_restricted_mode | 为 TRUE 时允许作业在数据库受限模式下运行（前提是作业属主允许在此模式登录）。默认 FALSE。 |
| auto_drop | 为 TRUE 时作业完成或被自动禁用后自动删除。完成指：end_date（或调度 end_date）已过；已运行 max_runs 次（max_runs 用 SET_ATTRIBUTE 设）；非重复作业且已运行一次。失败 max_failures 次时自动禁用（max_failures 用 SET_ATTRIBUTE 设）。为 FALSE 时不删除，元数据保留至显式 DROP_JOB。默认 TRUE。 |
| comments | 可选注释。 |
| connect_credential_name | 可指向数据库凭据。对 SQL*Plus/备份脚本作业，凭据用于运行脚本前连接数据库；其它作业类型忽略。作业属主须对该凭据有 EXECUTE 权限否则作业失败。推荐用此属性，使口令安全存于数据库凭据而非明文出现在作业/程序动作/脚本中。 |
| credential_name | 远程数据库作业、远程外部作业、本地外部作业或处理文件到达事件的事件作业所用的凭据对象名。仅本地外部作业：为 NULL（默认）时选用首选（默认）凭据（见《Administrator's Guide》）。 |
| database_role | 用于 Data Guard 环境。设为 'PRIMARY' 则仅数据库为主库时运行；'LOGICAL STANDBY' 则仅逻辑备库时运行。主库时默认 'PRIMARY'，逻辑备库时默认 'LOGICAL STANDBY'。注意：要让作业在某主机所有数据库角色下运行，须在该主机创建两份作业，一份 'PRIMARY'、一份 'LOGICAL STANDBY'。 |
| destination | 11gR2 已弃用，改用 destination_name。指定远程外部作业运行主机，设为主机名或 IP，可选加端口，格式 `hostname:port`。默认 NULL。 |
| destination_name | 作业的数据库目标或外部目标，仅用于远程数据库/远程外部作业；本地数据库或本地外部作业须为 NULL。详见表 159-28。 |
| end_date | 作业过期、不再运行的日期时间。超过后 auto_drop 为 TRUE 则删除；为 FALSE 则禁用且 STATE=COMPLETED。未指定则永久重复，除非 max_runs/max_failures 达到。须晚于 start_date，否则报错；二者相同则不执行且不报错。 |
| event_spec | 取两个值：value 为事件条件，value2 为队列规范。详见 CREATE_JOB 的 event_condition、queue_spec。 |
| follow_default_timezone | 为 TRUE 且作业 start_date 为 null 时，default_timezone 调度器属性改变后调度器重算下次运行日期时间以符合新时区（如原 02:00 则新时区也 02:00）。start_date 非 null 时运行日期时间由 start_date 时区决定。为 FALSE 时不重算（旧时区比新早 3 小时则原 02:00 在新时区变 05:00）。夏冬切换不改默认时区名。 |
| instance_id | 仅 RAC 环境有效，指示作业在哪个实例运行。 |
| instance_stickiness | 仅 RAC 环境用，默认 TRUE。TRUE 时作业在负载最轻实例启动，之后尽量在同一实例运行；该实例宕机或长时间过载则在另一实例运行；运行间隔大时忽略此属性、按非粘性处理。FALSE 时每次在首个可用实例运行。非 RAC 无用。 |
| job_action | 作业执行的动作，取决于 job_type（如 STORED_PROCEDURE 时为存储过程名）。 |
| job_class | 作业关联的类。 |
| job_priority | 作业相对同类作业的优先级。同类多个作业同时计划执行时由它决定协调器拾取顺序，取值 1–5，1 最先。创建时未指定默认 3。 |
| job_type | 作业类型，取值：'PLSQL_BLOCK'、'STORED_PROCEDURE'、'EXECUTABLE'、'CHAIN'、'EXTERNAL_SCRIPT'、'SQL_SCRIPT'、'BACKUP_SCRIPT'。设了它则 program_name 须为 NULL。 |
| job_weight | 11gR2 已弃用，勿改默认值 1。并行执行的作业权重。 |
| logging_level | 记日志多少：LOGGING_OFF（默认，不记录，但作业类日志级别优先、可能仍记录）；LOGGING_FAILED_RUNS（只记失败及原因，作业类级别更高则优先）；LOGGING_RUNS（对该类每个作业所有运行写详细日志）；LOGGING_FULL（除每次运行外还记录对作业的所有操作：create、enable、disable、alter、stop 等）。 |
| max_failures | 作业连续失败多少次后自动禁用，禁用后不再执行且 STATE=BROKEN。取值 1–1,000,000，默认 NULL（不论失败多少次都启动新实例）。 |
| max_run_duration | 作业允许运行的最长时间（INTERVAL DAY TO SECOND）。设非零非 NULL 且作业运行超过则触发 JOB_OVER_MAX_DUR 事件，由事件处理器决定是否让其继续。 |
| max_runs | 作业连续计划运行的最大次数。达到后作业禁用、state=COMPLETED。取值 1–1,000,000，默认 NULL（永久重复或至 end_date/max_failures）。 |
| number_of_arguments | 内联程序的参数个数。设了它则 program_name 须为 NULL。 |
| parallel_instances | 布尔，仅事件作业可设。FALSE（默认）时若事件发生而处理该事件的事件作业正在运行则新事件被忽略；TRUE 时为每个事件实例启动一个作业实例，每个为轻量级作业故可并行，各轻量级作业从父作业定义取属性（动作、最大运行时长等），完成后丢弃。同时运行的轻量级作业数无显式上限（受系统资源限制），不在 *_SCHEDULER_JOBS 但在 *_SCHEDULER_RUNNING_JOBS 中，名同父作业、自动生成子名区分。 |
| program_name | 作业所用程序对象名。设了它则 job_action、job_type、number_of_arguments 须为 NULL。 |
| raise_events | 告诉调度器在作业执行各阶段引发哪些事件，是位向量，可设以下位（各有包常量对应）：job_started=1、job_succeeded=2、job_failed=4、job_broken=8、job_completed=16、job_stopped=32、job_sch_lim_reached=64、job_disabled=128、job_chain_stalled=256、job_all_events=511、job_run_completed=job_succeeded+job_failed+job_stopped。详见表 159-84。 |
| repeat_interval | 返回下次运行日期时间的 PL/SQL 函数，或日历语法表达式。设了它则 schedule_name 须为 NULL。见"日历语法"。 |
| restartable | 作业失败能否重启，默认 FALSE。TRUE 时若作业运行中失败则从头重启；链作业为 TRUE 时应用失败后链从头重启，为 FALSE 或数据库失败时从最后运行步骤重启（该步骤的 restart_on_recovery 决定重启或标为停止；标为停止则链评估规则继续）。注意设 TRUE 可能导致数据不一致（如作业中已提交数据）。出错重试不计为常规运行，run/failure 计数在作业成功或六次重试全失败后才递增。调度器据此属性决定应用错误与数据库故障后是否重试，最多重试六次（第一次等 1 秒，之后每次乘 10）。六次重试全失败则 run、failure 计数各 +1；任一次重试成功则 run 计数 +1。停止重试条件：某次重试成功；六次重试全失败；下次重试将晚于下次常规调度运行（重复作业下次常规运行后不再重试）。 |
| schedule_limit | 重载系统下作业不一定按时启动。此属性让你在启动延迟超过指定间隔时不启动作业，取值 1 分钟到 99 天。如某作业应 12:00 启动、schedule_limit=60 分钟，则 13:00 前未启动则不运行。未指定则在有资源时尽快后续运行。默认 NULL（可在计划时间后任意时间运行）。因该属性跳过的计划运行不计入运行/失败次数，作业日志有记录。 |
| schedule_name | 用作作业调度的调度、窗口或 WINDOW 类型组名。设了它则 end_date、start_date、repeat_interval 须为 NULL。 |
| start_date | 作业起始或计划起始的原始日期时间。设了它则 schedule_name 须为 NULL。 |
| stop_on_window_close | 仅当作业调度为窗口或窗口组时适用。TRUE 表示关联窗口关闭时作业应停止（用 force=FALSE 的 stop_job 停）。默认 FALSE（不设则窗口关闭后作业继续；注意虽继续但资源分配可能因关窗换资源计划而变）。 |
| store_output | 布尔。TRUE 时对已记日志的运行，所有作业输出与错误消息存入 *_JOB_RUN_DETAILS。FALSE 则不存。新作业默认 TRUE。 |

表 159-84 调度器引发的事件类型（raise_events 属性取值）：

| 事件类型 | 说明 |
|---|---|
| job_all_events | 非事件，是启用所有事件的便捷常量。 |
| job_broken | 作业被禁用并转为 BROKEN 状态（超过 max_failures）。 |
| job_chain_stalled | 运行链的作业处于 CHAIN_STALLED：无步骤运行或计划运行且 evaluation_interval 为 NULL 时链停滞，须人工干预才推进。 |
| job_completed | 作业因达 max_runs 或 end_date 而完成。 |
| job_disabled | 作业被调度器或 SET_ATTRIBUTE 禁用。 |
| job_failed | 作业因错误或异常终止而失败。 |
| job_over_max_dur | 作业超过 max_run_duration 指定最大运行时长（此事件无需用 raise_events 启用，始终启用）。 |
| job_run_completed | 作业运行失败、成功或被停止。 |
| job_sch_lim_reached | 达到 schedule_limit：启动延迟超过 schedule_limit 故未启动。 |
| job_started | 作业启动。 |
| job_stopped | 作业被 STOP_JOB 停止。 |
| job_succeeded | 作业成功完成。 |

**程序属性值**（表 159-85，详见 CREATE_PROGRAM）：

| 名称 | 说明 |
|---|---|
| comments | 可选注释，描述程序功能或用法。 |
| detached | TRUE 则为 detached 程序（见《Administrator's Guide》）。 |
| number_of_arguments | 程序调用的存储过程或可执行文件所需参数个数。 |
| program_action | 程序执行的动作，取决于 program_type（如 STORED_PROCEDURE 时为存储过程名）。 |
| program_type | 程序类型，须为 'PLSQL_BLOCK'、'STORED_PROCEDURE'、'EXECUTABLE' 之一。 |

**调度属性值**（表 159-86，详见 CREATE_SCHEDULE）：

| 名称 | 说明 |
|---|---|
| comments | 可选注释。 |
| end_date | 调度不再指定日期的截止日期时间。 |
| event_spec | 取两个值：value 为事件条件，value2 为队列规范（见 CREATE_JOB 的 event_condition、queue_spec）。 |
| repeat_interval | 用日历语法指定调度重复频率。见"日历语法"。 |
| start_date | 日历语法用的起始/参考日期时间。 |

**文件监视器属性值**（表 159-87）：

| 参数 | 说明 |
|---|---|
| destination | 文件预期到达的远程主机名或 IP；NULL 则为主机。 |
| directory_path | 文件预期到达的目录；路径首部单个通配符 '?' 表示 Oracle home 路径（如 '?/rdbms/log' 表示 Oracle home 下 rdbms/log 子目录）。 |
| file_name | 要查找的文件名。允许两个通配符：'?' 单字符、'*' 零或多个字符。不能为 NULL。 |
| credential_name | 有效凭据对象名，文件监视器用它向主机 OS 认证以访问被监视文件；属主须对该凭据有 EXECUTE 权限。不能为 NULL。 |
| min_file_size | 文件被视为找到前的最小字节数，默认 0。 |
| steady_state_duration | 文件须保持不变的最小时间间隔后才视为找到；NULL 用内部值，下限 10 秒。 |
| comments | 可选注释。 |

**作业类属性值**（表 159-88，详见 CREATE_JOB_CLASS）：

| 名称 | 说明 |
|---|---|
| comments | 关于作业类的可选注释。 |
| log_history | 该类作业日志条目保留天数，范围 0–1,000,000；0 不保留历史；NULL 则由 log_history 调度器属性（SET_SCHEDULER_ATTRIBUTE 设）决定。 |
| logging_level | 记日志多少：LOGGING_OFF（此类所有作业不记录）；LOGGING_FAILED_RUNS（只记失败及原因）；LOGGING_RUNS（对此类每个作业所有运行写详细日志，默认）；LOGGING_FULL（除每次运行外还记录对作业的所有操作：create/enable/disable/alter/stop 等）。 |
| resource_consumer_group | 作业类关联的资源使用者组，类中所有作业在该组下运行（见《Administrator's Guide》）。 |
| service | 作业类中作业有亲和性的数据库服务。若同时设 resource_consumer_group 与 service 且 service 映射到某资源使用者组，则 resource_consumer_group 优先。 |

**窗口属性值**（表 159-89，详见 CREATE_WINDOW）：

| 名称 | 说明 |
|---|---|
| comments | 关于窗口的可选注释。 |
| duration | 窗口持续时间。 |
| end_date | 窗口不再打开的日期。设了它则 schedule_name 须为 NULL。 |
| repeat_interval | 用日历语法指定调度重复频率，不允许 PL/SQL 日期函数。设了它则 schedule_name 须为 NULL。见"日历语法"。 |
| resource_plan | 与窗口关联的资源计划。窗口打开时系统切换到该计划，关闭时恢复原计划；若某资源计划以 force 选项激活则不切换。仅一个资源计划可与窗口关联，可为 NULL 或空串。NULL 时窗口打开期间保持当时生效的资源计划；空串时窗口期间禁用资源管理器。 |
| schedule_name | 窗口所用调度名。设了它则 start_date、end_date、repeat_interval 须为 NULL。 |
| start_date | 窗口计划下次打开的日期时间。设了它则 schedule_name 须为 NULL。 |
| window_priority | 窗口优先级，'LOW'（默认）或 'HIGH'。 |

**链属性值**（表 159-90，详见 CREATE_CHAIN）：

| 名称 | 说明 |
|---|---|
| comments | 描述链用途的可选注释。 |
| evaluation_interval | 非 NULL 时除正常评估时机（作业启动、步骤完成、事件步骤事件到达）外，按此间隔额外评估链。仅当链规则用 SQL 语法且条件含调度器不可控元素时使用（额外间隔耗 CPU）；多数链正常评估时机已足够。 |
| rule_set_name | 正常情况不传入规则集，调度器自动创建规则集与空评估上下文，用 DEFINE_CHAIN_RULE 加规则、DROP_CHAIN_RULE 删规则。高级用户可创建描述链依赖的规则集传入以获更大灵活性（条件可引用外部变量、表可通过评估上下文暴露）。传入须确保为链规则集格式（如所有步骤须列为评估上下文变量）。不传则规则集形如 SCHED_RULESET${N}、评估上下文形如 SCHED_EVCTX${N}。 |

**数据库目标属性值**（表 159-91，详见 CREATE_DATABASE_DESTINATION）：

| 名称 | 说明 |
|---|---|
| agent | 用于连接远程数据库的外部目标（agent 目标）名，可从 ALL_SCHEDULER_EXTERNAL_DESTS 获取。 |
| connect_info | 标识要连接远程数据库的 TNS 连接描述符，或 tnsnames.ora 中解析为该描述符的网络服务名（别名）。对应 CREATE_DATABASE_DESTINATION 的 tns_name 参数。 |
| enabled | TRUE 则数据库目标已启用。 |
| comments | 关于数据库目标的可选注释。 |

**外部目标属性值**（表 159-92，外部目标仅由向本地数据库注册远程调度器代理时隐式创建）：

| 名称 | 说明 |
|---|---|
| hostname | （仅 GET_ATTRIBUTE）调度器代理所在机器的全限定主机名（含域）或 IP。 |
| port | （仅 GET_ATTRIBUTE）代理监听的 TCP 端口。 |
| ip_address | （仅 GET_ATTRIBUTE）代理所在主机 IP。 |
| enabled | TRUE 则外部目标已启用。 |
| comments | 关于外部目标的可选注释。 |

**组属性值**（表 159-93，详见 CREATE_GROUP）：

| 名称 | 说明 |
|---|---|
| group_type | （仅 GET_ATTRIBUTE）组类型（WINDOW、DB_DEST、EXTERNAL_DEST）。 |
| member_name | 逗号分隔的成员列表，替换现有列表；要在现有列表上加成员用 ADD_GROUP_MEMBER。对应 CREATE_GROUP 的 member 参数。 |
| enabled | TRUE 则组已启用。 |
| comments | 关于组的可选注释。 |
| number_of_members | （仅 GET_ATTRIBUTE）组成员数。 |

**凭据属性值**（表 159-94，自 12.1 起对 SET_ATTRIBUTE/GET_ATTRIBUTE 已弃用，建议用 DBMS_CREDENTIAL 包的 UPDATE_CREDENTIAL 的 attribute 参数）：

| 名称 | 说明 |
|---|---|
| username | 登录主机 OS 或远程 Oracle 数据库的用户名，最大 64。 |
| password | 该用户名的口令，最大 128。 |
| comments | 凭据描述，最大 240。 |
| windows_domain | Windows 远程可执行目标时该用户所属域，最大 64。 |
| database_role | 用作登录远程数据库运行远程数据库作业的系统权限，取值 SYSDBA、SYSOPER。 |

**资源属性值**（表 159-95）：

| 名称 | 说明 |
|---|---|
| resource_name | 资源名。 |
| units | 作业或程序使用的该资源单元数。 |
| status | 资源状态：ENFORCE_CONSTRAINTS（默认，强制执行资源限制，达最大单元数后不再启动使用该资源的作业）；IGNORE_CONSTRAINTS（忽略该资源任何约束）；BLOCKED_ALL_JOBS（不允许有该资源约束的任何作业运行，视为永久阻塞直到切换到另两种状态）。 |
| constraint_level | 约束级别：JOB_LEVEL 或 PROGRAM_LEVEL。对不兼容项，JOB_LEVEL 时成员须为作业，PROGRAM_LEVEL 时成员须为程序。 |
| comments | 关于资源的描述性注释。 |

---

> 以上为 `DBMS_SCHEDULER` 包精译部分（概述 + 高级包/调度相关核心过程：CREATE_JOB、CREATE_PROGRAM、CREATE_SCHEDULE、DEFINE_PROGRAM_ARGUMENT、DISABLE、DROP_JOB、DROP_PROGRAM、ENABLE、RUN_JOB、SET_ATTRIBUTE、SET_JOB_ARGUMENT_VALUE、STOP_JOB、EVALUATE_CALENDAR_STRING）。其余过程后续按需补译。
