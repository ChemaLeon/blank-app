import streamlit as st
from openai import OpenAI
import random

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("⚔️ AI Boss Fight")

# game state
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100
    st.session_state.boss_hp = 100
    st.session_state.log = []

st.write(f"🧍 Player HP: {st.session_state.player_hp}")
st.write(f"👹 Boss HP: {st.session_state.boss_hp}")

attack = st.text_input("Describe your attack")

if st.button("Attack") and attack:
    
    player_damage = random.randint(10, 20)
    boss_damage = random.randint(8, 15)

    st.session_state.boss_hp -= player_damage
    st.session_state.player_hp -= boss_damage

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a boss in a video game. Describe the fight in 1–2 sentences."
            },
            {
                "role": "user",
                "content": f"The player attacked with: {attack}. They dealt {player_damage} damage. The boss dealt {boss_damage} damage back."
            }
        ]
    )

    result = response.choices[0].message.content
    st.session_state.log.append(result)

# battle log
st.subheader("Battle")
for line in reversed(st.session_state.log[-6:]):
    st.write(line)

# win/lose
if st.session_state.boss_hp <= 0:
    st.success("🏆 You defeated the boss!")

if st.session_state.player_hp <= 0:
    st.error("💀 You were defeated.")