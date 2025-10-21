print("=== MULTI-TASK CALCULATOR ===")
print()
client = input("Client name: ")
rate = float(input("Rate per hour: $"))
print()
print("Enter tasks (type 'done' when finished)")
print()
total_hours = 0
tasks = []
while True:
    task_name = input("Task (or 'done'): ")
    if task_name == 'done':
        break
    hours = float(input(" Hours: "))
    total_hours = total_hours + hours
    task_info = {
        'name': task_name,
        'hours': hours,
        'cost' : hours * rate
     }
tasks.append(task_info)
print(f"  Added: {task_name} - {hours} hours")
print()
total_cost = total_hours * rate
print("=" * 50)
print(f"INVOICE FOR: {client}")
print("=" * 50)
print()
for task in tasks:
    print(f"• {task['name']}")
    print(f"  {task['hours']} hours * ${rate}/hour = ${task['cost']:.2f}")
    print()
    print("=" * 50)
print(f"TOTAL HOURS: {total_hours}")
print(f"TOTAL COST: ${total_cost:.2f}")
print("=" * 50)

