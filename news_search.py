import requests
from config import NEWSAPI_KEY


NEWSAPI_URL = "https://newsapi.org/v2/everything"


def search_news(query, max_results=5):

    if not NEWSAPI_KEY:
        return {
            "status": "error",
            "message": "NewsAPI key missing",
            "articles": []
        }


    if not query.strip():
        return {
            "status": "error",
            "message": "Empty search",
            "articles": []
        }


    try:

        response = requests.get(
            NEWSAPI_URL,
            params={
                "q": query,
                "language": "en",
                "sortBy": "relevancy",
                "pageSize": max_results,
                "apiKey": NEWSAPI_KEY
            },
            timeout=10
        )


        data = response.json()


        if data.get("status") != "ok":

            return {
                "status": "error",
                "message": data.get("message", "API error"),
                "articles": []
            }


        articles = []


        for article in data.get("articles", []):

            articles.append(
                {
                    "title": article.get("title"),
                    "description": article.get("description"),
                    "source": article.get("source", {}).get("name"),
                    "url": article.get("url")
                }
            )


        return {
            "status": "success",
            "articles": articles
        }


    except Exception as e:

        return {
            "status": "error",
            "message": str(e),
            "articles": []
        }