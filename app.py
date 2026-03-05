"""
GRANITE MODELS — Portfolio Website v5
7-page static portfolio site served via Flask
"""
from flask import Flask, render_template, redirect
from readmes import READMES
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'granite-2026-portfolio')

PROJECTS = {
    'lead-hunter-pro': {
        'name': 'Lead Hunter Pro v2',
        'sector': 'Lead Generation & Sales',
        'status': 'Production',
        'tagline': 'AI-powered B2B lead generation platform',
        'description': 'Full-lifecycle lead generation: scrape businesses from 5 sources, score with AI, enrich emails and social profiles, deliver to clients with territory exclusivity, collect feedback, auto-adjust scoring. CAN-SPAM compliant email campaigns with SendGrid, drip sequences, and 45-day compliance wipe.',
        'stats': {'lines': '14,600+', 'tables': '27', 'routes': '81+'},
        'tech': ['Python', 'Flask', 'SQLite', 'SendGrid', 'Ollama', 'Google Places API'],
        'features': ['Multi-source scraping (Google, Yelp, BBB, Thumbtack, YellowPages)', 'AI lead scoring with intent signals', 'Territory exclusivity and delivery engine', 'Email campaigns with CAN-SPAM compliance', 'Drip sequence automation', 'Client portal with self-service', 'AI assistant with 4-provider failover', 'Invoice generation (GMA-YYYY-NNNN format)', 'Built-in admin panel for system management', 'Nationwide compliance coverage'],
        'video': 'lead-hunter-pro-20260205-094919.webm',
        'priority': 'flagship'
    },
    'organized-system': {
        'name': 'ORGANIZED_SYSTEM',
        'sector': 'Trading & Finance',
        'status': 'Production',
        'tagline': 'Institutional-grade automated trading platform — "The Buddy System"',
        'description': 'Massive multi-army trading system spanning FOREX, crypto, equities, DeFi, penny stocks, and arbitrage. Built as 6 interconnected programs called the Buddy System, plus a standalone Excel dashboard that logs and visualizes all trading data with charts and graphs across the entire system in real-time.',
        'stats': {'lines': '219,000+', 'files': '830', 'ai_modules': '194', 'armies': '6', 'programs': '6'},
        'tech': ['Python', 'Flask', 'SQLite', 'Plaid', 'FRED API', 'Jupiter/Pump.fun', 'Excel'],
        'features': ['Bot Buddy — Core trading bot orchestration and execution', 'Agent Buddy — Multi-LLM orchestration with Architect/Analyst/Sentinel agents', 'Bot Swarm — Distributed swarm intelligence for coordinated trading', 'Finance Buddy — Portfolio management and risk analysis (RAF)', 'Tester Buddy — Strategy backtesting and validation framework', 'Banker Buddy — Full accounting system with Plaid integration', 'Excel Dashboard — Standalone charting and logging for entire system', '6 trading armies (FOREX, CRYPTO, EQUITIES, DEFI, PENNY, ARBITRAGE)', 'MemRL memory framework for learning across sessions', 'Tournament system for module competition', 'FRED economic data integration', 'Pump.fun/Jupiter meme coin infrastructure', 'Cyberpunk-themed dashboards'],
        'video': None,
        'priority': 'flagship'
    },
    'granite-tester': {
        'name': 'Granite Tester',
        'sector': 'Quality & Testing',
        'status': 'Production',
        'tagline': 'Production readiness testing with PRR scoring — 5 integrated sections',
        'description': 'Centralized testing and quality platform for the entire Granite ecosystem. Five distinct sections: the main 30-system test runner, a dedicated Trades Dashboard tester, an LHP v2 integration tester, a Research page with AI-powered summarization, and a custom Admin Panel designed after Google\'s admin interface for managing the trades side.',
        'stats': {'lines': '2,700+', 'sections': '5', 'systems_tested': '30+'},
        'tech': ['Python', 'Flask', 'SQLite', 'SSE Streaming', 'Ollama AI'],
        'features': ['30-system test runner with live SSE streaming', 'Trades Dashboard test engine with phase-based testing', 'LHP v2 integration tester (7 phases, 40+ tests)', 'Research page with AI summarizer for test analysis', 'Google-style Admin Panel for trades system management', 'PRR scoring with letter grades (A-F)', 'Findings engine (BUG/WARNING/INFO severity)', 'Test history tracking and run comparison'],
        'video': None,
        'priority': 'flagship'
    },
    'landscape-dashboard': {
        'name': 'Landscape Dashboard',
        'sector': 'Trades Dashboards',
        'status': 'Production',
        'tagline': 'Complete business management for landscaping companies',
        'description': 'Reference build for the trades dashboard series. Full crew management, job scheduling, equipment tracking, invoicing, client CRM, and analytics. Role-based security with owner/admin/crew permissions.',
        'stats': {'lines': '12,000+', 'tables': '49', 'templates': '67', 'routes': '180+'},
        'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'],
        'features': ['Role-based security (owner/admin/crew)', 'Job scheduling and dispatch', 'Crew management and timesheets', 'Equipment tracking and maintenance', 'Client CRM with communication log', 'Invoicing and payment tracking', 'Weather-aware scheduling', 'Comprehensive analytics dashboard'],
        'video': None,
        'priority': 'high'
    },
    'empire-dashboard': {
        'name': 'Empire Dashboard',
        'sector': 'Operations & Admin',
        'status': 'Production',
        'tagline': 'Master command center for the entire Granite ecosystem',
        'description': 'Super admin panel with dropdown navigation per business division. Tab switching between tools across 10 corporate sectors. System health monitoring, revenue tracking, and cross-system management.',
        'stats': {'lines': '3,000+', 'sectors': '10'},
        'tech': ['Python', 'Flask', 'SQLite'],
        'features': ['10 corporate sector navigation', 'Cross-system health monitoring', 'Revenue and billing overview', 'Tool launcher for all systems', 'Empire-wide search'],
        'video': None,
        'priority': 'high'
    },
    'sales-pipeline': {
        'name': 'Sales Pipeline',
        'sector': 'Lead Generation & Sales',
        'status': 'Production',
        'tagline': 'CRM-style deal tracking with visual pipeline stages',
        'description': 'Kanban-style deal pipeline with drag-and-drop stage management, activity logging, revenue forecasting, and analytics charts.',
        'stats': {},
        'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'],
        'features': ['Visual pipeline stages', 'Deal tracking and activity log', 'Revenue forecasting', 'Analytics and charts'],
        'video': 'sales-pipeline-20260205-131725.webm',
        'priority': 'high'
    },
    'email-campaign': {
        'name': 'Email Campaign Engine',
        'sector': 'Lead Generation & Sales',
        'status': 'Production',
        'tagline': 'Automated email marketing built into Lead Hunter Pro',
        'description': 'Full email campaign system integrated directly into the Lead Hunter Pro dashboard. Template builder, audience segmentation, send scheduling, open/click tracking, and CAN-SPAM compliance — all managed from within LHP.',
        'stats': {},
        'tech': ['Python', 'Flask', 'SendGrid'],
        'features': ['Campaign builder with templates', 'Audience segmentation', 'Open and click tracking', 'CAN-SPAM compliance built-in', 'Integrated into Lead Hunter Pro dashboard'],
        'video': 'email-campaign-20260205-134527.webm',
        'priority': 'high'
    },
    'steel-dashboard': {'name': 'Steel Fabrication Dashboard', 'sector': 'Trades Dashboards', 'status': 'Rebuilding', 'tagline': 'Shop management for steel fabrication', 'description': 'Originally built as an 8-container Docker system for American Steel Fabricators. Currently being redesigned and tested as part of the Granite dashboard series with the same architecture as the completed Landscape Dashboard.', 'stats': {}, 'tech': ['Python', 'Flask', 'Docker', 'SQLite'], 'features': ['Job tracking', 'Material inventory', 'Shop scheduling', 'Client billing'], 'video': None, 'priority': 'high'},
    'hvac-dashboard': {'name': 'HVAC Dashboard', 'sector': 'Trades Dashboards', 'status': 'In Development', 'tagline': 'Service management for HVAC companies', 'description': 'HVAC-specific business dashboard with equipment tracking, service scheduling, warranty management, and seasonal planning.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Equipment and unit tracking', 'Service scheduling', 'Warranty management', 'Seasonal workload planning'], 'video': None, 'priority': 'medium'},
    'plumbing-dashboard': {'name': 'Plumbing Dashboard', 'sector': 'Trades Dashboards', 'status': 'In Development', 'tagline': 'Service management for plumbing companies', 'description': 'Plumbing-specific business dashboard with job dispatching, parts inventory, and emergency call routing.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Job dispatch', 'Parts inventory', 'Emergency routing', 'Client history'], 'video': None, 'priority': 'medium'},
    'construction-dashboard': {'name': 'Construction Dashboard', 'sector': 'Trades Dashboards', 'status': 'In Development', 'tagline': 'Project management for construction companies', 'description': 'Construction-specific dashboard with project phasing, subcontractor management, and permit tracking.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Project phasing', 'Subcontractor management', 'Permit tracking', 'Budget monitoring'], 'video': None, 'priority': 'medium'},
    'mechanic-dashboard': {'name': 'Mechanic Dashboard', 'sector': 'Trades Dashboards', 'status': 'Planned', 'tagline': 'Shop management for auto mechanics', 'description': 'Auto mechanic shop dashboard with vehicle tracking, repair orders, parts sourcing, and customer communication.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Vehicle tracking', 'Repair orders', 'Parts sourcing', 'Customer portal'], 'video': None, 'priority': 'medium'},
    'quote-generator': {'name': 'Quote Generator', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Instant professional quotes for trades businesses', 'description': 'Generate professional quotes with line items, labor rates, material costs, and PDF export.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Line item editor', 'Labor and material rates', 'PDF export', 'Client-facing portal'], 'video': 'quote-generator-20260205-140207.webm', 'priority': 'medium'},
    'proposal-generator': {'name': 'Proposal Generator', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Professional proposals in minutes', 'description': 'Create branded proposals with scope, timeline, pricing, and terms. Template library and PDF export.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Template library', 'Scope and timeline builder', 'PDF export', 'E-signature ready'], 'video': 'proposal-generator-20260205-134415.webm', 'priority': 'medium'},
    'referral-tracker': {'name': 'Referral Tracker', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Track and reward referral sources', 'description': 'Track which clients and partners send you business. Automated thank-you workflows and commission tracking.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Referral source tracking', 'Commission calculations', 'Automated thank-you emails', 'Referral leaderboard'], 'video': 'referral-tracker-20260205-134349.webm', 'priority': 'medium'},
    'social-media': {'name': 'Social Media Manager', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Schedule and manage social media posts', 'description': 'Content calendar, post scheduling, engagement tracking, and multi-platform management.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Content calendar', 'Post scheduling', 'Engagement tracking', 'Multi-platform support'], 'video': 'social-media-manager-20260205-134453.webm', 'priority': 'medium'},
    'review-manager': {'name': 'Review Manager', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Monitor and respond to online reviews', 'description': 'Track reviews across platforms, get alerts for new reviews, and manage responses from one dashboard.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Multi-platform monitoring', 'Review alerts', 'Response templates', 'Sentiment tracking'], 'video': 'review-manager-20260205-134556.webm', 'priority': 'medium'},
    'design-studio': {'name': 'Granite Design Studio', 'sector': 'Marketing & Content', 'status': 'Planned', 'tagline': 'Zero-cost design workspace for trades businesses', 'description': 'Guided-flow design workspace with dark theme, browser-style tabs, free asset sources only (Unsplash, Pexels, Pixabay, Iconify, Google Fonts). Exports PNG/JPG/SVG/PDF with video editing for Reels/TikTok/Shorts.', 'stats': {}, 'tech': ['Python', 'Flask', 'JavaScript'], 'features': ['Guided design workflow', 'Free asset sources only', 'Video editing for social', 'PNG/JPG/SVG/PDF export'], 'video': None, 'priority': 'medium'},
    'super-admin': {'name': 'Super Admin Panel', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Google-style admin panel for the trades ecosystem', 'description': 'Custom-built admin panel modeled after Google\'s admin interface. Manages all trades-side systems, user accounts, system health, and configuration from a single dashboard. Separate from the admin panel built into Lead Hunter Pro.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Google-style admin interface', 'Cross-system management', 'User and role administration', 'System health monitoring', 'Configuration management'], 'video': None, 'priority': 'high'},
    'trading-excel': {'name': 'Trading Excel Dashboard', 'sector': 'Trading & Finance', 'status': 'Production', 'tagline': 'Real-time Excel charting for the entire trading system', 'description': 'Standalone Excel dashboard that connects to ORGANIZED_SYSTEM and visualizes all trading data with charts and graphs. Logs every trade, position, and metric in real-time as the system operates.', 'stats': {}, 'tech': ['Python', 'Excel', 'VBA'], 'features': ['Real-time trade logging', 'Portfolio performance charts', 'Army-by-army breakdown graphs', 'P&L tracking and visualization', 'Standalone — runs alongside the main system'], 'video': None, 'priority': 'high'},
    'omniverse-apex': {'name': 'OmniVerse Apex Predator', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': 'Consumer-grade hardware running 1,000x faster than research labs', 'description': 'Proprietary optimization system that enables standard gaming hardware (RTX 3060/16GB RAM) to achieve simulation speeds previously requiring dedicated research infrastructure. Hybrid computation methods hit 43M+ FPS. Features self-evolving kernel optimization, infinite context memory architecture, distilled quantization for minimal VRAM, and real-time physics rendering at 120FPS via WebGPU.', 'stats': {'fps': '43M+', 'speedup': '1,000x'}, 'tech': ['Python', 'JAX', 'CUDA', 'Taichi', 'WebGPU', 'RWKV'], 'features': ['Taichi-JAX hybrid for 43M FPS simulations', 'FlashAttention-3 + Triton custom CUDA kernels', 'Distilled QLoRA 4-bit quantization (1GB VRAM)', 'Infinite context window via RWKV + JAX', 'Live WebGPU physics viewport at 120FPS', 'Self-evolving NEAT kernel mutation'], 'video': None, 'priority': 'flagship'},
    'harvester-agent': {'name': 'Harvester Agent', 'sector': 'Trading & Finance', 'status': 'In Development', 'tagline': 'Autonomous CPU mining empire — $100/day target on consumer hardware', 'description': 'Fully autonomous Docker-based mining orchestration system designed for consumer-grade PCs. Targets $100/day net profit mining CPU coins (RandomX) with zero manual intervention after deployment. Includes cloud resource optimization via free-tier rotation, genetic algorithm hash boost, Telegram alerting, and live profit dashboard.', 'stats': {'target': '$100/day', 'intervention': 'Zero'}, 'tech': ['Python', 'Docker', 'Oracle Cloud', 'Telegram API'], 'features': ['Docker Swarm orchestration', 'Oracle Always Free ARM integration', 'Cloud trial resource optimization', 'Genetic algorithm hash rate boosting', 'Telegram alerts and profit dashboard', 'Fully autonomous — zero manual intervention'], 'video': None, 'priority': 'flagship'},
    'ironworks-engine': {'name': 'Ironworks Engine', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': '1-click safe build orchestrator for 60+ agents', 'description': 'Master orchestration system that self-builds the entire Granite ecosystem in one click. Professional-grade safety controls at every level: human approval gates, 3x error retries, per-component kill switches, and auditable logging. Full deployment from zero to production in 60 minutes.', 'stats': {'agents': '60+', 'deploy_time': '60 min'}, 'tech': ['Python', 'n8n', 'Vercel', 'Docker'], 'features': ['1-click deployment of entire ecosystem', 'Human approval gates at every level', 'Automatic error retries (3x)', 'Per-component kill switches', 'Professional-grade auditable logs', 'Zero to production in 60 minutes'], 'video': None, 'priority': 'flagship'},
    'iot-sensor-hub': {'name': 'IoT Sensor Hub', 'sector': 'IoT & Smart Systems', 'status': 'Planned', 'tagline': 'Real-time sensor monitoring and alerting for trades operations', 'description': 'Centralized IoT platform for connecting sensors across job sites, shops, and equipment. Real-time temperature, humidity, vibration, and equipment health monitoring with automated alerts. Originally prototyped as part of the steel fabrication dashboard for shop floor monitoring.', 'stats': {}, 'tech': ['Python', 'MQTT', 'Flask', 'WebSocket', 'Raspberry Pi'], 'features': ['Multi-sensor real-time monitoring', 'Equipment health and vibration tracking', 'Temperature and humidity alerts', 'Shop floor environmental monitoring', 'Mobile-friendly live dashboard', 'Automated threshold alerting via SMS/email'], 'video': None, 'priority': 'medium'},
    'iot-fleet-tracker': {'name': 'Fleet & Equipment Tracker', 'sector': 'IoT & Smart Systems', 'status': 'Planned', 'tagline': 'GPS tracking and maintenance scheduling for trucks and equipment', 'description': 'IoT-powered fleet management for trades companies. Track vehicle locations, monitor engine diagnostics, schedule preventive maintenance, and log equipment usage hours. Designed for landscaping fleets, construction equipment, and service vehicles.', 'stats': {}, 'tech': ['Python', 'Flask', 'GPS/OBD-II', 'SQLite', 'Mapbox'], 'features': ['Real-time GPS vehicle tracking', 'OBD-II engine diagnostics', 'Preventive maintenance scheduling', 'Equipment usage hour logging', 'Fuel consumption tracking', 'Route optimization'], 'video': None, 'priority': 'medium'},
    'smart-shop': {'name': 'Smart Shop Controller', 'sector': 'IoT & Smart Systems', 'status': 'Planned', 'tagline': 'Automated shop environment control for fabrication and service bays', 'description': 'IoT automation for trade shop environments — automated ventilation based on air quality sensors, lighting control, compressor and tool power management, and safety system integration. Originally designed for steel fabrication shops with welding fume detection.', 'stats': {}, 'tech': ['Python', 'MQTT', 'Raspberry Pi', 'Relay Controllers'], 'features': ['Air quality monitoring with auto-ventilation', 'Welding fume detection and extraction', 'Automated lighting and power management', 'Compressor scheduling', 'Safety system integration', 'Energy usage optimization'], 'video': None, 'priority': 'medium'},
    'robo-dispatch': {'name': 'Robotic Dispatch System', 'sector': 'Robotics & Automation', 'status': 'Planned', 'tagline': 'Automated material handling and delivery for shop floors', 'description': 'Robotic dispatch and routing system for automated material movement within fabrication shops and warehouses. Integrates with job scheduling to pre-stage materials, route autonomous carts, and track delivery completion.', 'stats': {}, 'tech': ['Python', 'ROS2', 'Flask', 'Computer Vision'], 'features': ['Autonomous cart routing and dispatch', 'Job-based material pre-staging', 'Delivery completion tracking', 'Integration with trades dashboards', 'Collision avoidance pathfinding', 'Multi-robot coordination'], 'video': None, 'priority': 'medium'},
    'robo-inspection': {'name': 'Automated Inspection System', 'sector': 'Robotics & Automation', 'status': 'Planned', 'tagline': 'Computer vision quality inspection for fabricated parts', 'description': 'Automated visual inspection system using computer vision to check weld quality, dimensional accuracy, and surface defects on fabricated parts. Camera-based with AI classification trained on real shop data. Reduces manual QC time and catches defects humans miss.', 'stats': {}, 'tech': ['Python', 'OpenCV', 'TensorFlow', 'Flask', 'USB Cameras'], 'features': ['Weld quality inspection via computer vision', 'Dimensional accuracy measurement', 'Surface defect detection', 'AI classification trained on real shop data', 'Pass/fail grading with photo evidence', 'Integration with job tracking system'], 'video': None, 'priority': 'medium'},
    'robo-arm-controller': {'name': 'Robotic Arm Controller', 'sector': 'Robotics & Automation', 'status': 'Planned', 'tagline': 'Programmable robotic arm integration for repetitive shop tasks', 'description': 'Control interface for integrating programmable robotic arms into trades workflows. Handles repetitive tasks like material cutting, sorting, welding prep, and parts assembly. Visual programming interface so operators don\'t need to write code.', 'stats': {}, 'tech': ['Python', 'ROS2', 'Flask', 'Arduino/PLC'], 'features': ['Visual task programming interface', 'Repetitive task automation (cutting, sorting, assembly)', 'Safety zone enforcement', 'Integration with job scheduler', 'Operator-friendly — no coding required', 'Emergency stop and override controls'], 'video': None, 'priority': 'medium'},
}

SECTORS = [
    ('Lead Generation & Sales', 'lead-sales'),
    ('Trading & Finance', 'trading'),
    ('Trades Dashboards', 'trades'),
    ('Marketing & Content', 'marketing'),
    ('Quality & Testing', 'testing'),
    ('Operations & Admin', 'operations'),
    ('IoT & Smart Systems', 'iot'),
    ('Robotics & Automation', 'robotics'),
]

SOCIAL = {
    'linkedin': 'https://www.linkedin.com/in/jon-anderson-418122300',
    'facebook': 'https://www.facebook.com/jon.anderson.236899',
    'medium': 'https://granitemodels.store',
    'youtube': 'https://www.youtube.com/@granitemodels',
    'github': 'https://github.com/granitemodels-hub',
    'email': 'granitemodels@gmail.com',
}

@app.route('/')
def index():
    flagships = {k: v for k, v in PROJECTS.items() if k in ('lead-hunter-pro', 'organized-system', 'granite-tester')}
    return render_template('index.html', projects=flagships, social=SOCIAL)

@app.route('/story')
def story():
    return render_template('story.html', social=SOCIAL)

@app.route('/systems')
def systems():
    return render_template('systems.html', projects=PROJECTS, sectors=SECTORS, social=SOCIAL)

@app.route('/project/<slug>')
def project_detail(slug):
    p = PROJECTS.get(slug)
    if not p:
        return redirect('/systems')
    readme = READMES.get(slug, '')
    return render_template('project.html', project=p, slug=slug, readme=readme, social=SOCIAL)

@app.route('/process')
def process():
    return render_template('process.html', social=SOCIAL)

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html', social=SOCIAL)

@app.route('/contact')
def contact():
    return render_template('contact.html', social=SOCIAL)

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    pages = ['/', '/story', '/systems', '/process', '/roadmap', '/contact']
    pages += [f'/project/{slug}' for slug in PROJECTS]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in pages:
        xml += f'  <url><loc>https://granitemodels.store{p}</loc></url>\n'
    xml += '</urlset>'
    return xml, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5055))
    print(f'GRANITE MODELS v5 — http://127.0.0.1:{port}')
    app.run(host='0.0.0.0', port=port, debug=False)
