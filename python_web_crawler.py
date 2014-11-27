# -*- coding: UTF-8 -*-
import urllib
import re
import datetime
import urlparse
from bs4 import BeautifulSoup
from urlparse import urljoin

t = datetime.datetime.now() 
i = 1

for num in range(626,664):
    starturl = "http://125.218.212.143:81/rmrb/thread.php?fid="+str(num) 
    url = "http://125.218.212.143:81/rmrb/" 
    urls = [starturl] 
    visited = [starturl] 

    while len(urls)>0:
        try:
            content = urllib.urlopen(urls[0]).read()
        except:
            print urls[0]
            
        soup = BeautifulSoup(content)
        urls.pop(0)
        for each_div in soup.findAll('div',{'class':'pages'}):
            for a in each_div:
                newurl  = urlparse.urljoin(url,a.get('href'))
                if newurl not in visited and newurl != url:
                    urls.append(newurl) 
                    visited.append(newurl)
                    htmltext = urllib.urlopen("http://125.218.212.143:81/rmrb/"+str(a.get('href')))
                    soup1 = BeautifulSoup(htmltext)
                    for each_div in soup1.findAll('h3'):
                        for a in each_div:
                            contentpage = urllib.urlopen("http://125.218.212.143:81/rmrb/"+str(a.get('href')))
                            s = contentpage.read()
                            regex = '<div class="tpc_content" id="read_tpc">(.+?)</div>'
                            pattern = re.compile(regex)
                            content = re.findall(pattern,s)
                            try:
                                content = content[0].decode('gbk').encode('utf8')
                                print content + "\n"
                                r = open("C:\Users\Wong\Desktop\Project\web\web"+str(i)+".txt","w")
                                r.write(content)
                                r.close()  
                            except:
                                contentpage = urllib.urlopen("http://125.218.212.143:81/rmrb/"+str(a.get('href')))
                                s = contentpage.read() 
                                regex = '<div class="tpc_content" id="read_tpc">(.+?)</div>'
                                pattern = re.compile(regex)
                                content = re.findall(pattern,s)
                                content = content[0].decode('gbk').encode('utf8')
                                print content + "\n"
                                r = open("C:\Users\Wong\Desktop\Project\web\web"+str(i)+".txt","w")
                                r.write(content)
                                r.close()  
                                pass
                            i+=1


k = datetime.datetime.now() - t
print k
