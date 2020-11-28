def readDocsFromFile(file , language):

    with open(file+"_"+language+".txt" , 'r') as f_r:
        lines = f_r.readlines()
        lines =[line.replace("\n","") for line in lines]
    
    idDocs, sentences  = [] , []
    for line in lines:
        name , sentence = line.split("\t")[0] , line.split("\t")[1]
        _, id_doc, id_sent = name.split(".")[0] , name.split(".")[1] , name.split(".")[2]
        idDocs.append([id_doc , id_sent])
        sentences.append(sentence)
    with open("sentences_"+language+".txt","w") as f:
        f.write("\n".join(sentences))
    print(splitListIdDoc(idDocs))
    # print(sentences)

def splitListIdDoc(listIdDoc):
    result = {}
    if len(listIdDoc) == 1:
        return 0
    start = 0
    lenListDoc = len(listIdDoc)
    while start < lenListDoc :
        temp_result = [start] 
        current_index = start + 1
        while  current_index < lenListDoc  and listIdDoc[current_index][0] == listIdDoc[start][0] : 
            temp_result.append(current_index)
            current_index += 1 
        
        result[listIdDoc[start][0]] = temp_result
        start = current_index
    return result

# l= [ [1 , 1],[1 ,2],[2 , 1],[3,1],[3,2],[4,3],[4,1]]
# print(splitListIdDoc(l))
readDocsFromFile('data','vi')