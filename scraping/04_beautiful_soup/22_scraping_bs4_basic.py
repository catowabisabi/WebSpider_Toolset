from bs4 import BeautifulSoup as bs

# 解析本地文件

# 用呢一句可以拎晒成個網頁既內容, 原碼
soup = bs(open('22_sample.html', encoding = 'utf-8'), 'lxml')

# 拿第一個符合條件的數據
content_a1 = soup.a
#print (content_a1)

# 拿標簽是什麼和他的值
content_a2 = soup.a.attrs
#print (content_a2)

#bs4的三個方法
# find #拿第一個a
#print (soup.find('a'))
# 用title的值去找
#print (soup.find('a', title = "a2"))

# 用class要咁去用 class加底線 class_
# print (soup.find('li', class_ = "c6"))

# find_all, 會return 一個list
# print (soup.find_all('a'))

# 如加個細[] 先可以拎多過一個關建字
# print (soup.find_all(['a','span']))

#print (soup.find_all('li', limit =3))

# select
#print (soup.select('a'))

#class
#print (soup.select('.c6'))

#id
#print (soup.select('#li1'))

# 所有在li中有包含id的
#print(soup.select('li[id]'))

# 所有在li中id為li2
#print(soup.select('li[id="li2"]'))


# 所有在li中id為li2 用空格
#print(soup.select('div li'))

# 一層一層落
#print(soup.select('div>ul>li'))

# 找到a 和li 所有的
#print (soup.select('a,li'))

#obj = soup.select('#d1')[0]
#print (obj.string) # 如果裏邊有仲其他標簽, 會拎唔到

#print (obj.get_text())

# 會標簽的名字
obj = soup.select('#p1')[0]
#print (obj.name)

# 
print(obj.attrs)

# 拿class
obj = soup.select('#p1')[0]
print (obj.attrs.get('class'))
print (obj.get('class'))
print (obj['class'])