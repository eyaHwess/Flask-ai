from services.spam_detector import detect_spam

examples = [
    "This tool is very useful and well-documented.",
    "Great performance, fast integration!",
    "nice",
    "test",
    "amazing",
    "buy now!!! FREE access",
    "bbg",
    "hello",
    "super buggy and doesn't work at all"
]

for review in examples:
    label = detect_spam(review)
    print(f"📩 {review} ➜ {label}")
