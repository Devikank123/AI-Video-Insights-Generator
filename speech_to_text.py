import whisper
# library to convert audio/video to text and gives output as json files
# works offline
# supports multiple language

model=whisper.load_model("base")

# "base" is a pretrained model consists of function-->"Audio → Encoder → Hidden Representation → Decoder → Text"
def transcribe_audio(video_path):
    result=model.transcribe(video_path)
    # this method converts the audio to text and give the output in json format
    return result["text"]
# bcos in the resultant json there will many keys in that one of the key is "text"