import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Comms Tools", layout="wide", page_icon="📬")

components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
  body { background: transparent; padding: 0 0 1rem; }

  .hero-label { font-size: 11px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: #9ca3af; margin-bottom: 6px; }
  .hero-title { font-size: 26px; font-weight: 600; color: #f9fafb; margin: 0 0 6px; }
  .hero-sub { font-size: 14px; color: #9ca3af; margin: 0 0 2rem; }

  .tile-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 2rem; max-width: 720px; }

  .tile {
    background: #1e1e1e;
    border: 1px solid #2d2d2d;
    border-radius: 14px;
    padding: 1.4rem;
    display: flex; flex-direction: column; gap: 1rem;
    cursor: pointer;
    transition: border-color 0.15s;
    text-decoration: none;
  }
  .tile:hover { border-color: #444; }

  .tile-header { display: flex; align-items: flex-start; justify-content: space-between; }
  .tile-icon-wrap {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 19px;
  }
  .tile-icon-wrap.map  { background: #0d3326; color: #34d399; }
  .tile-icon-wrap.builder { background: #0c2240; color: #60a5fa; }
  .arrow { color: #4b5563; font-size: 17px; }

  .tile-title { font-size: 15px; font-weight: 600; color: #f3f4f6; margin-bottom: 4px; }
  .tile-desc  { font-size: 13px; color: #9ca3af; line-height: 1.6; }

  .tile-footer { display: flex; gap: 6px; flex-wrap: wrap; }
  .tag {
    font-size: 11px; padding: 3px 9px; border-radius: 100px;
    background: #2a2a2a; color: #9ca3af; border: 1px solid #333;
  }

  .divider { border: none; border-top: 1px solid #2d2d2d; margin: 0 0 1.4rem; }

  .section-label { font-size: 11px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: #6b7280; margin-bottom: 12px; }

  .shortcut-row { display: flex; gap: 10px; flex-wrap: wrap; }
  .shortcut {
    display: inline-flex; align-items: center; gap: 7px;
    background: #1a1a1a; border: 1px solid #2d2d2d; border-radius: 8px;
    padding: 8px 14px; font-size: 13px; color: #9ca3af; cursor: pointer;
    text-decoration: none;
  }
  .shortcut:hover { border-color: #444; color: #e5e7eb; }
  .shortcut i { font-size: 15px; }
</style>
</head>
<body>
  <p class="hero-label">noon seller comms</p>
  <h1 class="hero-title">Comms Tools</h1>
  <p class="hero-sub">Internal tools for communication workflows at noon.</p>

  <div class="tile-grid">
    <div class="tile" id="map-tile">
      <div class="tile-header">
        <div class="tile-icon-wrap map"><i class="ti ti-map-2"></i></div>
        <i class="ti ti-arrow-up-right arrow"></i>
      </div>
      <div>
        <p class="tile-title">Email Map</p>
        <p class="tile-desc">Visualise and navigate your full email communication structure across teams and workflows.</p>
      </div>
      <div class="tile-footer">
        <span class="tag">Templates</span>
        <span class="tag">Journeys</span>
        <span class="tag">Filters</span>
      </div>
    </div>

    <div class="tile" id="builder-tile">
      <div class="tile-header">
        <div class="tile-icon-wrap builder"><i class="ti ti-mail-forward"></i></div>
        <i class="ti ti-arrow-up-right arrow"></i>
      </div>
      <div>
        <p class="tile-title">Email Builder</p>
        <p class="tile-desc">Build and customise email templates for DSE seller communications and outreach campaigns.</p>
      </div>
      <div class="tile-footer">
        <span class="tag">DSE</span>
        <span class="tag">Onboarding</span>
        <span class="tag">Outreach</span>
      </div>
    </div>
  </div>

  <hr class="divider">
  <p class="section-label">Quick access</p>
  <div class="shortcut-row">
    <a class="shortcut" id="sc-map"><i class="ti ti-map-2"></i> Email Map</a>
    <a class="shortcut" id="sc-builder"><i class="ti ti-mail-forward"></i> Email Builder</a>
    <a class="shortcut" href="https://www.noon.com" target="_blank"><i class="ti ti-external-link"></i> noon Seller Portal</a>
  </div>
</body>
</html>
""", height=480, scrolling=False)

# Streamlit navigation buttons (hidden visually under the HTML, triggered by tile clicks isn't possible cross-frame,
# so we keep clean labelled buttons as the nav mechanism)
st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
col1, col2, _ = st.columns([1, 1, 2])
with col1:
    if st.button("Open Email Map →", use_container_width=True):
        st.switch_page("pages/email_map.py")
with col2:
    if st.button("Open Email Builder →", use_container_width=True):
        st.switch_page("pages/email_builder.py")
