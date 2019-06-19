# Udacity-Projects
Projects done under the Udacity Full Stack Development Program 
# PROJECT LOG ANALYSIS 
Project to explore a news database and print basic reporting statistics using a python program. The tables provided in the news database are as follows -
- authors 
- articles
- log 

The questions asked for reporting are as follows - 
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

# SETUP AND PRE-REQUISITIES 

- You should have the vagrant connection to remote server up and running so you can access the full setup that is needed to run the program
(Instructions found at Udacity's section 3, lesson 2) 
- You should be able to stand up the remote VM via the instructions  
```vagrant up```
- You should be able to connect to the environment using  
```vagrant ssh```
- You should load the news database provided by Udacity using  
```psql -d news -f newsdata.sql```
- You should then create the views that the Python program will be using , the views are as follows - 
- For Query 1  - This query asks about most popular 3 articles of all time. So we would be using the articles and the log tables to answer the question. 
  - ```CREATE VIEW popular_articles AS select split_part(path,'/',3), count(path) FROM log GROUP BY path ORDER BY count(path) DESC; ```
 


# CODE FILES 


# RUN PROGRAM 
Run the following Report.py program  - [a relative link](Report.py)
Syntax for running a python program on vagrant is -  
``` psql -d -news```
``` python Report.py ```
