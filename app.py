"""
GRANITE MODELS - Store
Port: 6091
Real 30 Granite Models Systems + Demo Videos
"""
from flask import Flask, render_template, jsonify, request, redirect, send_from_directory
from flask import render_template_string
import secrets as _sec
import sqlite3
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'granite-models-prod-2026')

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'granite.db')
STRIPE_KEY = os.environ.get('STRIPE_KEY', '')
VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'videos')
PACKAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages')

def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# REAL 30 GRANITE MODELS SYSTEMS
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

CATEGORIES = {
    'lead-sales': {'name': 'Lead & Sales', 'color': '#00e0ff', 'icon': '🎯'},
    'marketing': {'name': 'Marketing', 'color': '#ff4d9e', 'icon': '📢'},
    'operations': {'name': 'Operations', 'color': '#00ff88', 'icon': '⚙️'},
    'communication': {'name': 'Communication', 'color': '#aa44ff', 'icon': '💬'},
    'finance': {'name': 'Finance', 'color': '#ffaf00', 'icon': '💰'},
    'reporting': {'name': 'Reporting', 'color': '#00ddff', 'icon': '📊'},
    'automation': {'name': 'Automation', 'color': '#ff6600', 'icon': '🤖'},
}

PRODUCTS = {
    # â•â•â• LEAD & SALES (5) â•â•â•
    'lead-hunter-pro': {
        'name': 'Lead Hunter Pro', 'price': 299, 'category': 'lead-sales', 'port': 6001,
        'desc': 'AI-powered lead capture and scoring. Scrapes leads from Apollo.io, LinkedIn, Google Maps, Yelp. Scores each lead 0-100 and pushes hot leads to your CRM.',
        'features': ['Multi-source lead scraping', 'AI-powered lead scoring', 'CRM auto-integration', 'Real-time email alerts', 'Lead database with search', 'Daily/weekly reports'],
        'video': 'lead-hunter-pro-20260205-094919.webm'
    },
    'sales-pipeline': {
        'name': 'Sales Pipeline', 'price': 349, 'category': 'lead-sales', 'port': 6002,
        'desc': 'Visual deal tracking from first contact to closed sale. Drag-drop pipeline with revenue forecasting and team performance.',
        'features': ['Visual pipeline board', 'Deal tracking & stages', 'Revenue forecasting', 'Team performance metrics', 'Activity logging', 'Email integration'],
        'video': 'sales-pipeline-20260205-131725.webm'
    },
    'quote-generator': {
        'name': 'Quote Generator', 'price': 199, 'category': 'lead-sales', 'port': 6003,
        'desc': 'Create professional quotes in seconds. Templates, line items, tax calculation, and PDF export.',
        'features': ['Professional templates', 'Line item builder', 'Tax calculation', 'PDF export', 'Client portal', 'Follow-up reminders'],
        'video': 'quote-generator-20260205-140207.webm'
    },
    'referral-tracker': {
        'name': 'Referral Tracker', 'price': 249, 'category': 'lead-sales', 'port': 6004,
        'desc': 'Track referrals and automate rewards. Full referral program management with payout tracking.',
        'features': ['Referral link generation', 'Reward automation', 'Payout tracking', 'Leaderboards', 'Email notifications', 'Analytics dashboard'],
        'video': 'referral-tracker-20260205-134349.webm'
    },
    'proposal-generator': {
        'name': 'Proposal Generator', 'price': 299, 'category': 'lead-sales', 'port': 6005,
        'desc': 'Professional proposals with e-signature. Build proposals from templates with pricing tables and client approval.',
        'features': ['Template library', 'Pricing tables', 'E-signature integration', 'Client portal', 'Version tracking', 'Analytics'],
        'video': 'proposal-generator-20260205-134415.webm'
    },

    # â•â•â• MARKETING (5) â•â•â•
    'social-media-manager': {
        'name': 'Social Media Manager', 'price': 299, 'category': 'marketing', 'port': 6006,
        'desc': 'Schedule posts across all platforms. Post once, reach everywhere with 12+ platform support.',
        'features': ['LinkedIn, Twitter, Facebook', 'Instagram, TikTok, YouTube', 'Discord, Telegram, Reddit', 'Content scheduling', 'Analytics tracking', 'Bulk upload'],
        'video': 'social-media-manager-20260205-134453.webm'
    },
    'email-campaign': {
        'name': 'Email Campaign Engine', 'price': 349, 'category': 'marketing', 'port': 6007,
        'desc': 'Design and track email campaigns. Drag-drop builder, A/B testing, automation sequences.',
        'features': ['Drag-drop builder', 'A/B testing', 'Automation sequences', 'Analytics & tracking', 'List segmentation', 'Template library'],
        'video': 'email-campaign-20260205-134527.webm'
    },
    'review-manager': {
        'name': 'Review Manager', 'price': 249, 'category': 'marketing', 'port': 6008,
        'desc': 'Monitor reviews across Google, Yelp, Facebook. Auto-respond and track sentiment.',
        'features': ['Multi-platform monitoring', 'Auto-response templates', 'Sentiment analysis', 'Review request automation', 'Rating tracking', 'Alert system'],
        'video': 'review-manager-20260205-134556.webm'
    },
    'survey-builder': {
        'name': 'Survey Builder', 'price': 249, 'category': 'marketing', 'port': 6009,
        'desc': 'Custom surveys with analytics. Build surveys, collect responses, and analyze results.',
        'features': ['Drag-drop builder', 'Multiple question types', 'Response analytics', 'NPS tracking', 'Export reports', 'Embed widgets'],
        'video': 'survey-builder-20260205-134637.webm'
    },
    'content-calendar': {
        'name': 'Content Calendar', 'price': 249, 'category': 'marketing', 'port': 6010,
        'desc': 'Plan content across all channels. Visual calendar with team collaboration and approval workflows.',
        'features': ['Visual calendar view', 'Multi-channel planning', 'Team collaboration', 'Approval workflows', 'Content templates', 'Analytics'],
        'video': 'content-calendar-20260205-134708.webm'
    },

    # â•â•â• OPERATIONS (10) â•â•â•
    'job-scheduler': {
        'name': 'Job Scheduler', 'price': 299, 'category': 'operations', 'port': 6011,
        'desc': 'Drag-and-drop scheduling for jobs and crews. Assign teams, track progress, manage timelines.',
        'features': ['Drag-drop scheduling', 'Crew assignment', 'Progress tracking', 'Timeline view', 'Conflict detection', 'Mobile access'],
        'video': 'job-scheduler-20260205-134745.webm'
    },
    'document-organizer': {
        'name': 'Document Organizer', 'price': 249, 'category': 'operations', 'port': 6012,
        'desc': 'AI-powered filing system. Auto-categorize, tag, and search documents instantly.',
        'features': ['AI categorization', 'Full-text search', 'Tag system', 'Version control', 'Duplicate detection', 'Export tools'],
        'video': 'document-organizer-20260205-134834.webm'
    },
    'project-tracker': {
        'name': 'Project Tracker', 'price': 299, 'category': 'operations', 'port': 6013,
        'desc': 'Visual project management. Kanban boards, Gantt charts, task dependencies.',
        'features': ['Kanban boards', 'Gantt charts', 'Task dependencies', 'Time tracking', 'Team workload', 'Reporting'],
        'video': 'project-tracker-20260205-134914.webm'
    },
    'inventory-manager': {
        'name': 'Inventory Manager', 'price': 299, 'category': 'operations', 'port': 6014,
        'desc': 'Track stock with low-stock alerts. Multi-location inventory with barcode scanning.',
        'features': ['Multi-location tracking', 'Low-stock alerts', 'Barcode scanning', 'Purchase orders', 'Supplier management', 'Reporting'],
        'video': 'inventory-manager-20260205-134949.webm'
    },
    'appointment-scheduler': {
        'name': 'Appointment Scheduler', 'price': 299, 'category': 'operations', 'port': 6015,
        'desc': 'Online booking with reminders. Customer self-scheduling with calendar integration.',
        'features': ['Online booking page', 'SMS/email reminders', 'Calendar sync', 'Waitlist management', 'Payment integration', 'Staff scheduling'],
        'video': 'appointment-scheduler-20260205-135041.webm'
    },
    'contract-manager': {
        'name': 'Contract Manager', 'price': 249, 'category': 'operations', 'port': 6016,
        'desc': 'Track contracts and renewals. Never miss a renewal date with automated alerts.',
        'features': ['Contract database', 'Renewal alerts', 'Expiration tracking', 'Document storage', 'Approval workflows', 'Reporting'],
        'video': 'contract-manager-20260205-135158.webm'
    },
    'employee-directory': {
        'name': 'Employee Directory', 'price': 199, 'category': 'operations', 'port': 6017,
        'desc': 'Staff profiles and contact info. Searchable directory with org chart and skill tracking.',
        'features': ['Staff profiles', 'Org chart', 'Skill tracking', 'Contact directory', 'Search & filter', 'Export tools'],
        'video': 'employee-directory-20260205-135237.webm'
    },
    'hr-onboarding': {
        'name': 'HR Onboarding', 'price': 299, 'category': 'operations', 'port': 6024,
        'desc': 'New hire checklists and onboarding workflows. Automate day-one to day-ninety.',
        'features': ['Onboarding checklists', 'Document collection', 'Task automation', 'Progress tracking', 'Template library', 'Compliance tracking'],
        'video': 'hr-onboarding-20260206.webm'
    },
    'vendor-manager': {
        'name': 'Vendor Manager', 'price': 199, 'category': 'operations', 'port': 6020,
        'desc': 'Supplier database with performance tracking. Manage vendors, contracts, and spend.',
        'features': ['Vendor database', 'Performance ratings', 'Contract tracking', 'Spend analytics', 'Communication log', 'RFP management'],
        'video': 'vendor-manager-20260205-135317.webm'
    },

    # â•â•â• COMMUNICATION (3) â•â•â•
    'customer-support-bot': {
        'name': 'Customer Support Bot', 'price': 349, 'category': 'communication', 'port': 6021,
        'desc': 'AI chat that answers questions 24/7. Deploy on any website with knowledge base training.',
        'features': ['24/7 AI chat', 'Knowledge base training', 'Widget embed', 'Lead capture', 'Ticket escalation', 'Analytics'],
        'video': 'customer-support-bot-20260205-135351.webm'
    },
    'meeting-notes': {
        'name': 'Meeting Notes', 'price': 149, 'category': 'communication', 'port': 6022,
        'desc': 'Capture notes with action items. Auto-transcribe, extract tasks, and send summaries.',
        'features': ['Note capture', 'Action item extraction', 'Summary generation', 'Team sharing', 'Search & archive', 'Calendar integration'],
        'video': 'meeting-notes-20260205-135503.webm'
    },
    'knowledge-base': {
        'name': 'Knowledge Base', 'price': 249, 'category': 'communication', 'port': 6023,
        'desc': 'Internal wiki with search. Build a searchable knowledge base for your team.',
        'features': ['Wiki-style editor', 'Full-text search', 'Category organization', 'Version history', 'Team permissions', 'Public/private articles'],
        'video': 'knowledge-base-20260205-135600.webm'
    },

    # â•â•â• FINANCE (4) â•â•â•
    'invoice-automation': {
        'name': 'Invoice Automation', 'price': 249, 'category': 'finance', 'port': 6024,
        'desc': 'Auto-generate and send invoices. Recurring billing, payment tracking, and reminders.',
        'features': ['Auto-generation', 'Recurring billing', 'Payment tracking', 'Late reminders', 'PDF export', 'Client portal'],
        'video': 'invoice-automation-20260205-135629.webm'
    },
    'expense-tracker': {
        'name': 'Expense Tracker', 'price': 199, 'category': 'finance', 'port': 6025,
        'desc': 'Capture receipts for tax prep. Receipt OCR, auto-categorization, and report generation.',
        'features': ['Receipt OCR', 'Auto-categorization', 'Tax prep reports', 'Approval workflows', 'Budget tracking', 'Export tools'],
        'video': 'expense-tracker-20260205-135658.webm'
    },
    'budget-tracker': {
        'name': 'Budget Tracker', 'price': 199, 'category': 'finance', 'port': 6026,
        'desc': 'Set budgets and track spending. Visual dashboards with alerts when approaching limits.',
        'features': ['Budget setting', 'Spending tracking', 'Visual dashboards', 'Limit alerts', 'Category breakdown', 'Forecasting'],
        'video': 'budget-tracker-20260205-135734.webm'
    },
    'time-tracker': {
        'name': 'Time Tracker', 'price': 199, 'category': 'finance', 'port': 6027,
        'desc': 'Log billable hours with one click. Timer, manual entry, and client invoicing.',
        'features': ['One-click timer', 'Manual entry', 'Client billing', 'Project allocation', 'Team tracking', 'Invoice integration'],
        'video': 'time-tracker-20260205-135830.webm'
    },

    # â•â•â• REPORTING (3) â•â•â•
    'business-dashboard': {
        'name': 'Business Dashboard', 'price': 299, 'category': 'reporting', 'port': 6028,
        'desc': 'Your business at a glance. KPIs, charts, and real-time metrics in one place.',
        'features': ['KPI tracking', 'Real-time charts', 'Custom widgets', 'Data integrations', 'Scheduled reports', 'Team sharing'],
        'video': 'business-dashboard-20260205-135912.webm'
    },
    'analytics-dashboard': {
        'name': 'Analytics Dashboard', 'price': 349, 'category': 'reporting', 'port': 6029,
        'desc': 'Real-time metrics visualization. Advanced analytics with drill-down and custom reports.',
        'features': ['Real-time metrics', 'Custom dashboards', 'Drill-down analysis', 'Scheduled exports', 'Multi-source data', 'Trend detection'],
        'video': 'analytics-dashboard-20260205-135946.webm'
    },
    'goal-tracker': {
        'name': 'Goal Tracker', 'price': 199, 'category': 'reporting', 'port': 6030,
        'desc': 'Set and track goals with OKR framework. Visual progress tracking for teams.',
        'features': ['OKR framework', 'Visual progress', 'Team alignment', 'Milestone tracking', 'Check-in reminders', 'Reporting'],
        'video': 'goal-tracker-20260205-140020.webm'
    },

    # â•â•â• AUTOMATION (1) â•â•â•
    'agent-bot-builder': {
        'name': 'Agent Bot Builder', 'price': 499, 'category': 'automation', 'port': 6018,
        'desc': 'Visual workflow builder with AI. Build custom automation agents with drag-drop logic.',
        'features': ['Visual workflow builder', 'AI agent creation', 'API connectors', 'Conditional logic', 'Scheduling', 'Multi-step automation'],
        'video': 'coming-soon'
    },
}

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# VIDEO HELPERS
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def get_video_info(product_id):
    """Check if demo video exists for product"""
    p = PRODUCTS.get(product_id)
    if not p or not p.get('video'):
        return None
    video_path = os.path.join(VIDEO_DIR, p['video'])
    if os.path.exists(video_path):
        size_mb = round(os.path.getsize(video_path) / (1024*1024), 1)
        return {'filename': p['video'], 'size_mb': size_mb, 'exists': True}
    return None

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# DATABASE
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def init_store_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        product_id TEXT, product_name TEXT,
        category TEXT, price REAL,
        customer_email TEXT,
        status TEXT DEFAULT 'pending',
        stripe_session TEXT
    )''')
    conn.commit()
    conn.close()

init_store_db()

# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# ROUTES
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

@app.route('/store')
def store():
    return render_template('store.html', products=PRODUCTS, categories=CATEGORIES)

@app.route('/product/<product_id>')
def product_detail(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        return "Product not found", 404
    video = get_video_info(product_id)
    cat_info = CATEGORIES.get(product.get('category'), {})
    pkg = _get_package(product_id)
    pkg_info = None
    if pkg:
        pkg_info = {'size_kb': round(os.path.getsize(pkg)/1024, 1), 'filename': os.path.basename(pkg)}
    return render_template('product.html',
        product=product, product_id=product_id,
        video=video, cat_info=cat_info, package=pkg_info)

@app.route('/demo-video/<filename>')
def serve_demo_video(filename):
    """Serve demo videos from D:\\GRANITE-FINAL\\videos"""
    return send_from_directory(VIDEO_DIR, filename)

@app.route('/api/products')
def api_products():
    cat = request.args.get('category', 'all')
    result = []
    for pid, p in PRODUCTS.items():
        if cat != 'all' and p['category'] != cat:
            continue
        cat_info = CATEGORIES.get(p['category'], {})
        has_video = bool(p.get('video') and os.path.exists(os.path.join(VIDEO_DIR, p['video'])))
        result.append({**p, 'id': pid,
            'cat_name': cat_info.get('name', ''),
            'cat_color': cat_info.get('color', '#ffaa00'),
            'cat_icon': cat_info.get('icon', ''),
            'has_video': has_video})
    return jsonify(result)

@app.route('/api/checkout/<product_id>', methods=['POST'])
def checkout(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    if STRIPE_KEY:
        try:
            import stripe
            stripe.api_key = STRIPE_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': product['name']},
                    'unit_amount': int(product['price'] * 100),
                }, 'quantity': 1}],
                mode='payment',
                success_url=f'http://localhost:6091/success?session_id={{CHECKOUT_SESSION_ID}}',
                cancel_url=f'http://localhost:6091/product/{product_id}',
            )
            conn = get_db()
            c = conn.cursor()
            c.execute("INSERT INTO orders (product_id,product_name,category,price,stripe_session) VALUES (?,?,?,?,?)",
                (product_id, product['name'], product['category'], product['price'], session.id))
            conn.commit(); conn.close()
            return jsonify({'url': session.url})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        # Demo mode
        conn = get_db()
        c = conn.cursor()
        c.execute("INSERT INTO orders (product_id,product_name,category,price,status) VALUES (?,?,?,?,?)",
            (product_id, product['name'], product['category'], product['price'], 'demo'))
        conn.commit(); conn.close()
        return jsonify({'url': f'/success?demo=true&product={product_id}'})

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/api/orders')
def api_orders():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM orders ORDER BY timestamp DESC LIMIT 50")
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/api/store/stats')
def store_stats():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM orders")
    total_orders = c.fetchone()[0]
    c.execute("SELECT COALESCE(SUM(price),0) FROM orders WHERE status != 'cancelled'")
    total_rev = c.fetchone()[0]
    conn.close()
    # Count by category
    cat_counts = {}
    for p in PRODUCTS.values():
        cat = p['category']
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    # Count videos
    video_count = sum(1 for p in PRODUCTS.values()
        if p.get('video') and os.path.exists(os.path.join(VIDEO_DIR, p['video'])))
    # Count packages
    pkg_count = sum(1 for pid in PRODUCTS if _get_package(pid))
    return jsonify({
        'total_products': len(PRODUCTS),
        'total_orders': total_orders,
        'total_revenue': total_rev,
        'video_count': video_count,
        'package_count': pkg_count,
        'categories': cat_counts
    })

def _get_package(product_id):
    """Find zip package for a product"""
    # Try exact match first, then variations
    candidates = [
        f"{product_id}.zip",
        product_id.replace('-', '_') + '.zip',
    ]
    for c in candidates:
        path = os.path.join(PACKAGE_DIR, c)
        if os.path.exists(path):
            return path
    return None

@app.route('/api/package/<product_id>')
def package_info(product_id):
    pkg = _get_package(product_id)
    if pkg:
        size_kb = round(os.path.getsize(pkg) / 1024, 1)
        return jsonify({'exists': True, 'size_kb': size_kb, 'filename': os.path.basename(pkg)})
    return jsonify({'exists': False})

@app.route('/download/<product_id>')
def download_package(product_id):
    pkg = _get_package(product_id)
    if not pkg:
        return "Package not found", 404
    return send_from_directory(os.path.dirname(pkg), os.path.basename(pkg), as_attachment=True)


# ---- LANDING PAGE ----
from landing import CSS, HOMEPAGE

@app.route('/')
def landing():
    from flask import session as s
    if '_csrf_token' not in s:
        s['_csrf_token'] = _sec.token_hex(32)
    return render_template_string(HOMEPAGE, success=request.args.get('success'), error=request.args.get('error'), csrf_token=lambda: s['_csrf_token'])

@app.route('/request-access', methods=['POST'])
def request_access():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    company = request.form.get('company', '').strip()
    if not name or not email:
        return redirect('/?error=Please+fill+in+name+and+email')
    conn = get_db()
    try:
        conn.execute("CREATE TABLE IF NOT EXISTS leads (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, company TEXT, source TEXT, timestamp TEXT DEFAULT CURRENT_TIMESTAMP)")
        conn.execute("INSERT OR IGNORE INTO leads (name, email, company, source) VALUES (?, ?, ?, ?)", (name, email, company, 'landing'))
        conn.commit()
    except: pass
    finally: conn.close()
    return redirect('/store')

if __name__ == '__main__':
    print("=" * 60)
    print("  GRANITE MODELS - Store")
    print(f"  http://localhost:6091")
    print(f"  {len(PRODUCTS)} systems loaded")
    vids = sum(1 for p in PRODUCTS.values()
        if p.get('video') and os.path.exists(os.path.join(VIDEO_DIR, p['video'])))
    print(f"  {vids} demo videos available")
    print("=" * 60)
    app.run(host='0.0.0.0', port=6091, debug=True)



