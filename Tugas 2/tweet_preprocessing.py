import twitter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def save_to_file(list):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i in range(len(list)):
            f.write(str((i+1)) + "\n") 
            f.write("account name : ") 
            f.write("%s\n" % list[i]["name"])
            f.write("tweet :\n")
            f.write("%s\n" % list[i]["tweet"])
            f.write("\n")
            f.write("Stemmed words :\n")
            for j in range(len(list[i]["stemmed_words_arr"])):
                f.write("%s => %s\n" % (list[i]["tweet_words_arr"][j], list[i]["stemmed_words_arr"][j]))

            f.write("\n")

def generate_keywords_string():
    keywords = [
        'anjing',
        'babi',
        'kampret',
        'tolol'
        'jancok',
        'bangke',
        'bacot',
        'goblok',
        'cebong',
        'unta',
    ]

    result = "q="
    for keyword in keywords:
        result += keyword
        result += "%20OR%20"

    result = result[:len(result)-5]
    result += "&src=typd&count=100"
    return result

# split sentence to words
def tokenization(tweet):
    words_array = tweet.text.split(' ')
    return words_array

def case_folding(tweet_words):
    temp = []

    for word in tweet_words:
        temp.append(word.lower())
    
    return temp

def stemming(tweet_words):
    temp = []

    for word in tweet_words:
        temp.append(stemmer.stem(word))
    
    return temp


CONSUMER_KEY='ZTcA1bjkWRgQkfPjzDeeIo5YH'
CONSUMER_SECRET='Co3MqpnTpA62GtN6Sl6WkPxswL0Oyp74bksDL5TUIHtmwNPu0t'
ACCESS_TOKEN_KEY='2470645682-qcPQjWZj2ER54FQDGa8pwSSxOpJmGeaT9imaaq3'
ACCESS_TOKEN_SECRET='SwzQS3BwmjXE4hGFi4UK4p9Xqd7J2xcRQI8YMOXm2mS7T'

factory = StemmerFactory()
stemmer = factory.create_stemmer()

twitter_api = twitter.Api(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token_key = ACCESS_TOKEN_KEY, access_token_secret = ACCESS_TOKEN_SECRET)

tweet_results = twitter_api.GetSearch(raw_query=generate_keywords_string())

result_list = []

for tweet in tweet_results:
    temp = {}

    tweet_words_arr = tokenization(tweet)
    tweet_words_arr = case_folding(tweet_words_arr)

    tweet_stemmed_words_arr = stemming(tweet_words_arr)

    temp["name"] = tweet.user.name
    temp["tweet"] = tweet.text
    temp["stemmed_words_arr"] = tweet_stemmed_words_arr
    temp["tweet_words_arr"] = tweet_words_arr

    result_list.append(temp)

save_to_file(result_list)