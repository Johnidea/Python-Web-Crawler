<center>Information Retrieval</center>

<center><h1>Python Web Crawler</h1></center>

First, you need to determine the starting URL for the program. The out-most for loop will go through all the assigned period. The while loop within it will crawl all the subpage link of a month and append the new URL to the urls and the visited list. New pages will be opened according to those two lists and output a href link. Then, the program will use that href link to open all the news pages and crawl the contents. As the content is encoded with gbk, the program will have to decode it first and then encode it with utf8 (otherwise the content will be unreadable). Finally, the program will write the content to the txt file.

<center><h1>Chinese Word Count</h1></center>

Jieba is an extremely useful and powerful library to divide sentences into phrases or words. First, the program will read the news file and remove the <br /> tag. Then, the program will divide the news into meaningful Chinese words and put it into the worddict dictionary. If the word is already in the dictionary, the value (occurrences) of it will be plus one. 
After that, the program will use the built-in sorting method which is timsort to sort the Chinese words according to their occurrences. Finally, the program will write the results to the text file.

<center><h1>News Headline Extraction</h1></center>

First, the program retrieve the first sentence of the contents as it can summarize the contents of news in most cases. After that, the program weighted the rest of the sentences by who, when, where and what keywords. After counting the value of those keywords, the program then divided it with the length of the sentence. 
	After the calculation, the program used the timsort to sort the sentence value. The final headline has two parts. The first part is the first sentence and the second part will be the highest score sentence.

<center><h1>Retrieval of related (most similar) news</h1></center>

In this section, the programme used the cosine similarity to find the most similar news.
There are two loops in the program. They are used to loop 50 and 13000 news respectively. The text_to_vector function is used to calculate the number of occurrence of a word and store it on the dictionary as a vector. Then, get_cosine function will calculate these two vectors and return a cosine value. After that, the program used the python built-in sort, which is the timsort to sort the cosine value and write the highest five cosine value news to a file.
