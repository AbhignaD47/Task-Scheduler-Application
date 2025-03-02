# Task-Scheduler-Application

# 🕒 Task Scheduler Application  

## 🚀 Overview  
The **Task Scheduler Application** is a Python-based console tool designed to **automate and manage daily tasks**. It allows users to **create, edit, delete, and prioritize tasks** with deadlines, ensuring efficient task management.  

🔹 **Custom Scheduling Algorithm** for sorting tasks by priority and due date  
🔹 **Persistent Storage** – Saves tasks to a local text file  
🔹 **Error Handling & Logging** – Tracks errors and user activities  
🔹 **User-friendly Console Interface**  

---

## 📌 Features  
✅ **Add Tasks** – Set task title, description, priority (High, Medium, Low), and deadline  
✅ **Edit Tasks** – Modify task details anytime  
✅ **Delete Tasks** – Remove completed or unnecessary tasks  
✅ **View Tasks** – Sorted by **priority** and **due date**  
✅ **Input Validation** – Ensures correct data entry  
✅ **Persistent Data** – Stores tasks locally for future access  

---

## 🛠️ Tech Stack  
- **Language:** Python 🐍  
- **Storage:** Local text file 📂  
- **Modules Used:** `datetime`, `logging`, `os`, `sys`  

---

## 🧪 Test Cases  
| Test Case | Input | Expected Output |
|-----------|--------|----------------|
| ✅ Add Task | "Study Python", High, 2025-03-10 | Task added successfully |
| ❌ Invalid Priority | "Workout", Urgent, 2025-03-05 | Error: Invalid priority |
| ❌ Invalid Date | "Meeting", Medium, 03/10/2025 | Error: Use YYYY-MM-DD |
| ✅ Edit Task | Task ID 2 → Change priority to Low | Task updated successfully |
| ❌ Edit Non-existent Task | Task ID 99 | Error: Task not found |
| ✅ Delete Task | Task ID 3 | Task deleted successfully |
| ❌ Delete Non-existent Task | Task ID 50 | Error: Task not found |
| ✅ View Tasks | - | Displays sorted list or "No tasks available" |

---
