# Python-NLTK-Story-Text-Analysis-

The purpose of this project is to perform a comparative natural language processing (NLP) analysis on four distinct unstructured text files. By using the Natural Language Toolkit (NLTK), the project demonstrates how to programmatically derive meaning, identify subjects, and recognize authorial patterns across different writing styles.

*Class Design and Implementation*

The implementation follows a functional programming approach in Python, utilizing specific modules from NLTK to handle the complexities of human language.

*1. Data Pre-processing Method*

Tokenization: Splits the raw text into individual words or "tokens" to make the data digestible for the machine.

Stemming: Uses the PorterStemmer to chop words down to their root form (e.g., "feuding" becomes "feud").

Lemmatization: Uses the WordNetLemmatizer to find the actual dictionary root of a word, which is more linguistically accurate than stemming.

Filtering: The method removes "stopwords" (common words like "the" or "and") and non-alphabetic characters to focus on meaningful content.

*2. Named Entity Recognition (NER)*

MethodFunction: This method tags parts of speech and then "chunks" them to identify proper nouns such as people, places, and organizations.

Usage: Identifying high concentrations of entities like "Verona," "Romeo," or "House Eldermore" helps the program determine the geographical and character-based subject of the text.

*3. N-Gram Analysis*

MethodFunction: This method generates "trigrams" ($n=3$), which are sequences of three consecutive words.

Purpose: Trigrams are used to identify unique "fingerprints" in an author's writing style to determine if the author of the first three texts wrote the fourth.

*Class Attributes and Logic*

files: A dictionary attribute mapping the text labels (Text_1 through Text_4) to their respective filenames to ensure the analysis follows the required order.

nltk.download: These attributes are necessary to fetch the linguistic databases (like the Maxent NE Chunker or WordNet) required for the code to run in a fresh environment.

Counter: Used to track the frequency of lemmas and n-grams to provide the "top 20" and "top 5" lists required by the assignment.

*Limitations*

Stopword Dependency: The accuracy of the "Most Common Tokens" is dependent on the NLTK stopword list; some context-specific words may still appear if they aren't in the default list.

NER Accuracy: Named Entity Recognition can occasionally misidentify capitalized words at the start of sentences as proper nouns, which may slightly inflate the entity count.

N-Gram Context: Trigrams provide a stylistic snapshot but do not account for overall plot structure, meaning they are best used alongside lemmatization for author identification.
