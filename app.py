"""
FactLens AI
AI Powered Fake News Detection & Verification System

Developed by Shubham Pashte
"""

import streamlit as st
import joblib

from utils import clean_text
from logic import check_fact
from news_search import search_news
from ai_explainer import generate_explanation
from ai_model import ai_analysis


MODEL_PATH = "fake_news_model.pkl"


st.set_page_config(
    page_title="FactLens AI",
    page_icon="🧠",
    layout="centered"
)


@st.cache_resource
def load_model():

    return joblib.load(MODEL_PATH)



try:

    model = load_model()

except Exception:

    st.error(
        "Model not found. Run train.py first."
    )

    st.stop()



st.title("🧠 FactLens AI")

st.subheader(
    "AI Powered Fake News Detection, Fact Verification & Source Analysis"
)


st.markdown(
"""
FactLens AI combines:

🤖 Machine Learning Prediction  
📚 Fact Knowledge Base  
🌐 Live News Verification  
🧠 AI Explanation Engine
"""
)


st.divider()



demo_news = [

"Virat Kohli won FIFA World Cup",

"Virat Kohli is an Indian cricket player",

"MS Dhoni won Cricket World Cup 2011",

"Lionel Messi won FIFA World Cup 2022",

"Cristiano Ronaldo plays football",

"Elon Musk is Prime Minister of India",

"Elon Musk owns Tesla",

"Narendra Modi is Prime Minister of India",

"India capital is New Delhi",

"Taj Mahal is located in Agra",

"Apple creates iPhone",

"Microsoft created Windows",

"ChatGPT is an artificial intelligence chatbot",

"Python is a programming language",

"Water chemical formula is H2O",

"IPL is cricket tournament"

]



selected = st.selectbox(
    "🎯 Demo News",
    ["Custom News"] + demo_news
)



if selected != "Custom News":

    news = st.text_area(
        "📰 News Claim",
        selected,
        height=130
    )

else:

    news = st.text_area(
        "📰 Enter News Claim",
        height=130
    )




if st.button(
    "🔍 Analyze News",
    type="primary"
):


    if not news.strip():

        st.warning(
            "Please enter news"
        )

        st.stop()



    with st.spinner(
        "Analyzing..."
    ):


        # -----------------------------
        # ML Prediction
        # -----------------------------

        cleaned = clean_text(news)


        prediction = model.predict(
            [cleaned]
        )[0]


        probability = model.predict_proba(
            [cleaned]
        )[0]


        confidence = max(probability) * 100



        if prediction == 1:

            ml_result = "REAL"

        else:

            ml_result = "FAKE"



        # -----------------------------
        # Fact Checking
        # -----------------------------

        fact_status, facts, fact_score = check_fact(
            news
        )



        # -----------------------------
        # Live News Search
        # -----------------------------

        live_result = search_news(
            news
        )


        articles = []


        if isinstance(live_result, dict):

            if live_result.get(
                "status"
            ) == "success":

                articles = live_result.get(
                    "articles",
                    []
                )



        # -----------------------------
        # FINAL DECISION ENGINE
        # -----------------------------


        final_result = ml_result



        # Fact database highest priority

        if fact_status == "true":

            final_result = "REAL"



        elif fact_score >= 35:

            final_result = "REAL"



        # Negative facts override

        for item in facts:

            fact = item["fact"].lower()


            if any(word in fact for word in [

                "false",
                "fake",
                "not true",
                "never",
                "did not"

            ]):

                final_result = "FAKE"



        # Live verified news

        if articles:

            final_result = "REAL"



    # -----------------------------
    # RESULT
    # -----------------------------


    st.divider()

    st.subheader(
        "📊 Final Result"
    )



    if final_result == "FAKE":

        st.error(
            "❌ FAKE NEWS DETECTED"
        )

    else:

        st.success(
            "✅ REAL NEWS"
        )



    st.metric(
        "AI Confidence",
        f"{confidence:.2f}%"
    )



    st.divider()

    st.subheader(
        "📚 Fact Verification"
    )



    if facts:


        for item in facts[:5]:

            st.info(
f"""
**{item['subject'].title()}**

{item['fact']}

Match Score: {item['score']}%
"""
            )


    else:

        st.warning(
            "No matching facts found."
        )



    st.divider()

    st.subheader(
        "🧠 AI Explanation"
    )



    try:


        if fact_score < 40 or len(facts) == 0:


            explanation = ai_analysis(
                news,
                final_result,
                confidence,
                facts,
                articles
            )


        else:


            explanation = generate_explanation(
                news,
                final_result,
                confidence,
                facts,
                articles
            )


        st.write(
            explanation
        )


    except Exception as e:

        st.warning(
            "AI explanation unavailable."
        )

        st.write(e)




    # Sources

    if articles:


        st.divider()

        st.subheader(
            "🌐 Related Sources"
        )


        for article in articles[:5]:


            st.markdown(
f"""
**{article.get('title')}**

Source: {article.get('source')}

{article.get('url')}

---
"""
            )




st.divider()


st.caption(
"""
🧠 FactLens AI

Fake News Detection + AI Verification System

Built using:
Machine Learning | Fact Checking | AI

Developed by Shubham Pashte
"""
)