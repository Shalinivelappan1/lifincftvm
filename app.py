import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Experiential TVM Learning Lab",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def currency(x):
    return f"₹{x:,.2f}"

# =========================================================
# TITLE
# =========================================================

st.title("💰 Experiential Learning Lab: Time Value of Money")

st.markdown("""
Welcome to the experiential finance learning platform.

This app teaches:

- Future Value
- Present Value
- Annuities
- Annuity Due
- Perpetuity
- Growing Cash Flows
- Retirement Planning
- APR vs EAR
- NPV and Valuation

through:

✅ Practical financial decisions  
✅ Real-world examples  
✅ Simulations  
✅ Gamification  
✅ AI hints  
✅ Formula selection guidance  
✅ Interactive visualizations
""")

# =========================================================
# SIDEBAR
# =========================================================

menu = st.sidebar.radio(
    "Choose Feature",
    [
        "Introduction",
        "Cash Flow Visualization",
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
        "Decision Simulator",
        "Formula Selection Assistant",
        "Gamification",
        "AI Hint System",
        "Quiz Engine",
        "Inflation Impact Simulator",
        "Excel Formula Trainer",
        "Loan Amortization",
        "Step-by-Step Solver",
        "Behavioral Finance",
        "Formula Cheat Sheet",
        "Advanced Quiz Bank",
        "Progress Tracker",
        "Case-Based Learning",
        "Common Student Mistakes"
    ]
)

# =========================================================
# INTRODUCTION
# =========================================================

if menu == "Introduction":

    st.header("📘 Introduction to Time Value of Money")

    st.markdown("""
## Core Idea

A rupee today is worth more than a rupee tomorrow.

Why?

- Money can earn returns
- Inflation reduces purchasing power
- Future cash flows are uncertain
- Individuals prefer immediate consumption

---

## Experiential Question

Would you prefer:

- ₹10,000 today
OR
- ₹12,000 after 2 years?

This introduces:

- compounding
- discounting
- opportunity cost
- delayed gratification
""")

    st.info("""
TVM is the foundation of:

- investing
- retirement planning
- startup valuation
- fintech
- insurance
- loans
- real estate
""")

# =========================================================
# CASH FLOW VISUALIZATION
# =========================================================

elif menu == "Cash Flow Visualization":

    st.header("📊 Cash Flow Visualization")

    st.markdown("""
Visualize:

- inflows
- outflows
- annuities
- uneven cash flows
""")

    years = [0, 1, 2, 3, 4, 5]

    cashflows = []

    for i in years:
        cf = st.number_input(
            f"Cash Flow Year {i}",
            value=0.0,
            key=f"cf_{i}"
        )
        cashflows.append(cf)

    colors = [
        'green' if cf >= 0 else 'red'
        for cf in cashflows
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=years,
            y=cashflows,
            text=[currency(cf) for cf in cashflows],
            textposition='outside',
            marker_color=colors
        )
    )

    fig.update_layout(
        title="Cash Flow Timeline",
        xaxis_title="Year",
        yaxis_title="Cash Flow (₹)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
Green = inflow

Red = outflow
""")

# =========================================================
# FUTURE VALUE
# =========================================================

elif menu == "Future Value":

    st.header("📈 Future Value")

    st.markdown("""
## Formula

FV = PV × (1+r)^n

---

## Real-World Examples

- SIP investments
- Mutual funds
- Fixed deposits
- Retirement investing
- Startup investing
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        pv = st.number_input("Present Value (₹)", value=100000.0, min_value=0.0)

    with col2:
        r = st.number_input("Annual Interest Rate (%)", value=10.0, min_value=0.0, max_value=100.0)

    with col3:
        # FIX: cast to int to avoid float exponent issues
        n = int(st.number_input("Years", value=5, min_value=1, step=1))

    fv = pv * ((1 + r / 100) ** n)

    st.success(f"Future Value = {currency(fv)}")

    # Growth chart
    years_range = list(range(0, n + 1))
    fv_values = [pv * ((1 + r / 100) ** t) for t in years_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years_range, y=fv_values,
        mode='lines+markers',
        name='Future Value',
        line=dict(color='green', width=2)
    ))
    fig.update_layout(
        title="Growth of Investment Over Time",
        xaxis_title="Year",
        yaxis_title="Value (₹)"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("✅ Solved Example")

    st.markdown("""
Investment:

- ₹1,00,000
- 10%
- 5 years

FV = 1,00,000 × (1.10)^5
""")

    st.info(f"Answer = {currency(100000 * ((1.10) ** 5))}")

    st.subheader("📝 Practice Problem")

    st.markdown("""
A student invests:

- ₹50,000
- at 12%
- for 8 years

Find Future Value.
""")

    if st.checkbox("Show Practice Solution"):
        ans = 50000 * ((1.12) ** 8)
        st.success(f"Answer = {currency(ans)}")

# =========================================================
# PRESENT VALUE
# =========================================================

elif menu == "Present Value":

    st.header("📉 Present Value")

    st.markdown("""
## Formula

PV = FV / (1+r)^n

---

## Real-World Examples

- salary negotiations
- startup funding
- deferred payments
- bond valuation
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        fv = st.number_input("Future Value (₹)", value=500000.0, min_value=0.0)

    with col2:
        r = st.number_input("Discount Rate (%)", value=12.0, min_value=0.0, max_value=100.0)

    with col3:
        # FIX: cast to int
        n = int(st.number_input("Years", value=4, min_value=1, step=1))

    pv = fv / ((1 + r / 100) ** n)

    st.success(f"Present Value = {currency(pv)}")

    # Discount chart
    years_range = list(range(0, n + 1))
    pv_values = [fv / ((1 + r / 100) ** t) for t in years_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years_range, y=pv_values,
        mode='lines+markers',
        name='Present Value',
        line=dict(color='blue', width=2)
    ))
    fig.update_layout(
        title="Present Value of Future Amount",
        xaxis_title="Years from Now",
        yaxis_title="Present Value (₹)"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧠 Practical Example")

    st.markdown("""
Company Offer:

Option A:
- ₹8 lakh today

Option B:
- ₹10 lakh after 3 years

Which is better at 12% discount rate?
""")

    pv_option_b = 1000000 / ((1.12) ** 3)
    st.info(f"PV of Option B = {currency(pv_option_b)}")

    if pv_option_b > 800000:
        st.success("Option B is better (higher present value).")
    else:
        st.success("Option A is better (higher present value).")

# =========================================================
# REGULAR ANNUITY
# =========================================================

elif menu == "Regular Annuity":

    st.header("🏦 Regular Annuity")

    st.markdown("""
## Equal Payments at END of Period

Examples:

- EMI
- pension
- loan repayment
- salary

---

## Formula

PV = C × [(1-(1+r)^-n) / r]
""")

    payment = st.number_input("Payment per Period (₹)", value=10000.0, min_value=0.0)
    r = st.number_input("Rate per Period (%)", value=8.0, min_value=0.0, max_value=100.0)
    # FIX: cast to int
    n = int(st.number_input("Number of Periods", value=10, min_value=1, step=1))

    if r == 0:
        pv = payment * n
    else:
        pv = payment * ((1 - (1 + r / 100) ** (-n)) / (r / 100))

    st.success(f"Present Value of Annuity = {currency(pv)}")

    # FV of annuity as bonus
    if r > 0:
        fv_ann = payment * (((1 + r / 100) ** n - 1) / (r / 100))
        st.info(f"Future Value of Annuity = {currency(fv_ann)}")

# =========================================================
# ANNUITY DUE
# =========================================================

elif menu == "Annuity Due":

    st.header("🏠 Annuity Due")

    st.markdown("""
## Payments at BEGINNING of Period

Examples:

- rent
- insurance
- school fees
- subscriptions
- lease rentals

---

## Formula

PV(Annuity Due) = PV(Ordinary Annuity) × (1+r)
""")

    payment = st.number_input("Payment per Period (₹)", value=25000.0, min_value=0.0)
    r = st.number_input("Rate per Period (%)", value=9.0, min_value=0.0, max_value=100.0)
    # FIX: cast to int
    n = int(st.number_input("Number of Periods", value=5, min_value=1, step=1))

    if r == 0:
        ordinary = payment * n
    else:
        ordinary = payment * ((1 - (1 + r / 100) ** (-n)) / (r / 100))

    annuity_due = ordinary * (1 + r / 100)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Ordinary Annuity PV", currency(ordinary))
    with col2:
        st.metric("Annuity Due PV", currency(annuity_due))

    st.success(f"Annuity Due Present Value = {currency(annuity_due)}")
    st.info("Annuity due is always higher — earlier payments are more valuable.")

# =========================================================
# PERPETUITY
# =========================================================

elif menu == "Perpetuity":

    st.header("♾️ Perpetuity")

    st.markdown("""
## Formula

PV = C / r

---

## Examples

- rental property
- scholarship fund
- preferred stock
- consol bonds
""")

    c = st.number_input("Annual Cash Flow (₹)", value=300000.0, min_value=0.0)
    r = st.number_input("Required Return (%)", value=10.0, min_value=0.01, max_value=100.0)

    value = c / (r / 100)

    st.success(f"Perpetuity Value = {currency(value)}")

    st.markdown(f"""
**Interpretation:** You need {currency(value)} invested today at {r}%
to generate {currency(c)} per year forever.
""")

# =========================================================
# GROWING PERPETUITY
# =========================================================

elif menu == "Growing Perpetuity":

    st.header("📊 Growing Perpetuity")

    st.markdown("""
## Formula

PV = C₁ / (r - g)

---

## Examples

- dividend discount model (Gordon Growth)
- real estate rental with inflation growth
""")

    c1 = st.number_input("Next Year's Cash Flow (₹)", value=50000.0, min_value=0.0)
    r = st.number_input("Required Return (%)", value=11.0, min_value=0.0, max_value=100.0)
    g = st.number_input("Growth Rate (%)", value=5.0, min_value=0.0, max_value=100.0)

    if r <= g:
        st.error("⚠️ Required return must be STRICTLY greater than growth rate (r > g).")
    else:
        value = c1 / ((r / 100) - (g / 100))
        st.success(f"Growing Perpetuity Value = {currency(value)}")

# =========================================================
# GROWING ANNUITY
# =========================================================

elif menu == "Growing Annuity":

    st.header("📈 Growing Annuity")

    st.markdown("""
## Formula

PV = [C / (r-g)] × [1 - ((1+g)/(1+r))^n]

---

## Examples

- salary growing at a fixed rate
- rental income with annual step-up
""")

    c = st.number_input("First Payment (₹)", value=800000.0, min_value=0.0)
    r = st.number_input("Discount Rate (%)", value=11.0, min_value=0.0, max_value=100.0)
    g = st.number_input("Growth Rate (%)", value=7.0, min_value=0.0, max_value=100.0)
    # FIX: cast to int
    n = int(st.number_input("Years", value=25, min_value=1, step=1))

    if r <= g:
        st.error("⚠️ Discount rate must be STRICTLY greater than growth rate (r > g).")
    else:
        pv = (
            (c / ((r / 100) - (g / 100)))
            * (1 - (((1 + g / 100) / (1 + r / 100)) ** n))
        )
        st.success(f"Present Value = {currency(pv)}")

# =========================================================
# APR VS EAR
# =========================================================

elif menu == "APR vs EAR":

    st.header("🏦 Comparing Loan Rates: APR vs EAR")

    st.markdown("""
## Why 12% is NOT Always 12%

Banks and fintech apps advertise APR.

But actual borrowing cost depends on:

- compounding frequency
- hidden charges
- payment timing

---

## Formula

EAR = (1 + APR/m)^m - 1
""")

    frequency_options = {
        "Annual": 1,
        "Semi-Annual": 2,
        "Quarterly": 4,
        "Monthly": 12,
        "Daily": 365
    }

    col1, col2 = st.columns(2)

    with col1:
        apr = st.number_input("APR (%)", value=12.0, min_value=0.0, max_value=100.0)

    with col2:
        frequency_label = st.selectbox(
            "Compounding Frequency",
            list(frequency_options.keys())
        )

    m = frequency_options[frequency_label]

    ear = ((1 + (apr / 100) / m) ** m) - 1

    st.success(f"Effective Annual Rate (EAR) = {round(ear * 100, 4)}%")

    st.subheader("📘 Excel Formula")
    st.code("=EFFECT(APR, m)", language="excel")

    st.subheader("💳 Practical Loan Comparison")

    loanA = ((1 + 0.12 / 12) ** 12) - 1
    loanB = ((1 + 0.123) ** 1) - 1

    comparison = pd.DataFrame({
        "Loan": ["Loan A", "Loan B"],
        "APR": ["12%", "12.3%"],
        "Compounding": ["Monthly", "Annual"],
        "EAR": [
            f"{round(loanA * 100, 4)}%",
            f"{round(loanB * 100, 4)}%"
        ]
    })

    st.table(comparison)

    if loanA < loanB:
        st.success("✅ Loan A (12% monthly compounding) is cheaper despite lower APR.")
    else:
        st.success("✅ Loan B (12.3% annual compounding) is cheaper.")

    st.info("Financial products with identical APR may have different effective costs due to compounding frequency.")

# =========================================================
# NPV
# =========================================================

elif menu == "NPV and Uneven Cash Flows":

    st.header("💼 NPV and Uneven Cash Flows")

    st.markdown("""
## Formula

NPV = Σ [ CFₜ / (1+r)^t ]

**Note:** Year 0 cash flow (initial investment) is NOT discounted.  
Excel's =NPV() discounts ALL inputs — always add Year 0 separately:  
`=NPV(rate, cf1:cfn) + initial_investment`
""")

    rate = st.number_input("Discount Rate (%)", value=12.0, min_value=0.0, max_value=100.0)

    num_years = int(st.number_input("Number of Years (excluding Year 0)", value=4, min_value=1, max_value=20, step=1))

    initial = st.number_input("Year 0 Cash Flow (Initial Investment — enter negative for outflow)", value=-500000.0)

    cashflows = [initial]

    cols = st.columns(min(num_years, 4))
    for i in range(1, num_years + 1):
        col = cols[(i - 1) % len(cols)]
        with col:
            cf = st.number_input(f"Year {i} CF (₹)", value=100000.0 * i, key=f"npv_cf_{i}")
        cashflows.append(cf)

    npv = sum(cf / ((1 + rate / 100) ** t) for t, cf in enumerate(cashflows))

    if npv >= 0:
        st.success(f"NPV = {currency(npv)} ✅ Accept the project (NPV ≥ 0)")
    else:
        st.error(f"NPV = {currency(npv)} ❌ Reject the project (NPV < 0)")

    # Waterfall chart
    disc_cfs = [cf / ((1 + rate / 100) ** t) for t, cf in enumerate(cashflows)]
    fig = go.Figure(go.Bar(
        x=[f"Year {i}" for i in range(len(cashflows))],
        y=disc_cfs,
        marker_color=['red' if v < 0 else 'green' for v in disc_cfs]
    ))
    fig.update_layout(title="Discounted Cash Flows by Year", yaxis_title="Discounted CF (₹)")
    st.plotly_chart(fig, use_container_width=True)

    # Excel formula note
    excel_args = ", ".join([f"cf{i}" for i in range(1, num_years + 1)])
    st.code(f"=NPV({rate}%, {excel_args}) + {initial}", language="excel")

# =========================================================
# RETIREMENT PLANNING
# =========================================================

elif menu == "Retirement Planning":

    st.header("👴 Retirement Planning Simulator")

    monthly = st.number_input("Monthly Investment (₹)", value=15000.0, min_value=0.0)
    annual_return = st.number_input("Expected Annual Return (%)", value=12.0, min_value=0.0, max_value=50.0)
    # FIX: cast to int
    years = int(st.number_input("Years to Retirement", value=35, min_value=1, step=1))

    monthly_rate = annual_return / 100 / 12
    periods = years * 12

    if monthly_rate == 0:
        corpus = monthly * periods
    else:
        corpus = monthly * (
            (((1 + monthly_rate) ** periods) - 1) / monthly_rate
        )

    total_invested = monthly * periods
    wealth_created = corpus - total_invested

    st.success(f"Estimated Retirement Corpus = {currency(corpus)}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Invested", currency(total_invested))
    with col2:
        st.metric("Wealth Created", currency(wealth_created))
    with col3:
        st.metric("Corpus", currency(corpus))

    # Growth chart
    year_list = list(range(0, years + 1))
    corpus_list = []
    for y in year_list:
        p = y * 12
        if monthly_rate == 0:
            corpus_list.append(monthly * p)
        else:
            corpus_list.append(monthly * (((1 + monthly_rate) ** p - 1) / monthly_rate))

    invested_list = [monthly * y * 12 for y in year_list]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=year_list, y=corpus_list, name="Corpus", fill='tozeroy', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=year_list, y=invested_list, name="Amount Invested", line=dict(color='blue', dash='dash')))
    fig.update_layout(title="Retirement Corpus Growth", xaxis_title="Year", yaxis_title="Value (₹)")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# DECISION SIMULATOR
# =========================================================

elif menu == "Decision Simulator":

    st.header("🧠 Financial Decision Simulator")

    scenario = st.selectbox(
        "Choose Scenario",
        ["Buy vs Rent", "SIP vs FD"]
    )

    if scenario == "Buy vs Rent":

        home_price = st.slider("House Price (₹)", 1000000, 20000000, 5000000, step=100000)
        down_payment = st.slider("Down Payment (₹)", 100000, 5000000, 1000000, step=50000)
        rate = st.slider("Loan Rate (%)", 5.0, 15.0, 8.5, step=0.1)
        years = st.slider("Loan Years", 5, 30, 20)

        principal = home_price - down_payment
        r = rate / 100 / 12
        n = years * 12

        emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
        total_payment = emi * n
        total_interest = total_payment - principal

        st.success(f"Monthly EMI = ₹{emi:,.2f}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Principal", currency(principal))
        with col2:
            st.metric("Total Interest", currency(total_interest))
        with col3:
            st.metric("Total Payment", currency(total_payment))

    elif scenario == "SIP vs FD":

        investment = st.slider("Monthly Investment (₹)", 1000, 100000, 10000, step=1000)
        years = st.slider("Years", 1, 40, 20)
        sip_return = st.slider("SIP Return (%)", 5.0, 20.0, 12.0, step=0.5)
        fd_return = st.slider("FD Return (%)", 3.0, 10.0, 6.5, step=0.5)

        sip_r = sip_return / 100 / 12
        fd_r = fd_return / 100 / 12
        n = years * 12

        sip_fv = investment * (((1 + sip_r) ** n) - 1) / sip_r
        fd_fv = investment * (((1 + fd_r) ** n) - 1) / fd_r
        total_invested = investment * n

        comparison = pd.DataFrame({
            "Option": ["SIP", "FD", "Total Invested"],
            "Value": [currency(sip_fv), currency(fd_fv), currency(total_invested)]
        })

        st.table(comparison)

        if sip_fv > fd_fv:
            st.success(f"SIP outperforms FD by {currency(sip_fv - fd_fv)} over {years} years.")
        else:
            st.info("FD outperforms SIP for this combination.")

# =========================================================
# FORMULA SELECTION ASSISTANT
# =========================================================

elif menu == "Formula Selection Assistant":

    st.header("🧮 Formula Selection Assistant")

    equal = st.radio("Are cash flows equal?", ["Yes", "No"])

    if equal == "No":
        st.success("Recommended Formula: NPV / Uneven Cash Flows")

    else:
        infinite = st.radio("Do cash flows continue forever?", ["Yes", "No"])

        if infinite == "Yes":
            growth = st.radio("Do cash flows grow?", ["Yes", "No"])
            if growth == "Yes":
                st.success("Recommended Formula: Growing Perpetuity — PV = C₁/(r-g)")
            else:
                st.success("Recommended Formula: Perpetuity — PV = C/r")
        else:
            growth = st.radio("Do cash flows grow over time?", ["Yes", "No"])
            if growth == "Yes":
                st.success("Recommended Formula: Growing Annuity — PV = [C/(r-g)] × [1-((1+g)/(1+r))^n]")
            else:
                timing = st.radio("When do payments occur?", ["Beginning of period", "End of period"])
                if timing == "Beginning of period":
                    st.success("Recommended Formula: Annuity Due — PV = PV(Ordinary Annuity) × (1+r)")
                else:
                    st.success("Recommended Formula: Ordinary Annuity — PV = C × [(1-(1+r)^-n)/r]")

# =========================================================
# GAMIFICATION
# =========================================================

elif menu == "Gamification":

    st.header("🎮 Financial Literacy Challenge")

    score = 0

    q1 = st.radio(
        "Q1: You receive ₹1 lakh bonus. What do you do?",
        ["Spend Entirely", "Invest in SIP", "Buy Expensive Gadget"]
    )

    if q1 == "Invest in SIP":
        score += 10
        st.success("✅ Excellent financial decision! +10 points")
    elif q1 != "Spend Entirely" and q1 != "Buy Expensive Gadget":
        pass
    else:
        st.warning("❌ Short-term pleasure reduces long-term wealth.")

    q2 = st.radio(
        "Q2: Which loan is actually cheaper?",
        ["12% compounded monthly", "12.3% compounded annually"]
    )

    if q2 == "12.3% compounded annually":
        score += 10
        st.success("✅ Correct! EAR of 12% monthly = 12.68%. Compare EAR, not APR. +10 points")
    else:
        st.warning("❌ 12% monthly compounding gives EAR of 12.68%, making it more expensive.")

    q3 = st.radio(
        "Q3: You need ₹50 lakh in 20 years. What helps most?",
        ["Starting SIP today", "Starting SIP 5 years later", "Saving in cash"]
    )

    if q3 == "Starting SIP today":
        score += 10
        st.success("✅ Time in market matters most — compounding rewards early starters. +10 points")
    else:
        st.warning("❌ Every year of delay significantly reduces the final corpus.")

    st.divider()

    st.progress(score / 30)
    st.metric("Financial Literacy Score", f"{score}/30")

    if score == 30:
        st.balloons()
        st.success("🏆 Perfect score! You're a financial wizard!")
    elif score >= 20:
        st.success("Strong financial reasoning!")
    else:
        st.warning("Review the TVM modules to improve your score.")

# =========================================================
# AI HINT SYSTEM
# =========================================================

elif menu == "AI Hint System":

    st.header("🤖 AI Finance Hint System")

    st.markdown("""
A student deposits:

- ₹50,000 today
- 10% interest per year
- 5 years

Find the future value.
""")

    answer = st.number_input("Enter Your Answer (₹)", value=0.0)

    correct = 50000 * ((1.10) ** 5)

    if st.button("Check Answer"):
        if abs(answer - correct) < 100:
            st.success(f"✅ Correct! Answer = {currency(correct)}")
            st.balloons()
        else:
            diff = abs(answer - correct)
            st.error(f"❌ Incorrect. You're off by {currency(diff)}. Use hints below.")

    if st.checkbox("Hint 1: Direction"):
        st.info("💡 Is money moving forward or backward in time? (Forward → compounding)")

    if st.checkbox("Hint 2: Concept"):
        st.info("💡 Money grows over time. We are finding what ₹50,000 becomes after 5 years.")

    if st.checkbox("Hint 3: Formula"):
        st.info("💡 Use FV = PV × (1+r)^n = 50,000 × (1.10)^5")

    if st.checkbox("Show Full Solution"):
        st.latex(r"FV = 50000 \times (1.10)^5")
        st.success(f"Correct Answer = {currency(correct)}")

# =========================================================
# QUIZ ENGINE
# =========================================================

elif menu == "Quiz Engine":

    st.header("📝 Finance Quiz Engine")

    difficulty = st.selectbox("Choose Difficulty", ["Beginner", "Intermediate"])

    # FIX: Use session_state to lock random values so they don't regenerate on every rerun
    if "quiz_generated" not in st.session_state or st.button("🔄 New Question"):
        if difficulty == "Beginner":
            st.session_state.quiz_pv = random.randint(10000, 100000)
            st.session_state.quiz_r = random.randint(5, 15)
            st.session_state.quiz_n = random.randint(1, 10)
            st.session_state.quiz_type = "FV"
        else:
            st.session_state.quiz_pv = random.randint(50000, 500000)
            st.session_state.quiz_r = random.randint(6, 18)
            st.session_state.quiz_n = random.randint(3, 15)
            st.session_state.quiz_type = "PV"
        st.session_state.quiz_generated = True

    pv = st.session_state.quiz_pv
    r = st.session_state.quiz_r
    n = st.session_state.quiz_n
    qtype = st.session_state.quiz_type

    if qtype == "FV":
        correct = pv * ((1 + r / 100) ** n)
        st.markdown(f"""
**Calculate Future Value:**

- Present Value = ₹{pv:,}
- Interest Rate = {r}% per year
- Years = {n}
""")
    else:
        fv_val = pv
        correct = fv_val / ((1 + r / 100) ** n)
        st.markdown(f"""
**Calculate Present Value:**

- Future Value = ₹{fv_val:,}
- Discount Rate = {r}% per year
- Years = {n}
""")

    ans = st.number_input("Your Answer (₹)", value=0.0, key="quiz_ans")

    if st.button("Submit Answer"):
        if abs(ans - correct) < 100:
            st.success(f"✅ Correct! Answer = {currency(correct)}")
            st.balloons()
        else:
            st.error(f"❌ Incorrect. Correct Answer = {currency(correct)}")

# =========================================================
# INFLATION MODULE
# =========================================================

elif menu == "Inflation Impact Simulator":

    st.header("📉 Inflation Impact Simulator")

    st.markdown("""
Understand how inflation erodes purchasing power over time.
""")

    current_money = st.number_input("Current Amount (₹)", value=1000000.0, min_value=0.0)
    inflation = st.slider("Inflation Rate (%)", 1.0, 15.0, 6.0, step=0.5)
    years = st.slider("Years", 1, 40, 20)

    future_purchasing_power = current_money / ((1 + inflation / 100) ** years)

    st.success(f"Future Purchasing Power = {currency(future_purchasing_power)}")
    st.warning(f"Inflation erodes {currency(current_money - future_purchasing_power)} of your wealth over {years} years.")

    # Real return example
    st.subheader("Real vs Nominal Return")

    nominal = st.number_input("Nominal Return (%)", value=10.0, min_value=0.0, max_value=50.0)

    real_return = ((1 + nominal / 100) / (1 + inflation / 100)) - 1

    st.info(f"Real Return = {round(real_return * 100, 2)}%  (Fisher Equation)")

    # Chart
    years_list = list(range(0, years + 1))
    pp_list = [current_money / ((1 + inflation / 100) ** y) for y in years_list]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years_list, y=pp_list, mode='lines+markers', name='Purchasing Power', line=dict(color='red')))
    fig.add_hline(y=current_money, line_dash="dash", annotation_text="Starting Amount")
    fig.update_layout(title="Purchasing Power Over Time", xaxis_title="Year", yaxis_title="Purchasing Power (₹)")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# EXCEL FORMULA TRAINER
# =========================================================

elif menu == "Excel Formula Trainer":

    st.header("📊 Excel Formula Trainer")

    problems = {
        "Future Value": {
            "description": "Find FV: PV = ₹1,00,000 | Rate = 10% | Years = 5",
            "correct_fn": "FV",
            "correct_formula": "=FV(10%,5,0,-100000)",
            "hint": "FV(rate, nper, pmt, [pv])"
        },
        "Present Value": {
            "description": "Find PV: FV = ₹5,00,000 | Rate = 10% | Years = 5",
            "correct_fn": "PV",
            "correct_formula": "=PV(10%,5,0,-500000)",
            "hint": "PV(rate, nper, pmt, [fv])"
        },
        "EMI Calculation": {
            "description": "Find EMI: Loan = ₹10,00,000 | Rate = 8%/yr | Tenure = 10 years",
            "correct_fn": "PMT",
            "correct_formula": "=PMT(8%/12,120,-1000000)",
            "hint": "PMT(rate, nper, pv)"
        },
        "EAR from APR": {
            "description": "Find EAR: APR = 12% | Compounding = Monthly",
            "correct_fn": "EFFECT",
            "correct_formula": "=EFFECT(12%,12)",
            "hint": "EFFECT(nominal_rate, npery)"
        }
    }

    selected = st.selectbox("Choose Problem", list(problems.keys()))
    prob = problems[selected]

    st.subheader("Problem")
    st.markdown(prob["description"])
    st.info(f"💡 Function hint: `{prob['hint']}`")

    user_formula = st.text_input("Enter Excel Formula (start with =)")

    if st.button("Validate Formula"):
        if prob["correct_fn"] in user_formula.upper():
            st.success(f"✅ Correct Excel function used! Reference answer: `{prob['correct_formula']}`")
        else:
            st.error(f"❌ Try using the {prob['correct_fn']}() function.")

    if st.checkbox("Show Answer"):
        st.code(prob["correct_formula"], language="excel")

# =========================================================
# LOAN AMORTIZATION SCHEDULE
# =========================================================

elif menu == "Loan Amortization":

    st.header("🏦 Loan Amortization Schedule")

    principal = st.number_input("Loan Amount (₹)", value=1000000.0, min_value=1000.0)
    annual_rate = st.slider("Annual Interest Rate (%)", 1.0, 20.0, 8.0, step=0.25)
    years = st.slider("Loan Tenure (Years)", 1, 30, 10)

    r = annual_rate / 100 / 12
    n = years * 12

    emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)

    total_payment = emi * n
    total_interest = total_payment - principal

    st.success(f"Monthly EMI = {currency(emi)}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Principal", currency(principal))
    with col2:
        st.metric("Total Interest", currency(total_interest))
    with col3:
        st.metric("Total Payment", currency(total_payment))

    balance = principal
    schedule = []

    for month in range(1, n + 1):
        interest = balance * r
        principal_paid = emi - interest
        balance = balance - principal_paid

        # FIX: clamp balance to 0 for last payment floating point error
        if month == n:
            balance = 0.0

        schedule.append([
            month,
            round(emi, 2),
            round(principal_paid, 2),
            round(interest, 2),
            round(max(balance, 0), 2)
        ])

    df = pd.DataFrame(
        schedule,
        columns=["Month", "EMI (₹)", "Principal (₹)", "Interest (₹)", "Balance (₹)"]
    )

    st.subheader("Amortization Schedule (first 24 months)")
    st.dataframe(df.head(24), use_container_width=True)

    # Interest vs Principal chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Month"], y=df["Principal (₹)"], name="Principal", fill='tozeroy'))
    fig.add_trace(go.Scatter(x=df["Month"], y=df["Interest (₹)"], name="Interest", fill='tozeroy'))
    fig.update_layout(title="Principal vs Interest Over Time", xaxis_title="Month", yaxis_title="Amount (₹)")
    st.plotly_chart(fig, use_container_width=True)

    st.download_button(
        "📥 Download Full Schedule",
        df.to_csv(index=False),
        file_name="amortization_schedule.csv",
        mime="text/csv"
    )

    st.info("Early EMI payments contain mostly interest. Principal repayment accelerates over time.")

# =========================================================
# STEP-BY-STEP SOLVER
# =========================================================

elif menu == "Step-by-Step Solver":

    st.header("🧠 Step-by-Step Finance Solver")

    problem_type = st.selectbox(
        "Choose Problem Type",
        ["Future Value", "Present Value", "Annuity PV", "EMI"]
    )

    if problem_type == "Future Value":
        pv = st.number_input("Present Value (₹)", value=100000.0)
        r = st.number_input("Rate (%)", value=10.0)
        n = int(st.number_input("Years", value=5, min_value=1, step=1))

        st.write("**Step 1: Identify formula**")
        st.latex(r"FV = PV \times (1+r)^n")

        st.write("**Step 2: Substitute values**")
        st.latex(rf"FV = {pv:,.0f} \times (1 + {r/100})^{{{n}}}")

        st.write("**Step 3: Calculate**")
        answer = pv * ((1 + r / 100) ** n)
        st.success(f"FV = {currency(answer)}")

    elif problem_type == "Present Value":
        fv = st.number_input("Future Value (₹)", value=500000.0)
        r = st.number_input("Discount Rate (%)", value=12.0)
        n = int(st.number_input("Years", value=5, min_value=1, step=1))

        st.write("**Step 1: Identify formula**")
        st.latex(r"PV = \frac{FV}{(1+r)^n}")

        st.write("**Step 2: Substitute values**")
        st.latex(rf"PV = \frac{{{fv:,.0f}}}{{(1 + {r/100})^{{{n}}}}}")

        st.write("**Step 3: Calculate**")
        answer = fv / ((1 + r / 100) ** n)
        st.success(f"PV = {currency(answer)}")

    elif problem_type == "Annuity PV":
        c = st.number_input("Payment per Period (₹)", value=10000.0)
        r = st.number_input("Rate per Period (%)", value=8.0)
        n = int(st.number_input("Periods", value=10, min_value=1, step=1))

        st.write("**Step 1: Identify formula**")
        st.latex(r"PV = C \times \frac{1-(1+r)^{-n}}{r}")

        st.write("**Step 2: Substitute values**")
        answer = c * ((1 - (1 + r / 100) ** (-n)) / (r / 100))
        st.success(f"PV = {currency(answer)}")

    elif problem_type == "EMI":
        p = st.number_input("Loan Amount (₹)", value=1000000.0)
        r_annual = st.number_input("Annual Rate (%)", value=8.0)
        years = int(st.number_input("Years", value=10, min_value=1, step=1))

        r = r_annual / 100 / 12
        n = years * 12

        st.write("**Step 1: Identify formula**")
        st.latex(r"EMI = \frac{P \times r \times (1+r)^n}{(1+r)^n - 1}")

        st.write("**Step 2: Convert to monthly rate**")
        st.info(f"Monthly rate = {r_annual}% / 12 = {round(r*100, 4)}%")

        st.write("**Step 3: Calculate**")
        emi = p * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
        st.success(f"EMI = {currency(emi)}")

# =========================================================
# BEHAVIORAL FINANCE
# =========================================================

elif menu == "Behavioral Finance":

    st.header("🧠 Behavioral Finance Simulator")

    st.markdown("""
Understand how emotional biases affect financial decision-making.
""")

    st.subheader("Scenario 1: Windfall Decision")

    choice = st.radio(
        "You receive ₹1 lakh bonus. What do you do?",
        ["Buy Luxury Phone", "Invest in SIP", "Travel Vacation"]
    )

    if choice == "Invest in SIP":
        future = 100000 * ((1.12) ** 20)
        st.success(f"✅ Smart! In 20 years at 12%, this becomes {currency(future)}")
    else:
        st.warning("⚠️ Present bias: Short-term pleasure reduces long-term wealth creation.")
        st.info("₹1 lakh invested at 12% for 20 years = " + currency(100000 * ((1.12) ** 20)))

    st.subheader("Scenario 2: Loss Aversion")

    st.markdown("""
Your mutual fund is down 15%. What do you do?
""")

    choice2 = st.radio(
        "Decision:",
        ["Sell immediately to stop losses", "Hold — stay invested", "Buy more at lower price"]
    )

    if choice2 == "Sell immediately to stop losses":
        st.warning("⚠️ Loss aversion bias — most people feel losses 2x more than gains. Selling locks in losses.")
    elif choice2 == "Hold — stay invested":
        st.success("✅ Markets recover over time. Staying invested is usually the right call.")
    else:
        st.success("✅ Rupee-cost averaging — buying more at lower prices reduces average cost.")

# =========================================================
# FORMULA CHEAT SHEET
# =========================================================

elif menu == "Formula Cheat Sheet":

    st.header("📘 Complete TVM Formula Cheat Sheet")

    formulas = """
TIME VALUE OF MONEY FORMULAS
---------------------------------------------------
1. FUTURE VALUE
---------------------------------------------------
FV = PV(1+r)^n
Excel: =FV(rate,nper,pmt,pv)
---------------------------------------------------
2. PRESENT VALUE
---------------------------------------------------
PV = FV/(1+r)^n
Excel: =PV(rate,nper,pmt,fv)
---------------------------------------------------
3. ORDINARY ANNUITY
---------------------------------------------------
PV = C[(1-(1+r)^-n)/r]
Excel: =PV(rate,nper,pmt)
---------------------------------------------------
4. ANNUITY DUE
---------------------------------------------------
PV(AD) = PV(OA)(1+r)
Excel: =PV(rate,nper,pmt,,1)
---------------------------------------------------
5. PERPETUITY
---------------------------------------------------
PV = C/r
---------------------------------------------------
6. GROWING PERPETUITY
---------------------------------------------------
PV = C1/(r-g)
---------------------------------------------------
7. GROWING ANNUITY
---------------------------------------------------
PV = [C/(r-g)] x [1-((1+g)/(1+r))^n]
---------------------------------------------------
8. EFFECTIVE ANNUAL RATE (EAR)
---------------------------------------------------
EAR = (1+APR/m)^m - 1
Excel: =EFFECT(APR,m)
---------------------------------------------------
9. NET PRESENT VALUE (NPV)
---------------------------------------------------
NPV = Sum[CF/(1+r)^t]
Excel: =NPV(rate, cf1:cfn) + initial_investment
NOTE: Excel NPV does NOT include Year 0 automatically
---------------------------------------------------
10. EMI FORMULA
---------------------------------------------------
EMI = P*r*(1+r)^n / [(1+r)^n - 1]
Excel: =PMT(rate,nper,pv)
---------------------------------------------------
11. REAL RETURN (Fisher Equation)
---------------------------------------------------
Real Return = [(1+Nominal)/(1+Inflation)] - 1
---------------------------------------------------
12. CAGR
---------------------------------------------------
CAGR = (FV/PV)^(1/n) - 1
---------------------------------------------------
13. FUTURE VALUE OF SIP
---------------------------------------------------
FV = PMT[((1+r)^n - 1)/r]
Excel: =FV(rate,nper,-pmt)
---------------------------------------------------
14. PAYBACK PERIOD
---------------------------------------------------
Payback = Initial Investment / Annual Cash Flow
---------------------------------------------------
15. PROFITABILITY INDEX
---------------------------------------------------
PI = PV of Future Cash Flows / Initial Investment
Accept if PI > 1
---------------------------------------------------
16. ANNUITY DUE FV
---------------------------------------------------
FV(AD) = FV(OA)(1+r)
---------------------------------------------------
COMMON FINANCE MISTAKES
---------------------------------------------------
- Using 10 instead of 0.10 (forget decimal conversion)
- Mixing monthly and annual rates
- Ignoring compounding frequency
- Forgetting annuity due timing adjustment
- Using APR instead of EAR for true cost comparison
- Wrong sign convention in Excel (PV negative, FV positive)
- Ignoring inflation in long-term planning
- Excel NPV() excludes Year 0 — always add manually
- Using annual rate with monthly cash flows
- Using monthly rate with yearly cash flows
---------------------------------------------------
"""

    st.text_area("TVM Formula Reference", formulas, height=700)

    st.download_button(
        label="📥 Download Formula Cheat Sheet",
        data=formulas,
        file_name="TVM_Formula_Cheat_Sheet.txt"
    )

# =========================================================
# ADVANCED QUIZ BANK
# =========================================================

elif menu == "Advanced Quiz Bank":

    st.header("📝 Advanced Quiz Bank")

    level = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":

        st.markdown("""
**Problem:** A bank offers 8% annual interest.
You deposit ₹2,00,000 today.
What is the value after 6 years?
""")

        answer = st.number_input("Your Answer (₹)", value=0.0, key="aq_beg")
        correct = 200000 * ((1.08) ** 6)

        if st.button("Evaluate", key="aq_beg_btn"):
            if abs(answer - correct) < 100:
                st.success(f"✅ Correct! Answer = {currency(correct)}")
                st.balloons()
            else:
                st.error(f"❌ Correct Answer = {currency(correct)}")
                st.latex(r"FV = 2,00,000 \times (1.08)^6")

    elif level == "Intermediate":

        st.markdown("""
**Problem:** You want ₹50 lakh after 15 years.
Expected return = 10% per year.
What monthly SIP amount is required?
""")

        answer = st.number_input("Your Answer (₹/month)", value=0.0, key="aq_int")

        r = 10 / 100 / 12
        n = 15 * 12
        fv_target = 5000000
        correct = fv_target * r / (((1 + r) ** n) - 1)

        if st.button("Evaluate", key="aq_int_btn"):
            if abs(answer - correct) < 200:
                st.success(f"✅ Correct! Monthly SIP = {currency(correct)}")
                st.balloons()
            else:
                st.error(f"❌ Correct Answer = {currency(correct)} per month")

    elif level == "Advanced":

        st.markdown("""
**Problem:** A startup generates:

- Year 1 = ₹1 lakh
- Year 2 = ₹3 lakh
- Year 3 = ₹5 lakh

Discount Rate = 15%  
Initial Investment = ₹4 lakh

Find NPV. Should you invest?
""")

        answer = st.number_input("Your Answer (₹)", value=0.0, key="aq_adv")

        correct = (
            -400000
            + 100000 / (1.15)
            + 300000 / (1.15 ** 2)
            + 500000 / (1.15 ** 3)
        )

        if st.button("Evaluate", key="aq_adv_btn"):
            if abs(answer - correct) < 100:
                st.success(f"✅ Correct! NPV = {currency(correct)}")
                if correct >= 0:
                    st.success("Accept the project (NPV ≥ 0)")
                else:
                    st.error("Reject the project (NPV < 0)")
                st.balloons()
            else:
                st.error(f"❌ Correct Answer = {currency(correct)}")
                st.markdown("""
**Solution:**
NPV = -4,00,000 + 1,00,000/1.15 + 3,00,000/1.15² + 5,00,000/1.15³
""")

# =========================================================
# PROGRESS TRACKER
# =========================================================

elif menu == "Progress Tracker":

    st.header("📈 Student Progress Tracker")

    # FIX: Use session_state to actually track progress across modules
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = []

    if "quiz_scores" not in st.session_state:
        st.session_state.quiz_scores = []

    all_modules = [
        "Future Value", "Present Value", "Regular Annuity", "Annuity Due",
        "Perpetuity", "Growing Perpetuity", "Growing Annuity", "APR vs EAR",
        "NPV and Uneven Cash Flows", "Retirement Planning",
        "Inflation Impact Simulator", "Loan Amortization"
    ]

    st.subheader("Mark Completed Modules")

    selected = st.multiselect(
        "Select modules you have completed:",
        all_modules,
        default=st.session_state.completed_modules
    )

    st.session_state.completed_modules = selected

    st.subheader("Log a Quiz Score")

    col1, col2 = st.columns(2)
    with col1:
        quiz_name = st.selectbox("Quiz", ["Beginner", "Intermediate", "Advanced"])
    with col2:
        quiz_score = st.number_input("Score (%)", 0, 100, 75)

    if st.button("Log Score"):
        st.session_state.quiz_scores.append({"quiz": quiz_name, "score": quiz_score})
        st.success("Score logged!")

    st.divider()

    completed_count = len(selected)
    total = len(all_modules)

    st.metric("Modules Completed", f"{completed_count}/{total}")
    st.progress(completed_count / total)

    if st.session_state.quiz_scores:
        avg_score = sum(s["score"] for s in st.session_state.quiz_scores) / len(st.session_state.quiz_scores)
        st.metric("Average Quiz Score", f"{round(avg_score, 1)}%")

        score_df = pd.DataFrame(st.session_state.quiz_scores)
        st.dataframe(score_df, use_container_width=True)

    if completed_count == total:
        st.success("🏆 You have completed all modules!")
        st.balloons()
    elif completed_count > total * 0.75:
        st.success("Almost there! Keep going.")
    else:
        st.warning("Practice more advanced problems.")

# =========================================================
# CASE-BASED LEARNING
# =========================================================

elif menu == "Case-Based Learning":

    st.header("📚 Financial Life Case Study")

    st.markdown("""
**Arjun is 25 years old.**

He has ₹5 lakh in savings and earns ₹1 lakh/month.

He is deciding between:

1. Buying a car (₹8 lakh on EMI at 9%)
2. Starting ₹20,000/month SIP at 12% for 30 years
3. Taking education loan for MBA abroad
4. Saving for retirement from age 25 vs age 35

What should he prioritize?
""")

    option = st.radio(
        "Best Long-Term Financial Decision:",
        [
            "Luxury Consumption (car, gadgets)",
            "Early Investing (SIP from age 25)",
            "High Credit Card Spending"
        ]
    )

    if option == "Early Investing (SIP from age 25)":
        corpus_25 = 20000 * (((1 + 12/100/12) ** (30*12)) - 1) / (12/100/12)
        corpus_35 = 20000 * (((1 + 12/100/12) ** (20*12)) - 1) / (12/100/12)
        st.success("✅ Correct. Early investing benefits enormously from compounding.")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Starting at 25 (30 yrs)", currency(corpus_25))
        with col2:
            st.metric("Starting at 35 (20 yrs)", currency(corpus_35))
        st.info(f"Delaying by 10 years costs {currency(corpus_25 - corpus_35)} in final corpus!")
    else:
        st.warning("⚠️ Short-term consumption reduces long-term wealth significantly.")
        st.info("₹20,000/month SIP at 12% for 30 years = " + currency(20000 * (((1 + 12/100/12) ** (30*12)) - 1) / (12/100/12)))

# =========================================================
# COMMON STUDENT MISTAKES
# =========================================================

elif menu == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes in TVM")

    mistakes = pd.DataFrame({
        "Mistake": [
            "Using 10 instead of 0.10",
            "Confusing PV and FV",
            "Ignoring payment timing",
            "Using APR instead of EAR",
            "Wrong sign convention in Excel",
            "Ignoring inflation",
            "Ignoring compounding frequency",
            "Using annual rate with monthly cash flows",
            "Using monthly rate with yearly cash flows",
            "Confusing quarterly, monthly, half-yearly compounding",
            "Excel NPV() does not include Year 0",
            "Applying perpetuity formula when g ≥ r",
        ],
        "Explanation": [
            "Always convert percentage to decimal: r = 10/100 = 0.10",
            "Discounting brings money back; compounding grows money forward",
            "Beginning of period (annuity due) vs end of period (ordinary annuity) changes PV",
            "EAR gives true borrowing/lending cost — always compare EAR across products",
            "Initial investment is negative; FV is positive in Excel functions",
            "Real purchasing power shrinks with inflation — use Fisher equation",
            "Monthly, quarterly and annual compounding produce very different results",
            "Monthly cash flows require monthly interest rate (APR/12)",
            "Annual cash flows require annual discount rate — don't use monthly rate",
            "Each frequency changes EAR and total cost significantly",
            "=NPV(rate, cf1:cfn) excludes Year 0 — add initial investment separately outside the formula",
            "Growing perpetuity formula PV = C/(r-g) requires r > g strictly",
        ]
    })

    st.table(mistakes)

    st.warning("""
Most TVM mistakes happen because students fail to identify:

- Cash flow structure (equal vs unequal)
- Timing (beginning vs end of period)
- Compounding frequency (annual vs monthly vs daily)
- What Excel functions actually compute
""")
