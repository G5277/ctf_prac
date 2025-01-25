import streamlit as st
import pandas as pd
from datetime import datetime

# Title and Header
st.title("Capture the Flag (CTF) @_@ ")

# Sidebar for navigation
menu = st.sidebar.selectbox("Navigate", ["Home", "Leaderboard", "Contact Us"])

# Dummy data for leaderboard
leaderboard_data = {
    "Name": ["None"],
    "Score": [1000],
    "Last Submission": ["2025-01-01 12:30"]
}
leaderboard_df = pd.DataFrame(leaderboard_data)

import streamlit as st
import pandas as pd
from datetime import datetime

# Title and Header
st.title("Capture the Flag (CTF) Platform")
st.header("Welcome to the Ultimate CTF Challenge")

# Sidebar for navigation
menu = st.sidebar.selectbox("Navigate", ["Home", "Challenges", "Submit Flag", "Leaderboard", "Contact Us"])

# Dummy data for leaderboard
leaderboard_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [150, 100, 50],
    "Last Submission": ["2025-01-01 12:30", "2025-01-01 12:00", "2025-01-01 11:45"]
}
leaderboard_df = pd.DataFrame(leaderboard_data)

if menu == "Home":
    st.subheader("About the Event")
    st.write("""
        Capture the Flag (CTF) is a fun and engaging cybersecurity competition where participants solve challenges, find flags, and score points.
        
        - **Beginner-friendly**
        - **Exciting prizes**
        - **A great way to test your skills!**
    
        Get ready to explore various challenges across cryptography, web exploitation, reverse engineering, and more!
    
        **Event Date:** January 30, 2025
    """)
    st.subheader("What is Capture the Flag (CTF)?")
    st.write("""
        Capture the Flag (CTF) is a type of cybersecurity competition where participants complete security-related challenges to discover hidden 'flags' (strings of text).
        These challenges are designed to teach participants about various aspects of computer security, ranging from basic skills to advanced exploitation techniques.

        **Types of CTF Challenges:**
        - **Jeopardy-style:** Solve independent challenges across different categories (e.g., cryptography, reverse engineering, web security) to earn points.
        - **Attack-Defense:** Teams defend their systems while trying to attack opponents' systems to steal flags.

        **Why Participate in CTFs?**
        - Enhance your cybersecurity skills.
        - Learn to think like an attacker.
        - Build teamwork and collaboration skills.
        - Gain exposure to real-world scenarios in a controlled environment.
    """)

    # Form for flag submission
    with st.form("flag_form"):
        username = st.text_input("Your Name")
        challenge_name = st.text_input("Challenge Name")
        flag = st.text_input("Enter Flag")
        submit = st.form_submit_button("Submit")

    if submit:
        # Dummy flag validation
        if flag == "CTF{dummy_flag}":
            st.success(f"Correct Flag! Well done, {username}!")
        else:
            st.error("Incorrect Flag. Try again!")

elif menu == "Leaderboard":
    st.subheader("Leaderboard")
    st.write("Top participants:")
    st.table(leaderboard_df)

elif menu == "Contact Us":
    st.subheader("Contact Us")
    st.write("""
        For any queries, reach out to us:

        Discord ;)
        """)
