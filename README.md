<div align="center">

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.31%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-5.18%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-00BCD4?style=for-the-badge"/>

<br/><br/>

# ⚡ Smart DC Power Supply Monitoring System

### *Industrial-Grade Real-Time Power Analytics Dashboard*

**[ English ]** &nbsp;|&nbsp; **[ 日本語 ]**

---

*A professional, bilingual Streamlit dashboard for monitoring DC power supply parameters — Voltage, Current, Temperature, Power, and Efficiency — in real time, with interactive charts, smart alerting, and CSV export.*

</div>

### 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [Dashboard Sections](#-dashboard-sections)
4. [Tech Stack](#-tech-stack)
5. [Project Structure](#-project-structure)
6. [Installation & Setup](#-installation--setup)
7. [Running the Dashboard](#-running-the-dashboard)
8. [Screenshots](#-screenshots)
9. [Future Improvements](#-future-improvements)
10. [Author](#-author)
11. [License](#-license)

---

### 🔍 Project Overview

The **Smart DC Power Supply Monitoring System** is a professional industrial-grade analytics dashboard built with Python and Streamlit. It provides real-time visualization and analysis of DC power supply parameters including **Voltage (V)**, **Current (A)**, **Temperature (°C)**, **Power (W)**, and **Efficiency (%)**.

The system is designed to simulate a real-world embedded hardware monitoring setup — making it suitable for internship portfolios, GitHub showcases, and academic project presentations. The dashboard is fully **bilingual (English / Japanese)**, allowing seamless language switching via a single toggle button.

This project demonstrates end-to-end software engineering competence: data generation, interactive data visualization, alert logic, data export, and a premium UI/UX design — all in a single, well-structured codebase.

---

### ✨ Key Features

| Feature | Description |
|---|---|
| 🌐 **Bilingual UI** | Full English ↔ Japanese toggle for all labels, graphs, alerts, and navigation |
| 🎨 **Premium Dark Theme** | Navy, cyan, teal, and blue palette with glassmorphism-style cards |
| 📊 **5 Interactive Charts** | Voltage, Current, Temperature, Power, and Efficiency vs Time (Plotly) |
| 🃏 **Live Metric Cards** | Color-coded sensor cards with latest reading and trend indicators |
| ⚠️ **Smart Alerts** | Real-time warning cards for high temperature, low voltage, low efficiency |
| 📋 **Data Table** | Searchable, sortable, filterable table with bilingual column headers |
| 💾 **CSV Export** | One-click download of all sensor data as a CSV file |
| 📈 **Correlation Heatmap** | Pearson correlation matrix for all sensor parameters |
| 🖥️ **System Info Panel** | Aggregated statistics: averages, extremes, and data range |
| 🔮 **Future Improvements** | Roadmap cards for IoT, cloud, ML, mobile, and email integrations |

---

### 🗂️ Dashboard Sections

The sidebar provides navigation across **8 dedicated sections**:

```
⊞  Dashboard Overview    — Overview, metric cards & all charts
◉  Sensor Readings       — Detailed metrics + statistical summary
◈  Graph Analysis        — Full-screen charts + correlation heatmap
⚠  Alerts & Warnings     — Conditional alert cards + alert bar chart
☰  Data Table            — Searchable & sortable sensor data table
↓  Download CSV          — Export full dataset as CSV
ℹ  System Information    — Aggregated stats and data range info
★  Future Improvements   — Planned enhancements and integration roadmap
```

---

### 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **Frontend Framework** | Streamlit 1.31+ |
| **Data Visualization** | Plotly 5.18+ |
| **Data Processing** | Pandas 2.0+, NumPy 1.24+ |
| **Styling** | Custom CSS (CSS Variables, Flexbox, Grid, Animations) |
| **Typography** | Google Fonts — Inter |
| **Data** | Synthetic sensor simulation (200 readings over 24 hours) |

---

### 📁 Project Structure

```
smart-dc-power-monitor/
│
├── dashboard.py              # Main Streamlit dashboard application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
│
└── smart-dc-power-monitor/   # Supporting project files
    ├── arduino/              # Arduino firmware for hardware integration
    │   └── power_monitor/
    │       └── power_monitor.ino
    ├── python/               # Python utilities and helper scripts
    ├── data/                 # Sample or collected data files
    ├── graphs/               # Exported graph images
    ├── images/               # Project screenshots and assets
    ├── demo/                 # Demo files
    ├── docs/                 # Project documentation and flow diagrams
    ├── reports/              # Generated reports
    ├── config.py             # Configuration constants
    ├── main.py               # Entry point for non-dashboard mode
    └── requirements.txt      # Inner dependencies
```

---

### 📦 Installation & Setup

#### Prerequisites

- Python **3.9** or higher
- `pip3` package manager
- A modern web browser (Chrome / Firefox / Safari)

#### Step 1 — Clone the Repository

```bash
git clone https://github.com/Harsh-PAHADIA/smart-dc-power-monitor.git
cd smart-dc-power-monitor
```

#### Step 2 — Install Dependencies

```bash
pip3 install -r requirements.txt
```

Or install manually:

```bash
pip3 install streamlit pandas numpy plotly
```

#### Step 3 — Run the Dashboard

```bash
[python3 -m streamlit run dashboard.py](https://smart-dc-power-monitor-hp-iitianj.streamlit.app/)
```

The dashboard will open automatically at:

```
Local URL:   http://localhost:8510
```

---

### ▶️ Running the Dashboard

```bash
# Standard run
python3 -m streamlit run dashboard.py

# Custom port
python3 -m streamlit run dashboard.py --server.port 8510

# Headless (server deployment)
python3 -m streamlit run dashboard.py --server.headless true
```

---

### 📸 Screenshots

> Dashboard running at `http://localhost:8510`

| View | Description |
|---|---|
| **Dashboard Overview** | Header, 5 metric cards, and all 5 interactive time-series charts |
| **Graph Analysis** | Full-width Plotly charts with correlation heatmap |
| **Alerts & Warnings** | Red/Yellow/Blue/Green conditional alert cards |
| **System Information** | Aggregated stats in a responsive grid layout |
| **Future Improvements** | 6 roadmap cards with hover effects |
| **Japanese Mode** | Full Japanese translation applied across all UI elements |

---

### 🔮 Future Improvements

| Improvement | Description |
|---|---|
| 📡 **IoT Integration** | Connect to real hardware sensors via MQTT / RS-485 protocol |
| ☁️ **Cloud Storage** | Push measurements to AWS / Azure / GCP for remote access |
| 🔌 **Hardware Sensors** | Deploy INA226 / ACS712 chips for high-precision measurements |
| 📧 **Email Alerts** | Automated SMTP notifications when thresholds are exceeded |
| 📱 **Mobile App** | Cross-platform Flutter app with push notifications |
| 🤖 **ML Prediction** | LSTM-based anomaly detection to predict failures proactively |

---

### 👩‍💻 Author

<div align="center">

**Harshita Pahadia**

*Data Science & AI Enthusiast | Python Developer | Dashboard Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-HarshitaPahadia-181717?style=flat-square&logo=github)](https://github.com/Harsh-PAHADIA)

---

*Built with precision, designed for industry.*

</div>

---

### 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

```
MIT License © 2025 Harshita Pahadia
```

---
---

## 🇯🇵 日本語

---

### 📋 目次

1. [プロジェクト概要](#-プロジェクト概要)
2. [主な機能](#-主な機能)
3. [ダッシュボードセクション](#-ダッシュボードセクション)
4. [技術スタック](#-技術スタック)
5. [プロジェクト構成](#-プロジェクト構成)
6. [インストールとセットアップ](#-インストールとセットアップ)
7. [ダッシュボードの起動](#-ダッシュボードの起動)
8. [スクリーンショット](#-スクリーンショット)
9. [今後の改善点](#-今後の改善点)
10. [作者](#-作者)
11. [ライセンス](#-ライセンス)

---

### 🔍 プロジェクト概要

**スマートDC電源監視システム**は、PythonとStreamlitで構築されたプロフェッショナル産業用分析ダッシュボードです。DC電源パラメータ（**電圧 (V)**、**電流 (A)**、**温度 (°C)**、**電力 (W)**、**効率 (%)**）のリアルタイム可視化と分析を提供します。

本システムは実際の組み込みハードウェア監視環境をシミュレートするよう設計されており、インターンシップのポートフォリオ、GitHubのショーケース、学術プロジェクトの発表に適しています。ダッシュボードは完全に**バイリンガル（英語/日本語）**対応しており、トグルボタン一つでシームレスに言語を切り替えることができます。

本プロジェクトは、データ生成・インタラクティブデータ可視化・アラートロジック・データエクスポート・プレミアムUI/UXデザインをすべて一つの整理されたコードベースに収め、エンドツーエンドのソフトウェアエンジニアリング能力を実証しています。

---

### ✨ 主な機能

| 機能 | 説明 |
|---|---|
| 🌐 **バイリンガルUI** | ラベル・グラフ・アラート・ナビゲーション全体の英語 ↔ 日本語切替 |
| 🎨 **プレミアムダークテーマ** | ネイビー・シアン・ティール・ブルーのカラーパレット |
| 📊 **5つのインタラクティブグラフ** | 電圧・電流・温度・電力・効率の時系列グラフ（Plotly） |
| 🃏 **ライブメトリクスカード** | 最新値とトレンド指標を持つカラーコード化センサーカード |
| ⚠️ **スマートアラート** | 高温・低電圧・低効率に対するリアルタイム警告カード |
| 📋 **データテーブル** | バイリンガル列ヘッダー付きの検索・ソート・フィルター可能なテーブル |
| 💾 **CSVエクスポート** | ワンクリックでセンサーデータ全体をCSVとしてダウンロード |
| 📈 **相関ヒートマップ** | 全センサーパラメータのピアソン相関行列 |
| 🖥️ **システム情報パネル** | 平均値・極値・データ範囲などの集計統計 |
| 🔮 **今後の改善点** | IoT・クラウド・機械学習・モバイル・メールの統合ロードマップ |

---

### 🗂️ ダッシュボードセクション

サイドバーから **8つの専用セクション** にアクセスできます：

```
⊞  ダッシュボード概要   — 概要、メトリクスカード、全グラフ
◉  センサー読み取り      — 詳細指標と統計サマリー
◈  グラフ分析           — フルスクリーンチャートと相関ヒートマップ
⚠  アラートと警告        — 条件付きアラートカードとバーチャート
☰  データテーブル        — 検索・ソート可能なセンサーデータテーブル
↓  CSVダウンロード       — データセット全体をCSVとしてエクスポート
ℹ  システム情報          — 集計統計とデータ範囲情報
★  今後の改善点          — 計画中の機能強化と統合ロードマップ
```

---

### 🛠️ 技術スタック

| レイヤー | 技術 |
|---|---|
| **言語** | Python 3.9以上 |
| **フロントエンドフレームワーク** | Streamlit 1.31以上 |
| **データ可視化** | Plotly 5.18以上 |
| **データ処理** | Pandas 2.0以上、NumPy 1.24以上 |
| **スタイリング** | カスタムCSS（CSS変数・Flexbox・Grid・アニメーション） |
| **タイポグラフィ** | Google Fonts — Inter |
| **データ** | 合成センサーシミュレーション（24時間で200サンプル） |

---

### 📁 プロジェクト構成

```
smart-dc-power-monitor/
│
├── dashboard.py              # Streamlitダッシュボードメインアプリケーション
├── requirements.txt          # Python依存関係
├── README.md                 # プロジェクトドキュメント（本ファイル）
│
└── smart-dc-power-monitor/   # サポートプロジェクトファイル
    ├── arduino/              # ハードウェア統合用Arduinoファームウェア
    │   └── power_monitor/
    │       └── power_monitor.ino
    ├── python/               # Pythonユーティリティとヘルパースクリプト
    ├── data/                 # サンプルまたは収集データファイル
    ├── graphs/               # エクスポートされたグラフ画像
    ├── images/               # プロジェクトスクリーンショットとアセット
    ├── demo/                 # デモファイル
    ├── docs/                 # プロジェクトドキュメントとフロー図
    ├── reports/              # 生成されたレポート
    ├── config.py             # 設定定数
    ├── main.py               # ダッシュボード外モードのエントリーポイント
    └── requirements.txt      # 内部依存関係
```

---

### 📦 インストールとセットアップ

#### 前提条件

- Python **3.9** 以上
- `pip3` パッケージマネージャー
- 最新のWebブラウザ（Chrome / Firefox / Safari）

#### ステップ1 — リポジトリのクローン

```bash
git clone https://github.com/Harsh-PAHADIA/smart-dc-power-monitor.git
cd smart-dc-power-monitor
```

#### ステップ2 — 依存関係のインストール

```bash
pip3 install -r requirements.txt
```

または手動でインストール：

```bash
pip3 install streamlit pandas numpy plotly
```

#### ステップ3 — ダッシュボードの起動

```bash
python3 -m streamlit run dashboard.py
```

ダッシュボードは以下のURLで自動的に開きます：

```
ローカルURL:  http://localhost:8501
```

---

### ▶️ ダッシュボードの起動

```bash
# 標準起動
python3 -m streamlit run dashboard.py

# カスタムポート
[python3 -m streamlit run dashboard.py --server.port 8510](https://smart-dc-power-monitor-hp-iitianj.streamlit.app/)

# ヘッドレス（サーバーデプロイ）
python3 -m streamlit run dashboard.py --server.headless true
```

---

### 📸 スクリーンショット

> ダッシュボードは `http://localhost:8510` で動作中

| ビュー | 説明 |
|---|---|
| **ダッシュボード概要** | ヘッダー、5つのメトリクスカード、5つのインタラクティブ時系列グラフ |
| **グラフ分析** | フル幅Plotlyグラフと相関ヒートマップ |
| **アラートと警告** | 赤/黄/青/緑の条件付きアラートカード |
| **システム情報** | レスポンシブグリッドレイアウトの集計統計 |
| **今後の改善点** | ホバーエフェクト付き6つのロードマップカード |
| **日本語モード** | 全UI要素に適用された完全な日本語翻訳 |

---

### 🔮 今後の改善点

| 改善項目 | 説明 |
|---|---|
| 📡 **IoT統合** | MQTT / RS-485プロトコルを介してリアルハードウェアセンサーに接続 |
| ☁️ **クラウドストレージ** | AWS / Azure / GCPへの測定値送信でリモートアクセスを実現 |
| 🔌 **ハードウェアセンサー** | INA226 / ACS712チップによる高精度測定のデプロイ |
| 📧 **メールアラート** | しきい値超過時の自動SMTP通知 |
| 📱 **モバイルアプリ** | プッシュ通知付きクロスプラットフォームFlutterアプリ |
| 🤖 **機械学習予測** | LSTMベースの異常検知による障害の事前予測 |

---

### 👩‍💻 作者

<div align="center">

**Harshita Pahadia（ハルシタ・パハディア）**

*データサイエンス・AI愛好家 | Pythonデベロッパー | ダッシュボードエンジニア*

[![GitHub](https://img.shields.io/badge/GitHub-HarshitaPahadia-181717?style=flat-square&logo=github)](https://github.com/Harsh-PAHADIA)

---

*精密に構築し、産業のために設計。*

</div>

---

### 📄 ライセンス

本プロジェクトは **MITライセンス** のもとで公開されています — 帰属表示を条件として、自由に使用・修正・配布できます。

```
MIT License © 2025 Harshita Pahadia
```

---

<div align="center">

---

*Smart DC Power Supply Monitoring System*
*スマートDC電源監視システム*

**Made with ⚡ by Harshita Pahadia**

</div>
