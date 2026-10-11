# Student Data Management & Performance Evaluation Tool

## 📁 Project Overview
A lightweight Python application designed to track, manage, and audit student academic metrics. This project demonstrates deep data structuring via nested dictionary objects, real-time aggregate querying, and conditional classification logic.

## 🛠️ Core Programming Concepts Demonstrated
* **Nested Data Modeling:** Engineered an in-memory data store utilizing nested JSON-like dictionary structures (`{roll_number: {'name': name, 'marks': marks}}`) to efficiently group and manage relational attributes.
* **Dynamic Type Casting:** Implemented defensive float-casting mechanics to convert unstructured terminal input strings into numeric values for quantitative tracking.
* **Automated Classification Logic:** Programmed conditional sorting parameters to automatically evaluate data points against performance benchmarks (Pass/Fail conditional loops at a ≥ 40-point threshold).
* **Targeted Querying Functions:** Developed localized search parameters that query key identifiers (Roll Numbers) to isolate and extract specific records with O(1) lookup efficiency.

## 🖥️ Terminal Interface Preview
```text
----- Student Management App -----
1. Add Student
2. View Students
3. Check Result
4. Exit
Enter your choice (1-4): 3
Enter roll number to check result: 101

Roll Number: 101
Name: Alex Smith
Marks: 78.5
Result: Pass
```
# Student-Result-Manager
A lightweight Python application designed to track, manage, and audit student academic metrics. This project demonstrates deep data structuring via nested dictionary objects, real-time aggregate querying, and conditional classification logic.
