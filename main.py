import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

st.title("Activity Selection: Greedy Animation")

# ---------- 1. User input ----------
st.subheader("1. Enter your activities")
st.caption("Edit the table, or click the empty last row to add more activities. "
           "Select a row and press Delete to remove it.")

default = pd.DataFrame({
    "Activity": ["A1", "A2", "A3", "A4", "A5"],
    "Start":    [0, 1, 2, 3, 6],
    "Finish":   [3, 5, 4, 6, 9],
})

df = st.data_editor(default, num_rows="dynamic", use_container_width=True, key="editor")

# ---------- 2. Clean and validate ----------
df = df.dropna(subset=["Start", "Finish"]).reset_index(drop=True)

if df.empty:
    st.warning("Add at least one activity.")
    st.stop()

if (df["Finish"] <= df["Start"]).any():
    st.error("Every activity must have Finish greater than Start. Please fix the table.")
    st.stop()

acts = []
for i, row in df.iterrows():
    name = str(row["Activity"]).strip() if pd.notna(row["Activity"]) and str(row["Activity"]).strip() else f"A{i+1}"
    acts.append((name, float(row["Start"]), float(row["Finish"])))

# Sort by finish time (ties broken by start time)
acts.sort(key=lambda a: (a[2], a[1]))

# ---------- 3. Precompute every greedy step ----------
steps, selected, last_finish = [], [], float("-inf")
for name, s, f in acts:
    if s >= last_finish:
        selected = selected + [name]
        last_finish = f
        status = "selected"
    else:
        status = "rejected"
    steps.append((name, s, f, status, selected, last_finish))

# ---------- 4. Step control ----------
st.subheader("2. Step through the algorithm")
n = len(acts)
k = st.slider("Step", 0, n, 0, help="Step 0 shows activities sorted by finish time. Move to step 1 and beyond to evaluate them.")
# ---------- 5. Draw ----------
fig, ax = plt.subplots(figsize=(9, 0.6 * n + 1.5))
for i, (name, s, f) in enumerate(acts):
    if i < k:
        color = "green" if steps[i][3] == "selected" else "red"
    else:
        color = "lightgray"
    ax.barh(i, f - s, left=s, color=color, edgecolor="black", alpha=0.8)
    ax.text(s + (f - s) / 2, i, f"{name} ({s:g}-{f:g})", ha="center", va="center")

ax.set_yticks([])
ax.set_xlabel("Time")
ax.invert_yaxis()
ax.legend(handles=[Patch(color="green", label="Selected"),
                   Patch(color="red", label="Rejected"),
                   Patch(color="lightgray", label="Not checked yet")],
          loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False)
st.pyplot(fig)

# ---------- 6. Explanation ----------
if k == 0:
    st.write("Activities are sorted by finish time. Move the slider to start.")
else:
    name, s, f, status, sel, lf = steps[k - 1]
    if status == "selected":
        st.write(f"Checked **{name}**: start {s:g} is at or after the previous finish, so it is **selected**.")
    else:
        st.write(f"Checked **{name}**: start {s:g} is before the previous finish, so it is **rejected**.")
    st.write(f"Selected so far: {sel} | last_finish = {lf:g}")

if k == n:
    st.success(f"Final answer: {steps[-1][4]} ({len(steps[-1][4])} activities)")