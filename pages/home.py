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
  .hero-sub    { font-size: 14px; color: #9ca3af; margin: 0 0 2rem; }

  /* ── Built-in tools ── */
  .tile-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 2.5rem; max-width: 720px; }

  .tile {
    background: #1e1e1e; border: 1px solid #2d2d2d; border-radius: 14px;
    padding: 1.4rem; display: flex; flex-direction: column; gap: 1rem;
    cursor: pointer; transition: border-color 0.15s, background 0.15s; text-decoration: none;
  }
  .tile:hover { border-color: #555; background: #222; }

  .tile-header { display: flex; align-items: flex-start; justify-content: space-between; }
  .tile-icon-wrap {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 19px;
  }
  .tile-icon-wrap.map     { background: #0d3326; color: #34d399; }
  .tile-icon-wrap.builder { background: #0c2240; color: #60a5fa; }
  .arrow { color: #4b5563; font-size: 17px; }
  .tile-title { font-size: 15px; font-weight: 600; color: #f3f4f6; margin-bottom: 4px; }
  .tile-desc  { font-size: 13px; color: #9ca3af; line-height: 1.6; }
  .tile-footer { display: flex; gap: 6px; flex-wrap: wrap; }
  .tag { font-size: 11px; padding: 3px 9px; border-radius: 100px; background: #2a2a2a; color: #9ca3af; border: 1px solid #333; }

  /* ── External link sections ── */
  .divider { border: none; border-top: 1px solid #2d2d2d; margin: 0 0 1.5rem; }

  .section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
  .section-icon { font-size: 15px; }
  .section-icon.mail   { color: #f59e0b; }
  .section-icon.help   { color: #a78bfa; }
  .section-icon.ticket { color: #38bdf8; }
  .section-label { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6b7280; }

  .link-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 2rem; max-width: 720px; }

  .link-card {
    display: flex; align-items: center; justify-content: space-between;
    background: #1a1a1a; border: 1px solid #2d2d2d; border-radius: 10px;
    padding: 12px 14px; text-decoration: none;
    transition: border-color 0.15s, background 0.15s;
    gap: 10px;
  }
  .link-card:hover { border-color: #444; background: #222; }
  .link-card-left { display: flex; align-items: center; gap: 10px; }
  .link-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .dot-mail   { background: #f59e0b; }
  .dot-help   { background: #a78bfa; }
  .dot-ticket { background: #38bdf8; }
  .link-name  { font-size: 13px; color: #d1d5db; font-weight: 500; }
  .link-arrow { color: #4b5563; font-size: 14px; flex-shrink: 0; }
</style>
</head>
<body>

  <p class="hero-label">noon seller comms</p>
  <h1 class="hero-title">Comms Tools</h1>
  <p class="hero-sub">Internal tools for communication workflows at noon.</p>

  <!-- Built-in tools -->
  <div class="tile-grid">
    <a class="tile" href="/email-map" target="_top">
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
    </a>

    <a class="tile" href="/email-builder" target="_top">
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
    </a>
  </div>

  <!-- Mail Deployment -->
  <hr class="divider">
  <div class="section-header">
    <i class="ti ti-send section-icon mail"></i>
    <span class="section-label">Mail Deployment</span>
  </div>
  <div class="link-grid">
    <a class="link-card" href="https://notification-cms.noon.team/partner/email/template/" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-mail"></div>
        <span class="link-name">Notification CMS</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
    <a class="link-card" href="https://crm.noon.team/campaign?tenant=partner" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-mail"></div>
        <span class="link-name">Cerebro (noon CRM)</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
  </div>

  <!-- Help Center -->
  <hr class="divider">
  <div class="section-header">
    <i class="ti ti-lifebuoy section-icon help"></i>
    <span class="section-label">Help Center</span>
  </div>
  <div class="link-grid">
    <a class="link-card" href="https://helpcenter.noon.partners/" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-help"></div>
        <span class="link-name">Help Center Admin Panel</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
    <a class="link-card" href="https://helpcenter.noon.team/" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-help"></div>
        <span class="link-name">Help Center Portal</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
  </div>

  <!-- Ticket Handling -->
  <hr class="divider">
  <div class="section-header">
    <i class="ti ti-ticket section-icon ticket"></i>
    <span class="section-label">Ticket Handling</span>
  </div>
  <div class="link-grid">
    <a class="link-card" href="https://next-square.atlassian.net/jira/servicedesk/projects/SC/queues/custom/962" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-ticket"></div>
        <span class="link-name">JIRA Tickets Admin Panel</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
    <a class="link-card" href="https://next-square.atlassian.net/servicedesk/customer/portal/89" target="_blank">
      <div class="link-card-left">
        <div class="link-dot dot-ticket"></div>
        <span class="link-name">New JIRA Ticket</span>
      </div>
      <i class="ti ti-external-link link-arrow"></i>
    </a>
  </div>

</body>
</html>
""", height=900, scrolling=True)
