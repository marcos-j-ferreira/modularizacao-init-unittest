# modularizacao-init-unittest

Important concepts in Python that apply to many other areas of programming.

## What is *modularização*?

> *Note:* Consists of separating functions into different files instead of having everything packed into a single file (commonly known as a **"monolith"**). The idea is to keep everything well-structured and organized, which improves maintainability, scalability, and facilitates future enhancements.

### Tree

> *Note:* As an example, we have the following project structure (purely illustrative):

```
projeto_tarefas/
├── main.py         # This is the kernel of the system, where everything is well organized and functions are called.
├── tarefas.py      # Functions such as add, list, complete tasks
├── utils.py        # Auxiliary functions (e.g., generate ID)
├── tarefas.json    # Database
└── README.md
```

### Purpose

> *Note:* My main goal is to acquire this knowledge for future and larger projects, so I can understand and apply good organization. It is also worth noting that modularization applies to many other technologies beyond Python.
