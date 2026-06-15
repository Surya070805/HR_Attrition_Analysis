# HR Attrition Analysis
## 🛠️ Tech Stack
<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>

<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>

<img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>

<img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>

<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>

</p>

## Repository Structure & Project Artifacts

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/a4270f0e-4120-4b6d-92dd-118e7f30eb65" />

## Workforce Retention Analytics Using the IBM HR Employee Attrition Dataset

### Project Overview

Employee attrition is one of the most critical challenges faced by HR departments. High turnover increases recruitment costs, impacts productivity, causes knowledge loss, and affects business continuity.

This project develops an end-to-end HR Analytics solution using the IBM HR Employee Attrition Dataset to identify workforce risks, discover attrition drivers, uncover high-risk employee personas, and provide data-driven retention recommendations.

The project goes beyond traditional HR dashboards by combining descriptive analytics, diagnostic analytics, risk analysis, and persona analysis to support workforce retention decisions.

---

## Dashboard Preview
<img width="1693" height="929" alt="image" src="https://github.com/user-attachments/assets/da8e2554-557a-4c00-a5af-ae60b5044293" />

## Business Problem

HR leaders need answers to questions such as:

* Which employees are most likely to leave?
* What factors influence attrition?
* Which workforce segments contribute most to employee exits?
* Which employee personas represent the highest retention risk?
* Where should retention efforts be prioritized?

Traditional reporting explains **what happened**, but rarely explains **why it happened**.

This project aims to bridge that gap.

---

## Dataset

**Dataset:** IBM HR Employee Attrition Dataset

### Dataset Characteristics

* 1,470 Employee Records
* 35 Workforce Attributes
* Employee Demographics
* Job Information
* Compensation Data
* Employee Experience Metrics
* Career Progression Information
* Attrition Status

### Target Variable

```text
Attrition (Yes / No)
```

---

## Project Objectives

* Measure workforce health and attrition.
* Identify key attrition drivers.
* Discover high-risk employee segments.
* Identify employee groups contributing most to workforce loss.
* Build a retention risk framework.
* Generate actionable business recommendations.
* Support HR decision-making through analytics.

---

## Project Methodology

```text
Data Assessment
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Driver Analysis
        ↓
Contribution Analysis
        ↓
Risk Matrix
        ↓
2D Driver Analysis
        ↓
3D Persona Analysis
        ↓
Recommendations
        ↓
Dashboard Design
```

---

## Feature Engineering

The following analytical fields were created:

| Feature       | Purpose                     |
| ------------- | --------------------------- |
| Age_Band      | Employee age segmentation   |
| Income_Band   | Compensation segmentation   |
| Tenure_Band   | Employee lifecycle analysis |
| Promotion_Gap | Career progression analysis |

---

## Key Analytical Framework

### 1. Driver Analysis

Identifies employee segments with the highest attrition risk.

Metrics:

* Attrition Rate
* Attrition Difference
* Attrition Index

Example:

| Driver   | Highest Risk Segment | Attrition Rate |
| -------- | -------------------- | -------------- |
| Job Role | Sales Representative | 39.76%         |
| Tenure   | New Hire             | 34.88%         |
| Age Band | 18–25                | 34.78%         |

---

### 2. Contribution Analysis

Identifies workforce segments responsible for the largest share of employee exits.

Example:

| Driver     | Largest Contributor    | Exits |
| ---------- | ---------------------- | ----- |
| Department | Research & Development | 133   |
| Job Role   | Laboratory Technician  | 62    |
| Job Level  | Level 1                | 143   |

---

### 3. Risk Matrix

Combines:

* Attrition Risk
* Workforce Impact

to prioritize retention efforts.

---

### 4. Two-Dimensional Analysis

Analyzes interactions between workforce drivers.

Example:

| Combination           | Attrition Rate |
| --------------------- | -------------- |
| OverTime + Low Income | 58.49%         |
| OverTime + New Hire   | 55.07%         |
| Sales + Low Income    | 43.75%         |

---

### 5. Three-Dimensional Persona Analysis

Identifies employee personas exhibiting elevated attrition risk.

Example:

| Persona                                     | Attrition Rate |
| ------------------------------------------- | -------------- |
| Low Income + OverTime + New Hire            | 81.25%         |
| Laboratory Technician + OverTime + New Hire | 75.00%         |
| Sales + Job Level 1 + OverTime              | 72.73%         |

---

## Key Findings

### Highest Attrition Risk Segments

| Dimension         | Segment              | Attrition Rate |
| ----------------- | -------------------- | -------------- |
| Job Role          | Sales Representative | 39.76%         |
| Tenure Band       | New Hire             | 34.88%         |
| Age Band          | 18–25                | 34.78%         |
| Work-Life Balance | Level 1              | 31.25%         |
| OverTime          | Yes                  | 30.53%         |

---

### Largest Contributors to Attrition

| Dimension      | Segment                | Exits |
| -------------- | ---------------------- | ----- |
| Department     | Research & Development | 133   |
| Job Level      | Level 1                | 143   |
| Income Band    | Low Income             | 108   |
| Marital Status | Single                 | 120   |

---

### Major Workforce Risks

* Early-career employee attrition
* Overtime-related turnover
* Low-income employee retention challenges
* Entry-level workforce instability
* Sales Representative turnover

---

## Recommendations

### Short-Term Actions

* Improve onboarding programs.
* Review overtime policies.
* Strengthen manager support for new hires.
* Monitor high-risk employee groups.

### Long-Term Actions

* Develop career progression programs.
* Review compensation competitiveness.
* Improve retention strategies for entry-level employees.
* Build workforce planning initiatives around identified risk segments.

---

## Project Deliverables

### Notebooks

* IBM-HR-Analytics_Notebook_1.ipynb
* IBM-HR-Analytics_Notebook_2.ipynb

### Documentation

* Project Charter
* Business Requirements Document (BRD)
* Functional Requirements Document (FRD)
* User Stories
* KPI Dictionary
* Insight Log
* Recommendation Log
* Requirements Traceability Matrix (RTM)

### Dashboard

* HR Analytics Dashboard (Excel)

---

## Repository Structure

```text
HR-Analytics-Dashboard/

├── data/
│   └── IBM_HR_Dataset.xlsx
│
├── notebooks/
│   ├── IBM-HR-Analytics_Notebook_1.ipynb
│   └── IBM-HR-Analytics_Notebook_2.ipynb
│
├── dashboard/
│   └── HR_Analytics_Dashboard.xlsx
│
├── documentation/
│   └── Project_Portfolio_Report.pdf
│
├── assets/
│   └── dashboard_screenshots/
│
└── README.md
```

---

## Skills Demonstrated

### Business Analysis

* Stakeholder Analysis
* Requirements Gathering
* KPI Definition
* User Story Development

### Data Analytics

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Driver Analysis
* Risk Analysis
* Persona Analysis

### Reporting & Visualization

* Excel Dashboard Design
* Business Insight Generation
* Recommendation Framework

### Documentation

* BRD
* FRD
* RTM
* KPI Dictionary
* Insight Log
* Recommendation Log

---

## Project Outcome

The project successfully transformed employee data into actionable retention intelligence by identifying workforce risks, discovering attrition drivers, prioritizing retention opportunities, and supporting data-driven HR decision-making.

This project demonstrates both technical analytics capabilities and business-focused problem-solving skills commonly expected from Data Analysts and Business Analysts.
