def readDocsFromFile(file):

    with open(file , 'r') as f_r:
        lines = f_r.readlines()
        lines =[line.replace("\n","") for line in lines]
    
    idDocs, sentences  = [] , []
    for line in lines:
        name , sentence = line.split("\t")[0] , line.split("\t")[1]
        _, id_doc, id_sent = name.split(".")[0] , name.split(".")[1] , name.split(".")[2]
        idDocs.append([id_doc , id_sent])
        sentences.append(sentence)
    with open("fdfd","w") as f:
        f.write("\n".join(sentences))
    print(idDocs)

file ='data_khm.txt'
readDocsFromFile(file)

def splitListIdDoc(listIdDoc):
    result = [] 
    if len(listIdDoc) == 1:
        return 0
    start = 0
    lenListDoc = len(listIdDoc)
    while start < lenListDoc :
        temp_result = [] 
        current_index = start
        while listIdDoc[current_index][0] == listIdDoc[start][0] : 
            