"""
FactLens AI
AI Explanation Engine
Developed by Shubham Pashte
"""


def generate_explanation(
    news,
    result,
    confidence,
    facts,
    articles
):

    explanation = ""


    if result == "FAKE":

        explanation += f"""
🧠 AI Analysis:

This claim is likely FALSE.

Machine Learning Confidence:
{confidence:.2f}%


Reason:

The claim does not match with verified facts and available information.

"""

    else:

        explanation += f"""
🧠 AI Analysis:

This claim appears to be TRUE based on available facts and verification sources.

Machine Learning Confidence:
{confidence:.2f}%


Reason:

The claim matches with available knowledge and verified information.

"""


    if facts:

        explanation += """

Supporting Evidence:

"""

        for fact in facts[:5]:

            explanation += (
                f"✅ {fact['subject'].title()} : "
                f"{fact['fact'].capitalize()}\n"
            )


    if articles:

        explanation += """

Live Verification:

Verified related news sources were found online.

"""

        for article in articles[:3]:

            explanation += (
                f"📰 {article['source']} : "
                f"{article['title']}\n"
            )


    else:

        explanation += """

Live Verification:

No direct verified news evidence was found for this exact claim.

"""


    explanation += """

Final Decision:

The result is generated using:
🤖 Machine Learning Prediction
📚 Fact Verification
🔎 Live Source Analysis

"""


    return explanation