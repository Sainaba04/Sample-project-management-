def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Student Grade Calculator")
    n = int(input("Enter number of subjects: "))
    total = 0
    for i in range(n):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total += marks
    average = total / n
    grade = calculate_grade(average)
    print(f"\nAverage: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
  Added grade_calculator.py with core logic  (Fixes #2)
Updated README with usage instructions (Fixes #3)
Performed testing and fixed input bug (Fixes #4)
