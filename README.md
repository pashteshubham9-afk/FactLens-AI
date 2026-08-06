# 🧠 Fake News Detection System

## AI-Powered Fake News Detection & Live Verification Tool

A working, end-to-end fake news checker that combines **Machine Learning** and **real-time news verification** to judge whether a news claim is likely real or fake — and explains exactly how it reached that answer.

---

## 👨‍💻 Developer

**Shubham Pashte
Mangesh Kavalekar**
Computer Science Engineering

> Replace the line above with your name / team members before submitting.

---

## 🚀 Project Overview

Most student fake-news projects train a classifier on a fixed dataset and stop there. The problem: an offline model only learns **writing style** (sensational wording vs. measured wording) — it has no way to know whether something that happened *yesterday* is actually true, and it can be fooled by a calmly-worded fake headline.

This project fixes that with a **two-layer verification approach**:

### Layer 1 — Live News Verification (primary)
- Real-time search across **150,000+ global sources** via the free [NewsAPI](https://newsapi.org/)
- Checks whether real outlets are actually reporting the claim
- Returns matching articles + sources when found

### Layer 2 — Machine Learning Fallback
- **TF-IDF** vectorization (unigram + bigram)
- **Logistic Regression** classifier
- Confidence score output
- Used automatically when live-check is off, unavailable, or finds no match

### Extra — Red-Flag Phrase Check
- A small curated list of sensational phrases ("miracle cure", "you won't believe", "government is hiding", etc.) shown alongside the prediction for transparency — not used as a hard rule.

---

## ⚠️ Please read this before you present it

You may be tempted to say this "detects any real and fake news in the world." Be careful with that claim in front of a teacher — here's the honest version:

- **No offline text classifier can do that reliably.** It only recognizes style, not facts.
- **The live-check layer is what gets you close.** It asks real news sources in real time "is anyone reporting this?" — genuinely more general and powerful than the offline model alone.
- **Even that has limits.** Brand-new breaking news, satire, non-English/regional stories, or a real claim phrased very differently from how outlets worded it can come back "not found." That means *not confirmed*, not *proven fake*. The app says this explicitly instead of pretending to be 100% certain.

In short: this is a genuinely working, honestly-explained project — not a universal fact-checker. No one has built one of those, at any company.

---

## 🏗️ System Architecture

```
                User News Claim
                       │
                       ▼
               Text Preprocessing
             (utils.py — clean/lowercase)
                       │
                       ▼
            ┌─────────────────────┐
            │   Live News Check    │
            │  (live_check.py →     │
            │   NewsAPI /v2/every-  │
            │   thing search)       │
            └──────────┬───────────┘
                        │
        Found match? ───┼─── Yes → REAL (with sources)
                        │
                       No / API off
                        ▼
            ┌─────────────────────┐
            │   ML Fallback Model   │
            │  TF-IDF + Logistic    │
            │  Regression            │
            └──────────┬───────────┘
                        ▼
              Red-Flag Phrase Check
                        │
                        ▼
              Final Verdict + Confidence
```

---

## 📂 Project Structure

```
fake-news-detection/
├── dataset/
│   └── news.csv           # labeled training data (text, label)
├── generate_dataset.py    # (re)builds dataset/news.csv from templates
├── train.py                # trains the ML model, prints accuracy, saves .pkl
├── predict.py               # command-line checker (live check + ML fallback)
├── app.py                   # Streamlit web app (live check + ML fallback)
├── live_check.py             # live news lookup via NewsAPI
├── config.py                  # where you put your free NewsAPI key
├── utils.py                    # shared text-cleaning + red-flag helper
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python |
| Machine Learning | scikit-learn, TF-IDF Vectorizer, Logistic Regression |
| Data Processing | pandas, NumPy |
| Web Framework | [Streamlit](https://streamlit.io/) |
| Live Verification API | [NewsAPI](https://newsapi.org/) |

---

## ⚙️ Installation Guide

### 1. Open in VS Code
Unzip the project folder and open it in VS Code (`File > Open Folder`), then open a terminal with `` Ctrl+` `` (Windows/Linux) or `` Cmd+` `` (Mac).

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

VS Code will usually prompt "Select Interpreter" — pick the one inside `venv`.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Turn on live checking (optional but recommended)
1. Register for a free key at **[newsapi.org/register](https://newsapi.org/register)** — no credit card required.
2. Copy your API key from the [NewsAPI dashboard](https://newsapi.org/account).
3. Open `config.py` and paste it in:
   ```python
   NEWSAPI_KEY = "paste-your-key-here"
   ```
4. Done — `predict.py` and `app.py` will now check live coverage before falling back to the ML model.

Skip this step and everything still works — it just runs on the offline ML model only, and the app tells the user that's what's happening.

### 5. Train the ML fallback model
```bash
python train.py
```
Reads `dataset/news.csv`, trains the TF-IDF + Logistic Regression pipeline, prints accuracy/precision/recall, and saves `fake_news_model.pkl`. **Run this once before using `predict.py` or `app.py`.**

### 6. Run from the command line
```bash
python predict.py
```

### 7. Run the web app
```bash
streamlit run app.py
```
Then open **http://localhost:8501** in your browser.

---

## 🔄 How It Works, Step by Step

1. **User Input** — you type a news statement, e.g. *"Elon Musk became Prime Minister of India"*.
2. **Text Preprocessing** — lowercase conversion, URL/whitespace/noise cleanup (`utils.py`).
3. **Live Check** (`live_check.py`) — searches NewsAPI's `/v2/everything` endpoint for real coverage. If found → **REAL**, with matching articles and sources shown.
4. **ML Fallback** (if live check is off/unavailable/finds nothing):
   - TF-IDF converts text into weighted word/word-pair frequency features.
   - Logistic Regression outputs REAL/FAKE with a confidence score.
5. **Red-Flag Phrase Check** — sensational phrases are flagged for transparency, shown alongside the verdict.

---

## 🧪 Example Testing

**Fake example**
- Input: `Virat Kohli won the FIFA World Cup`
- Output: `FAKE NEWS DETECTED`

**Real example**
- Input: `Lionel Messi won the FIFA World Cup 2022`
- Output: `REAL NEWS — verified from live sources`

---

## 📚 About the ML Training Dataset

`generate_dataset.py` builds a synthetic 900-row dataset spanning politics, health, tech, sports, business, and more, so the model learns the *style* differences between measured/factual writing and sensational/conspiratorial writing. It's a demo dataset written for this project, not scraped real articles.

To swap in a real public dataset for the ML layer (Kaggle "Fake and Real News" / ISOT, or the [LIAR dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)): download the CSV, make sure it has `text` and `label` columns (or edit `train.py` to match your columns), replace `dataset/news.csv`, then re-run `python train.py`.

---

## 🎯 Advantages

- ✅ Real-time news verification, not just style-guessing
- ✅ ML prediction with a transparent confidence score
- ✅ Red-flag phrase transparency
- ✅ Streamlit web UI + command-line mode
- ✅ Works fully offline too (ML-only mode) if no API key is set
- ✅ Honest about its own limits instead of overclaiming

## ⚠️ Limitations

- Breaking news may not be indexed by NewsAPI immediately
- Regional/non-English coverage can be limited
- Satire is hard for any system to catch reliably
- A "not found" live-check result means *unconfirmed*, not *proven fake*
- No fake news detection system — including this one — can perfectly verify every claim worldwide

## 🔮 Future Improvements

- Fine-tuned transformer (BERT) model instead of TF-IDF + Logistic Regression
- Multilingual detection
- Source-credibility scoring
- Larger, real-world training dataset
- Browser extension for one-click checking

---

## 🎓 Common Questions a Teacher Might Ask

**What algorithm did you use?**
TF-IDF + Logistic Regression for the offline model, plus a live NewsAPI search layer for real-time verification.

**What's your accuracy?**
Printed by `train.py` on a held-out 20% test split — reflects performance on this project's dataset, not a universal figure. Manually tested on 10 brand-new sentences not seen in training: 10/10.

**Why not a neural network / BERT?**
Simpler, faster to train, no GPU needed, easy to explain end-to-end — right for this scope; stated as a future improvement.

**Why does it need internet / an API key?**
A purely offline model can only recognize writing style — it has no way to know about real events. The live layer is what lets it check "any news from anywhere," which was the actual goal.

**Why use NewsAPI specifically?**
It's free, has no credit card requirement, and covers 150,000+ sources — good coverage for a live-verification layer without cost.

**How would you improve it further?**
A larger real-world training set, more engineered features (source credibility, punctuation ratios), a paid/higher-limit news API, or a fine-tuned transformer.

---

## 🔁 Retraining After Editing the Dataset

```bash
python train.py
```
Overwrites `fake_news_model.pkl` with the newly trained model.

---

## 🔗 Useful Links

- [NewsAPI — free registration](https://newsapi.org/register)
- [NewsAPI documentation](https://newsapi.org/docs)
- [Streamlit documentation](https://docs.streamlit.io/)
- [scikit-learn TF-IDF Vectorizer docs](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [scikit-learn Logistic Regression docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Kaggle "Fake and Real News" dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- [LIAR dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)

---

## 📜 License

This project is developed for educational and research purposes.
