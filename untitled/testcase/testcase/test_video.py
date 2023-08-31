"""
===============
    jishubu
    NAME = guxiaoyu
    2020年 月 18日 小时 分
    E-email:18339435211@139.com
================
"""

# import re
# import requests
#
# response =  requests.get('https://vd4.bdstatic.com/mda-jcrx64vi5vct2d2u/sc/mda-jcrx64vi5vct2d2u.mp4?auth_key=1557734214-0-0-d6a29a90222c6caf233e8a2a34c2e37a&bcevod_channel=searchbox_feed&pd=bjh&abtest=all')
# video = response.content         #把文件保存成二进制
# with open(r'C:\Users\jishubu\Desktop\python图片\绿色.mp4','wb') as fw:
#     fw.write(video)           #将文件内容写入该文件
#     fw.flush()               #刷新
#

"""
‘r’：只读。该文件必须已存在。
‘r+’：可读可写。该文件必须已存在，写为追加在文件内容末尾。
‘rb’：表示以二进制方式读取文件。该文件必须已存在。
‘w’：只写。打开即默认创建一个新文件，如果文件已存在，则覆盖写（即文件内原始数据会被新写入的数据清空覆盖）。
‘w+’：写读。打开创建新文件并写入数据，如果文件已存在，则覆盖写。
‘wb’：表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写。
‘a’：追加写。若打开的是已有文件则直接对已有文件操作，若打开文件不存在则创建新文件，只能执行写（追加在后面），不能读。
‘a+’：追加读写。打开文件方式与写入方式和'a'一样，但是可以读。需注意的是你若刚用‘a+’打开一个文件，一般不能直接读取，因为此时光标已经是文件末尾，除非你把光标移动到初始位置或任意非末尾的位置。（可使用seek() 方法解决这个问题，详细请见下文Model 8 示例）
"""
# 爬取视频--失败了
# import re  # 载入模块
# import requests  # 载入模块
#
# new_list = []
# time = 0
# response = requests.get('https://www.ku6.com/index')
# data = response.text
# # print(data)
# url = re.findall('<a class="video-image-warp" target="_blank" href="(.*?)">', data)
# for a in url:  # type:str
#     if a.startswith('/v') or a.startswith('/d'):
#         new_list.append(f'https://www.ku6.com{a}')
#     elif a.startswith('ht'):
#         new_list.append(f"{a.split('垃')[0]}")
# for url_1 in new_list:
#     response_1 = requests.get(url_1)
#     data_1 = response_1.text
#     video = re.findall('<source src="(.*?)" type="video/mp4">', data_1) or re.findall('type: "video/mp4", src: "(.*?)"',
#                                                                                       data_1)
#     video_1 = video[0]
#     x = video_1.split('/')[-1]
#     name = f'{x}.mp4'
#     video_response = requests.get(video_1)
#     video_3 = video_response.content
#     with open(f'C:\Users\jishubu\Desktop\python图片\{name}', 'wb') as fw:
#         fw.write(video_3)
#         fw.flush()
#         time += 1
#         print(f'已经爬取{time}个视频')

# 爬取百家号的段子内容
# import re
# import requests  # 如果没这模块运行CMD pip  install requests
#
# response = requests.get('http://baijiahao.baidu.com/s?id=1598724756013298998&wfr=spider&for=pc')
# data = response.text
# # 按F12选择自己想要的内容所在的位置copy出来
# new_list = re.findall('<span class="bjh-p">(.*?)</span></p><p>', data)  # (.*?)是我们要的内容
#
# for a in new_list:
#     with open(r'C:\Users\jishubu\Desktop\python图片\段子.txt', 'a') as fw:
#         fw.write(a)
#         fw.flush()

#
# import requests
# import json
# import pprint
# import re
#
# def getMusic(song_id):
#     #抓包在media里面找更快，复制音频代码在搜索框里面搜索歌曲信息找到song_linnk，才抓包成果。如果是post请求，可删除cookise从新抓包。
#     # url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery17201201302791909522_1583251981396&songid=242078437&from=web&_=1583251984376'
#     url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid='+song_id
#     response=requests.get(url)
#     pprint.pprint(response.json())
#     data=response.json()
#     # print(data['bitrate']['file_link'])
#     # print(data['songinfo']['title'])
#     filename=data['songinfo']['title']
#     link=data['bitrate']['file_link']
#     res=requests.get(link,stream=True)
#     with open(filename+'.mp3','wb') as music:
#         for sic in res.iter_content(102400):
#             music.write(sic)
#
#
# # URL='http://music.taihe.com/search?key=%E8%96%9B%E4%B9%8B%E8%B0%A6'
# # 要去点歌手获取id,而不是输入薛之谦
# URL='http://music.taihe.com/artist/2517'
# res=requests.get(URL)
# res.encoding=res.apparent_encoding
# print(res)
# html=res.text
# print(html)
# pattern = re.compile('href="/song/(.*?)"',re.S)
# song_ids=re.findall(pattern,html)
# print(song_ids)
# # for song_id in song_ids:
# #     print(song_id)
# #     getMusic(song_id)


page = 26
for page in range(26,64):
    page += 1
    print(page)
