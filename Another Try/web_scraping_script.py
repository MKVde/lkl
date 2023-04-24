import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

project_name = web_scraping_script
url = 'https://www.amazon.com/iPhone-13-128GB-Midnight-Unlocked/dp/B0BGQKY8S9/ref=sr_1_4?crid=2TU4BPIX0YEK9&keywords=iphone+13&qid=1682283902&sprefix=iphone+13+%2Caps%2C287&sr=8-4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

reviews = soup.find_all('div', {'class': 'a-section review aok-relative'})

sentiments = []

for review in reviews:
    # Extract the review text and other relevant information
    review_text = review.find('span', {'class': 'a-size-base review-text'}).text
    rating = review.find('span', {'class': 'a-icon-alt'}).text.split(' ')[0]
    
    # Perform sentiment analysis
    blob = TextBlob(review_text)
    sentiment = blob.sentiment.polarity
    
    sentiments.append(sentiment)
    
    print(f'Review Text: {review_text}')
    print(f'Rating: {rating}')
    print(f'Sentiment: {sentiment}')
    print('--------------------------')

df = pd.DataFrame(sentiments, columns=['Sentiment'])
df['Sentiment'] = df['Sentiment'].astype(float)
df.hist(bins=10)

plt.show()
