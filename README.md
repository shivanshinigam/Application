


# Hosting a Python Program as a REST API using Flask / FastAPI and AWS Elastic Beanstalk / Render

---
````bash
# 1. Objective

The purpose of this project is to show how:

- A Python program using NumPy  
- Is converted into a REST API using Flask / FastAPI  
- Is deployed on AWS Elastic Beanstalk  
- Is tested using a public URL  
- Is deleted after use to avoid billing  

An alternate free deployment using Render is also included.

---

# 2. What is Being Built?

We are converting this Python program:

```python
import numpy as np

def calculate(numbers):
    arr = np.array(numbers)
    return {
        "mean": float(arr.mean()),
        "sum": float(arr.sum())
    }

print(calculate([1,2,3]))
````

Into a public web API:

```
POST /calculate
{"numbers": [1,2,3]}
```

Response:

```
{"mean":2.0,"sum":6.0}
```

---

# SECTION A — Building the API using Flask

---

## Step 1: Create Project

Open PyCharm
File → New Project
Name it: numpy_api_project

---

## Step 2: Create application.py

Paste:

```python
from flask import Flask, request, jsonify
import numpy as np

application = Flask(__name__)

def calculate(numbers):
    arr = np.array(numbers)
    return {
        "mean": float(arr.mean()),
        "sum": float(arr.sum())
    }

@application.route("/", methods=["GET"])
def home():
    return "API is running"

@application.route("/calculate", methods=["POST"])
def calculate_api():
    data = request.get_json()
    numbers = data.get("numbers", [])
    return jsonify(calculate(numbers))

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
```

---

## Step 3: Create requirements.txt

```
Flask
numpy
gunicorn
```

---

## Step 4: Test Locally

Run:

```bash
python application.py
```

Visit:

```
http://127.0.0.1:5001
```

---

## Step 5: Test with CURL

```bash
curl -X POST http://127.0.0.1:5001/calculate \
     -H "Content-Type: application/json" \
     -d '{"numbers":[1,2,3]}'
```

---
![Picture1](https://github.com/user-attachments/assets/d1928b19-6236-4910-aaf8-3eb467a0e90f)


# SECTION B — Deploy Using AWS Elastic Beanstalk

---

## Step 6: Zip Project

```bash
zip app.zip application.py requirements.txt
```

---

## Step 7: Login AWS

Search: Elastic Beanstalk
Click Create Application

Fill:

Name: numpy-api
Platform: Python
Upload: app.zip
Preset: Single Instance

Click Create

---

## Step 8: Test Live

```bash
curl -X POST http://AWS_URL/calculate \
     -H "Content-Type: application/json" \
     -d '{"numbers":[10,20]}'
```

Expected:

```
{"mean":15.0,"sum":30.0}
```

---

## Step 9: Delete After Use

Elastic Beanstalk → Actions → Terminate Environment

IMPORTANT: This avoids billing.

---

# SECTION C — Flask, FastAPI & REST

---

## REST API

Programs talk using HTTP and JSON instead of UI.

---

## Flask

A lightweight Python web framework.

---

## FastAPI

Faster, modern, auto-validates inputs.

```python
from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.post("/calculate")
def calculate(nums: list[int]):
    arr = np.array(nums)
    return {"mean": float(arr.mean()), "sum": float(arr.sum())}
```

---

# SECTION D — Deploy for Free using Render

---

## Step 1: Push Code to GitHub

Upload:

* application.py
* requirements.txt

---

## Step 2: Render Setup

Go to:

[https://render.com](https://render.com)

Click:

New → Web Service

Connect GitHub

---

## Step 3: Commands

Build:

```bash
pip install -r requirements.txt
```

Start:

```bash
gunicorn application:application
```

Click Deploy.

Render returns a public URL.

---

# DONE ✅

Python → API → Cloud Deployment → Cleanup implemented.
Link - https://application-2j5j.onrender.com 

Test the API the same way using that URL. 

![Picture2](https://github.com/user-attachments/assets/583d8140-cb6c-4bc7-8c1d-21d8b942f66e)

