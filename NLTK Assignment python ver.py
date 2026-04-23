import nltk
import os
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.util import ngrams

# 1. Essential Downloads for NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

# 2. File Setup based on your specific order
# Text_1: Lovecraft style, Text_2: Tolkien style, Text_3: Martin style, Text_4: Fantasy Original
files = {
    "Text_1": "RJ_Lovecraft.txt",
    "Text_2": "RJ_Tolkein.txt",
    "Text_3": "RJ_Martin.txt",
    "Text_4": "Martin.txt"
}

def process_text(file_name):
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as f:
        return f.read()

# 3. Tokenization, Stemming, and Lemmatization
def get_analysis(text_content):
    # Tokenize and clean (remove stop words and non-alphabetic characters)
    stop_words = set(stopwords.words('english'))
    tokens = [w.lower() for w in word_tokenize(text_content) if w.isalpha() and w.lower() not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stems = [stemmer.stem(t) for t in tokens]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    
    return Counter(lemmas).most_common(20)

# 4. Named Entity Recognition
def count_entities(text_content):
    tokens = word_tokenize(text_content)
    tags = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tags)
    return sum(1 for leaf in tree if hasattr(leaf, 'label'))

# 5. N-Gram Analysis (Trigrams)
def get_trigrams(text_content):
    tokens = [w.lower() for w in word_tokenize(text_content) if w.isalpha()]
    trigs = list(ngrams(tokens, 3))
    return Counter(trigs).most_common(5)

# Execution Loop
for label, filename in files.items():
    content = process_text(filename)
    if content:
        print(f"--- {label} ({filename}) ---")
        print(f"Top 20 Lemmas: {get_analysis(content)}")
        print(f"Named Entities: {count_entities(content)}")
        print(f"Top Trigrams: {get_trigrams(content)}\n")