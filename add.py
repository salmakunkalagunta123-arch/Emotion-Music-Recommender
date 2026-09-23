import streamlit as st

st.set_page_config(
    page_title="Emotional Music Recommender",
    page_icon="🎵"
)

st.title("🎵 Emotional Music Recommender")
st.write("Select your mood and discover songs that match your emotions. 💙")

mood = st.selectbox(
    "How are you feeling today?",
    [
        "Happy 😊",
        "Sad 😔",
        "Relaxed 😌",
        "Energetic ⚡",
        "Romantic ❤️",
        "Stressed 😟",
        "Motivated 🔥"
    ]
)

music = {
    "Happy 😊": [
        ("Happy – Pharrell Williams",
         "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("On Top of the World – Imagine Dragons",
         "https://www.youtube.com/watch?v=w5tWYmIOWGk"),
        ("Best Day of My Life – American Authors",
         "https://www.youtube.com/watch?v=Y66j_BUCBMY"),
        ("Uptown Funk – Mark Ronson ft. Bruno Mars",
         "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
        ("Can't Stop the Feeling – Justin Timberlake",
         "https://www.youtube.com/watch?v=ru0K8uYEZWw")
    ],

    "Sad 😔": [
        ("Someone Like You – Adele",
         "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go – Passenger",
         "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Fix You – Coldplay",
         "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("Lovely – Billie Eilish",
         "https://www.youtube.com/watch?v=V1Pl8CzNzCw"),
        ("When I Was Your Man – Bruno Mars",
         "https://www.youtube.com/watch?v=ekzHIouo8Q4")
    ],

    "Relaxed 😌": [
        ("Perfect – Ed Sheeran",
         "https://www.youtube.com/watch?v=2Vv-BfVoq4g"),
        ("Photograph – Ed Sheeran",
         "https://www.youtube.com/watch?v=nSDgHBxUbVQ"),
        ("Ocean Eyes – Billie Eilish",
         "https://www.youtube.com/watch?v=viimfQi_pUw"),
        ("Yellow – Coldplay",
         "https://www.youtube.com/watch?v=yKNxeF4KMsY"),
        ("A Thousand Years – Christina Perri",
         "https://www.youtube.com/watch?v=rtOvBOTyX00")
    ],

    "Energetic ⚡": [
        ("Believer – Imagine Dragons",
         "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Thunder – Imagine Dragons",
         "https://www.youtube.com/watch?v=fKopy74weus"),
        ("Hall of Fame – The Script",
         "https://www.youtube.com/watch?v=mk48xRzuNvA"),
        ("Eye of the Tiger – Survivor",
         "https://www.youtube.com/watch?v=btPJPFnesV4"),
        ("Don't Stop Me Now – Queen",
         "https://www.youtube.com/watch?v=HgzGwKwL
