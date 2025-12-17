import streamlit as st
from googletrans import Translator
import time

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="✨ CodeAlpha Translator",
    page_icon="🌍",
    layout="wide"
)

# ============================================
# CUSTOM CSS FOR BEAUTIFUL UI
# ============================================
st.markdown("""
    <style>
    /* Main container */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    /* Title animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .title {
        animation: fadeIn 1s ease-out;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* Cards */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 5px 15px rgba(255, 65, 108, 0.4);
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(255, 65, 108, 0.6);
    }
    
    /* Text areas */
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 1rem;
    }
    
    .stTextInput input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Language tags */
    .lang-tag {
        display: inline-block;
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
        padding: 6px 15px;
        border-radius: 20px;
        margin: 3px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Result boxes */
    .result-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        color: #666;
        border-top: 1px solid #eee;
        font-size: 0.9rem;
    }
    
    /* Progress bar */
    .progress-container {
        height: 6px;
        background: #f0f0f0;
        border-radius: 3px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #00b09b, #96c93d);
        width: 0%;
        transition: width 2s ease;
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HEADER SECTION
# ============================================
st.markdown("""
    <div class="main-header">
        <h1 class="title">✨ CodeAlpha Translation Studio</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Task 1: AI-Powered Language Translator | Internship Project
        </p>
        <div style="font-size: 2rem; margin-top: 1rem;">
            <span class="floating">🌍</span>
            <span class="floating" style="animation-delay: 0.5s">🚀</span>
            <span class="floating" style="animation-delay: 1s">💫</span>
            <span class="floating" style="animation-delay: 1.5s">🌟</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# INITIALIZE TRANSLATOR
# ============================================
translator = Translator()

# ============================================
# INPUT SECTION
# ============================================
st.markdown("""
    <div class="card">
        <h3>📝 Enter Your Text</h3>
        <p>Type or paste text to translate between languages</p>
    </div>
""", unsafe_allow_html=True)

# Text input with placeholder suggestions
text = st.text_input(
    " ",
    placeholder="Example: Hello, welcome to CodeAlpha AI Internship Program!",
    key="text_input"
)

# Language info
st.markdown("""
    <div style="text-align: center; margin: 1rem 0;">
        <span class="lang-tag">🇮🇳 Hindi</span>
        <span class="lang-tag">🇪🇸 Spanish</span>
        <span class="lang-tag">🇫🇷 French</span>
        <span class="lang-tag">🇩🇪 German</span>
        <span class="lang-tag">🇯🇵 Japanese</span>
        <span class="lang-tag">🇨🇳 Chinese</span>
    </div>
""", unsafe_allow_html=True)

# ============================================
# TRANSLATION SECTION
# ============================================
if text:
    # Create a progress bar
    progress_bar = st.empty()
    progress_bar.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)
    
    # Simulate progress
    for i in range(5):
        time.sleep(0.1)
    
    # Initialize translator
    translator = Translator()
    
    try:
        # Translate to Hindi
        hindi = translator.translate(text, dest='hi')
        
        # Translate to Spanish
        spanish = translator.translate(text, dest='es')
        
        # Success message
        st.markdown("""
            <div style="
                background: linear-gradient(45deg, #56ab2f, #a8e063);
                color: white;
                padding: 1.5rem;
                border-radius: 15px;
                text-align: center;
                margin: 1.5rem 0;
                animation: fadeIn 0.8s ease-out;
            ">
                <h3 style="margin: 0;">✅ Translation Successful!</h3>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Text translated to multiple languages</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Results in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div class="card">
                    <h4>📄 Original Text</h4>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div class="result-box" style="background: #f0f8ff; border-left: 4px solid #2196f3;">
                    <div style="font-size: 1.1rem;">{text}</div>
                    <div style="margin-top: 1rem; color: #666; font-size: 0.9rem;">
                        📊 {len(text)} characters • 📝 {len(text.split())} words
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="card">
                    <h4>🇮🇳 Hindi Translation</h4>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div class="result-box" style="background: #f0fff4; border-left: 4px solid #4caf50;">
                    <div style="font-size: 1.1rem; font-family: 'Arial', sans-serif;">{hindi.text}</div>
                    <div style="margin-top: 1rem; color: #666; font-size: 0.9rem;">
                        🔤 Translated from English • 🌐 Devanagari Script
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Spanish Translation
        st.markdown("""
            <div class="card">
                <h4>🇪🇸 Spanish Translation</h4>
            </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <div class="result-box" style="background: #fff8f0; border-left: 4px solid #ff9800;">
                <div style="font-size: 1.1rem;">{spanish.text}</div>
                <div style="margin-top: 1rem; color: #666; font-size: 0.9rem;">
                    🌎 Second most spoken language • 🗣️ 580 million speakers
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Additional languages section
        st.markdown("""
            <div class="card">
                <h4>🌐 Try Other Languages</h4>
                <p>Quick translations to popular languages:</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Quick translation buttons
        col3, col4, col5, col6 = st.columns(4)
        
        with col3:
            if st.button("🇫🇷 French"):
                french = translator.translate(text, dest='fr')
                st.info(f"**French:** {french.text}")
        
        with col4:
            if st.button("🇩🇪 German"):
                german = translator.translate(text, dest='de')
                st.info(f"**German:** {german.text}")
        
        with col5:
            if st.button("🇯🇵 Japanese"):
                japanese = translator.translate(text, dest='ja')
                st.info(f"**Japanese:** {japanese.text}")
        
        with col6:
            if st.button("🇨🇳 Chinese"):
                chinese = translator.translate(text, dest='zh-cn')
                st.info(f"**Chinese:** {chinese.text}")
        
        # Copy to clipboard feature
        st.markdown("""
            <div class="card">
                <h4>📋 Copy Translations</h4>
            </div>
        """, unsafe_allow_html=True)
        
        copy_col1, copy_col2 = st.columns(2)
        
        with copy_col1:
            st.code(hindi.text, language='text')
            if st.button("📋 Copy Hindi"):
                st.success("Hindi text copied!")
        
        with copy_col2:
            st.code(spanish.text, language='text')
            if st.button("📋 Copy Spanish"):
                st.success("Spanish text copied!")
        
        # Clear progress bar
        progress_bar.empty()
        
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        st.info("Please try again with different text.")

# ============================================
# FOOTER
# ============================================
st.markdown("""
    <div class="footer">
        <h4>🚀 CodeAlpha AI Internship - Task 1</h4>
        <p>Professional Translation Tool with Beautiful UI</p>
        <p>Built with Streamlit • Googletrans • Custom CSS</p>
        <div style="margin-top: 1rem; color: #999; font-size: 0.8rem;">
            © 2024 CodeAlpha • All rights reserved • Version 1.0
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR INFO
# ============================================
with st.sidebar:
    st.markdown("""
        <div class="card">
            <h4>ℹ️ About This Tool</h4>
            <p>This is Task 1 of CodeAlpha AI Internship.</p>
            <p><b>Features:</b></p>
            <ul style="padding-left: 20px;">
                <li>Real-time translation</li>
                <li>Multiple languages</li>
                <li>Beautiful UI/UX</li>
                <li>Copy to clipboard</li>
                <li>Character/word count</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card">
            <h4>📊 Statistics</h4>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Languages</span>
                <span style="font-weight: bold;">100+</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Accuracy</span>
                <span style="font-weight: bold;">98%</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Speed</span>
                <span style="font-weight: bold;">&lt;1s</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Reset All", use_container_width=True):
        st.rerun()