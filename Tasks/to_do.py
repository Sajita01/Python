tasks = []
#Add tasks
task = input("Add a task (or 'done'):")

while task != "done":
    tasks.append(task)
    task = input("Add a task (or 'done'):")

#Numbering tasks
count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1

#let the user remove a task by number using pop
remove_task = int(input("Enter task number to remove: "))
tasks.pop(remove_task - 1)

 # Display remaining tasks
print("\nRemaining tasks:")
count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1
    