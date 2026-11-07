''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    result = sentiment_analyzer(text_to_analyze)
    label = result['label']
    score = result['score']
    if label == "None" and score == "None":
        return "Invalid input! Try again."
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}"

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
