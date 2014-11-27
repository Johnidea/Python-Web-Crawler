# -*- coding: UTF-8 -*-
import jieba
import datetime
import jieba.posseg as pseg
t = datetime.datetime.now()

    


with open ("C:\Users\Wong\Desktop\Project\web\webnews10"+".txt", "r") as content:
    data = content.read().replace('<br />','')
    data = unicode(data,'utf8')
    words = pseg.cut(data)
    worddict = {}
    
for w in words:
   if w.word not in worddict and len(w.word) > 1:
         worddict[w.word] = 1
   elif w.word in worddict :
         worddict[w.word] += 1

   
    
a = sorted(worddict.items(),key=lambda(k,v):(v,k),reverse=True)

d = 1
for word in a:
        word =  str(word).replace('(','').replace(')','')
        word = word.encode('utf8')
        if d < 51:
            v = str(d)+", "+ word + "\n"
            r = open("C:\Users\Wong\Desktop\Job\Information Retrieval\Project2\word50"+".txt","a")
            r.write(v)
        else:
            break
        d+= 1


k = datetime.datetime.now() - t
print k
