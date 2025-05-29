import streamlit as st
from components.interactive import display_interactive_chart


def experience_page():
    # ─────────────────────────────
    # PROFESSIONAL EXPERIENCE
    # ─────────────────────────────
    st.markdown("## Professional Experience")

    # — Brand Management Intern, Chanel —
    st.markdown("""
    ### Brand Management Intern  
    **Chanel** | *Feb 2024 – May 2024 · Hong Kong, SAR*  

    - Localized global beauty campaigns for the Hong Kong market  
    - Organized influencer relations and store activations during Lunar New Year, driving a 10% uplift in foot traffic  
    - Analyzed weekly sales data and customer feedback to optimize in-store merchandising layouts  
    """)

    # — Marketing Intern, Louis Vuitton —
    st.markdown("""
    ### Marketing Intern  
    **Louis Vuitton** | *Jun 2022 – Aug 2022 · Paris, France*  

    - Supported the Grande Boutique team in planning and executing the Spring/Summer product launch  
    - Conducted competitive benchmarking and consumer surveys; synthesized insights into executive presentation decks  
    - Coordinated social media teasers, boosting Instagram engagement by 15% during campaign period  
    """)

    # — Digital Marketing Intern, L’Oréal Groupe —
    st.markdown("""
    ### Digital Marketing Intern  
    **L’Oréal Groupe** | *Jul 2021 – Sep 2021 · Paris, France*  

    - Developed content calendars and managed paid-social campaigns for Lancôme and Kiehl’s on Facebook and WeChat  
    - Monitored campaign KPIs and optimized ad spend to improve ROI by 12%  
    - Generated monthly performance reports and proposed A/B testing initiatives to enhance click-through rates  
    """)

    st.markdown("---")

    # ─────────────────────────────
    # SELECTED PROJECTS
    # ─────────────────────────────
    st.markdown("## Selected Projects")

    projects = [
        {
            "title": "Live-Streaming Engagement Strategies for Beauty Brands in China",
            "description": "Built a social-listening pipeline scraping Douyin & Weibo (20k posts/week) and performed sentiment analysis to identify top engagement drivers.",
            "skills": ["Python", "Topic Modeling", "Social Listening", "Power BI"],
            "outcome": "Presented insights to L’Oréal HK marketing team, informing Q3 campaign strategy."
        },
        {
            "title": "Omnichannel Retail Audit for LV Spring/Summer Launch",
            "description": "Conducted competitor and customer journey assessments across online and offline touchpoints for a Spring/Summer product rollout.",
            "skills": ["Excel", "Consumer Surveys", "Benchmarking", "Presentation"],
            "outcome": "Shared findings with senior management to refine channel activation plans."
        },
        {
            "title": "AR Try-On Conversion A/B Test",
            "description": "Designed and executed A/B test comparing virtual try-on vs static images for a lip product campaign.",
            "skills": ["GA4", "Optimizely", "R", "Statistical Analysis"],
            "outcome": "Identified a 14% lift in add-to-cart rate for the AR variant."
        }
    ]

    for i, proj in enumerate(projects):
        with st.expander(proj["title"], expanded=i == 0):
            st.markdown(f"**Description:** {proj['description']}")
            st.markdown(f"**Skills Used:** {', '.join(proj['skills'])}")
            st.markdown(f"**Outcome:** {proj['outcome']}")

    # 示例交互图表 – 可删除
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** Sample interactive chart used in insights sharing.")
        display_interactive_chart()

    st.markdown("---")

    # ─────────────────────────────
    # PROFESSIONAL SKILLS
    # ─────────────────────────────
    st.markdown("## Professional Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Marketing & Analytics  
        - **Research:** Qualtrics · SPSS · Conjoint Analysis  
        - **Data & BI:** Excel (Pivot Tables, VLOOKUP) · SPSS · Tableau  
        - **Digital Marketing:** Meta Ads Manager · WeChat Ads · Paid Social Campaigns  
        - **Visual:** Canva  
        """)

    with col2:
        st.markdown("""
        ### Soft Skills  
        - **Storytelling:** Data-driven narratives for executive audiences  
        - **Multicultural Collaboration:** Experience in 🇫🇷 🇭🇰 environments  
        - **Languages:** Mandarin (Native) · English (Fluent) · French (Advanced)  
        - **Leadership:** Organized workshops for HEC Marketing Club and led teams to case competition wins  
        """)

    st.markdown("---")
