import streamlit as st

# Page settings
st.set_page_config(
    page_title="Emotion Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# Title
st.title("🎵 Emotion Music Recommender")
st.write("Choose your mood and get a song recommendation!")

# Songs based on emotions
songs = {
    "Happy 😊": {
        "song": "Pharrell Williams - Happy",
        "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    },
    "Sad 😢": {
        "song": "Adele - Someone Like You",
        "link": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"
    },
    "Relaxed 😌": {
        "song": "Ed Sheeran - Perfect",
        "link": "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    },
    "Energetic ⚡": {
        "song": "Imagine Dragons - Believer",
        "link": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
    },
    "Romantic ❤️": {
        "song": "Ed Sheeran - Perfect",
        "link": "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    },
    "Angry 😡": {
        "song": "Imagine Dragons - Believer",
        "link": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
    }
}

# Select emotion
emotion = st.selectbox(
    "How are you feeling today?",
    list(songs.keys())
)

# Recommendation button
if st.button("🎧 Recommend Song"):

    selected_song = songs[emotion]

    st.success(
        f"Recommended for your mood: {selected_song['song']}"
    )

    st.link_button(
        "▶️ Listen on YouTube",
        selected_song["link"]
    )
