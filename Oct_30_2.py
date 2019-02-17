filename='UKeconomic.txt'
try:
    with open(filename) as f:
        contents=f.read()
except FileNotFoundError :
   # msg = filename+' does not exist'
   # print(msg)
    pass
else:
    #计算多少文件包含单词
    #words=contents.split()
    #num_words=len(words)
    num_words=contents.count('the')
    print(filename+' has about '+str(num_words)+' words')