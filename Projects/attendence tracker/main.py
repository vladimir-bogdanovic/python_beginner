import csv
from datetime import datetime

FILE_NAME = "attendance.csv"


def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    except FileExistsError:
        pass


def mark_attendance(name, status):
    date = datetime.now().strftime("%Y-%m-%d")
    with open (FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name , date, status])
    print(f"Attendance marked for {name} as {status} on {date}.")


def view_attendance():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No attendance records found.")

def main():
    initialize_file()
    while True:
        print("\nAttendance Tracker")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            status = input("Enter status (Present/Absent): ")
            mark_attendance(name, status)
        elif choice == "2":
            print("\nAttendance Records:")
            view_attendance()
        elif choice == "3":
            print("Exiting:")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
