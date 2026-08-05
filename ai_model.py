"""
FactLens AI
Generative AI Verification Engine
Developed by Shubham Pashte
"""

from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ai_analysis(
    news,
    result,
    confidence,
    facts,
    articles
):

    facts_text = ""

    for item in facts[:5]:

        facts_text += (
            f"- {item['subject']}: "
            f"{item['fact']}\n"
        )


    sources_text = ""

    for article in articles[:3]:

        sources_text += (
            f"- {article['title']} "
            f"({article['source']})\n"
        )


    prompt = f"""

You are a professional Fake News Verification AI.

Analyze this news claim:

Claim:
{news}


Machine Learning Prediction:
{result}

Confidence:
{confidence:.2f}%


Available Facts:
{facts_text}


Live Sources:
{sources_text}


Create a verification report:

1. Final verdict
2. Why this is true or false
3. Supporting facts
4. Source analysis
5. Simple explanation


"""


    try:

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[

                {
                    "role": "system",
                    "content":
                    "You are an expert fact checking assistant."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.2
        )


        return response.choices[0].message.content



    except Exception as e:

        return (
            "AI verification unavailable.\n"
            f"{e}"
        )