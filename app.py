from flask import Flask, render_template, request
from youtube import get_video_comments
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    comments = []
    samples = {}
    breakdown = {"positive": 0, "neutral": 0, "negative": 0}

    if request.method == "POST":
        url = request.form["video_url"]
        limit = int(request.form.get("limit", 20))
        video_id = extract_video_id(url)
        comments = get_video_comments(video_id, max_results=limit)

        scored_comments = {
            "positive": [],
            "neutral": [],
            "negative": []
        }

        for comment in comments:
            label, polarity = analyze_sentiment(comment)
            scored_comments[label].append((comment, polarity))
            breakdown[label] += 1

        total = sum(breakdown.values())
        result = {k: f"{(v / total) * 100:.1f}%" for k, v in breakdown.items()}

        samples = {
            "positive": sorted(scored_comments["positive"], key=lambda x: x[1], reverse=True)[:3],
            "neutral": sorted(scored_comments["neutral"], key=lambda x: abs(x[1]))[:3],
            "negative": sorted(scored_comments["negative"], key=lambda x: x[1])[:3],
        }

        # Remove polarity scores, keep only comment text
        samples = {k: [comment for comment, _ in v] for k, v in samples.items()}

    return render_template("index.html", result=result, samples=samples)

def extract_video_id(url):
    import re
    match = re.search(r"(?:v=|youtu.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)