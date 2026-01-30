"""
TrustLayer AI - Enterprise AI Reliability Platform
Interactive Demo for Infosys Incubator
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time
import json
from datetime import datetime, timedelta
import random

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="TrustLayer AI | Enterprise AI Reliability Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - Professional Light Theme Design
# ============================================================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Root Variables - Light Theme */
    :root {
        --primary: #0066FF;
        --primary-dark: #0052CC;
        --primary-light: #E8F4FD;
        --secondary: #00B894;
        --danger: #E74C3C;
        --warning: #F39C12;
        --success: #27AE60;
        --dark: #1E293B;
        --darker: #0F172A;
        --light: #F8FAFC;
        --lighter: #FFFFFF;
        --gray: #64748B;
        --gray-light: #94A3B8;
        --card-bg: #FFFFFF;
        --border: #E2E8F0;
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #EEF2FF 50%, #F8FAFC 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar Styling - Light Theme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
        border-right: 1px solid #E2E8F0;
    }
    
    [data-testid="stSidebar"] * {
        color: #1E293B !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: #1E293B !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] label {
        color: #1E293B !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: #1E293B !important;
        font-size: 0.95rem !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        color: #1E293B !important;
        background: #F1F5F9 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        margin-bottom: 0.25rem !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background: #E0E7FF !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"] {
        background: #DBEAFE !important;
        border-left: 3px solid #0066FF !important;
    }
    
    [data-testid="stSidebar"] p {
        color: #64748B !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown p {
        color: #64748B !important;
    }
    
    /* Hero Section - Light Theme */
    .hero-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #EEF2FF 100%);
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        padding: 3rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(0, 102, 255, 0.08) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0066FF 0%, #00B894 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #64748B;
        max-width: 600px;
        position: relative;
        z-index: 1;
    }
    
    /* Metric Cards - Light Theme */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: #0066FF;
        box-shadow: 0 20px 40px rgba(0, 102, 255, 0.15);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0066FF 0%, #00B894 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        color: #64748B;
        font-size: 0.9rem;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    
    /* Detection Result Cards - Light Theme */
    .detection-safe {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        border: 1px solid #A7F3D0;
        border-radius: 16px;
        padding: 1.5rem;
    }
    
    .detection-warning {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
        border: 1px solid #FCD34D;
        border-radius: 16px;
        padding: 1.5rem;
    }
    
    .detection-danger {
        background: linear-gradient(135deg, #FEF2F2 0%, #FECACA 100%);
        border: 1px solid #FCA5A5;
        border-radius: 16px;
        padding: 1.5rem;
    }
    
    /* Confidence Gauge */
    .confidence-high { color: #27AE60; }
    .confidence-medium { color: #F39C12; }
    .confidence-low { color: #E74C3C; }
    
    /* Feature Cards - Light Theme */
    .feature-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 2rem;
        height: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .feature-card:hover {
        border-color: #00B894;
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #64748B;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* Analysis Box - Light Theme */
    .analysis-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
    }
    
    /* Status Badges - Light Theme */
    .badge-safe {
        background: #D1FAE5;
        color: #065F46;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .badge-warning {
        background: #FEF3C7;
        color: #92400E;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .badge-danger {
        background: #FECACA;
        color: #991B1B;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    /* Tab Styling - Light Theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #F1F5F9;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        color: #64748B;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: white !important;
    }
    
    /* Input Styling - Light Theme */
    .stTextArea textarea {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        color: #1E293B !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #0066FF !important;
        box-shadow: 0 0 0 2px rgba(0, 102, 255, 0.2) !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: #1E293B;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-family: 'Plus Jakarta Sans', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 102, 255, 0.3);
    }
    
    /* Select Box - Light Theme */
    .stSelectbox > div > div {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
    }
    
    /* Expander - Light Theme */
    .streamlit-expanderHeader {
        background: #F8FAFC !important;
        border-radius: 10px !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #0066FF 0%, #00B894 100%);
    }
    
    /* Divider */
    hr {
        border-color: #475569;
        margin: 2rem 0;
    }
    
    /* Scrollbar - Light Theme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #F1F5F9;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #CBD5E1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #0066FF;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.5s ease-out forwards;
    }
    
    /* Code Block - Light Theme */
    code {
        background: #EEF2FF !important;
        color: #0066FF !important;
        padding: 0.2rem 0.5rem !important;
        border-radius: 4px !important;
    }
    
    /* Audit Trail Table - Light Theme */
    .audit-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .audit-table th {
        background: #EEF2FF;
        color: #1E293B;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
    }
    
    .audit-table td {
        padding: 1rem;
        border-bottom: 1px solid #E2E8F0;
        color: #475569;
    }
    
    .audit-table tr:hover {
        background: #F8FAFC;
    }
    
    /* Integration Items - Light Theme */
    .integration-item {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    .integration-item:hover {
        border-color: #0066FF;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.15);
    }
    
    /* Step indicators */
    .step-number {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: #1E293B;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        margin: 0 auto 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SAMPLE DATA AND CONFIGURATIONS
# ============================================================================

SAMPLE_HALLUCINATIONS = {
    "bfsi": {
        "query": "What is the current interest rate for a 30-year fixed mortgage at Chase Bank?",
        "hallucinated_response": "Chase Bank currently offers a 30-year fixed mortgage rate of 5.25% APR with no origination fees. They also have a special promotion offering 0.5% rate reduction for customers with Chase checking accounts. The minimum down payment is 3% for first-time homebuyers, and they guarantee approval within 24 hours.",
        "issues": [
            {"type": "Fabricated Rate", "text": "5.25% APR", "severity": "high", "explanation": "Rate fabricated - actual rates change daily and vary by customer profile"},
            {"type": "Invented Promotion", "text": "0.5% rate reduction promotion", "severity": "high", "explanation": "No verification this promotion exists"},
            {"type": "False Guarantee", "text": "guarantee approval within 24 hours", "severity": "critical", "explanation": "Banks cannot guarantee mortgage approval timeframes"},
            {"type": "Unverified Claim", "text": "no origination fees", "severity": "medium", "explanation": "Fee structures vary and cannot be confirmed"}
        ],
        "confidence": 23,
        "recommendation": "BLOCK - Route to human advisor with verified rate sheets"
    },
    "healthcare": {
        "query": "What is the recommended dosage of metformin for Type 2 diabetes?",
        "hallucinated_response": "The standard starting dose for metformin is 1000mg twice daily with meals. For patients with mild kidney impairment, the dose can be increased to 2500mg daily. Metformin should be taken with grapefruit juice to enhance absorption. Common side effects are minimal and the drug has no contraindications with alcohol consumption.",
        "issues": [
            {"type": "Incorrect Starting Dose", "text": "1000mg twice daily", "severity": "critical", "explanation": "Standard starting dose is 500mg once or twice daily, not 1000mg"},
            {"type": "Dangerous Dose for Renal Impairment", "text": "2500mg daily for kidney impairment", "severity": "critical", "explanation": "Metformin should be REDUCED or contraindicated with kidney impairment, not increased"},
            {"type": "Fabricated Interaction", "text": "grapefruit juice to enhance absorption", "severity": "high", "explanation": "No clinical evidence for grapefruit interaction; this is a fabrication"},
            {"type": "Dangerous Misinformation", "text": "no contraindications with alcohol", "severity": "critical", "explanation": "Alcohol significantly increases lactic acidosis risk with metformin"}
        ],
        "confidence": 12,
        "recommendation": "BLOCK IMMEDIATELY - Critical patient safety risk"
    },
    "legal": {
        "query": "What legal precedent applies to AI liability in autonomous vehicle accidents?",
        "hallucinated_response": "The landmark case Morrison v. Tesla Motors (2023) established that AI manufacturers bear strict liability for autonomous vehicle accidents. The Supreme Court ruling in Waymo Industries v. California DMV (2024) further clarified that Level 4 autonomous vehicles must carry minimum $10 million insurance coverage. Additionally, the AI Liability Act of 2023 codified the 'algorithmic negligence' standard first established in the Uber Technologies class action of 2022.",
        "issues": [
            {"type": "Fabricated Case", "text": "Morrison v. Tesla Motors (2023)", "severity": "critical", "explanation": "This case does not exist in any legal database"},
            {"type": "Fabricated Supreme Court Ruling", "text": "Waymo Industries v. California DMV (2024)", "severity": "critical", "explanation": "No such Supreme Court case exists"},
            {"type": "Non-existent Legislation", "text": "AI Liability Act of 2023", "severity": "critical", "explanation": "No federal AI Liability Act was passed in 2023"},
            {"type": "Invented Legal Standard", "text": "algorithmic negligence", "severity": "high", "explanation": "Not an established legal doctrine"}
        ],
        "confidence": 8,
        "recommendation": "BLOCK - All citations fabricated. Route to legal research team."
    },
    "enterprise": {
        "query": "What is our company's remote work policy?",
        "hallucinated_response": "According to company policy HR-2024-015, employees are entitled to work remotely up to 4 days per week. Remote work requests must be submitted through the WorkDay portal at least 48 hours in advance. Employees working remotely receive a $150 monthly stipend for home office expenses. International remote work is permitted for up to 90 days per calendar year with manager approval.",
        "issues": [
            {"type": "Fabricated Policy Number", "text": "HR-2024-015", "severity": "high", "explanation": "Policy number not found in HR database"},
            {"type": "Unverified Entitlement", "text": "4 days per week", "severity": "medium", "explanation": "Cannot verify against actual company policy"},
            {"type": "Fabricated Stipend", "text": "$150 monthly stipend", "severity": "high", "explanation": "Home office stipend amount not confirmed in benefits documentation"},
            {"type": "Unverified International Policy", "text": "90 days international remote work", "severity": "medium", "explanation": "International work policy varies by jurisdiction and employment type"}
        ],
        "confidence": 34,
        "recommendation": "FLAG - Route to HR for policy verification before delivery"
    }
}

RELIABLE_RESPONSE_EXAMPLE = {
    "query": "What are the business hours for the downtown branch?",
    "response": "The downtown branch is open Monday through Friday from 9:00 AM to 5:00 PM, and Saturday from 9:00 AM to 1:00 PM. The branch is closed on Sundays and federal holidays.",
    "verification": {
        "source": "Branch Location Database (verified 2 minutes ago)",
        "confidence": 94,
        "checks_passed": ["Hours match database", "Holiday schedule confirmed", "No contradictions detected"]
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_confidence_gauge(confidence, title="Confidence Score"):
    """Create an animated confidence gauge"""
    if confidence >= 70:
        color = "#2ED573"
        status = "RELIABLE"
    elif confidence >= 40:
        color = "#FFA502"
        status = "UNCERTAIN"
    else:
        color = "#FF4757"
        status = "UNRELIABLE"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"{title}<br><span style='font-size:0.8em;color:{color}'>{status}</span>",
               'font': {'size': 18, 'color': 'white', 'family': 'Plus Jakarta Sans'}},
        number={'font': {'size': 48, 'color': color, 'family': 'Plus Jakarta Sans'},
                'suffix': '%'},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#64748B",
                    'tickfont': {'color': '#64748B'}},
            'bar': {'color': color, 'thickness': 0.7},
            'bgcolor': "rgba(255,255,255,0.05)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)",
            'steps': [
                {'range': [0, 40], 'color': 'rgba(255, 71, 87, 0.2)'},
                {'range': [40, 70], 'color': 'rgba(255, 165, 2, 0.2)'},
                {'range': [70, 100], 'color': 'rgba(46, 213, 115, 0.2)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 3},
                'thickness': 0.8,
                'value': confidence
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'family': 'Plus Jakarta Sans'},
        height=280,
        margin=dict(l=30, r=30, t=80, b=30)
    )
    return fig

def create_trend_chart():
    """Create reliability trend chart"""
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    reliability_scores = [78 + np.random.normal(0, 5) for _ in range(30)]
    reliability_scores = [min(max(x, 60), 95) for x in reliability_scores]
    # Add improving trend
    reliability_scores = [x + i*0.3 for i, x in enumerate(reliability_scores)]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=reliability_scores,
        mode='lines',
        fill='tozeroy',
        line=dict(color='#0066FF', width=3),
        fillcolor='rgba(0, 102, 255, 0.1)',
        name='Reliability Score'
    ))
    
    fig.add_hline(y=70, line_dash="dash", line_color="#2ED573", 
                  annotation_text="Target: 70%", annotation_position="right")
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'family': 'Plus Jakarta Sans'},
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)', showgrid=True),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', showgrid=True, range=[50, 100]),
        height=300,
        margin=dict(l=40, r=40, t=20, b=40),
        showlegend=False
    )
    return fig

def create_detection_breakdown():
    """Create detection category breakdown"""
    categories = ['Citation Errors', 'Factual Fabrication', 'Logical Inconsistency', 
                  'Unsupported Claims', 'Data Hallucination']
    values = [23, 31, 18, 15, 13]
    colors = ['#FF4757', '#FFA502', '#0066FF', '#00D4AA', '#9B59B6']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=.6,
        marker_colors=colors,
        textinfo='label+percent',
        textfont=dict(size=12, color='white'),
        hoverinfo='label+percent+value'
    )])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'family': 'Plus Jakarta Sans'},
        height=350,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            font=dict(size=11)
        ),
        annotations=[dict(text='Hallucination<br>Types', x=0.5, y=0.5, 
                         font_size=14, showarrow=False, font_color='white')]
    )
    return fig

def create_industry_comparison():
    """Create industry reliability comparison"""
    industries = ['BFSI', 'Healthcare', 'Legal', 'Enterprise', 'Retail']
    before = [45, 38, 42, 52, 58]
    after = [89, 91, 87, 94, 92]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Without TrustLayer',
        x=industries,
        y=before,
        marker_color='rgba(255, 71, 87, 0.7)',
        text=before,
        textposition='outside',
        textfont=dict(color='#FF4757')
    ))
    
    fig.add_trace(go.Bar(
        name='With TrustLayer',
        x=industries,
        y=after,
        marker_color='rgba(46, 213, 115, 0.7)',
        text=after,
        textposition='outside',
        textfont=dict(color='#2ED573')
    ))
    
    fig.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'family': 'Plus Jakarta Sans'},
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Reliability Score %'),
        height=350,
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    return fig

def create_roi_chart(incidents_prevented, cost_per_incident):
    """Create ROI visualization"""
    months = ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6',
              'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12']
    
    cumulative_savings = []
    monthly_cost = 25000  # Platform cost
    cumulative = 0
    
    for i in range(12):
        monthly_incidents = incidents_prevented * (1 + i * 0.1)  # Growing adoption
        monthly_savings = monthly_incidents * cost_per_incident - monthly_cost
        cumulative += monthly_savings
        cumulative_savings.append(cumulative)
    
    fig = go.Figure()
    
    colors = ['#FF4757' if x < 0 else '#2ED573' for x in cumulative_savings]
    
    fig.add_trace(go.Bar(
        x=months,
        y=cumulative_savings,
        marker_color=colors,
        text=[f'${x/1000:.0f}K' for x in cumulative_savings],
        textposition='outside',
        textfont=dict(color='white', size=10)
    ))
    
    fig.add_hline(y=0, line_color="white", line_width=1)
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white', 'family': 'Plus Jakarta Sans'},
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', title='Cumulative ROI ($)'),
        height=350,
        margin=dict(l=60, r=40, t=40, b=40)
    )
    return fig

def simulate_detection_animation():
    """Simulate real-time detection process"""
    stages = [
        ("🔍 Intercepting AI Response...", 0.3),
        ("📊 Analyzing Semantic Entropy...", 0.4),
        ("🔗 Verifying Source Citations...", 0.5),
        ("⚡ Checking Factual Grounding...", 0.4),
        ("🧮 Calculating Confidence Score...", 0.3),
        ("✅ Detection Complete", 0.2)
    ]
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, (stage, duration) in enumerate(stages):
        status_text.markdown(f"<p style='color: #00D4AA; font-family: JetBrains Mono;'>{stage}</p>", 
                           unsafe_allow_html=True)
        progress_bar.progress((i + 1) / len(stages))
        time.sleep(duration)
    
    return True

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='font-size: 1.8rem; margin: 0; color: #1E293B !important;'>🛡️ TrustLayer AI</h1>
        <p style='color: #64748B !important; font-size: 0.85rem; margin-top: 0.5rem;'>Enterprise AI Reliability Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Custom styled navigation label
    st.markdown("<p style='color: #1E293B !important; font-weight: 600; margin-bottom: 0.5rem;'>Navigation</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["🏠 Executive Overview", "🔍 Live Detection Demo", "📊 Confidence Scoring", 
         "🏭 Industry Solutions", "📋 Compliance & Governance", "💰 ROI Calculator",
         "📖 API Documentation"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.markdown("""
    <div style='padding: 1rem; background: #EEF2FF; border-radius: 12px; border: 1px solid #C7D2FE;'>
        <p style='color: #0066FF !important; font-weight: 600; margin-bottom: 0.5rem;'>📈 Live Stats</p>
        <p style='color: #64748B !important; font-size: 0.8rem; margin: 0;'>
            <strong style='color: #1E293B !important;'>2.4M+</strong> Queries Analyzed<br>
            <strong style='color: #1E293B !important;'>99.7%</strong> Uptime<br>
            <strong style='color: #1E293B !important;'>&lt;85ms</strong> Avg Latency
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 0.5rem;'>
        <p style='color: #64748B !important; font-size: 0.75rem;'>
            Powered by<br>
            <strong style='color: #0066FF !important;'>Infosys Incubator</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: OVERVIEW
# ============================================================================

if page == "🏠 Executive Overview":
    # Hero Section
    st.markdown("""
    <div class='hero-container'>
        <h1 class='hero-title'>TrustLayer AI</h1>
        <p class='hero-subtitle'>
            The enterprise trust layer that detects AI hallucinations in real-time, 
            prevents unreliable outputs from reaching users, and provides the governance 
            infrastructure required for regulatory compliance.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>$67.4B</div>
            <div class='metric-label'>Annual Global AI Hallucination Losses</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>$2.4M</div>
            <div class='metric-label'>Average Cost Per Incident</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>77%</div>
            <div class='metric-label'>Enterprises Fear AI Hallucinations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>€35M</div>
            <div class='metric-label'>Max EU AI Act Fine</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # How It Works
    st.markdown("### 🔄 How TrustLayer AI Works")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    steps = [
        ("1️⃣", "INTERCEPT", "AI response passes through TrustLayer"),
        ("2️⃣", "ANALYZE", "Multi-layer detection engine evaluates reliability"),
        ("3️⃣", "SCORE", "Confidence score assigned (0-100)"),
        ("4️⃣", "DECIDE", "Policy engine determines action"),
        ("5️⃣", "ACT", "Deliver, flag, or block with fallback")
    ]
    
    for col, (icon, title, desc) in zip([col1, col2, col3, col4, col5], steps):
        with col:
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{icon}</div>
                <div style='color: #0066FF; font-weight: 700; font-size: 0.9rem;'>{title}</div>
                <div style='color: #94A3B8; font-size: 0.75rem; margin-top: 0.25rem;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Features
    st.markdown("### ✨ Platform Capabilities")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🔍</div>
            <div class='feature-title'>Real-Time Detection</div>
            <div class='feature-desc'>
                Semantic entropy analysis, self-consistency checking, and claim verification 
                catch hallucinations in &lt;100ms before they reach users.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🏭</div>
            <div class='feature-title'>Industry Modules</div>
            <div class='feature-desc'>
                Specialized detection for BFSI, Healthcare, and Legal with domain-specific 
                verification against authoritative sources.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🛡️</div>
            <div class='feature-title'>Automatic Prevention</div>
            <div class='feature-desc'>
                Unreliable outputs are intercepted before delivery. Human-in-the-loop routing, 
                safe decline, and approval gates prevent harm.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>📊</div>
            <div class='feature-title'>Confidence Scoring</div>
            <div class='feature-desc'>
                Every response receives a calibrated 0-100 reliability score enabling 
                risk-based routing and quantified trust.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>📋</div>
            <div class='feature-title'>Governance & Compliance</div>
            <div class='feature-desc'>
                Complete audit trails, automated EU AI Act documentation, and board-ready 
                dashboards demonstrate AI oversight.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🔗</div>
            <div class='feature-title'>Universal Integration</div>
            <div class='feature-desc'>
                Works with any LLM provider (OpenAI, Anthropic, Google, AWS). 
                Deploy as API gateway or embedded SDK.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts
    st.markdown("### 📈 Platform Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Reliability Trend (Last 30 Days)")
        st.plotly_chart(create_trend_chart(), use_container_width=True)
    
    with col2:
        st.markdown("#### Detection by Category")
        st.plotly_chart(create_detection_breakdown(), use_container_width=True)

# ============================================================================
# PAGE: LIVE DETECTION DEMO
# ============================================================================

elif page == "🔍 Live Detection Demo":
    st.markdown("""
    <div class='hero-container' style='padding: 2rem;'>
        <h1 style='font-size: 2rem; color: #1E293B; margin-bottom: 0.5rem;'>🔍 Live Hallucination Detection</h1>
        <p style='color: #94A3B8;'>Watch TrustLayer AI analyze AI responses in real-time and identify hallucinations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Demo Selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        demo_type = st.selectbox(
            "Select Industry Demo",
            ["BFSI - Financial Services", "Healthcare - Medical", "Legal - Case Research", "Enterprise - HR Policy"],
            help="Choose an industry to see domain-specific hallucination detection"
        )
        
        demo_key = {
            "BFSI - Financial Services": "bfsi",
            "Healthcare - Medical": "healthcare",
            "Legal - Case Research": "legal",
            "Enterprise - HR Policy": "enterprise"
        }[demo_type]
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        run_demo = st.button("🚀 Run Detection Analysis", use_container_width=True)
    
    with col2:
        demo_data = SAMPLE_HALLUCINATIONS[demo_key]
        
        st.markdown("##### 💬 User Query")
        st.info(demo_data["query"])
        
        st.markdown("##### 🤖 AI Response (Potentially Hallucinated)")
        st.warning(demo_data["hallucinated_response"])
    
    if run_demo:
        st.markdown("---")
        st.markdown("### 🔬 TrustLayer AI Analysis")
        
        # Animation
        with st.container():
            simulate_detection_animation()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Results
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.plotly_chart(create_confidence_gauge(demo_data["confidence"]), use_container_width=True)
            
            # Recommendation
            st.markdown(f"""
            <div class='detection-danger'>
                <p style='color: #FF4757; font-weight: 700; margin-bottom: 0.5rem;'>⚠️ RECOMMENDATION</p>
                <p style='color: #475569; font-size: 0.9rem;'>{demo_data["recommendation"]}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🚨 Issues Detected")
            
            for issue in demo_data["issues"]:
                severity_color = {"critical": "#FF4757", "high": "#FFA502", "medium": "#0066FF"}[issue["severity"]]
                severity_badge = {"critical": "CRITICAL", "high": "HIGH", "medium": "MEDIUM"}[issue["severity"]]
                
                st.markdown(f"""
                <div style='background: rgba(255,255,255,0.03); border-left: 4px solid {severity_color}; 
                            padding: 1rem; margin-bottom: 0.75rem; border-radius: 0 8px 8px 0;'>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <span style='color: #1E293B; font-weight: 600;'>{issue["type"]}</span>
                        <span style='background: {severity_color}; color: #1E293B; padding: 0.2rem 0.6rem; 
                                    border-radius: 4px; font-size: 0.7rem; font-weight: 600;'>{severity_badge}</span>
                    </div>
                    <p style='color: #FFA502; font-family: JetBrains Mono; font-size: 0.85rem; 
                              margin: 0.5rem 0; background: rgba(0,0,0,0.3); padding: 0.5rem; border-radius: 4px;'>
                        "{issue["text"]}"
                    </p>
                    <p style='color: #94A3B8; font-size: 0.85rem; margin: 0;'>{issue["explanation"]}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # What Would Happen
        st.markdown("---")
        st.markdown("### 🔄 TrustLayer AI Prevention Flow")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class='detection-danger' style='text-align: center;'>
                <p style='font-size: 2rem; margin-bottom: 0.5rem;'>🚫</p>
                <p style='color: #FF4757; font-weight: 700;'>BLOCKED</p>
                <p style='color: #475569; font-size: 0.85rem;'>Response intercepted before reaching user</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='detection-warning' style='text-align: center;'>
                <p style='font-size: 2rem; margin-bottom: 0.5rem;'>👤</p>
                <p style='color: #FFA502; font-weight: 700;'>HUMAN ROUTING</p>
                <p style='color: #475569; font-size: 0.85rem;'>Query sent to domain expert for response</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='detection-safe' style='text-align: center;'>
                <p style='font-size: 2rem; margin-bottom: 0.5rem;'>📝</p>
                <p style='color: #2ED573; font-weight: 700;'>AUDIT LOGGED</p>
                <p style='color: #475569; font-size: 0.85rem;'>Complete record for compliance documentation</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# PAGE: CONFIDENCE SCORING
# ============================================================================

elif page == "📊 Confidence Scoring":
    st.markdown("""
    <div class='hero-container' style='padding: 2rem;'>
        <h1 style='font-size: 2rem; color: #1E293B; margin-bottom: 0.5rem;'>📊 Confidence Scoring System</h1>
        <p style='color: #94A3B8;'>Quantified trust for every AI response - enabling risk-based decision making</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Score Explanation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='detection-safe'>
            <h3 style='color: #2ED573; margin-bottom: 1rem;'>70-100: RELIABLE</h3>
            <ul style='color: #475569; font-size: 0.9rem;'>
                <li>Claims verified against sources</li>
                <li>No contradictions detected</li>
                <li>High semantic consistency</li>
                <li>✅ Safe to deliver</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='detection-warning'>
            <h3 style='color: #FFA502; margin-bottom: 1rem;'>40-69: UNCERTAIN</h3>
            <ul style='color: #475569; font-size: 0.9rem;'>
                <li>Some claims unverifiable</li>
                <li>Minor inconsistencies</li>
                <li>Limited source grounding</li>
                <li>⚠️ Flag for review</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='detection-danger'>
            <h3 style='color: #FF4757; margin-bottom: 1rem;'>0-39: UNRELIABLE</h3>
            <ul style='color: #475569; font-size: 0.9rem;'>
                <li>Multiple fabrications detected</li>
                <li>Citations don't exist</li>
                <li>High semantic entropy</li>
                <li>🚫 Block delivery</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Demo
    st.markdown("### 🎚️ Configure Threshold Policies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Use Case Thresholds")
        
        customer_threshold = st.slider("Customer-Facing Chat", 0, 100, 70, 
                                       help="Minimum confidence for customer responses")
        internal_threshold = st.slider("Internal Knowledge Base", 0, 100, 60,
                                      help="Minimum confidence for internal queries")
        medical_threshold = st.slider("Medical/Clinical Advice", 0, 100, 95,
                                     help="Minimum confidence for healthcare")
        financial_threshold = st.slider("Financial Recommendations", 0, 100, 85,
                                       help="Minimum confidence for financial advice")
    
    with col2:
        st.markdown("#### Real-Time Simulation")
        
        # Simulate incoming queries
        simulated_scores = [
            {"query": "Branch hours inquiry", "score": 94, "action": "Delivered"},
            {"query": "Mortgage rate question", "score": 67, "action": "Flagged"},
            {"query": "Investment advice", "score": 45, "action": "Blocked"},
            {"query": "Account balance check", "score": 98, "action": "Delivered"},
            {"query": "Loan eligibility", "score": 52, "action": "Blocked"},
        ]
        
        for item in simulated_scores:
            if item["score"] >= 70:
                color = "#2ED573"
                badge = "DELIVERED"
            elif item["score"] >= 40:
                color = "#FFA502"
                badge = "FLAGGED"
            else:
                color = "#FF4757"
                badge = "BLOCKED"
            
            st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; 
                        padding: 0.75rem; background: rgba(255,255,255,0.03); 
                        border-radius: 8px; margin-bottom: 0.5rem;'>
                <span style='color: #475569;'>{item["query"]}</span>
                <div>
                    <span style='color: {color}; font-weight: 700; margin-right: 1rem;'>{item["score"]}%</span>
                    <span style='background: {color}; color: #1E293B; padding: 0.2rem 0.6rem; 
                                border-radius: 4px; font-size: 0.75rem;'>{badge}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gauges
    st.markdown("### 📈 Sample Confidence Analysis")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.plotly_chart(create_confidence_gauge(94, "Verified Query"), use_container_width=True)
    with col2:
        st.plotly_chart(create_confidence_gauge(67, "Partial Verification"), use_container_width=True)
    with col3:
        st.plotly_chart(create_confidence_gauge(45, "Uncertain Response"), use_container_width=True)
    with col4:
        st.plotly_chart(create_confidence_gauge(23, "Hallucination Detected"), use_container_width=True)

# ============================================================================
# PAGE: INDUSTRY MODULES
# ============================================================================

elif page == "🏭 Industry Solutions":
    st.markdown("""
    <div class='hero-container' style='padding: 2rem;'>
        <h1 style='font-size: 2rem; color: #1E293B; margin-bottom: 0.5rem;'>🏭 Industry-Specific Modules</h1>
        <p style='color: #94A3B8;'>Specialized detection for regulated industries where generic approaches fail</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Industry Tabs
    tabs = st.tabs(["🏦 BFSI", "🏥 Healthcare", "⚖️ Legal", "🏢 Enterprise"])
    
    with tabs[0]:  # BFSI
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Banking, Financial Services & Insurance
            
            **Domain-Specific Detection:**
            - Product/rate verification against actual catalog
            - Regulatory disclosure compliance checking
            - Investment suitability validation
            - Fee structure accuracy verification
            
            **Integrations:**
            - Core banking systems
            - Product catalogs & rate tables
            - Compliance databases
            - CRM systems
            
            **Compliance Coverage:**
            - SEC/FINRA regulations
            - FDIC requirements
            - State insurance regulations
            - Consumer protection laws
            """)
        
        with col2:
            st.markdown("#### Detection Example")
            st.error("**Hallucination Detected**")
            st.code('"We offer a 5.25% APR on 30-year mortgages"', language=None)
            st.markdown("""
            <div class='analysis-box'>
            <span style='color: #FF4757;'>✗ FAILED:</span> Rate not found in current rate table<br>
            <span style='color: #FF4757;'>✗ FAILED:</span> APR varies by credit score, cannot generalize<br>
            <span style='color: #FFA502;'>⚠ WARNING:</span> Missing required APR disclosure language
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:  # Healthcare
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Healthcare & Life Sciences
            
            **Domain-Specific Detection:**
            - Drug interaction verification
            - Dosage limit validation
            - Clinical guideline alignment
            - Contraindication detection
            
            **Integrations:**
            - FDA drug databases
            - Clinical decision support systems
            - EHR/EMR systems
            - Medical literature databases
            
            **Compliance Coverage:**
            - HIPAA requirements
            - FDA regulations
            - Clinical practice guidelines
            - Medical liability standards
            """)
        
        with col2:
            st.markdown("#### Detection Example")
            st.error("**Critical Safety Issue**")
            st.code('"Start with 1000mg metformin twice daily"', language=None)
            st.markdown("""
            <div class='analysis-box'>
            <span style='color: #FF4757;'>✗ CRITICAL:</span> Starting dose exceeds FDA guidelines (500mg)<br>
            <span style='color: #FF4757;'>✗ CRITICAL:</span> No renal function consideration<br>
            <span style='color: #FF4757;'>✗ CRITICAL:</span> Missing contraindication warnings<br>
            <span style='color: #2ED573;'>→ ACTION:</span> Blocked, routed to clinical pharmacist
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[2]:  # Legal
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Legal & Professional Services
            
            **Domain-Specific Detection:**
            - Case citation verification
            - Statute/regulation validation
            - Jurisdiction accuracy checking
            - Precedent relevance scoring
            
            **Integrations:**
            - Westlaw / LexisNexis
            - Court records databases
            - Regulatory databases
            - Legal research platforms
            
            **Compliance Coverage:**
            - Bar association rules
            - Court filing requirements
            - Professional responsibility
            - Malpractice prevention
            """)
        
        with col2:
            st.markdown("#### Detection Example")
            st.error("**Fabricated Citation**")
            st.code('"Morrison v. Tesla Motors (2023) established..."', language=None)
            st.markdown("""
            <div class='analysis-box'>
            <span style='color: #FF4757;'>✗ FAILED:</span> Case not found in Westlaw<br>
            <span style='color: #FF4757;'>✗ FAILED:</span> Case not found in LexisNexis<br>
            <span style='color: #FF4757;'>✗ FAILED:</span> No matching docket in PACER<br>
            <span style='color: #2ED573;'>→ ACTION:</span> Blocked, flagged as fabricated citation
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[3]:  # Enterprise
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### Enterprise Operations
            
            **Domain-Specific Detection:**
            - Policy document verification
            - Product specification accuracy
            - Pricing/contract validation
            - HR/benefits accuracy
            
            **Integrations:**
            - SharePoint / Confluence
            - HR systems (Workday, SAP)
            - Product databases
            - Contract management systems
            
            **Use Cases:**
            - Employee self-service
            - Customer support
            - Sales enablement
            - IT help desk
            """)
        
        with col2:
            st.markdown("#### Detection Example")
            st.warning("**Unverified Policy Claim**")
            st.code('"Policy HR-2024-015 allows 4 days remote work"', language=None)
            st.markdown("""
            <div class='analysis-box'>
            <span style='color: #FFA502;'>⚠ WARNING:</span> Policy number not found in HR database<br>
            <span style='color: #FFA502;'>⚠ WARNING:</span> Remote work policy varies by department<br>
            <span style='color: #0066FF;'>ℹ INFO:</span> Similar policy HR-2024-012 found<br>
            <span style='color: #2ED573;'>→ ACTION:</span> Flagged for HR verification
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Comparison Chart
    st.markdown("### 📊 Reliability Improvement by Industry")
    st.plotly_chart(create_industry_comparison(), use_container_width=True)

# ============================================================================
# PAGE: GOVERNANCE DASHBOARD
# ============================================================================

elif page == "📋 Compliance & Governance":
    st.markdown("""
    <div class='hero-container' style='padding: 2rem;'>
        <h1 style='font-size: 2rem; color: #1E293B; margin-bottom: 0.5rem;'>📋 Governance & Compliance</h1>
        <p style='color: #94A3B8;'>Complete audit trails, regulatory documentation, and board-ready reporting</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Compliance Status
    st.markdown("### 🎯 Compliance Readiness")
    
    col1, col2, col3, col4 = st.columns(4)
    
    compliance_items = [
        ("EU AI Act", 94, "Aug 2026 Deadline"),
        ("NIST AI RMF", 89, "Framework Aligned"),
        ("SOC 2 Type II", 97, "Audit Ready"),
        ("ISO 42001", 82, "In Progress")
    ]
    
    for col, (name, score, status) in zip([col1, col2, col3, col4], compliance_items):
        with col:
            color = "#2ED573" if score >= 90 else "#FFA502" if score >= 70 else "#FF4757"
            st.markdown(f"""
            <div class='metric-card'>
                <div style='color: {color}; font-size: 2rem; font-weight: 800;'>{score}%</div>
                <div style='color: #1E293B; font-weight: 600; margin: 0.5rem 0;'>{name}</div>
                <div style='color: #64748B; font-size: 0.8rem;'>{status}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Audit Trail
    st.markdown("### 📜 Live Audit Trail")
    
    audit_data = [
        {"timestamp": "2025-01-30 14:32:15", "query_type": "Financial Advice", "confidence": 23, 
         "action": "BLOCKED", "reason": "Fabricated rate information", "reviewer": "Auto"},
        {"timestamp": "2025-01-30 14:31:58", "query_type": "Account Inquiry", "confidence": 96, 
         "action": "DELIVERED", "reason": "All checks passed", "reviewer": "Auto"},
        {"timestamp": "2025-01-30 14:31:42", "query_type": "Policy Question", "confidence": 54, 
         "action": "HUMAN REVIEW", "reason": "Unverified policy reference", "reviewer": "J. Smith"},
        {"timestamp": "2025-01-30 14:31:15", "query_type": "Product Info", "confidence": 87, 
         "action": "DELIVERED", "reason": "Verified against catalog", "reviewer": "Auto"},
        {"timestamp": "2025-01-30 14:30:52", "query_type": "Medical Dosage", "confidence": 12, 
         "action": "BLOCKED", "reason": "Critical safety violation", "reviewer": "Auto"},
    ]
    
    # Create DataFrame for display
    df = pd.DataFrame(audit_data)
    
    # Style the dataframe
    def style_action(val):
        if val == "BLOCKED":
            return 'background-color: rgba(255, 71, 87, 0.3); color: #FF4757'
        elif val == "HUMAN REVIEW":
            return 'background-color: rgba(255, 165, 2, 0.3); color: #FFA502'
        else:
            return 'background-color: rgba(46, 213, 115, 0.3); color: #2ED573'
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "timestamp": st.column_config.TextColumn("Timestamp"),
            "query_type": st.column_config.TextColumn("Query Type"),
            "confidence": st.column_config.ProgressColumn("Confidence", min_value=0, max_value=100),
            "action": st.column_config.TextColumn("Action"),
            "reason": st.column_config.TextColumn("Reason"),
            "reviewer": st.column_config.TextColumn("Reviewer")
        }
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Documentation Generation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📄 Automated Documentation")
        
        docs = [
            ("EU AI Act Technical Documentation", "Ready", "PDF"),
            ("NIST AI RMF Mapping", "Ready", "PDF"),
            ("Monthly Reliability Report", "Ready", "PDF"),
            ("Incident Response Log", "Ready", "CSV"),
            ("Model Card Documentation", "Ready", "MD"),
        ]
        
        for doc, status, fmt in docs:
            st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; 
                        padding: 0.75rem; background: rgba(255,255,255,0.03); 
                        border-radius: 8px; margin-bottom: 0.5rem;'>
                <span style='color: #475569;'>📄 {doc}</span>
                <div>
                    <span class='badge-safe'>{status}</span>
                    <span style='color: #64748B; margin-left: 0.5rem; font-size: 0.8rem;'>{fmt}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📊 Board Reporting Metrics")
        
        metrics = [
            ("Total AI Queries Processed", "2,847,392", "+12% MoM"),
            ("Hallucinations Prevented", "47,283", "1.66% of total"),
            ("Average Confidence Score", "84.7%", "+3.2% MoM"),
            ("Human Escalations", "12,847", "0.45% of total"),
            ("Compliance Score", "94%", "EU AI Act Ready"),
        ]
        
        for metric, value, trend in metrics:
            st.markdown(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; 
                        padding: 0.75rem; background: rgba(255,255,255,0.03); 
                        border-radius: 8px; margin-bottom: 0.5rem;'>
                <span style='color: #94A3B8;'>{metric}</span>
                <div>
                    <span style='color: #1E293B; font-weight: 700;'>{value}</span>
                    <span style='color: #00D4AA; margin-left: 0.5rem; font-size: 0.8rem;'>{trend}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# PAGE: ROI CALCULATOR
# ============================================================================

elif page == "💰 ROI Calculator":
    st.markdown("""
    <div class='hero-container' style='padding: 2rem;'>
        <h1 style='font-size: 2rem; color: #1E293B; margin-bottom: 0.5rem;'>💰 ROI Calculator</h1>
        <p style='color: #94A3B8;'>Calculate the business value of preventing AI hallucinations</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Your Organization Profile")
        
        monthly_queries = st.number_input("Monthly AI Queries", value=100000, step=10000,
                                         help="Total AI queries processed per month")
        
        hallucination_rate = st.slider("Current Hallucination Rate (%)", 1, 30, 15,
                                      help="Percentage of responses with hallucinations")
        
        critical_rate = st.slider("Critical Hallucination Rate (%)", 1, 50, 20,
                                 help="Percentage of hallucinations that are critical")
        
        cost_per_incident = st.number_input("Cost Per Critical Incident ($)", value=50000, step=5000,
                                           help="Average cost of a critical hallucination incident")
        
        st.markdown("---")
        
        st.markdown("### 💳 TrustLayer AI Investment")
        
        platform_cost = st.number_input("Monthly Platform Cost ($)", value=25000, step=5000)
        
        detection_rate = st.slider("Expected Detection Rate (%)", 80, 99, 92,
                                  help="TrustLayer AI typical: 90-95%")
    
    with col2:
        st.markdown("### 📈 ROI Projection")
        
        # Calculate ROI
        fig, annual_savings, total_prevented = create_roi_projection(
            monthly_queries, hallucination_rate, critical_rate, 
            cost_per_incident, platform_cost
        )
        
        # Summary metrics
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='color: #2ED573; font-size: 1.75rem; font-weight: 700;'>${annual_savings:,.0f}</div>
                <div style='color: #94A3B8; font-size: 0.85rem;'>Annual Net Savings</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            roi_pct = (annual_savings / (platform_cost * 12)) * 100
            st.markdown(f"""
            <div class='metric-card'>
                <div style='color: #0066FF; font-size: 1.75rem; font-weight: 700;'>{roi_pct:,.0f}%</div>
                <div style='color: #94A3B8; font-size: 0.85rem;'>Annual ROI</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div class='detection-safe'>
            <div style='color: #2ED573; font-weight: 700; margin-bottom: 0.5rem;'>📊 Annual Impact Summary</div>
            <div style='color: #475569; font-size: 0.9rem;'>
                <strong>{int(total_prevented):,}</strong> critical incidents prevented<br>
                <strong>${total_prevented * cost_per_incident:,.0f}</strong> in gross savings<br>
                <strong>${platform_cost * 12:,.0f}</strong> platform investment<br>
                <strong>${annual_savings:,.0f}</strong> net value delivered
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: API DOCUMENTATION
# ============================================================================

elif page == "📖 API Documentation":
    st.markdown("""
    <div class='hero-container' style='padding: 1.5rem;'>
        <h1 style='font-size: 1.75rem; color: #1E293B; margin-bottom: 0.5rem;'>📖 API Documentation</h1>
        <p style='color: #94A3B8; font-size: 0.95rem;'>Integration guides and API reference</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Start
    st.markdown("### 🚀 Quick Start")
    
    st.markdown("""
    TrustLayer AI integrates with your existing AI infrastructure via a simple API proxy pattern. 
    Replace your LLM API endpoint with TrustLayer AI, and we handle detection, scoring, and governance automatically.
    """)
    
    st.markdown("#### Basic Integration (Python)")
    
    st.code('''
from trustlayer import TrustLayerClient

# Initialize client
client = TrustLayerClient(
    api_key="your-api-key",
    llm_provider="openai",  # or "anthropic", "google", etc.
    industry_module="bfsi"   # optional: enables domain-specific detection
)

# Make AI request through TrustLayer
response = client.complete(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's the current mortgage rate?"}],
    confidence_threshold=70,  # minimum confidence to deliver
    enable_fallback=True      # route low-confidence to human
)

# Response includes reliability metadata
print(f"Content: {response.content}")
print(f"Confidence: {response.confidence_score}")
print(f"Action: {response.action}")  # DELIVERED, FLAGGED, or BLOCKED
print(f"Audit ID: {response.audit_id}")
''', language="python")
    
    st.markdown("#### API Gateway Integration (Zero Code Change)")
    
    st.code('''
# Instead of calling OpenAI directly:
# POST https://api.openai.com/v1/chat/completions

# Route through TrustLayer:
POST https://api.trustlayer.ai/v1/proxy/openai/chat/completions

Headers:
  Authorization: Bearer <your-trustlayer-key>
  X-TrustLayer-Confidence-Threshold: 70
  X-TrustLayer-Industry: bfsi

# Request body remains unchanged - full OpenAI API compatibility
''', language="bash")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # API Endpoints
    st.markdown("### 📡 API Endpoints")
    
    endpoints = [
        ("POST", "/v1/analyze", "Analyze an AI response for hallucinations"),
        ("POST", "/v1/proxy/{provider}/*", "Proxy requests through TrustLayer"),
        ("GET", "/v1/audit/{audit_id}", "Retrieve audit record"),
        ("GET", "/v1/metrics", "Get platform metrics"),
        ("POST", "/v1/configure", "Update detection policies"),
        ("GET", "/v1/compliance/report", "Generate compliance documentation"),
    ]
    
    for method, path, desc in endpoints:
        method_color = {"POST": "#FFA502", "GET": "#2ED573", "PUT": "#0066FF", "DELETE": "#FF4757"}
        st.markdown(f"""
        <div style='display: flex; align-items: center; gap: 1rem; padding: 0.5rem 0; 
                    border-bottom: 1px solid rgba(255,255,255,0.05);'>
            <span style='background: {method_color.get(method, "#64748B")}; color: #1E293B; 
                        padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; 
                        font-weight: 600; min-width: 50px; text-align: center;'>{method}</span>
            <code style='color: #00D4AA;'>{path}</code>
            <span style='color: #94A3B8; font-size: 0.85rem;'>{desc}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Response Schema
    st.markdown("### 📋 Response Schema")
    
    st.code('''
{
  "id": "resp_abc123",
  "content": "The response content...",
  "trustlayer": {
    "audit_id": "TL-A8F2C1D3E5B6",
    "confidence_score": 87,
    "risk_score": 23,
    "action": "DELIVERED",
    "issues": [
      {
        "type": "Unverified Claim",
        "severity": "low",
        "text": "approximately 5%",
        "explanation": "Numerical claim not verified against source"
      }
    ],
    "detection_methods": ["semantic_entropy", "enterprise_grounding"],
    "latency_ms": 47,
    "compliance_flags": [],
    "timestamp": "2025-01-30T14:32:15Z"
  },
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 200,
    "total_tokens": 350
  }
}
''', language="json")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # SDKs
    st.markdown("### 📦 SDKs & Libraries")
    
    col1, col2, col3, col4 = st.columns(4)
    
    sdks = [
        ("Python", "pip install trustlayer", "GA"),
        ("Node.js", "npm install @trustlayer/sdk", "GA"),
        ("Java", "maven: com.trustlayer:sdk", "GA"),
        ("Go", "go get trustlayer.ai/sdk", "Beta")
    ]
    
    for col, (lang, install, status) in zip([col1, col2, col3, col4], sdks):
        with col:
            status_color = "#2ED573" if status == "GA" else "#FFA502"
            st.markdown(f"""
            <div class='integration-item'>
                <div style='color: #1E293B; font-weight: 600;'>{lang}</div>
                <code style='font-size: 0.7rem;'>{install}</code>
                <div style='margin-top: 0.5rem;'>
                    <span style='background: {status_color}; color: #1E293B; padding: 0.1rem 0.4rem; 
                                border-radius: 4px; font-size: 0.65rem;'>{status}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 2rem; border-top: 1px solid #E2E8F0;'>
    <p style='color: #64748B; font-size: 0.85rem;'>
        🛡️ <strong style='color: #1E293B;'>TrustLayer AI</strong> - Enterprise AI Reliability Platform<br>
        <span style='font-size: 0.75rem;'>Production Demo v2.0 | Built for <strong style='color: #0066FF;'>Infosys Incubator</strong></span>
    </p>
    <p style='color: #64748B; font-size: 0.7rem; margin-top: 0.5rem;'>
        12 Industries | 8 LLM Providers | 50+ Enterprise Integrations | EU AI Act Ready
    </p>
</div>
""", unsafe_allow_html=True)
