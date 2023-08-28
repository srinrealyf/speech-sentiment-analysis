# speech-sentiment-analysis
## Speech Sentiment Analysis using VADER

We have a lot of underutilised audio data, although sentiment analysis is often done using text data. In order to manage various AI-related apps, we made the decision to create a processor that could identify a person's emotions based solely on their speech. Examples include the ability of call centres to play music during tense exchanges. Another example may be a smart car that slows down when the driver is scared or angry. This program captures audio using a microphone, converts it to text using Google's Speech Recognition API, performs sentiment analysis on the recognized text using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool, and visualizes the sentiment using a bar chart.

### Table of Contents
- Requirements
- Installation
- Usage
- Output Visualization
- Contributing
- License


### Requirements
To run this program, you need:

- Python 3.x
- vaderSentiment library (for sentiment analysis)
- speech_recognition library (for speech recognition)
- matplotlib library (for visualization)

### Installation
1. Installing 'vaderSentiment' Library using PIP
   
   ``` pip install vaderSentiment ```
   
2. Installing 'SpeechRecognition' Library using PIP

   ``` pip install speech_recognition ```   

3. Installing 'Matplotlib' Library using PIP

   ``` pip install matplotlib ```
### Usage
Run the following program using a Python interpreter

``` python speech-sentiment-analysis.py ```

Follow the on-screen instructions to capture the audio message. Audio recieved from microphone will be processed to remove the ambient noise for better results. The program will perform sentiment analysis on the recognized text and display the sentiment visualization.
### Output
The program converts the speech to text and prints in the output terminal. Post analysing the speech, VADER gives the polarity score of the speech in four parameters such as ; 'pos' - positive, 'neg' - negative, 'neu' - neutral, 'compound' - aggregated score
### Visualization
The program generates a bar chart visualization to represent the sentiment of the captured sentence. The bars are colored green for positive sentiment (compound score above 0) and red for negative sentiment (compound score below 0).
### Contributing
Contributions are welcome! If you find any issues or want to enhance the program, feel free to submit a pull request or open an issue.
### License
This project is licensed under the Creative Commons License.
