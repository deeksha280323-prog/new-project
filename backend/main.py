from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def root():
    return {"message": "Task Manager API Running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        tasks.pop(task_id)
        return {"message": "Task deleted"}
    return {"error": "Task not found"}