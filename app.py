import streamlit as st

st.set_page_config(page_title="Innovators' Hub", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Challenges", "Reflections", "Achievements"])

st.sidebar.title("📞 Contact Info")
st.sidebar.write("📧 Email: contact@innovatorshub.com")
st.sidebar.write("🌐 Website: [www.innovatorshub.com](https://www.innovatorshub.com)")

# Home Section
if section == "Home":
    st.title("Innovators' Hub: Unlocking Creative Potential")
    st.header("🚀 Welcome to the Future of Innovation! 🧠")
    st.write("Step into a world where creativity meets technology...")
    st.image("images/home.png")

# Challenges Section
elif section == "Challenges":
    st.header("💡 Think Differently!")
    st.image("images/chal.webp")
    user_input = st.text_input("Challenge yourself: What's a unique idea you've been thinking about?")
    if user_input:
        st.success(f"🚀 Amazing! Keep refining your idea: {user_input}")
    else:
        st.warning("💭 Share your thoughts and start innovating!")

# Reflections Section
elif section == "Reflections":
    st.header("🔍 Learn & Evolve!")
    st.image("images/ref.webp")
    reflection = st.text_area("What key lesson did you learn today?")
    if reflection:
        st.success(f"🌟 Insightful Reflection: {reflection}")
    else:
        st.info("📝 Writing down your thoughts helps shape your journey.")

# Achievements Section
elif section == "Achievements":
    st.header("🎯 Celebrate Your Wins!")
    st.image("images/achiment.webp")
    achievement = st.text_input("What’s one accomplishment you’re proud of today?")
    if achievement:
        st.success(f"🏆 Well done! Keep up the great work: {achievement}")
    else:
        st.info("🚀 Every step forward matters!")

# Footer
st.markdown("---")
st.write("Great minds create great futures. Stay inspired! 💪")
st.write("**📌 © 2025 Innovators' Hub**")
