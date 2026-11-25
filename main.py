from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

tasks = {}
next_task_id = 1

@app.get("/")
def root():
    return {"message": "Hello, DevOps!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/tasks")
def add_task(task: Task):
    global next_task_id

    tasks[next_task_id] = task.model_dump()
    next_task_id += 1

    return {"id": next_task_id - 1, **tasks[next_task_id - 1]}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task ID not found")

    tasks[task_id] = task.model_dump()

    return {"id": task_id, **tasks[task_id]}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task ID not found")

    tasks.pop(task_id)

    return {"message": "Task deleted successfully"}
