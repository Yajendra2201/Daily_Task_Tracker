import pandas as pd

def get_total_task(tasks):
    return len(tasks)
def completed_task(tasks):
    return sum(t['completed'] for t in tasks)
def pending_task(tasks):
    return len(tasks) - sum(t['completed'] for t in tasks)
def overdue_task(tasks):
    return sum(1 for t in tasks if not t['completed'] and t['due_date'] < str(pd.Timestamp('today').date()))    
def due_today_task(tasks):  
    return sum(1 for t in tasks if not t['completed'] and t['due_date'] == str(pd.Timestamp('today').date()))        
