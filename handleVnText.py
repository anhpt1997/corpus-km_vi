import string
import re
import unicodedata

def norm_text(text):
    text = unicodedata.normalize('NFC', text)
    text = re.sub(r"òa", "oà", text)
    text = re.sub(r"óa", "oá", text)
    text = re.sub(r"ỏa", "oả", text)
    text = re.sub(r"õa", "oã", text)
    text = re.sub(r"ọa", "oạ", text)
    text = re.sub(r"òe", "oè", text)
    text = re.sub(r"óe", "oé", text)
    text = re.sub(r"ỏe", "oẻ", text)
    text = re.sub(r"õe", "oẽ", text)
    text = re.sub(r"ọe", "oẹ", text)
    text = re.sub(r"ùy", "uỳ", text)
    text = re.sub(r"úy", "uý", text)
    text = re.sub(r"ủy", "uỷ", text)
    text = re.sub(r"ũy", "uỹ", text)
    text = re.sub(r"ụy", "uỵ", text)
    text = re.sub(r"Ủy", "Uỷ", text)
    return text


# Storing the sets of punctuation in variable result
punc = set(string.punctuation)
list_punctuations_out = ['”', '”', "›", "“", '"' ,'...', '…']
for e_punc in list_punctuations_out:
    punc.add(e_punc)

with open('stop_word.txt') as f:
	stopWords = f.readlines()
	stopWords = [norm_text(word.replace("\n","")) for word in stopWords]

# print(stopWords)

def removeMultiSpaceToSpace(string):
	return re.sub(' +', ' ', string)

def removeStopword(doc):
	tokens = doc.split()
	return " ".join([word for word in tokens if word not in stopWords])

def handlePunc(string):
	result = ""
	for c in string:
		if c not in punc:
			result += c
		else:
			result += " "
	return result

def processDoc(doc):
	doc = doc.lower()
	doc = handlePunc(doc)
	doc = norm_text(doc)
	doc = removeStopword(doc)
	doc = removeMultiSpaceToSpace(doc)
	return doc 

doc = """ Tiếp đó, Thượng nghị sĩ Kerry O'Brien (Đảng Lao động, bang Tasmania) chỉ trích việc thực hiện phòng thủ bờ biển của Chính phủ, và nhấn mạnh sự nguy hiểm khi bỏ qua con tàu trong mười bảy ngày, nói rằng "nó đã và có thể vẫn còn tạo ra các rủi ro không rõ ràng về môi trường và kiểm dịch" và rằng tàu Jian Seng "đã bị từ chối cập cảng Weipa. .Nó có thể đã vận chuyển bất cứ thứ gì."
"""
doc1 = """Thượng nghị sĩ Kerry O'Brien (Đảng Công nhân Tasmania) sau đó đã chỉ trích việc chính phủ bảo vệ bờ biển, nhấn mạnh nguy cơ bỏ bê con tàu trong 17 ngày, nói rằng "nó làm tăng rủi ro về môi trường và châm biếm" và Jian. Seng: "Không được phép vào cảng Wei Pa ... thực sự không thể hỏi."
"""
print(doc)
doc1 = processDoc(doc)
print(doc1)