import streamlit as st

st.set_page_config(
    page_title="Comms Tools",
    layout="wide",
    page_icon="📬"
)

email_map_page = st.Page(
    "pages/email_map.py",
    title="Email Map",
    url_path="email-map",
    icon="🗺️"
)
email_builder_page = st.Page(
    "pages/email_builder.py",
    title="Email Builder",
    url_path="email-builder",
    icon="✉️"
)

pg = st.navigation(
    [email_map_page, email_builder_page],
    position="hidden"
)

# Only render the home page when we're at the root (no sub-page selected)
if pg.url_path == "" or pg.url_path is None:
    st.markdown("""
        <style>
            .block-container { padding-top: 3rem; }

            .home-title {
                font-size: 2rem;
                font-weight: 700;
                color: #111;
                margin-bottom: 0.25rem;
            }
            .home-subtitle {
                font-size: 1rem;
                color: #666;
                margin-bottom: 2.5rem;
            }
            .tile-card {
                border: 1px solid #e5e7eb;
                border-radius: 12px;
                padding: 2rem;
                background: #fff;
                transition: box-shadow 0.2s ease, transform 0.2s ease;
                cursor: pointer;
                height: 100%;
            }
            .tile-card:hover {
                box-shadow: 0 8px 24px rgba(0,0,0,0.09);
                transform: translateY(-2px);
            }
            .tile-icon { font-size: 2.5rem; margin-bottom: 0.75rem; }
            .tile-title {
                font-size: 1.15rem;
                font-weight: 600;
                color: #111;
                margin-bottom: 0.4rem;
            }
            .tile-desc {
                font-size: 0.875rem;
                color: #6b7280;
                line-height: 1.5;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="home-title">📬 Comms Tools</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-subtitle">Internal tools for communication workflows at noon.</div>', unsafe_allow_html=True)

    col1, col2, _ = st.columns([1, 1, 2])

    with col1:
        st.markdown("""
            <div class="tile-card">
                <div class="tile-icon">🗺️</div>
                <div class="tile-title">Email Map</div>
                <div class="tile-desc">Visualise and navigate your email communication structure across teams and workflows.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        if st.button("Open Email Map →", key="go_email_map", use_container_width=True):
            st.switch_page(email_map_page)

    with col2:
        st.markdown("""
            <div class="tile-card">
                <div class="tile-icon">✉️</div>
                <div class="tile-title">Email Builder</div>
                <div class="tile-desc">Build and customise email templates for DSE communications and seller outreach.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        if st.button("Open Email Builder →", key="go_email_builder", use_container_width=True):
            st.switch_page(email_builder_page)

pg.run()
