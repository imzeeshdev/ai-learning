from rag import load_chunks, embed, retrieve

TESTS = [
    ("How much exercise does a dog need?", "dog_care_handbook.pdf"),
    ("Which foods are dangerous for dogs?", "dog_care_handbook.pdf"),
    ("What is a revision in PLM?", "plm_change_management.pdf"),
    ("Who sits on a change board?", "plm_change_management.pdf"),
    ("What does visibility of system status mean?", "ux_usability_heuristics.pdf"),
    ("How do I prevent user errors in an interface?", "ux_usability_heuristics.pdf"),
    ("How do I get around Malmö?", "malmo_newcomer_guide.pdf"),
    ("What is SFI?", "malmo_newcomer_guide.pdf"),
    ("How should I practise Swedish pronunciation?", "swedish_learning_guide.pdf"),
    ("How does Swedish word order work?", "swedish_learning_guide.pdf"),
]

items = load_chunks()
vectors = embed(["search_document: " + item["text"] for item in items])

passed = 0
top1 = 0
top3 = 0
refused = 0
MIN_SCORE = 0.55

for question, expected in TESTS:
    hits = retrieve(question, items, vectors, k=3)
    sources = [item["source"] for _, item in hits]
    best_score = hits[0][0]
    in_top1 = sources[0] == expected
    in_top3 = expected in sources
    would_refuse = best_score < MIN_SCORE
    top1 += in_top1
    top3 += in_top3
    refused += would_refuse
    flag = "OK  " if in_top1 and not would_refuse else "FAIL"
    print(flag, question, "->", sources[0], f"({best_score:.2f})")

n = len(TESTS)
print(f"\nTop-1 correct: {top1}/{n}   Top-3 contains it: {top3}/{n}   Wrongly refused: {refused}/{n}")