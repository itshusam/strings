reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    modified_review = review
    for keyword in keywords:
        modified_review = modified_review.replace(keyword, keyword.upper())
    print(modified_review)
    
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def count(review):
    positive_count = sum(review.lower().count(word) for word in positive_words)
    negative_count = sum(review.lower().count(word) for word in negative_words)
    return positive_count, negative_count


def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        summary = review[:30]
        last_space_index = summary.rfind(' ')
        if last_space_index != -1:
            summary = summary[:last_space_index]
        return summary + "…"
