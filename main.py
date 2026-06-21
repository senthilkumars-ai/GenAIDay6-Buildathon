from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# -------------------------
# Database Connection
# -------------------------
conn = sqlite3.connect(
    "leave_management.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS leave_requests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    leave_type TEXT,
    start_date TEXT,
    end_date TEXT,
    reason TEXT,
    status TEXT
)
""")

conn.commit()


# -------------------------
# Model
# -------------------------
class Leave(BaseModel):
    employee_name: str
    leave_type: str
    start_date: str
    end_date: str
    reason: str


# -------------------------
# Apply Leave
# -------------------------
@app.post("/apply-leave")
def apply_leave(data: Leave):

    cursor.execute(
        """
        INSERT INTO leave_requests
        (
            employee_name,
            leave_type,
            start_date,
            end_date,
            reason,
            status
        )
        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        (
            data.employee_name,
            data.leave_type,
            data.start_date,
            data.end_date,
            data.reason,
            "Pending"
        )
    )

    conn.commit()

    return {
        "message": "Leave Applied"
    }


# -------------------------
# View History
# -------------------------
@app.get("/leave-history")
def history():

    cursor.execute(
        "SELECT * FROM leave_requests"
    )

    rows = cursor.fetchall()

    return rows


# -------------------------
# Approve Leave
# -------------------------
@app.put("/approve/{leave_id}")
def approve(leave_id: int):

    cursor.execute(
        """
        UPDATE leave_requests
        SET status='Approved'
        WHERE id=?
        """,
        (leave_id,)
    )

    conn.commit()

    return {
        "message": "Approved"
    }


# -------------------------
# Reject Leave
# -------------------------
@app.put("/reject/{leave_id}")
def reject(leave_id: int):

    cursor.execute(
        """
        UPDATE leave_requests
        SET status='Rejected'
        WHERE id=?
        """,
        (leave_id,)
    )

    conn.commit()

    return {
        "message": "Rejected"
    }