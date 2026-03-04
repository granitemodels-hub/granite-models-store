"""
GRANITE MODELS - Website v4 (Phase 1 Cleanup)
Port: 5055

CHANGES FROM v3:
- Removed broken localhost:6091 redirects
- Removed Request Access form (was redirecting to nowhere)
- Added portfolio banner: "Engineering Portfolio - Actively Rebuilding"
- Removed /systems route (pointed to localhost)
- Stripped all pricing/checkout references
- Clean single-page portfolio placeholder
"""

from flask import Flask, render_template_string, request, redirect
import os
import secrets
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(32))
DEBUG_MODE = False

CSS = '''
:root{--bg:#0a0a0f;--panel:#1a1a2e;--text:#e0e0e0;--muted:#888;--gold:#d4a745;--border:rgba(255,255,255,0.08)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Inter,system-ui,sans-serif;background:var(--bg);color:var(--text)}
a{color:inherit;text-decoration:none}
.banner{background:linear-gradient(135deg,rgba(212,167,69,0.15),rgba(212,167,69,0.05));border-bottom:2px solid var(--gold);padding:12px 40px;text-align:center;font-size:14px;color:var(--gold);font-weight:600;letter-spacing:0.5px}
.nav{border-bottom:1px solid var(--border);padding:20px 40px;display:flex;justify-content:space-between;align-items:center;max-width:1200px;margin:0 auto}
.logo{font-weight:700;font-size:22px;color:#fff}.logo span{color:var(--gold)}
.hero{padding:60px 40px;max-width:1200px;margin:0 auto}
.eyebrow{color:var(--gold);font-size:12px;letter-spacing:2px;margin-bottom:20px;text-transform:uppercase}
h1{font-size:42px;margin-bottom:16px;line-height:1.2;font-weight:700}h1 em{color:var(--gold);font-style:italic}
h2{font-size:28px;margin-bottom:24px;font-weight:600}
h3{font-size:18px;margin-bottom:8px}
.hero-sub{color:var(--muted);margin:16px 0 30px;max-width:580px;line-height:1.7;font-size:16px}
.section{max-width:1200px;margin:0 auto;padding:50px 40px}
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;margin-bottom:40px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:28px;transition:border-color 0.2s}
.card:hover{border-color:var(--gold)}
.card-num{font-size:42px;color:var(--gold);opacity:0.2;font-weight:700}
.card p{color:var(--muted);font-size:14px;margin:12px 0;line-height:1.7}
.about-section{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start}
.about-text p{color:var(--muted);margin-bottom:18px;line-height:1.7}
.about-skills{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:28px}
.about-skills li{padding:10px 0;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px;list-style:none;color:var(--muted);font-size:14px}
.about-skills li:last-child{border:none}
.check{color:var(--gold);font-weight:700}
.stats{display:flex;gap:40px;margin-top:32px;flex-wrap:wrap}
.stat h3{font-size:42px;margin-bottom:4px;color:#fff}.stat p{color:var(--muted);font-size:13px}
.footer{border-top:1px solid var(--border);padding:30px;text-align:center;color:var(--muted);margin-top:40px;font-size:13px}
.contact-links{display:flex;gap:20px;justify-content:center;margin:16px 0;flex-wrap:wrap}
.contact-links a{color:var(--gold);font-size:14px;font-weight:600}
.contact-links a:hover{text-decoration:underline}
@media(max-width:768px){.about-section{grid-template-columns:1fr}.hero{padding:30px 20px}.section{padding:30px 20px}.stats{gap:24px}}
'''

HOMEPAGE = '''<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Granite Models Automations — Engineering Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>''' + CSS + '''</style>
</head><body>

<div class="banner">
    &#9889; Engineering Portfolio — Site rebuild in progress. All systems shown are real production software.
</div>

<nav class="nav">
    <div class="logo">Granite<span>Models</span></div>
    <div style="color:var(--muted);font-size:13px">Jon Anderson &bull; New Hampshire</div>
</nav>

<section class="hero">
    <p class="eyebrow">FROM JOB SITES TO SOFTWARE</p>
    <h1>Building What the Trades<br>Industry <em>Needs</em></h1>
    <p class="hero-sub">30 years in the trades. Then I built the automation software the industry is missing. Real production systems — not demos, not mockups.</p>
</section>

<section class="section" id="services">
    <h2>What I Build</h2>
    <div class="card-grid">
        <div class="card">
            <span class="card-num">01</span>
            <h3>Lead Generation & Sales</h3>
            <p>AI-powered lead scraping, scoring, territory management, and automated delivery. Lead Hunter Pro: 14,600+ lines, 27 database tables, 81+ routes.</p>
        </div>
        <div class="card">
            <span class="card-num">02</span>
            <h3>Trades Dashboards</h3>
            <p>Complete business management for landscaping, HVAC, plumbing, steel fabrication, and more. Role-based security, job tracking, crew management.</p>
        </div>
        <div class="card">
            <span class="card-num">03</span>
            <h3>Automated Trading</h3>
            <p>Institutional-grade trading platform. 219,000+ lines of Python, 830 files, 6 trading armies across FOREX, crypto, equities, DeFi, and arbitrage.</p>
        </div>
        <div class="card">
            <span class="card-num">04</span>
            <h3>Quality & Testing</h3>
            <p>Production Readiness Reports with automated scoring. Every system tested against real endpoints with pass/fail grading before deployment.</p>
        </div>
    </div>
</section>

<section class="section" id="about">
    <h2>Who I Am</h2>
    <div class="about-section">
        <div class="about-text">
            <p>I'm Jon Anderson — a machine learning engineer based in New Hampshire with 30 years of experience across landscaping, roofing, HVAC, plumbing, paving, and steel fabrication.</p>
            <p>I build production-grade automation systems from the ground up. Not tutorials, not demos — real software that runs real businesses. My first client was a steel fabrication shop where I built an 8-container Docker dashboard system.</p>
            <p>I wrote 219,000+ lines of code for a single trading platform in about 4 weeks. I've built 30+ complete automation systems. I'm now building Granite Models Automations into a full business to bring this technology to every trades company that needs it.</p>
            <div class="stats">
                <div class="stat"><h3>30+</h3><p>Systems Built</p></div>
                <div class="stat"><h3>219K+</h3><p>Lines (Trading Alone)</p></div>
                <div class="stat"><h3>30</h3><p>Years in Trades</p></div>
                <div class="stat"><h3>6</h3><p>Trades Covered</p></div>
            </div>
        </div>
        <div class="about-skills">
            <ul>
                <li><span class="check">&#10003;</span> Production ML Systems Architecture</li>
                <li><span class="check">&#10003;</span> Multi-Component System Integration</li>
                <li><span class="check">&#10003;</span> Real-Time Data Pipeline Development</li>
                <li><span class="check">&#10003;</span> Institutional-Grade Validation Frameworks</li>
                <li><span class="check">&#10003;</span> Python, JavaScript, Flask, SQLite, SQL</li>
                <li><span class="check">&#10003;</span> SendGrid, Ollama, AI/LLM Integration</li>
                <li><span class="check">&#10003;</span> End-to-End Solution Deployment</li>
                <li><span class="check">&#10003;</span> Patent-Pending Innovations</li>
            </ul>
        </div>
    </div>
</section>

<footer class="footer">
    <div class="logo" style="margin-bottom:12px">Granite<span>Models</span></div>
    <div class="contact-links">
        <a href="mailto:granitemodels@gmail.com">&#9993; Email</a>
        <a href="https://www.youtube.com/@granitemodels" target="_blank">&#9654; YouTube</a>
        <a href="https://medium.com/@granitemodels" target="_blank">&#9998; Medium</a>
    </div>
    <p style="margin-top:12px">&copy; 2026 Granite Models Automations &bull; New Hampshire &bull; granitemodels.store</p>
</footer>

</body></html>'''


@app.route('/')
def index():
    return render_template_string(HOMEPAGE)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5055))
    print(f'GRANITE MODELS v4 - http://127.0.0.1:{port}')
    app.run(host='0.0.0.0', port=port, debug=DEBUG_MODE)
