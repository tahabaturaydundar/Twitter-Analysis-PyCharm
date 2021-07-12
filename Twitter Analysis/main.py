from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
# yukarıdaki kütüphaneler import edildi !


def percentage(part, whole):
    return 100 * float(part)/float(whole)

# twitter api tokenlerı aşağıda tanımlandı !
consumerKey = 'Hg0VQLd3f1CMd8G66nYL1KR4n'
consumerSecret = 'W9EDgrlTDytqMEHyWBWQccvVrhOjSD7Dejt3ytuJlCA2HT6trI'
accessToken = '3166559529-ceLoQIZtOrNzMNn97RQPNYc5ats3RV6cRvtoYKB'
accessTokenSecret = 'tDiHsL4YHIDkM0uGNnditDjS05SfjgJ5kXYeY05g4rt5e'

# twitter api'ye bağlantı kodları -- gerektiği şekilde optimize edildi ! ancak verileri çekmiyor !
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="Turkish").items(noOfSearchTerms)
#cursor methodu Twitter API'deki erişim limitlerinin etrafında dolaşmamızı sağlayan methoddur !

positive = 0
negative = 0
neutral = 0
polarity = 0

# for döngüsü başlangıç !
for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
# for döngüsü bitiş

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + "  Tweets.")
if(polarity == 0):
    print("Nötr")
elif(polarity < 0):
    print("Negatif")
elif(polarity > 0):
    print("Pozitif")


labels = ['Positive [' + str(positive)+ '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative] # boyutlar !
colors = ['yellowgreen', 'gold', 'red'] # renk ayarları !
patches, texts, = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + 'by analyzing ' + str(noOfSearchTerms) + 'Tweets.') #baslık !
plt.axis('equal')
plt.tight_layout()  # grafikler arasındaki boşlukları optimize edebilmek için kullanılan fonksiyondur.
plt.show()  # grafiğin gösterilmesini sağlayan kod !










