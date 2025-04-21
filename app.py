import streamlit as st

st.set_page_config(page_title="Growth Mindset App", page_icon="🌱")

st.title("🌱 Build Your Growth Mindset")
st.subheader("Change your thoughts, change your life!")

# User Inputs
name = st.text_input("👤 Your Name:")
goal = st.text_input("🎯 What's your goal?")
challenge = st.text_area("⚠️ What challenge are you facing?")

if st.button("Motivate Me!"):
    if name and goal and challenge:
        st.success(f"Hello {name}! Your goal is: **{goal}**")
        st.write("💪 Facing challenges is the first step toward a growth mindset.")
        st.info("🚀 Tips for a Growth Mindset:")
        st.markdown("- Improve a little every single day")
        st.markdown("- Mistakes make you stronger")
        st.markdown("- Start thinking: 'I'm learning'")
        st.markdown("- Never give up — consistency is the key")
        st.balloons()
    else:
        st.warning("⛔ Please fill out all the fields so I can motivate you!")

st.write("---")
st.caption("Made by "ATIF AHMED"")
