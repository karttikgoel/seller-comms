import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Comms Tools", layout="wide", page_icon="📬")

# Tighten Streamlit's own container padding
st.markdown("""
<style>
  .block-container { padding-top: 0.5rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html data-theme="dark">
<head>
<link rel="stylesheet" href="https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
<style>
  [data-theme="dark"] {
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
    --toggle-bg:      #2a2a2a;
    --toggle-border:  #3a3a3a;
    --toggle-text:    #9ca3af;
  }
  [data-theme="light"] {
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
    --toggle-bg:      #e5e7eb;
    --toggle-border:  #d1d5db;
    --toggle-text:    #374151;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
  html, body { background: var(--bg); transition: background 0.2s; }
  body { padding: 12px 0 24px; display: flex; flex-direction: column; gap: 18px; }

  /* Hero */
  .topbar { display: flex; align-items: flex-start; justify-content: space-between; }
  .hero-meta { display: flex; flex-direction: column; gap: 2px; }
  .hero-label { font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); }
  .hero-title { font-size: 22px; font-weight: 700; color: var(--text-primary); line-height: 1.2; }
  .hero-sub   { font-size: 12px; color: var(--text-secondary); margin-top: 2px; }

  /* Toggle */
  .toggle-btn {
    display: flex; align-items: center; gap: 6px;
    padding: 7px 12px; border-radius: 8px;
    background: var(--toggle-bg); border: 1px solid var(--toggle-border);
    color: var(--toggle-text); font-size: 12px; font-weight: 500;
    cursor: pointer; transition: all 0.15s; white-space: nowrap; outline: none;
  }
  .toggle-btn:hover { border-color: var(--border-hover); color: var(--text-primary); }
  .toggle-btn i { font-size: 14px; }

  /* Section */
  .section { display: flex; flex-direction: column; gap: 10px; }
  .section-header { display: flex; align-items: center; gap: 8px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
  .section-icon { font-size: 15px; }
  .section-icon.comms  { color: #6b7280; }
  .section-icon.help   { color: #7c3aed; }
  .section-icon.ticket { color: #0284c7; }
  .section-label { font-size: 13px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--section-label); }

  /* All grids use 3 columns so tile widths stay consistent */
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }

  /* Nav tile */
  .tile {
    background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
    padding: 16px; display: flex; flex-direction: column; gap: 10px;
    text-decoration: none; transition: border-color 0.15s, box-shadow 0.15s;
  }
  .tile:hover { border-color: var(--border-hover); box-shadow: 0 2px 10px rgba(0,0,0,0.1); }

  .tile-top { display: flex; align-items: flex-start; justify-content: space-between; }
  .tile-icon {
    width: 36px; height: 36px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center; font-size: 17px; flex-shrink: 0;
  }
  .tile-icon.map     { background: #0d3326; color: #34d399; }
  .tile-icon.builder { background: #0c2240; color: #60a5fa; }
  .tile-icon.mail    { background: #2d1a00; color: #f59e0b; }
  .tile-icon.help    { background: #1c1040; color: #a78bfa; }
  .tile-icon.ticket  { background: #001e2d; color: #38bdf8; }

  .arrow { color: var(--text-muted); font-size: 15px; }
  .tile-title { font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; }
  .tile-desc  { font-size: 12px; color: var(--text-secondary); line-height: 1.55; }

  /* Launcher tile */
  .launcher {
    background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
    padding: 16px; display: flex; flex-direction: column; gap: 10px;
  }
  .launcher-desc { font-size: 12px; color: var(--text-secondary); line-height: 1.55; }

  /* Link items */
  .link-list { display: flex; flex-direction: column; gap: 6px; margin-top: 2px; }

  .link-item {
    display: flex; align-items: center; justify-content: space-between;
    background: var(--surface-deep); border: 1px solid var(--border); border-radius: 8px;
    padding: 9px 12px; text-decoration: none; transition: border-color 0.15s; gap: 8px;
  }
  .link-item:hover { border-color: var(--border-hover); }
  .link-item-left { display: flex; align-items: center; gap: 8px; }

  .link-item-row {
    display: flex; align-items: center;
    background: var(--surface-deep); border: 1px solid var(--border); border-radius: 8px;
    padding: 9px 12px; gap: 8px; transition: border-color 0.15s;
  }
  .link-item-row:hover { border-color: var(--border-hover); }
  .link-anchor { display: flex; align-items: center; gap: 8px; text-decoration: none; flex: 1; min-width: 0; }

  .dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
  .dot-mail   { background: #f59e0b; }
  .dot-help   { background: #a78bfa; }
  .dot-ticket { background: #38bdf8; }

  .link-name { font-size: 13px; color: var(--text-primary); font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .link-ext  { color: var(--text-muted); font-size: 13px; flex-shrink: 0; }

  .link-actions { display: flex; align-items: center; gap: 5px; flex-shrink: 0; }
  .copy-btn {
    display: flex; align-items: center; justify-content: center;
    width: 24px; height: 24px; border-radius: 6px;
    background: var(--copy-bg); border: 1px solid var(--border);
    color: var(--text-muted); cursor: pointer; font-size: 12px;
    transition: all 0.15s; outline: none; flex-shrink: 0;
  }
  .copy-btn:hover { border-color: var(--border-hover); color: var(--text-primary); }
  .copy-btn.copied { background: #0d3326; color: #34d399; border-color: #1a5c40; }
</style>
</head>
<body>

  <!-- Hero -->
  <div class="topbar">
    <div class="hero-meta">
      <span class="hero-label">noon seller comms</span>
      <span class="hero-title">Comms Tools</span>
      <span class="hero-sub">Internal tools for communication workflows at noon.</span>
    </div>
    <button class="toggle-btn" onclick="toggleTheme()" id="theme-btn">
      <i class="ti ti-moon" id="theme-icon"></i>
      <span id="theme-label">Light mode</span>
    </button>
  </div>

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
  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.getAttribute('data-theme') === 'dark';
    html.setAttribute('data-theme', isDark ? 'light' : 'dark');
    document.getElementById('theme-icon').className = isDark ? 'ti ti-moon' : 'ti ti-sun';
    document.getElementById('theme-label').textContent = isDark ? 'Light mode' : 'Dark mode';
  }
  function copyLink(btn, url) {
    navigator.clipboard.writeText(url).then(function() {
      btn.classList.add('copied');
      btn.innerHTML = '<i class="ti ti-check"></i>';
      setTimeout(function() { btn.classList.remove('copied'); btn.innerHTML = '<i class="ti ti-copy"></i>'; }, 2000);
    });
  }
</script>
</body>
</html>
""", height=720, scrolling=True)
