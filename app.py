# app.py

import streamlit as st
import pandas as pd
import math

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Experiential Learning Lab - Time Value of Money",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def currency(x):
    return f"₹{x:,.2f}"

def future_value(pv, r, n):
    return pv * ((1 + r) ** n)

def present_value(fv, r, n):
    return fv / ((1 + r) ** n)

def annuity_pv(c, r, n):
    return c * ((1 - (1 + r) ** (-n)) / r)

def annuity_due_pv(c, r, n):
    return annuity_pv(c, r, n) * (1 + r)

def perpetuity_value(c, r):
    return c / r

def growing_perpetuity(c1, r, g):
    return c1 / (r - g)

def growing_annuity(c, r, g, n):
    return (c / (r - g)) * (1 - (((1 + g) / (1 + r)) ** n))

def calculate_npv(rate, cashflows):
    total = 0
    for i, cf in enumerate(cashflows):
        total += cf / ((1 + rate) ** i)
    return total

# =========================================================
# TITLE
# =========================================================

st.title("💰 Experiential Learning Lab: Time Value of Money")

st.markdown("""
This interactive learning platform teaches:

✅ Time Value of Money  
✅ Present Value & Future Value  
✅ Annuities & Annuity Due  
✅ Perpetuities  
✅ Retirement Planning  
✅ Loan Comparison  
✅ APR vs EAR  
✅ Startup & Project Valuation  

through:
- practical scenarios,
- experiential learning,
- real-world financial decisions,
- interactive simulations,
- solved examples,
- practice problems,
- common student mistakes.
""")

# =========================================================
# SIDEBAR
# =========================================================

module = st.sidebar.radio(
    "Choose Module",
    [
        "Introduction",
        "Future Value",
        "Present Value",
        "Regular Annuity",
        "Annuity Due",
        "Perpetuity",
        "Growing Perpetuity",
        "Growing Annuity",
        "APR vs EAR",
        "NPV and Uneven Cash Flows",
        "Retirement Planning",
        "Common Student Mistakes",
        "Financial Decision Lab"
    ]
)

# =========================================================
# INTRODUCTION
# =========================================================

if module == "Introduction":

    st.header("📘 Introduction to Time Value of Money")

    st.markdown("""
## Core Idea

A rupee today is worth more than a rupee tomorrow because:

- money can earn returns,
- inflation reduces purchasing power,
- future payments are uncertain,
- individuals prefer immediate consumption.

---

## Experiential Trigger

Would you prefer:

- ₹10,000 today
OR
- ₹12,000 after 2 years?

Why?

This simple question introduces:
- opportunity cost,
- compounding,
- discounting,
- risk.
""")

    st.info("""
TVM forms the foundation of:
- investing,
- retirement planning,
- loans,
- startups,
- fintech,
- real estate,
- insurance,
- valuation.
""")

# =========================================================
# FUTURE VALUE
# =========================================================

elif module == "Future Value":

    st.header("📈 Future Value")

    st.markdown("""
## Real-World Examples

- SIP investments
- Mutual funds
- Fixed deposits
- Retirement investments
- Startup investing

---

## Formula

FV = PV × (1+r)^n
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        pv = st.number_input("Present Value", value=100000.0)

    with col2:
        rate = st.number_input("Interest Rate (%)", value=10.0)

    with col3:
        years = st.number_input("Years", value=5)

    result = future_value(pv, rate / 100, years)

    st.success(f"Future Value = {currency(result)}")

    st.subheader("✅ Solved Example")

    st.markdown("""
Investment:
- ₹1,00,000
- 10%
- 5 years

FV = 1,00,000 × (1.10)^5

Answer = ₹1,61,051
""")

    st.subheader("📝 Practice Problem")

    st.markdown("""
A student invests:
- ₹50,000
- at 12%
- for 8 years

Find future value.
""")

    if st.checkbox("Show Solution"):
        ans = future_value(50000, 0.12, 8)
        st.success(f"Answer = {currency(ans)}")

# =========================================================
# PRESENT VALUE
# =========================================================

elif module == "Present Value":

    st.header("📉 Present Value")

    st.markdown("""
## Real-World Examples

- Salary negotiations
- Deferred payments
- Bond valuation
- Startup funding
- Insurance

---

## Formula

PV = FV / (1+r)^n
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        fv = st.number_input("Future Value", value=500000.0)

    with col2:
        rate = st.number_input("Discount Rate (%)", value=12.0)

    with col3:
        years = st.number_input("Years", value=4)

    result = present_value(fv, rate / 100, years)

    st.success(f"Present Value = {currency(result)}")

    st.subheader("🧠 Practical Example")

    st.markdown("""
Company Offer:

Option A:
- ₹8 lakh today

Option B:
- ₹10 lakh after 3 years

Which is better?
""")

# =========================================================
# REGULAR ANNUITY
# =========================================================

elif module == "Regular Annuity":

    st.header("🏦 Regular Annuity")

    st.markdown("""
## Equal Payments at END of Period

### Examples
- EMI
- Loan repayment
- Pension
- Salary

---

## Formula

PV = C[(1-(1+r)^-n)/r]
""")

    payment = st.number_input("Payment", value=10000.0)
    rate = st.number_input("Rate (%)", value=8.0)
    periods = st.number_input("Periods", value=10)

    result = annuity_pv(payment, rate / 100, periods)

    st.success(f"Present Value = {currency(result)}")

    st.subheader("🚗 Practical Example")

    st.markdown("""
Bike loan:
- EMI = ₹10,000
- 10 years
- 8% discount rate
""")

# =========================================================
# ANNUITY DUE
# =========================================================

elif module == "Annuity Due":

    st.header("🏠 Annuity Due")

    st.markdown("""
## Equal Payments at BEGINNING of Period

### Examples
- House rent
- Insurance premium
- Lease rentals
- Netflix subscription
- School fees

---

## Formula

PV(Annuity Due) = PV(Ordinary Annuity) × (1+r)
""")

    payment = st.number_input("Payment", value=25000.0)
    rate = st.number_input("Rate (%)", value=9.0)
    periods = st.number_input("Periods", value=5)

    result = annuity_due_pv(payment, rate / 100, periods)

    st.success(f"Present Value = {currency(result)}")

    st.subheader("🏠 Experiential Scenario")

    st.markdown("""
Why do landlords ask rent in advance?

Because earlier cash flows are more valuable.
""")

# =========================================================
# PERPETUITY
# =========================================================

elif module == "Perpetuity":

    st.header("♾️ Perpetuity")

    st.markdown("""
## Infinite Constant Cash Flows

### Examples
- Rental property
- Endowment funds
- Preferred shares

---

## Formula

PV = C/r
""")

    cashflow = st.number_input("Annual Cash Flow", value=300000.0)
    rate = st.number_input("Required Return (%)", value=10.0)

    result = perpetuity_value(cashflow, rate / 100)

    st.success(f"Value = {currency(result)}")

# =========================================================
# GROWING PERPETUITY
# =========================================================

elif module == "Growing Perpetuity":

    st.header("📊 Growing Perpetuity")

    st.markdown("""
## Cash Flows Grow Forever

### Examples
- Dividend stocks
- Mature startups
- Growing rentals

---

## Formula

PV = C1/(r-g)
""")

    c1 = st.number_input("Next Year's Cash Flow", value=50.0)
    r = st.number_input("Required Return (%)", value=11.0)
    g = st.number_input("Growth Rate (%)", value=5.0)

    if r > g:
        result = growing_perpetuity(c1, r / 100, g / 100)
        st.success(f"Value = {currency(result)}")
    else:
        st.error("Required return must exceed growth rate.")

# =========================================================
# GROWING ANNUITY
# =========================================================

elif module == "Growing Annuity":

    st.header("📈 Growing Annuity")

    st.markdown("""
## Payments Grow but Eventually Stop

### Examples
- Salary growth
- Tuition inflation
- Career income

---

## Formula

PV = [C/(r-g)] × [1-((1+g)/(1+r))^n]
""")

    c = st.number_input("First Payment", value=800000.0)
    r = st.number_input("Discount Rate (%)", value=11.0)
    g = st.number_input("Growth Rate (%)", value=7.0)
    n = st.number_input("Years", value=25)

    if r > g:
        result = growing_annuity(c, r / 100, g / 100, n)
        st.success(f"Present Value = {currency(result)}")
    else:
        st.error("Discount rate must exceed growth rate.")

# =========================================================
# APR VS EAR
# =========================================================

elif module == "APR vs EAR":

    st.header("🏦 Comparing Loan Rates: APR vs EAR")

    st.markdown("""
## Why 12% is NOT Always 12%

Banks and fintech apps often advertise low APR.

But actual borrowing cost depends on:
- compounding,
- hidden charges,
- payment frequency.

---

## Formula

EAR = (1 + APR/m)^m - 1
""")

    col1, col2 = st.columns(2)

    with col1:
        apr = st.number_input("APR (%)", value=12.0)

    with col2:
        m = st.selectbox(
            "Compounding Frequency",
            {
                "Annual": 1,
                "Semi-Annual": 2,
                "Quarterly": 4,
                "Monthly": 12,
                "Daily": 365
            }
        )

    ear = ((1 + (apr / 100) / m) ** m) - 1

    st.success(f"Effective Annual Rate = {round(ear*100,2)}%")

    st.subheader("📘 Excel Formula")

    st.code("=EFFECT(APR,m)", language="excel")

    st.subheader("💳 Practical Loan Comparison")

    loanA = ((1 + 0.12 / 12) ** 12) - 1
    loanB = ((1 + 0.123) ** 1) - 1

    comparison = pd.DataFrame({
        "Loan": ["Loan A", "Loan B"],
        "APR": ["12%", "12.3%"],
        "Compounding": ["Monthly", "Annual"],
        "EAR": [
            f"{round(loanA*100,2)}%",
            f"{round(loanB*100,2)}%"
        ]
    })

    st.table(comparison)

    st.subheader("⚠️ Common Student Mistakes")

    mistakes = pd.DataFrame({
        "Mistake": [
            "Comparing APR directly",
            "Ignoring compounding",
            "Ignoring processing fees"
        ],
        "Why Wrong": [
            "APR ignores actual compounding impact",
            "More frequent compounding increases cost",
            "Hidden charges increase effective borrowing"
        ]
    })

    st.table(mistakes)

# =========================================================
# NPV
# =========================================================

elif module == "NPV and Uneven Cash Flows":

    st.header("💼 NPV and Uneven Cash Flows")

    st.markdown("""
## Real-World Examples

- Startup valuation
- Capital budgeting
- Business projects
- Investment analysis

---

## Formula

NPV = Initial Investment + Discounted Future Cash Flows
""")

    rate = st.number_input("Discount Rate (%)", value=12.0)

    initial = st.number_input("Initial Investment", value=-500000.0)

    cf1 = st.number_input("Year 1 Cash Flow", value=100000.0)
    cf2 = st.number_input("Year 2 Cash Flow", value=200000.0)
    cf3 = st.number_input("Year 3 Cash Flow", value=300000.0)
    cf4 = st.number_input("Year 4 Cash Flow", value=400000.0)

    cashflows = [initial, cf1, cf2, cf3, cf4]

    result = calculate_npv(rate / 100, cashflows)

    st.success(f"NPV = {currency(result)}")

# =========================================================
# RETIREMENT
# =========================================================

elif module == "Retirement Planning":

    st.header("👴 Retirement Planning Simulator")

    st.markdown("""
## Build Your Retirement Corpus

Estimate how much wealth you can accumulate.
""")

    monthly = st.number_input("Monthly Investment", value=15000.0)

    annual_return = st.number_input(
        "Expected Annual Return (%)",
        value=12.0
    )

    years = st.number_input("Years to Retirement", value=35)

    monthly_rate = annual_return / 100 / 12

    periods = years * 12

    corpus = monthly * (
        (((1 + monthly_rate) ** periods) - 1)
        / monthly_rate
    )

    st.success(f"Estimated Retirement Corpus = {currency(corpus)}")

# =========================================================
# COMMON STUDENT MISTAKES
# =========================================================

elif module == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes")

    mistakes = pd.DataFrame({
        "Mistake": [
            "Using 10 instead of 0.10",
            "Confusing PV and FV",
            "Ignoring timing of payments",
            "Using APR instead of EAR",
            "Ignoring inflation",
            "Wrong cash flow signs",
            "Using wrong formula"
        ],
        "Explanation": [
            "Percentages must be converted to decimals",
            "Compounding vs discounting",
            "Beginning vs end matters",
            "EAR gives actual borrowing cost",
            "Real value differs from nominal",
            "Initial investment usually negative",
            "Cash flow pattern matters"
        ]
    })

    st.table(mistakes)

# =========================================================
# DECISION LAB
# =========================================================

elif module == "Financial Decision Lab":

    st.header("🧠 Financial Decision Lab")

    st.markdown("""
## Integrated Experiential Exercise

You are planning:
- education,
- career,
- home purchase,
- retirement,
- investments.

How do financial decisions today affect future wealth?
""")

    st.subheader("📘 Reflection Questions")

    st.markdown("""
1. Would you rather consume today or invest today?
2. How does debt affect your future?
3. Why do earlier investments create more wealth?
4. How does inflation reduce purchasing power?
5. Why is financial literacy important?
""")

    st.info("""
This module can be used for:
- classroom discussion,
- simulations,
- group activities,
- reflective learning,
- experiential finance education.
""")
