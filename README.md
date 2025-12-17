# 📝 Daily Task Tracker Application

### Project Overview

**What problem this app solves**

Managing daily tasks often becomes messy when users rely on scattered notes, reminders, or tools that are either too complex or overkill for personal use. This application solves the problem of simple, structured, and trackable task management with a clear visual overview of progress.

**It allows users to:**

* Create and manage tasks easily
* Organize tasks by category
* Track completion status
* Visualize progress in a simple dashboard
* Persist tasks across sessions without external dependencies

**Why this project was built**

**This project was built to:**

* Understand state-driven UI development using Streamlit
* Practice application architecture (UI, logic, analytics, storage separation)
* Demonstrate end-to-end ownership of a small but complete product
* Avoid unnecessary complexity (no backend server required)
* The goal was to build something simple, reliable, and explainable in interviews rather than a framework-heavy solution.

**Features**

* Task Management (CRUD)
* Add new tasks
* View all tasks
* Delete tasks
* Update task completion status

**Categories**

* Tasks can be grouped into categories (Work, Personal, Health, Other)
* Category-based filtering for focused viewing
* Due Dates
* Each task can have an optional due date
* Enables better planning and prioritization
* Status Tracking
* Tasks can be marked as completed or pending
* Completion state is stored persistently

**Filters**

**Filter tasks by:**

* Category
* Completion status
* Dashboard Metrics
* Total number of tasks
* Completed tasks
* Pending tasks

**Progress Visualization**

**Pie chart visualization of:**

* Completed vs Pending tasks

**Visual feedback:**

* Red when no tasks are completed
* Green slice appears as tasks get completed

**Persistent Storage**

* All tasks are stored locally using JSON
* Data persists across app restarts without a database

**Architecture (IMPORTANT)**

This application is intentionally designed with clear separation of responsibilities, which is critical for maintainability and interview discussions.

**Why Streamlit**

* Streamlit allows rapid UI development with minimal boilerplate
* Ideal for state-driven apps and dashboards
* No need for frontend frameworks or REST APIs
* Perfect for prototyping and small-to-medium tools

**Why JSON Storage**

* Eliminates the need for a database during early development
* Human-readable and easy to debug
* Suitable for low-volume, single-user task data
* Keeps the architecture simple and portable

#### (Designed so it can be easily replaced with MySQL later.)

**How st.session_state is used**

#### Streamlit reruns the entire script on every interaction.

**To handle this:**

#### st.session_state is used as the single source of truth during runtime

**It stores:**

**Task list**

* Current UI mode (add / show / delete / track)
* Filter selections
* Prevents UI flickering and loss of data on reruns
* Enables controlled UI rendering based on active state
* Separation of Concerns

**The codebase is logically separated into:**

**UI Layer**

* Streamlit components (buttons, inputs, tables, charts)
* Handles user interaction and rendering

**Logic Layer**

* Task creation, deletion, filtering
* ID generation
* Status updates
* Analytics Layer
* Task statistics
* Progress calculations
* Data preparation for charts

**Storage Layer**

* JSON read/write operations
* Ensures persistence outside runtime memory

**This structure ensures:**

* Readable code
* Easy debugging
* Clear explanation during interviews
* Smooth future migration to a database-backed system

**How to Run Locally**

**Python Version**

Python 3.9+ recommended

**Install Dependencies**

#### ``` pip install -r requirements.txt```

**Run the Application**

#### ```streamlit run dashboard.py```

**The app will open automatically in your browser.**

**Future Improvements**

* Replace JSON with MySQL/PostgreSQL
* Multi-user authentication
* Task reminders and notifications
* Cloud deployment
* Mobile-friendly UI

**Interview Tip**

**This project demonstrates:**

* State management
* UI-driven architecture
* Clean separation of logic
* Practical decision-making

**It is intentionally simple — and that’s the strength.**