"""
Scrape a CNN article using BeautifulSoup and extract named entities using spaCy.
"""

import requests
from bs4 import BeautifulSoup
import spacy


def fetch_article(url: str) -> str:
    """Fetch and parse article content from URL using BeautifulSoup."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script and style elements
    for element in soup(["script", "style"]):
        element.decompose()

    # Try common CNN article content selectors
    article_text_parts = []

    # CNN uses various structures; try article body paragraphs
    article = soup.find("article") or soup.find("div", class_=lambda c: c and "article" in str(c).lower())
    if article:
        paragraphs = article.find_all("p")
        article_text_parts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

    # Fallback: get all paragraphs in main content area
    if not article_text_parts:
        main = soup.find("main") or soup.find("div", {"class": "article__content"})
        if main:
            paragraphs = main.find_all("p")
            article_text_parts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

    # Last fallback: first 30 substantial paragraphs
    if not article_text_parts:
        paragraphs = soup.find_all("p")
        article_text_parts = [
            p.get_text(strip=True)
            for p in paragraphs
            if len(p.get_text(strip=True)) > 50
        ][:30]

    return " ".join(article_text_parts)


def extract_entities(text: str) -> None:
    """Extract and display named entities using spaCy."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Group entities by type
    entities_by_type = {}
    for ent in doc.ents:
        label = ent.label_
        if label not in entities_by_type:
            entities_by_type[label] = []
        if ent.text not in entities_by_type[label]:
            entities_by_type[label].append(ent.text)

    # Entity type descriptions
    type_descriptions = {
        "PERSON": "People",
        "ORG": "Organizations",
        "GPE": "Geopolitical entities (countries, cities, states)",
        "LOC": "Locations",
        "DATE": "Dates",
        "EVENT": "Events",
        "WORK_OF_ART": "Works of art",
        "LAW": "Laws",
        "NORP": "Nationalities, religious, political groups",
        "FAC": "Facilities",
        "PRODUCT": "Products",
        "MONEY": "Monetary values",
        "TIME": "Times",
        "QUANTITY": "Quantities",
        "ORDINAL": "Ordinals",
        "CARDINAL": "Cardinal numbers",
    }

    print("\n" + "=" * 60)
    print("NAMED ENTITIES IN THE ARTICLE")
    print("=" * 60)

    for label in sorted(entities_by_type.keys()):
        desc = type_descriptions.get(label, label)
        print(f"\n{desc} ({label}):")
        print("-" * 40)
        for entity in sorted(entities_by_type[label], key=str.lower):
            print(f"  • {entity}")


def main():
    url = "https://www.cnn.com/2026/02/24/politics/team-usa-hockey-olympics-trump-state-of-the-union"

    print("Fetching article...")
    article_text = fetch_article(url)

    if not article_text.strip():
        print("Could not extract article content. The page structure may have changed.")
        return

    print(f"Extracted {len(article_text)} characters of article text.\n")
    print("=" * 60)
    print("ARTICLE PREVIEW (first 500 chars)")
    print("=" * 60)
    print(article_text[:500] + "..." if len(article_text) > 500 else article_text)

    extract_entities(article_text)


if __name__ == "__main__":
    main()
