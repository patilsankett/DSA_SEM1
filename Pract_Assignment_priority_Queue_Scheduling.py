class PriorityQueue:

    def __init__(self):
        self.queue = []

    # 1. Add Process
    def enqueue(self, pid, name, priority):

        if priority < 1 or priority > 4:
            print("Invalid Priority!")
            return

        self.queue.append([pid, name, priority])
        self.queue.sort(key=lambda x: x[2])

        print("Process Added Successfully!")

    # 2. Execute Process
    def dequeue(self):

        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            process = self.queue.pop(0)
            print("Executed Process:", process)

    # 3. View Next Process
    def display_next(self):

        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            print("Next Process:", self.queue[0])

    # 4. Display All Processes
    def display_all(self):

        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            print("Pending Processes:")
            for process in self.queue:
                print(process)

    # 5. Count Processes
    def count(self):

        print("Total Processes:", len(self.queue))


# main program
pq = PriorityQueue()

while True:

    print("\n--- CPU PROCESS SCHEDULING ---")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        pid = int(input("Enter Process ID: "))
        name = input("Enter Process Name: ")
        priority = int(input("Enter Priority (1-4): "))

        pq.enqueue(pid, name, priority)

    elif choice == 2:
        pq.dequeue()

    elif choice == 3:
        pq.display_next()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        pq.count()

    elif choice == 6:
        print("Program Terminated!")
        break

    else:
        print("Invalid Choice!")