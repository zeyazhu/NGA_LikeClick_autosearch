{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import re\n",
    "import bs4\n",
    "\n",
    "NGA_name= 'fanrk' #可更改\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getLike(name):\n",
    "    localurl='https://bbs.nga.cn/nuke.php?__lib=ucp&__act=get&lite=js&__inchst=UTF8&username='\n",
    "    #抓取页码内容，返回响应对象\n",
    "    url = localurl+name\n",
    "    response = requests.get(url)\n",
    "\n",
    " \n",
    "\n",
    "    #查看响应状态码\n",
    "    \n",
    "    status_code = response.status_code\n",
    "\n",
    " \n",
    "\n",
    "    #使用BeautifulSoup解析代码,并锁定页码指定标签内容\n",
    "\n",
    "    content = bs4.BeautifulSoup(response.content,'lxml')\n",
    "\n",
    "    element = content.find_all(id='username')\n",
    "\n",
    "    soup=content\n",
    "\n",
    "\n",
    "    #print(status_code)\n",
    "\n",
    "    #print(element)\n",
    "    #print(soup.text)\n",
    "    urlget=soup.text.split()             \n",
    "    for ll in urlget:\n",
    "\n",
    "        ll = ll.strip(\"\\n\")\n",
    "\n",
    "        #print(ll)\n",
    "    ss = ll.strip(\"window.script_muti_get_var_store=\").strip(\"{}\").split(\",\")\n",
    "#print(ss)\n",
    "    for aa in ss:\n",
    "        xx= aa.replace('\"','')\n",
    "    #print(xx)\n",
    "        if \"data\" in xx:\n",
    "            like_click = re.findall(\"\\d\",xx)\n",
    "    #a=''.join(s)\n",
    "    like_click=''.join(like_click)\n",
    "    #print(like_click)\n",
    "    return like_click"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "107\n"
     ]
    }
   ],
   "source": [
    "print(getLike(NGA_name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
