from collections import Counter, defaultdict
import string
from search_engine import SearchEngine
from weather_predictor import WeatherPredictor
import nltk
from nltk.stem import WordNetLemmatizer

class MtPyDataWorldsService:

    wordnet_lemmatizer = WordNetLemmatizer()
    stopwords = set(w.rstrip() for w in open('resources/stopwords.txt'))

    def my_tokenizer(self,s):
        s = s.lower()
        tokens = nltk.tokenize.word_tokenize(s)
        tokens = [t for t in tokens if len(t) > 2]
        tokens = [self.wordnet_lemmatizer.lemmatize(t) for t in tokens]
        tokens = [t for t in tokens if t not in self.stopwords]
        return tokens
    
    
    def runSearchEngine(self, q):
        se = SearchEngine()
        return se.search(q)
    
    def runWeatherPredictor(self, m):
        we = WeatherPredictor()
        return we.runANNCatModel()
    
    def gospel_analysis(self):
        all_lines =[]
        for line in open('resources/gospel.txt', encoding="UTF-8"):
            line = line.translate(str.maketrans('', '', string.punctuation))
            line_splt = line.split("\t")
            all_lines.append(line_splt[1])

        word_counts = {}    

        all_str = ''.join(all_lines)    
        tokens = self.my_tokenizer(all_str)
        for token in tokens:
            if not(token in word_counts):
                word_counts[token] = 0
            word_counts[token] = word_counts[token] + 1    

        list_words = []
        for token in word_counts:
            list_words.append({"token":token, "cnt":word_counts[token]})

        list_words.sort(key=lambda x: x['cnt'], reverse=True)
        ret = {"word_counts":list_words}       

        bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
    
        bigram_counts = Counter(bigrams)
        
        most_common = bigram_counts.most_common(50)
        
        list_bigrams = []
        for bigram, count in most_common:
            list_bigrams.append({"token":' '.join(bigram), "cnt":count})
        ret["list_bigrams"] = list_bigrams      

        return ret

        






    

    




    
    
       