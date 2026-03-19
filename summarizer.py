from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

def summarize_text(text):
    # limit long text (important)
    text = text[:1000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]['summary_text']