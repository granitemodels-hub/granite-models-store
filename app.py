"""
GRANITE MODELS — Portfolio Website v5
7-page static portfolio site served via Flask
"""
from flask import Flask, render_template, redirect, send_from_directory, request, flash
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
        'architecture': [
            'Single-file Flask monolith by design — one Python file containing all routes, templates, logic, and scheduled jobs. This makes deployment dead simple: copy one file, restart. The database is SQLite, stored separately from the app.',
            'The scraper engine supports 5 sources with a unified interface. Each source module returns normalized lead data that feeds into the same scoring pipeline. An ALL mode runs every source in sequence with deduplication.',
            'Email infrastructure uses a priority chain: SendGrid API first, SMTP fallback, then simulated sends for development. The send_email() function never crashes the app — all failures are logged and silently handled.',
            'The AI assistant uses a 4-provider failover chain: Anthropic Claude, Ollama (local llama3.1), OpenAI, and a keyword-based fallback. It has full database context — it can answer questions about your leads, pipeline, and system health by querying live data.',
            'Compliance is built into every layer. 45-day data wipe runs on schedule. DNC checking happens before every delivery. CAN-SPAM footers with unsubscribe links are injected into every outbound email. Open/click tracking uses per-send unique IDs.'
        ],
        'journey': [
            'Lead Hunter Pro started as a simple Google Places scraper — pull businesses by industry and location, dump them in a database. Version 1 had maybe 2,000 lines and did one thing: scrape and list.',
            'The rebuild into v2 was driven by a real question: what would a trades business owner actually need to turn leads into revenue? That meant scoring (not all leads are equal), territory exclusivity (two clients in the same city shouldn\'t get the same lead), delivery automation, and feedback loops that adjust scoring over time.',
            'The biggest lesson was compliance. CAN-SPAM, DNC lists, data retention limits — this stuff isn\'t optional if you\'re sending real emails to real businesses. Building the 45-day wipe and multi-state compliance framework took longer than building the scraper itself.',
            'v2 grew from 2,000 lines to 14,600+ lines across 27 database tables. It\'s now a complete business platform, not just a scraper. The AI assistant alone handles four different LLM providers with automatic failover.'
        ],
        'video': 'lead-hunter-pro-20260205-094919.webm',
        'video_v2': 'lhp-v2-current.mp4',
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
        'architecture': [
            'The Tester is a single Flask application with 5 distinct sections served from one process. The main test runner handles 30+ registered systems. Each system can be tested individually or all at once with results streaming via Server-Sent Events (SSE) to the browser in real-time.',
            'The Trades Dashboard test engine and LHP v2 test engine are separate Python modules imported by the main tester. Each defines its own test phases with specific endpoint expectations. The LHP engine runs 7 phases covering connectivity, scrapers, enrichment, email, drip sequences, compliance, and API integrity.',
            'PRR scoring follows Google SWE/SRE standards: each test gets a point value, phases are weighted, and a letter grade (A through F) is calculated from the aggregate. The Findings Engine categorizes issues as BUG (must fix), WARNING (should fix), or INFO (note for later).',
            'The Research page stores every test run in a SQLite database with individual test results as run outputs. The AI summarizer uses Ollama to analyze test results and generate plain-English recommendations for what to fix next.',
            'The Admin Panel section is modeled after Google\'s admin interface design. It provides cross-system management for the trades side of the business — user administration, system configuration, and health monitoring.'
        ],
        'journey': [
            'The Granite Tester was born from a painful realization: with 30+ systems running on different ports, there was no way to know if a code change in one system broke something in another. Manual testing was a joke at this scale.',
            'The first version just hit endpoints and checked for 200 status codes. That caught the obvious stuff — dead routes, import errors, missing templates. But it missed the subtle bugs: wrong data in responses, missing form fields, broken database queries that returned empty instead of erroring.',
            'Adding the Findings Engine and PRR scoring changed everything. Now every test run produces a grade. You can see at a glance whether a system is production-ready or needs work. The LHP v2 tester went from a 50% PRR score to 90% in one session just by aligning test paths to actual routes.',
            'The Research page with AI summarization was the final piece — instead of reading through 40 test results manually, the AI reads them and tells you in plain English what\'s broken and what to fix first.'
        ],
        'video': None,
        'priority': 'flagship'
    },
    'file-processor': {
        'name': 'File Automation Pro',
        'sector': 'Operations & Automation',
        'status': 'Production',
        'tagline': 'Automated document processing for every trade — $10/page or $250/month',
        'description': 'Every trade runs on paperwork — drawings, specs, cut lists, BOMs, compliance documents, permits, inspection reports. File Automation Pro takes the chaos out of document management by automatically sorting, validating, checking for completeness, and packaging files into branded delivery bundles for any trade. For steel fabrication and CNC shops, it goes deeper — routing DSTV files to beam lines, PXFT files to plasma tables, AGXT files to robotic welders.',
        'stats': {'trades': '22', 'file_types': 'All', 'pricing': '$10/page'},
        'tech': ['Python', 'Flask', 'SQLite', 'FFmpeg', 'CNC Routing'],
        'features': ['Automated file sorting and categorization for any trade', 'Completeness checking against trade-specific requirements', 'Branded package delivery with professional cover reports', 'Steel fab CNC routing — DSTV, PXFT, AGXT file parsing', 'Machine destination tagging from file headers', 'Metadata extraction and file validation', 'PDF, drawing, spreadsheet, and compliance doc handling', 'Works for all 22 supported industries'],
        'architecture': [
            'File Automation Pro is a Flask-based processing pipeline. Files are uploaded, identified by type, routed to the correct processing module, validated against trade-specific requirements, and packaged into branded delivery bundles.',
            'For steel fabrication, the system reads DSTV file headers to identify part types and machine destinations. CNC routing logic tags each file for beam lines, plasma tables, or robotic welders based on the operation codes in the file.',
            'For all other trades, the system handles standard document workflows — sorting PDFs, drawings, spreadsheets, permits, inspection reports, and compliance documents into organized project folders with completeness checking.'
        ],
        'journey': [
            'File Automation Pro started from a real problem in steel fabrication shops. CNC files arrive in bulk and someone has to manually sort them by machine type. That process is slow, error-prone, and expensive when you get it wrong.',
            'The system expanded beyond steel to handle document management for every trade. Construction companies need permit tracking. HVAC shops need compliance documentation. Landscapers need proposal and photo organization. The core engine handles it all.'
        ],
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
        'architecture': [
            'The Landscape Dashboard is the reference build for all trades dashboards. It establishes the architecture that HVAC, Plumbing, Construction, Steel, and Mechanic dashboards will follow: 49 database tables, 67 HTML templates, 180+ route decorators, and role-based security with three tiers (owner, admin, crew).',
            'The security model enforces permissions at the route level — crew members can view their assigned jobs and submit timesheets, admins can manage schedules and clients, owners see everything including financials. Each role has a different dashboard view with only the tools they need.',
            'Job scheduling integrates with weather data to prevent dispatching crews during storms or extreme conditions. The system pulls forecasts and flags jobs that might need rescheduling, showing warnings on the dispatch board.',
            'The analytics dashboard aggregates data across all 49 tables: revenue by client, crew utilization rates, equipment maintenance schedules, job completion rates, and seasonal trends. Everything a landscaping company owner needs to run their business from one screen.'
        ],
        'journey': [
            'The Landscape Dashboard was the first complete trades dashboard — and the hardest to build because there was no template to follow. Every decision about database schema, security model, and UI layout became the pattern for every dashboard after it.',
            'The biggest challenge was the role-based security. In a landscaping company, the owner needs to see financials, the admin needs to manage the schedule, and the crew just needs to know where to show up. Building three different views of the same data without duplicating code required careful template architecture.',
            'Weather integration was an afterthought that turned out to be one of the most valuable features. Landscaping is entirely weather-dependent — dispatching a crew to mow lawns in a thunderstorm wastes everyone\'s time. Having the system flag weather conflicts automatically saves real money.',
            'At 12,000+ lines with 49 database tables and 67 templates, this is the most thoroughly built dashboard in the series. It serves as proof that the architecture scales — every future trades dashboard follows this same pattern.'
        ],
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
        'architecture': [
            'The Empire Dashboard is the master command center — a single Flask app that provides dropdown navigation across all 10 corporate sectors with tab switching between individual tools. It doesn\'t duplicate functionality; it launches and monitors the other systems.',
            'Health monitoring pings every running system on its port and displays status indicators. Revenue tracking aggregates billing data from Lead Hunter Pro\'s invoice system and Stripe integration. The tool launcher opens any system in the ecosystem from one central interface.',
            'The 10 sectors (Sales & Revenue, Marketing & Content, Client Management, Finance, Operations, Communications, Legal & Compliance, Analytics & Intelligence, IoT & Smart Systems, Robotics & Automation) each have their own dropdown with the relevant tools grouped logically.'
        ],
        'journey': [
            'The Empire Dashboard came from a practical problem: with 30+ systems running on different ports, there was no central place to manage everything. You\'d have browser tabs open to localhost:6001, localhost:6092, localhost:8003 — it was chaos.',
            'Building it was straightforward once the sector mapping was done. The hard part was deciding how to organize 30+ tools into categories that actually make sense. The 10-sector model emerged from thinking about how a real business operates, not how a developer organizes code.'
        ],
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
    'steel-dashboard': {'name': 'Steel Fabrication Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Complete shop management, AI scheduling, and IoT-ready automation for steel fabrication operations', 'description': 'Full-stack business management platform purpose-built for steel fabrication shops. Handles job tracking from quote to delivery, material inventory with reorder automation, crew and machine scheduling, client billing and invoicing, and real-time shop floor visibility. Includes a built-in AI assistant for job costing estimates, schedule optimization, and material usage forecasting. Architected to integrate with IoT sensor monitoring, robotic inspection systems, and smart shop environmental controls — turning a fabrication shop into a connected, data-driven operation.', 'stats': {'tables': '49', 'templates': '67+', 'routes': '180+', 'security_tiers': '3'}, 'tech': ['Python', 'Flask', 'SQLite', 'Docker', 'Ollama AI', 'MQTT', 'Raspberry Pi', 'WebSocket'], 'features': ['Job tracking — quote to fabrication to delivery with status pipeline', 'Material inventory with automated reorder thresholds and vendor tracking', 'Crew scheduling with machine assignments and shift management', 'Client billing, invoicing, and payment tracking', 'AI assistant — job cost estimating, schedule optimization, material forecasting', 'Shop floor dashboard — real-time job status across all workstations', 'Weld log tracking with welder certifications and inspection records', 'Equipment maintenance scheduling with usage hour tracking', 'IoT-ready — connects to sensor hubs for temperature, air quality, and vibration monitoring', 'Smart shop integration — automated ventilation, welding fume detection, compressor scheduling', 'Robotic inspection integration — computer vision weld quality and dimensional checks', 'Role-based security — owner, shop manager, and fabricator access tiers', 'Mobile-friendly — check job status and update progress from the shop floor'], 'video': None, 'priority': 'high'},
    'hvac-dashboard': {'name': 'HVAC Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for HVAC companies', 'description': 'HVAC-specific business dashboard with equipment tracking, service scheduling, warranty management, and seasonal planning.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Equipment and unit tracking', 'Service scheduling', 'Warranty management', 'Seasonal workload planning'], 'video': None, 'priority': 'medium'},
    'plumbing-dashboard': {'name': 'Plumbing Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for plumbing companies', 'description': 'Plumbing-specific business dashboard with job dispatching, parts inventory, and emergency call routing.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Job dispatch', 'Parts inventory', 'Emergency routing', 'Client history'], 'video': None, 'priority': 'medium'},
    'construction-dashboard': {'name': 'Construction Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Project management for construction companies', 'description': 'Construction-specific dashboard with project phasing, subcontractor management, and permit tracking.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Project phasing', 'Subcontractor management', 'Permit tracking', 'Budget monitoring'], 'video': None, 'priority': 'medium'},
    'mechanic-dashboard': {'name': 'Mechanic Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Shop management for auto mechanics', 'description': 'Auto mechanic shop dashboard with vehicle tracking, repair orders, parts sourcing, and customer communication.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Vehicle tracking', 'Repair orders', 'Parts sourcing', 'Customer portal'], 'video': None, 'priority': 'medium'},
    'paving-dashboard': {'name': 'Paving Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Job and crew management for paving companies', 'description': 'Paving-specific dashboard with project estimating, material tonnage tracking, crew dispatch, and weather-dependent scheduling.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Tonnage and material tracking', 'Weather-aware scheduling', 'Crew dispatch', 'Project estimating'], 'video': None, 'priority': 'medium'},
    'logging-dashboard': {'name': 'Logging Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Operations management for logging companies', 'description': 'Logging-specific dashboard with timber inventory, harvest planning, equipment tracking, and compliance documentation.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Timber inventory', 'Harvest planning', 'Equipment tracking', 'Compliance docs'], 'video': None, 'priority': 'medium'},
    'painting-dashboard': {'name': 'Painting Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Business management for painting contractors', 'description': 'Painting-specific dashboard with job estimating by square footage, color and material tracking, crew scheduling, and client galleries.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Square footage estimating', 'Color and material tracking', 'Crew scheduling', 'Client photo galleries'], 'video': None, 'priority': 'medium'},
    'electrical-dashboard': {'name': 'Electrical Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for electrical contractors', 'description': 'Electrical-specific dashboard with permit tracking, inspection scheduling, panel and circuit documentation, and code compliance.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Permit tracking', 'Inspection scheduling', 'Panel documentation', 'Code compliance'], 'video': None, 'priority': 'medium'},
    'insulation-dashboard': {'name': 'Insulation Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Job management for insulation contractors', 'description': 'Insulation-specific dashboard with R-value tracking, material estimating, energy audit integration, and inspection scheduling.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['R-value tracking', 'Material estimating', 'Energy audit integration', 'Inspection scheduling'], 'video': None, 'priority': 'medium'},
    'sealcoat-dashboard': {'name': 'Sealcoat Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Operations management for sealcoating businesses', 'description': 'Sealcoat-specific dashboard with square footage estimating, material usage tracking, weather scheduling, and route optimization.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Square footage estimating', 'Material usage tracking', 'Weather scheduling', 'Route optimization'], 'video': None, 'priority': 'medium'},
    'concrete-dashboard': {'name': 'Concrete Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Project management for concrete contractors', 'description': 'Concrete-specific dashboard with pour scheduling, mix design tracking, yardage estimating, weather monitoring, and cure time management.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Pour scheduling', 'Mix design tracking', 'Yardage estimating', 'Cure time management'], 'video': None, 'priority': 'medium'},
    'pool-pond-dashboard': {'name': 'Pool & Pond Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for pool and pond companies', 'description': 'Pool and pond-specific dashboard with water chemistry tracking, service route management, equipment maintenance, and seasonal scheduling.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Water chemistry tracking', 'Service route management', 'Equipment maintenance', 'Seasonal scheduling'], 'video': None, 'priority': 'medium'},
    'excavation-dashboard': {'name': 'Excavation Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Operations management for excavation companies', 'description': 'Excavation-specific dashboard with dig permit tracking, utility locate management, equipment dispatch, and haul tracking.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Dig permit tracking', 'Utility locate management', 'Equipment dispatch', 'Haul tracking'], 'video': None, 'priority': 'medium'},
    'hardscape-dashboard': {'name': 'Hardscape Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Project management for hardscape contractors', 'description': 'Hardscape-specific dashboard with material estimating, design visualization, project phasing, and client approval workflows.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Material estimating', 'Design visualization', 'Project phasing', 'Client approval workflows'], 'video': None, 'priority': 'medium'},
    'fencing-dashboard': {'name': 'Fencing Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Business management for fencing contractors', 'description': 'Fencing-specific dashboard with linear footage estimating, material ordering, permit tracking, and installation scheduling.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Linear footage estimating', 'Material ordering', 'Permit tracking', 'Installation scheduling'], 'video': None, 'priority': 'medium'},
    'septic-dashboard': {'name': 'Septic Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for septic companies', 'description': 'Septic-specific dashboard with pump scheduling, tank inspection records, perc test tracking, and compliance documentation.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Pump scheduling', 'Tank inspection records', 'Perc test tracking', 'Compliance documentation'], 'video': None, 'priority': 'medium'},
    'irrigation-dashboard': {'name': 'Irrigation Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Service management for irrigation companies', 'description': 'Irrigation-specific dashboard with zone mapping, winterization scheduling, spring startup tracking, and backflow certification management.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Zone mapping', 'Winterization scheduling', 'Spring startup tracking', 'Backflow certification'], 'video': None, 'priority': 'medium'},
    'striping-dashboard': {'name': 'Line Striping Dashboard', 'sector': 'Trades Dashboards', 'status': 'Production', 'tagline': 'Operations management for line striping companies', 'description': 'Line striping-specific dashboard with lot layout templates, paint usage tracking, night work scheduling, and ADA compliance verification.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Lot layout templates', 'Paint usage tracking', 'Night work scheduling', 'ADA compliance'], 'video': None, 'priority': 'medium'},
    'quote-generator': {'name': 'Quote Generator', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Instant professional quotes for trades businesses', 'description': 'Generate professional quotes with line items, labor rates, material costs, and PDF export.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Line item editor', 'Labor and material rates', 'PDF export', 'Client-facing portal'], 'video': 'quote-generator-20260205-140207.webm', 'priority': 'medium'},
    'proposal-generator': {'name': 'Proposal Generator', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Professional proposals in minutes', 'description': 'Create branded proposals with scope, timeline, pricing, and terms. Template library and PDF export.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Template library', 'Scope and timeline builder', 'PDF export', 'E-signature ready'], 'video': 'proposal-generator-20260205-134415.webm', 'priority': 'medium'},
    'referral-tracker': {'name': 'Referral Tracker', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'Track and reward referral sources', 'description': 'Track which clients and partners send you business. Automated thank-you workflows and commission tracking.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Referral source tracking', 'Commission calculations', 'Automated thank-you emails', 'Referral leaderboard'], 'video': 'referral-tracker-20260205-134349.webm', 'priority': 'medium'},
    'social-media': {'name': 'Social Media Manager', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Schedule and manage social media posts', 'description': 'Content calendar, post scheduling, engagement tracking, and multi-platform management.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Content calendar', 'Post scheduling', 'Engagement tracking', 'Multi-platform support'], 'video': 'social-media-manager-20260205-134453.webm', 'priority': 'medium'},
    'review-manager': {'name': 'Review Manager', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Monitor and respond to online reviews', 'description': 'Track reviews across platforms, get alerts for new reviews, and manage responses from one dashboard.', 'stats': {}, 'tech': ['Python', 'Flask'], 'features': ['Multi-platform monitoring', 'Review alerts', 'Response templates', 'Sentiment tracking'], 'video': 'review-manager-20260205-134556.webm', 'priority': 'medium'},
    'design-studio': {'name': 'Granite Design Studio', 'sector': 'Marketing & Content', 'status': 'Planned', 'tagline': 'Zero-cost design workspace for trades businesses', 'description': 'Guided-flow design workspace with dark theme, browser-style tabs, free asset sources only (Unsplash, Pexels, Pixabay, Iconify, Google Fonts). Exports PNG/JPG/SVG/PDF with video editing for Reels/TikTok/Shorts.', 'stats': {}, 'tech': ['Python', 'Flask', 'JavaScript'], 'features': ['Guided design workflow', 'Free asset sources only', 'Video editing for social', 'PNG/JPG/SVG/PDF export'], 'video': None, 'priority': 'medium'},
    'super-admin': {'name': 'Super Admin Panel', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Google-style admin panel for the trades ecosystem', 'description': 'Custom-built admin panel modeled after Google\'s admin interface. Manages all trades-side systems, user accounts, system health, and configuration from a single dashboard. Separate from the admin panel built into Lead Hunter Pro.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Google-style admin interface', 'Cross-system management', 'User and role administration', 'System health monitoring', 'Configuration management'], 'architecture': ['Designed to mirror the look and workflow of Google\'s admin console — clean, card-based layout with sidebar navigation. Every system in the trades ecosystem can be configured from this one interface without opening individual dashboards.', 'Separate from the admin panel built into LHP, this is a standalone app focused on system-level administration: adding/removing systems, managing user roles across dashboards, and monitoring health status of all running services.'], 'journey': ['The Super Admin Panel was built because managing 30+ systems from individual admin pages was unsustainable. Having one Google-style interface where everything is managed centrally turned system administration from a chore into a one-screen operation.'], 'video': None, 'priority': 'high'},
'omniverse-apex': {'name': 'OmniVerse Apex Predator', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': 'Consumer-grade hardware running 1,000x faster than research labs', 'description': 'Proprietary optimization system that enables standard gaming hardware (RTX 3060/16GB RAM) to achieve simulation speeds previously requiring dedicated research infrastructure. Hybrid computation methods hit 43M+ FPS. Features self-evolving kernel optimization, infinite context memory architecture, distilled quantization for minimal VRAM, and real-time physics rendering at 120FPS via WebGPU.', 'stats': {'fps': '43M+', 'speedup': '1,000x'}, 'tech': ['Python', 'JAX', 'CUDA', 'Taichi', 'WebGPU', 'RWKV'], 'features': ['Taichi-JAX hybrid for 43M FPS simulations', 'FlashAttention-3 + Triton custom CUDA kernels', 'Distilled QLoRA 4-bit quantization (1GB VRAM)', 'Infinite context window via RWKV + JAX', 'Live WebGPU physics viewport at 120FPS', 'Self-evolving NEAT kernel mutation'], 'video': None, 'priority': 'flagship'},
'ironworks-engine': {'name': 'Ironworks Engine', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': '1-click safe build orchestrator for 60+ agents', 'description': 'Master orchestration system that self-builds the entire Granite ecosystem in one click. Professional-grade safety controls at every level: human approval gates, 3x error retries, per-component kill switches, and auditable logging. Full deployment from zero to production in 60 minutes.', 'stats': {'agents': '60+', 'deploy_time': '60 min'}, 'tech': ['Python', 'n8n', 'Vercel', 'Docker'], 'features': ['1-click deployment of entire ecosystem', 'Human approval gates at every level', 'Automatic error retries (3x)', 'Per-component kill switches', 'Professional-grade auditable logs', 'Zero to production in 60 minutes'], 'video': None, 'priority': 'flagship'},
    'iot-sensor-hub': {'name': 'IoT Sensor Hub', 'sector': 'IoT & Smart Systems', 'status': 'Production', 'tagline': 'Real-time sensor monitoring and alerting for trades operations', 'description': 'Centralized IoT platform for connecting sensors across job sites, shops, and equipment. Real-time temperature, humidity, vibration, and equipment health monitoring with automated alerts. Originally prototyped as part of the steel fabrication dashboard for shop floor monitoring.', 'stats': {}, 'tech': ['Python', 'MQTT', 'Flask', 'WebSocket', 'Raspberry Pi'], 'features': ['Multi-sensor real-time monitoring', 'Equipment health and vibration tracking', 'Temperature and humidity alerts', 'Shop floor environmental monitoring', 'Mobile-friendly live dashboard', 'Automated threshold alerting via SMS/email'], 'video': None, 'priority': 'medium'},
    'iot-fleet-tracker': {'name': 'Fleet & Equipment Tracker', 'sector': 'IoT & Smart Systems', 'status': 'Production', 'tagline': 'GPS tracking and maintenance scheduling for trucks and equipment', 'description': 'IoT-powered fleet management for trades companies. Track vehicle locations, monitor engine diagnostics, schedule preventive maintenance, and log equipment usage hours. Designed for landscaping fleets, construction equipment, and service vehicles.', 'stats': {}, 'tech': ['Python', 'Flask', 'GPS/OBD-II', 'SQLite', 'Mapbox'], 'features': ['Real-time GPS vehicle tracking', 'OBD-II engine diagnostics', 'Preventive maintenance scheduling', 'Equipment usage hour logging', 'Fuel consumption tracking', 'Route optimization'], 'video': None, 'priority': 'medium'},
    'smart-shop': {'name': 'Smart Shop Controller', 'sector': 'IoT & Smart Systems', 'status': 'Production', 'tagline': 'Automated shop environment control for fabrication and service bays', 'description': 'IoT automation for trade shop environments — automated ventilation based on air quality sensors, lighting control, compressor and tool power management, and safety system integration. Originally designed for steel fabrication shops with welding fume detection.', 'stats': {}, 'tech': ['Python', 'MQTT', 'Raspberry Pi', 'Relay Controllers'], 'features': ['Air quality monitoring with auto-ventilation', 'Welding fume detection and extraction', 'Automated lighting and power management', 'Compressor scheduling', 'Safety system integration', 'Energy usage optimization'], 'video': None, 'priority': 'medium'},
    'robo-dispatch': {'name': 'Robotic Dispatch System', 'sector': 'Robotics & Automation', 'status': 'Production', 'tagline': 'Automated material handling and delivery for shop floors', 'description': 'Robotic dispatch and routing system for automated material movement within fabrication shops and warehouses. Integrates with job scheduling to pre-stage materials, route autonomous carts, and track delivery completion.', 'stats': {}, 'tech': ['Python', 'ROS2', 'Flask', 'Computer Vision'], 'features': ['Autonomous cart routing and dispatch', 'Job-based material pre-staging', 'Delivery completion tracking', 'Integration with trades dashboards', 'Collision avoidance pathfinding', 'Multi-robot coordination'], 'video': None, 'priority': 'medium'},
    'robo-inspection': {'name': 'Automated Inspection System', 'sector': 'Robotics & Automation', 'status': 'Production', 'tagline': 'Computer vision quality inspection for fabricated parts', 'description': 'Automated visual inspection system using computer vision to check weld quality, dimensional accuracy, and surface defects on fabricated parts. Camera-based with AI classification trained on real shop data. Reduces manual QC time and catches defects humans miss.', 'stats': {}, 'tech': ['Python', 'OpenCV', 'TensorFlow', 'Flask', 'USB Cameras'], 'features': ['Weld quality inspection via computer vision', 'Dimensional accuracy measurement', 'Surface defect detection', 'AI classification trained on real shop data', 'Pass/fail grading with photo evidence', 'Integration with job tracking system'], 'video': None, 'priority': 'medium'},
    'robo-arm-controller': {'name': 'Robotic Arm Controller', 'sector': 'Robotics & Automation', 'status': 'Production', 'tagline': 'Programmable robotic arm integration for repetitive shop tasks', 'description': 'Control interface for integrating programmable robotic arms into trades workflows. Handles repetitive tasks like material cutting, sorting, welding prep, and parts assembly. Visual programming interface so operators don\'t need to write code.', 'stats': {}, 'tech': ['Python', 'ROS2', 'Flask', 'Arduino/PLC'], 'features': ['Visual task programming interface', 'Repetitive task automation (cutting, sorting, assembly)', 'Safety zone enforcement', 'Integration with job scheduler', 'Operator-friendly — no coding required', 'Emergency stop and override controls'], 'video': None, 'priority': 'medium'},
    'analytics-dashboard': {'name': 'Analytics Dashboard', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Business intelligence and KPI tracking for trades companies', 'description': 'Centralized analytics dashboard with real-time KPI tracking, revenue charts, job completion metrics, and trend analysis. Designed for trades business owners who want to see how their company is performing at a glance.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Real-time KPI tracking', 'Revenue and profit charts', 'Job completion metrics', 'Trend analysis and forecasting', 'Custom report builder', 'Export to PDF and Excel'], 'video': 'analytics-dashboard-20260205-135946.webm', 'priority': 'medium'},
    'appointment-scheduler': {'name': 'Appointment Scheduler', 'sector': 'Client Management', 'status': 'Production', 'tagline': 'Online booking and appointment management for service businesses', 'description': 'Client-facing booking system with calendar management, automated reminders, availability windows, and integration with your trades dashboard. Customers book online, you manage from one screen.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Online client booking portal', 'Calendar management', 'Automated email and SMS reminders', 'Availability window settings', 'Recurring appointment support', 'Dashboard integration'], 'video': 'appointment-scheduler-20260205-135041.webm', 'priority': 'medium'},
    'budget-tracker': {'name': 'Budget Tracker', 'sector': 'Finance', 'status': 'Production', 'tagline': 'Job budgeting and cost tracking for trades projects', 'description': 'Track project budgets against actuals in real time. Material costs, labor hours, equipment rental, and overhead — all in one place with variance alerts when jobs go over budget.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Project budget creation', 'Real-time cost tracking', 'Material and labor cost breakdown', 'Budget variance alerts', 'Profitability analysis', 'Historical comparison'], 'video': 'budget-tracker-20260205-135734.webm', 'priority': 'medium'},
    'business-dashboard': {'name': 'Business Dashboard', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Executive overview dashboard for trades business owners', 'description': 'High-level business overview with revenue summaries, active jobs, crew status, upcoming schedule, and alerts. The one screen a business owner checks every morning.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Revenue summary widgets', 'Active job status board', 'Crew availability overview', 'Upcoming schedule preview', 'Alert and notification center', 'Quick-action shortcuts'], 'video': 'business-dashboard-20260205-135912.webm', 'priority': 'medium'},
    'content-calendar': {'name': 'Content Calendar', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Plan and schedule marketing content across all channels', 'description': 'Visual content planning calendar for trades businesses. Schedule blog posts, social media, email campaigns, and promotions. Drag-and-drop interface with content templates for common trades marketing needs.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Visual drag-and-drop calendar', 'Multi-channel planning', 'Content templates for trades', 'Scheduling and auto-publish', 'Team collaboration', 'Performance tracking'], 'video': 'content-calendar-20260205-134708.webm', 'priority': 'medium'},
    'contract-manager': {'name': 'Contract Manager', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Contract creation, tracking, and compliance management', 'description': 'Create, store, and track contracts with clients, subcontractors, and vendors. Template library, expiration alerts, and compliance tracking. Never miss a renewal or let a contract lapse.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Contract template library', 'Digital signature support', 'Expiration and renewal alerts', 'Compliance tracking', 'Version history', 'Searchable contract vault'], 'video': 'contract-manager-20260205-135158.webm', 'priority': 'medium'},
    'customer-support-bot': {'name': 'Customer Support Bot', 'sector': 'Client Management', 'status': 'Production', 'tagline': 'AI-powered customer service automation for trades businesses', 'description': 'Automated customer support chatbot trained on trades-specific FAQs. Handles scheduling questions, quote requests, job status inquiries, and common service questions 24/7 without staff involvement.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'Ollama AI'], 'features': ['24/7 automated customer responses', 'Trades-specific FAQ training', 'Quote request handling', 'Job status inquiries', 'Escalation to human support', 'Conversation logging and analytics'], 'video': 'customer-support-bot-20260205-135351.webm', 'priority': 'medium'},
    'document-organizer': {'name': 'Document Organizer', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Automated document sorting and filing for trades businesses', 'description': 'Automatically sort, tag, and file business documents — permits, contracts, invoices, inspection reports, photos, and compliance paperwork. Searchable vault with folder templates for every trade.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Automated document sorting', 'Smart tagging and categorization', 'Searchable document vault', 'Trade-specific folder templates', 'Compliance document tracking', 'Bulk upload and processing'], 'video': 'document-organizer-20260205-134834.webm', 'priority': 'medium'},
    'employee-directory': {'name': 'Employee Directory', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Team management and employee information hub', 'description': 'Centralized employee directory with contact info, certifications, skills, emergency contacts, and availability. Quick-reference for dispatchers and managers who need to find the right person fast.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Employee profiles and contact info', 'Certification and license tracking', 'Skills and qualifications database', 'Emergency contact management', 'Availability and schedule view', 'Search and filter by skill or cert'], 'video': 'employee-directory-20260205-135237.webm', 'priority': 'medium'},
    'expense-tracker': {'name': 'Expense Tracker', 'sector': 'Finance', 'status': 'Production', 'tagline': 'Business expense tracking and receipt management', 'description': 'Track business expenses, capture receipts, categorize spending, and generate expense reports. Built for trades businesses that need to track fuel, materials, tools, and job-specific costs.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Expense entry and categorization', 'Receipt capture and storage', 'Job-specific expense tagging', 'Expense report generation', 'Spending trend analysis', 'Export for tax preparation'], 'video': 'expense-tracker-20260205-135658.webm', 'priority': 'medium'},
    'goal-tracker': {'name': 'Goal Tracker', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Business goal setting and progress monitoring', 'description': 'Set revenue targets, job completion goals, growth milestones, and team objectives. Visual progress tracking with automated check-ins and milestone alerts.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Revenue and growth goal setting', 'Visual progress dashboards', 'Milestone tracking and alerts', 'Team objective assignments', 'Quarterly and annual planning', 'Historical goal performance'], 'video': 'goal-tracker-20260205-140020.webm', 'priority': 'medium'},
    'hr-onboarding': {'name': 'HR Onboarding', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'New hire onboarding and training management', 'description': 'Streamline new employee onboarding with checklists, document collection, training schedules, and progress tracking. Get new hires field-ready faster with trade-specific onboarding templates.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Onboarding checklist templates', 'Document collection and storage', 'Training schedule management', 'Progress tracking per hire', 'Trade-specific onboarding paths', 'Certification requirement tracking'], 'video': 'hr-onboarding-20260206.webm', 'priority': 'medium'},
    'inventory-manager': {'name': 'Inventory Manager', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Parts and materials inventory tracking with reorder alerts', 'description': 'Track materials, parts, tools, and supplies across job sites and warehouses. Automated reorder alerts, vendor management, and usage tracking tied to specific jobs.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Real-time inventory tracking', 'Automated reorder alerts', 'Vendor and supplier management', 'Job-specific material allocation', 'Barcode and manual entry', 'Usage history and reporting'], 'video': 'inventory-manager-20260205-134949.webm', 'priority': 'medium'},
    'invoice-automation': {'name': 'Invoice Automation', 'sector': 'Finance', 'status': 'Production', 'tagline': 'Automated invoicing and payment tracking', 'description': 'Generate professional invoices from completed jobs, send automatically, track payments, and follow up on overdue accounts. PDF export with your branding, line items from job data, and payment integration.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Auto-generate from job data', 'Branded PDF invoices', 'Automated sending and reminders', 'Payment tracking and aging', 'Overdue account follow-up', 'Stripe and QuickBooks integration'], 'video': 'invoice-automation-20260205-135629.webm', 'priority': 'medium'},
    'job-scheduler': {'name': 'Job Scheduler', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Drag-and-drop job scheduling and crew dispatch', 'description': 'Visual scheduling board for assigning jobs to crews and equipment. Drag-and-drop calendar, conflict detection, route optimization suggestions, and automated crew notifications.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Drag-and-drop scheduling', 'Crew and equipment assignment', 'Conflict and overlap detection', 'Route optimization suggestions', 'Automated crew notifications', 'Weather-aware scheduling'], 'video': 'job-scheduler-20260205-134745.webm', 'priority': 'medium'},
    'knowledge-base': {'name': 'Knowledge Base', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Internal wiki and documentation system for your team', 'description': 'Build an internal knowledge base for your trades business. SOPs, safety procedures, equipment manuals, troubleshooting guides, and training materials — all searchable and accessible by your crew.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Searchable article system', 'Category and tag organization', 'Rich text editor with images', 'Version history and revisions', 'Role-based access control', 'Mobile-friendly for field access'], 'video': 'knowledge-base-20260205-135600.webm', 'priority': 'medium'},
    'meeting-notes': {'name': 'Meeting Notes', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Meeting documentation with action item tracking', 'description': 'Capture meeting notes, assign action items, track follow-ups, and share summaries with your team. Templates for safety meetings, client meetings, and project kickoffs.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Meeting note templates', 'Action item assignment', 'Follow-up tracking and reminders', 'Team sharing and distribution', 'Searchable meeting archive', 'Attendee management'], 'video': 'meeting-notes-20260205-135503.webm', 'priority': 'medium'},
    'project-tracker': {'name': 'Project Tracker', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Multi-phase project management for trades jobs', 'description': 'Track projects from bid to completion with phase management, milestone tracking, budget monitoring, and team assignments. Built for multi-week trades projects with multiple crews and phases.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['Multi-phase project management', 'Milestone tracking', 'Budget vs actual monitoring', 'Team and crew assignments', 'Client communication log', 'Photo documentation per phase'], 'video': 'project-tracker-20260205-134914.webm', 'priority': 'medium'},
    'survey-builder': {'name': 'Survey Builder', 'sector': 'Marketing & Content', 'status': 'Production', 'tagline': 'Customer feedback surveys and satisfaction tracking', 'description': 'Create and send customer satisfaction surveys after job completion. Track NPS scores, collect testimonials, and identify improvement areas. Automated survey triggers tied to job status changes.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Custom survey builder', 'Automated post-job triggers', 'NPS score tracking', 'Testimonial collection', 'Response analytics', 'Email and SMS delivery'], 'video': 'survey-builder-20260205-134637.webm', 'priority': 'medium'},
    'time-tracker': {'name': 'Time Tracker', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Crew time tracking with job costing integration', 'description': 'GPS-verified clock-in/out for crews in the field. Track hours per job, per employee, per week. Automatic overtime calculations, break compliance, and payroll export. Ties directly into job costing.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'JavaScript'], 'features': ['GPS-verified clock-in/out', 'Per-job time allocation', 'Overtime and break tracking', 'Payroll export', 'Job cost integration', 'Mobile-friendly field entry'], 'video': 'time-tracker-20260205-135830.webm', 'priority': 'medium'},
    'vendor-manager': {'name': 'Vendor Manager', 'sector': 'Operations & Admin', 'status': 'Production', 'tagline': 'Supplier and vendor relationship management', 'description': 'Track vendors, compare pricing, manage purchase orders, and monitor delivery performance. Keep all your supplier relationships organized with contact info, payment terms, and order history.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite'], 'features': ['Vendor profiles and contacts', 'Price comparison tracking', 'Purchase order management', 'Delivery performance monitoring', 'Payment terms tracking', 'Order history and reporting'], 'video': 'vendor-manager-20260205-135317.webm', 'priority': 'medium'},
    'ai-answering-service': {'name': 'AI Answering Service', 'sector': 'Client Management', 'status': 'In Development', 'tagline': 'AI-powered phone and message answering for trades businesses', 'description': 'Never miss a call again. AI answering service handles incoming calls and messages 24/7, qualifies leads, books appointments, answers common questions, and routes urgent calls to the right person. Trained on your specific business and services.', 'stats': {}, 'tech': ['Python', 'Flask', 'Twilio', 'Ollama AI', 'WebSocket'], 'features': ['24/7 AI call and message handling', 'Lead qualification and routing', 'Appointment booking integration', 'Custom business training', 'Urgent call escalation', 'Call transcript logging and analytics'], 'video': None, 'priority': 'high'},
    'document-automation': {'name': 'Document Automation Service', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': 'Automated document processing and generation for any trade', 'description': 'Automated document workflows — generate contracts, proposals, permits, compliance reports, and delivery packages from templates and job data. Eliminates manual paperwork across every trade.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'PDF Generation'], 'features': ['Template-based document generation', 'Auto-fill from job and client data', 'Compliance document packaging', 'Permit and inspection report automation', 'Branded PDF output', 'Batch processing for large projects'], 'video': None, 'priority': 'high'},
    'ai-review-reputation': {'name': 'AI Review Response & Reputation Manager', 'sector': 'Marketing & Content', 'status': 'In Development', 'tagline': 'AI-powered review responses and online reputation management', 'description': 'Monitor reviews across Google, Yelp, Facebook, and BBB. AI generates professional, personalized responses to every review — positive or negative. Tracks your reputation score over time and alerts you to review trends.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'Ollama AI'], 'features': ['Multi-platform review monitoring', 'AI-generated personalized responses', 'Reputation score tracking', 'Negative review alerts and escalation', 'Response approval workflow', 'Review trend analytics'], 'video': None, 'priority': 'high'},
    'ecommerce-return-bot': {'name': 'E-Commerce Return Reduction Bot', 'sector': 'Lead Generation & Sales', 'status': 'In Development', 'tagline': 'AI bot that reduces e-commerce return rates and saves revenue', 'description': 'AI-powered system that intercepts return requests, identifies the reason, and offers targeted solutions — exchanges, store credit, troubleshooting, or personalized alternatives. Reduces return rates and recovers revenue that would otherwise be lost.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'Ollama AI'], 'features': ['Return request interception', 'AI reason analysis and routing', 'Targeted solution offers', 'Exchange and store credit automation', 'Return rate analytics', 'Revenue recovery tracking'], 'video': None, 'priority': 'high'},
    'safety-compliance-bot': {'name': 'Safety & Compliance Bot', 'sector': 'Operations & Admin', 'status': 'In Development', 'tagline': 'Automated safety checks and compliance tracking for job sites', 'description': 'AI-powered safety and compliance system for trades job sites. Daily safety checklists, incident reporting, OSHA compliance tracking, certification verification, and automated safety briefings. Keeps your crews safe and your business compliant.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'Ollama AI'], 'features': ['Daily safety checklist automation', 'Incident reporting and tracking', 'OSHA compliance monitoring', 'Crew certification verification', 'Automated safety briefings', 'Compliance audit trail'], 'video': None, 'priority': 'high'},
    'scope-identifier': {'name': 'Steel Scope Identifier', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'AI-powered blueprint reading and steel scope analysis', 'description': 'Three-panel Bloomberg-style interface for steel detailing and fabrication scope analysis. Claude Vision reads blueprints and structural drawings, cross-references against a 741-section AISC weight table, runs Go/No-Go feasibility checks, and delivers analytics on scope viability. Built for steel detailers and fabricators who need to evaluate project scope fast and accurately.', 'stats': {'sections': '741', 'test_phases': '9', 'grade': 'A'}, 'tech': ['Python', 'Flask', 'SQLite', 'Claude Vision API', 'SendGrid'], 'features': ['Three-panel Bloomberg-style UI', '741-section AISC steel weight table', 'AI blueprint reading via Claude Vision', 'Go/No-Go feasibility engine', 'Scope analytics dashboard', 'Email delivery via SendGrid', '52-test verification engine (Grade A)', 'PDF and drawing analysis'], 'video': None, 'priority': 'flagship'},
    'bidding-system': {'name': 'Bidding Intelligence System', 'sector': 'Lead Generation & Sales', 'status': 'Production', 'tagline': 'AI-powered bid analysis and competitive intelligence for trades', 'description': 'Analyze bid opportunities, track win/loss rates, compare against competitors, and optimize pricing strategy. AI-assisted bid preparation with historical data analysis to help you win more profitable jobs.', 'stats': {}, 'tech': ['Python', 'Flask', 'SQLite', 'Ollama AI'], 'features': ['Bid opportunity tracking', 'Win/loss rate analytics', 'Competitor analysis', 'AI-assisted bid preparation', 'Historical pricing data', 'Profitability optimization'], 'video': None, 'priority': 'high'},
}

SECTORS = [
    ('Lead Generation & Sales', 'lead-sales'),
    ('Trades Dashboards', 'trades'),
    ('Client Management', 'client'),
    ('Marketing & Content', 'marketing'),
    ('Finance', 'finance'),
    ('Quality & Testing', 'testing'),
    ('Operations & Admin', 'operations'),
    ('IoT & Smart Systems', 'iot'),
    ('Robotics & Automation', 'robotics'),
]

SOCIAL = {
    'linkedin': 'https://www.linkedin.com/in/jon-anderson-418122300',
    'facebook': 'https://www.facebook.com/jon.anderson.236899',
    'medium': 'https://medium.com/@axelfrankie525',
    'youtube': 'https://www.youtube.com/@granitemodels',
    'github': 'https://github.com/granitemodels-hub',
    'x': 'https://x.com/granitemodels',
    'email': 'granitemodels@gmail.com',
}

@app.route('/')
def index():
    flagships = {k: v for k, v in PROJECTS.items() if k in ('lead-hunter-pro', 'file-processor', 'granite-tester')}
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

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', social=SOCIAL)

@app.route('/terms')
def terms():
    return render_template('terms.html', social=SOCIAL)


@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        business = request.form.get('business', '')
        phone = request.form.get('phone', '')
        trade = request.form.get('trade', '')
        interest = request.form.get('interest', '')
        message = request.form.get('message', '')
        # Send via SendGrid
        try:
            import requests as _req
            sg_key = 'SG.HvOfqghiS0O7d-0xHeNtUA.9OhSEuFmDIOc5yhyWL8lfn1wh1jg1oPC7S'
            body_html = f"""
            <h2>New Lead from granitemodels.store</h2>
            <table style="border-collapse:collapse;font-family:Arial;">
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Name</td><td style="padding:8px;border-bottom:1px solid #ddd;">{name}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Email</td><td style="padding:8px;border-bottom:1px solid #ddd;">{email}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Business</td><td style="padding:8px;border-bottom:1px solid #ddd;">{business}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Phone</td><td style="padding:8px;border-bottom:1px solid #ddd;">{phone}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Trade</td><td style="padding:8px;border-bottom:1px solid #ddd;">{trade}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;border-bottom:1px solid #ddd;">Interested In</td><td style="padding:8px;border-bottom:1px solid #ddd;">{interest}</td></tr>
            <tr><td style="padding:8px;font-weight:bold;">Message</td><td style="padding:8px;">{message}</td></tr>
            </table>
            """
            _req.post('https://api.sendgrid.com/v3/mail/send', json={
                'personalizations': [{'to': [{'email': 'jon@granitemodels.store'}]}],
                'from': {'email': 'leads@granitemodels.store', 'name': 'Granite Store'},
                'subject': f'[NEW LEAD] {name} - {interest} - {trade}',
                'content': [{'type': 'text/html', 'value': body_html}]
            }, headers={'Authorization': f'Bearer {sg_key}', 'Content-Type': 'application/json'}, timeout=10)
        except Exception as e:
            print(f'[SendGrid] Error: {e}')
        return render_template('pricing.html', social=SOCIAL, success=True)
    return render_template('pricing.html', social=SOCIAL, success=False)

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(os.path.join(app.root_path, 'videos'), filename)

@app.route('/sitemap.xml')
def sitemap():
    pages = ['/', '/story', '/systems', '/process', '/roadmap', '/pricing', '/contact']
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
