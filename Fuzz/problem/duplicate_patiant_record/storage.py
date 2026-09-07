patients = [
    {"id": 1, "name": "Rahul Kumar", "phone": "9835743740", "age": 34},
    {"id": 2, "name": "Rahul  Kumar", "phone": "9835743740", "age": 34},       # extra space, same person
    {"id": 3, "name": "Rahul Kumr", "phone": "9835743740", "age": 34},        # typo, same person
    {"id": 4, "name": "RAHUL KUMAR", "phone": "9835743740", "age": 34},       # case diff, same person
    {"id": 5, "name": "R. Kumar", "phone": "9835743740", "age": 34},          # abbreviated, same person

    {"id": 6, "name": "Rakul Kumar", "phone": "9123456780", "age": 29},       # DIFFERENT person, similar name
    {"id": 7, "name": "Rahul Kumar Sahoo", "phone": "9988776655", "age": 41}, # DIFFERENT person, superstring name

    {"id": 8, "name": "Priya Sharma", "phone": "9776655443", "age": 27},
    {"id": 9, "name": "Priya Sharmaa", "phone": "9776655443", "age": 27},     # typo, same person
    {"id": 10, "name": "Priya S.", "phone": "9776655443", "age": 27},         # abbreviated, same person
    {"id": 11, "name": "Preeti Sharma", "phone": "9012345678", "age": 33},    # DIFFERENT person, similar name

    {"id": 12, "name": "Anil Mohanty", "phone": "8877665544", "age": 52},
    {"id": 13, "name": "Anil  Mohanty ", "phone": "8877665544", "age": 52},   # trailing/extra spaces
    {"id": 14, "name": "anil mohanty", "phone": "8877665544", "age": 52},     # lowercase, same person

    {"id": 15, "name": "Sunita Devi", "phone": "7788990011", "age": 45},
    {"id": 16, "name": "Sunita Devi", "phone": "7788990012", "age": 45},      # SAME name, DIFFERENT phone — ambiguous case!

    {"id": 17, "name": "Mohan Das", "phone": "9090909090", "age": 60},
    {"id": 18, "name": "Mohon Das", "phone": "9090909090", "age": 60},        # typo, same person
]