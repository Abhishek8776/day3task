ls=["Lorem ipsum, dolor sit amet consectetur adipisicing elit. Adipisci architecto accusamus provident esse corporis commodi enim excepturi, amet rem deleniti minima eius dolor ipsa, molestias veniam possimus totam consequuntur maxime consequatur"]
count={}
for sentance in ls:
    for word in sentance.split():
        if word not in count:
            count[word]=1
        else:
            count[word]=count[word]+1
unique=sentance.split()
for word in unique:
    print(word,count[word])
# print(word)
# for i in range(len(word)):
#     count=0
#     for j in range(len(word)):
#         if i != j and word[i] == word[j]:
#             count=count+1
#     print("conunt of word",word[i],"is :",count)
# # my_set = {"a","b",}
# print(my_set)