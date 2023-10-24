### Phase Task:

A project plan document for a Python Django to-do list application provides a detailed roadmap, outlining the tasks, timelines, resources, and milestones required to develop and deploy the application. It serves as a blueprint for the project, guiding the development team and stakeholders through each phase of the software lifecycle.

### LLM Tool:

Even though this is a document, this is a more complex thought task, so using ChatGPT-4 may be a better idea

### Prompt Pattern:

The template pattern would also work here if we had a template of a project plan to pass in. However the Persona pattern seems like the best choice. What we will do is pass in the completed “Vision and Scope” document and reference it using the below prompt

### Exact Input:

```
Act as a professional project manager. You are working a new software project to make a TODO list application. Show me how to plan the project and then display the full project plan. This will be used in the engineering team's agile process. You can use the following "Vision and Scope" document to plan out the project timeline:

(Paste Vision and Scope document contents here.)
```

### Exact Output:

```
### 2. Key Stakeholders:

- **Product Owner:** [Name]

- **Scrum Master:** [Name]

- **Development Team:** [List of developers]

### 3. Sprints and Milestones:

#### Sprint 1: Design and Setup (2 weeks)

- **Goal:** Design the user interface and set up the development environment.

- Task 1.1: Design mockups for the application.

- Task 1.2: Set up the Django development environment.

- Task 1.3: Set up version control (e.g., Git).

#### Sprint 2: Core Features Development (3 weeks)

- **Goal:** Implement task creation, editing, and deletion.

- Task 2.1: Implement the 'Create a new task' feature.

- Task 2.2: Implement the 'Edit an existing task' feature.

- Task 2.3: Implement the 'Delete a task' feature.

#### Sprint 3: Advanced Features Development (3 weeks)

- **Goal:** Implement advanced features like task assignment, categorization, and due dates.

- Task 3.1: Implement 'Assign a task to a category or project' feature.

- Task 3.2: Implement 'View tasks by category or project' feature.

- Task 3.3: Implement 'Set due dates for tasks' feature.

#### Sprint 4: Additional Features and Testing (2 weeks)

- **Goal:** Implement task completion tracking and conduct initial testing.

- Task 4.1: Implement 'Mark tasks as complete' feature.

- Task 4.2: Start initial testing and debugging.

#### Sprint 5: Testing, Debugging, and Documentation (2 weeks)

- **Goal:** Complete testing, address any bugs, and finalize documentation.

- Task 5.1: Complete thorough testing.

- Task 5.2: Debug identified issues.

- Task 5.3: Finalize documentation and user manuals.

#### Sprint 6: Deployment and Feedback (1 week)

- **Goal:** Deploy the application and gather initial user feedback.

- Task 6.1: Deploy the Django application.

- Task 6.2: Collect user feedback.

- Task 6.3: Make necessary quick fixes based on feedback.

### 4. Dependencies:

- Django Framework

- Database (e.g., PostgreSQL, SQLite)

- Front-end libraries (e.g., Bootstrap)

- Version Control (e.g., Git)

### 5. Risks and Mitigation:

- **Risk:** Scope creep - Introduction of features not initially agreed upon.

- **Mitigation:** Any new features will be considered for future iterations.

- **Risk:** Technical challenges with Django.

- **Mitigation:** Provide additional training or resources as needed. Consider consultation with Django experts.

### 6. Review and Retrospective:

After each sprint, conduct a review to demo the sprint's outcomes and a retrospective to analyze the sprint process and identify areas of improvement.

### 7. Communication:

- **Daily Scrum Meetings:** 15 minutes, every day.

- **Sprint Review:** End of each sprint.

- **Sprint Retrospective:** After every sprint review.

- **Sprint Planning:** Beginning of each sprint.

### 8. Tools:

- **Project Management:** Jira, Trello, or Asana

- **Version Control:** Git (with GitHub, GitLab, or Bitbucket)

- **Communication:** Slack, Teams, or Discord

- **Documentation:** Confluence or Google Docs

### 9. Approval:

Once the project plan is agreed upon by key stakeholders, obtain their approval to proceed.
```

### Usage Result:

This result can be saved to a markdown document, however another trick to leverage the LLM is to import it into Excel since most project managers don't use markdown documents for planning. In ChatGPT-4:

```
Can you convert that plan into a format that could be imported into Microsoft Excel?
```

### File:
`ProjectPlan.xlsx`

---------------------------------------------------------------------------------------
### Phase Task:

A backlog comprises prioritized tasks and user stories that detail desired features or improvements, which are then visualized on a Scrum board for team collaboration and sprint planning. The input will consist of a persona and reference the Task Division list created out of the options presented to us in the intelligent feedback exercise in this phase (see intelligent_feedback.md in this directory)

### LLM Tool:

ChatGPT-4 since complex reasoning is required

### Prompt Pattern:

Template Pattern. We want these in a similar format we can copy/paste into something like an agile project management tool.

### Exact Input:

```
Act as a software engineer on a team of engineers that use the scrum methodology. Assign a point value and estimated length of time for each task in the task division list below. The results should be in the format
|Sprint #|Task Name|Estimated Scrum Points|Estimated time (in days)|

Order the results by Sprint #

Here is the task division list:

Feature-Based Task Division:

(Paste task division list from intelligent feedback exercise here).
```

### Exact Output:

```
|Sprint #|Task Name|Estimated Scrum Points|Estimated time (in days)|

|-------|-------|-------|-------|

|Sprint 1|Design mockups for the application|3|2|

|Sprint 1|Set up the Django development environment|5|3|

|Sprint 1|Set up version control (e.g., Git)|2|1|

|Sprint 2|Implement the 'Create a new task' feature|5|3|

|Sprint 2|Implement the 'Edit an existing task' feature|5|3|

|Sprint 2|Implement the 'Delete a task' feature|4|2|

|Sprint 3|Implement 'Assign a task to a category or project' feature|5|3|

|Sprint 3|Implement 'View tasks by category or project' feature|4|2|

|Sprint 3|Implement 'Set due dates for tasks' feature|3|2|

|Sprint 4|Implement 'Mark tasks as complete' feature|4|2|

|Sprint 4|Start initial testing and debugging|8|4|

|Sprint 5|Complete thorough testing (collaboration with the full-time senior developer)|8|4|

|Sprint 5|Debug identified issues|7|4|

|Sprint 5|Draft initial documentation and user manuals|4|2|

|Sprint 6|Assist in deploying the Django application|5|3|

|Sprint 6|Collect user feedback|3|2|

|Sprint 6|Make necessary quick fixes based on feedback|6|3|
```

### Usage Result:

This can be saved as a markdown file and later inpput into an agile PM tool.


### File:
`ScrumEstimations.md`