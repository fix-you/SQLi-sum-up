# SQLi-sum-up
这个仓库是自己学习工程中用来复盘的，因为切换输入法不方便，基本采用英语 来写，看官朋友们遇到不清楚的单词请自行查阅，感谢观看！ 另外，为了让自己方便观看，将采用倒序编写，最新的内容会在最前面 ```
# SQL injection（注入）
```
本篇文章是自己学习工程中用来复盘的，因为切换输入法不方便，基本采用英语
来写，看官朋友们遇到不清楚的单词请自行查阅，感谢观看！
另外，为了让自己方便观看，将采用倒序编写，最新的内容会在最前面
```
## Practice

### DVWA SQLi
> http://43.247.91.228:81/login.php
1. Vulnerability: SQL Injection
- low 
	omited
- middle
	1. get the number of columns, whose payload is:
		> 1 order by 2--
	2. find out  by using UNION SELECT 1,2,3,4...n, 
		and  the payload_id is:
		> 1 UNION SELECT 1,2&Submit=Submit#
		
	3. Fetch data, considering the structure of a classic Mysql_DB:
	![https://henry-wp-backup.oss-cn-shenzhen.aliyuncs.com/Wordpress/WEB_PENETRATION/SQL_STRUCTUTRE.png?Expires=1558839911&OSSAccessKeyId=TMP.AgEnMPRvFnZWH2pt2zL2a-LiQDzkLXjGUB67M9WdK00USBLurBmvAJr4sWVZADAtAhUA2TeC9aA7vq7Oczv1vzoAkWWIxn4CFFK7JRKD4Po90RmVs7St2MA4mMga&Signature=7aSOU9AyG7dglRY4aY1wpaq6mJI%3D]()
	Basic form of payloads should be like 
	> ?id=1/**/union/**/SELECT/**/table_schema,table_name/**/FROM/**/information_schema.tables/**/limit/**/2,3
	
	by using the tricks below you can gradually form the entire TABLE_NAME and COLUMN_NAME
	*** Addtionally, i should emphasize that '/**/' is a sort of replacements of space(' '), which sometimes is able to bypass WAF ***
	
	4. In the 3rd part, it's quite dull and of *LOW efficiency* to fetch data little by little, so i decide to make it AUTOMATIC:
- Python:
before using, the injection param should be put at the TAIL of url, which is 
from *?id=1%20UNION%20SELECT%201,user()&Submit=Submit#*  to  *?Submit=Submit&id=1%20UNION%20SELECT%201,user()* 

```
[https://github.com/fix-you/SQLi-sum-up/blob/master/Sqli_auto_fetch_via_union.py](点击查看py代码0.0)
```
效果如下：
![https://henry-wp-backup.oss-cn-shenzhen.aliyuncs.com/Wordpress/WEB_PENETRATION/sqli_fuzz/auto_fuzzing.png?Expires=1558849553&OSSAccessKeyId=TMP.AgEnMPRvFnZWH2pt2zL2a-LiQDzkLXjGUB67M9WdK00USBLurBmvAJr4sWVZADAtAhUA2TeC9aA7vq7Oczv1vzoAkWWIxn4CFFK7JRKD4Po90RmVs7St2MA4mMga&Signature=9tJs2gYLx%2BsVnV06TaSQk6bgSfI%3D]()


- 编程心得
	1. python regex
		- findall(r[pattern],String) //extract from string
		- match(r[pattern],String) //match string
	

	
## Reasons of sqli
1. user-provided params which directly connect to db *WITHOUT* filter
	> $_GET
	> $_POST
	> $_REQUEST	
	
2. $result should be seen outside
	> echo($query)
	> echo...


	
