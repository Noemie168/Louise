import streamlit as st


def contact_page():
    st.markdown("## Contact Me")
    
    st.markdown("""
    Feel free to reach out to me through any of the following channels:
    
    ### Direct Contact
    - **Email**: [Lewis.liu@email.com](mailto:Lewis.liu@email.com)
    - **Phone**: +33 6 12 34 56 78
    - **LinkedIn**: [linkedin.com/in/Lewisliu](https://linkedin.com/in/Lewisliu)
    """)
    
    st.markdown("### Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # Here you could integrate an email service or database to store messages
    
    st.markdown("---")
    
    st.markdown("""
    ### Availability
    I’m generally available for virtual meetings Monday through Friday,
    9 AM to 5 PM Central European Time (CET).
    Please email me to schedule a call or video conference.
    """)
