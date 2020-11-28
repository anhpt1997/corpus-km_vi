from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import rouge


def get_cosine_sim(*strs): 
	vectors = [t for t in get_vectors(*strs)]
	return cosine_similarity(vectors)
	
def get_vectors(*strs):
	text = [t for t in strs]
	vectorizer = CountVectorizer(text)
	vectorizer.fit(text)
	return vectorizer.transform(text).toarray()

def jaccard_similarity(list1, list2):
	s1 = set(list1)
	s2 = set(list2)
	return float(len(s1.intersection(s2)) / len(s1.union(s2)))

def jaccardSimPairDoc(doc1 , doc2):
	list1 = doc1.split()
	list2= doc2.split()
	return jaccard_similarity(list1 , list2)

def compute_rouge_document(string1 , string2):
	evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l'],
						   max_n=2,
						   limit_length=True,
						   length_limit=1000)
	scores = evaluator.get_scores(string1, string2)
	return scores

# string1 = 'tuan anh'
# string2 = 'tuan anh phan'
# l = [string1 , string2]
# print(get_cosine_sim(string1, string2))
print(compute_rouge_document(string1 , string2)['rouge-1'])