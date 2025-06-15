from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

@app.route("/noticias")
def noticias():
    url_rss = "https://rss.app/feeds/kBDQ4R9HXXok1OeG.xml"
    feed = feedparser.parse(url_rss)

    titulares = []
    for entry in feed.entries[:5]:
        titulares.append({
            "titulo": entry.title,
            "fecha": entry.published,
            "link": entry.link
        })

    return jsonify({"noticias": titulares})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
