import streamlit as st
import pandas as pd
import altair as alt


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
    - Coordinated social media teasers, boosting Instagram engagement by 15% during the campaign period  
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
            "description": "Conducted competitor and customer journey assessments across online and offline touchpoints.",
            "skills": ["Excel", "Consumer Surveys", "Benchmarking", "Presentation"],
            "outcome": "Shared findings with senior management to refine channel activation plans."
        },
        {
            "title": "AR Try-On Conversion A/B Test",
            "description": "Designed and executed A/B test for virtual try-on vs static images.",
            "skills": ["GA4", "Optimizely", "R", "Statistical Analysis"],
            "outcome": "Identified a 14% lift in add-to-cart rate for the AR variant."
        }
    ]

    for i, proj in enumerate(projects):
        with st.expander(proj["title"], expanded=(i == 0)):
            st.markdown(f"**Description:** {proj['description']}")
            st.markdown(f"**Skills Used:** {', '.join(proj['skills'])}")
            st.markdown(f"**Outcome:** {proj['outcome']}")

    st.markdown("---")

    # ─────────────────────────────
    # INTERACTIVE DATA VISUALIZATION
    # ─────────────────────────────
    with st.expander("Interactive Data Visualization ", expanded=False):
        st.markdown("**Description:** Key KPI trends for each internship role.")

        # Chanel: Monthly Foot Traffic Uplift
        chanel_data = pd.DataFrame({
            'Month': ['Feb', 'Mar', 'Apr', 'May'],
            'Foot Traffic Uplift (%)': [5, 8, 10, 10]
        })
        chanel_chart = alt.Chart(chanel_data).mark_line(point=True).encode(
            x=alt.X('Month:N', title='Month'),
            y=alt.Y('Foot Traffic Uplift (%):Q', title='Uplift (%)'),
            tooltip=['Month', 'Foot Traffic Uplift (%)']
        ).properties(title='Chanel Foot Traffic Uplift', width=200, height=200)

        # Louis Vuitton: Weekly Instagram Engagement Rate
        lv_data = pd.DataFrame({
            'Week': ['W1', 'W2', 'W3', 'W4'],
            'Engagement Rate (%)': [12, 14, 15, 15]
        })
        lv_chart = alt.Chart(lv_data).mark_area(opacity=0.6).encode(
            x=alt.X('Week:N', title='Week'),
            y=alt.Y('Engagement Rate (%):Q', title='Engagement (%)'),
            tooltip=['Week', 'Engagement Rate (%)']
        ).properties(title='LV Instagram Engagement Rate', width=200, height=200)

        # L'Oréal: ROI Improvement by Campaign Phase
        loreal_data = pd.DataFrame({
            'Phase': ['Planning', 'Launch', 'Optimization'],
            'ROI Improvement (%)': [5, 8, 12]
        })
        loreal_chart = alt.Chart(loreal_data).mark_bar().encode(
            x=alt.X('ROI Improvement (%):Q', title='Improvement (%)'),
            y=alt.Y('Phase:N', sort='-x', title='Campaign Phase'),
            tooltip=['Phase', 'ROI Improvement (%)']
        ).properties(title="L'Oréal ROI Improvement", width=200, height=200)

        # Display charts side by side
        combined = alt.hconcat(chanel_chart, lv_chart, loreal_chart).resolve_scale(y='independent')
        st.altair_chart(combined, use_container_width=True)

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
