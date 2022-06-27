# start project
code = 'scrapy startproject scrapy_baidu_091' #(最後的是項目名字)
# 不可以使用數字或中文開頭

# 進入spiders文件夾
code = 'cd scrapy_baidu_091.py\scrapy_baidu_091\spiders'

# 建立spider文件
code = 'scrapy genspider 虫仔文件名 要爬既網'
code = 'scrapy genspider baidu www.baidu.com'

# 運行爬虫, 加入虫的名字
code = 'scrapy crawl baidu'

# 修改君子協定 setting.py
ROBOTSTXT_OBEY = True #改為False
