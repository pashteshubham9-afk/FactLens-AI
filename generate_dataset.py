"""
generate_dataset.py

Builds dataset/news.csv used to train the model.

The original project shipped with only 6 example rows, which is nowhere
near enough for a text classifier to learn real patterns - it would just
memorize those 6 sentences and fail on anything a teacher actually typed
in live. This script generates a much larger, more varied set of REAL vs
FAKE style headlines/sentences using templates + word banks, covering many
topics (politics, health, tech, sports, business, environment, crime,
entertainment) so the model sees many different phrasings of each style.

NOTE: This is a synthetic/curated demo dataset written for this project,
not scraped from real news outlets. It is good enough to demonstrate a
working end-to-end pipeline and to reward the *style* differences between
real reporting and fake/sensational writing (which is what these classic
TF-IDF + Logistic Regression projects actually learn). For higher real-world
accuracy, swap this file for a public dataset such as the Kaggle
"Fake and Real News" (ISOT) dataset or the LIAR dataset - see README.md
for how to do that swap.

Run: python generate_dataset.py
"""

import csv
import itertools
import random

random.seed(42)

# ---------------------------------------------------------------------------
# Word banks
# ---------------------------------------------------------------------------

countries = ["India", "the United States", "the United Kingdom", "Japan", "Brazil",
             "Germany", "Canada", "Australia", "South Africa", "France", "Kenya", "Mexico"]
cities = ["Mumbai", "New York", "London", "Tokyo", "Sao Paulo", "Berlin",
          "Toronto", "Sydney", "Cape Town", "Paris", "Nairobi", "Delhi"]
universities = ["Harvard University", "Oxford University", "IIT Delhi", "Stanford University",
                "MIT", "University of Cambridge", "University of Tokyo", "the University of Toronto"]
journals = ["Nature", "The Lancet", "Science", "the Journal of Applied Physics",
            "the British Medical Journal", "Cell"]
diseases = ["diabetes", "the common cold", "arthritis", "insomnia", "hair loss",
            "high blood pressure", "back pain", "acne", "obesity"]
sports = ["cricket", "football", "basketball", "tennis", "hockey", "badminton"]
companies = ["a leading tech firm", "a major automobile manufacturer", "a national airline",
             "a large retail chain", "a well-known electronics company", "a regional bank"]
ministries = ["the Ministry of Education", "the Ministry of Health", "the Department of Transport",
              "the Finance Ministry", "the local municipal council", "the state government"]
celebrities = ["a popular film actor", "a well-known singer", "a famous cricketer",
               "a prominent politician", "a top business leader"]
objects = ["a common kitchen spice", "tap water", "a household plant", "baking soda",
           "a fruit peel", "ordinary tea leaves", "coconut oil", "lemon juice"]
percentages = [str(n) for n in range(2, 20)]
years_ahead = [str(n) for n in range(2, 200, 7)]

# ---------------------------------------------------------------------------
# REAL templates - measured, attributed, specific, checkable claims
# ---------------------------------------------------------------------------

real_templates = [
    "{ministry} announced a new policy to improve public services in {city}.",
    "Researchers at {university} published a study on {disease} treatment in {journal}.",
    "{country}'s economy grew by {pct} percent last quarter, according to official data.",
    "The local team won the {sport} match after a closely fought contest in {city}.",
    "{company} reported its quarterly earnings today, showing steady growth.",
    "{ministry} confirmed that road repair work will begin in {city} next month.",
    "A new study from {university} found that regular exercise improves sleep quality.",
    "{country} signed a trade agreement aimed at boosting exports this year.",
    "Health officials in {city} recommended flu vaccinations ahead of the winter season.",
    "The city council in {city} approved funding for a new public library.",
    "Scientists at {university} are studying the effects of climate change on rainfall patterns.",
    "{company} recalled a batch of products after a minor safety issue was identified.",
    "{ministry} released updated guidelines for {disease} prevention this week.",
    "The national cricket board announced the schedule for the upcoming {sport} season.",
    "Unemployment in {country} fell slightly last month, labour ministry data shows.",
    "A team of doctors at {university} hospital successfully completed a rare surgery.",
    "{country} will host an international conference on renewable energy next year.",
    "Local authorities in {city} opened a new public park after months of construction.",
    "The central bank of {country} kept interest rates unchanged this quarter.",
    "Farmers in {city} reported an improved harvest this season due to favourable rainfall.",
    "{company} announced plans to open a new manufacturing plant near {city}.",
    "A report by {university} researchers highlights steady progress in reducing {disease} cases.",
    "Election officials in {country} confirmed voter turnout figures for the recent polls.",
    "The transport department in {city} introduced new bus routes to ease congestion.",
    "{ministry} published its annual report on education outcomes across the country.",
    "NASA-funded researchers confirmed the discovery of water traces on a distant exoplanet.",
    "Astronomers at {university} discovered a new comet using a ground-based telescope.",
    "A peer-reviewed clinical trial confirmed a new treatment for {disease} is safe and effective.",
    "Engineers at {university} unveiled a prototype for more efficient solar panels.",
    "Officials confirmed that the bridge project in {city} is on schedule for completion next year.",
]

# ---------------------------------------------------------------------------
# FAKE templates - sensational, absolute, unverifiable, conspiratorial, clickbait
# ---------------------------------------------------------------------------

fake_templates = [
    "Doctors don't want you to know this one trick that cures {disease} overnight!",
    "{object} can completely cure {disease} in just three days, scientists are stunned.",
    "Aliens were spotted landing near {city} and the government is hiding the truth.",
    "Drinking {object} every morning will make you live to {years_ahead} years old.",
    "BREAKING: {celebrity} secretly controls the world's banks, insider reveals.",
    "Government of {country} is secretly using hidden machines to control the weather.",
    "This {object} trick will make you lose 10 kilos in a week, no diet needed!",
    "Shocking video proves the moon landing in {country} was completely fake.",
    "You won't believe what {celebrity} did that doctors are trying to cover up.",
    "Scientists confirm {disease} can be cured instantly by staring at the sun for 5 minutes.",
    "Secret documents reveal {country} government is hiding evidence of time travel.",
    "This one weird trick cures {disease} permanently, big pharma hates it!",
    "{city} residents report seeing ghosts controlling the traffic lights at night.",
    "Miracle {object} discovered to reverse aging completely, must share before it's banned!",
    "Leaked report claims {company} is secretly implanting microchips in every product.",
    "Experts warn that 5G towers in {city} are turning water into poison overnight.",
    "{celebrity} reveals they are actually an alien sent to observe {country}.",
    "New study 'proves' that the earth is actually shrinking every single year.",
    "Government hiding cure for {disease} to keep hospitals in business, whistleblower claims.",
    "Share this before it gets deleted: {object} instantly detoxifies your entire body!",
    "Secret society in {city} is controlling world governments, anonymous source claims.",
    "This banned {object} remedy cures {disease} that doctors refuse to prescribe.",
    "Video 'proof' shows {celebrity} is secretly a robot built by a tech company.",
    "Officials in {country} confirm bottled water is being replaced with mind control serum.",
    "A grandmother's forgotten {object} remedy is curing {disease} overnight, doctors baffled.",
]

# ---------------------------------------------------------------------------
# Build the rows
# ---------------------------------------------------------------------------

def fill(template):
    return template.format(
        ministry=random.choice(ministries),
        city=random.choice(cities),
        university=random.choice(universities),
        journal=random.choice(journals),
        disease=random.choice(diseases),
        country=random.choice(countries),
        sport=random.choice(sports),
        company=random.choice(companies),
        celebrity=random.choice(celebrities),
        object=random.choice(objects),
        pct=random.choice(percentages),
        years_ahead=random.choice(years_ahead),
    )


def generate(templates, n):
    rows = set()
    attempts = 0
    while len(rows) < n and attempts < n * 30:
        t = random.choice(templates)
        rows.add(fill(t))
        attempts += 1
    return list(rows)


REAL_COUNT = 450
FAKE_COUNT = 450

real_rows = generate(real_templates, REAL_COUNT)
fake_rows = generate(fake_templates, FAKE_COUNT)

data = [(text, "REAL") for text in real_rows] + [(text, "FAKE") for text in fake_rows]
random.shuffle(data)

with open("dataset/news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(data)

print(f"Wrote {len(data)} rows to dataset/news.csv "
      f"({len(real_rows)} REAL, {len(fake_rows)} FAKE)")
