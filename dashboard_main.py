import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px
import task_manager as tm
import analytics as an
import storage as storage

st.set_page_config(page_title="Daily Task Tracker", layout="centered")

st.title("Daily Task Tracker Application")

if "tasks" not in st.session_state:
    st.session_state.tasks = storage.load_data()

def dashboard():
  
    tasks = st.session_state.tasks
    col1, col2, col3,col4,col5 = st.columns(5)
    col1.metric("Total Tasks", an.get_total_task(tasks),delta_color="normal",delta = an.get_total_task(tasks))
    col2.metric("Completed Tasks", an.completed_task(tasks),delta_color="normal",delta = an.completed_task(tasks))
    col3.metric("Pending Tasks", an.pending_task(tasks),delta_color="normal",delta = an.pending_task(tasks))
    col4.metric("Overdue Tasks", an.overdue_task(tasks),delta_color="normal",delta = an.overdue_task(tasks))
    col5.metric("Tasks Due Today", an.due_today_task(tasks),delta_color="normal",delta = an.due_today_task(tasks))

    st.write("## Welcome to the Daily Task Tracker Application!")
    st.write("""
    This application helps you manage your daily tasks efficiently.
    
    ### Features:
    - **Add Tasks**: Input your tasks along with categories and due dates.
    - **View Tasks**: Display all your tasks with filtering options.
    - **Delete Tasks**: Remove tasks that are no longer needed.
    - **Track Progress**: Mark tasks as completed and visualize your progress with charts.
    - **Edit Tasks**: Modify existing tasks as needed.
    
    ### How to Use:
    1. Click on the "Add Task" button to create a new task.
    2. Use the "Show Tasks list" button to view and filter your tasks.
    3. Select "Delete Task" to remove any task.
    4. Use "Track Task Progress" to mark tasks as completed.
    5. Click on "Show Progress Chart" to see a visual representation of your task completion status.
    6. Use "Edit a task" to update any task details.
    
    Start managing your tasks effectively today!
    """)               

st.sidebar.header("Actions")                

page = st.sidebar.radio("Select Action", 
                        ("Dashboard", "Add Task", "Show Tasks list", "Delete Task", 
                         "Track Task Progress", "Show Progress Chart", "Edit a task"))

if page=="Dashboard":
    dashboard()                         

if page=="Add Task":
    tm.add_task()

if page=="Show Tasks list":
    tm.show_task()

if page=="Delete Task":
    tm.delete_task()    

if page=="Track Task Progress":
    tm.mark_as_completed() 

if page=="Show Progress Chart":
    tm.show_progress()                    