# Distributed Process Scheduling System

A **web-based CPU scheduling simulator** that visualizes and compares multiple scheduling algorithms in real-time.
This project demonstrates core **Operating System concepts** with an interactive and modern UI.

---
## 🚀 Features

* 🔄 Supports multiple scheduling algorithms:

  * First Come First Serve (FCFS)
  * Shortest Job First (SJF)
  * Shortest Remaining Job First (SRJF)
  * Round Robin (RR)

* 📊 Real-time **Gantt Chart Visualization**

* 📈 **Algorithm Comparison Dashboard**

* 🧠 Automatic **Best Algorithm Selection**

* 📋 Detailed results:

  * Waiting Time
  * Turnaround Time
  * Start & Finish Time

* 🎨 Professional UI with responsive design

* ⚙️ Dynamic task input system

---

## 🏗️ Project Structure

```
project/
│
├── app.py                # Flask backend server
├── scheduler.py          # Scheduling algorithms
│
├── templates/
│   ├── index.html        # Main simulator UI
│   └── welcome.html      # Landing page
│
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend logic
│
└── README.md
```

---

## ⚙️ Technologies Used

* **Frontend:**

  * HTML, CSS, JavaScript
  * Chart.js (for visualization)

* **Backend:**

  * Python
  * Flask

---

## 🧠 Algorithms Implemented

### 1. FCFS (First Come First Serve)

* Executes processes in order of arrival.

### 2. SJF (Shortest Job First)

* Selects process with smallest burst time.

### 3. SRJF (Shortest Remaining Job First)

* Preemptive version of SJF.

### 4. Round Robin

* Uses time quantum for fair scheduling.

👉 All algorithms generate:

* Execution timeline (Gantt)
* Waiting time
* Turnaround time

---

## 📊 Visualization

### 🔹 Gantt Chart

Displays execution sequence of processes over time.

### 🔹 Comparison Graph

Bar chart comparing:

* Average Waiting Time
* Average Turnaround Time

### 🔹 Smart Conclusion

System automatically highlights the **best algorithm** based on performance.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/scheduler-project.git
cd scheduler-project
```

---

### 2. Install Dependencies

```bash
pip install flask
```

---

### 3. Run the Application

```bash
python app.py
```

---

### 4. Open in Browser

```
http://127.0.0.1:5000
```

👉 Click **"Launch Simulator"**

---

## 📌 API Endpoints

### 🔹 `/schedule`

* Method: POST
* Input: tasks + algorithm
* Output: execution result + timeline

### 🔹 `/compare`

* Method: POST
* Input: tasks
* Output: comparison metrics + best algorithm

---

## 🧪 Example Input

| Process | Arrival Time | Burst Time |
| ------- | ------------ | ---------- |
| P1      | 0            | 5          |
| P2      | 1            | 3          |
| P3      | 2            | 8          |

---
outputs
<img width="1364" height="686" alt="image" src="https://github.com/user-attachments/assets/445c0d2b-23a4-45f1-9083-4c8904c9b6fd" /># Distributed-Scheduling-System
# Distributed-Scheduling-System 
<img width="1362" height="620" alt="image" src="https://github.com/user-attachments/assets/897caf62-7745-4494-b954-4a10ea6fe638" />

## 🎯 Use Cases

* Operating System learning
* Algorithm comparison
* Academic projects
* Visualization of scheduling concepts

 🏆 Conclusion
This project provides a complete simulation of CPU scheduling with:
* Accurate algorithm implementation
* Real-time visualization
* Performance comparison

It helps users understand how different scheduling strategies impact system performance.

## 👨‍💻 Author
Rudrayani Adichwal 
* B.Tech Student
* Interested in OS,CN, AI, ML & Systems

## 📌 Future Enhancements
🔐 User login system
📄 Export results as PDF
🌐 Deploy on cloud (Render / Railway)
🎞️ Real-time animation of scheduling

