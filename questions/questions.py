import nltk
import sys
import os
import math 

FILE_MATCHES = 3
SENTENCE_MATCHES = 3


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    
    
    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)
        print()


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    d = dict()
    for file in os.listdir(directory):
    	path = os.path.join(directory,file)
    	f = open(path,'r',encoding='utf8')
    	d[file] = f.read()
    return d



def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    stopwords = nltk.corpus.stopwords.words("english")
    words = [x for x in nltk.word_tokenize(document.lower()) if x.isalpha() and x not in stopwords]
    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    words = set( word for key in documents.keys() for word in documents[key])
    word_idfs = {word:1 for word in words}
    for word in words:
    	c = 0
    	for doc in documents:
    		if word in documents[doc]:
    			c += 1
    	word_idfs[word] += math.log(len(words)/c)
    return word_idfs



def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idf_values = dict()
    for file in files:
    	c = 0
    	for word in query:
    		if word in idfs:
    			c += (files[file].count(word)/len(files[file])) * idfs[word]

    	tf_idf_values[file] = c
    tf_idf_values = sorted(tf_idf_values, key= lambda k: (-tf_idf_values[k]))
    return tf_idf_values[:n]



def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    idf_values = dict()
    for sentence in sentences:
    	c = 0
    	t = 0
    	exclude = 1
    	if '==' in sentence:
            exclude = 0
    	for word in query:
    		if word in sentences[sentence]:
    			c += idfs[word] * exclude
    			t += 1/len(sentences[sentence])
    	idf_values[sentence] = [c,t]
    idf_values = sorted(idf_values, key=lambda k: (-idf_values[k][0], -idf_values[k][1]))
    return idf_values[:n]



if __name__ == "__main__":
    main()
