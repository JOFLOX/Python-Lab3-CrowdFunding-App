import streamlit as st

def home():
            # Hero Section
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <h1 style="color: #1f77b4; font-size: 3rem; margin-bottom: 1rem;">🚀 Welcome to CrowdFund</h1>
            <h3 style="color: #666; font-weight: 300; margin-bottom: 2rem;">Turn Your Dreams Into Reality</h3>
        </div>
        """, unsafe_allow_html=True)

        # Main value proposition
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white; padding: 2rem; border-radius: 15px; margin: 2rem 0;">
                <h2>🌟 Bring Ideas to Life Through Community Support</h2>
                <p style="font-size: 1.2rem; margin: 1rem 0;">
                    Whether you're an innovator with a groundbreaking idea or a supporter looking to back the next big thing,
                    CrowdFund connects dreamers with believers.
                </p>
            </div>
            """, unsafe_allow_html=True)

        # Features section
        st.markdown("## 🎯 Why Choose CrowdFund?")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            ### 💡 For Creators
            - **Easy Project Setup**: Launch your campaign in minutes
            - **Flexible Funding**: Set your own goals and timelines
            - **Real-time Analytics**: Track your progress with detailed insights
            - **Community Engagement**: Connect directly with your supporters
            """)

        with col2:
            st.markdown("""
            ### 🤝 For Backers
            - **Discover Innovation**: Explore cutting-edge projects
            - **Secure Transactions**: Safe and protected funding process
            - **Early Access**: Get exclusive rewards and early bird offers
            - **Impact Tracking**: See how your support makes a difference
            """)

        with col3:
            st.markdown("""
            ### 🛡️ Trust & Security
            - **Verified Projects**: All campaigns are reviewed and verified
            - **Transparent Process**: Clear funding goals and progress tracking
            - **Secure Payments**: Industry-standard security protocols
            - **Community Reviews**: Peer feedback and rating system
            """)

        # Statistics section
        st.markdown("---")
        st.markdown("## 📊 Platform Impact")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Projects Funded", "1,250+", "↗️ 15%")
        with col2:
            st.metric("Total Raised", "$2.8M", "↗️ 23%")
        with col3:
            st.metric("Active Backers", "15,000+", "↗️ 8%")
        with col4:
            st.metric("Success Rate", "78%", "↗️ 5%")

        # Call to action
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background-color: #f8f9fa; border-radius: 10px;">
                <h3 style="color: #333;">Ready to Get Started?</h3>
                <p style="color: #666; margin-bottom: 1.5rem;">
                    Join thousands of creators and backers who are already making dreams come true.
                </p>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🚀 Start a Project", use_container_width=True, type="primary"):
                    st.info("👆 Please register or login first to create a project!")
            with col_b:
                if st.button("🔍 Explore Projects", use_container_width=True):
                    st.info("👆 Please register or login first to view projects!")

        # Footer info
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; padding: 1rem;">
            <p><strong>New to CrowdFund?</strong> Register for a free account to start creating or backing projects today!</p>
            <p><strong>Already have an account?</strong> Login to access your dashboard and manage your projects.</p>
        </div>
        """, unsafe_allow_html=True)