[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/xiG6Hhkb)
# SQL Assessment

SQL Schema

<img width="799" alt="Screenshot 2020-10-19 at 2 05 12 PM" src="https://user-images.githubusercontent.com/68887221/96415428-29d55680-1221-11eb-90d3-bc2fd66f0ce5.png">

##### IMPORTANT: the table name is CASE SENSITIVE (e.g. Worker is different from worker)
##### When you write the query, make sure to have the correct case of table name.

##### Also, make sure your dataframe column names are exactly same as the column names in expected output. (e.g.Salary is different from SALARY)

##### Problem 1: Write an SQL query to fetch “LAST_NAME” from Worker table.

Expected output (should be a dataframe):

```
   LAST_NAME
0        Doe
1      Smith
2        Lee
3    Johnson
4     Watson
5        Kim
6       Chen
7      White
8      Brown
9    Johnson
10    Nguyen
11    Harris
12      Tran
13     Lopez
14  Gonzalez
15     Perez
16  Madercod
```


##### Problem 2: Write an SQL query to fetch unique values of DEPARTMENT from Worker table with ascending Department name order.

Expected output (should be a dataframe):

```
         DEPARTMENT
0  Customer Service
1       Engineering
2         Executive
3           Finance
4   Human Resources
5                IT
6         Marketing
7        Operations
8             Sales
9      Supply Chain
```

##### Problem 3: Write an SQL query to print only the FIRST_NAME, SALARY details from the Worker table with  ascending FIRST_NAME order and descending SALARY order.

Expected output (should be a dataframe):

```
   FIRST_NAME  SALARY
0     Charles   72000
1       David  950000
2        Emma   68000
3       Frank   33000
4        Ivan   80000
5       James   85000
6        Jane   75000
7     Jessica   60000
8        John   80000
9       Kevin   80000
10       Lily   70000
11       Lisa   75000
12    Melissa   65000
13    Michael   90000
14   Samantha   68000
15        Tom   90000
16    Zachary   72000
```

##### Problem 4: Write an SQL query to fetch no. of workers for each department in the ascending order of number of worker.
##### Make sure to name the correct column stated in expected output.

Expected output (should be a dataframe):

```
         DEPARTMENT  WORKER_NUM
0         Executive           1
1      Supply Chain           1
2           Finance           1
3   Human Resources           1
4                IT           1
5       Engineering           2
6         Marketing           2
7        Operations           2
8  Customer Service           2
9             Sales           4
```

##### Problem 5: Write an SQL query to fetch the WORKER_TITLE, FIRST_NAME, SALARY with descending SALARY and ascending FIRST NAME as second sorting order.


Expected output (should be a dataframe):

```
                       WORKER_TITLE FIRST_NAME  SALARY
0                        Accountant      David  950000
1                 Assistant Manager    Michael   90000
2                     Sales Manager        Tom   90000
3              Supply Chain Manager      James   85000
4                Operations Manager       Ivan   80000
5                     Lead Engineer       John   80000
6                   Senior Engineer       John   80000
7                       Salesperson      Kevin   80000
8                           Manager       Jane   75000
9                 Financial Analyst       Lisa   75000
10               Software Developer    Charles   72000
11              Marketing Associate    Zachary   72000
12            Operations Supervisor       Lily   70000
13             Marketing Specialist       Emma   68000
14                    Sales Manager   Samantha   68000
15  Customer Service Representative    Melissa   65000
16                              CEO    Jessica   60000
17                      Salesperson      Frank   33000
```

##### Problem 6: Write an SQL query to fetch the list of employees with the same salary with descending SALARY and ascending FIRST NAME as second sorting order.
##### NOTE: WORKER_TITLE is the first column in the dataframe.

Expected output (should be a dataframe):
NOTE: WORKER_TITLE is the first column in the dataframe

```
            WORKER_TITLE FIRST_NAME  SALARY
0      Assistant Manager    Michael   90000
1          Sales Manager        Tom   90000
2     Operations Manager       Ivan   80000
3          Lead Engineer       John   80000
4        Senior Engineer       John   80000
5            Salesperson      Kevin   80000
6                Manager       Jane   75000
7      Financial Analyst       Lisa   75000
8     Software Developer    Charles   72000
9    Marketing Associate    Zachary   72000
10  Marketing Specialist       Emma   68000
11         Sales Manager   Samantha   68000
```

##### Problem 7: Write an SQL query to fetch the departments that have exactly 4 people in it. Make sure to name the correct column stated in expected output.

Expected output (should be a dataframe):

```
  DEPARTMENT  No_Of_Workers
0      Sales              4
```
