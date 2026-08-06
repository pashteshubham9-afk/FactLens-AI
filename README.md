# 🧠 FactLens AI

## AI-Powered Fake News Detection, Fact Verification & Source Analysis System

FactLens AI is an intelligent fake news detection and verification platform that combines **Machine Learning, Natural Language Processing, Fact Verification, Live News Search, and Generative AI** to analyze news claims and provide an understandable verification report.

The system does not only predict whether a statement looks fake or real based on text patterns, but also verifies information using external sources and provides explanations with supporting evidence.

---

# 🚀 Project Overview

Fake news has become one of the biggest challenges in the digital world. Millions of misleading articles and social media posts are created every day, making it difficult for users to identify trustworthy information.

Traditional fake news detection models mainly depend on previously trained datasets. Such models can identify writing patterns but cannot understand whether a new event actually happened.

FactLens AI solves this problem by combining multiple verification layers:

### 1. Machine Learning Detection

The ML model analyzes the writing style and language patterns of news content.

Technologies used:

- TF-IDF Vectorization
- Logistic Regression Classification
- Probability-based confidence scoring

---

### 2. Fact Knowledge Base Verification

FactLens AI contains a custom fact database that compares user claims with stored verified information.

It uses:

- NLP text similarity
- TF-IDF similarity matching
- Cosine similarity scoring

This helps identify known true and false claims.

---

### 3. Live News Verification

The system connects with live news sources using NewsAPI.

It checks:

- Whether trusted sources are reporting the same information
- Related articles
- Source details
- Current coverage

---

### 4. AI Explanation Engine

Using Generative AI, FactLens provides a detailed explanation:

- Final verdict
- Reason behind decision
- Supporting facts
- Source analysis
- Simple human-readable explanation

---

# ⭐ Key Features

## 🤖 AI Powered Verification

- Machine Learning prediction
- Fact checking
- AI generated explanations
- Confidence score


## 🌐 Live Source Verification

- Real-time news search
- Related article display
- Source credibility information


## 📚 Fact Database

- Custom knowledge base
- Similarity based matching
- Verified information comparison


## 📊 Smart Decision System

Combines:

Machine Learning
        +
Fact Verification
        +
Live News Search
        +
AI Explanation

to generate the final result.


## 🖥️ Streamlit Web Application

Provides:

- User-friendly interface
- Demo examples
- Instant analysis
- Result dashboard


---

# 🏗️ System Architecture


             User News Claim

                   |

                   ▼

          Text Preprocessing

          (Cleaning + NLP)

                   |

                   ▼


    ┌────────────────────────┐
    │ Fact Knowledge Base     │
    │   facts.csv             │
    └──────────┬─────────────┘

               |

               ▼


    ┌────────────────────────┐
    │ Live News Verification  │
    │       NewsAPI            │
    └──────────┬─────────────┘

               |

    ┌──────────┴──────────┐

    ▼                     ▼
   Verified Source       No Match
    |                     |

    ▼                     ▼


 REAL RESULT      ML Prediction


                          |

                          ▼


             TF-IDF + Logistic Regression


                          |

                          ▼


                Final Verdict

                          |

                          ▼


                AI Explanation Report

---

# 🛠️ Technologies Used


| Category | Technology |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| Algorithm | Logistic Regression |
| Data Processing | Pandas, NumPy |
| Web Framework | Streamlit |
| AI Model | OpenAI API |
| Live Verification | NewsAPI |
| Model Saving | Joblib |
| Version Control | Git & GitHub |


---

# 📂 Project Structure


FactLens-AI/
│
├── app.py
├── train.py
├── predict.py
│
├── ai_model.py
├── ai_explainer.py
├── logic.py
├── news_search.py
├── live_check.py
├── utils.py
├── config.py
│
├── dataset/
│   ├── news.csv
│   └── facts.csv
│
├── fake_news_model.pkl
│
├── requirements.txt
│
└── README.md

---

# ⚙️ Installation Guide


## Step 1: Clone Repository


```bash
git clone https://github.com/pashteshubham9-afk/FactLens-AI.git
Move into folder:
cd FactLens-AI
Step 2: Create Virtual Environment
python -m venv venv
Activate:
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
🔑 API Configuration
NewsAPI Setup
Create account:
https://newsapi.org/register
Add API key in:
config.py
Example:
NEWSAPI_KEY="your_newsapi_key"
OpenAI API Setup
Add:
OPENAI_API_KEY="your_openai_key"
This enables AI generated verification reports.
🧠 Machine Learning Model
Algorithm Used
TF-IDF + Logistic Regression
TF-IDF
Converts text into numerical features by calculating word importance.
Example:
News Text

↓

Important Word Features

↓

Machine Learning Input
Logistic Regression
Classification:
0 → Fake News

1 → Real News
The model also provides confidence probability.
📚 Dataset Information
The project uses labeled news data containing:
Real news examples
Fake news examples
Different categories
Various writing styles
Dataset categories include:
Politics
Sports
Technology
Health
Business
General News
The dataset can be replaced with larger public datasets such as:
ISOT Fake News Dataset
LIAR Dataset
Kaggle Fake and Real News Dataset


# 🔄 Working Process


## Step 1: User Input

User enters a news claim in the FactLens AI application.


Example:

Cristiano Ronaldo plays football


---

## Step 2: Text Processing

The system cleans the input:

- Converts text to lowercase
- Removes unnecessary characters
- Removes noise
- Prepares text for analysis


---

## Step 3: Fact Verification

The claim is compared with the internal fact database.

The system calculates similarity between:

User Claim
    +
Stored Facts


If a strong match is found, the fact verification result is generated.


---

## Step 4: Live News Search


The system searches online news sources using NewsAPI.


It checks:

- Matching headlines
- News articles
- Publishing sources
- Current reports


---

## Step 5: ML Prediction


If live verification is unavailable, the ML model predicts using:


Input Text
↓
TF-IDF Feature Extraction
↓
Logistic Regression
↓
Prediction + Confidence Score


---

## Step 6: AI Explanation


The AI engine generates:

- Final verdict
- Reasoning
- Supporting information
- Source analysis
- Easy explanation


---

# 🧪 Testing Examples


## Example 1: Fake News Detection


Input:

Virat Kohli won FIFA World Cup


Output:

❌ FAKE NEWS DETECTED
Reason:
No verified sources found and fact database does not support the claim.


---


## Example 2: Real Information


Input:

Lionel Messi won FIFA World Cup 2022


Output:

✅ REAL NEWS
Verified from available information and sources.


---


## Example 3: General Fact


Input:

Python is a programming language


Output:

✅ REAL NEWS


---

# 📊 Result Analysis


FactLens AI provides:


### Prediction

REAL / FAKE


### Confidence Score

Example:

Confidence: 92.45%


### Evidence

- Matching facts
- Related sources
- AI explanation


---

# 🎯 Advantages


✅ Hybrid AI + Machine Learning approach

✅ Real-time news verification

✅ Explainable AI output

✅ Fact-based verification

✅ Confidence score generation

✅ User-friendly Streamlit interface

✅ Offline ML fallback support

✅ Suitable for educational and research purposes


---

# ⚠️ Limitations


Although FactLens AI provides advanced verification, some limitations exist:


- Breaking news may not appear immediately in external APIs

- Regional and non-English news coverage may be limited

- Satirical content can be difficult to classify

- A missing news result does not always mean fake

- No AI system can guarantee 100% worldwide fact verification


---

# 🔮 Future Improvements


Future versions can include:


## Advanced AI Models

- BERT based transformer models
- Large Language Models
- Better contextual understanding


## Multilingual Support

Support for:

- Marathi
- Hindi
- Other regional languages


## Source Credibility System

Add:

- Website reputation scoring
- Author verification
- Trust ranking


## Browser Extension

Allow users to verify news directly while browsing.


## Social Media Integration

Analyze:

- Twitter/X posts
- Facebook posts
- Viral content


---

# 🎓 Viva Questions & Answers


## Q1. What is the main objective of this project?


Answer:

The objective is to detect misleading news and provide verification using Machine Learning, live sources, and AI explanation.


---

## Q2. Which Machine Learning algorithm is used?


Answer:

TF-IDF is used for feature extraction and Logistic Regression is used for classification.


---

## Q3. Why not use only Machine Learning?


Answer:

A normal ML model only learns patterns from old data. It cannot know whether a new event actually happened, therefore live verification is added.


---

## Q4. Why use NewsAPI?


Answer:

NewsAPI provides access to current news articles from multiple sources, helping the system verify recent claims.


---

## Q5. Why use Streamlit?


Answer:

Streamlit allows quick development of an interactive machine learning web application using Python.


---

## Q6. What is the future scope?


Answer:

Future improvements include transformer models, multilingual support, better source credibility scoring, and browser extension integration.


---

# 🌐 Project Links


## GitHub Repository

https://github.com/pashteshubham9-afk/FactLens-AI


## Live Streamlit Application

https://factlens-ai-mnqpcgcrm3yv2bi6vtepsg.streamlit.app/


## Documentation Links


Python:

https://www.python.org/


Streamlit:

https://streamlit.io/


Scikit-learn:

https://scikit-learn.org/


NewsAPI:

https://newsapi.org/


OpenAI:

https://openai.com/


---

# 📸 Project Screenshots


## FactLens AI Dashboard


![FactLens AI Home](screenshots/home.png)



## News Analysis Result


![News Result](screenshots/result.png)



## AI Explanation Output


![AI Explanation](screenshots/ai_explanation.png)



---

# 📜 License


This project is developed for educational and research purposes.


---

# 👨‍💻 Developers


## Main Developer


**Shubham Pashte**

Computer Science Engineering



## Second Developer


**Mangesh Kavalekar**

Information Technology


---

⭐ If you find this project useful, consider giving it a star on GitHub.
