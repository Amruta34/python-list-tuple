employees = [
    (101, "Ram", "HR"),
    (102, "Aniket", "IT"),
    (103, "Prathmesh", "Finance"),
    (104, "Shruti", "IT"),
    (105, "Shreyas", "Marketing")]
attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Absent"),
    (105, "2025-03-01", "Present")
]
def mark_attendance(employee_id, date, status):
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")
def search_attendance(employee_id):
    results = [record for record in attendance_records if record[0] == employee_id]
    if results:
        print(f"\nSearching Attendance for Employee ID {employee_id}:")
        for record in results:
            print(f"Date: {record[1]}, Status: {record[2]}")
    else:
        print(f"No attendance records found for Employee ID {employee_id}.")
def display_summary():
    summary = {}
    for emp in employees:
        emp_id = emp[0]
        total_days = sum(1 for record in attendance_records if record[0] == emp_id)
        present_days = sum(1 for record in attendance_records if record[0] == emp_id and record[2] == "Present")
        attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0
        summary[emp_id] = attendance_percentage
    print("\nAttendance Summary:")
    for emp_id, percentage in summary.items():
        emp_name = next(emp[1] for emp in employees if emp[0] == emp_id)
        print(f"{emp_name}: {percentage:.2f}% Present")
mark_attendance(101, "2025-03-02", "Present")
mark_attendance(102, "2025-03-02", "Present")
mark_attendance(103, "2025-03-02", "Absent")
mark_attendance(104, "2025-03-02", "Present")
mark_attendance(105, "2025-03-02", "Present")
search_attendance(104)
display_summary()
