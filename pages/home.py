import streamlit as st

st.set_page_config(page_title="Comms Tools", layout="wide", page_icon="📬")

# Tighten Streamlit's own container padding
st.markdown("""
<style>
  .block-container {
    padding-top: 1.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 1rem !important;
    max-width: 100% !important;
  }
  footer { display: none !important; }
  [data-testid="stBottom"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# Hero in native Streamlit (above the st.html block)
st.markdown("""
<div style="margin-bottom:1.2rem">
  <span style="font-size:10px;font-weight:500;letter-spacing:0.1em;text-transform:uppercase;opacity:0.45;">noon seller comms</span><br>
  <span style="font-size:22px;font-weight:700;">Comms Tools</span><br>
  <span style="font-size:12px;opacity:0.5;">Internal tools for communication workflows at noon.</span>
</div>
""", unsafe_allow_html=True)

# st.html: no markdown parsing, auto-sizes to content, same-origin so parent CSS vars work
st.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://unpkg.com/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
  body { padding: 2px 0 20px; background: transparent; }

  .ct-section { margin-bottom: 20px; }
  .ct-section-header {
    display: flex; align-items: center; gap: 7px;
    padding-bottom: 7px; border-bottom: 1px solid rgba(128,128,128,0.2); margin-bottom: 12px;
  }
  .ct-section-icon { font-size: 14px; }
  .ct-section-icon.comms  { color: #6b7280; }
  .ct-section-icon.help   { color: #7c3aed; }
  .ct-section-icon.ticket { color: #0284c7; }
  .ct-section-label { font-size: 12px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; }

  .ct-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }

  a.ct-tile {
    display: flex; flex-direction: column; gap: 10px;
    border: 1px solid rgba(128,128,128,0.2); border-radius: 14px; padding: 16px;
    text-decoration: none; transition: border-color 0.15s, box-shadow 0.15s;
  }
  a.ct-tile:hover { border-color: rgba(128,128,128,0.5); box-shadow: 0 2px 12px rgba(0,0,0,0.08); }

  .ct-tile-top { display: flex; align-items: flex-start; justify-content: space-between; }
  .ct-icon {
    width: 36px; height: 36px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center; font-size: 17px; flex-shrink: 0;
  }
  .ct-icon.map     { background: #0d3326; color: #34d399; }
  .ct-icon.builder { background: #0c2240; color: #60a5fa; }
  .ct-icon.mail    { background: #2d1a00; color: #f59e0b; }
  .ct-icon.help    { background: #1c1040; color: #a78bfa; }
  .ct-icon.ticket  { background: #001e2d; color: #38bdf8; }
  .ct-arrow { font-size: 15px; opacity: 0.3; }
  .ct-tile-title { font-size: 14px; font-weight: 600; margin-bottom: 3px; }
  .ct-tile-desc  { font-size: 12px; line-height: 1.55; opacity: 0.6; }

  .ct-launcher { display: flex; flex-direction: column; gap: 10px; border: 1px solid rgba(128,128,128,0.2); border-radius: 14px; padding: 16px; }
  .ct-launcher-desc { font-size: 12px; line-height: 1.55; opacity: 0.6; }

  .ct-link-list { display: flex; flex-direction: column; gap: 6px; }

  a.ct-link {
    display: flex; align-items: center; justify-content: space-between;
    border: 1px solid rgba(128,128,128,0.15); border-radius: 8px; padding: 9px 12px;
    text-decoration: none; transition: border-color 0.15s; gap: 8px;
  }
  a.ct-link:hover { border-color: rgba(128,128,128,0.4); }
  .ct-link-left { display: flex; align-items: center; gap: 8px; }
  .ct-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
  .ct-dot.mail   { background: #f59e0b; }
  .ct-dot.help   { background: #a78bfa; }
  .ct-dot.ticket { background: #38bdf8; }
  .ct-link-name { font-size: 13px; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .ct-link-ext  { font-size: 13px; opacity: 0.3; flex-shrink: 0; }

  .ct-copy-row {
    display: flex; align-items: center;
    border: 1px solid rgba(128,128,128,0.15); border-radius: 8px; padding: 9px 12px; gap: 8px;
    transition: border-color 0.15s;
  }
  .ct-copy-row:hover { border-color: rgba(128,128,128,0.4); }
  a.ct-copy-anchor { display: flex; align-items: center; gap: 8px; text-decoration: none; flex: 1; min-width: 0; }
  .ct-copy-actions { display: flex; align-items: center; gap: 5px; flex-shrink: 0; }
  button.ct-copy-btn {
    display: flex; align-items: center; justify-content: center;
    width: 24px; height: 24px; border-radius: 6px;
    background: rgba(128,128,128,0.1); border: 1px solid rgba(128,128,128,0.2);
    opacity: 0.6; cursor: pointer; font-size: 12px; transition: all 0.15s; outline: none; flex-shrink: 0;
  }
  button.ct-copy-btn:hover { opacity: 1; border-color: rgba(128,128,128,0.5); }
  button.ct-copy-btn.copied { background: #0d3326; color: #34d399 !important; border-color: #1a5c40; opacity: 1; }

  /* Theme: read from parent Streamlit body via JS, set on <html> */
  html.dark  { color-scheme: dark; color: #f3f4f6; }
  html.dark  a.ct-tile,
  html.dark  .ct-launcher { background: #1a1a1a; }
  html.dark  a.ct-link,
  html.dark  .ct-copy-row { background: #111; }
  html.dark  button.ct-copy-btn { color: #f3f4f6; }

  html.light { color-scheme: light; color: #111827; }
  html.light a.ct-tile,
  html.light .ct-launcher { background: #ffffff; }
  html.light a.ct-link,
  html.light .ct-copy-row { background: #f9fafb; }
  html.light button.ct-copy-btn { color: #111827; }
</style>
</head>
<body>

<div class="ct-section">
  <div class="ct-section-header">
    <i class="ti ti-tools ct-section-icon comms"></i>
    <span class="ct-section-label">Comms Tools</span>
  </div>
  <div class="ct-grid-3">
    <a class="ct-tile" href="/email-map" target="_top">
      <div class="ct-tile-top">
        <div class="ct-icon map"><i class="ti ti-map-2"></i></div>
        <i class="ti ti-arrow-up-right ct-arrow"></i>
      </div>
      <p class="ct-tile-title">Email Map</p>
      <p class="ct-tile-desc">Visualise and navigate your full email communication structure across teams.</p>
    </a>
    <a class="ct-tile" href="/email-builder" target="_top">
      <div class="ct-tile-top">
        <div class="ct-icon builder"><i class="ti ti-mail-forward"></i></div>
        <i class="ti ti-arrow-up-right ct-arrow"></i>
      </div>
      <p class="ct-tile-title">Email Builder</p>
      <p class="ct-tile-desc">Build and customise email templates for DSE seller communications and outreach.</p>
    </a>
    <div class="ct-launcher">
      <div class="ct-icon mail" style="margin-bottom:4px"><i class="ti ti-send"></i></div>
      <p class="ct-tile-title">Mail Deployment</p>
      <p class="ct-launcher-desc">Send and manage campaigns via noon's mailing infrastructure.</p>
      <div class="ct-link-list">
        <a class="ct-link" href="https://notification-cms.noon.team/partner/email/template/" target="_blank">
          <div class="ct-link-left"><div class="ct-dot mail"></div><span class="ct-link-name">Notification CMS</span></div>
          <i class="ti ti-external-link ct-link-ext"></i>
        </a>
        <a class="ct-link" href="https://crm.noon.team/campaign?tenant=partner" target="_blank">
          <div class="ct-link-left"><div class="ct-dot mail"></div><span class="ct-link-name">Cerebro (noon CRM)</span></div>
          <i class="ti ti-external-link ct-link-ext"></i>
        </a>
      </div>
    </div>
  </div>
</div>

<div class="ct-section">
  <div class="ct-section-header">
    <i class="ti ti-lifebuoy ct-section-icon help"></i>
    <span class="ct-section-label">Help Center</span>
  </div>
  <div class="ct-grid-3">
    <div class="ct-launcher">
      <div class="ct-icon help" style="margin-bottom:4px"><i class="ti ti-headset"></i></div>
      <p class="ct-tile-title">Help Center Tools</p>
      <p class="ct-launcher-desc">Manage and access noon's partner and team help center platforms.</p>
      <div class="ct-link-list">
        <a class="ct-link" href="https://helpcenter.noon.partners/" target="_blank">
          <div class="ct-link-left"><div class="ct-dot help"></div><span class="ct-link-name">Admin Panel</span></div>
          <i class="ti ti-external-link ct-link-ext"></i>
        </a>
        <div class="ct-copy-row">
          <a class="ct-copy-anchor" href="https://helpcenter.noon.team/" target="_blank">
            <div class="ct-dot help"></div><span class="ct-link-name">Help Center Portal</span>
          </a>
          <div class="ct-copy-actions">
            <button class="ct-copy-btn" onclick="ctCopy(this,'https://helpcenter.noon.team/')" title="Copy link"><i class="ti ti-copy"></i></button>
            <a href="https://helpcenter.noon.team/" target="_blank" style="display:flex;align-items:center;"><i class="ti ti-external-link ct-link-ext"></i></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="ct-section">
  <div class="ct-section-header">
    <i class="ti ti-ticket ct-section-icon ticket"></i>
    <span class="ct-section-label">Ticket Handling</span>
  </div>
  <div class="ct-grid-3">
    <div class="ct-launcher">
      <div class="ct-icon ticket" style="margin-bottom:4px"><i class="ti ti-brand-jira"></i></div>
      <p class="ct-tile-title">JIRA</p>
      <p class="ct-launcher-desc">Manage and raise support tickets for partner operations.</p>
      <div class="ct-link-list">
        <a class="ct-link" href="https://next-square.atlassian.net/jira/servicedesk/projects/SC/queues/custom/962" target="_blank">
          <div class="ct-link-left"><div class="ct-dot ticket"></div><span class="ct-link-name">Tickets Admin Panel</span></div>
          <i class="ti ti-external-link ct-link-ext"></i>
        </a>
        <div class="ct-copy-row">
          <a class="ct-copy-anchor" href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank">
            <div class="ct-dot ticket"></div><span class="ct-link-name">New JIRA Ticket</span>
          </a>
          <div class="ct-copy-actions">
            <button class="ct-copy-btn" onclick="ctCopy(this,'https://next-square.atlassian.net/servicedesk/customer/portal/89')" title="Copy link"><i class="ti ti-copy"></i></button>
            <a href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank" style="display:flex;align-items:center;"><i class="ti ti-external-link ct-link-ext"></i></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Detect Streamlit parent theme via luminance of its background colour
  function applyTheme() {
    try {
      var bg = getComputedStyle(window.parent.document.body).backgroundColor;
      var rgb = bg.match(/\d+/g);
      if (rgb) {
        var lum = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2];
        document.documentElement.className = lum < 128 ? 'dark' : 'light';
      }
    } catch(e) {
      document.documentElement.className = 'dark';
    }
  }
  applyTheme();
  // Re-apply whenever Streamlit changes its theme (triggers body attribute changes)
  try {
    new MutationObserver(applyTheme).observe(
      window.parent.document.body,
      { attributes: true, childList: false, subtree: false }
    );
  } catch(e) {}

  function ctCopy(btn, url) {
    navigator.clipboard.writeText(url).then(function() {
      btn.classList.add('copied');
      btn.innerHTML = '<i class="ti ti-check"></i>';
      setTimeout(function() { btn.classList.remove('copied'); btn.innerHTML = '<i class="ti ti-copy"></i>'; }, 2000);
    });
  }
</script>
</body>
</html>
""")
