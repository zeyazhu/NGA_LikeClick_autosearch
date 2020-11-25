# NGA_LikeClick_autosearch
 A python tool for listing how many likes u have on NGA.com

# 项目说明
nga最近终于喜迎zeg开放赞数查询窗口（做中国的reddit草），靠
```https://bbs.nga.cn/nuke.php?__lib=ucp&__act=get&lite=js&__inchst=UTF8&username=```
这句话即可查到jason化的数据信息，本项目基于此的一个简单小脚本，直出你的赞数数据。同时我在自动测试里.txt文件放了比如水区猴区的版主列表，可以直接查看谁最丢人


# 使用简介
整个项目我封装在nga.py里了，使用getLike(你的ID）调用即可出结果。
在测试脚本.ipynb里，使用jupyter notebook打开哦。
```python
%run nga.py #载入查询接口
import requests
import re
import bs4
with open("dotaWD.txt", "r",encoding='utf-8') as f:  # 多个用户id储存在txt中直接读取
#不加encoding='utf-8会有编码bug，一定要加 encoding这句话
    data = f.readlines()  # 读取文件
    #print(data)
    for l in data:
        l = l.strip("\n")
        name=''.join(l)
        #print(name)
        #print('版主名:%s,赞数是：%s'%(l,getLike(l)))
        getLike(name)
    print('end')
```
嘛，未来考虑下再写个脚本抓取不同版块的版主id做个数据库好了。真正的赞少丢人大会就可以开始辣
