import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px
import datetime
import storage as storage

# if "tasks" not in st.session_state:
#     st.session_state.tasks = []
    
def show_task():
    st.write("### Tasks")
    if not st.session_state.tasks:
        st.info("No tasks found.")
        return

    category_filter = st.selectbox("Select Category", ["Work", "Personal", "Health", "Other"], key="category_filter_select")
    filtered = [t for t in st.session_state.tasks if t["category"] == category_filter]
    status = st.selectbox("Select Status", ["Completed", "Pending","Due Today","Overdue"], key="status_filter_select")
    if status == "Completed":
        filtered = [t for t in filtered if t["completed"]]
    elif status == "Pending":
        filtered = [t for t in filtered if not t["completed"]]
    elif status == "Due Today":
        from datetime import date
        today_str = str(date.today())
        filtered = [t for t in filtered if t["due_date"] == today_str and not t["completed"]]
    elif status == "Overdue":
        from datetime import date
        today_str = str(date.today())
        filtered = [t for t in filtered if t["due_date"] < today_str and not t["completed"]]

    if not filtered:
        st.warning("No tasks found for this category.")
        return

    df = pd.DataFrame(filtered)
    st.dataframe(df.style.apply(is_task_complted, axis=1))

def plot_chart(df):

    df = get_progress_df(st.session_state.tasks)

    fig = px.pie(
        df,
        values="count",
        names="status",
        title="Progress of Tasks Completion",
        color="status",             # color by status
        color_discrete_map={
            "Completed": "green",
            "Pending": "red"
        }
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)

def get_progress_df(tasks):
    completed_count = sum(t["completed"] for t in tasks)
    pending_count = len(tasks) - completed_count

    data = {
        "status": ["Completed", "Pending"],
        "count": [completed_count, pending_count]
    }

    return pd.DataFrame(data)

def is_task_complted(s):
    return ['background-color: green']*len(s) if s["completed"] else ['background-color: red']*len(s)

def color_survived(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'


def get_new_id(tasks):
    if not tasks:
        return str(datetime.datetime.now().timestamp()).replace('.','')
    return str(datetime.datetime.now().timestamp()).replace('.','')  

def add_task():
    st.write("### Add a New Task")
    # use a key for text_input so value is preserved across reruns until submit
    task_input = st.text_input("Enter Task", key="task_input")
    category = st.selectbox("Select Category", ["Work", "Personal", "Health", "Other"], key="category_select")
    due_date = st.date_input("Select Due Date", key="due_date_input")
    # Submit button
    if st.button("Submit Task", key="submit_task"):
        if task_input and task_input.strip():

            task_obj = {
                "id": get_new_id(st.session_state.tasks),
                "task": task_input,
                "completed": False,
                "category":category,
                "due_date":str(due_date)
            }    

            st.session_state.tasks.append(task_obj)
            storage.save_tasks(st.session_state.tasks)
            st.success("Task added successfully!")
            
            st.session_state.add_mode = False
        else:
            st.error("Please enter a non-empty task")   


def delete_task():
    st.write("### Delete a Task")

    if not st.session_state.tasks:
        st.info("No tasks to delete.")
        st.session_state.delete_mode = False
    else:
        # Show all tasks
        for t in st.session_state.tasks:
            st.write(f"{t['id']}. {t['task']}")

        # Dropdown to choose task
        task_ids = [t["id"] for t in st.session_state.tasks]
        selected_id = st.selectbox("Select Task ID to delete", task_ids)

        if st.button("Confirm Delete"):
            st.session_state.tasks = [
                t for t in st.session_state.tasks if t["id"] != selected_id
            ]
            storage.save_tasks(st.session_state.tasks)
            st.success("Task deleted successfully!")

            st.session_state.delete_mode = False

def mark_as_completed():
    st.write("### Mark Task as Completed")

    if not st.session_state.tasks:
        st.info("No tasks to track.")
        st.session_state.mark_complete_mode = False
    else:
        # Show all tasks
        for t in st.session_state.tasks:
            st.write(f"{t['id']}. {t['task']} - Completed: {t['completed']}")

        # Dropdown to choose task
        task_ids = [t["id"] for t in st.session_state.tasks if not t["completed"]]
        if not task_ids:
            st.info("All tasks are already completed.")
            st.session_state.mark_complete_mode = False
        else:
            selected_id = st.selectbox("Select Task ID to mark as completed", task_ids)

            if st.button("Confirm Mark as Completed"):
                for t in st.session_state.tasks:
                    if t["id"] == selected_id:
                        t["completed"] = True
                        break
                storage.save_tasks(st.session_state.tasks)
                st.success("Task marked as completed!")

                st.session_state.mark_complete_mode = False           

def show_progress():
    st.write("### Task Completion Progress Chart")

    if not st.session_state.tasks:
        st.info("No tasks to show progress.")
    else:
        df = pd.DataFrame(st.session_state.tasks)
        plot_chart(df)                 

def edit_task():
    st.write("### Edit a Task")

    if not st.session_state.tasks:
        st.info("No tasks to edit.")
        st.session_state.edit_mode = False
    else:
        # Show all tasks
        for t in st.session_state.tasks:
            st.write(f"{t['id']}. {t['task']}")

        # Dropdown to choose task
        task_ids = [t["id"] for t in st.session_state.tasks]
        selected_id = st.selectbox("Select Task ID to edit", task_ids)

        new_task_desc = st.text_input("Enter new task description",key="new_task_input")

        if st.button("Confirm Edit"):
            if new_task_desc and new_task_desc.strip():
                for t in st.session_state.tasks:
                    if t["id"] == selected_id:
                        t["task"] = new_task_desc
                        break
                storage.save_tasks(st.session_state.tasks)
                st.success("Task edited successfully!")
                st.session_state.edit_mode = False
            else:
                st.error("Please enter a non-empty task description")        


