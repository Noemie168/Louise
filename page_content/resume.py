import streamlit as st
import os


def resume_page():
    # ─────────────────────────────
    # RESUME DOWNLOAD
    # ─────────────────────────────
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="Louise_Liu_Resume.pdf",
            mime='application/octet-stream'
        )
    else:
        st.warning("Resume PDF file not found")

    st.title("Louise Liu")

    # ─────────────────────────────
    # CONTACT INFO
    # ─────────────────────────────
    st.header("Contact Information")
    st.markdown("""
    - **Email:** Louise.liu@email.com  
    - **Phone:** +33 6 12 34 56 78  
    - **LinkedIn:** [linkedin.com/in/Louiseliu](https://linkedin.com/in/Louiseliu)  
    - **Location:** Paris, France
    """)

    # ─────────────────────────────
    # SUMMARY
    # ─────────────────────────────
    st.header("Professional Summary")
    st.markdown("""
    Driven Master’s student in Marketing with strong academic background and internship experience in luxury fashion and beauty brands.
    Seeking a marketing internship or entry-level role to leverage analytical skills and creative insight in a dynamic global organization.
    """)

    # ─────────────────────────────
    # EXPERIENCE
    # ─────────────────────────────
    st.header("Work Experience")
    st.markdown("""
    **Marketing Intern, Louis Vuitton**  
    *June 2022 – August 2022*  
    - Supported the Grande Boutique team in planning and executing the Spring/Summer product launch event  
    - Conducted competitive benchmarking and consumer surveys; synthesized findings into presentation decks  
    - Coordinated social media teasers, resulting in a 15% increase in Instagram engagement  

    **Brand Management Intern, Chanel**  
    *February 2024 – May 2024*  
    - Localized global beauty campaigns for the Hong Kong market  
    - Assisted in organizing influencer relations and store activations during Lunar New Year, driving a 10% uplift in foot traffic  
    - Analyzed weekly sales data and customer feedback to refine in-store merchandising layouts  

    **Digital Marketing Intern, L’Oréal Groupe**  
    *July 2021 – September 2021*  
    - Created content calendars and managed paid-social campaigns for Lancôme and Kiehl’s on Facebook and WeChat  
    - Monitored KPIs and optimized ad spend, improving ROI by 12%  
    - Produced monthly performance reports and recommended A/B testing ideas  
    """)

    # ─────────────────────────────
    # EDUCATION
    # ─────────────────────────────
    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**  
    HEC Paris, France | *Sep 2023 – Jun 2025*  
    - GPA: 3.8/4.0  

    **MSc in Marketing (Exchange Semester)**  
    CUHK Business School, Hong Kong | *Jan 2024 – May 2024*  

    **Bachelor of Business Administration – Marketing Track**  
    ESSEC Business School, France | *Sep 2019 – Jun 2023*  
    - Graduated with Distinction; Honors thesis: “The Evolution of Omnichannel Luxury Retail in Post-Pandemic Europe”  
    """)

    # ─────────────────────────────
    # SKILLS
    # ─────────────────────────────
    st.header("Skills")
    st.markdown("""
    - **Marketing Tools:** Google Analytics · SEMrush · Hootsuite · Salesforce Marketing Cloud  
    - **Data & Analytics:** Excel (Pivot Tables, VLOOKUP) · SPSS · Tableau  
    - **Digital Marketing:** Meta Ads Manager · WeChat Ads · Paid Social Campaigns  
    - **Brand Strategy:** Strategic Brand Communications · Competitive Benchmarking · Consumer Surveys  
    - **Design & Visual:** Canva  
    """)

    # ─────────────────────────────
    # CERTIFICATIONS
    # ─────────────────────────────
    st.header("Certifications")
    st.markdown("""
    - Google Analytics 4 IQ (Mar 2024)  
    - Meta Blueprint – Digital Marketing Associate (Jul 2023)  
    - HubSpot Inbound Marketing (Apr 2023)  
    """)

    # ─────────────────────────────
    # PROJECTS
    # ─────────────────────────────
    st.header("Projects")
    st.markdown("""
    **Live-Streaming Engagement Strategies for Beauty Brands in China**  
    - Developed a social listening pipeline scraping Douyin & Weibo (20k posts/week)  
    - Performed sentiment analysis and topic modelling to identify top engagement drivers  
    - Presented insights to L’Oréal HK marketing team to inform Q3 campaign strategy  

    **The Evolution of Omnichannel Luxury Retail in Post-Pandemic Europe**  
    - Conducted qualitative interviews (n = 20 executives) and secondary data analysis  
    - Mapped consumer journey across online and offline touchpoints  
    - Awarded Distinction; presented at ESSEC Luxury Lab 2023  
    """)

    # ─────────────────────────────
    # LANGUAGES & INTERESTS
    # ─────────────────────────────
    st.header("Languages")
    st.markdown("""
    - Mandarin (Native)  
    - English (Fluent)  
    - French (Advanced)  
    """)

    st.header("Interests")
    st.markdown("""
    - Trend forecasting in fashion and beauty  
    - Travel photography  
    - Running (Paris Half-Marathon 2023 finisher)  
    """)

    st.markdown("---")
