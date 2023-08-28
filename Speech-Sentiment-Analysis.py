# Importing Libraries

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import matplotlib.pyplot as plt

# Getting Input from Microphone

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing Background Noise....")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message....")
    recordedaudio = recognizer.listen(source)
    print("Done recording....")
    
try:
    print("Printing your message....")
    text=recognizer.recognize_google(recordedaudio,language="en-US")
    print("Your Message: {}".format(text))
except Exception as ex:
    print(ex)

# Sentiment Analysis

Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
sentiment_scores = []

for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v)
    sentiment_scores.append(v)   
    
# Extract compound scores for visualization

compound_scores = [score['compound'] for score in sentiment_scores]

# Determine color based on sentiment scores

bar_colors = ['red' if score < 0 else 'green' for score in compound_scores]

# Create a simple visualization

plt.figure(figsize=(8, 6))
plt.bar(range(len(compound_scores)), compound_scores, color=bar_colors)
plt.ylabel('Sentiment Compound Score')
plt.title('Sentiment Analysis of Captured Sentence')
plt.xticks(range(len(compound_scores)), ['Captured Sentence'])
plt.ylim([-1, 1])
plt.grid(True)
plt.show()

