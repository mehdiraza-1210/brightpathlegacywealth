import base64
import os
import re

# Load base64 assets
with open('brightpath-logo.webp', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('college-savings-flyer.webp', 'rb') as f:
    flyer_b64 = base64.b64encode(f.read()).decode('utf-8')

print("Loaded assets: logo b64 length =", len(logo_b64), ", flyer b64 length =", len(flyer_b64))

# HTML Template
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BrightPath Legacy Wealth Corporation | College Funding Showdown</title>
  <meta name="description" content="Discover smart wealth building and college funding strategies with BrightPath Legacy Wealth Corporation. Compare Trump Accounts, 529 Plans, and Flexible Life Insurance." />
  <link rel="icon" type="image/png" href="brightpath-logo-transparent.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
</head>
<body>

<div id="cfs-root">
<style>
/* ==========================================================================
   GLOBAL ZERO-MARGIN & FULL-BLEED RESET
   Eliminates all gaps on standalone browser preview and within GoHighLevel
   ========================================================================== */
html, body {{
  margin: 0 !important;
  padding: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
  background-color: #ffffff;
}}

/* Ensure parent GoHighLevel wrappers do not inject gutters */
.c-custom-code,
.inner-section,
.c-wrapper,
.section-wrapper,
.hl-page-preview--content {{
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
}}

#cfs-root *,
#cfs-root *::before,
#cfs-root *::after {{
  box-sizing: border-box;
  max-width: 100%;
  min-width: 0;
}}

#cfs-root {{
  /* BrightPath Legacy Wealth Brand Color Palette - Matched Directly to Official Logo */
  --navy-dark: #041426;
  --navy: #082444;
  --navy-mid: #0d3663;
  --navy-light: #164e8a;
  --blue-accent: #1da4db;
  --blue-ice: #edf5fc;

  --gold: #d49b28;
  --gold-dark: #b07e1a;
  --gold-light: #f5cb5c;
  --gold-pale: #fcf7ed;

  --growth-green: #10b981;
  --alert-red: #ef4444;

  --white: #ffffff;
  --off-white: #f5f8fc;
  --grey-light: #e1e7f0;
  --grey-text: #485c72;
  --dark-text: #081f38;

  --radius: 12px;
  --pill: 50px;
  --shadow-sm: 0 2px 8px rgba(4,20,38,.08);
  --shadow-md: 0 6px 24px rgba(4,20,38,.14);
  --shadow-lg: 0 16px 40px rgba(4,20,38,.22);
  --t: .25s ease;

  /* Color mapping for full backwards and semantic compatibility */
  --green: var(--navy);
  --green-dark: var(--navy-dark);
  --green-mid: var(--navy-mid);
  --green-light: var(--navy-light);

  font-family: "Open Sans", sans-serif;
  color: var(--dark-text);
  background: #fff;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  display: block;
}}

#cfs-root h1,
#cfs-root h2,
#cfs-root h3,
#cfs-root h4,
#cfs-root h5,
#cfs-root p,
#cfs-root span,
#cfs-root a,
#cfs-root li {{
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
  hyphens: auto;
}}

/* ==========================================================================
   BRAND NAVIGATION HEADER - REFINED CORPORATE IDENTITY LOCKUP
   ========================================================================== */
#cfs-root .cfs-brand-bar {{
  width: 100% !important;
  background: var(--white);
  border-bottom: 2px solid var(--grey-light);
  padding: clamp(.75rem, 2vw, 1.1rem) clamp(1rem, 4vw, 2.5rem);
  box-shadow: 0 2px 10px rgba(4,20,38,.06);
  position: relative;
  z-index: 100;
  margin: 0 !important;
}}

#cfs-root .cfs-brand-inner {{
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}}

#cfs-root .cfs-brand-logo-wrap {{
  display: inline-flex;
  align-items: center;
  gap: clamp(.65rem, 2vw, 1rem);
  text-decoration: none;
}}

/* Refined circular/squircle crest frame */
#cfs-root .cfs-brand-crest-frame {{
  height: clamp(52px, 8vw, 68px);
  width: clamp(52px, 8vw, 68px);
  border-radius: 14px;
  overflow: hidden;
  border: 2px solid var(--gold);
  box-shadow: 0 4px 14px rgba(4,20,38,.18);
  background: #041426;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform .25s ease, box-shadow .25s ease;
}}

#cfs-root .cfs-brand-logo-wrap:hover .cfs-brand-crest-frame {{
  transform: scale(1.04);
  box-shadow: 0 6px 18px rgba(212,155,40,.35);
}}

#cfs-root .cfs-brand-crest-frame img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}}

/* Typographic Brand Identity Lockup */
#cfs-root .cfs-brand-wordmark {{
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

#cfs-root .cfs-brand-company-name {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.15rem, 2.6vw, 1.45rem);
  font-weight: 900;
  letter-spacing: .04em;
  color: var(--navy);
  line-height: 1.1;
  text-transform: uppercase;
}}

#cfs-root .cfs-brand-company-name span {{
  color: var(--gold);
}}

#cfs-root .cfs-brand-tagline-text {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(.65rem, 1.6vw, .76rem);
  font-weight: 800;
  letter-spacing: .12em;
  color: var(--gold-dark);
  text-transform: uppercase;
  margin-top: 3px;
  line-height: 1.2;
}}

#cfs-root .cfs-brand-sub-motto {{
  font-size: clamp(.62rem, 1.4vw, .72rem);
  color: var(--grey-text);
  margin-top: 2px;
  font-style: italic;
  display: none;
}}

@media (min-width: 680px) {{
  #cfs-root .cfs-brand-sub-motto {{
    display: block;
  }}
}}

#cfs-root .cfs-brand-badge {{
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  background: var(--gold-pale);
  border: 1px solid var(--gold);
  border-radius: var(--pill);
  padding: clamp(.3rem, 1.5vw, .45rem) clamp(.65rem, 2vw, 1.1rem);
  font-family: "Montserrat", sans-serif;
  font-size: clamp(.68rem, 2vw, .8rem);
  font-weight: 700;
  color: var(--navy-mid);
  white-space: nowrap;
}}

#cfs-root .cfs-badge-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--gold);
  display: inline-block;
  animation: cfsPulse 2s infinite ease-in-out;
}}

@keyframes cfsPulse {{
  0%, 100% {{ transform: scale(1); opacity: 1; }}
  50% {{ transform: scale(1.35); opacity: .7; }}
}}

/* ==========================================================================
   HERO SECTION - FULL-BLEED WITH NO EDGE GAPS
   ========================================================================== */
#cfs-root .cfs-hero {{
  width: 100% !important;
  background: linear-gradient(145deg, var(--navy-dark) 0%, var(--navy) 55%, var(--navy-mid) 100%);
  color: var(--white);
  padding: clamp(2.5rem, 6vw, 4.5rem) clamp(1rem, 4vw, 2.5rem);
  position: relative;
  overflow: hidden;
  border-bottom: 3px solid var(--gold);
  margin: 0 !important;
}}

#cfs-root .cfs-hero::after {{
  content: "";
  position: absolute;
  top: -30%;
  right: -10%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(212,155,40,.15) 0%, rgba(29,164,219,.08) 45%, transparent 70%);
  pointer-events: none;
}}

#cfs-root .cfs-hero-container {{
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(2rem, 5vw, 3.5rem);
  align-items: center;
  position: relative;
  z-index: 1;
}}

@media (min-width: 920px) {{
  #cfs-root .cfs-hero-container {{
    grid-template-columns: 1.1fr 0.9fr;
  }}
}}

#cfs-root .cfs-hero-content {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: clamp(.75rem, 2vw, 1.25rem);
}}

#cfs-root .cfs-eyebrow {{
  display: inline-block;
  font-family: "Montserrat", sans-serif;
  font-size: clamp(.72rem, 2vw, .85rem);
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--gold-light);
  background: rgba(212,155,40,.15);
  border: 1px solid rgba(212,155,40,.35);
  padding: .35rem .9rem;
  border-radius: var(--pill);
  margin: 0;
}}

#cfs-root .cfs-h1 {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.85rem, 4.2vw, 3rem);
  font-weight: 900;
  line-height: 1.18;
  color: var(--white);
  margin: 0;
}}

#cfs-root .cfs-sub {{
  font-size: clamp(.95rem, 2vw, 1.12rem);
  line-height: 1.6;
  color: #d8e5f2;
  margin: 0;
  max-width: 560px;
}}

#cfs-root .cfs-hero-visual {{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}}

#cfs-root .cfs-hero-image-frame {{
  position: relative;
  width: 100%;
  max-width: 540px;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,.45);
  border: 2px solid rgba(212, 155, 40, 0.45);
  background: #041426;
}}

#cfs-root .cfs-hero-image-frame img {{
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  transition: transform .4s ease;
}}

#cfs-root .cfs-hero-image-frame:hover img {{
  transform: scale(1.02);
}}

#cfs-root .cfs-hero-badge {{
  position: absolute;
  bottom: 14px;
  left: 14px;
  background: rgba(4, 20, 38, 0.9);
  backdrop-filter: blur(8px);
  border: 1px solid var(--gold);
  border-radius: 10px;
  padding: .6rem 1rem;
  display: flex;
  align-items: center;
  gap: .65rem;
  color: var(--white);
  box-shadow: 0 6px 20px rgba(0,0,0,.4);
}}

#cfs-root .cfs-hero-badge-icon {{
  font-size: 1.25rem;
  color: var(--gold-light);
}}

#cfs-root .cfs-hero-badge strong {{
  display: block;
  font-family: "Montserrat", sans-serif;
  font-size: .82rem;
  font-weight: 800;
  color: var(--gold-light);
}}

#cfs-root .cfs-hero-badge span {{
  display: block;
  font-size: .72rem;
  color: #c9d7e6;
}}

#cfs-root .cfs-btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .65rem;
  background: linear-gradient(135deg, var(--gold) 0%, #b8831a 100%);
  color: #041426;
  font-family: "Montserrat", sans-serif;
  font-size: clamp(.88rem, 2.5vw, 1.05rem);
  font-weight: 800;
  padding: clamp(.75rem, 2.5vw, 1rem) clamp(1.4rem, 4vw, 2.2rem);
  border-radius: var(--pill);
  text-decoration: none;
  border: 1.5px solid #ffe391;
  cursor: pointer;
  box-shadow: 0 4px 18px rgba(212,155,40,.4);
  transition: transform var(--t), box-shadow var(--t), background var(--t);
  white-space: normal;
  text-align: center;
  letter-spacing: .02em;
}}

#cfs-root .cfs-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(212,155,40,.55);
  background: linear-gradient(135deg, #dfa938 0%, #c48f21 100%);
  color: #041426;
}}

#cfs-root .cfs-btn--lg {{
  width: 100%;
  max-width: 480px;
  padding: 1.05rem 2rem;
  font-size: 1.08rem;
}}

#cfs-root .cfs-hero-note {{
  font-size: clamp(.75rem, 2vw, .85rem);
  color: #b0c4de;
  margin: 0;
}}

/* ==========================================================================
   SIDE-BY-SIDE COMPARISON SECTION (Positioned Prior to Calculator)
   ========================================================================== */
#cfs-root .cfs-compare {{
  width: 100% !important;
  padding: clamp(3rem, 7vw, 5rem) clamp(1rem, 4vw, 2.5rem);
  background: var(--off-white);
  text-align: center;
  border-bottom: 1px solid var(--grey-light);
  margin: 0 !important;
}}

#cfs-root .cfs-section-intro {{
  max-width: 780px;
  margin: 0 auto clamp(2rem, 5vw, 3rem);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .75rem;
}}

#cfs-root .cfs-h2 {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.6rem, 3.8vw, 2.4rem);
  font-weight: 800;
  line-height: 1.25;
  color: var(--navy);
  margin: 0;
}}

#cfs-root .cfs-section-intro p {{
  font-size: clamp(.92rem, 2vw, 1.05rem);
  color: var(--grey-text);
  margin: 0;
  line-height: 1.6;
}}

#cfs-root .cfs-card-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.75rem;
  max-width: 1200px;
  margin: 0 auto 2.5rem;
  text-align: left;
}}

@media (min-width: 860px) {{
  #cfs-root .cfs-card-grid {{
    grid-template-columns: repeat(3, 1fr);
  }}
}}

#cfs-root .cfs-card {{
  background: var(--white);
  border: 1px solid var(--grey-light);
  border-radius: var(--radius);
  padding: clamp(1.5rem, 4vw, 2rem);
  display: flex;
  flex-direction: column;
  transition: transform var(--t), box-shadow var(--t);
  position: relative;
  box-shadow: var(--shadow-sm);
}}

#cfs-root .cfs-card:hover {{
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
}}

#cfs-root .cfs-card--featured {{
  background: var(--white);
  border: 2px solid var(--gold);
  box-shadow: 0 8px 30px rgba(212,155,40,.2);
}}

#cfs-root .cfs-card--featured::before {{
  content: "Featured Alternative";
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--gold);
  color: #041426;
  font-family: "Montserrat", sans-serif;
  font-size: .72rem;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: 4px 16px;
  border-radius: var(--pill);
  box-shadow: 0 2px 8px rgba(0,0,0,.2);
  white-space: nowrap;
}}

#cfs-root .cfs-card-icon {{
  font-size: 2.2rem;
  margin-bottom: .75rem;
  line-height: 1;
}}

#cfs-root .cfs-card-title {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.15rem, 2.8vw, 1.35rem);
  font-weight: 800;
  color: var(--navy);
  margin: 0 0 .35rem 0;
}}

#cfs-root .cfs-card-sub {{
  font-size: .82rem;
  font-weight: 700;
  color: var(--blue-accent);
  text-transform: uppercase;
  letter-spacing: .05em;
  margin: 0 0 .75rem 0;
}}

#cfs-root .cfs-card-desc {{
  font-size: .92rem;
  line-height: 1.6;
  color: var(--grey-text);
  margin: 0 0 1.25rem 0;
  flex: 1 1 auto;
}}

#cfs-root .cfs-card-desc strong {{
  color: var(--navy);
}}

#cfs-root .cfs-card-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  margin-top: auto;
}}

#cfs-root .cfs-tag {{
  display: inline-block;
  font-family: "Montserrat", sans-serif;
  font-size: .72rem;
  font-weight: 700;
  padding: .3rem .7rem;
  border-radius: var(--pill);
  background: var(--grey-light);
  color: var(--navy);
}}

#cfs-root .cfs-tag--good {{
  background: rgba(16,185,129,.14);
  color: #065f46;
  border: 1px solid rgba(16,185,129,.35);
}}

#cfs-root .cfs-tag--bad {{
  background: rgba(239,68,68,.12);
  color: #991b1b;
  border: 1px solid rgba(239,68,68,.25);
}}

#cfs-root .cfs-tag--gold {{
  background: rgba(212,155,40,.18);
  color: #8c5d08;
  border: 1px solid rgba(212,155,40,.45);
  font-weight: 800;
}}

#cfs-root .cfs-callout {{
  background: var(--white);
  border-left: 4px solid var(--gold);
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  max-width: 860px;
  margin: 0 auto 2rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--navy);
  box-shadow: var(--shadow-sm);
  text-align: left;
}}

#cfs-root .cfs-callout strong {{
  display: block;
  font-family: "Montserrat", sans-serif;
  font-size: 1.05rem;
  color: var(--navy);
  margin-bottom: .25rem;
}}

/* ==========================================================================
   CALCULATOR & FUNNEL SECTION - FULL-BLEED
   ========================================================================== */
#cfs-root .cfs-calculator-section {{
  width: 100% !important;
  padding: clamp(3rem, 7vw, 5rem) clamp(1rem, 4vw, 2.5rem);
  background: #ffffff;
  margin: 0 !important;
}}

#cfs-root .cfs-calc-container {{
  max-width: 980px;
  margin: 0 auto;
}}

#cfs-root .cfs-calc-card {{
  background: var(--off-white);
  border: 1.5px solid var(--grey-light);
  border-radius: 16px;
  padding: clamp(1.5rem, 5vw, 2.75rem);
  box-shadow: var(--shadow-md);
  margin-bottom: 2rem;
}}

#cfs-root .cfs-calc-step-header {{
  display: flex;
  align-items: center;
  gap: .85rem;
  margin-bottom: 1.25rem;
}}

#cfs-root .cfs-step-pill {{
  background: var(--navy);
  color: var(--white);
  font-family: "Montserrat", sans-serif;
  font-size: .78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .06em;
  padding: .35rem .85rem;
  border-radius: var(--pill);
  white-space: nowrap;
}}

#cfs-root .cfs-step-title {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.15rem, 2.8vw, 1.45rem);
  font-weight: 800;
  color: var(--navy);
  margin: 0;
}}

#cfs-root .cfs-step-sub {{
  font-size: .88rem;
  color: var(--grey-text);
  margin: .25rem 0 0 0;
}}

#cfs-root .cfs-calc-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}}

@media (min-width: 680px) {{
  #cfs-root .cfs-calc-grid {{
    grid-template-columns: 1fr 1fr;
  }}
}}

#cfs-root .cfs-input-group--full {{
  grid-column: 1 / -1;
}}

#cfs-root .cfs-label {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-family: "Montserrat", sans-serif;
  font-size: .88rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: .5rem;
}}

#cfs-root .cfs-label-val {{
  color: var(--navy-mid);
  font-weight: 800;
  font-size: .95rem;
}}

#cfs-root .cfs-range {{
  width: 100%;
  height: 8px;
  border-radius: 4px;
  background: #cbd5e1;
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
}}

#cfs-root .cfs-range::-webkit-slider-thumb {{
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--gold);
  border: 3px solid var(--white);
  box-shadow: 0 2px 6px rgba(0,0,0,.3);
  cursor: pointer;
  transition: transform .15s ease;
}}

#cfs-root .cfs-range::-webkit-slider-thumb:hover {{
  transform: scale(1.18);
}}

#cfs-root .cfs-range-ticks {{
  display: flex;
  justify-content: space-between;
  font-size: .74rem;
  color: var(--grey-text);
  margin-top: .4rem;
}}

#cfs-root .cfs-hint {{
  font-size: .82rem;
  color: var(--grey-text);
  margin-top: .4rem;
}}

#cfs-root .cfs-select-box,
#cfs-root .cfs-form-input {{
  width: 100%;
  padding: .85rem 1rem;
  border: 1.5px solid var(--grey-light);
  border-radius: 8px;
  font-family: inherit;
  font-size: .95rem;
  color: var(--navy);
  background: var(--white);
  outline: none;
  transition: border-color var(--t), box-shadow var(--t);
}}

#cfs-root .cfs-select-box:focus,
#cfs-root .cfs-form-input:focus {{
  border-color: var(--navy-mid);
  box-shadow: 0 0 0 3px rgba(13,54,99,.15);
}}

/* Opt-In Mandatory Form Styles */
#cfs-root .cfs-form-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.15rem;
}}

@media (min-width: 680px) {{
  #cfs-root .cfs-form-grid {{
    grid-template-columns: 1fr 1fr;
  }}
}}

#cfs-root .cfs-form-group--full {{
  grid-column: 1 / -1;
}}

#cfs-root .cfs-consent-wrap {{
  display: flex;
  align-items: flex-start;
  gap: .65rem;
  font-size: .78rem;
  line-height: 1.45;
  color: var(--grey-text);
  cursor: pointer;
}}

#cfs-root .cfs-consent-wrap input {{
  margin-top: .15rem;
  cursor: pointer;
}}

/* Captcha Styles */
#cfs-root .cfs-captcha-row {{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .65rem;
  margin-top: .35rem;
}}

#cfs-root .cfs-captcha-badge {{
  background: linear-gradient(135deg, #041426 0%, #0d3663 100%);
  border: 1.5px dashed var(--gold);
  border-radius: 8px;
  padding: .65rem 1.1rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  user-select: none;
  box-shadow: inset 0 1px 4px rgba(0,0,0,.4);
}}

#cfs-root #cfs-captcha-text {{
  font-family: "Courier New", Courier, monospace;
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: .3em;
  color: var(--gold-light);
  text-decoration: line-through;
  text-shadow: 1px 1px 3px rgba(0,0,0,.7);
  transform: skewX(-10deg);
  display: inline-block;
}}

#cfs-root .cfs-captcha-refresh-btn {{
  background: var(--white);
  border: 1px solid var(--grey-light);
  border-radius: 8px;
  padding: .75rem 1rem;
  font-size: .84rem;
  font-weight: 700;
  color: var(--navy);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  transition: all var(--t);
}}

#cfs-root .cfs-captcha-refresh-btn:hover {{
  background: var(--gold-pale);
  border-color: var(--gold);
  color: var(--gold-dark);
}}

#cfs-root .cfs-captcha-input {{
  flex: 1 1 140px;
  min-width: 130px;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: .12em;
}}

#cfs-root .cfs-form-error {{
  background: #fef2f2;
  border-left: 4px solid #ef4444;
  color: #991b1b;
  padding: .75rem 1rem;
  border-radius: 6px;
  font-size: .88rem;
  font-weight: 700;
  margin-top: .75rem;
  grid-column: 1 / -1;
}}

/* ==========================================================================
   TEASER SCORECARD BOX - WITH EMPHASIZED SCALE
   ========================================================================== */
#cfs-root .cfs-teaser-box {{
  background: linear-gradient(145deg, #041426 0%, #082444 60%, #0d3663 100%);
  border: 2px solid var(--gold);
  border-radius: 16px;
  padding: clamp(1.75rem, 5vw, 3rem);
  box-shadow: 0 16px 44px rgba(4,20,38,.35);
  color: var(--white);
  margin-bottom: 2.5rem;
}}

#cfs-root .cfs-teaser-header {{
  text-align: center;
  max-width: 820px;
  margin: 0 auto;
}}

#cfs-root .cfs-teaser-pill {{
  display: inline-block;
  background: rgba(212,155,40,.2);
  border: 1px solid var(--gold);
  color: var(--gold-light);
  font-family: "Montserrat", sans-serif;
  font-size: .75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .08em;
  padding: .35rem .95rem;
  border-radius: var(--pill);
  margin-bottom: .75rem;
}}

#cfs-root .cfs-teaser-headline {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.6rem, 3.8vw, 2.2rem);
  font-weight: 900;
  color: var(--white);
  margin: 0 0 .5rem 0;
}}

/* EMPHASIZED CALCULATOR SCALE STYLES */
#cfs-root .cfs-prominent-scale-card {{
  background: rgba(4, 20, 38, 0.55);
  border: 1.5px solid rgba(212, 155, 40, 0.45);
  border-radius: 14px;
  padding: clamp(1.25rem, 3vw, 1.75rem);
  margin: 1.5rem 0 2rem 0;
  box-shadow: inset 0 2px 12px rgba(0,0,0,.35);
  text-align: left;
}}

#cfs-root .cfs-scale-top {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.75rem;
  text-align: center;
}}

@media (min-width: 640px) {{
  #cfs-root .cfs-scale-top {{
    flex-direction: row;
    justify-content: space-between;
    text-align: left;
  }}
}}

#cfs-root .cfs-scale-badge-wrap {{
  display: inline-flex;
  align-items: baseline;
  background: linear-gradient(135deg, rgba(212,155,40,.25) 0%, rgba(212,155,40,.08) 100%);
  border: 2px solid var(--gold);
  border-radius: var(--pill);
  padding: .5rem 1.6rem;
  box-shadow: 0 4px 16px rgba(0,0,0,.3);
}}

#cfs-root .cfs-scale-score-main {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(2.4rem, 5vw, 3.2rem);
  font-weight: 900;
  color: var(--gold-light);
  line-height: 1;
}}

#cfs-root .cfs-scale-score-denominator {{
  font-size: 1.05rem;
  font-weight: 800;
  color: rgba(255,255,255,.75);
  margin-left: .35rem;
}}

#cfs-root .cfs-scale-status-title {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.1rem, 2.8vw, 1.35rem);
  font-weight: 800;
  color: #ffffff;
  margin-bottom: .25rem;
}}

#cfs-root .cfs-scale-status-desc {{
  font-size: .88rem;
  color: #cbd5e1;
}}

/* Segmented Progress Track with Dynamic Pointer */
#cfs-root .cfs-scale-bar-wrapper {{
  position: relative;
  margin: 2.75rem 0 1rem 0;
  padding-top: 1.5rem;
}}

#cfs-root .cfs-scale-pointer-container {{
  position: absolute;
  top: -16px;
  left: 0;
  width: 100%;
  height: 28px;
  pointer-events: none;
}}

#cfs-root .cfs-scale-pointer {{
  position: absolute;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: left .5s cubic-bezier(.34, 1.56, .64, 1);
  z-index: 10;
}}

#cfs-root .cfs-pointer-bubble {{
  background: var(--gold);
  color: #041426;
  font-family: "Montserrat", sans-serif;
  font-size: .8rem;
  font-weight: 900;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
  box-shadow: 0 2px 10px rgba(0,0,0,.45);
  letter-spacing: .02em;
}}

#cfs-root .cfs-pointer-arrow {{
  width: 0;
  height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-top: 8px solid var(--gold);
}}

#cfs-root .cfs-scale-track {{
  display: grid;
  grid-template-columns: 49fr 20fr 15fr 16fr;
  height: 32px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: inset 0 2px 8px rgba(0,0,0,.6), 0 2px 8px rgba(0,0,0,.3);
  border: 1px solid rgba(255,255,255,.2);
}}

#cfs-root .cfs-scale-seg {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  text-align: center;
}}

#cfs-root .cfs-seg-critical {{
  background: linear-gradient(90deg, #b91c1c 0%, #ef4444 100%);
}}

#cfs-root .cfs-seg-warning {{
  background: linear-gradient(90deg, #d97706 0%, #f59e0b 100%);
}}

#cfs-root .cfs-seg-good {{
  background: linear-gradient(90deg, #0284c7 0%, #0ea5e9 100%);
}}

#cfs-root .cfs-seg-elite {{
  background: linear-gradient(90deg, #059669 0%, #10b981 100%);
}}

#cfs-root .cfs-seg-range {{
  font-size: .72rem;
  font-weight: 900;
  color: #ffffff;
  text-shadow: 0 1px 3px rgba(0,0,0,.7);
  line-height: 1;
}}

#cfs-root .cfs-seg-name {{
  font-size: .64rem;
  font-weight: 700;
  color: rgba(255,255,255,.95);
  text-shadow: 0 1px 2px rgba(0,0,0,.7);
  text-transform: uppercase;
  letter-spacing: .03em;
  margin-top: 1px;
}}

/* Teaser Stats Cards */
#cfs-root .cfs-teaser-stats {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.25rem;
  margin: 2rem 0;
}}

@media (min-width: 640px) {{
  #cfs-root .cfs-teaser-stats {{
    grid-template-columns: repeat(3, 1fr);
  }}
}}

#cfs-root .cfs-stat-card {{
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 12px;
  padding: 1.25rem 1rem;
  text-align: center;
}}

#cfs-root .cfs-stat-title {{
  font-size: .84rem;
  font-weight: 700;
  color: #cbd5e1;
  text-transform: uppercase;
  letter-spacing: .04em;
  margin-bottom: .35rem;
}}

#cfs-root .cfs-stat-num {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.6rem, 3.5vw, 2.2rem);
  font-weight: 900;
  color: var(--white);
}}

#cfs-root .cfs-stat-num--gold {{
  color: var(--gold-light);
}}

#cfs-root .cfs-stat-num--alert {{
  color: #f87171;
}}

#cfs-root .cfs-teaser-copy {{
  font-size: 1rem;
  line-height: 1.7;
  color: #e2e8f0;
  max-width: 760px;
  margin: 0 auto 1.5rem;
  text-align: center;
}}

#cfs-root .cfs-teaser-curiosity {{
  background: rgba(212,155,40,.18);
  border-left: 4px solid var(--gold);
  border-radius: 6px;
  padding: 1rem 1.35rem;
  margin: 0 auto 2rem;
  max-width: 760px;
  font-size: .95rem;
  line-height: 1.6;
  color: #ffffff;
  text-align: left;
}}

#cfs-root .cfs-report-unlock-banner {{
  background: rgba(4,20,38,.5);
  border: 1.5px solid var(--gold);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}}

/* ==========================================================================
   FULL REPORT SECTION
   ========================================================================== */
#cfs-root .cfs-full-report {{
  background: var(--white);
  border: 1.5px solid var(--grey-light);
  border-radius: 16px;
  padding: clamp(1.75rem, 5vw, 3rem);
  box-shadow: var(--shadow-lg);
  margin-bottom: 2rem;
}}

#cfs-root .cfs-report-header {{
  display: flex;
  flex-direction: column;
  gap: 1rem;
  border-bottom: 2px solid var(--grey-light);
  padding-bottom: 1.5rem;
  margin-bottom: 2rem;
}}

@media (min-width: 680px) {{
  #cfs-root .cfs-report-header {{
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }}
}}

#cfs-root .cfs-report-title {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.5rem, 3.5vw, 2rem);
  font-weight: 900;
  color: var(--navy);
  margin: 0;
}}

#cfs-root .cfs-report-badge {{
  display: inline-flex;
  align-items: center;
  background: var(--gold-pale);
  border: 1.5px solid var(--gold);
  color: var(--gold-dark);
  font-family: "Montserrat", sans-serif;
  font-size: .88rem;
  font-weight: 800;
  padding: .5rem 1.25rem;
  border-radius: var(--pill);
}}

/* Showdown Comparison Matrix Table */
#cfs-root .cfs-table-wrap {{
  width: 100%;
  overflow-x: auto;
  margin: 2rem 0;
  border-radius: 10px;
  border: 1px solid var(--grey-light);
  box-shadow: var(--shadow-sm);
}}

#cfs-root .cfs-matrix-table {{
  width: 100%;
  border-collapse: collapse;
  min-width: 720px;
  text-align: left;
  font-size: .88rem;
}}

#cfs-root .cfs-matrix-table th,
#cfs-root .cfs-matrix-table td {{
  padding: 1.05rem 1.2rem;
  border-bottom: 1px solid var(--grey-light);
  vertical-align: top;
}}

#cfs-root .cfs-matrix-table thead th {{
  background: var(--navy);
  color: var(--white);
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: .92rem;
}}

#cfs-root .cfs-matrix-table thead th.th-highlight {{
  background: #041426;
  border-top: 4px solid var(--gold);
  color: var(--gold-light);
}}

#cfs-root .cfs-matrix-table tbody tr:nth-child(even) {{
  background: var(--off-white);
}}

#cfs-root .cfs-matrix-table tbody tr:hover {{
  background: var(--gold-pale);
}}

#cfs-root .cfs-matrix-table td.td-highlight {{
  background: rgba(212,155,40,.07);
  font-weight: 600;
  color: var(--navy);
  border-left: 2px solid rgba(212,155,40,.35);
  border-right: 2px solid rgba(212,155,40,.35);
}}

/* Booking Callout Card */
#cfs-root .cfs-booking-card {{
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-dark) 100%);
  color: var(--white);
  border: 2px solid var(--gold);
  border-radius: 14px;
  padding: clamp(1.75rem, 5vw, 2.5rem);
  text-align: center;
  margin-top: 2.5rem;
}}

#cfs-root .cfs-booking-card h4 {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.3rem, 3vw, 1.75rem);
  font-weight: 800;
  color: var(--white);
  margin: 0 0 .65rem 0;
}}

#cfs-root .cfs-booking-card p {{
  color: #cbd5e1;
  font-size: .98rem;
  max-width: 650px;
  margin: 0 auto 1.5rem auto;
  line-height: 1.6;
}}

/* Compliance Disclosures */
#cfs-root .cfs-disclosures {{
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--grey-light);
  font-size: .76rem;
  line-height: 1.55;
  color: var(--grey-text);
}}

#cfs-root .cfs-disclosures h5 {{
  font-family: "Montserrat", sans-serif;
  font-size: .82rem;
  font-weight: 700;
  color: var(--navy);
  margin: 0 0 .5rem 0;
  text-transform: uppercase;
  letter-spacing: .04em;
}}

/* ==========================================================================
   BENEFITS SECTION - FULL-BLEED
   ========================================================================== */
#cfs-root .cfs-benefits {{
  width: 100% !important;
  padding: clamp(3rem, 7vw, 5rem) clamp(1rem, 4vw, 2.5rem);
  background: var(--off-white);
  text-align: center;
  border-top: 1px solid var(--grey-light);
  margin: 0 !important;
}}

#cfs-root .cfs-benefits-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  max-width: 1080px;
  margin: 2.5rem auto 0 auto;
}}

@media (min-width: 800px) {{
  #cfs-root .cfs-benefits-grid {{
    grid-template-columns: repeat(4, 1fr);
  }}
}}

#cfs-root .cfs-benefit-item {{
  background: var(--white);
  border: 1px solid var(--grey-light);
  border-radius: var(--radius);
  padding: 1.75rem 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .85rem;
  transition: transform var(--t), box-shadow var(--t);
}}

#cfs-root .cfs-benefit-item:hover {{
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
}}

#cfs-root .cfs-benefit-icon {{
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--gold-pale);
  border: 1.5px solid var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.6rem;
  color: var(--gold-dark);
}}

#cfs-root .cfs-benefit-label {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(.82rem, 2.5vw, .95rem);
  font-weight: 800;
  color: var(--navy);
  line-height: 1.35;
  margin: 0;
}}

/* ==========================================================================
   FOOTER - REFINED PRESTIGE CORPORATE SEAL & FULL-BLEED
   ========================================================================== */
#cfs-root .cfs-footer {{
  width: 100% !important;
  background: var(--navy-dark);
  border-top: 3px solid var(--gold);
  padding: clamp(3rem, 6vw, 4.5rem) clamp(1rem, 4vw, 2.5rem);
  text-align: center;
  color: var(--white);
  position: relative;
  margin: 0 !important;
}}

#cfs-root .cfs-footer-brand {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}}

/* Prestige corporate seal frame */
#cfs-root .cfs-footer-crest-frame {{
  width: clamp(120px, 18vw, 160px);
  height: clamp(90px, 14vw, 120px);
  border-radius: 18px;
  overflow: hidden;
  border: 2.5px solid var(--gold);
  box-shadow: 0 10px 35px rgba(0,0,0,.55), 0 0 25px rgba(212,155,40,.25);
  background: #041426;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform .3s ease, box-shadow .3s ease;
}}

#cfs-root .cfs-footer-crest-frame:hover {{
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 14px 40px rgba(0,0,0,.65), 0 0 35px rgba(212,155,40,.4);
}}

#cfs-root .cfs-footer-crest-frame img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}}

#cfs-root .cfs-footer-brand-title {{
  font-family: "Montserrat", sans-serif;
  font-size: clamp(1.25rem, 3.2vw, 1.7rem);
  font-weight: 900;
  letter-spacing: .06em;
  color: var(--white);
  margin: 0;
  text-transform: uppercase;
}}

#cfs-root .cfs-footer-brand-title span {{
  color: var(--gold-light);
}}

#cfs-root .cfs-footer-corp-sub {{
  font-family: "Montserrat", sans-serif;
  font-size: .82rem;
  font-weight: 800;
  letter-spacing: .15em;
  color: var(--gold);
  text-transform: uppercase;
  margin-top: -4px;
}}

#cfs-root .cfs-footer-motto {{
  font-size: clamp(.85rem, 2vw, .95rem);
  color: #cbd5e1;
  font-style: italic;
  margin: 0;
  max-width: 580px;
  line-height: 1.5;
}}

#cfs-root .cfs-footer-disc {{
  max-width: 820px;
  margin: 0 auto 1.5rem auto;
  font-size: .78rem;
  line-height: 1.6;
  color: #94a3b8;
}}

#cfs-root .cfs-footer-links {{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}}

#cfs-root .cfs-footer-links a {{
  color: #cbd5e1;
  text-decoration: none;
  font-size: .84rem;
  font-weight: 600;
  transition: color var(--t);
}}

#cfs-root .cfs-footer-links a:hover {{
  color: var(--gold-light);
}}

#cfs-root .cfs-footer-copy {{
  font-size: .78rem;
  color: #64748b;
  margin: 0;
}}
</style>

  <!-- Brand Navigation Header -->
  <header class="cfs-brand-bar" role="banner">
    <div class="cfs-brand-inner">
      <a href="#cfs-root" class="cfs-brand-logo-wrap" aria-label="BrightPath Legacy Wealth Home">
        <div class="cfs-brand-crest-frame">
          <img
            src="data:image/webp;base64,{logo_b64}"
            alt="BrightPath Legacy Wealth Crest"
            class="cfs-brand-logo-img"
          />
        </div>
        <div class="cfs-brand-wordmark">
          <div class="cfs-brand-company-name">BRIGHT<span>PATH</span></div>
          <div class="cfs-brand-tagline-text">LEGACY WEALTH CORPORATION</div>
          <div class="cfs-brand-sub-motto">Empowering Every Child's Financial Future</div>
        </div>
      </a>
      <div class="cfs-brand-badge" aria-label="Official Evaluation">
        <span class="cfs-badge-dot" aria-hidden="true"></span>
        <span>Official College Funding Analysis</span>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="cfs-hero" aria-label="College funding comparison hero">
    <div class="cfs-hero-container">
      
      <!-- Left Column: Headline, Copy & Action -->
      <div class="cfs-hero-content">
        <p class="cfs-eyebrow">The Ultimate College Funding Showdown</p>

        <h1 class="cfs-h1">
          There&rsquo;s More Than One Way<br />to Pay for College
        </h1>

        <p class="cfs-sub">
          Compare Trump Accounts, 529 Plans, and a Flexible Insurance
          Option in 60 seconds &mdash; and discover which strategy aligns with your family&rsquo;s goals.
        </p>

        <div class="cfs-btn-wrap">
          <a
            href="#cfs-calculator" id="cta-hero"
            class="cfs-btn"
            role="button"
            aria-label="Get My Free College Funding Score"
          ><span>Get My Free College Funding Score</span><span class="cfs-btn-arrow" aria-hidden="true">&rarr;</span></a>
        </div>

        <p class="cfs-hero-note">Free &bull; No obligation &bull; Under 60 seconds</p>
      </div>

      <!-- Right Column: Hero Image (College Savings Flyer) -->
      <div class="cfs-hero-visual">
        <div class="cfs-hero-image-frame">
          <img
            src="data:image/webp;base64,{flyer_b64}"
            alt="Today's Plans Build Tomorrow's Dreams - BrightPath College Funding"
            loading="eager"
            width="540"
            height="540"
          />
          <div class="cfs-hero-badge">
            <span class="cfs-hero-badge-icon" aria-hidden="true">&#9733;</span>
            <div>
              <strong>3-Way Showdown</strong>
              <span>529 vs Trump Acct vs Life Ins</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- SIDE-BY-SIDE COMPARISON SECTION (Positioned Prior to Calculator) -->
  <section class="cfs-compare" id="cfs-compare" aria-label="Compare college-funding options">
    <div class="cfs-section-intro">
      <p class="cfs-eyebrow">Side-by-Side Comparison</p>
      <h2 class="cfs-h2">Which Strategy Wins for Your Family?</h2>
      <p>
        Not all college-savings vehicles are created equal. Here&rsquo;s
        what each option actually delivers &mdash; and what it costs in
        control, flexibility, and long-term wealth.
      </p>
    </div>

    <!-- 3 Tiles Rearranged in Requested Order: 1. Traditional, 2. Trump Acct, 3. Flexible Life Insurance Option -->
    <div class="cfs-card-grid" role="list">
      
      <!-- Tile 1: Traditional -->
      <article class="cfs-card" role="listitem">
        <div class="cfs-card-icon" aria-hidden="true">&#127891;</div>
        <h3 class="cfs-card-title">Traditional College Savings Plans</h3>
        <p class="cfs-card-sub">529 Plans &amp; Coverdell ESAs</p>
        <p class="cfs-card-desc">
          529s offer tax-deferred growth, but contributions are capped,
          withdrawals are strictly restricted to qualified education expenses,
          and stock market downturns directly threaten your balance before enrollment.
        </p>
        <div class="cfs-card-tags">
          <span class="cfs-tag cfs-tag--good">Tax Deferred</span>
          <span class="cfs-tag cfs-tag--bad">Education-Only Mandate</span>
          <span class="cfs-tag cfs-tag--bad">Market Volatility Risk</span>
          <span class="cfs-tag cfs-tag--bad">Reduces FAFSA Aid (Up to 5.64%/yr)</span>
        </div>
      </article>

      <!-- Tile 2: Trump Acct -->
      <article class="cfs-card" role="listitem">
        <div class="cfs-card-icon" aria-hidden="true">&#127963;&#65039;</div>
        <h3 class="cfs-card-title">Trump Accounts</h3>
        <p class="cfs-card-sub">Federal College &amp; Career Initiative</p>
        <p class="cfs-card-desc">
          Government-backed savings accounts with strict statutory rules on contributions,
          withdrawals, and qualifying expenses &mdash; leaving families with limited flexibility
          and uncertain future regulatory adjustments.
        </p>
        <div class="cfs-card-tags">
          <span class="cfs-tag cfs-tag--bad">Strict Statutory Rules</span>
          <span class="cfs-tag cfs-tag--bad">Limited Contribution Room</span>
          <span class="cfs-tag">New &amp; Evolving Structure</span>
          <span class="cfs-tag cfs-tag--bad">Government Oversight</span>
        </div>
      </article>

      <!-- Tile 3: Flexible Life Insurance Option -->
      <article class="cfs-card cfs-card--featured" role="listitem">
        <div class="cfs-card-icon" aria-hidden="true">&#128737;&#65039;</div>
        <h3 class="cfs-card-title">Flexible Life Insurance Option</h3>
        <p class="cfs-card-sub">Structured Cash-Value Strategy</p>
        <p class="cfs-card-desc">
          A properly structured cash-value life insurance strategy grows wealth tax-advantaged,
          protects your family with immediate coverage, and funds college &mdash; or a home, business,
          or retirement &mdash; completely on your terms with <strong>zero market downside loss</strong>.
        </p>
        <div class="cfs-card-tags">
          <span class="cfs-tag cfs-tag--gold">Exempt from FAFSA Form</span>
          <span class="cfs-tag cfs-tag--good">Zero Market Downside Risk</span>
          <span class="cfs-tag cfs-tag--good">100% Tax-Advantaged Access</span>
          <span class="cfs-tag cfs-tag--good">Use for Any Life Purpose</span>
        </div>
      </article>

    </div>

    <div class="cfs-callout">
      <strong>Discover the strategy that helps you save for college while building lasting wealth.</strong>
      Run your free funding score below &mdash; zero obligation, just personalized clarity.
    </div>

    <div style="text-align: center;">
      <a
        href="#cfs-calculator" id="cta-secondary"
        class="cfs-btn"
        role="button"
        aria-label="Start My Free College Funding Calculator"
      ><span>Start My Free Funding Calculator</span><span class="cfs-btn-arrow" aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

  <!-- SHOWDOWN CALCULATOR SECTION -->
  <section class="cfs-calculator-section" id="cfs-calculator" aria-label="College Funding Showdown Calculator">
    <div class="cfs-calc-container">
      
      <div class="cfs-section-intro" style="margin-bottom: 1.25rem;">
        <p class="cfs-eyebrow">Interactive Self-Service Analysis</p>
        <h2 class="cfs-h2">The College Funding Showdown Calculator</h2>
        <p>
          Compare your family&rsquo;s current college trajectory against the 3 major options. Calculate your personalized <strong>College Funding Score</strong> and uncover your projected funding gap in 60 seconds.
        </p>
      </div>

      <!-- Calculator Inputs & Mandatory Verification Opt-In Card -->
      <div class="cfs-calc-card" id="cfs-calc-input-card">
        <form id="cfs-calculator-form" onsubmit="return false;">
          
          <!-- STEP 1: College Parameters -->
          <div class="cfs-calc-step-header">
            <span class="cfs-step-pill">Step 1</span>
            <div>
              <h3 class="cfs-step-title">Your College Savings Parameters</h3>
              <p class="cfs-step-sub">Adjust the sliders to reflect your current college savings horizon and targets.</p>
            </div>
          </div>

          <div class="cfs-calc-grid">
            <!-- Child's Age Slider -->
            <div class="cfs-input-group cfs-input-group--full">
              <label for="cfs-child-age" class="cfs-label">
                <span>Child&rsquo;s Current Age</span>
                <span class="cfs-label-val" id="cfs-age-display">Age 5 (Starts College in 2039)</span>
              </label>
              <input type="range" id="cfs-child-age" class="cfs-range" min="0" max="17" value="5" step="1" />
              <div class="cfs-range-ticks">
                <span>Newborn (0)</span><span>Age 5</span><span>Age 10</span><span>Age 15</span><span>High School (17)</span>
              </div>
              <p class="cfs-hint">Time Horizon: <strong id="cfs-years-left">13 years</strong> until college enrollment (Age 18).</p>
            </div>

            <!-- Current Savings Slider -->
            <div class="cfs-input-group">
              <label for="cfs-current-savings" class="cfs-label">
                <span>Current College Savings ($)</span>
                <span class="cfs-label-val" id="cfs-savings-display">$15,000</span>
              </label>
              <input type="range" id="cfs-current-savings" class="cfs-range" min="0" max="150000" value="15000" step="1000" />
              <div class="cfs-range-ticks">
                <span>$0</span><span>$50k</span><span>$100k</span><span>$150k</span>
              </div>
            </div>

            <!-- Monthly Savings Contribution Slider -->
            <div class="cfs-input-group">
              <label for="cfs-monthly-savings" class="cfs-label">
                <span>Planned Monthly Savings ($/mo)</span>
                <span class="cfs-label-val" id="cfs-monthly-display">$350/mo</span>
              </label>
              <input type="range" id="cfs-monthly-savings" class="cfs-range" min="50" max="2500" value="350" step="25" />
              <div class="cfs-range-ticks">
                <span>$50/mo</span><span>$500/mo</span><span>$1,000/mo</span><span>$2,500/mo</span>
              </div>
            </div>

            <!-- College Target Benchmark Dropdown -->
            <div class="cfs-input-group cfs-input-group--full">
              <label for="cfs-college-benchmark" class="cfs-label">
                <span>Estimated Target 4-Year College Cost Benchmark</span>
                <span class="cfs-label-val" id="cfs-benchmark-display">$110,000 (In-State Public)</span>
              </label>
              <select id="cfs-college-benchmark" class="cfs-select-box">
                <option value="110000" selected>In-State 4-Year Public University ($110,000 total)</option>
                <option value="180000">Out-of-State 4-Year Public University ($180,000 total)</option>
                <option value="240000">Private 4-Year Non-Profit College ($240,000 total)</option>
                <option value="350000">Elite Private / Healthcare Pre-Med ($350,000 total)</option>
              </select>
              <p class="cfs-hint">Benchmark estimates reflect current 4-year tuition, fees, room, and board with projected cost inflation.</p>
            </div>
          </div>

          <!-- STEP 2: Mandatory Opt-In to Receive Score Inputs & Preliminary Results -->
          <div class="cfs-calc-step-header" style="margin-top: 2.25rem;">
            <span class="cfs-step-pill">Step 2</span>
            <div>
              <h3 class="cfs-step-title">Where Should We Send Your Score &amp; Preliminary Results?</h3>
              <p class="cfs-step-sub">Mandatory opt-in required to calculate and view your college funding score inputs.</p>
            </div>
          </div>

          <div class="cfs-form-grid" style="margin-top: 1rem;">
            <div class="cfs-form-group">
              <label for="cfs-user-name" class="cfs-label">Full Name *</label>
              <input type="text" id="cfs-user-name" class="cfs-form-input" placeholder="e.g. Sarah Jenkins" required />
            </div>

            <div class="cfs-form-group">
              <label for="cfs-user-email" class="cfs-label">Email Address *</label>
              <input type="email" id="cfs-user-email" class="cfs-form-input" placeholder="sarah@example.com" required />
            </div>

            <div class="cfs-form-group">
              <label for="cfs-user-phone" class="cfs-label">Phone Number *</label>
              <input type="tel" id="cfs-user-phone" class="cfs-form-input" placeholder="(555) 000-0000" required />
            </div>

            <div class="cfs-form-group">
              <label for="cfs-user-concern" class="cfs-label">Biggest College Funding Concern</label>
              <select id="cfs-user-concern" class="cfs-select-box">
                <option value="Financial Aid Impact">Losing financial aid/FAFSA eligibility due to 529 assets</option>
                <option value="Market Risk">Market volatility wiping out savings right before college</option>
                <option value="Non-College Penalties">Penalties/taxes if child gets a scholarship or skips college</option>
                <option value="Not Saving Enough">Falling short of high future tuition bills</option>
                <option value="Lack of Flexibility">Wanting funds to also be usable for a home, business, or life</option>
              </select>
            </div>

            <!-- Captcha Security Verification Code -->
            <div class="cfs-form-group--full cfs-captcha-container">
              <label for="cfs-captcha-input" class="cfs-label">Security Verification Code *</label>
              <div class="cfs-captcha-row">
                <div class="cfs-captcha-badge" id="cfs-captcha-display" aria-label="Security verification code">
                  <span id="cfs-captcha-text">7K9M2</span>
                </div>
                <button type="button" id="cfs-btn-refresh-captcha" class="cfs-captcha-refresh-btn" title="Get new security code" aria-label="Get new security code">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
                  <span>Refresh Code</span>
                </button>
                <input type="text" id="cfs-captcha-input" class="cfs-form-input cfs-captcha-input" placeholder="Enter code above" maxlength="6" required autocomplete="off" />
              </div>
              <p class="cfs-hint">Verification code prevents false submissions and ensures delivery to valid contact info.</p>
            </div>

            <div class="cfs-form-group--full">
              <label class="cfs-consent-wrap">
                <input type="checkbox" id="cfs-tcpa-consent" checked required />
                <span>
                  I consent to receive text messages, phone calls, and emails regarding my College Funding Showdown Report from BrightPath Legacy Wealth Corporation at the number provided. Message &amp; data rates may apply. Message frequency varies. Reply STOP to cancel. I acknowledge that I have read the Privacy Policy and Disclosures.
                </span>
              </label>
            </div>

            <div id="cfs-form-error-msg" class="cfs-form-error" style="display:none;" role="alert"></div>

            <div class="cfs-form-group--full" style="text-align: center; margin-top: .75rem;">
              <button type="button" id="cfs-btn-calculate" class="cfs-btn cfs-btn--lg">
                <span>Calculate &amp; Unlock My College Funding Score</span>
                <span class="cfs-btn-arrow" aria-hidden="true">&rarr;</span>
              </button>
            </div>
          </div>
        </form>
      </div>

      <!-- TEASER RESULTS: Gated until valid opt-in is submitted -->
      <div class="cfs-teaser-box" id="cfs-teaser-box" role="region" aria-live="polite" style="display: none;">
        
        <div class="cfs-teaser-header">
          <span class="cfs-teaser-pill">Preliminary Evaluation</span>
          <h3 class="cfs-teaser-headline">
            My College Funding Scorecard
          </h3>
          <p style="color: rgba(255,255,255,0.85); font-size: .95rem; margin: 0 0 1rem 0;">
            Personalized Analysis Prepared for: <strong id="cfs-teaser-client-name" style="color:var(--gold-light);">Valued Family</strong>
          </p>

          <!-- EMPHASIZED CALCULATOR SCALE (PROMINENT GAUGE & BANDS) -->
          <div class="cfs-prominent-scale-card">
            <div class="cfs-scale-top">
              <div class="cfs-scale-badge-wrap">
                <span class="cfs-scale-score-main" id="cfs-teaser-score-val">74</span>
                <span class="cfs-scale-score-denominator">/ 100</span>
              </div>
              <div>
                <div class="cfs-scale-status-title" id="cfs-readiness-status">
                  Moderate Readiness &mdash; Funding Gap Identified
                </div>
                <div class="cfs-scale-status-desc">
                  Your current trajectory leaves you exposed to market drops and tuition inflation shortfalls.
                </div>
              </div>
            </div>

            <!-- 4-Band Segmented Progress Scale Bar with Dynamic Pointer -->
            <div class="cfs-scale-bar-wrapper">
              <div class="cfs-scale-pointer-container">
                <div class="cfs-scale-pointer" id="cfs-scale-pointer" style="left: 74%;">
                  <div class="cfs-pointer-bubble" id="cfs-pointer-bubble">My Score: 74</div>
                  <div class="cfs-pointer-arrow"></div>
                </div>
              </div>
              
              <div class="cfs-scale-track">
                <div class="cfs-scale-seg cfs-seg-critical" title="0-49: Critical Funding Gap">
                  <span class="cfs-seg-range">0 - 49</span>
                  <span class="cfs-seg-name">Critical Gap</span>
                </div>
                <div class="cfs-scale-seg cfs-seg-warning" title="50-69: Action Needed">
                  <span class="cfs-seg-range">50 - 69</span>
                  <span class="cfs-seg-name">Action Needed</span>
                </div>
                <div class="cfs-scale-seg cfs-seg-good" title="70-84: On Track">
                  <span class="cfs-seg-range">70 - 84</span>
                  <span class="cfs-seg-name">On Track</span>
                </div>
                <div class="cfs-scale-seg cfs-seg-elite" title="85-100: Fully Shielded">
                  <span class="cfs-seg-range">85 - 100</span>
                  <span class="cfs-seg-name">Fully Shielded</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="cfs-teaser-stats">
          <div class="cfs-stat-card">
            <div class="cfs-stat-title">Estimated 4-Year Cost</div>
            <div class="cfs-stat-num" id="cfs-stat-target">$110,000</div>
          </div>
          <div class="cfs-stat-card">
            <div class="cfs-stat-title">Projected Savings</div>
            <div class="cfs-stat-num cfs-stat-num--gold" id="cfs-stat-projected">$86,400</div>
          </div>
          <div class="cfs-stat-card">
            <div class="cfs-stat-title">Projected Funding Gap</div>
            <div class="cfs-stat-num cfs-stat-num--alert" id="cfs-stat-gap">$23,600</div>
          </div>
        </div>

        <p class="cfs-teaser-copy" id="cfs-teaser-narrative">
          Based on your inputs, you have a projected savings gap of <strong id="cfs-narrative-gap">$23,600</strong>. 
          While traditional 529 plans lock your funds into rigid education-only mandates with market risk, and Trump Accounts face strict statutory limits, 
          the <strong>Flexible Insurance Option</strong> offers a protected alternative that builds wealth with zero market downside loss.
        </p>

        <div class="cfs-teaser-curiosity">
          <strong>Curiosity Insight:</strong> Did you know cash-value life insurance is <em>completely exempt</em> from the FAFSA financial aid formula, while 529 plans can reduce financial aid eligibility by up to 5.64% per year?
        </div>

        <p style="font-size:0.75rem; color:rgba(255,255,255,0.65); text-align:center; margin-bottom:1.5rem;">
          *This is a hypothetical illustration based on an assumed 6.0% illustrative annual rate of return. It is not a guarantee of future performance. Actual values will vary.
        </p>

        <div class="cfs-report-unlock-banner">
          <p style="margin: 0 0 0.85rem 0; font-weight: 700; font-size: 1.05rem; color: #fff;">
            Your complete 3-way showdown comparison analysis is unlocked below.
          </p>
          <a href="#cfs-full-report" class="cfs-btn">
            <span>View My Full 3-Way Showdown Report</span>
            <span class="cfs-btn-arrow" aria-hidden="true">&darr;</span>
          </a>
        </div>
      </div>

      <!-- FULL REPORT SECTION (Unlocked after opt-in) -->
      <div class="cfs-full-report" id="cfs-full-report" style="display: none;">
        
        <div class="cfs-report-header">
          <div>
            <h3 class="cfs-report-title">My Full 3-Way Showdown Report</h3>
            <p style="color:var(--grey-text); margin:0.35rem 0 0 0; font-size:0.95rem;">
              Prepared for: <strong id="cfs-report-client-name">Valued Family</strong> &bull; Personalized Strategy Analysis
            </p>
          </div>
          <div class="cfs-report-badge">
            Score: <span id="cfs-report-score-display">74</span>/100 &bull; Verified
          </div>
        </div>

        <!-- Executive Summary Recap -->
        <div style="background:var(--gold-pale); border:1px solid rgba(212,155,40,0.35); border-radius:10px; padding:1.25rem 1.5rem; margin-bottom:2rem;">
          <p style="margin:0; font-size:.92rem; color:var(--navy); line-height:1.6;" id="cfs-report-summary-text">
            <strong>Analysis Summary:</strong> For your child starting college in <span id="cfs-sum-year">2039</span>, projected 4-year tuition benchmark is <span id="cfs-sum-cost">$110,000</span>. At your planned savings rate, you are projected to accumulate <span id="cfs-sum-saved">$86,400</span>, leaving a projected funding gap of <span id="cfs-sum-gap">$23,600</span>. Below is your complete side-by-side evaluation of how Trump Accounts, Traditional 529s, and the Flexible Life Insurance Option address this gap.
          </p>
        </div>

        <!-- 3-Way Side-by-Side Comparison Matrix Table -->
        <div class="cfs-table-wrap">
          <table class="cfs-matrix-table" aria-label="College Funding Comparison Table">
            <thead>
              <tr>
                <th style="width: 25%;">Decision Criteria</th>
                <th style="width: 25%;">1. Traditional 529 / ESA</th>
                <th style="width: 25%;">2. Trump Account</th>
                <th class="th-highlight" style="width: 25%;">3. Flexible Life Insurance Option</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Contribution Limits</strong></td>
                <td>High state maximums ($300k-$500k aggregate), subject to federal gift tax limits.</td>
                <td>Strict government annual statutory cap ($5,000/yr). Strict eligibility rules.</td>
                <td class="td-highlight">&#10004; Flexible funding structured to parent&rsquo;s cash flow &amp; capacity.</td>
              </tr>
              <tr>
                <td><strong>Tax-Free Growth &amp; Distributions</strong></td>
                <td>Tax-free only for IRS-qualified education expenses.</td>
                <td>Tax-advantaged for authorized educational/training uses only.</td>
                <td class="td-highlight">&#10004; Tax-free cash-value growth &amp; tax-free distributions via policy loans.</td>
              </tr>
              <tr>
                <td><strong>FAFSA Financial Aid Impact</strong></td>
                <td>Counted as parental asset (assessed up to 5.64%/yr against student aid).</td>
                <td>Expected to be counted as student/parent asset, potentially reducing aid.</td>
                <td class="td-highlight">&#10004; <strong>100% EXEMPT from FAFSA formula.</strong> Does not reduce financial aid.</td>
              </tr>
              <tr>
                <td><strong>Market Downside Protection</strong></td>
                <td>No downside protection. Market crashes right before college can severely cut savings.</td>
                <td>Exposed to underlying federal investment portfolio risks.</td>
                <td class="td-highlight">&#10004; <strong>Zero Downside Risk.</strong> Guaranteed annual floor protects all principal &amp; gains.</td>
              </tr>
              <tr>
                <td><strong>Withdrawal Restrictions</strong></td>
                <td>Strict. 10% federal penalty + income tax on earnings if used for non-college purposes.</td>
                <td>Rigid rules on qualifying expenses and approved institutions.</td>
                <td class="td-highlight">&#10004; <strong>Unrestricted.</strong> Use for college, first home, business launch, or emergencies.</td>
              </tr>
              <tr>
                <td><strong>Non-College Flexibility</strong></td>
                <td>Rigid. Can roll up to $35k to Roth IRA (after 15 yrs) or change beneficiary to family.</td>
                <td>Locked into statutory career/education program rules.</td>
                <td class="td-highlight">&#10004; <strong>Full Ownership.</strong> Child gets a lifetime financial asset with no penalties.</td>
              </tr>
              <tr>
                <td><strong>Family Protection &amp; Death Benefit</strong></td>
                <td>None. Account balance only. If parent passes, funding ceases.</td>
                <td>None. No life insurance protection component.</td>
                <td class="td-highlight">&#10004; <strong>Self-Completing.</strong> Substantial tax-free death benefit ensures college is funded.</td>
              </tr>
              <tr>
                <td><strong>Creditor &amp; Asset Protection</strong></td>
                <td>Varies widely by state statute; limited federal bankruptcy protection.</td>
                <td>Subject to statutory federal limits.</td>
                <td class="td-highlight">&#10004; High statutory protection in most states for life insurance cash value.</td>
              </tr>
              <tr>
                <td><strong>Tax-Free Policy Loans &amp; Liquidity</strong></td>
                <td>Not permitted. Cannot borrow against a 529 account.</td>
                <td>Not permitted. Funds locked until distribution eligibility.</td>
                <td class="td-highlight">&#10004; Access cash value anytime via policy loans without IRS qualification triggers.</td>
              </tr>
              <tr>
                <td><strong>Generational Wealth Transfer</strong></td>
                <td>Limited to changing account beneficiary across generations.</td>
                <td>Strict beneficiary distribution rules upon maturity.</td>
                <td class="td-highlight">&#10004; Transfers wealth income-tax-free to heirs via death benefit.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Strategy Session Booking Card -->
        <div class="cfs-booking-card">
          <h4>Review My College Funding Score with a Specialist</h4>
          <p>
            Your personalized report indicates opportunities to eliminate your projected funding gap while shielding your assets from FAFSA calculations and stock market volatility. Book a complimentary 15-minute Strategy Review.
          </p>
          <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
            <a
              href="https://api.leadconnectorhq.com/widget/booking"
              target="_blank"
              rel="noopener noreferrer"
              class="cfs-btn"
            >
              <span>Schedule My Strategy Review</span>
              <span class="cfs-btn-arrow" aria-hidden="true">&rarr;</span>
            </a>
          </div>
          <p style="font-size:0.78rem; color:rgba(255,255,255,0.7); margin-top:1rem; margin-bottom:0;">
            100% Free Consultation &bull; Licensed Professionals &bull; No Obligation
          </p>
        </div>

        <!-- Compliance & Regulatory Disclosures -->
        <div class="cfs-disclosures">
          <h5>Required Compliance &amp; Illustrative Disclosures</h5>
          <p>
            <strong>Hypothetical Illustration Notice:</strong> This comparison and calculator tool provide hypothetical illustrations based on an assumed 6.0% illustrative annual rate of return. It is not a guarantee of future performance. Actual policy values and growth will vary based on premiums paid, policy charges, cost of insurance, and actual (non-guaranteed) performance. See your carrier&rsquo;s official policy illustration for guaranteed and non-guaranteed values.
          </p>
          <p>
            <strong>Non-Guaranteed Features &amp; Advice Limitation:</strong> BrightPath Legacy Wealth Corporation professionals hold insurance licenses. This campaign and report are governed by state insurance advertising rules (following NAIC Life Insurance Illustrations and Advertisements Regulations) and evaluate general structural features &mdash; flexibility, access, control, and tax treatment &mdash; rather than investment performance. This material does not constitute securities, investment, tax, or legal advice.
          </p>
          <p>
            <strong>Tax Law &amp; State Specificity:</strong> Federal and state tax laws, Trump Account statutory frameworks, 529 plan rules, and FAFSA guidelines are subject to legislative change. Tax-free distributions from life insurance assume the policy remains in force and is not a Modified Endowment Contract (MEC). Consult your qualified tax professional and licensed advisor for personalized guidance.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- Benefits Section -->
  <section class="cfs-benefits" aria-label="Key benefits">
    <div class="cfs-section-intro" style="margin-bottom:0;">
      <p class="cfs-eyebrow">Why Families Choose This Approach</p>
      <h2 class="cfs-h2">Multiple Strategies. Four Powerful Outcomes.</h2>
    </div>

    <div class="cfs-benefits-grid">
      <div class="cfs-benefit-item">
        <div class="cfs-benefit-icon" aria-hidden="true">&#128737;&#65039;</div>
        <p class="cfs-benefit-label">Protect What<br />Matters Most</p>
      </div>

      <div class="cfs-benefit-item">
        <div class="cfs-benefit-icon" aria-hidden="true">&#128200;</div>
        <p class="cfs-benefit-label">Build Wealth<br />That Lasts</p>
      </div>

      <div class="cfs-benefit-item">
        <div class="cfs-benefit-icon" aria-hidden="true">&#127891;</div>
        <p class="cfs-benefit-label">Fund Their<br />Education</p>
      </div>

      <div class="cfs-benefit-item">
        <div class="cfs-benefit-icon" aria-hidden="true">&#128273;</div>
        <p class="cfs-benefit-label">Create Financial<br />Freedom</p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="cfs-footer" role="contentinfo">
    <div class="cfs-footer-brand">
      <div class="cfs-footer-crest-frame">
        <img
          src="data:image/webp;base64,{logo_b64}"
          alt="BrightPath Legacy Wealth Official Crest"
          class="cfs-footer-logo"
        />
      </div>
      <div class="cfs-footer-brand-title">BRIGHT<span>PATH</span></div>
      <div class="cfs-footer-corp-sub">LEGACY WEALTH CORPORATION</div>
      <p class="cfs-footer-motto">
        Empowering Every Child&rsquo;s Financial Future &bull; From Birth and Beyond
      </p>
    </div>

    <p class="cfs-footer-disc">
      This material is for informational and educational purposes only and does not constitute financial, tax, or legal advice. Insurance products and wealth planning strategies are subject to individual qualifications and underwriting approval. Cash values and benefits may vary. Past performance is not indicative of future results. Consult a licensed professional at BrightPath Legacy Wealth Corporation before making any financial decision.
    </p>

    <div class="cfs-footer-links">
      <a href="#">Privacy Policy</a>
      <a href="#">Terms of Use</a>
      <a href="#">Disclosures</a>
      <a href="#">Contact Us</a>
    </div>

    <p class="cfs-footer-copy">&copy; 2026 BrightPath Legacy Wealth Corporation. All rights reserved.</p>
  </footer>

</div>

<script>
(function() {{
  // Elements
  var ageSlider = document.getElementById('cfs-child-age');
  var ageDisplay = document.getElementById('cfs-age-display');
  var yearsLeftDisplay = document.getElementById('cfs-years-left');
  var savingsInput = document.getElementById('cfs-current-savings');
  var savingsDisplay = document.getElementById('cfs-savings-display');
  var monthlyInput = document.getElementById('cfs-monthly-savings');
  var monthlyDisplay = document.getElementById('cfs-monthly-display');
  var benchmarkSelect = document.getElementById('cfs-college-benchmark');
  var benchmarkDisplay = document.getElementById('cfs-benchmark-display');

  // Opt-in & Captcha elements
  var userNameInput = document.getElementById('cfs-user-name');
  var userEmailInput = document.getElementById('cfs-user-email');
  var userPhoneInput = document.getElementById('cfs-user-phone');
  var userConcernSelect = document.getElementById('cfs-user-concern');
  var tcpaConsent = document.getElementById('cfs-tcpa-consent');
  var captchaText = document.getElementById('cfs-captcha-text');
  var captchaInput = document.getElementById('cfs-captcha-input');
  var btnRefreshCaptcha = document.getElementById('cfs-btn-refresh-captcha');
  var formErrorMsg = document.getElementById('cfs-form-error-msg');
  var btnCalculate = document.getElementById('cfs-btn-calculate');

  // Result display containers
  var teaserBox = document.getElementById('cfs-teaser-box');
  var fullReport = document.getElementById('cfs-full-report');

  // Captcha Generator
  var currentCaptcha = '';
  function generateCaptcha() {{
    var chars = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
    var code = '';
    for (var i = 0; i < 5; i++) {{
      code += chars.charAt(Math.floor(Math.random() * chars.length));
    }}
    currentCaptcha = code;
    if (captchaText) {{
      captchaText.textContent = code;
    }}
    if (captchaInput) {{
      captchaInput.value = '';
    }}
  }}

  if (btnRefreshCaptcha) {{
    btnRefreshCaptcha.addEventListener('click', generateCaptcha);
  }}
  generateCaptcha();

  // Format Helpers
  function formatMoney(n) {{
    return '$' + Math.round(n).toLocaleString('en-US');
  }}

  function updateInputDisplays() {{
    var age = parseInt(ageSlider.value, 10);
    var currentYear = 2026;
    var enrollYear = currentYear + (18 - age);
    var yearsLeft = 18 - age;

    ageDisplay.textContent = 'Age ' + age + ' (Starts College in ' + enrollYear + ')';
    yearsLeftDisplay.textContent = yearsLeft + (yearsLeft === 1 ? ' year' : ' years');

    savingsDisplay.textContent = formatMoney(savingsInput.value);
    monthlyDisplay.textContent = formatMoney(monthlyInput.value) + '/mo';

    var bIndex = benchmarkSelect.selectedIndex;
    var bText = benchmarkSelect.options[bIndex].text;
    benchmarkDisplay.textContent = bText;
  }}

  ageSlider.addEventListener('input', updateInputDisplays);
  savingsInput.addEventListener('input', updateInputDisplays);
  monthlyInput.addEventListener('input', updateInputDisplays);
  benchmarkSelect.addEventListener('change', updateInputDisplays);
  updateInputDisplays();

  // Core Math Calculation
  function calculateShowdown() {{
    var age = parseInt(ageSlider.value, 10);
    var years = Math.max(1, 18 - age);
    var currentSavings = parseFloat(savingsInput.value) || 0;
    var monthly = parseFloat(monthlyInput.value) || 0;
    var baseCost = parseFloat(benchmarkSelect.value) || 110000;

    // Projected cost with 3.5% educational inflation
    var targetCost = baseCost * Math.pow(1 + 0.035, years);

    // Projected savings compounding at 6.0% annual rate
    var r = 0.06;
    var futureCurrentSavings = currentSavings * Math.pow(1 + r, years);
    var rm = r / 12;
    var nMonths = years * 12;
    var futureMonthlySavings = monthly * ((Math.pow(1 + rm, nMonths) - 1) / rm);
    var totalProjected = futureCurrentSavings + futureMonthlySavings;

    var gap = Math.max(0, targetCost - totalProjected);
    var fundedRatio = Math.min(1.2, totalProjected / targetCost);

    // Scoring: funded ratio, time horizon, monthly commitment
    var score = Math.round(fundedRatio * 75 + Math.min(20, (monthly / 500) * 15) + Math.min(10, years));
    score = Math.max(20, Math.min(96, score));

    return {{
      age: age,
      years: years,
      targetCost: targetCost,
      totalProjected: totalProjected,
      gap: gap,
      score: score
    }};
  }}

  function showError(msg) {{
    if (formErrorMsg) {{
      formErrorMsg.textContent = msg;
      formErrorMsg.style.display = 'block';
      formErrorMsg.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    }} else {{
      alert(msg);
    }}
  }}

  function clearError() {{
    if (formErrorMsg) {{
      formErrorMsg.textContent = '';
      formErrorMsg.style.display = 'none';
    }}
  }}

  // Action Button Click -> Validate Mandatory Opt-In & Captcha, Then Calculate & Reveal
  btnCalculate.addEventListener('click', function() {{
    clearError();

    var nameVal = userNameInput ? userNameInput.value.trim() : '';
    var emailVal = userEmailInput ? userEmailInput.value.trim() : '';
    var phoneVal = userPhoneInput ? userPhoneInput.value.trim() : '';
    var captchaVal = captchaInput ? captchaInput.value.trim().toUpperCase() : '';

    if (!nameVal) {{
      showError('Please enter your full name.');
      userNameInput.focus();
      return;
    }}

    var emailPattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{{2,}}$/;
    if (!emailVal || !emailPattern.test(emailVal) || emailVal.endsWith('@test.com') || emailVal.endsWith('@asdf.com') || emailVal.endsWith('@example.com')) {{
      showError('Please enter a valid, active email address to receive your report.');
      userEmailInput.focus();
      return;
    }}

    var phoneDigits = phoneVal.replace(/\\D/g, '');
    if (!phoneVal || phoneDigits.length < 10) {{
      showError('Please enter a valid 10-digit phone number.');
      userPhoneInput.focus();
      return;
    }}

    if (!captchaVal || captchaVal !== currentCaptcha.toUpperCase()) {{
      showError('Incorrect verification security code. Please check the code and try again.');
      generateCaptcha();
      captchaInput.focus();
      return;
    }}

    if (tcpaConsent && !tcpaConsent.checked) {{
      showError('Please confirm your consent to receive your personalized analysis.');
      tcpaConsent.focus();
      return;
    }}

    // All validation passed: execute calculation
    var res = calculateShowdown();

    // Populate Teaser Scorecard & Scale
    document.getElementById('cfs-teaser-score-val').textContent = res.score;
    document.getElementById('cfs-teaser-client-name').textContent = nameVal;
    document.getElementById('cfs-stat-target').textContent = formatMoney(res.targetCost);
    document.getElementById('cfs-stat-projected').textContent = formatMoney(res.totalProjected);
    document.getElementById('cfs-stat-gap').textContent = formatMoney(res.gap);
    document.getElementById('cfs-narrative-gap').textContent = formatMoney(res.gap);

    // Update Prominent Scale Position & Needle
    var scalePointer = document.getElementById('cfs-scale-pointer');
    var pointerBubble = document.getElementById('cfs-pointer-bubble');
    if (scalePointer) {{
      // Bound pointer position within visible track (4% to 96%)
      var pointerPos = Math.max(4, Math.min(96, res.score));
      scalePointer.style.left = pointerPos + '%';
    }}
    if (pointerBubble) {{
      pointerBubble.textContent = 'My Score: ' + res.score;
    }}

    // Update Readiness Status Label
    var statusTitle = document.getElementById('cfs-readiness-status');
    if (statusTitle) {{
      if (res.score >= 85) {{
        statusTitle.textContent = 'Excellent Readiness — College Savings Fully Shielded';
      }} else if (res.score >= 70) {{
        statusTitle.textContent = 'Moderate Readiness — Optimization Opportunity';
      }} else if (res.score >= 50) {{
        statusTitle.textContent = 'Needs Action — Noticeable Funding Gap Identified';
      }} else {{
        statusTitle.textContent = 'Critical Action Needed — Significant College Funding Gap';
      }}
    }}

    // Populate Full Report
    document.getElementById('cfs-report-client-name').textContent = nameVal;
    document.getElementById('cfs-report-score-display').textContent = res.score;
    document.getElementById('cfs-sum-year').textContent = 2026 + res.years;
    document.getElementById('cfs-sum-cost').textContent = formatMoney(res.targetCost);
    document.getElementById('cfs-sum-saved').textContent = formatMoney(res.totalProjected);
    document.getElementById('cfs-sum-gap').textContent = formatMoney(res.gap);

    // Reveal Teaser Box & Full Report
    teaserBox.style.display = 'block';
    fullReport.style.display = 'block';

    // Smooth scroll down to the revealed scorecard
    teaserBox.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }});

}})();
</script>

</body>
</html>
'''

# Write index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated index.html, size:", os.path.getsize('index.html'))

# Write college-funding-showdown.html
# Make sure college-funding-showdown.html has the global reset style at the top so opening it standalone in browser has zero margins
ghl_body = re.sub(r'<!DOCTYPE html>.*?<div id="cfs-root">', '<div id="cfs-root">', html_content, flags=re.DOTALL)
ghl_body = re.sub(r'</body>\s*</html>', '', ghl_body, flags=re.DOTALL).strip()

with open('college-funding-showdown.html', 'w', encoding='utf-8') as f:
    f.write(ghl_body)
print("Updated college-funding-showdown.html, size:", os.path.getsize('college-funding-showdown.html'))
