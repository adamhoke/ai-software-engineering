### Entities:

1. **User**

    - Attributes: UserID (PK), Username, Password, Email, DateJoined

    - Relationships:

        - Owns many tasks

2. **Task**

    - Attributes: TaskID (PK), TaskName, Description, CreationDate, DueDate, CompletionStatus

    - Relationships:

        - Owned by one user

### Relationships:

1. **Owns**

    - User (1) -----> (M) Task