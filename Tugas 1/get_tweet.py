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

def case_folding(tweet_word):
    return tweet_word.lower()

def stemming(tweet_word):
    return stemmer.stem(tweet_word)



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

    print(tokenization(tweet))

    # temp["name"] = tweet.user.name
    # temp["tweet"] = tweet.text

    # result_list.append(temp)

# save_to_file(result_list)