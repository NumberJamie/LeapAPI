from fastapi import FastAPI
import random

print(random.randint(0,9))

app = FastAPI()


FIRST_NAMES = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Julia"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]


@app.get('/users/{user_id}')
def get_user(user_id: str):
    first_name, last_name = random.choice(FIRST_NAMES), random.choice(LAST_NAMES)
    username = f'{first_name} {last_name}'
    display_name = f'{first_name}{last_name[0]}'.lower()
    return {
        "username": username,
        "displayName": display_name,
    }
