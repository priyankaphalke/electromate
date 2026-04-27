import streamlit as st
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ElectroMate ⚡", layout="wide")

st.title("⚡ ElectroMate – Smart Electrical Problem Solver")
st.write("Solve electrical problems with step-by-step explanations 🧠")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Choose Module",
    ["Ohm's Law", "Power", "Parallel Resistance", "Graph"]
)

# =========================================================
# 🔌 OHM'S LAW
# =========================================================
if menu == "Ohm's Law":
    st.header("🔌 Ohm’s Law Solver (Step-by-Step)")

    st.latex("V = IR")

    V = st.number_input("Voltage (V)", min_value=0.0)
    I = st.number_input("Current (A)", min_value=0.0)
    R = st.number_input("Resistance (Ω)", min_value=0.0)

    if st.button("Solve"):
        filled = sum([V > 0, I > 0, R > 0])

        if filled != 2:
            st.error("⚠️ Enter exactly 2 values only")
        else:
            st.subheader("🧠 Step-by-Step Solution")

            # Find V
            if V == 0:
                st.write("**Step 1:** Formula → V = I × R")
                st.write(f"**Step 2:** Substitute → V = {I} × {R}")
                result = I * R
                st.write(f"**Step 3:** V = {result:.2f} V")
                st.success(f"✅ Final Answer: {result:.2f} V")

            # Find I
            elif I == 0:
                if R == 0:
                    st.error("Resistance cannot be zero")
                else:
                    st.write("**Step 1:** Formula → I = V / R")
                    st.write(f"**Step 2:** Substitute → I = {V} / {R}")
                    result = V / R
                    st.write(f"**Step 3:** I = {result:.2f} A")
                    st.success(f"✅ Final Answer: {result:.2f} A")

            # Find R
            elif R == 0:
                if I == 0:
                    st.error("Current cannot be zero")
                else:
                    st.write("**Step 1:** Formula → R = V / I")
                    st.write(f"**Step 2:** Substitute → R = {V} / {I}")
                    result = V / I
                    st.write(f"**Step 3:** R = {result:.2f} Ω")
                    st.success(f"✅ Final Answer: {result:.2f} Ω")

# =========================================================
# 🔋 POWER
# =========================================================
elif menu == "Power":
    st.header("🔋 Power Calculator (Step-by-Step)")

    st.latex("P = VI")

    V = st.number_input("Voltage (V)", min_value=0.0)
    I = st.number_input("Current (A)", min_value=0.0)

    if st.button("Calculate"):
        if V == 0 or I == 0:
            st.error("⚠️ Enter valid values")
        else:
            st.subheader("🧠 Step-by-Step Solution")

            st.write("**Step 1:** Formula → P = V × I")
            st.write(f"**Step 2:** Substitute → P = {V} × {I}")
            result = V * I
            st.write(f"**Step 3:** P = {result:.2f} W")

            if result > 1000:
                st.warning("⚠️ High power! Be careful in real-world usage")

            st.success(f"✅ Final Answer: {result:.2f} Watts")

# =========================================================
# 🔌 PARALLEL RESISTANCE
# =========================================================
elif menu == "Parallel Resistance":
    st.header("🔌 Parallel Resistance (Step-by-Step)")

    st.latex(r"\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}")

    r1 = st.number_input("R1 (Ω)", min_value=0.1)
    r2 = st.number_input("R2 (Ω)", min_value=0.1)

    if st.button("Solve"):
        st.subheader("🧠 Step-by-Step Solution")

        st.write("**Step 1:** Formula:")
        st.latex(r"\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}")

        st.write(f"**Step 2:** Substitute → 1/Req = 1/{r1} + 1/{r2}")

        reciprocal = (1/r1) + (1/r2)
        st.write(f"**Step 3:** 1/Req = {reciprocal:.4f}")

        req = 1 / reciprocal
        st.write(f"**Step 4:** Req = {req:.2f} Ω")

        st.success(f"✅ Final Answer: {req:.2f} Ω")

# =========================================================
# 📊 GRAPH
# =========================================================
elif menu == "Graph":
    st.header("📊 V-I Graph Visualization")

    R = st.slider("Select Resistance (Ω)", 1, 20, 5)

    I = list(range(1, 11))
    V = [i * R for i in I]

    st.subheader("🧠 Explanation")
    st.write(f"Using V = I × R with R = {R} Ω")

    fig, ax = plt.subplots()
    ax.plot(I, V)
    ax.set_xlabel("Current (A)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("Voltage vs Current")

    st.pyplot(fig)