import streamlit as st
import os
import base64
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mudassir Hussain", layout="wide")

# --- HELPER: FILE DOWNLOADER FOR CV ---
def get_cv_download_link(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    # Button design strictly following your screenshot style
    href = f'''
    <a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" style="text-decoration:none;">
        <div style="
            background: rgba(255,255,255,0.05); 
            border: 1px solid rgba(255,255,255,0.1); 
            color: #3B82F6; 
            padding: 12px 25px; 
            border-radius: 10px; 
            font-weight: 600; 
            text-align: center; 
            width: 180px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        ">
            Download CV <span style="font-size: 14px;">⬇</span>
        </div>
    </a>
    '''
    return href

# --- CUSTOM CSS (STRICT DESIGN) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #030014 !important;
        color: #ffffff !important;
        font-family: 'Urbanist', sans-serif;
    }

    /* Removing all default navigation elements as requested */
    [data-testid="stSidebar"], .logo, .nav-bar, header { display: none !important; }

    /* Button Styling to match screenshot image_a3869c.png */
    .stButton>button {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        padding: 12px 25px !important;
        border-radius: 10px !important;
        font-weight: 400 !important;
        width: 180px !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        border-color: #A855F7 !important;
    }

    /* Portrait & Ring (Strictly as per previous working style) */
    .pic-box { position: relative; width: 380px; height: 380px; margin: auto; display: flex; align-items: center; justify-content: center; }
    .ring { position: absolute; width: 100%; height: 100%; border-radius: 50%; border: 2px solid transparent; border-top: 2px solid #A855F7; border-right: 2px solid #3B82F6; animation: spin 4s linear infinite; }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .pic-box img { width: 320px; height: 320px; border-radius: 50%; object-fit: cover; z-index: 2; }

    /* Glass Cards */
    .glass-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 25px; height: 100%; }

    /* Form Styling */
    .stForm {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        max-width: 800px;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER (Fiverr Link Only) ---
st.markdown("""
<div style="display: flex; justify-content: flex-end; padding: 20px 5%;">
    <a href="https://www.fiverr.com/sellers/hifza403/edit" style="border: 1px solid #A855F7; padding: 8px 20px; border-radius: 10px; font-size: 14px; color: white; text-decoration: none;">Hire Me on Fiverr 🚀</a>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
c1, c2 = st.columns([1.3, 0.7])
with c1:
    st.markdown("<p style='opacity:0.8; font-size:18px; background:rgba(255,255,255,0.05); padding:10px 22px; border-radius:30px; display:inline-block;'>HELLO, I'M</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 70px; font-weight: 800; margin:0;'>MUDASSIR <span style='color:#A855F7;'>HUSSAIN</span></h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='opacity:0.8;'>Full-Stack Developer & UI/UX Designer</h3>", unsafe_allow_html=True)
    st.write("I design and build modern, responsive websites with clean code and creative UI/UX. Specialized in Python automation and SEO audits.")
    
    st.write("##")
    # Exact Button Placement as per image_a3869c.png
    b_col1, b_col2 = st.columns([0.5, 1])
    with b_col1:
        # This button scrolls to the form at the end
        if st.button("Contact Me ✉️"):
             st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
    with b_col2:
        if os.path.exists("Mudassir Cv.pdf"):
            st.markdown(get_cv_download_link("Mudassir Cv.pdf"), unsafe_allow_html=True)

with c2:
    if os.path.exists("selfimage.png"):
        with open("selfimage.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="pic-box"><div class="ring"></div><img src="data:image/png;base64,{data}"></div>', unsafe_allow_html=True)

# --- MIDDLE SECTIONS (Stats, About, Skills, Projects) ---
# Keeping these exactly as they were in the previous version
st.write("##")
s1, s2, s3, s4 = st.columns(4)
stats = [("2+", "Years Experience"), ("20+", "Projects Completed"), ("15+", "Happy Clients"), ("100%", "Client Satisfaction")]
for i, (v, l) in enumerate(stats):
    with [s1, s2, s3, s4][i]:
        st.markdown(f"<div style='text-align:center;'><span style='font-size:32px; font-weight:800; color:#A855F7; display:block;'>{v}</span><span style='font-size:12px; opacity:0.5; text-transform:uppercase;'>{l}</span></div>", unsafe_allow_html=True)

st.write("##")
col_a, col_s = st.columns(2, gap="large")
with col_a:
    st.markdown("### 👤 ABOUT ME")
    st.markdown("""<div class="glass-card"><p style='opacity:0.8;'>I'm a passionate Full-Stack Developer and UI/UX Designer from Pakistan. I specialize in bridging the gap between artistic design and logical backend systems using Python, Flask, and modern web tech.</p></div>""", unsafe_allow_html=True)
with col_s:
    st.markdown("### 🛠️ MY SKILLS")
    skills = {"Python Automation": 95, "UI/UX Design": 90, "Web Dev": 92, "SEO Audits": 88}
    for n, v in skills.items():
        st.markdown(f"<div style='display:flex; justify-content:space-between; font-size:14px;'><span>{n}</span><span style='color:#A855F7;'>{v}%</span></div><div style='background:rgba(255,255,255,0.1); height:8px; border-radius:10px; margin-bottom:15px;'><div style='height:100%; background:linear-gradient(90deg, #3B82F6, #A855F7); border-radius:10px; width:{v}%;'></div></div>", unsafe_allow_html=True)

st.write("##")
st.markdown("### 📂 FEATURED PROJECTS")
p1, p2, p3 = st.columns(3)
projs = [{"n": "Automation Bot", "i": "automation.png"}, {"n": "Python Game", "i": "game.png"}, {"n": "SEO Audit", "i": "seo.png"}]
for i, p in enumerate(projs):
    with [p1, p2, p3][i]:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        if os.path.exists(p['i']):
             with open(p['i'], "rb") as f:
                 p_data = base64.b64encode(f.read()).decode()
             st.markdown(f'<img src="data:image/png;base64,{p_data}" style="width:100%; border-radius:15px; margin-bottom:10px;">', unsafe_allow_html=True)
        st.markdown(f"<h4>{p['n']}</h4></div>", unsafe_allow_html=True)

# --- THE CONTACT FORM (At the very end) ---
st.write("---")
st.markdown("<h2 style='text-align:center;'>Let's <span style='color:#A855F7;'>Talk</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; opacity:0.6;'>Messages will be sent to xavierbacklinksexpert@gmail.com</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("How can I help you?")

    submit_button = st.form_submit_button("Send Message 🚀")

    if submit_button:
        if name and email and msg:
            import requests

            response = requests.post(
                "https://formspree.io/f/mzdovygb",
                data={
                    "name": name,
                    "email": email,
                    "message": msg
                }
            )

            if response.status_code == 200:
                st.success(f"Hi {name}, your message has been sent successfully!")
            else:
                st.error("Failed to send message. Please try again.")
        else:
            st.error("Please fill all fields.")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:12px;'>© 2026 Mudassir Hussain</p>", unsafe_allow_html=True)
