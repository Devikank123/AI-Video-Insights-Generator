import re
# search for patterns in text
def detect_actions(text):
    sentences=text.split(".")
    action=[]
    for s in sentences:
        if re.search(r"will|should|need to|must",s.lower()):
            action.append(s.strip())
    return action

# Text
#  ↓
# Split into sentences
#  ↓
# Check each sentence
#  ↓
# Find action words (regex)
#  ↓
# Store matching sentences
#  ↓
# Return actions