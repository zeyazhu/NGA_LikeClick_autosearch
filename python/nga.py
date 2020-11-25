#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import bs4

#NGA_name= 'fanrk' #可更改
global like_click
def getLike(name):
    import requests
    import re
    import bs4
    localurl='https://bbs.nga.cn/nuke.php?__lib=ucp&__act=get&lite=js&__inchst=UTF8&username='
    #抓取页码内容，返回响应对象
    url = localurl+name
    response = requests.get(url)
    global like_click
 

    #查看响应状态码
    
    status_code = response.status_code

 

    #使用BeautifulSoup解析代码,并锁定页码指定标签内容

    content = bs4.BeautifulSoup(response.content,'lxml')

    element = content.find_all(id='username')

    soup=content


    #print(status_code)

    #print(element)
    #print(soup.text)
    urlget=soup.text             
    #for ll in urlget:

    ll = soup.text.strip("\n").strip("window.script_muti_get_var_store=").strip("{}")

        #print(ll)
    ss = ll#.strip("window.script_muti_get_var_store=").strip("{}").split(",")
    asd=''.join(ss)
    asd= asd.replace(',"',';').replace('"data"','').replace('"','').replace('type:8;',';like')
    asd=asd.split(";")
    #print(asd)
    aaa=0
    #like_click ="null"
    for a in asd:
        i=0
    #x= a.replace('"','')
    #print(a)
        if "likedata" in a:
            like_click = re.findall("\d",a)
#a=''.join(s)
            aaa=''.join(like_click)
            #print(aaa)
    print('uid:%s ,likes：%s'%(name,aaa))
            #return like_click
    #print(aaa)
#print(getLike(NGA_name))

