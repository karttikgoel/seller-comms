import streamlit as st

st.set_page_config(page_title="Comms Tools", layout="wide", page_icon="📬")

st.markdown("""
<style>
@import url('https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css');

.block-container { padding-top: 3rem !important; max-width: 860px !important; }

.hero-label {
    font-size: 11px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #9ca3af; margin-bottom: 4px;
}
.hero-title {
    font-size: 28px; font-weight: 600; color: #111827;
    margin: 0 0 6px; line-height: 1.2;
}
.hero-sub { font-size: 14px; color: #6b7280; margin: 0 0 2rem; }

.tile-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 2rem; }

.tile {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1.5rem;
    display: flex; flex-direction: column; gap: 1rem;
    transition: border-color 0.15s, box-shadow 0.15s;
}
.tile:hover { border-color: #d1d5db; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }

.tile-header { display: flex; align-items: flex-start; justify-content: space-between; }
.tile-icon-wrap {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 20px;
}
.tile-icon-wrap.map { background: #E1F5EE; color: #0F6E56; }
.tile-icon-wrap.builder { background: #E6F1FB; color: #185FA5; }
.ti-arrow-up-right { color: #9ca3af; font-size: 18px; }

.tile-title { font-size: 15px; font-weight: 600; color: #111827; margin: 0 0 4px; }
.tile-desc { font-size: 13px; color: #6b7280; line-height: 1.6; margin: 0; }

.tile-footer { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.tile-tag {
    font-size: 11px; padding: 3px 8px; border-radius: 100px;
    background: #f3f4f6; color: #6b7280;
    border: 1px solid #e5e7eb;
}

.divider { border: none; border-top: 1px solid #f3f4f6; margin: 0 0 1.5rem; }
.section-label {
    font-size: 11px; font-weight: 500; letter-spacing: 0.08em;
    text-transform: uppercase; color: #9ca3af; margin-bottom: 12px;
}
.shortcut-row { display: flex; gap: 10px; flex-wrap: wrap; }
.shortcut {
    display: inline-flex; align-items: center; gap: 8px;
    background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px;
    padding: 8px 14px; font-size: 13px; color: #374151;
    text-decoration: none;
}
.shortcut:hover { background: #f3f4f6; border-color: #d1d5db; }
</style>

<div>
    <p class="hero-label">noon seller comms</p>
    <h1 class="hero-title">Comms Tools</h1>
    <p class="hero-sub">Internal tools for communication workflows at noon.</p>

    <div class="tile-grid">
        <div class="tile">
            <div class="tile-header">
                <div class="tile-icon-wrap map">
                    <i class="ti ti-map-2"></i>
                </div>
                <i class="ti ti-arrow-up-right"></i>
            </div>
            <div>
                <p class="tile-title">Email Map</p>
                <p class="tile-desc">Visualise and navigate your full email communication structure across teams and workflows.</p>
            </div>
            <div class="tile-footer">
                <span class="tile-tag">Templates</span>
                <span class="tile-tag">Journeys</span>
                <span class="tile-tag">Filters</span>
            </div>
        </div>

        <div class="tile">
            <div class="tile-header">
                <div class="tile-icon-wrap builder">
                    <i class="ti ti-mail-forward"></i>
                </div>
                <i class="ti ti-arrow-up-right"></i>
            </div>
            <div>
                <p class="tile-title">Email Builder</p>
                <p class="tile-desc">Build and customise email templates for DSE seller communications and outreach campaigns.</p>
            </div>
            <div class="tile-footer">
                <span class="tile-tag">DSE</span>
                <span class="tile-tag">Onboarding</span>
                <span class="tile-tag">Outreach</span>
            </div>
        </div>
    </div>

    <hr class="divider">
    <p class="section-label">Quick access</p>
    <div class="shortcut-row">
        <span class="shortcut"><i class="ti ti-map-2"></i> Email Map</span>
        <span class="shortcut"><i class="ti ti-mail-forward"></i> Email Builder</span>
        <span class="shortcut"><i class="ti ti-external-link"></i> noon Seller Portal</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

col1, col2, _ = st.columns([1, 1, 2])
with col1:
    if st.button("Open Email Map", use_container_width=True):
        st.switch_page("pages/email_map.py")
with col2:
    if st.button("Open Email Builder", use_container_width=True):
        st.switch_page("pages/email_builder.py")
