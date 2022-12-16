from module_inverted_index import remove_punc_and_lower_case

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# list of documents
doc_list = []

# reading the docs
doc1 = open(r'C:\Users\asus\Desktop\mabani\inverted_index_proj\doc1.txt', encoding='utf8')
doc1 = doc1.read()


doc2 = open(r'C:\Users\asus\Desktop\mabani\inverted_index_proj\doc2.txt', encoding='utf8')
doc2 = doc2.read()

# add the docs to the doc_list
doc_list.append(doc1)
doc_list.append(doc2)

# print(doc_list)

# list of documents without punctuation in lowercase
doc_list_no_punc = []

# remove punctuation from all docs and put them in lower case format and append to doc_list_no_punc
for document in doc_list:
    doc_list_no_punc.append(remove_punc_and_lower_case(document))

print(doc_list_no_punc)

# the list contains the tokenized words without stopwords
tokenized_docs_list_no_sw = []

for document in doc_list_no_punc:
    #first tokenize the word
    text_tokens = word_tokenize(document)
    #removes the stopwords
    tokens_without_sw = [
    word for word in text_tokens if not word in stopwords.words()]
    #elimiate the repeated words and append it
    tokenized_docs_list_no_sw.append(set(tokens_without_sw))


# print(tokenized_docs_list_no_sw)

inverted_index_dict = {}


for doc in tokenized_docs_list_no_sw:
    for word in doc:
        if word  not in inverted_index_dict:
            posting_list = []
            posting_list.append(tokenized_docs_list_no_sw.index(doc)+1)

            inverted_index_dict[word] = posting_list
        else:
            value = inverted_index_dict[word]
            value.append(tokenized_docs_list_no_sw.index(doc)+1)
            inverted_index_dict[word] = value


# sorts the inverted index
inverted_index_dict = {key: value for key, value in sorted(inverted_index_dict.items())}
print(inverted_index_dict["terms"])