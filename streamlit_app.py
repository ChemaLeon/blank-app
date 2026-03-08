import streamlit as st

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

with st.form("my_form"):
    fav_color = st.selectbox(
        "What's your favorite color?",
        [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple"
        ]
    )
    
    reason = st.text_area("Talk about why that's your favorite color.")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("It's interesting that you like " + fav_color + ".")
        st.write("Your say it's because:")
        st.write("""
        ```
        reason
        ```
        """.replace("reason", reason))