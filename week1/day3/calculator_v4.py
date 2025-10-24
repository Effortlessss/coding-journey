import json
from datetime import datetime


def get_positive_number(prompt, max_value=10000):
    """
    Get a positive number from user.
    Keeps asking until valid.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(" X Must be greater then zero! X")
                continue
            if value > max_value:
                print(" X Be realistic... X")
                continue
            return value
        except ValueError:
            print(" X Must be a number... X")


def get_text(prompt):
    """
    Get non-empty text from user.
    """
    while True:
        text = input(prompt).strip()
        if len(text) == 0:
            print("X Can't be left empty! X")
            continue
        return text


print("=" * 60)
print("BULLETPROOF CALCULATOR V3")
print("=" * 60)
print()
client = get_text("Client name: ")
rate = get_positive_number("Hourly rate: $", max_value=5000)
print()
print("Enter task (type 'done' when finished)")
print()
total_hours = 0
tasks = []
while True:
    task_name = input("Task name (or 'done'): ").strip()

    if len(task_name) == 0:
        print("  ❌ Task name can't be empty!")
        continue

    if task_name.lower() == "done":
        if len(tasks) == 0:
            print("  ⚠️  Add at least one task!")
            continue
        break

    hours = get_positive_number("  Hours: ", max_value=24)

    total_hours += hours
    task_info = {"name": task_name, "hours": hours, "cost": hours * rate}
    tasks.append(task_info)
    print(f"  ✅ Added: {task_name} - {hours} hours")
    print()
total_cost = total_hours * rate
print()
print("=" * 60)
print(f"INVOICE FOR: {client.upper()}")
print("=" * 60)
print()
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task['name']}")
    print(f"   {task['hours']} hours × ${rate:.2f}/hour = ${task['cost']:.2f}")
    print()

print("=" * 60)
print(f"TOTAL HOURS: {total_hours:.2f}")
print(f"TOTAL COST: ${total_cost:.2f}")
print("=" * 60)
print()
print("✅ Invoice complete! Ready to send.")
print()
save = input("Save this invoice (y/n): ").strip().lower()
if save == "y":
    # Create invoice data structure
    invoice = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "client": client,
        "rate": rate,
        "tasks": tasks,
        "total_hours": total_hours,
        "total_cost": total_cost,
    }

    filename = f"invoice_{client.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as file:
        json.dump(invoice, file, indent=2)

    print(f"✅ Invoice saved as: {filename}")
else:
    print("Invoice not saved.")
