import streamlit as st
from PIL import Image

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Julian Ramil Y. Andales | Portfolio",
    page_icon="💻",
    layout="wide",
)

# -----------------------------
# CUSTOM STYLES
# -----------------------------
st.markdown("""
    <style>
    .title {
        font-size: 60px;
        text-align: center;
        color: #a56eff;
        text-shadow: 2px 2px 6px #d8b4fe;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #d8b4fe;
    }
    .section-title {
        font-size: 28px;
        color: #a56eff;
        border-bottom: 2px solid #a56eff;
        margin-top: 30px;
        padding-bottom: 5px;
    }
    .highlight {
        color: #facc15;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='title'>🚀✨ Julian Ramil Y. Andales 🚀✨</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Aspiring Data & Backend Developer | Curious Learner | Problem Solver</div>", unsafe_allow_html=True)
st.write("")

# -----------------------------
# SIDEBAR - Contact Info
# -----------------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] img {
        border-radius: 50%;
        border: 3px solid #a56eff;
        box-shadow: 0px 0px 10px #d8b4fe;
    }
    </style>
""", unsafe_allow_html=True)
st.sidebar.image("photo.jpg", use_container_width=True, caption="Julian Ramil Y. Andales")
st.sidebar.header("📞 Contact Information")
st.sidebar.markdown("""
**Address:** Dumlog, Talisay City, Cebu  
**Birthday:** July 15, 2004  
**Mobile:** 0961-780-4983  
**Institutional Email:** [julianramil.andales@cit.edu](mailto:julianramil.andales@cit.edu)  
**Personal Email:** [julianramilandales@gmail.com](mailto:julianramilandales@gmail.com)  
**Facebook:** [Andales Julian Ramil](https://www.facebook.com/julianramil.andales.5)
""")

# -----------------------------
# MAIN CONTENT
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧍 About Me", "🎓 Education", "📈 Development", "💡 Projects", "💬 Philosophy & Goals"])

# -----------------------------
# TAB 1: ABOUT ME
# -----------------------------
with tab1:
    st.markdown("<div class='section-title'>Early Life</div>", unsafe_allow_html=True)
    st.write("""
    I was born in **Cordova, Cebu** and developed an early curiosity about how things work, 
    from **mechanical objects** to **living organisms**.  
    This fascination with functionality became the foundation of my analytical mindset.
    """)

    with st.expander("🌱 Fun Fact About My Childhood"):
        st.info("I once disassembled a toy robot just to understand how it is attached together and managed to reassemble it successfully!")

    st.markdown("<div class='section-title'>Quick Facts</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👶 Born", "July 15, 2004")
    with col2:
        st.metric("🏠 From", "Cordova, Cebu")
    with col3:
        st.metric("📍 Currently in", "Talisay City, Cebu")

# -----------------------------
# TAB 2: EDUCATION
# -----------------------------
with tab2:
    st.markdown("<div class='section-title'>Education Journey</div>", unsafe_allow_html=True)
    
    timeline = {
        "2011-2017": "🏫 Pilipog Elementary School",
        "2017-2021": "🎓 Talisay City Science High School",
        "2021-2023": "🏅 Cebu Institute of Technology-University (STEM Strand)",
        "2023-Present": "💻 Cebu Institute of Technology-University — **BS Computer Science**"
    }
    
    for year, details in timeline.items():
        st.markdown(f"**{year}** — {details}")

    st.progress(0.7)
    st.caption("Currently pursuing my college degree!")

# -----------------------------
# TAB 3: PERSONAL DEVELOPMENT
# -----------------------------
with tab3:
    st.markdown("<div class='section-title'>Personal Development</div>", unsafe_allow_html=True)
    st.write("""
    My fascination with how things function drives my curiosity.  
    I constantly seek to understand **the logic behind systems**, whether biological, mechanical, or digital.
    """)

    st.write("### 🌐 Interests & Learning Areas:")
    st.slider("Biology Knowledge", 0, 100, 65)
    st.slider("Chemistry Knowledge", 0, 100, 60)
    st.slider("Computing & Programming", 0, 100, 90)
    st.slider("Mathematics", 0, 100, 85)

    st.info("📚 I watch and read educational content regularly to stay updated and improve my analytical thinking.")

    st.markdown("<div class='section-title'>Technical Skills</div>", unsafe_allow_html=True)
    st.write("#### 💻 Programming Languages & Tools:")
    skills = {
        "C/C++/C#": 85,
        "Java": 80,
        "Python": 90,
        "Kotlin": 70,
        "HTML/CSS": 75,
        "Data Structures & Algorithms": 88
    }
    for s, level in skills.items():
        st.write(f"**{s}**")
        st.progress(level / 100)

# -----------------------------
# TAB 4: PROJECTS
# -----------------------------
with tab4:
    st.markdown("<div class='section-title'>Notable Projects</div>", unsafe_allow_html=True)

    projects = [
        {
            "name": "Castle TD",
            "desc": "A tower defense game inspired by strategic gameplay mechanics.",
            "tags": "🎮 Game Development"
        },
        {
            "name": "QuizMo",
            "desc": "An AI-integrated quiz and flashcard app designed to enhance study sessions.",
            "tags": "🧠 AI / Education"
        },
        {
            "name": "Simple Solitaire",
            "desc": "A minimalistic solitaire game app.",
            "tags": "🎮 Game Development"
        },
        {
            "name": "Numbuddy",
            "desc": "A math education app for children that makes learning fun.",
            "tags": "🔢 Education / Kids"
        }
    ]

    for proj in projects:
        with st.container():
            st.subheader(f"{proj['name']} {proj['tags']}")
            st.write(proj["desc"])
            st.divider()

# -----------------------------
# TAB 5: PERSONAL PHILOSOPHY & GOALS
# -----------------------------
with tab5:
    st.markdown("<div class='section-title'>Personal Philosophy</div>", unsafe_allow_html=True)
    st.success("💭 “Don’t worry about failing, worry about making the best out of it.”")

    st.markdown("<div class='section-title'>Future Goals</div>", unsafe_allow_html=True)
    st.write("""
    My future goal is to specialize in **data management** and **backend development** — 
    fields that perfectly align with my analytical mindset and passion for problem-solving.  
    I'm also eager to dive deeper into **data science** and **artificial intelligence** 
    as I continue growing my career as a computer scientist.
    """)

    st.balloons()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>© 2025 Julian Ramil Y. Andales</p>", unsafe_allow_html=True)
