from lxml import etree

# xpath helper ctrl + shift + x open xpath helper on chrome


#如果是本地文件, 用etree.parse
tree = etree.parse('17_sample.html')

#如果是本地文件, 用etree.html
#tree = etree.HTML(content)

print(tree)

li_list = tree.xpath('//li/text()')


# 查找所有有ID的LI
li_list = tree.xpath('//li[@id]/text()')


# 查找所有有ID的LI = li1 引號係一大一細一大一細咁
li_list = tree.xpath('//li[@id = "li1"]/text()')

# 查找所有有ID的LI = li1 查佢既class
li_list = tree.xpath('//li[@id = "li1"]/@class')
# 會check到呢個野個class 係c1


#li 入邊id 包括L
li_list = tree.xpath('//li[contains(@id, "l")]/text()')

#li 入邊id 由L開始
li_list = tree.xpath('//li[starts-with(@id, "l")]/text()')

# id 為l1 and class 為c1
li_list = tree.xpath('//li[@id ="li1" and @class = "c1"]/text()')

# 
li_list = tree.xpath('//ul/li [@id = "li1"]/text() | //ul/li [@class = "class1"]/text()')



print (li_list)



