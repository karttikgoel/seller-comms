import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Comms Tools", layout="wide", page_icon="📬")

# Theme state
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# Kill Streamlit footer and tighten container
st.markdown("""
<style>
  .block-container {
    padding-top: 1rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
  }
  footer { display: none !important; }
  [data-testid="stBottom"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Streamlit native top bar ──────────────────────────────
col_title, col_toggle = st.columns([9, 1])
with col_title:
    st.markdown("""
      <div style="line-height:1.3; margin-bottom: 4px;">
        <span style="font-size:10px; font-weight:500; letter-spacing:0.1em; text-transform:uppercase; color:#6b7280;">
          noon seller comms
        </span><br>
        <span style="font-size:22px; font-weight:700;">Comms Tools</span><br>
        <span style="font-size:12px; color:#9ca3af;">Internal tools for communication workflows at noon.</span>
      </div>
    """, unsafe_allow_html=True)

with col_toggle:
    label = "☀️ Light" if st.session_state.theme == "dark" else "🌙 Dark"
    if st.button(label, use_container_width=True):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()

theme = st.session_state.theme

# ── iframe: only sections, no hero ───────────────────────
components.html(f"""
<!DOCTYPE html>
<html data-theme="{theme}">
<head>
<link rel="stylesheet" href="https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
<style>
  [data-theme="dark"] {{
    --bg:             #0e0e0e;
    --surface:        #1a1a1a;
    --surface-deep:   #111;
    --border:         #2d2d2d;
    --border-hover:   #555;
    --text-primary:   #f3f4f6;
    --text-secondary: #9ca3af;
    --text-muted:     #4b5563;
    --section-label:  #c9d1db;
    --copy-bg:        #1e1e1e;
  }}
  [data-theme="light"] {{
    --bg:             #f5f5f5;
    --surface:        #ffffff;
    --surface-deep:   #f9fafb;
    --border:         #e5e7eb;
    --border-hover:   #9ca3af;
    --text-primary:   #111827;
    --text-secondary: #6b7280;
    --text-muted:     #9ca3af;
    --section-label:  #1f2937;
    --copy-bg:        #f3f4f6;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
  html, body {{ background: var(--bg); }}
  body {{ padding: 4px 20px 24px; display: flex; flex-direction: column; gap: 18px; }}

  .section {{ display: flex; flex-direction: column; gap: 10px; }}
  .section-header {{
    display: flex; align-items: center; gap: 8px;
    padding-bottom: 6px; border-bottom: 1px solid var(--border);
  }}
  .section-icon {{ font-size: 15px; }}
  .section-icon.comms  {{ color: #6b7280; }}
  .section-icon.help   {{ color: #7c3aed; }}
  .section-icon.ticket {{ color: #0284c7; }}
  .section-label {{
    font-size: 13px; font-weight: 700;
    letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--section-label);
  }}

  .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }}

  .tile {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
    padding: 16px; display: flex; flex-direction: column; gap: 10px;
    text-decoration: none; transition: border-color 0.15s, box-shadow 0.15s;
  }}
  .tile:hover {{ border-color: var(--border-hover); box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
  .tile-top {{ display: flex; align-items: flex-start; justify-content: space-between; }}
  .tile-icon {{
    width: 36px; height: 36px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center; font-size: 17px; flex-shrink: 0;
  }}
  .tile-icon.map     {{ background: #0d3326; color: #34d399; }}
  .tile-icon.builder {{ background: #0c2240; color: #60a5fa; }}
  .tile-icon.mail    {{ background: #2d1a00; color: #f59e0b; }}
  .tile-icon.help    {{ background: #1c1040; color: #a78bfa; }}
  .tile-icon.ticket  {{ background: #001e2d; color: #38bdf8; }}
  .arrow      {{ color: var(--text-muted); font-size: 15px; }}
  .tile-title {{ font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; }}
  .tile-desc  {{ font-size: 12px; color: var(--text-secondary); line-height: 1.55; }}

  .launcher {{
    background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
    padding: 16px; display: flex; flex-direction: column; gap: 10px;
  }}
  .launcher-desc {{ font-size: 12px; color: var(--text-secondary); line-height: 1.55; }}

  .link-list {{ display: flex; flex-direction: column; gap: 6px; margin-top: 2px; }}
  .link-item {{
    display: flex; align-items: center; justify-content: space-between;
    background: var(--surface-deep); border: 1px solid var(--border); border-radius: 8px;
    padding: 9px 12px; text-decoration: none; transition: border-color 0.15s; gap: 8px;
  }}
  .link-item:hover {{ border-color: var(--border-hover); }}
  .link-item-left {{ display: flex; align-items: center; gap: 8px; }}
  .link-item-row {{
    display: flex; align-items: center;
    background: var(--surface-deep); border: 1px solid var(--border); border-radius: 8px;
    padding: 9px 12px; gap: 8px; transition: border-color 0.15s;
  }}
  .link-item-row:hover {{ border-color: var(--border-hover); }}
  .link-anchor {{ display: flex; align-items: center; gap: 8px; text-decoration: none; flex: 1; min-width: 0; }}
  .dot        {{ width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }}
  .dot-mail   {{ background: #f59e0b; }}
  .dot-help   {{ background: #a78bfa; }}
  .dot-ticket {{ background: #38bdf8; }}
  .link-name  {{ font-size: 13px; color: var(--text-primary); font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .link-ext   {{ color: var(--text-muted); font-size: 13px; flex-shrink: 0; }}
  .link-actions {{ display: flex; align-items: center; gap: 5px; flex-shrink: 0; }}
  .copy-btn {{
    display: flex; align-items: center; justify-content: center;
    width: 24px; height: 24px; border-radius: 6px;
    background: var(--copy-bg); border: 1px solid var(--border);
    color: var(--text-muted); cursor: pointer; font-size: 12px;
    transition: all 0.15s; outline: none; flex-shrink: 0;
  }}
  .copy-btn:hover {{ border-color: var(--border-hover); color: var(--text-primary); }}
  .copy-btn.copied {{ background: #0d3326; color: #34d399; border-color: #1a5c40; }}
</style>
</head>
<body>

  <!-- Comms Tools -->
  <div class="section">
    <div class="section-header">
      <i class="ti ti-tools section-icon comms"></i>
      <span class="section-label">Comms Tools</span>
    </div>
    <div class="grid-3">
      <a class="tile" href="/email-map" target="_top">
        <div class="tile-top">
          <div class="tile-icon map"><i class="ti ti-map-2"></i></div>
          <i class="ti ti-arrow-up-right arrow"></i>
        </div>
        <p class="tile-title">Email Map</p>
        <p class="tile-desc">Visualise and navigate your full email communication structure across teams.</p>
      </a>
      <a class="tile" href="/email-builder" target="_top">
        <div class="tile-top">
          <div class="tile-icon builder"><i class="ti ti-mail-forward"></i></div>
          <i class="ti ti-arrow-up-right arrow"></i>
        </div>
        <p class="tile-title">Email Builder</p>
        <p class="tile-desc">Build and customise email templates for DSE seller communications and outreach.</p>
      </a>
      <div class="launcher">
        <div class="tile-icon mail" style="margin-bottom:4px"><i class="ti ti-send"></i></div>
        <p class="tile-title">Mail Deployment</p>
        <p class="launcher-desc">Send and manage campaigns via noon's mailing infrastructure.</p>
        <div class="link-list">
          <a class="link-item" href="https://notification-cms.noon.team/partner/email/template/" target="_blank">
            <div class="link-item-left"><div class="dot dot-mail"></div><span class="link-name">Notification CMS</span></div>
            <i class="ti ti-external-link link-ext"></i>
          </a>
          <a class="link-item" href="https://crm.noon.team/campaign?tenant=partner" target="_blank">
            <div class="link-item-left"><div class="dot dot-mail"></div><span class="link-name">Cerebro (noon CRM)</span></div>
            <i class="ti ti-external-link link-ext"></i>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Help Center -->
  <div class="section">
    <div class="section-header">
      <i class="ti ti-lifebuoy section-icon help"></i>
      <span class="section-label">Help Center</span>
    </div>
    <div class="grid-3">
      <div class="launcher">
        <div class="tile-icon help" style="margin-bottom:4px"><i class="ti ti-headset"></i></div>
        <p class="tile-title">Help Center Tools</p>
        <p class="launcher-desc">Manage and access noon's partner and team help center platforms.</p>
        <div class="link-list">
          <a class="link-item" href="https://helpcenter.noon.partners/" target="_blank">
            <div class="link-item-left"><div class="dot dot-help"></div><span class="link-name">Admin Panel</span></div>
            <i class="ti ti-external-link link-ext"></i>
          </a>
          <div class="link-item-row">
            <a class="link-anchor" href="https://helpcenter.noon.team/" target="_blank">
              <div class="dot dot-help"></div><span class="link-name">Help Center Portal</span>
            </a>
            <div class="link-actions">
              <button class="copy-btn" onclick="copyLink(this,'https://helpcenter.noon.team/')" title="Copy link"><i class="ti ti-copy"></i></button>
              <a href="https://helpcenter.noon.team/" target="_blank" style="display:flex;align-items:center;"><i class="ti ti-external-link link-ext"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Ticket Handling -->
  <div class="section">
    <div class="section-header">
      <i class="ti ti-ticket section-icon ticket"></i>
      <span class="section-label">Ticket Handling</span>
    </div>
    <div class="grid-3">
      <div class="launcher">
        <div class="tile-icon ticket" style="margin-bottom:4px"><i class="ti ti-brand-jira"></i></div>
        <p class="tile-title">JIRA</p>
        <p class="launcher-desc">Manage and raise support tickets for partner operations.</p>
        <div class="link-list">
          <a class="link-item" href="https://next-square.atlassian.net/jira/servicedesk/projects/SC/queues/custom/962" target="_blank">
            <div class="link-item-left"><div class="dot dot-ticket"></div><span class="link-name">Tickets Admin Panel</span></div>
            <i class="ti ti-external-link link-ext"></i>
          </a>
          <div class="link-item-row">
            <a class="link-anchor" href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank">
              <div class="dot dot-ticket"></div><span class="link-name">New JIRA Ticket</span>
            </a>
            <div class="link-actions">
              <button class="copy-btn" onclick="copyLink(this,'https://next-square.atlassian.net/servicedesk/customer/portal/89')" title="Copy link"><i class="ti ti-copy"></i></button>
              <a href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank" style="display:flex;align-items:center;"><i class="ti ti-external-link link-ext"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  // Auto-size iframe to content height + 20px bottom padding
  function syncHeight() {{
    const h = document.body.scrollHeight + 20;
    window.parent.postMessage({{type: 'streamlit:setFrameHeight', height: h}}, '*');
  }}
  // Fire on load and whenever content resizes
  window.addEventListener('load', syncHeight);
  new ResizeObserver(syncHeight).observe(document.body);

  function copyLink(btn, url) {{
    navigator.clipboard.writeText(url).then(function() {{
      btn.classList.add('copied');
      btn.innerHTML = '<i class="ti ti-check"></i>';
      setTimeout(function() {{ btn.classList.remove('copied'); btn.innerHTML = '<i class="ti ti-copy"></i>'; }}, 2000);
    }});
  }}
</script>
</body>
</html>
""", height=2000, scrolling=False)
