

import psycopg2, bleach,datetime



DBNAME = "news"

def popular_articles():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select articles.title,popular_articles.count FROM popular_articles INNER JOIN articles ON (popular_articles.split_part = articles.slug) LIMIT 3")
  pop_articles = c.fetchall()
  db.close()
  return pop_articles

def popular_authors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select authors.name,popular_authors.sum from authors INNER JOIN popular_authors ON (popular_authors.author = authors.id)")
  pop_authors_string = c.fetchall()
  db.close()
  return pop_authors_string

def error_report():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("SELECT (COUNT(*) FILTER (where status = '404 NOT FOUND') * 100.0 )/COUNT(*) AS ERROR_PERCENTAGE_PER_DAY,time::timestamp::date AS DATE FROM log GROUP BY DATE HAVING ((COUNT(*) FILTER (where status = '404 NOT FOUND') * 100.0) / COUNT(*))> 1")
  error_report_string = c.fetchall()
  db.close()
  return error_report_string

pop_articles_string = popular_articles()
pop_authors_string_return = popular_authors()
error_report_string_return = error_report()

print "****Reporting Statistics for News****"

print "\nThe most popular 3 articles of all time are - "
counter = 0
for tuple in pop_articles_string:
  counter = counter + 1
  print 'Article #' ,counter,'is',tuple[0] , 'with', tuple[1], 'views'

print "\nThe most popular authors of all times are - "
counter1 = 0
for tuple in pop_authors_string_return:
  print pop_authors_string_return[counter1][0],'-',pop_authors_string_return[counter1][1],'views'
  counter1 = counter1 + 1

print "\nDays where more than 1 percent of requests lead to errors-"
print error_report_string_return[0][1].strftime('%b %d %Y'),"-",round(error_report_string_return[0][0],2),"%"