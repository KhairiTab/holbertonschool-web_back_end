# MySQL Advanced
- Learning Objectives

How to create tables with constraint

How to optimize queries by adding indexes

What is and how to implement stored procedures and functions in MySQL

What is and how to implement views in MySQL

What is and how to implement triggers in MySQL

- Requirements

All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0

All your files should end with a new line

All your SQL queries should have a comment just before (i.e., syntax above)

All your files should start by a comment describing the task

All SQL keywords should be in uppercase (SELECT, WHERE...)

A README.md file, at the root of the folder of the project, is mandatory

The length of your files will be tested using wc

Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_ed_tvshows.sql" -o hbtn_ed_tvshows.sql
$ mysql -uroot -p hbtn_ed_tvshows < hbtn_ed_tvshows.sql
Enter password:
$ echo "SELECT * FROM tv_genres;" | mysql -uroot -p hbtn_ed_tvshows
Enter password:
1    Drama
2    Mystery
3    Adventure
4    Fantasy
5    Comedy
6    Crime
7    Suspense
8    Thriller

-Tasks

We are all unique!
In and not out
Best band ever!
Old school band
Buy buy buy
Email validation to sent
Add bonus
Average score
Optimize simple search
Optimize search and score
Safe divide
No table for a meeting