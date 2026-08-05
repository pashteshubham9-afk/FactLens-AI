import sys
import joblib

from utils import clean_text, find_red_flags

MODEL_PATH = "fake_news_model.pkl"


def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print(f"Could not find {MODEL_PATH}. Run 'python train.py' first.")
        sys.exit(1)


def predict_one(model, text: str):
    cleaned = clean_text(text)

    prediction = model.predict([cleaned])[0]

    probability = model.predict_proba([cleaned])[0]
    classes = list(model.classes_)

    confidence = probability[classes.index(prediction)]

    flags = find_red_flags(text)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "flags": flags
    }


def main():

    model = load_model()

    print("Fake News Detector (CLI) - type 'quit' to exit\n")

    while True:

        news = input("Enter News: ").strip()

        if news.lower() in ("quit", "exit"):
            break

        if not news:
            print("Please enter some text.\n")
            continue


        result = predict_one(model, news)


        if result["prediction"] == 0:
            label = "FAKE News"
        else:
            label = "REAL News"


        print(
            f"\nVerdict: {label} "
            f"(confidence: {result['confidence'] * 100:.1f}%)"
        )


        if result["flags"]:
            print(
                "Red-flag phrases detected:",
                ", ".join(result["flags"])
            )

        print()


if __name__ == "__main__":
    main()