import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from config import NEWSAPI_KEY


NEWSAPI_URL = "https://newsapi.org/v2/everything"



def check_live_news(query, max_results=5):

    if not NEWSAPI_KEY:
        return "unavailable", []


    if not query.strip():
        return "unavailable", []



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
            timeout=5
        )


        data = response.json()


        if data.get("status") != "ok":
            return "unavailable", []



        articles = data.get("articles", [])


        if not articles:
            return "not_found", []



        matches = []


        for article in articles:


            title = article.get("title","")


            similarity = calculate_similarity(
                query,
                title
            )


            # Only accept strong matches

            if similarity >= 70:


                matches.append(
                    {
                        "title": title,
                        "source": article["source"]["name"],
                        "url": article["url"],
                        "similarity": similarity
                    }
                )



        if matches:

            return "found", matches


        return "not_found", []



    except Exception:

        return "unavailable", []




def calculate_similarity(text1,text2):


    vectorizer = TfidfVectorizer(
        stop_words="english"
    )


    vectors = vectorizer.fit_transform(
        [text1,text2]
    )


    score = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]


    return round(score*100,2)