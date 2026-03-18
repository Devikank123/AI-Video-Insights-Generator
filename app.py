import streamlit as st

from youtube_downloader import download_video
from speech_to_text import transcribe_audio
from keywords import extract_keywords
from summarizer import summarize_text
from actions import detect_actions

st.set_page_config(page_title="AI Video Insights",layout="wide")
# it sets browser tab title

st.title("📽️ AI Video Meeting Insights Generator")
# it shows the title in the webpage

st.markdown("Upload or paste a Youtube link to extract insights automatically")
# it acts as a bar for pasting utube link

url=st.text_input("🔗 Enter the Youtube Link")
# it creates the input box for attaching the youtube link

# Button logic
if st.button("🔎Analyze Video"):
    if url=="":
        st.warning("Please enter a Youtube URL")

    else:
        progress=st.progress(0)
        # it generates the progress bar from 0-100 if actions done one by one then it get increased automatically

        # Download Video Setup
        with st.spinner("📥 Downloading video..."):
            # shows loading animations
            video_path=download_video(url)
            # downloads video
            progress.progress(20)
            # changes the progress to 20
        
            st.success("✅ Video Downloaded")
            st.video(url)
            # success msg will be shown along with the youtube video

        with st.spinner("🎙️ Transcribing speech..."):
            input=transcribe_audio(video_path)
            # converts speech to text using whisper
            progress.progress(50)

        with st.expander("📜 View Transcript"):
            st.write(input)

        with st.spinner("🧠 Generating AI insights..."):
            summary=summarize_text(input)
            keywords=extract_keywords(input)
            actions=detect_actions(input)
            progress.progress(100)

        st.success("🎉 Analysis Complete!")

        tab1,tab2,tab3=st.tabs(["📄 Summary", "🔑 Keywords", "✅ Action Items"])
        # creates tabbed interface

        with tab1:
            st.subheader("Summary")
            st.write(summary)

        with tab2:
            st.subheader("Key Topics")
            st.write(",".join(keywords))
            # convert list into readable string

        with tab3:
            st.subheader("Action items")
            for a in actions:
                st.write("✔️",a)

