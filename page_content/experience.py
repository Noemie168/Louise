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
    with st.expander("Interactive Data Visualization", expanded=False):
        st.markdown("**Description:** Select an internship or project to view its KPI chart and download the data as CSV.")

        # Prepare datasets and charts

        # Chanel internship data
        chanel_data = pd.DataFrame({
            'Month': ['Feb', 'Mar', 'Apr', 'May'],
            'Foot Traffic Uplift (%)': [5, 8, 10, 10]
        })
        chanel_chart = alt.Chart(chanel_data).mark_line(point=True).encode(
            x=alt.X('Month:N', title='Month'),
            y=alt.Y('Foot Traffic Uplift (%):Q', title='Uplift (%)'),
            tooltip=['Month', 'Foot Traffic Uplift (%)']
        )

        # Louis Vuitton internship data
        lv_data = pd.DataFrame({
            'Week': ['W1', 'W2', 'W3', 'W4'],
            'Engagement Rate (%)': [12, 14, 15, 15]
        })
        lv_chart = alt.Chart(lv_data).mark_area(opacity=0.6).encode(
            x=alt.X('Week:N', title='Week'),
            y=alt.Y('Engagement Rate (%):Q', title='Engagement (%)'),
            tooltip=['Week', 'Engagement Rate (%)']
        )

        # L'Oréal internship data
        loreal_data = pd.DataFrame({
            'Phase': ['Planning', 'Launch', 'Optimization'],
            'ROI Improvement (%)': [5, 8, 12]
        })
        loreal_chart = alt.Chart(loreal_data).mark_bar().encode(
            x=alt.X('ROI Improvement (%):Q', title='Improvement (%)'),
            y=alt.Y('Phase:N', sort='-x', title='Phase'),
            tooltip=['Phase', 'ROI Improvement (%)']
        )

        # Live-Streaming project data
        sent_df = pd.DataFrame({
            'Sentiment': ['Positive', 'Neutral', 'Negative'],
            'Percentage': [65, 25, 10]
        })
        sent_chart = alt.Chart(sent_df).mark_arc(innerRadius=30).encode(
            theta=alt.Theta('Percentage:Q', title=''),
            color=alt.Color('Sentiment:N', scale=alt.Scale(range=['#4CAF50','#FFC107','#F44336'])),
            tooltip=['Sentiment', 'Percentage']
        )

        # Omnichannel audit project data
        om_df = pd.DataFrame({
            'Metric': ['Online Path Completion', 'In-Store Conversion', 'Cart Abandonment'],
            'Value (%)': [80, 30, 20]
        })
        om_chart = alt.Chart(om_df).mark_bar().encode(
            x=alt.X('Value (%):Q', title='Percentage (%)'),
            y=alt.Y('Metric:N', sort='-x', title=None),
            tooltip=['Metric', 'Value (%)']
        )

        # AR Try-On A/B Test project data
        ab_df = pd.DataFrame([
            {'Variant': 'Static', 'CTR (%)': 8, 'Add-to-Cart (%)': 10},
            {'Variant': 'AR', 'CTR (%)': 22, 'Add-to-Cart (%)': 24}
        ])
        ab_long = ab_df.melt(id_vars=['Variant'], var_name='Metric', value_name='Value')
        ab_chart = alt.Chart(ab_long).mark_bar().encode(
            x=alt.X('Value:Q', title='Percentage (%)'),
            y=alt.Y('Variant:N', title=None),
            color='Metric:N',
            tooltip=['Variant', 'Metric', 'Value']
        )

        # Map selections to data and charts
        options = {
            'Chanel Foot Traffic': (chanel_data, chanel_chart),
            'LV Instagram Engagement': (lv_data, lv_chart),
            "L'Oréal ROI Improvement": (loreal_data, loreal_chart),
            'Live-Stream Sentiment': (sent_df, sent_chart),
            'Omnichannel Audit': (om_df, om_chart),
            'AR Try-On A/B Test': (ab_long, ab_chart)
        }

        choice = st.selectbox('Select a dataset', list(options.keys()))
        df, chart = options[choice]
        st.altair_chart(chart, use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Download CSV',
            data=csv,
            file_name=f"{choice.replace(' ','_')}.csv",
            mime='text/csv'
        )

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
