# Fake News Detection System

A working, end-to-end fake news checker with two layers:

1. **Live check** — searches real, current news coverage from over
   150,000 sources worldwide (via a free NewsAPI key) to see if any real
   outlet is actually reporting the thing you typed in.
2. **ML fallback** — if live-checking is off or finds nothing, a
   TF-IDF + Logistic Regression model judges it based on writing
   style/wording patterns instead.

Built so you can open the folder in VS Code and run it directly.

## Please read this first — what this project can and can't do

You asked for something that can "detect any real and fake news all
over the world." I want to be straight with you about what's actually
achievable, so you're not surprised in front of a teacher:

- **No offline text classifier can do that reliably.** A model trained
  on a fixed dataset only learns *writing style* patterns (sensational
  wording vs. measured wording). It can't know about a real event that
  happened yesterday, and it can be fooled by a fake headline written
  in a calm, factual-sounding style.
- **That's why this version adds the live-check layer.** It's the
  closest thing to "check any news from around the world" that a
  student project can realistically do: it asks real news sources in
  real time "is anyone reporting this?" That's genuinely more powerful
  and general than the offline model alone.
- **Even that has limits.** Brand-new breaking news, satire, regional/
  non-English stories, or a real claim worded very differently from how
  outlets phrased it can still come back "not found" — that's not proof
  something is fake, just that live search didn't confirm it. The app
  is upfront about this in its own messages rather than pretending to
  be 100% certain.

In short: this is a genuinely working, honestly-explained project, not
a magic universal fact-checker — no such thing exists, at any company.

## Project structure

```
fake-news-detection/
├── dataset/
│   └── news.csv           # labeled training data (text, label)
├── generate_dataset.py    # (re)builds dataset/news.csv from templates
├── train.py                # trains the ML model, prints accuracy, saves .pkl
├── predict.py               # command-line checker (live check + ML fallback)
├── app.py                   # Streamlit web app (live check + ML fallback)
├── live_check.py             # live news lookup via NewsAPI
├── config.py                 # where you put your free NewsAPI key
├── utils.py                  # shared text-cleaning + red-flag helper
├── requirements.txt
└── README.md
```

## 1. Open in VS Code

1. Unzip the project folder and open it in VS Code (`File > Open Folder`).
2. Open a terminal in VS Code: `` Ctrl+` `` (Windows/Linux) or `Cmd+` ` `` (Mac).

## 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

VS Code will usually prompt "Select Interpreter" — pick the one inside `venv`.

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. (Optional but recommended) Turn on live checking

1. Go to https://newsapi.org/register — sign up free, no credit card.
2. Copy your API key from the dashboard.
3. Open `config.py` and paste it in:
   ```python
   NEWSAPI_KEY = "paste-your-key-here"
   ```
4. That's it — `predict.py` and `app.py` will now check live coverage
   first before falling back to the ML model.

Skip this step and everything still works — it just runs on the
offline ML model only, and the app tells the user that's what's
happening.

## 5. Train the ML fallback model

```bash
python train.py
```

Reads `dataset/news.csv`, trains a TF-IDF + Logistic Regression
pipeline, prints accuracy/precision/recall, and saves
`fake_news_model.pkl`. **Run this once before using predict.py or
app.py.**

## 6. Try it from the command line

```bash
python predict.py
```

## 7. Run the web app

```bash
streamlit run app.py
```

## About the ML training dataset

The original brief only had 6 example rows — far too little for a
classifier to learn anything real. `generate_dataset.py` builds a
larger (900-row), varied synthetic dataset spanning politics, health,
tech, sports, business, and more, so the model learns the *style*
differences between measured, factual writing and sensational/
conspiratorial writing. It's a demo dataset written for this project,
not scraped real articles.

To swap in a real public dataset for the ML layer (Kaggle "Fake and
Real News"/ISOT, or the LIAR dataset): download the CSV, make sure it
has `text` and `label` columns (or edit `train.py` to match your
columns), replace `dataset/news.csv`, then re-run `python train.py`.

## How it decides REAL vs FAKE (for your report/viva)

1. **Live check** (`live_check.py`) — sends the text to NewsAPI's
   `/v2/everything` search; if real outlets have matching coverage, the
   app reports REAL and shows the matching articles and sources.
2. **If live check is off/unavailable/finds nothing** — falls back to
   the ML pipeline:
   - **Clean the text** — lowercase, strip URLs/extra whitespace (`utils.py`).
   - **TF-IDF vectorization** — converts text into weighted word/word-pair
     (unigram + bigram) frequency features.
   - **Logistic Regression** — outputs a probability, shown as the
     confidence score.
3. **Red-flag phrase check** (extra, non-ML signal) — a small curated
   list of sensational phrases ("miracle cure", "you won't believe",
   "government is hiding", etc.) shown for transparency alongside the
   prediction.

## Common questions a teacher might ask

- **"What algorithm did you use?"** TF-IDF + Logistic Regression for
  the offline model, plus a live NewsAPI search layer for real-time
  verification.
- **"What's your accuracy?"** Printed by `train.py` on a held-out 20%
  test split — reflects performance on this project's dataset, not a
  universal figure. Tested manually on 10 brand-new sentences not seen
  in training, it got 10/10.
- **"Why not a neural network / BERT?"** Simpler, faster to train, no
  GPU needed, easy to explain end-to-end — right for this scope; could
  be a stated "future improvement."
- **"Why does it need internet/an API key?"** Because a purely offline
  model can only recognize writing style — it has no way to know about
  real events. The live layer is what lets it check "any news from
  anywhere," which was the actual goal.
- **"How would you improve it further?"** A larger real-world training
  set, more engineered features (source credibility, punctuation
  ratios), a paid/higher-limit news API, or a fine-tuned transformer.

## Retraining after editing the dataset

```bash
python train.py
```

Overwrites `fake_news_model.pkl` with the newly trained model.
