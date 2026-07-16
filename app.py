from flask import Flask, render_template
import logging

app = Flask(__name__)

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

@app.route("/")
def home():

    logger.info("Home page accessed")
    return render_template("index.html")

@app.route("/health")
def health():
    logger.info("Health check accessed")
    return {
        "status": "healthy"
    }

@app.route("/about")
def about():
    logger.info("about page accessed")
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)