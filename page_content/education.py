import streamlit as st


def education_page():
    # ─────────────────────────────
    # EDUCATION
    # ─────────────────────────────
    st.markdown("## Education")

    st.markdown("""
    ### Master of Science in Marketing  
    **HEC Paris (Paris, France)** | *Sep 2023 – Jun 2025*  

    - GPA: 3.8/4.0  

    ### MSc in Marketing (Exchange Semester)  
    **CUHK Business School (Hong Kong, SAR)** | *Jan 2024 – May 2024*  

    - Focus: APAC Beauty & Skincare Markets · Digital Analytics  

    ### Bachelor of Business Administration – Marketing Track  
    **ESSEC Business School (Cergy-Pontoise, France)** | *Sep 2019 – Jun 2023*  

    - Graduated **with Distinction** · Honors thesis: “The Evolution of Omnichannel Luxury Retail in Post-Pandemic Europe”  
    """)

    st.markdown("---")

    # ─────────────────────────────
    # CERTIFICATIONS
    # ─────────────────────────────
    st.markdown("## Certifications")

    cert1, cert2, cert3 = st.columns(3)

    with cert1:
        st.markdown("""
        ### Google Analytics 4 IQ  
        *Issued Mar 2024*  
        """)
    with cert2:
        st.markdown("""
        ### Meta Blueprint – Digital Marketing Associate  
        *Issued Jul 2023*  
        """)
    with cert3:
        st.markdown("""
        ### HubSpot Inbound Marketing  
        *Issued Apr 2023*  
        """)

    st.markdown("---")

    # ─────────────────────────────
    # ACADEMIC PROJECTS
    # ─────────────────────────────
    st.markdown("## Academic Projects")

    st.markdown("""
    ### “Live-Streaming Engagement Strategies for Beauty Brands in China”  
    - Conducted social listening pipeline scraping Douyin & Weibo (20k posts/week)  
    - Performed sentiment analysis and topic modelling to identify top engagement drivers  
    - Presented findings to L’Oréal HK marketing team, informing Q3 campaign strategy   

    ### “The Evolution of Omnichannel Luxury Retail in Post-Pandemic Europe”  
    - Honors thesis based on qualitative interviews (n = 20 executives) and secondary data  
    - Analyzed consumer journey across online and offline touchpoints  
    - Awarded Distinction and presented at ESSEC Luxury Lab 2023  
    """)

    st.markdown("---")
