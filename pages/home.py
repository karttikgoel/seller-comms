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
  body { background: transparent; padding: 0 0 2rem; }

  .hero-label { font-size: 11px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: #9ca3af; margin-bottom: 6px; }
  .hero-title  { font-size: 26px; font-weight: 600; color: #f9fafb; margin: 0 0 6px; }
  .hero-sub    { font-size: 14px; color: #9ca3af; margin: 0 0 1.5rem; }

  .divider { border: none; border-top: 1px solid #2d2d2d; margin: 0 0 1.5rem; }

  .section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
  .section-label  { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6b7280; }
  .section-icon   { font-size: 14px; }
  .section-icon.comms  { color: #9ca3af; }
  .section-icon.help   { color: #a78bfa; }
  .section-icon.ticket { color: #38bdf8; }

  .tile-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 2rem; }

  .tile {
    background: #1e1e1e; border: 1px solid #2d2d2d; border-radius: 14px;
    padding: 1.4rem; display: flex; flex-direction: column; gap: 1rem;
    text-decoration: none; transition: border-color 0.15s, background 0.15s;
  }
  .tile:hover { border-color: #555; background: #222; }

  .tile-header { display: flex; align-items: flex-start; justify-content: space-between; }
  .tile-icon-wrap {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 19px;
  }
  .tile-icon-wrap.map     { background: #0d3326; color: #34d399; }
  .tile-icon-wrap.builder { background: #0c2240; color: #60a5fa; }
  .tile-icon-wrap.mail    { background: #2d1a00; color: #f59e0b; }
  .tile-icon-wrap.help    { background: #1c1040; color: #a78bfa; }
  .tile-icon-wrap.ticket  { background: #001e2d; color: #38bdf8; }

  .arrow { color: #4b5563; font-size: 17px; }
  .tile-title { font-size: 15px; font-weight: 600; color: #f3f4f6; margin-bottom: 4px; }
  .tile-desc  { font-size: 13px; color: #9ca3af; line-height: 1.6; }
  .tile-footer { display: flex; gap: 6px; flex-wrap: wrap; margin-top: auto; }
  .tag { font-size: 11px; padding: 3px 9px; border-radius: 100px; background: #2a2a2a; color: #9ca3af; border: 1px solid #333; }

  .launcher-tile {
    background: #1e1e1e; border: 1px solid #2d2d2d; border-radius: 14px;
    padding: 1.4rem; display: flex; flex-direction: column; gap: 1rem;
  }
  .launcher-desc { font-size: 13px; color: #9ca3af; line-height: 1.6; margin-bottom: 0.5rem; }

  .link-list { display: flex; flex-direction: column; gap: 8px; margin-top: auto; }

  /* Standard link item (no copy btn) */
  .link-item {
    display: flex; align-items: center; justify-content: space-between;
    background: #141414; border: 1px solid #2d2d2d; border-radius: 8px;
    padding: 10px 12px; text-decoration: none;
    transition: border-color 0.15s, background 0.15s; gap: 8px;
  }
  .link-item:hover { border-color: #444; background: #1a1a1a; }
  .link-item-left { display: flex; align-items: center; gap: 8px; }

  /* Link item with copy button */
  .link-item-row {
    display: flex; align-items: center;
    background: #141414; border: 1px solid #2d2d2d; border-radius: 8px;
    padding: 10px 12px; gap: 8px;
    transition: border-color 0.15s, background 0.15s;
  }
  .link-item-row:hover { border-color: #444; background: #1a1a1a; }
  .link-item-row .link-anchor {
    display: flex; align-items: center; gap: 8px;
    text-decoration: none; flex: 1; min-width: 0;
  }

  .link-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
  .dot-mail   { background: #f59e0b; }
  .dot-help   { background: #a78bfa; }
  .dot-ticket { background: #38bdf8; }
  .link-name  { font-size: 13px; color: #d1d5db; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .link-ext   { color: #4b5563; font-size: 13px; flex-shrink: 0; }

  .link-actions { display: flex; align-items: center; gap: 5px; flex-shrink: 0; }

  .copy-btn {
    display: flex; align-items: center; justify-content: center;
    width: 26px; height: 26px; border-radius: 6px;
    background: #252525; border: 1px solid #3a3a3a;
    color: #6b7280; cursor: pointer; font-size: 12px;
    transition: background 0.15s, color 0.15s, border-color 0.15s;
    flex-shrink: 0; outline: none;
  }
  .copy-btn:hover { background: #333; color: #d1d5db; border-color: #555; }
  .copy-btn.copied { background: #0d3326; color: #34d399; border-color: #1a5c40; }
</style>
</head>
<body>

  <p class="hero-label">noon seller comms</p>
  <h1 class="hero-title">Comms Tools</h1>
  <p class="hero-sub">Internal tools for communication workflows at noon.</p>

  <!-- Comms Tools -->
  <div class="section-header">
    <i class="ti ti-tools section-icon comms"></i>
    <span class="section-label">Comms Tools</span>
  </div>
  <div class="tile-grid">

    <a class="tile" href="/email-map" target="_top">
      <div class="tile-header">
        <div class="tile-icon-wrap map"><i class="ti ti-map-2"></i></div>
        <i class="ti ti-arrow-up-right arrow"></i>
      </div>
      <div>
        <p class="tile-title">Email Map</p>
        <p class="tile-desc">Visualise and navigate your full email communication structure across teams.</p>
      </div>
      <div class="tile-footer">
        <span class="tag">Templates</span>
        <span class="tag">Journeys</span>
        <span class="tag">Filters</span>
      </div>
    </a>

    <a class="tile" href="/email-builder" target="_top">
      <div class="tile-header">
        <div class="tile-icon-wrap builder"><i class="ti ti-mail-forward"></i></div>
        <i class="ti ti-arrow-up-right arrow"></i>
      </div>
      <div>
        <p class="tile-title">Email Builder</p>
        <p class="tile-desc">Build and customise email templates for DSE seller communications and outreach.</p>
      </div>
      <div class="tile-footer">
        <span class="tag">DSE</span>
        <span class="tag">Onboarding</span>
        <span class="tag">Outreach</span>
      </div>
    </a>

    <div class="launcher-tile">
      <div>
        <div class="tile-icon-wrap mail" style="margin-bottom:0.75rem"><i class="ti ti-send"></i></div>
        <p class="tile-title">Mail Deployment</p>
        <p class="launcher-desc">Send and manage campaigns via noon's mailing infrastructure.</p>
      </div>
      <div class="link-list">
        <a class="link-item" href="https://notification-cms.noon.team/partner/email/template/" target="_blank">
          <div class="link-item-left">
            <div class="link-dot dot-mail"></div>
            <span class="link-name">Notification CMS</span>
          </div>
          <i class="ti ti-external-link link-ext"></i>
        </a>
        <a class="link-item" href="https://crm.noon.team/campaign?tenant=partner" target="_blank">
          <div class="link-item-left">
            <div class="link-dot dot-mail"></div>
            <span class="link-name">Cerebro (noon CRM)</span>
          </div>
          <i class="ti ti-external-link link-ext"></i>
        </a>
      </div>
    </div>

  </div>

  <!-- Help Center -->
  <hr class="divider">
  <div class="section-header">
    <i class="ti ti-lifebuoy section-icon help"></i>
    <span class="section-label">Help Center</span>
  </div>
  <div class="tile-grid">
    <div class="launcher-tile">
      <div>
        <div class="tile-icon-wrap help" style="margin-bottom:0.75rem"><i class="ti ti-headset"></i></div>
        <p class="tile-title">Help Center Tools</p>
        <p class="launcher-desc">Manage and access noon's partner and team help center platforms.</p>
      </div>
      <div class="link-list">
        <a class="link-item" href="https://helpcenter.noon.partners/" target="_blank">
          <div class="link-item-left">
            <div class="link-dot dot-help"></div>
            <span class="link-name">Admin Panel</span>
          </div>
          <i class="ti ti-external-link link-ext"></i>
        </a>
        <!-- Help Center Portal with copy button -->
        <div class="link-item-row">
          <a class="link-anchor" href="https://helpcenter.noon.team/" target="_blank">
            <div class="link-dot dot-help"></div>
            <span class="link-name">Help Center Portal</span>
          </a>
          <div class="link-actions">
            <button class="copy-btn" onclick="copyLink(this, 'https://helpcenter.noon.team/')" title="Copy link">
              <i class="ti ti-copy"></i>
            </button>
            <a href="https://helpcenter.noon.team/" target="_blank" style="display:flex;align-items:center;">
              <i class="ti ti-external-link link-ext"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Ticket Handling -->
  <hr class="divider">
  <div class="section-header">
    <i class="ti ti-ticket section-icon ticket"></i>
    <span class="section-label">Ticket Handling</span>
  </div>
  <div class="tile-grid">
    <div class="launcher-tile">
      <div>
        <div class="tile-icon-wrap ticket" style="margin-bottom:0.75rem"><i class="ti ti-brand-jira"></i></div>
        <p class="tile-title">JIRA</p>
        <p class="launcher-desc">Manage and raise support tickets for partner operations.</p>
      </div>
      <div class="link-list">
        <a class="link-item" href="https://next-square.atlassian.net/jira/servicedesk/projects/SC/queues/custom/962" target="_blank">
          <div class="link-item-left">
            <div class="link-dot dot-ticket"></div>
            <span class="link-name">Tickets Admin Panel</span>
          </div>
          <i class="ti ti-external-link link-ext"></i>
        </a>
        <!-- New JIRA Ticket with copy button -->
        <div class="link-item-row">
          <a class="link-anchor" href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank">
            <div class="link-dot dot-ticket"></div>
            <span class="link-name">New JIRA Ticket</span>
          </a>
          <div class="link-actions">
            <button class="copy-btn" onclick="copyLink(this, 'https://next-square.atlassian.net/servicedesk/customer/portal/89')" title="Copy link">
              <i class="ti ti-copy"></i>
            </button>
            <a href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank" style="display:flex;align-items:center;">
              <i class="ti ti-external-link link-ext"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  function copyLink(btn, url) {
    navigator.clipboard.writeText(url).then(function() {
      btn.classList.add('copied');
      btn.innerHTML = '<i class="ti ti-check"></i>';
      setTimeout(function() {
        btn.classList.remove('copied');
        btn.innerHTML = '<i class="ti ti-copy"></i>';
      }, 2000);
    });
  }
</script>
</body>
</html>
""", height=1000, scrolling=True)
