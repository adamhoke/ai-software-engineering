### Phase Task:

A "vision and scope" document for a Python Django to-do list application outlines the project's primary goals, target audience, and high-level features, setting boundaries on what the application will and will not achieve. It serves as a foundational reference, ensuring stakeholders have a shared understanding of the project's purpose and limitations.

### LLM Tool:

Since this a high-level document that should be very readable to a less technical audience, using Claude would be the best tool


### Prompt Pattern:

Since this is a document with many sections, the Outline Pattern may be the best choice

### Exact Input:

```
I would like a rough outline of the "Vision and Scope" document for my Django to-do list application. Please outline the technical documentation and include the sections:

- Title page

- Table of contents

- Various sections of the application including:

- A table of common REST API HTTP methods and and their use

- <Placeholder for the rest of the sections>

- Appendix

- A changelog table

Ask me questions if you need any info deciding on sections of the application.
```

### Exact Output:

```
Title Page

Table of Contents

1. Introduction

  - Purpose and scope

  - Definitions, acronyms, and abbreviations

  - References

  - Overview

2. Application Overview

  - User needs

  - Major features

  - Constraints

  - Dependencies

  - Future iterations

3. Functional Requirements

  - User stories

  - Use cases

4. Common REST API Methods

  - Table with HTTP methods (GET, POST, PUT, DELETE etc.) and their typical usage

5. <Placeholder for other sections>

6. Appendix

7. Changelog

  - Table with version number, date, changes
```

### Usage Result:
This provided a simpole vision and scope document outline. We could have easily filled out this outline. For the sake of time and in the interest of experimentation I provided the vision and scope document to Bing Chat and asked it to fill in the details based on similar projects. The reason for this is because Bing Chat has some reasoning ability since it's based on ChatGPT 3.5 and is also internet enabled:
```
Given the following vision and scope document outline, please fill in the details based on similar Python Django projects. Here is the Vision and Scope document:

(Vision and Scope document was pasted here)
```

### File:
`VisionScope.docx`