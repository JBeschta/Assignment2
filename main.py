"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (SEMESTERS_PER_YEAR * credits)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER * (credits / CS1430_CREDITS))

def cost_of_skipped_classes(annual_cost, credits, skipped_count):
    """Give back the total cost of skipped classes."""
    per_class = cost_per_class(annual_cost, credits)
    return per_class * skipped_count


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter your annual cost of attendance: $"))
    credits = int(input("Enter the number of credits you are enrolled in: "))

    while True:
        print("\nTHE COST OF COLLEGE")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost of skipped classes")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            print("Thanks for using!")
            break
        elif choice == "1":
            semester_cost = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${semester_cost:.2f}")
        elif choice == "2":
            month_cost = cost_per_month(annual_cost)
            print(f"Cost per month: ${month_cost:.2f}")
        elif choice == "3":
            day_cost = cost_per_day(annual_cost)
            print(f"Cost per day: ${day_cost:.2f}")
        elif choice == "4":
            credit_cost = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${credit_cost:.2f}")
        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"Cost per class: ${class_cost:.2f}")
        elif choice == "6":
            skipped_count = int(input("Enter the number of classes you skipped: "))
            total_skipped_cost = cost_of_skipped_classes(annual_cost, credits, skipped_count)
            print(f"Total cost of skipped classes: ${total_skipped_cost:.2f}")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
