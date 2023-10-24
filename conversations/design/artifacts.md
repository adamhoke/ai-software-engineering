### Phase Task:

A flow diagram in the context of a software engineering project is a graphical representation that depicts the sequence of operations, data flow, or activities in a system or process.

### LLM Tool:

ChatGPT-4 since this is the only tool that can come close to this type of task.

### Prompt Pattern:

PQD, since LLMs can’t actually build visual flow diagrams, we will generate the code for the flow diagram in a format called Mermaid. So this is actually a new code design exercise.

### Exact Input:

```
You are an expert python programmer. You are working on a Django web application with a Postgres backend. This is a to-do list application. You can reference the project from the Vision and Scope document at the end of the prompt.

I want you to create a flow diagram that includes all aspects of the flow of the application including any high-level DJango functionality

The diagram must be returned in "Mermaid format so it can be import into the open source Drawio application. Please include comments about the justification for the flow design.

Here is the original Vision and Scope Document for the project:

(Paste contents of Viision and Scope document here.)
```

### Exact Output:

The Mermaid document:

```
graph TD

A[User] --> B[Web Frontend: Django Views & Templates]

subgraph Django Web Application

B --> C[URL Dispatcher]

C --> D[View Functions]

D --> |GET| E1[Retrieve Task/List]

D --> |POST| E2[Create Task]

D --> |PUT| E3[Update Task]

D --> |DELETE| E4[Delete Task]

end

subgraph Django ORM

E1 --> F1[QuerySet: Filter & Retrieve from DB]

E2 --> F2[Model: Create New Task]

E3 --> F3[Model: Update Existing Task]

E4 --> F4[Model: Delete Task]

end

subgraph PostgreSQL Database

F1 --> G1[Tasks Table]

F2 --> G1

F3 --> G1

F4 --> G1

end
```

ChatGPT-4's remarks:

```
%% Comments:

%% 1. User interacts with the web frontend built using Django's views and templates.

%% 2. Django's URL Dispatcher routes the request to the appropriate view function based on the URL.

%% 3. View functions handle the web request. They can retrieve, create, update, or delete data based on the request type.

%% 4. Django ORM (Object-Relational Mapping) is used to interact with the database in an object-oriented manner.

%% 5. PostgreSQL Database contains the tasks table where all the to-do list tasks are stored.

%% 6. Depending on the action (GET, POST, PUT, DELETE), the application interacts with the database to perform the desired operation.
```

### Usage Result:

What's great about the Mermaid format is that it can be rendered into a visual graph by any number of free tools designed specifically for Mermaid. It can also be imported into the popular draw.io diagramming tool and saved in draw.io format.

### File:

`FlowDiagram.mmd`

---------------------------------------------------------------------------------------
### Phase Task:

An Entity-Relationship Diagram (ERD) is a graphical representation that depicts the relationships between entities within a database in software engineering.

### LLM Tool:

As mentioned, LLM AI tools don’t support creating visual diagrams (yet). So what we’ll have to create is an Entity-Relationship _Document_ instead.

### Prompt Pattern:

This would probably be the persona pattern. The tactic we will try is the persona pattern with the Mermaid code from the flow diagram as a reference, pasted into ChatGPT-4.

### Exact Input:

```
Act as a professional database architect. You are working on creating the ERD for the project. Using a descriptive outline, show me how map out the ERD diagram. This will eventually be transferred to a ERD diagram using a diagramming tool. You can base your design off the Mermaid flow diagram code at the end of this prompt. Also, Suggest a better version of the application flow if it is not feasible for your ERD design.

Here is the Mermaid application flow diagram code:

(Paste Mermaid code from FlowDiagram.mmd here.)
```

### Exact Output:

Descriptive ERD Outline:

```
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
```

ChatGPT-4's enhanced application flow:

```
### Enhanced Application Flow:

graph TD

A[User] --> B[Web Frontend: Django Views & Templates]

subgraph Django Web Application

B --> C[URL Dispatcher]

C --> D[View Functions]

D --> |GET| E1[Retrieve User Info/Task List]

D --> |GET| E5[Retrieve Specific Task]

D --> |POST| E2[Create Task]

D --> |PUT| E3[Update Task]

D --> |DELETE| E4[Delete Task]

end

subgraph Django ORM

E1 --> F1[QuerySet: Filter & Retrieve User Info/Task List from DB]

E5 --> F5[QuerySet: Filter & Retrieve Specific Task from DB]

E2 --> F2[Model: Create New Task]

E3 --> F3[Model: Update Existing Task]

E4 --> F4[Model: Delete Task]

end

subgraph PostgreSQL Database

F1 --> G1[Users Table]

F1 --> G2[Tasks Table]

F5 --> G2

F2 --> G2

F3 --> G2

F4 --> G2

end
```

ChatGPT-4's remarks:

```
%% Comments:

%% 1. User interacts with the web frontend built using Django's views and templates.

%% 2. Django's URL Dispatcher routes the request to the appropriate view function based on the URL.

%% 3. View functions handle the web request. They can retrieve user info, specific tasks, or the whole task list, and can also create, update, or delete tasks based on the request type.

%% 4. Django ORM (Object-Relational Mapping) is used to interact with the database in an object-oriented manner.

%% 5. PostgreSQL Database contains the users table for user info and the tasks table where all the to-do list tasks are stored.

%% 6. Depending on the action (GET, POST, PUT, DELETE), the application interacts with the database to perform the desired operation.

Improvements:

1. **Introduced "Retrieve Specific Task" flow**. This allows a more granular operation of fetching a specific task rather than always fetching the whole list.

2. **Added "Users Table" in the PostgreSQL Database**. This will store user-specific information, allowing for individual user accounts and personal task lists.
```

### File:

`ERDDesign.md`
