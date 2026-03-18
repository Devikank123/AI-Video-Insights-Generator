from transformers import pipeline
# transformer is library in hugging face transformers used for handling the text like summarizer,keyword extraction
summarizer=pipeline("text2text-generation", model="google/flan-t5-base")
# summarization is pre-trained model which is present in pipeline module in transformer
def summarize_text(text):
    # text from speech-to-text.py
    summary=summarizer(text,max_length=150,min_length=50,do_sample=False)
    # maximum length of the summary must be max of 120 words and minnimum of 30
    # do_false means randomly generating the summary that at everytym we refresh we need same memory
    return summary[0]["generated_text"]
# in json format as output array inside that we have json
