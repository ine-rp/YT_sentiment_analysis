# YouTube Sentiment Analyzer 🎥

This project is a simple web app that integrates a natural language processing (NLP) model to analyze the sentiment of YouTube video comments.

You enter a YouTube video URL, and the app:
1. Fetches comments using the YouTube Data API
2. Processes the text with a pre-trained NLP model (TextBlob)
3. Classifies each comment as positive, neutral, or negative
4. Displays a sentiment breakdown (% positive, neutral, negative)
5. Shows the top 3 comments for each sentiment category

---

## 🧠 **Why I Built This**

My goal was to explore **integrating an NLP model into an end-to-end application**.

I wanted to build more than a standalone ML notebook — I wanted to connect:
- External data collection (YouTube API)
- Natural language processing
- Real-time inference
- A working web interface to deliver results

---

## 💻 **Tech Stack**

- **Python**
- **Flask (serving the app & inference)**
- **TextBlob (pre-trained sentiment analysis model)**
- **YouTube API (external data source)**
- **HTML/CSS**

---

## 🚀 **Key Features**

✅ Fetch live YouTube comments  
✅ Analyze sentiment with pre-trained NLP  
✅ Categorize by polarity (positive / neutral / negative)  
✅ Sort comments by polarity strength  
✅ Display results in a user-friendly web interface

---

## 🏃‍♀️ **Run Locally**

1. Clone this repository
2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
   
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

4. Add your Youtube API key in .env file
```bash
YOUTUBE_API_KEY=your_api_key_here
```

---

## 🙋‍♀️ About Me
I’m a software engineer with experience in mobile development and a growing focus on AI engineering and ML model integration.

This project is part of my hands-on journey building applied machine learning projects that connect models to real users.

Feel free to connect:
<br/>https://www.linkedin.com/in/ines-rodriguez-piola
<br/>https://www.instagram.com/inesthetechie
<br/>https://www.x.com/inesthetechie
