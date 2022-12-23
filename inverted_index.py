from module_inverted_index import remove_punc_and_lower_case
import pathlib
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# takes the current folder path
current_path = str(pathlib.Path().cwd())


# list of documents
doc_list = []

doc1_path = current_path + "\\" +"doc1.txt"

# reading the docs
doc1 = open(doc1_path, encoding='utf8')
doc1 = doc1.read()


doc2_path = current_path + "\\" +"doc2.txt"

doc2 = open(doc2_path, encoding='utf8')
doc2 = doc2.read()

# add the docs to the doc_list
doc_list.append(doc1)
doc_list.append(doc2)


# list of documents without punctuation in lowercase
doc_list_no_punc = []

# remove punctuation from all docs and put them in lower case format and append to doc_list_no_punc
for document in doc_list:
    doc_list_no_punc.append(remove_punc_and_lower_case(document))


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



inverted_index_dict = {}

# iterates over the docs
for doc in tokenized_docs_list_no_sw:
    # iterates over the words in the doc
    for word in doc:
        # if the word is not in the dic it will be added to the dic as a key
        # then the value will be the number of the doc
        if word  not in inverted_index_dict:
            posting_list = []
            posting_list.append(tokenized_docs_list_no_sw.index(doc)+1)

            inverted_index_dict[word] = posting_list
        # if the word is already there then the number of the doc will be appended to the values of that word
        else:
            value = inverted_index_dict[word]
            value.append(tokenized_docs_list_no_sw.index(doc)+1)
            inverted_index_dict[word] = value


# sorts the inverted index by alphabet
inverted_index_dict = {key: value for key, value in sorted(inverted_index_dict.items())}

print(inverted_index_dict)

num = 90

while(num !=0):
    print("""
    0)exit \n
    1) search for a word
    """)

    num = int(input(" choose an option:"))

    if num == 1:
        input_word = str(input("enter a word:")).lower().strip()

        if input_word in inverted_index_dict:
            print("the enterd word was found in docs with the following number(s):")
            print(inverted_index_dict[input_word])
        else:
            print('no result found')
