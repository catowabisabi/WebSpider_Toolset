import urllib.request

url_page = 'http://www.baidu.com'

# 這一句是下載全個網頁
urllib.request.urlretrieve(url_page, 'baidu.html') #兩個參數, 第一個是url, 第二個是文件的名字

url_image = 'https://pm1.narvii.com/6469/c39c26b17e4729ae7829d66f8e0ee1f65f8f5e6d_hq.jpg'
urllib.request.urlretrieve(url = url_image, filename = 'lida.jpg')

url_video = 'https://vd2.bdstatic.com/mda-nfc6xm6yv1dv4y45/720p/h264/1655098183363731536/mda-nfc6xm6yv1dv4y45.mp4?v_from_s=hkapp-haokan-hna&auth_key=1655244428-0-0-a76e4dd02d5643b3f76a3afac92e58b2&bcevod_channel=searchbox_feed&cd=0&pd=1&pt=3&logid=2228527056&vid=16772523523884082699&abtest=102599_2-102777_6-102784_1-102836_1-17451_1-3000232_1&klogid=2228527056'

urllib.request.urlretrieve(url_video, 'lida.mp4')