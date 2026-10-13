# 📊 IBM HR Analytics & Workforce Retention Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Power_BI-PBIP_%26_PBIR-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/DAX-28_Curated_Measures-005FB8?style=for-the-badge&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

An enterprise-grade **People Analytics & Workforce Retention Intelligence System** built using the IBM HR Employee Attrition dataset. This project diagnoses the root causes of employee turnover, isolates anomalous high-risk flight cohorts, and equips HR leadership with an executive single-page decision canvas.

The solution integrates **Exploratory Data Analysis (EDA)**, **Statistical Profiling**, **Machine Learning Feature Importance**, and a **production Power BI Desktop (PBIP / PBIR)** report backed by a **TMDL Tabular Semantic Model** with **28 production DAX business measures**.

---

## 📸 Executive Dashboard Showcase

The dashboard is engineered as an executive single-page decision canvas (`1920 × 1080` FHD, Fit-to-Page) delivering high information density with zero vertical scrolling:

<p align="center">
  <img width="1693" height="929" alt="HR Analytics Executive Dashboard" src="https://github.com/user-attachments/assets/da8e2554-557a-4c00-a5af-ae60b5044293" />
</p>

> *Local Dashboard Asset: [`dashboard/HR Analytics Dashboard.png`](dashboard/HR%20Analytics%20Dashboard.png) 

---


## 🎯 Executive Summary & Business Problem

Unplanned employee turnover costs modern enterprises between **50% to 200% of an employee's annual salary** due to recruitment costs, lost institutional knowledge, onboarding overhead, and lost productivity. In a workforce of 1,470 employees with an average monthly income of $6,503, unchecked turnover incurs millions of dollars in preventable expenses.

### 🏢 Key Workforce Metrics at a Glance
| Metric | Value | Benchmark / Status | Strategic Implication |
| :--- | :---: | :---: | :--- |
| **Total Headcount** | `1,470` | Enterprise Base | Workforce population across R&D, Sales, and HR |
| **Active Workforce** | `1,233` | `83.88%` | Retained talent driving ongoing business operations |
| **Total Exits** | `237` | Cumulative | Total voluntary and involuntary departures |
| **Company Attrition Rate** | `16.12%` | **+3.12% vs Industry (13.00%)** | 🚨 Elevated turnover exceeding industry target benchmark |
| **Overtime Workforce** | `416` | `28.30%` of staff | High burnout risk cohort requiring governance |
| **Average Tenure** | `7.0 Yrs` | Company average | Heavily skewed by senior cohort retention |

---

## 🔍 Core Analytical Discoveries & Anomalies

Through in-depth Python EDA, correlation analysis, machine learning feature importance, and Power BI DAX modeling, four distinct attrition dynamics were isolated:

### 1. 📉 The "1st-Year Cliff" (Onboarding Disruption)
Attrition is heavily front-loaded in the employee lifecycle:
- **0 – 1 Year (New Hires)**: **34.88% Attrition Rate** (75 departures out of 215 new hires).
- **1 – 3 Years**: Drops sharply to **18.43%**.
- **3 – 5 Years**: Stabilizes to **13.07%**.
- **5 – 10 Years**: Reaches **12.28%**.
- **10+ Years**: Stabilizes to **8.13%**.
> **Key Finding**: 1 out of every 3 new hires departs within their first 12 months. Retention interventions past year 2 yield diminishing returns compared to pre-emptive 90-day onboarding programs.

### 2. ⚡ The OverTime Multiplier (~3× Turnover Rate)
- **Employees working OverTime**: **30.53% Attrition Rate** (127 exits / 416 employees).
- **Employees on Standard Hours**: **10.32% Attrition Rate** (110 exits / 1,054 employees).
> **Key Finding**: Assigning staff to ongoing overtime nearly **triples their turnover probability**. Overtime is the single strongest operational catalyst of voluntary exits.

### 3. 🎯 The Attrition Risk Matrix (Impact vs. Risk Quadrants)
Taking inspiration from the Risk Matrix analysis in our Jupyter notebooks, we evaluated **Attrition Rate (Risk)** against **Total Exits (Impact)**:

```
                      HIGH RISK (Attrition Rate > 18%)
                                    ▲
        [High Risk / Moderate Volume] │ [CRITICAL RISK / MASS IMPACT]
        • Sales Representative:     │ • Laboratory Technician:
          39.76% Attrition, 33 Exits│   23.94% Attrition, 62 Exits (26.2% share)
        • Human Resources:          │ • Sales Executive:
          23.08% Attrition, 12 Exits│   17.48% Attrition, 57 Exits (24.1% share)
                                    │
LOW IMPACT ─────────────────────────┼─────────────────────────► HIGH IMPACT
(< 20 Exits)                        │                           (> 40 Exits)
        [STABLE FOUNDATION]         │ [HIGH VOLUME / LOW RISK]
        • Research Director:        │ • Research Scientist:
          2.50% Attrition, 2 Exits  │   16.10% Attrition, 47 Exits (19.8% share)
        • Manager:                  │
          4.90% Attrition, 5 Exits  │
                                    ▼
                      LOW RISK (Attrition Rate < 10%)
```

* **The Core Vulnerability**: **Laboratory Technicians (62 exits)** and **Sales Executives (57 exits)** account for **50.21% of all company exits** (119 out of 237). Targeted retention in these two roles resolves over half of the organization's attrition volume.
* **The High Churn Outlier**: **Sales Representatives** experience extreme turnover (**39.76%**), signaling severe commission volatility or role expectation mismatch.

### 4. 🚨 Multi-Factor Persona Anomaly Intersections
Applying multi-factor combinatorial slicing reveals hyper-vulnerable employee cohorts where turnover surges past 70%:
1. **Low Income (<$3.5K) + OverTime + New Hire (0-1 Yr)**: **71.43% Attrition** (30 exits / 42 staff).
2. **Laboratory Technician + OverTime + New Hire (0-1 Yr)**: **75.00% Attrition** (15 exits / 20 staff).
3. **Sales Department + Job Level 1 + OverTime**: **72.73% Attrition** (16 exits / 22 staff).

---

## 💻 Code & Technical Implementation

### 1. Production DAX Measures Catalog (`dax/all_measures.dax`)
The semantic model features **28 business measures** categorized into 5 display folders inside the dedicated `_Measures` table:

```dax
----------------------------------------------------------------------------------------
-- 1. WORKFORCE HEADCOUNT & POPULATION KPIS
----------------------------------------------------------------------------------------
Total Employees = COUNTROWS('WA_Fn-UseC_-HR-Employee-Attriti')

Active Employees = 
CALCULATE(
    COUNTROWS('WA_Fn-UseC_-HR-Employee-Attriti'), 
    'WA_Fn-UseC_-HR-Employee-Attriti'[Attrition] = "No"
)

Active Employee % = DIVIDE([Active Employees], [Total Employees], 0)

----------------------------------------------------------------------------------------
-- 2. ATTRITION METRICS & BENCHMARKS
----------------------------------------------------------------------------------------
Attrited Employees = 
CALCULATE(
    COUNTROWS('WA_Fn-UseC_-HR-Employee-Attriti'), 
    'WA_Fn-UseC_-HR-Employee-Attriti'[Attrition] = "Yes"
)

Attrition Rate = DIVIDE([Attrited Employees], [Total Employees], 0)

Company Attrition Rate = CALCULATE([Attrition Rate], ALL('WA_Fn-UseC_-HR-Employee-Attriti'))

Industry Attrition Rate = 0.13

Attrition Variance to Industry = [Attrition Rate] - [Industry Attrition Rate]

----------------------------------------------------------------------------------------
-- 3. ADVANCED ANALYTICS & RISK MATRIX METRICS
----------------------------------------------------------------------------------------
Contribution to Total Exits = 
DIVIDE(
    [Attrited Employees], 
    CALCULATE([Attrited Employees], ALL('WA_Fn-UseC_-HR-Employee-Attriti')), 
    0
)

Department Risk Level = 
SWITCH(
    TRUE(), 
    [Attrition Rate] >= 0.18, "High", 
    [Attrition Rate] >= 0.10, "Medium", 
    "Low"
)

----------------------------------------------------------------------------------------
-- 5. WORKLOAD & COMPENSATION ANALYTICS
----------------------------------------------------------------------------------------
OverTime Employees = 
CALCULATE(
    COUNTROWS('WA_Fn-UseC_-HR-Employee-Attriti'), 
    'WA_Fn-UseC_-HR-Employee-Attriti'[OverTime] = "Yes"
)

OverTime Attrition Rate = 
CALCULATE([Attrition Rate], 'WA_Fn-UseC_-HR-Employee-Attriti'[OverTime] = "Yes")

Non-OverTime Attrition Rate = 
CALCULATE([Attrition Rate], 'WA_Fn-UseC_-HR-Employee-Attriti'[OverTime] = "No")
```

👉 *Browse all 28 DAX measures in [`dax/all_measures.dax`](dax/all_measures.dax).*

---

### 2. Feature Engineering & Bins (`scripts/feature_engineering.py`)
To prevent arbitrary binning and support dynamic slicers, strategic cohorts and integer sort columns were engineered in both Python and TMDL:

```python
# 1. Tenure Bands (Crucial for first-year cliff analysis)
def assign_tenure_band(years):
    if years <= 1:
        return "0 - 1 Yr", 1
    elif years <= 3:
        return "1 - 3 Yrs", 2
    elif years <= 5:
        return "3 - 5 Yrs", 3
    elif years <= 10:
        return "5 - 10 Yrs", 4
    else:
        return "10+ Yrs", 5

# 2. Age Groups (Dashboard Slicer)
def assign_age_group(age):
    if age < 30:
        return "Under 30", 1
    elif age <= 40:
        return "30 - 40", 2
    elif age <= 50:
        return "41 - 50", 3
    else:
        return "50+", 4

# 3. Monthly Income Tiers
def assign_income_band(income):
    if income < 3000:
        return "Low (<$3K)", 1
    elif income < 6000:
        return "Medium ($3K-$6K)", 2
    elif income < 10000:
        return "High ($6K-$10K)", 3
    else:
        return "Executive ($10K+)", 4
```

👉 *Execute the complete Python script via `python scripts/feature_engineering.py`.*

---

## 📊 Power BI Dashboard Visual Architecture

The dashboard is composed of **17 modular PBIR visual containers** organized into a 3-tier hierarchy:

| Zone | Visual Containers | Business Function |
| :--- | :--- | :--- |
| **Top Navigation** | `v_0001_header_title` + 4 Slicers (`Dept`, `OverTime`, `JobRole`, `AgeGroup`) | Global filtering, context switching, and metadata status |
| **Tier 1: KPI Cards** | 6 Cards (`Total HC`, `Active HC`, `Exits`, `Attrition %`, `OverTime HC`, `Avg Tenure`) | High-level organizational health scorecards |
| **Tier 2: Diagnostics** | `v_0012_scatter_risk_matrix`, `v_0013_combo_tenure_trend`, `v_0014_bar_overtime` | Visualizes the Risk Matrix quadrants, 1st-year cliff, and overtime penalty |
| **Tier 3: Granular Action**| `v_0015_table_dept_risk`, `v_0016_bar_jobrole_churn`, `v_0017_card_briefing` | Department impact table, role ranking, and executive retention briefing |

---

## 💡 Strategic HR Action Plan & Interventions

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           STRATEGIC HR RETENTION PLAYBOOK                               │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────┤
│ 1. 90-Day Onboarding Overhaul │ 2. Overtime Governance        │ 3. Comp & Level-1 Review│
├───────────────────────────────┼───────────────────────────────┼─────────────────────────┤
│ • Tackle the 34.88% cliff     │ • Cap mandatory overtime      │ • Address 72.7% churn   │
│ • Assign peer mentors         │   to max 10 hrs/week          │   in Level-1 sales/tech │
│ • Check-ins at 30/60/90 days  │ • Provide compensatory rest   │ • Re-index entry comp   │
│ • Target: Lower 1st-year churn│ • Target: Lower overtime churn│ • Target: Stabilize base│
│   from 34.9% to < 20%         │   from 30.5% to < 18%         │   turnover in R&D/Sales │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────┘
```

---

## 📁 Repository Structure

```text
HR_Attrition_Analysis/
├── IBM HR Analytics.pbip                 # Power BI Project root file
├── IBM HR Analytics.Report/              # PBIR report definition layer
│   └── definition/
│       ├── pages/
│       │   ├── b5ec51fc64ab1a1b4998/     # Single-page executive canvas (1920x1080)
│       │   │   ├── page.json             # Canvas dimensions & background settings
│       │   │   └── visuals/              # 17 modular PBIR visual container JSONs
│       │   └── pages.json                # Page metadata index
│       └── report.json                   # Theme and report settings
├── IBM HR Analytics.SemanticModel/       # TMDL Semantic Model definition
│   └── definition/
│       ├── tables/
│       │   ├── _Measures.tmdl            # 28 DAX measures catalog
│       │   └── WA_Fn-UseC_-HR-...tmdl    # Base dataset & calculated columns
│       └── model.tmdl                    # Model configuration & relationships
├── dax/
│   └── all_measures.dax                  # Standalone DAX measures catalog
├── scripts/
│   └── feature_engineering.py            # Python feature engineering & risk matrix script
├── notebooks/
│   ├── IBM-HR-Analytics_Notebook_1.ipynb # Deep EDA, distributions, correlations
│   └── IBM-HR-Analytics_Notebook_2.ipynb # ML predictive models & feature importance
├── data/
│   └── IBM_HR_Dataset.xlsx               # Source HR workforce dataset (1,470 records)
├── documentation/
│   └── HR_Dashboard_documentation.pdf    # Comprehensive project & KPI documentation
├── dashboard/
│   ├── HR Analytics Dashboard.png        # Production dashboard screenshot
│   └── HR_Dashboard.png                  # Template & wireframe reference
├── assets/                               # Business analysis & project governance documents
│   ├── Business Requirements Document.docx
│   ├── Functional Requirements Document.docx
│   ├── KPI Dictionary.docx
│   ├── User Stories Document.docx
│   └── Requirements Traceability Matrix.docx
├── _brief/
│   └── report-spec.md                    # Report design brief & UI specifications
├── requirements.txt                      # Python environment dependencies
└── README.md                             # Flagship project documentation
```

---

## 🚀 How to Run & Explore

### 1. Open the Power BI Desktop PBIP Project
1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (June 2024 or later with PBIP preview enabled).
2. Double-click [`IBM HR Analytics.pbip`](IBM%20HR%20Analytics.pbip).
3. The report will load the live TMDL semantic model with all 17 pre-configured visuals and interactive cross-filtering.

### 2. Run the Python Feature Engineering Pipeline
```bash
# Clone the repository
git clone https://github.com/Surya070805/HR_Attrition_Analysis.git
cd HR_Attrition_Analysis

# Create a virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate  # On Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

# Run feature engineering & risk matrix validation
python scripts/feature_engineering.py
```

### 3. Explore the Jupyter Notebooks
```bash
jupyter notebook notebooks/IBM-HR-Analytics_Notebook_1.ipynb
```

---

## 👨‍💻 Author & Contact

**Surya Velugula**
* GitHub: [@Surya070805](https://github.com/Surya070805)
* Repository: [HR_Attrition_Analysis](https://github.com/Surya070805/HR_Attrition_Analysis)

*Developed as an end-to-end People Analytics portfolio project demonstrating Data Analytics, modern Power BI PBIP/TMDL report authoring, DAX engineering, and strategic HR intelligence.*
