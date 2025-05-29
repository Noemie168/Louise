import streamlit as st
from PIL import Image
import os


def home_page():
    # ─────────────────────────────
    # HERO SECTION
    # ─────────────────────────────
    left_col, right_col = st.columns(2)

    # ── Profile text ───────────────────────────────────────────
    left_col.markdown(
        """
        <h3>Louise&nbsp;Liu</h3>
        <p>
            Master of Science in Marketing – HEC Paris<br>
            Exchange MSc in Marketing – CUHK Business School<br>
            Paris · Hong Kong<br>
            <a href="mailto:Louise.liu@email.com">Louise.liu@email.com</a>
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ── Profile picture ───────────────────────────────────────
    image_path = os.path.join("static", "images", "photo.png")  # Replace with your profile image
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=256)
    else:
        right_col.warning("✨ Upload your profile image to static/images/photo.png")

    st.markdown("---")

    # ─────────────────────────────
    # ABOUT ME
    # ─────────────────────────────
    st.markdown(
        """
        ### About Me
        Passionate **luxury fashion & beauty marketing enthusiast** with a strong academic foundation from **HEC Paris** and an exchange experience at **CUHK Business School**.

        During my studies, I completed internships at **Louis Vuitton**, **Chanel**, and **L’Oréal Luxe**, where I applied consumer insight, competitive benchmarking, and data-driven storytelling to support product launches, digital campaigns, and in-store activations.

        Analytical, creative, and fluent in **English, Mandarin, and French**, I thrive in cross-functional teams and aspire to develop impactful marketing strategies for global luxury brands.
        """
    )

    # ─────────────────────────────
    # SKILLS SUMMARY
    # ─────────────────────────────
    st.markdown(
        """
        ### Key Skills
        - **Marketing Tools:** Google Analytics · SEMrush · Hootsuite · Salesforce Marketing Cloud  
        - **Data & Analytics:** Excel (Pivot Tables, VLOOKUP) · SPSS · Tableau  
        - **Digital Marketing:** Meta Ads Manager · WeChat Ads · Paid Social Campaigns  
        - **Brand Strategy:** Strategic Brand Communications · Competitive Benchmarking · Consumer Surveys  
        - **Design & Visual:** Canva  
        - **Languages:** Mandarin (Native) · English (Fluent) · French (Advanced)
        """
    )

    st.markdown("---")
