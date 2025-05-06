# TO-DO

A previously developed project, reused here to apply the concept of modularization, with its functions separated and organized hierarchically.

## What is this project about?

> *Note:* This project reuses an earlier version of a task manager application, now restructured using modularization principles. The goal is to organize code by separating responsibilities into distinct files, improving clarity, reusability, and scalability.

### Tree

> *Note:* Below is the folder structure of the project, illustrating the modular approach:

`projeto_tarefas/  
├── main.py         # The kernel of the program, responsible for initializing and coordinating function calls  
├── tarefas.py      # Core functions such as add, list, complete tasks  
├── utils.py        # Auxiliary functions (e.g., generating unique IDs)  
├── tarefas.json    # Simulated non-relational database  
└── README.md`

### main.py

> *Note:* Acts as the main script (kernel) of the program. It starts the execution and coordinates calls to the appropriate modules, creating a "domino effect" in the system's workflow.

### utils.py

> *Note:* Contains supporting functions that are not the core logic, but are essential to the system's functionality. Future enhancements and extra utilities are expected to be added here.

### tarefas.py

> *Note:* Holds all the core business logic. It can be seen as the sub-kernel of the application.

### tarefas.json

> *Note:* Serves as a simple non-relational database. A more complex implementation could be used, but a JSON file suffices for demonstration and learning purposes.

