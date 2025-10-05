import streamlit as st

st.set_page_config(page_title="Toxic Radar Quiz", page_icon="🚨", layout="wide")

# CSS for styling
st.markdown("""
<style>
.header { text-align: center; font-weight: bold; color: #d32f2f; margin: 2rem 0; }
.q { background: #f9f9f9; padding: 1rem; border-left: 4px solid #d32f2f; margin: 1rem 0; }
.result { background: #fff3cd; padding: 1rem; border-radius: 8px; font-weight: 500; }
.subscribe { text-align: center; margin-top: 2rem; }
.footer { text-align: center; color: #666; font-size: 0.8rem; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="header">Toxic Radar Quiz</div>', unsafe_allow_html=True)
st.markdown("Answer honestly. Spot the signs before they trap you.")

# Questions
questions = [
    "Charm Overload: Does he charm everyone instantly—friends, strangers, even servers—so your complaints about him sound unbelievable?",
    "Sudden Absence: Does he vanish for days without a word, leaving you checking his status while he acts like nothing happened?",
    "Jealousy Flip: Does he accuse you of cheating or flirting while he’s the one hiding texts or dodging questions?",
    "Gift Guilt: Does he give small favors or cash, then act like you owe him your loyalty forever?",
    "Public Praise, Private Sting: Does he praise you in front of others but criticize you harshly when you’re alone?",
    "Gaslight Twist: Does he call you too sensitive or say you misremember events, making you question your own reality?",
    "Isolation Web: Does he make you feel watched everywhere—stores, parks, socials—so you avoid going out to escape his judgment?",
    "Ambition Block: Does he mock your goals or hobbies, turning your progress into proof you’re neglecting him?",
    "Blame Shift: Does he claim you’re the one hurting him, even when you’ve done nothing but try to please him?",
    "Control Probe: Does he ask about your day or friends, only to use your answers later as ammo to control or shame you?"
]

# Quiz logic
if 'answers' not in st.session_state:
    st.session_state.answers = []

if len(st.session_state.answers) < len(questions):
    q_num = len(st.session_state.answers)
    st.markdown(f'<div class="q">{q_num + 1}. {questions[q_num]}</div>', unsafe_allow_html=True)
    ans = st.radio("", ["Yes", "No"], key=f"q{q_num}")
    if st.button("Next"):
        st.session_state.answers.append(ans)
else:
    score = sum(1 for a in st.session_state.answers if a == 'Yes')
    if score == 0:
        msg = "He might just be clueless. Watch closer."
    elif score <= 3:
        msg = "Early red flags. Trust your gut."
    elif score <= 6:
        msg = "Clear patterns. He’s playing games."
    elif score <= 9:
        msg = "Danger zone. You’re not imagining this."
    else:
        msg = "Black Hole Vacuum: He’s a parasite draining your soul."
    st.markdown(f'<div class="result">{msg}</div>', unsafe_allow_html=True)
    st.markdown('<div class="subscribe">Want the full escape plan? <a href="https://rumble.com/c/LisaSilvaToxicRadar">Subscribe on Rumble – $5/month</a>: tools, scripts, and ways to break free.</div>', unsafe_allow_html=True)
    if st.button("Restart"):
        st.session_state.answers = []

# Footer with your name
st.markdown('<div class="footer">Built by Lisa Silva | Deployed with Streamlit Cloud</div>', unsafe_allow_html=True)