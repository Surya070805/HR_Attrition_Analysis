"""
========================================================================================
  IBM HR ATTRITION ANALYTICS - FEATURE ENGINEERING & DATA TRANSFORMATION SCRIPT
  Author: Surya Velugula
  Repository: https://github.com/Surya070805/HR_Attrition_Analysis
========================================================================================
This script performs domain-driven feature engineering, binned cohorts,
and calculates the Risk Matrix and Persona Intersection metrics.
"""

import os
import pandas as pd
import numpy as np


def load_data(file_path: str) -> pd.DataFrame:
    """Loads the HR dataset from Excel or CSV format."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    print(f"Loading dataset from: {file_path}")
    return pd.read_excel(file_path)


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies strategic feature engineering and ordinal sort columns:
    1. Age Groups (Dashboard 4-band & Detailed 5-band)
    2. Tenure Cohorts (First-year cliff analysis)
    3. Income Tiers (Executive, Senior, Mid, Low)
    4. Promotion Gap Categories
    """
    df = df.copy()

    # Numeric indicator for Attrition
    df["Attrition_Num"] = (df["Attrition"].str.strip().str.lower() == "yes").astype(int)

    # 1. Age Groups (Dashboard Slicer)
    def assign_age_group(age):
        if age < 30:
            return "Under 30", 1
        elif age <= 40:
            return "30 - 40", 2
        elif age <= 50:
            return "41 - 50", 3
        else:
            return "50+", 4

    age_res = df["Age"].apply(assign_age_group)
    df["Age_Group_Dashboard"] = [x[0] for x in age_res]
    df["Age_Group_Dashboard_Sort"] = [x[1] for x in age_res]

    # 2. Tenure Bands (Crucial for first-year churn analysis)
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

    tenure_res = df["YearsAtCompany"].apply(assign_tenure_band)
    df["Tenure_Band_Dashboard"] = [x[0] for x in tenure_res]
    df["Tenure_Band_Dashboard_Sort"] = [x[1] for x in tenure_res]

    # 3. Monthly Income Bands
    def assign_income_band(income):
        if income < 3000:
            return "Low (<$3K)", 1
        elif income < 6000:
            return "Medium ($3K-$6K)", 2
        elif income < 10000:
            return "High ($6K-$10K)", 3
        else:
            return "Executive ($10K+)", 4

    income_res = df["MonthlyIncome"].apply(assign_income_band)
    df["Income_Band"] = [x[0] for x in income_res]
    df["Income_Band_Sort"] = [x[1] for x in income_res]

    # 4. Promotion Gap (Stagnation indicator)
    def assign_promotion_gap(years):
        if years <= 1:
            return "Recently Promoted (<=1 yr)", 1
        elif years <= 3:
            return "Normal Progression (2-3 yrs)", 2
        elif years <= 7:
            return "At Risk / Stagnant (4-7 yrs)", 3
        else:
            return "Severe Stagnation (8+ yrs)", 4

    promo_res = df["YearsSinceLastPromotion"].apply(assign_promotion_gap)
    df["Promotion_Gap"] = [x[0] for x in promo_res]
    df["Promotion_Gap_Sort"] = [x[1] for x in promo_res]

    return df


def generate_risk_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Computes Impact (Exits), Risk (Attrition Rate), and Headcount by Job Role."""
    total_exits = df["Attrition_Num"].sum()

    grouped = df.groupby("JobRole").agg(
        Total_Employees=("Attrition_Num", "count"),
        Attrited_Employees=("Attrition_Num", "sum"),
        Attrition_Rate=("Attrition_Num", "mean"),
    ).reset_index()

    grouped["Contribution_To_Exits"] = grouped["Attrited_Employees"] / total_exits
    grouped = grouped.sort_values(by="Attrited_Employees", ascending=False)
    return grouped


def analyze_high_risk_personas(df: pd.DataFrame):
    """Prints empirical high-risk persona combinations discovered during research."""
    print("\n--- HIGH-RISK MULTI-FACTOR PERSONAS ---")

    # Persona 1: Low Income + OverTime + New Hire (<=1 yr)
    p1 = df[(df["MonthlyIncome"] < 3500) & (df["OverTime"] == "Yes") & (df["YearsAtCompany"] <= 1)]
    rate_p1 = p1["Attrition_Num"].mean() * 100
    print(f"1. Low Income + OverTime + New Hire (0-1 yr): {p1['Attrition_Num'].sum()}/{len(p1)} exited ({rate_p1:.2f}%)")

    # Persona 2: Lab Tech + OverTime + New Hire (<=1 yr)
    p2 = df[(df["JobRole"] == "Laboratory Technician") & (df["OverTime"] == "Yes") & (df["YearsAtCompany"] <= 1)]
    rate_p2 = p2["Attrition_Num"].mean() * 100
    print(f"2. Lab Tech + OverTime + New Hire (0-1 yr): {p2['Attrition_Num'].sum()}/{len(p2)} exited ({rate_p2:.2f}%)")

    # Persona 3: Sales + Job Level 1 + OverTime
    p3 = df[(df["Department"] == "Sales") & (df["JobLevel"] == 1) & (df["OverTime"] == "Yes")]
    rate_p3 = p3["Attrition_Num"].mean() * 100
    print(f"3. Sales Dept + Job Level 1 + OverTime: {p3['Attrition_Num'].sum()}/{len(p3)} exited ({rate_p3:.2f}%)")


if __name__ == "__main__":
    dataset_path = os.path.join(os.path.dirname(__file__), "..", "data", "IBM_HR_Dataset.xlsx")
    if os.path.exists(dataset_path):
        df_raw = load_data(dataset_path)
        df_feat = engineer_features(df_raw)
        risk_matrix = generate_risk_matrix(df_feat)
        print("\n--- ATTRITION RISK MATRIX SUMMARY ---")
        print(risk_matrix.to_string(index=False))
        analyze_high_risk_personas(df_feat)
    else:
        print(f"Dataset path not found: {dataset_path}")
