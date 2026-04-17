"""
Smart DC Power Supply Monitoring System
Professional Streamlit Dashboard — Bilingual (EN / JP)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import io

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Smart DC Power Monitor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# TRANSLATIONS
# ──────────────────────────────────────────────
LANG = {
    "EN": {
        "title": "Smart DC Power Supply Monitoring System",
        "subtitle": "Real-time industrial-grade power analytics dashboard",
        "lang_btn": "🌐 日本語",
        "sidebar_title": "Navigation",
        "nav_overview": "Dashboard Overview",
        "nav_sensor": "Sensor Readings",
        "nav_graph": "Graph Analysis",
        "nav_alerts": "Alerts & Warnings",
        "nav_table": "Data Table",
        "nav_download": "Download CSV",
        "nav_sysinfo": "System Information",
        "nav_future": "Future Improvements",
        "voltage_label": "Voltage",
        "current_label": "Current",
        "temp_label": "Temperature",
        "power_label": "Power",
        "efficiency_label": "Efficiency",
        "voltage_unit": "V",
        "current_unit": "A",
        "temp_unit": "°C",
        "power_unit": "W",
        "efficiency_unit": "%",
        "latest": "Latest",
        "trend": "Trend",
        "metric_cards_header": "Live Sensor Metrics",
        "graph_header": "Interactive Time-Series Graphs",
        "volt_graph": "Voltage vs Time",
        "curr_graph": "Current vs Time",
        "temp_graph": "Temperature vs Time",
        "power_graph": "Power vs Time",
        "eff_graph": "Efficiency vs Time",
        "time_axis": "Time",
        "alerts_header": "System Alerts & Warnings",
        "alert_high_temp": "High Temperature Detected",
        "alert_high_temp_desc": "Temperature exceeded 75 °C threshold. Check cooling system.",
        "alert_low_volt": "Low Voltage Warning",
        "alert_low_volt_desc": "Voltage dropped below 11.5 V. Verify power source.",
        "alert_low_eff": "Efficiency Below Threshold",
        "alert_low_eff_desc": "Efficiency fell below 80%. Inspect load and connections.",
        "alert_normal": "All other parameters are within normal operating range.",
        "table_header": "Sensor Data Table",
        "search_placeholder": "Search / filter by value…",
        "sort_by": "Sort by column",
        "asc_desc": "Order",
        "ascending": "Ascending",
        "descending": "Descending",
        "download_btn": "Download CSV",
        "download_header": "Download Data",
        "download_desc": "Export the full sensor dataset as a CSV file.",
        "sysinfo_header": "System Information",
        "si_total": "Total Readings Collected",
        "si_avg_volt": "Average Voltage",
        "si_avg_curr": "Average Current",
        "si_avg_temp": "Average Temperature",
        "si_avg_eff": "Average Efficiency",
        "si_max_temp": "Highest Temperature Recorded",
        "si_min_volt": "Lowest Voltage Recorded",
        "future_header": "Future Improvements",
        "fi_iot": "IoT Integration",
        "fi_iot_desc": "Connect to real hardware sensors via MQTT / RS-485 protocol for live data ingestion.",
        "fi_cloud": "Cloud Storage",
        "fi_cloud_desc": "Push measurements to AWS / Azure / GCP for long-term retention and remote access.",
        "fi_sensors": "Real-time Hardware Sensors",
        "fi_sensors_desc": "Deploy INA226 / ACS712 chips for high-precision voltage, current, and power sensing.",
        "fi_email": "Email Alerts",
        "fi_email_desc": "Automated SMTP notifications when any parameter exceeds its safety threshold.",
        "fi_mobile": "Mobile App Integration",
        "fi_mobile_desc": "Cross-platform Flutter app with push notifications for on-the-go monitoring.",
        "fi_ml": "ML Prediction",
        "fi_ml_desc": "LSTM-based anomaly detection to forecast failures before they occur.",
        "overview_header": "Dashboard Overview",
        "overview_desc": (
            "This dashboard provides a comprehensive real-time view of the DC power supply "
            "parameters including voltage, current, temperature, power, and efficiency. "
            "Use the sidebar to navigate between sections."
        ),
        "recorded_at": "Recorded at",
        "col_time": "Timestamp",
        "col_volt": "Voltage (V)",
        "col_curr": "Current (A)",
        "col_temp": "Temperature (°C)",
        "col_pow": "Power (W)",
        "col_eff": "Efficiency (%)",
    },
    "JP": {
        "title": "スマートDC電源監視システム",
        "subtitle": "リアルタイム産業用電力分析ダッシュボード",
        "lang_btn": "🌐 English",
        "sidebar_title": "ナビゲーション",
        "nav_overview": "ダッシュボード概要",
        "nav_sensor": "センサー読み取り",
        "nav_graph": "グラフ分析",
        "nav_alerts": "アラートと警告",
        "nav_table": "データテーブル",
        "nav_download": "CSVダウンロード",
        "nav_sysinfo": "システム情報",
        "nav_future": "今後の改善点",
        "voltage_label": "電圧",
        "current_label": "電流",
        "temp_label": "温度",
        "power_label": "電力",
        "efficiency_label": "効率",
        "voltage_unit": "V",
        "current_unit": "A",
        "temp_unit": "°C",
        "power_unit": "W",
        "efficiency_unit": "%",
        "latest": "最新値",
        "trend": "トレンド",
        "metric_cards_header": "ライブセンサー指標",
        "graph_header": "インタラクティブ時系列グラフ",
        "volt_graph": "電圧 vs 時間",
        "curr_graph": "電流 vs 時間",
        "temp_graph": "温度 vs 時間",
        "power_graph": "電力 vs 時間",
        "eff_graph": "効率 vs 時間",
        "time_axis": "時間",
        "alerts_header": "システムアラートと警告",
        "alert_high_temp": "高温検出",
        "alert_high_temp_desc": "温度が75°Cのしきい値を超えました。冷却システムを確認してください。",
        "alert_low_volt": "低電圧警告",
        "alert_low_volt_desc": "電圧が11.5V未満に低下しました。電源を確認してください。",
        "alert_low_eff": "効率がしきい値以下",
        "alert_low_eff_desc": "効率が80%を下回りました。負荷と接続を検査してください。",
        "alert_normal": "他のすべてのパラメータは通常の動作範囲内です。",
        "table_header": "センサーデータテーブル",
        "search_placeholder": "値で検索/フィルター…",
        "sort_by": "列でソート",
        "asc_desc": "順序",
        "ascending": "昇順",
        "descending": "降順",
        "download_btn": "CSVダウンロード",
        "download_header": "データのダウンロード",
        "download_desc": "センサーデータセット全体をCSVファイルとしてエクスポートします。",
        "sysinfo_header": "システム情報",
        "si_total": "収集した総測定値",
        "si_avg_volt": "平均電圧",
        "si_avg_curr": "平均電流",
        "si_avg_temp": "平均温度",
        "si_avg_eff": "平均効率",
        "si_max_temp": "記録された最高温度",
        "si_min_volt": "記録された最低電圧",
        "future_header": "今後の改善点",
        "fi_iot": "IoT統合",
        "fi_iot_desc": "MQTT / RS-485プロトコルを介してリアルハードウェアセンサーに接続し、ライブデータを取り込みます。",
        "fi_cloud": "クラウドストレージ",
        "fi_cloud_desc": "AWS / Azure / GCPに測定値を送信し、長期保存とリモートアクセスを実現します。",
        "fi_sensors": "リアルタイムハードウェアセンサー",
        "fi_sensors_desc": "INA226 / ACS712チップを展開し、高精度な電圧・電流・電力の検知を行います。",
        "fi_email": "メールアラート",
        "fi_email_desc": "パラメータが安全しきい値を超えた際に自動SMTPメール通知を送信します。",
        "fi_mobile": "モバイルアプリ統合",
        "fi_mobile_desc": "プッシュ通知付きのクロスプラットフォームFlutterアプリで外出先でもモニタリング。",
        "fi_ml": "ML予測",
        "fi_ml_desc": "LSTMベースの異常検知で障害が発生する前に予測します。",
        "overview_header": "ダッシュボード概要",
        "overview_desc": (
            "このダッシュボードは、電圧、電流、温度、電力、効率を含むDC電源パラメータの"
            "包括的なリアルタイムビューを提供します。サイドバーを使用してセクション間を移動してください。"
        ),
        "recorded_at": "記録時刻",
        "col_time": "タイムスタンプ",
        "col_volt": "電圧 (V)",
        "col_curr": "電流 (A)",
        "col_temp": "温度 (°C)",
        "col_pow": "電力 (W)",
        "col_eff": "効率 (%)",
    },
}

# ──────────────────────────────────────────────
# SESSION STATE — language
# ──────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "EN"


def toggle_lang():
    st.session_state.lang = "JP" if st.session_state.lang == "EN" else "EN"


T = LANG[st.session_state.lang]

# ──────────────────────────────────────────────
# GLOBAL CSS
# ──────────────────────────────────────────────
st.markdown(
    """
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Root reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* ── Full-page dark background ── */
.stApp {
    background: #050d1a !important;
}

/* ── Hide default Streamlit chrome but KEEP sidebar toggle visible ── */
#MainMenu { visibility: hidden !important; }
footer    { visibility: hidden !important; }
/* Hide only the Streamlit branded toolbar/tagline, not the entire header */
[data-testid="stToolbar"]      { display: none !important; }
[data-testid="stDecoration"]   { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }
/* Keep the sidebar toggle button visible */
[data-testid="stHeader"] {
    background: transparent !important;
    height: auto !important;
}
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    background: #061428 !important;
    border-radius: 0 8px 8px 0 !important;
    border: 1px solid #0e2a4a !important;
    z-index: 999 !important;
}
[data-testid="collapsedControl"] svg,
[data-testid="stSidebarCollapsedControl"] svg {
    fill: #00e5ff !important;
    color: #00e5ff !important;
}
/* Force the sidebar panel to be visible and expanded */
[data-testid="stSidebar"][aria-expanded="false"] {
    display: block !important;
    width: 244px !important;
    transform: none !important;
    visibility: visible !important;
}

/* ── Sidebar background & always-visible ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #061428 0%, #0a1e34 100%) !important;
    border-right: 1px solid #0e2a4a !important;
    min-width: 240px !important;
    display: block !important;
    visibility: visible !important;
}
/* Show the sidebar collapse/expand chevron */
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    background: #061428 !important;
}
[data-testid="stSidebarCollapsedControl"] svg {
    color: #00e5ff !important;
    fill: #00e5ff !important;
}
/* Text colors inside sidebar — target specific elements, not wildcard */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown {
    color: #c8d8ea !important;
}

/* ── Sidebar nav buttons ── */
[data-testid="stSidebar"] button {
    width: 100% !important;
    text-align: left !important;
    justify-content: flex-start !important;
    border-radius: 10px !important;
    padding: 10px 16px !important;
    margin-bottom: 5px !important;
    font-size: 0.87rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.2px !important;
    transition: all 0.2s ease !important;
    background: rgba(14,42,74,0.5) !important;
    border: 1px solid rgba(14,62,110,0.6) !important;
    color: #a8c8e8 !important;
    box-shadow: none !important;
    display: flex !important;
    visibility: visible !important;
}
[data-testid="stSidebar"] button:hover {
    background: rgba(0,188,212,0.18) !important;
    border-color: rgba(0,188,212,0.4) !important;
    color: #00e5ff !important;
    transform: translateX(4px) !important;
    box-shadow: 2px 0 12px rgba(0,188,212,0.15) !important;
}
[data-testid="stSidebar"] button p {
    color: inherit !important;
    font-size: inherit !important;
    font-weight: inherit !important;
}


/* ── Header bar ── */
.header-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 22px 32px 18px;
    background: linear-gradient(135deg, #061428 0%, #0a1e34 60%, #071c36 100%);
    border-bottom: 1px solid #0e3060;
    border-radius: 0 0 18px 18px;
    margin-bottom: 28px;
    box-shadow: 0 4px 32px rgba(0,0,0,0.5);
}
.header-left { display: flex; align-items: center; gap: 18px; }
.header-icon {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, #00bcd4, #0288d1);
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 26px;
    box-shadow: 0 0 18px rgba(0,188,212,0.4);
}
.header-title { font-size: 1.65rem; font-weight: 800; color: #e8f4fd; letter-spacing: -0.5px; }
.header-subtitle { font-size: 0.82rem; color: #7eaed4; margin-top: 2px; font-weight: 400; }
.header-right { text-align: right; }
.header-datetime { font-size: 0.8rem; color: #7eaed4; }
.header-date { font-size: 1rem; font-weight: 600; color: #b0d4f0; }

/* ── Section headings ── */
.section-heading {
    font-size: 1.15rem; font-weight: 700; color: #00e5ff;
    text-transform: uppercase; letter-spacing: 1.2px;
    border-left: 4px solid #00bcd4;
    padding-left: 14px; margin: 28px 0 18px;
}

/* ── Metric card ── */
.metric-card {
    background: linear-gradient(135deg, #071931 0%, #0a2040 100%);
    border-radius: 16px;
    padding: 22px 20px 18px;
    border: 1px solid #0e3060;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    position: relative; overflow: hidden;
}
.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 34px rgba(0,0,0,0.55);
}
.metric-card::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 100%; height: 3px;
    border-radius: 16px 16px 0 0;
}
.mc-cyan::before  { background: linear-gradient(90deg,#00bcd4,#00e5ff); }
.mc-blue::before  { background: linear-gradient(90deg,#1565c0,#42a5f5); }
.mc-teal::before  { background: linear-gradient(90deg,#00695c,#26a69a); }
.mc-indigo::before{ background: linear-gradient(90deg,#283593,#5c6bc0); }
.mc-green::before { background: linear-gradient(90deg,#1b5e20,#66bb6a); }
.mc-icon {
    font-size: 1.6rem; margin-bottom: 10px;
    filter: drop-shadow(0 0 8px rgba(0,188,212,0.5));
}
.mc-label { font-size: 0.72rem; font-weight: 600; color: #7eaed4;
    text-transform: uppercase; letter-spacing: 1px; }
.mc-value { font-size: 2.1rem; font-weight: 800; color: #e8f4fd;
    line-height: 1.1; margin: 6px 0 4px; }
.mc-unit  { font-size: 0.85rem; color: #7eaed4; font-weight: 500; }
.mc-trend { font-size: 0.78rem; margin-top: 10px; padding: 4px 10px;
    border-radius: 20px; display: inline-block; font-weight: 600; }
.trend-up   { background: rgba(0,230,118,0.12); color: #00e676; }
.trend-down { background: rgba(255,82,82,0.12);  color: #ff5252; }
.trend-ok   { background: rgba(0,188,212,0.12);  color: #00e5ff; }

/* ── Alert cards ── */
.alert-card {
    border-radius: 14px; padding: 18px 20px;
    margin-bottom: 14px;
    border-left: 5px solid;
    box-shadow: 0 3px 14px rgba(0,0,0,0.35);
    transition: transform 0.15s;
}
.alert-card:hover { transform: translateX(4px); }
.alert-danger  { background: rgba(183,28,28,0.18); border-color: #ef5350; }
.alert-warning { background: rgba(245,127,23,0.15); border-color: #ffa726; }
.alert-info    { background: rgba(0,188,212,0.12);  border-color: #26c6da; }
.alert-ok      { background: rgba(27,94,32,0.18);   border-color: #66bb6a; }
.alert-title   { font-size: 0.95rem; font-weight: 700; color: #f5f5f5; margin-bottom: 4px; }
.alert-desc    { font-size: 0.82rem; color: #b0c8d8; }

/* ── Info grid (system info) ── */
.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px,1fr));
    gap: 16px; margin-top: 10px;
}
.info-card {
    background: #071931; border: 1px solid #0e3060;
    border-radius: 14px; padding: 18px 20px;
    transition: transform 0.15s, box-shadow 0.15s;
}
.info-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.info-card-label { font-size: 0.7rem; color: #7eaed4; text-transform: uppercase;
    letter-spacing: 0.8px; font-weight: 600; }
.info-card-value { font-size: 1.55rem; font-weight: 800; color: #00e5ff; margin-top: 6px; }
.info-card-sub   { font-size: 0.75rem; color: #5b8aa8; margin-top: 2px; }

/* ── Future improvement cards ── */
.fi-card {
    background: linear-gradient(135deg, #071931 0%, #0a2040 100%);
    border: 1px solid #0e3060;
    border-radius: 16px; padding: 22px 20px;
    transition: transform 0.18s, box-shadow 0.18s;
    height: 100%;
}
.fi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 36px rgba(0,188,212,0.18);
    border-color: #00bcd4;
}
.fi-icon { font-size: 1.8rem; margin-bottom: 12px; }
.fi-title { font-size: 0.95rem; font-weight: 700; color: #00e5ff; margin-bottom: 8px; }
.fi-desc  { font-size: 0.8rem; color: #7eaed4; line-height: 1.55; }

/* ── Data table styling ── */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden;
    border: 1px solid #0e3060;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #0288d1, #00bcd4) !important;
    color: white !important; border: none !important;
    border-radius: 10px !important; font-weight: 600 !important;
    padding: 9px 24px !important; transition: all 0.2s !important;
    box-shadow: 0 4px 14px rgba(0,188,212,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(0,188,212,0.45) !important;
}

/* ── Select / text input ── */
.stSelectbox > div, .stTextInput > div { border-radius: 10px !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# SYNTHETIC DATA  (200 readings over last 24 h)
# ──────────────────────────────────────────────
@st.cache_data
def generate_data():
    np.random.seed(42)
    n = 200
    base = datetime.now() - timedelta(hours=24)
    timestamps = [base + timedelta(minutes=i * 7.2) for i in range(n)]

    voltage = np.clip(
        12.0 + np.sin(np.linspace(0, 6 * np.pi, n)) * 0.8
        + np.random.normal(0, 0.15, n),
        10.8, 13.2,
    )
    current = np.clip(
        3.5 + np.cos(np.linspace(0, 4 * np.pi, n)) * 0.6
        + np.random.normal(0, 0.1, n),
        2.0, 5.5,
    )
    temperature = np.clip(
        45 + np.sin(np.linspace(0, 3 * np.pi, n)) * 20
        + np.random.normal(0, 1.5, n),
        30, 85,
    )
    power = voltage * current
    efficiency = np.clip(
        85 + np.sin(np.linspace(0, 5 * np.pi, n)) * 8
        + np.random.normal(0, 1, n),
        65, 98,
    )

    df = pd.DataFrame(
        {
            "Timestamp": timestamps,
            "Voltage (V)": np.round(voltage, 3),
            "Current (A)": np.round(current, 3),
            "Temperature (°C)": np.round(temperature, 2),
            "Power (W)": np.round(power, 3),
            "Efficiency (%)": np.round(efficiency, 2),
        }
    )
    return df


df = generate_data()
latest = df.iloc[-1]

# ──────────────────────────────────────────────
# HEADER  (language toggle top right)
# ──────────────────────────────────────────────
now = datetime.now()
hdr_col_left, hdr_col_right = st.columns([8, 2])
with hdr_col_left:
    st.markdown(
        f"""
    <div class="header-bar">
      <div class="header-left">
        <div class="header-icon">⚡</div>
        <div>
          <div class="header-title">{T['title']}</div>
          <div class="header-subtitle">{T['subtitle']}</div>
        </div>
      </div>
      <div class="header-right">
        <div class="header-date">{now.strftime('%A, %B %d, %Y')}</div>
        <div class="header-datetime">{now.strftime('%H:%M:%S')}  •  {T['recorded_at']}</div>
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
with hdr_col_right:
    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    st.button(T["lang_btn"], on_click=toggle_lang, key="lang_toggle")

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
# ── Sidebar nav state ──
if "section" not in st.session_state:
    st.session_state.section = T["nav_overview"]

# Build nav label list fresh every render (language may have changed)
NAV_LABELS = [
    ("⊞", T["nav_overview"]),
    ("◉", T["nav_sensor"]),
    ("◈", T["nav_graph"]),
    ("⚠", T["nav_alerts"]),
    ("☰", T["nav_table"]),
    ("↓", T["nav_download"]),
    ("ℹ", T["nav_sysinfo"]),
    ("★", T["nav_future"]),
]

# When language changed the labels change too — re-map active section by index
if "_last_lang" not in st.session_state:
    st.session_state._last_lang = st.session_state.lang
if st.session_state._last_lang != st.session_state.lang:
    # Find index of old active section in old lang labels, apply to new lang
    old_labels = [v for _, v in [
        ("⊞", LANG[st.session_state._last_lang]["nav_overview"]),
        ("◉", LANG[st.session_state._last_lang]["nav_sensor"]),
        ("◈", LANG[st.session_state._last_lang]["nav_graph"]),
        ("⚠", LANG[st.session_state._last_lang]["nav_alerts"]),
        ("☰", LANG[st.session_state._last_lang]["nav_table"]),
        ("↓", LANG[st.session_state._last_lang]["nav_download"]),
        ("ℹ", LANG[st.session_state._last_lang]["nav_sysinfo"]),
        ("★", LANG[st.session_state._last_lang]["nav_future"]),
    ]]
    curr_idx = old_labels.index(st.session_state.section) if st.session_state.section in old_labels else 0
    st.session_state.section = NAV_LABELS[curr_idx][1]
    st.session_state._last_lang = st.session_state.lang

with st.sidebar:
    st.markdown(
        f"""<div style='font-size:1.05rem;font-weight:800;color:#00e5ff;
        letter-spacing:0.6px;padding:8px 4px 16px;border-bottom:1px solid #0e2a4a;
        margin-bottom:14px;'>◈ {T['sidebar_title']}</div>""",
        unsafe_allow_html=True,
    )

    for icon, label in NAV_LABELS:
        is_active = (st.session_state.section == label)
        # Highlight the active item with a distinct style injected via CSS
        active_css = ""
        if is_active:
            escaped = label.replace("'", "\\'")
            active_css = f"""
            <style>
            [data-testid="stSidebar"] button[kind="secondary"]:nth-of-type({NAV_LABELS.index((icon,label))+1}),
            [data-testid="stSidebar"] div[data-testid="stButton"]:nth-of-type({NAV_LABELS.index((icon,label))+1}) > button {{
                background: linear-gradient(135deg,rgba(0,188,212,0.3),rgba(2,136,209,0.25)) !important;
                border: 1px solid #00bcd4 !important;
                color: #00e5ff !important;
                font-weight: 700 !important;
            }}
            </style>"""
            st.markdown(active_css, unsafe_allow_html=True)
        if st.button(
            f"{icon}  {label}",
            key=f"nav_{label}",
            use_container_width=True,
        ):
            st.session_state.section = label
            st.rerun()

    st.markdown(
        "<hr style='border-color:#0e2a4a;margin:16px 0 10px'/>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='font-size:0.7rem;color:#3d6080;text-align:center;'>"
        "Smart DC Power Monitor v1.0<br>© 2025 EktedarWorks</div>",
        unsafe_allow_html=True,
    )

section = st.session_state.section

# ──────────────────────────────────────────────
# HELPER — Plotly dark chart theme
# ──────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="#071931",
    plot_bgcolor="#071931",
    font=dict(family="Inter", color="#b0c8d8"),
    margin=dict(l=50, r=24, t=48, b=48),
    xaxis=dict(
        gridcolor="#0e2a4a", showgrid=True, zeroline=False,
        color="#7eaed4", title_font=dict(size=11),
    ),
    yaxis=dict(
        gridcolor="#0e2a4a", showgrid=True, zeroline=False,
        color="#7eaed4", title_font=dict(size=11),
    ),
    hovermode="x unified",
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,0,0,0)"),
)

LINE_COLORS = {
    "voltage":     "#00e5ff",
    "current":     "#42a5f5",
    "temperature": "#ff7043",
    "power":       "#ab47bc",
    "efficiency":  "#66bb6a",
}

# rgba fill versions (opacity 0.08) — Plotly only accepts rgba(), not 8-digit hex
LINE_FILL = {
    "#00e5ff": "rgba(0,229,255,0.08)",
    "#42a5f5": "rgba(66,165,245,0.08)",
    "#ff7043": "rgba(255,112,67,0.08)",
    "#ab47bc": "rgba(171,71,188,0.08)",
    "#66bb6a": "rgba(102,187,106,0.08)",
}


def make_line_chart(x, y, title, y_label, color, unit=""):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x, y=y, mode="lines", name=y_label,
            line=dict(color=color, width=2.5, shape="spline"),
            fill="tozeroy",
            fillcolor=LINE_FILL.get(color, "rgba(0,229,255,0.08)"),
            hovertemplate=f"<b>{y_label}</b>: %{{y:.2f}} {unit}<extra></extra>",
        )
    )
    fig.update_layout(
        title=dict(text=title, font=dict(size=14, color="#c8d8ea"), x=0.01),
        xaxis_title=T["time_axis"],
        yaxis_title=y_label,
        **PLOTLY_LAYOUT,
    )
    return fig


# ══════════════════════════════════════════════
# SECTION: DASHBOARD OVERVIEW
# ══════════════════════════════════════════════
if section == T["nav_overview"]:
    st.markdown(
        f"<div class='section-heading'>{T['overview_header']}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color:#7eaed4;font-size:0.9rem;line-height:1.75;max-width:780px;'>"
        f"{T['overview_desc']}</p>",
        unsafe_allow_html=True,
    )

    # Quick stats bar
    st.markdown(
        f"<div class='section-heading'>{T['metric_cards_header']}</div>",
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4, c5 = st.columns(5)
    cards = [
        (
            c1, "mc-cyan", "⚡", T["voltage_label"],
            f"{latest['Voltage (V)']:.2f}", T["voltage_unit"],
            "trend-up", "▲ +0.04 V",
        ),
        (
            c2, "mc-blue", "〜", T["current_label"],
            f"{latest['Current (A)']:.2f}", T["current_unit"],
            "trend-down", "▼ −0.02 A",
        ),
        (
            c3, "mc-teal", "🌡", T["temp_label"],
            f"{latest['Temperature (°C)']:.1f}", T["temp_unit"],
            "trend-up" if latest["Temperature (°C)"] > 60 else "trend-ok",
            "▲ +1.2 °C" if latest["Temperature (°C)"] > 60 else "● Stable",
        ),
        (
            c4, "mc-indigo", "◈", T["power_label"],
            f"{latest['Power (W)']:.2f}", T["power_unit"],
            "trend-up", "▲ +0.15 W",
        ),
        (
            c5, "mc-green", "◎", T["efficiency_label"],
            f"{latest['Efficiency (%)']:.1f}", T["efficiency_unit"],
            "trend-ok", "● Optimal",
        ),
    ]
    for col, mc_class, icon, label, value, unit, trend_class, trend_text in cards:
        with col:
            st.markdown(
                f"""
            <div class="metric-card {mc_class}">
              <div class="mc-icon">{icon}</div>
              <div class="mc-label">{label}</div>
              <div class="mc-value">{value}</div>
              <div class="mc-unit">{unit}</div>
              <div class="mc-trend {trend_class}">{trend_text}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # Mini preview charts
    st.markdown(
        f"<div class='section-heading'>{T['graph_header']}</div>",
        unsafe_allow_html=True,
    )
    row1_c1, row1_c2 = st.columns(2)
    with row1_c1:
        st.plotly_chart(
            make_line_chart(
                df["Timestamp"], df["Voltage (V)"],
                T["volt_graph"], T["voltage_label"],
                LINE_COLORS["voltage"], T["voltage_unit"],
            ),
            use_container_width=True,
        )
    with row1_c2:
        st.plotly_chart(
            make_line_chart(
                df["Timestamp"], df["Current (A)"],
                T["curr_graph"], T["current_label"],
                LINE_COLORS["current"], T["current_unit"],
            ),
            use_container_width=True,
        )
    row2_c1, row2_c2, row2_c3 = st.columns(3)
    with row2_c1:
        st.plotly_chart(
            make_line_chart(
                df["Timestamp"], df["Temperature (°C)"],
                T["temp_graph"], T["temp_label"],
                LINE_COLORS["temperature"], T["temp_unit"],
            ),
            use_container_width=True,
        )
    with row2_c2:
        st.plotly_chart(
            make_line_chart(
                df["Timestamp"], df["Power (W)"],
                T["power_graph"], T["power_label"],
                LINE_COLORS["power"], T["power_unit"],
            ),
            use_container_width=True,
        )
    with row2_c3:
        st.plotly_chart(
            make_line_chart(
                df["Timestamp"], df["Efficiency (%)"],
                T["eff_graph"], T["efficiency_label"],
                LINE_COLORS["efficiency"], T["efficiency_unit"],
            ),
            use_container_width=True,
        )


# ══════════════════════════════════════════════
# SECTION: SENSOR READINGS  (metric cards full)
# ══════════════════════════════════════════════
elif section == T["nav_sensor"]:
    st.markdown(
        f"<div class='section-heading'>{T['metric_cards_header']}</div>",
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    c4, c5, _ = st.columns(3)
    for col, mc_class, icon, label, value, unit, trend_class, trend_text in [
        (
            c1, "mc-cyan", "⚡", T["voltage_label"],
            f"{latest['Voltage (V)']:.3f}", T["voltage_unit"],
            "trend-up", "▲ +0.04 V",
        ),
        (
            c2, "mc-blue", "〜", T["current_label"],
            f"{latest['Current (A)']:.3f}", T["current_unit"],
            "trend-down", "▼ −0.02 A",
        ),
        (
            c3, "mc-teal", "🌡", T["temp_label"],
            f"{latest['Temperature (°C)']:.2f}", T["temp_unit"],
            "trend-up" if latest["Temperature (°C)"] > 60 else "trend-ok",
            "▲ +1.2 °C" if latest["Temperature (°C)"] > 60 else "● Stable",
        ),
        (
            c4, "mc-indigo", "◈", T["power_label"],
            f"{latest['Power (W)']:.3f}", T["power_unit"],
            "trend-up", "▲ +0.15 W",
        ),
        (
            c5, "mc-green", "◎", T["efficiency_label"],
            f"{latest['Efficiency (%)']:.2f}", T["efficiency_unit"],
            "trend-ok", "● Optimal",
        ),
    ]:
        with col:
            st.markdown(
                f"""
            <div class="metric-card {mc_class}">
              <div class="mc-icon">{icon}</div>
              <div class="mc-label">{label} — {T['latest']}</div>
              <div class="mc-value">{value}</div>
              <div class="mc-unit">{unit}</div>
              <div class="mc-trend {trend_class}">{trend_text}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # small stats
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='section-heading'>Statistical Summary</div>",
        unsafe_allow_html=True,
    )
    num_cols = ["Voltage (V)", "Current (A)", "Temperature (°C)", "Power (W)", "Efficiency (%)"]
    stat_df = df[num_cols].describe().round(3).T[["mean", "std", "min", "max"]]
    stat_df.columns = ["Mean", "Std Dev", "Min", "Max"]
    st.dataframe(
        stat_df.style.background_gradient(cmap="Blues"),
        use_container_width=True,
    )


# ══════════════════════════════════════════════
# SECTION: GRAPH ANALYSIS
# ══════════════════════════════════════════════
elif section == T["nav_graph"]:
    st.markdown(
        f"<div class='section-heading'>{T['graph_header']}</div>",
        unsafe_allow_html=True,
    )

    def full_chart(df_col, title, label, color, unit):
        st.plotly_chart(
            make_line_chart(df["Timestamp"], df[df_col], title, label, color, unit),
            use_container_width=True,
        )

    full_chart("Voltage (V)",     T["volt_graph"],  T["voltage_label"],     LINE_COLORS["voltage"],     T["voltage_unit"])
    full_chart("Current (A)",     T["curr_graph"],  T["current_label"],     LINE_COLORS["current"],     T["current_unit"])
    full_chart("Temperature (°C)",T["temp_graph"],  T["temp_label"],        LINE_COLORS["temperature"], T["temp_unit"])
    full_chart("Power (W)",       T["power_graph"], T["power_label"],       LINE_COLORS["power"],       T["power_unit"])
    full_chart("Efficiency (%)",  T["eff_graph"],   T["efficiency_label"],  LINE_COLORS["efficiency"],  T["efficiency_unit"])

    # Correlation heatmap
    st.markdown(
        "<div class='section-heading'>Correlation Matrix</div>",
        unsafe_allow_html=True,
    )
    num_cols = ["Voltage (V)", "Current (A)", "Temperature (°C)", "Power (W)", "Efficiency (%)"]
    corr = df[num_cols].corr()
    fig_corr = go.Figure(
        go.Heatmap(
            z=corr.values, x=corr.columns, y=corr.index,
            colorscale="Blues", zmin=-1, zmax=1,
            text=[[f"{v:.2f}" for v in row] for row in corr.values],
            texttemplate="%{text}",
            hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>r = %{z:.2f}<extra></extra>",
        )
    )
    fig_corr.update_layout(
        title=dict(text="Pearson Correlation Heatmap", font=dict(size=14, color="#c8d8ea"), x=0.01),
        **PLOTLY_LAYOUT,
    )
    st.plotly_chart(fig_corr, use_container_width=True)


# ══════════════════════════════════════════════
# SECTION: ALERTS & WARNINGS
# ══════════════════════════════════════════════
elif section == T["nav_alerts"]:
    st.markdown(
        f"<div class='section-heading'>{T['alerts_header']}</div>",
        unsafe_allow_html=True,
    )

    high_temp_flag = df["Temperature (°C)"].max() > 75
    low_volt_flag  = df["Voltage (V)"].min() < 11.5
    low_eff_flag   = df["Efficiency (%)"].min() < 80

    if high_temp_flag:
        st.markdown(
            f"""<div class="alert-card alert-danger">
              <div class="alert-title">🔴 {T['alert_high_temp']}</div>
              <div class="alert-desc">{T['alert_high_temp_desc']}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    if low_volt_flag:
        st.markdown(
            f"""<div class="alert-card alert-warning">
              <div class="alert-title">🟡 {T['alert_low_volt']}</div>
              <div class="alert-desc">{T['alert_low_volt_desc']}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    if low_eff_flag:
        st.markdown(
            f"""<div class="alert-card alert-info">
              <div class="alert-title">🔵 {T['alert_low_eff']}</div>
              <div class="alert-desc">{T['alert_low_eff_desc']}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    if not (high_temp_flag or low_volt_flag or low_eff_flag):
        st.markdown(
            f"""<div class="alert-card alert-ok">
              <div class="alert-title">✅ All Systems Normal</div>
              <div class="alert-desc">{T['alert_normal']}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    # Always display an "all-ok" banner if none triggered simultaneously
    if high_temp_flag or low_volt_flag or low_eff_flag:
        st.markdown(
            f"""<div class="alert-card alert-ok" style="margin-top:10px;">
              <div class="alert-title">✅ Other Parameters</div>
              <div class="alert-desc">{T['alert_normal']}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    # Alert distribution mini chart
    alert_counts = {
        T["alert_high_temp_desc"].split(".")[0]: int(high_temp_flag),
        T["alert_low_volt_desc"].split(".")[0]:  int(low_volt_flag),
        T["alert_low_eff_desc"].split(".")[0]:   int(low_eff_flag),
        "Normal": int(not any([high_temp_flag, low_volt_flag, low_eff_flag])),
    }
    fig_alert = go.Figure(
        go.Bar(
            x=list(alert_counts.keys()),
            y=list(alert_counts.values()),
            marker_color=["#ef5350", "#ffa726", "#26c6da", "#66bb6a"],
            text=list(alert_counts.values()),
            textposition="outside",
        )
    )
    fig_alert.update_layout(
        title=dict(text="Alert Status", font=dict(size=14, color="#c8d8ea"), x=0.01),
        **PLOTLY_LAYOUT,
    )
    fig_alert.update_yaxes(range=[0, 1.5])
    st.plotly_chart(fig_alert, use_container_width=True)



# ══════════════════════════════════════════════
# SECTION: DATA TABLE
# ══════════════════════════════════════════════
elif section == T["nav_table"]:
    st.markdown(
        f"<div class='section-heading'>{T['table_header']}</div>",
        unsafe_allow_html=True,
    )
    tc1, tc2, tc3 = st.columns([3, 2, 2])
    with tc1:
        search = st.text_input("", placeholder=T["search_placeholder"], key="tbl_search")
    with tc2:
        sort_col = st.selectbox(
            T["sort_by"],
            ["Timestamp", "Voltage (V)", "Current (A)", "Temperature (°C)", "Power (W)", "Efficiency (%)"],
            key="sort_col",
        )
    with tc3:
        order = st.selectbox(T["asc_desc"], [T["ascending"], T["descending"]], key="sort_order")

    filtered = df.copy()
    if search:
        mask = filtered.apply(lambda row: search.lower() in str(row).lower(), axis=1)
        filtered = filtered[mask]

    ascending = order == T["ascending"]
    filtered = filtered.sort_values(sort_col, ascending=ascending)

    # rename cols per language
    col_rename = {
        "Timestamp": T["col_time"],
        "Voltage (V)": T["col_volt"],
        "Current (A)": T["col_curr"],
        "Temperature (°C)": T["col_temp"],
        "Power (W)": T["col_pow"],
        "Efficiency (%)": T["col_eff"],
    }
    st.dataframe(
        filtered.rename(columns=col_rename),
        use_container_width=True,
        height=500,
    )
    st.caption(f"{len(filtered):,} / {len(df):,} rows")


# ══════════════════════════════════════════════
# SECTION: DOWNLOAD CSV
# ══════════════════════════════════════════════
elif section == T["nav_download"]:
    st.markdown(
        f"<div class='section-heading'>{T['download_header']}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color:#7eaed4;font-size:0.9rem;'>{T['download_desc']}</p>",
        unsafe_allow_html=True,
    )
    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    st.download_button(
        label=T["download_btn"],
        data=csv_buf.getvalue(),
        file_name="smart_dc_power_monitor_data.csv",
        mime="text/csv",
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-heading'>Preview (first 10 rows)</div>",
        unsafe_allow_html=True,
    )
    st.dataframe(df.head(10), use_container_width=True)


# ══════════════════════════════════════════════
# SECTION: SYSTEM INFORMATION
# ══════════════════════════════════════════════
elif section == T["nav_sysinfo"]:
    st.markdown(
        f"<div class='section-heading'>{T['sysinfo_header']}</div>",
        unsafe_allow_html=True,
    )
    stats = {
        T["si_total"]:    (f"{len(df):,}", "readings"),
        T["si_avg_volt"]: (f"{df['Voltage (V)'].mean():.3f}", "V"),
        T["si_avg_curr"]: (f"{df['Current (A)'].mean():.3f}", "A"),
        T["si_avg_temp"]: (f"{df['Temperature (°C)'].mean():.2f}", "°C"),
        T["si_avg_eff"]:  (f"{df['Efficiency (%)'].mean():.2f}", "%"),
        T["si_max_temp"]: (f"{df['Temperature (°C)'].max():.2f}", "°C"),
        T["si_min_volt"]: (f"{df['Voltage (V)'].min():.3f}", "V"),
    }
    st.markdown("<div class='info-grid'>", unsafe_allow_html=True)
    for label, (value, sub) in stats.items():
        st.markdown(
            f"""<div class="info-card">
              <div class="info-card-label">{label}</div>
              <div class="info-card-value">{value}</div>
              <div class="info-card-sub">{sub}</div>
            </div>""",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # Time-range info
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
    <div style='background:#071931;border:1px solid #0e3060;border-radius:14px;padding:18px 24px;'>
      <div style='color:#7eaed4;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.8px;'>Data Range</div>
      <div style='color:#00e5ff;font-size:1rem;font-weight:700;margin-top:6px;'>
        {df['Timestamp'].min().strftime('%Y-%m-%d %H:%M')}  →  {df['Timestamp'].max().strftime('%Y-%m-%d %H:%M')}
      </div>
      <div style='color:#3d6080;font-size:0.78rem;margin-top:4px;'>24-hour monitoring window · 200 samples · 7.2 min interval</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════
# SECTION: FUTURE IMPROVEMENTS
# ══════════════════════════════════════════════
elif section == T["nav_future"]:
    st.markdown(
        f"<div class='section-heading'>{T['future_header']}</div>",
        unsafe_allow_html=True,
    )
    improvements = [
        ("📡", T["fi_iot"],     T["fi_iot_desc"]),
        ("☁️", T["fi_cloud"],   T["fi_cloud_desc"]),
        ("🔌", T["fi_sensors"], T["fi_sensors_desc"]),
        ("📧", T["fi_email"],   T["fi_email_desc"]),
        ("📱", T["fi_mobile"],  T["fi_mobile_desc"]),
        ("🤖", T["fi_ml"],      T["fi_ml_desc"]),
    ]
    row1 = st.columns(3)
    row2 = st.columns(3)
    for i, (icon, title, desc) in enumerate(improvements):
        col = row1[i] if i < 3 else row2[i - 3]
        with col:
            st.markdown(
                f"""<div class="fi-card">
                  <div class="fi-icon">{icon}</div>
                  <div class="fi-title">{title}</div>
                  <div class="fi-desc">{desc}</div>
                </div>""",
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
