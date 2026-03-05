"""
README content for all Granite Models projects.
Each key matches a slug in app.py PROJECTS dict.
Content is pre-formatted HTML for direct template injection.
"""

READMES = {

'lead-hunter-pro': """
<h2>Overview</h2>
<p>Lead Hunter Pro v2 is the flagship product of Granite Models Automations — a complete B2B lead generation platform built as a single-file Flask application. It handles the full lead lifecycle: scrape businesses from 5 sources, score them with AI, enrich with email and social data, deliver to clients with territory exclusivity, collect feedback, and auto-adjust scoring.</p>

<p>This is not a prototype. It's 14,600+ lines of production Python running 81+ routes across 27 database tables. Every feature was built to solve a real problem that trades businesses face when trying to find and manage leads.</p>

<h2>Architecture</h2>
<p>Single-file Flask monolith by design — one Python file containing all routes, templates, logic, and scheduled jobs. This makes deployment dead simple: copy one file, restart. The database is SQLite, stored separately from the app.</p>

<p><strong>Why single-file?</strong> Because the target users are trades businesses, not engineering teams. One file means one thing to deploy, one thing to back up, one thing to troubleshoot. The entire system runs on a single port (6092) with zero external dependencies beyond Python and a few pip packages.</p>

<h2>The Scraper Engine</h2>
<p>Five scraper sources run through a unified interface:</p>
<ul>
<li><strong>Google Places API</strong> — Primary source. Pulls 20 businesses per run by industry and location with ratings, reviews, and contact info.</li>
<li><strong>Yelp Fusion API</strong> — Secondary source with rich review data. Ready to activate when API key budget is available.</li>
<li><strong>Better Business Bureau</strong> — Accreditation and complaint data for trust scoring.</li>
<li><strong>Thumbtack</strong> — Service professional listings with pricing data.</li>
<li><strong>YellowPages</strong> — Traditional directory data for broad coverage.</li>
</ul>
<p>An "ALL" mode runs every available source in sequence with deduplication. Batch scraping by state and industry is supported for large-scale lead generation.</p>

<h2>AI Integration</h2>
<p>The built-in AI assistant uses a four-provider failover chain: Anthropic Claude → Ollama (local llama3.1) → OpenAI → keyword fallback. It has full context about the lead database and can answer questions like "How many landscaping leads do I have in New Hampshire?" by querying the actual database.</p>
<p>The AI can also propose actions (approve/reject workflow) like adjusting lead scores, flagging stale leads, or suggesting scrape targets — all with human approval gates.</p>

<h2>Email System</h2>
<p>SendGrid-first with SMTP fallback. Campaign builder with audience segmentation, drip sequence automation with configurable delays, open/click tracking pixels, CAN-SPAM compliant unsubscribe handling, and a branded email template. The test email endpoint verifies the full send path works before launching campaigns.</p>

<h2>Compliance</h2>
<p>Built for nationwide coverage: DNC list management, opt-out tracking, suppression lists, consent logging, and an automated 45-day data wipe that purges aged lead data for regulatory compliance. Every email includes CAN-SPAM required unsubscribe links and physical address.</p>

<h2>Client System</h2>
<p>Self-service client portal with geographic preferences, plan tiers (Spark/Ignite/Blaze), lead delivery preferences, and feedback ratings. Territory exclusivity ensures a lead locked to one client can't be delivered to another. Invoice generation uses the GMA-YYYY-NNNN format with Stripe integration for payment processing.</p>
""",

'organized-system': """
<h2>Overview</h2>
<p>ORGANIZED_SYSTEM is an institutional-grade automated trading platform — 219,000+ lines of Python across 830 files, built in approximately 4 weeks at 12-18 hours per day. It's the largest single project in the Granite ecosystem and demonstrates the scale of what a solo developer can build when they commit fully.</p>

<h2>The Buddy System</h2>
<p>The platform is built as 6 interconnected programs, each handling a distinct domain:</p>

<ul>
<li><strong>Bot Buddy</strong> — Core trading bot orchestration and execution engine. Manages order placement, position sizing, and real-time market data processing across all 6 armies.</li>
<li><strong>Agent Buddy</strong> — Multi-LLM orchestration layer with three specialized AI agents: Architect (strategy design), Analyst (market analysis), and Sentinel (risk monitoring). Uses MemRL memory framework so agents learn across sessions.</li>
<li><strong>Bot Swarm</strong> — Distributed swarm intelligence for coordinated trading across multiple strategies simultaneously. Tournament system lets modules compete — winning strategies get more capital allocation.</li>
<li><strong>Finance Buddy</strong> — Portfolio management, risk analysis using the Risk Assessment Framework (RAF), and position correlation tracking. Connects to FRED for macroeconomic data integration.</li>
<li><strong>Tester Buddy</strong> — Strategy backtesting and validation framework. Paper trading simulation with realistic slippage, fees, and latency modeling before any strategy goes live.</li>
<li><strong>Banker Buddy</strong> — Full accounting system with Plaid integration for bank account connectivity. Tracks every transaction, calculates P&L, and generates financial reports.</li>
</ul>

<h2>The 6 Trading Armies</h2>
<p>Each army specializes in a market segment with dedicated strategies, risk parameters, and capital allocation:</p>
<ul>
<li><strong>FOREX</strong> — Major and minor currency pairs</li>
<li><strong>CRYPTO</strong> — Top cryptocurrencies by market cap</li>
<li><strong>EQUITIES</strong> — Stock market with sector rotation</li>
<li><strong>DEFI</strong> — Decentralized finance yield strategies</li>
<li><strong>PENNY</strong> — Small-cap momentum plays</li>
<li><strong>ARBITRAGE</strong> — Cross-exchange price discrepancies</li>
</ul>

<h2>Excel Dashboard</h2>
<p>A standalone Excel dashboard runs alongside the main system, logging every trade, position change, and performance metric in real-time. Charts and graphs break down performance by army, strategy, and time period. This provides a familiar interface for reviewing trading data without needing to access the web dashboards.</p>

<h2>Current Status</h2>
<p>The system is 95% production-ready. A planned 90-day paper trading validation period will run all 6 armies simultaneously before any live capital is deployed. This is a personal project separate from the Granite Models trades business — it demonstrates the range and depth of what I can build.</p>
""",

'granite-tester': """
<h2>Overview</h2>
<p>The Granite Tester is the quality assurance backbone of the entire Granite ecosystem. Most solo developers don't build QA infrastructure — they test manually and hope for the best. This system runs automated integration tests against live endpoints, generates Production Readiness Reports with letter grades, and tracks quality over time.</p>

<h2>Five Integrated Sections</h2>

<p><strong>1. Main Test Runner (30 Systems)</strong><br>
The core testing interface. Select any of the 30+ registered systems from the sidebar, configure test parameters, and run. Tests hit real HTTP endpoints, check response codes, verify page content, and time every request. Results stream live via Server-Sent Events so you watch tests execute in real-time.</p>

<p><strong>2. Trades Dashboard Tester</strong><br>
Dedicated test engine for the trades dashboard series (Landscape, Steel, HVAC, etc.). Runs phase-based integration tests covering: core pages, CRUD operations, role-based security, job scheduling, crew management, equipment tracking, and financial modules. Follows Google SWE/SRE PRR standards.</p>

<p><strong>3. LHP v2 Integration Tester</strong><br>
Purpose-built test engine for Lead Hunter Pro v2 with 7 test phases and 40+ individual tests: Connectivity & Core Pages, Scraper Sources, Enrichment Pipeline, Email & SendGrid, Drip Sequences, Compliance & Data Safety, and API Endpoints. Each phase generates its own sub-score that rolls up into the overall PRR.</p>

<p><strong>4. Research Page with AI Summarizer</strong><br>
Every test run is saved to a research database. The Research page lets you browse historical runs, compare results across time, and use an AI summarizer to analyze patterns in test failures. If the same endpoint has been failing for 3 runs straight, the AI flags it.</p>

<p><strong>5. Admin Panel</strong><br>
Custom admin interface designed after Google's admin console. Register new systems, configure test parameters, manage test data files, and view system-wide quality metrics. This is where you add new systems to the testing pipeline.</p>

<h2>PRR Scoring</h2>
<p>Every test run generates a Production Readiness Report:</p>
<ul>
<li><strong>Raw Score</strong> — 10 points per passing test</li>
<li><strong>Grade</strong> — A (90%+), B (80%+), C (70%+), D (60%+), F (below 60%)</li>
<li><strong>Phase Breakdown</strong> — Score per test phase with visual bars</li>
<li><strong>Findings Engine</strong> — Categorizes issues as BUG (critical), WARNING (important), or INFO (minor)</li>
<li><strong>Recommendations</strong> — Automated suggestions for improving the score</li>
</ul>
""",

'landscape-dashboard': """
<h2>Overview</h2>
<p>The Landscape Dashboard is the reference build for the entire trades dashboard series. It was built first and most completely — 49 database tables, 67 HTML templates, 180+ route decorators — and every subsequent trades dashboard (Steel, HVAC, Plumbing, etc.) follows its architecture.</p>

<h2>Architecture</h2>
<p>Role-based security with three permission levels: Owner (full access), Admin (management access), and Crew (field access only). Every route checks permissions before rendering. The database schema covers every aspect of running a landscaping company.</p>

<h2>Core Modules</h2>
<ul>
<li><strong>Job Management</strong> — Create, schedule, assign, and track jobs from estimate through completion. Photo documentation, time logging, and material tracking per job.</li>
<li><strong>Crew Management</strong> — Employee profiles, certifications, schedule availability, timesheet entry, and payroll prep. Crew leads can update job status from the field.</li>
<li><strong>Equipment Tracking</strong> — Every mower, trailer, truck, and tool tracked with maintenance schedules, service history, and replacement cost tracking.</li>
<li><strong>Client CRM</strong> — Full client database with property details, service history, communication log, and satisfaction tracking. Recurring service scheduling.</li>
<li><strong>Invoicing</strong> — Generate invoices from completed jobs, track payments, send reminders. Integrates with the financial reporting module.</li>
<li><strong>Weather Integration</strong> — Weather-aware scheduling that flags outdoor jobs when rain is forecast.</li>
<li><strong>Analytics Dashboard</strong> — Revenue charts, crew utilization, job completion rates, equipment costs, and seasonal trends. Export to CSV.</li>
</ul>

<h2>Why This Matters</h2>
<p>Most landscaping companies run on paper, spreadsheets, and memory. This system replaces all of that with one dashboard that the owner, office manager, and crew leads can all access with appropriate permissions. It was built by someone who spent years on landscaping crews and knows exactly what information matters in the field vs. the office.</p>
""",

'empire-dashboard': """
<h2>Overview</h2>
<p>The Empire Dashboard is the master command center for the entire Granite Models ecosystem. It provides a single interface to monitor, manage, and navigate across all 10 corporate sectors and 30+ systems.</p>

<h2>Design</h2>
<p>Dropdown navigation organized by business division with tab switching between tools within each sector. The dashboard shows system health status, revenue metrics, and quick-launch buttons for every tool in the ecosystem. Think of it as the mission control — you see everything from one screen.</p>

<h2>Sectors Managed</h2>
<p>Sales & Revenue, Marketing & Content, Client Management, Finance, Operations, Communications, Legal & Compliance, Analytics & Intelligence, IoT & Smart Systems, and Robotics & Automation. Each sector has its own navigation group with the tools that belong to it.</p>
""",

'super-admin': """
<h2>Overview</h2>
<p>The Super Admin Panel is a standalone administration interface modeled after Google's admin console design. It manages the trades-side systems separately from the Empire Dashboard, providing a focused admin experience for user management, system configuration, and health monitoring.</p>

<h2>Design Inspiration</h2>
<p>The interface follows Google Workspace Admin's layout patterns — clean card-based sections, search-first navigation, and role-based access controls. This familiar design means anyone who's used Google Admin can navigate it immediately.</p>
""",

}
