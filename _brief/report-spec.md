# Report Spec: HR Analytics Dashboard

## Report identity
- Report name: IBM HR Analytics
- Semantic model: IBM HR Analytics.SemanticModel
- Audience: HR Leadership, People Analytics Directors, Business Unit Heads, and Executive Management
- Primary purpose: Comprehensive single-page executive intelligence to diagnose workforce health, detect attrition anomalies and driver interactions, and prioritize retention interventions via an integrated 4-quadrant Risk Matrix.
- Delivery target: Local PBIP / Power BI Desktop

## Semantic model binding
- Entry mode: Local Model
- Model name: IBM HR Analytics.SemanticModel
- Path: ../IBM HR Analytics.SemanticModel
- Tables:
  - `WA_Fn-UseC_-HR-Employee-Attriti` (Core Employee Fact with 35 columns + 12 feature engineering & sort columns)
  - `_Measures` (Dedicated measure table containing 28 validated DAX metrics across 5 display folders)

## User decisions and constraints
- Scope: Single-page executive & diagnostic dashboard
- Canvas size: 1920 x 1080 (FHD 16:9)
- Interactivity: Global interactive cross-filtering across Department, OverTime, Job Role, and Age Band; dynamic cross-highlighting from Risk Matrix scatter plot to tables and bar charts.
- Design direction: Professional Executive Slate theme with high visual contrast, semantic color coding (Navy primary, Coral/Crimson for high risk, Teal for active workforce, Amber for watch areas).
- Publishing: Local PBIP authoring first (with live Power BI Desktop sync).

## Narrative
- Core story: The company experiences a **16.12% overall attrition rate**, running 3.12% above the industry benchmark (13.00%). While Research & Development accounts for the highest volume of exits (133 exits, 56.12% share), Sales suffers from the highest risk concentration (20.97% attrition rate).
- Root-cause anomalies:
  1. **The First-Year Cliff:** New hires (0-1 year tenure) face an alarming **34.88% attrition rate**, which rapidly stabilizes after year 3 (9.00%) and year 10 (3.03%).
  2. **The Overtime Burnout Multiplier:** Staff working overtime face a **30.53% attrition rate** versus **10.32%** for standard hours (~3x higher turnover).
  3. **High-Risk Personas:** Entry-level staff (`Job Level 1` + `Low Income`) subjected to overtime hit **81.25% turnover**.
- Strategic recommendations: Focus retention capital on first-year structured onboarding, rebalance overtime in R&D Lab Technicians and Sales, and conduct compensation reviews on Job Level 1 roles.

## Design identity
- Tone: Executive Decision Room (Authoritative, high-density, analytical, modern dark-accented navy canvas)
- Signature: 4-Quadrant Impact vs. Risk Matrix coupled with visual callouts for turnover multipliers.

## Page plan
1. Page 1: `Executive Workforce & Attrition Insights`
   - Archetype: Executive Summary & Diagnostic Risk Canvas
   - Canvas: 1920 x 1080 (FHD)
   - Layout Pattern: 12x12 grid with margin 32px, gutter 24px, snap 8px.
   - Purpose: Deliver full workforce overview, drillable risk matrix, tenure cliff trends, overtime anomalies, department summaries, and actionable insights in a single viewport without scrolling.

## Design system summary
- Base palette:
  - Background: Crisp Light Slate (`#F4F6F9`) with pure white card containers (`#FFFFFF`) and soft drop borders (`#E2E8F0`).
  - Primary / Headers: Deep Corporate Navy (`#0F172A`, `#1E293B`).
  - Risk / Attrition Accent: Vivid Crimson / Coral (`#DC2626` / `#EF4444`).
  - Active / Healthy Accent: Emerald / Teal (`#059669` / `#10B981`).
  - Watch / Warning Accent: Warm Amber (`#D97706` / `#F59E0B`).
  - Neutral / Benchmark: Cool Slate (`#64748B`).
- Typography pairing: Segoe UI / Aptos (Display Bold 20-28pt for KPIs & headers; Regular 10-12pt for data labels & axes).

## Model requirements
- Existing measures in `_Measures`:
  - `[Total Employees]`, `[Active Employees]`, `[Attrited Employees]`, `[Attrition Rate]`, `[Company Attrition Rate]`, `[Industry Attrition Rate]`, `[Attrition Variance to Industry]`, `[OverTime Employees]`, `[OverTime %]`, `[OverTime Attrition Rate]`, `[Non-OverTime Attrition Rate]`, `[Average Tenure]`, `[Average Age]`, `[Contribution to Total Exits]`, `[Department Risk Level]`.
- Existing calculated columns in `WA_Fn-UseC_-HR-Employee-Attriti`:
  - `Tenure_Band_Dashboard` (sorted by `Tenure_Band_Dashboard_Sort`)
  - `Age_Group_Dashboard` (sorted by `Age_Group_Dashboard_Sort`)
  - `Income_Band` (sorted by `Income_Band_Sort`)

---

## Canonical design contract

```yaml
Design Brief:
  generated_by: powerbi-report-cli
  contract_version: 1
  mode: greenfield
  design_identity:
    tone: Executive Decision Room
    signature: 4-Quadrant Impact vs Risk Matrix paired with Tenure Cliff and OverTime anomaly visualizers
  color_map:
    Total Employees: "#0F172A"
    Active Employees: "#059669"
    Attrited Employees: "#DC2626"
    Attrition Rate: "#DC2626"
    OverTime Employees: "#D97706"
    Average Tenure: "#2563EB"
    Company Attrition Rate: "#64748B"
  pages:
    - name: Executive Workforce & Attrition Insights
      archetype: Executive Summary & Diagnostic Risk Canvas
      layout_contract:
        canvas:
          width: 1920
          height: 1080
          margin: 32
          gutter: 24
          snap: 8
        grid:
          columns: 12
          rows: 12
          regions:
            header: [1, 1, 7, 2]
            filters: [7, 1, 13, 2]
            kpis: [1, 2, 13, 4]
            risk_matrix: [1, 4, 6, 8]
            tenure_trend: [6, 4, 10, 8]
            overtime_anomaly: [10, 4, 13, 8]
            dept_risk_table: [1, 8, 6, 13]
            jobrole_churn: [6, 8, 10, 13]
            executive_insights: [10, 8, 13, 13]
        placements:
          - name: page_title
            region: header
            visual_type: textbox
            title: "HR ANALYTICS — WORKFORCE & ATTRITION INTELLIGENCE"
            subtitle: "Diagnostic retention telemetry, driver risk matrix, and turnover anomaly analysis"
          - name: slicer_department
            region: filters
            visual_type: slicer
            field: "WA_Fn-UseC_-HR-Employee-Attriti[Department]"
            slicer_type: dropdown
          - name: slicer_overtime
            region: filters
            visual_type: slicer
            field: "WA_Fn-UseC_-HR-Employee-Attriti[OverTime]"
            slicer_type: dropdown
          - name: slicer_jobrole
            region: filters
            visual_type: slicer
            field: "WA_Fn-UseC_-HR-Employee-Attriti[JobRole]"
            slicer_type: dropdown
          - name: slicer_ageband
            region: filters
            visual_type: slicer
            field: "WA_Fn-UseC_-HR-Employee-Attriti[Age_Group_Dashboard]"
            slicer_type: dropdown
          - name: kpi_strip
            region: kpis
            visual_type: cardVisual
            measures:
              - "_Measures[Total Employees]"
              - "_Measures[Active Employees]"
              - "_Measures[Attrited Employees]"
              - "_Measures[Attrition Rate]"
              - "_Measures[OverTime Employees]"
              - "_Measures[Average Tenure]"
            color_strategy: measure_match
          - name: scatter_risk_matrix
            region: risk_matrix
            visual_type: scatterChart
            title: "Attrition Risk Matrix (Impact vs. Risk)"
            x_axis: "_Measures[Attrition Rate]"
            y_axis: "_Measures[Attrited Employees]"
            size: "_Measures[Total Employees]"
            details: "WA_Fn-UseC_-HR-Employee-Attriti[JobRole]"
            color_strategy: semantic
          - name: line_tenure_trend
            region: tenure_trend
            visual_type: lineChart
            title: "Attrition Rate by Tenure (1st-Year Cliff)"
            x_axis: "WA_Fn-UseC_-HR-Employee-Attriti[Tenure_Band_Dashboard]"
            y_axis: "_Measures[Attrition Rate]"
            color_strategy: unique
          - name: column_overtime_anomaly
            region: overtime_anomaly
            visual_type: columnChart
            title: "OverTime vs. Attrition Rate (~3x Multiplier)"
            x_axis: "WA_Fn-UseC_-HR-Employee-Attriti[OverTime]"
            y_axis: "_Measures[Attrition Rate]"
            color_strategy: semantic
          - name: table_dept_risk
            region: dept_risk_table
            visual_type: tableEx
            title: "Department Risk & Contribution Summary"
            columns:
              - "WA_Fn-UseC_-HR-Employee-Attriti[Department]"
              - "_Measures[Total Employees]"
              - "_Measures[Attrited Employees]"
              - "_Measures[Attrition Rate]"
              - "_Measures[Contribution to Total Exits]"
              - "_Measures[Department Risk Level]"
            color_strategy: none
          - name: bar_jobrole_churn
            region: jobrole_churn
            visual_type: barChart
            title: "Top Roles by Attrition Rate"
            category: "WA_Fn-UseC_-HR-Employee-Attriti[JobRole]"
            values: "_Measures[Attrition Rate]"
            color_strategy: gradient
          - name: card_executive_insights
            region: executive_insights
            visual_type: textbox
            title: "Executive Retention Insights & Personas"
            body: "• High-Risk Persona: Low Income + OverTime + New Hire has an 81.25% exit rate.\n• 1st Year Cliff: New hires exit at 34.88% (prioritize 90-day onboarding).\n• Volume Drivers: R&D and Sales account for 94.94% of all departures.\n• Workload Governance: Overtime creates a 3x attrition multiplier (30.5% vs 10.3%)."
        space_audit:
          total_grid_cells: 144
          occupied_cells: 144
          unplaced_regions: []
          empty_cell_pct: 0
          balance_rationale: "Full 12x12 grid utilized with zero wasted space: balanced across executive KPIs (row 2-3), core diagnostic drivers & risk matrix (row 4-7), and operational breakdown tables & prescriptive insights (row 8-12)."
```

## Implementation notes
- Model changes: All 28 measures and 12 calculated columns are already deployed and validated in the connected model and PBIP definition.
- PBIR/report authoring: Generate standard PBIR visual definition files inside `IBM HR Analytics.Report/definition/pages/`.
- Validation: Verify all visual bindings against schema, validate syntax and dimensions.
- Desktop preview: Reload Power BI Desktop to visually render the completed dashboard.
