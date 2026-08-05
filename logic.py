import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


FACT_FILE = "dataset/facts.csv"



def load_facts():

    try:

        data = pd.read_csv(FACT_FILE)


        data["subject"] = (
            data["subject"]
            .astype(str)
            .str.lower()
        )


        data["fact"] = (
            data["fact"]
            .astype(str)
            .str.lower()
        )


        return data


    except Exception as e:

        print("Fact loading error:", e)

        return pd.DataFrame(
            columns=["subject","fact"]
        )




def check_fact(news):


    facts = load_facts()


    if facts.empty:

        return "not_found", [], 0



    news = news.lower()



    fact_texts = (

        facts["subject"]
        + " "
        + facts["fact"]

    ).tolist()



    vectorizer = TfidfVectorizer(
        stop_words="english"
    )


    vectors = vectorizer.fit_transform(
        fact_texts + [news]
    )



    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )[0]



    top_indexes = similarity.argsort()[-5:][::-1]



    results=[]



    for index in top_indexes:


        score = similarity[index] * 100


        # increase accuracy

        if score >= 45:


            results.append(

                {

                "subject":
                facts.iloc[index]["subject"],


                "fact":
                facts.iloc[index]["fact"],


                "score":
                round(float(score),2)

                }

            )




    if results:


        return (

            "similar",

            results,

            results[0]["score"]

        )



    return (

        "not_found",

        [],

        0

    )