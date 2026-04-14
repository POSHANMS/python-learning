# Match-case Statement

# Problem 1: Assign grade

grade = input("Enter your grade(A/B/C: " ).upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Better")
    case _:
        print("Fail")

# Problem 2: Activity Suggestion based on weather condition

weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

match weather:
    case "sunny":
        print("Great day for a picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Perfect time for a walk.")
    case "snowy":
        print("Build a snowman or go skiing!")
    case _:
        print("Unknown weather condition.")

# Problem 3: Mobile notification settings based on user profile mode

mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()

match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")