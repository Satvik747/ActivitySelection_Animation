# Activity Selection Problem - Greedy Algorithm Visualizer

An interactive web application built with **Streamlit** and **Matplotlib** to visualize and step through the **Greedy Activity Selection Algorithm** (Interval Scheduling). 

Designed as a companion learning tool for Design and Analysis of Algorithms (DAA) courses, this app allows users to input custom task intervals, automatically sort them by finish time, and scrub through the execution step-by-step to see how the greedy choice property works in real time.

---

## Live Demo
Check out the live application here: [https://activityselection.streamlit.app/](https://activityselection.streamlit.app/)

---

## Features

* **Interactive Data Editor**: Add, edit, or remove activities directly in the browser table with instant validation checks.
* **Automated Greedy Sorting**: Automatically sorts activities by their finish times (with start-time tie-breaking).
* **Step-by-Step Slider Control**: Scrub forward and backward through algorithm iterations to observe which tasks get selected or rejected.
* **Dynamic Timeline Visualization**: Clean, color-coded Matplotlib timeline charts highlighting:
  * 🟢 **Green**: Selected optimal activities.
  * 🔴 **Red**: Rejected conflicting activities.
  * ⚫ **Light Gray**: Unprocessed activities.
* **Live Step Explanations**: Real-time narrative explanations showing why a specific task meets or violates the greedy criteria at each step.

---

## Tech Stack

* **Python 3.x**
* **[Streamlit](https://streamlit.io/)** (Web App Framework)
* **[Pandas](https://pandas.pydata.org/)** (Data Manipulation & Input Handling)
* **[Matplotlib](https://matplotlib.org/)** (Timeline Chart Rendering)

---

## Local Installation & Setup

To run this application locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Satvik747/ActivitySelection_Animation.git](https://github.com/Satvik747/ActivitySelection_Animation.git)
   cd ActivitySelection_Animation