from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import get_connection
from gemini_service import generate_sql, format_answer

app = FastAPI()

# Serve Frontend Files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Branch Mapping
BRANCH_MAPPING = {
    "CSE(AI)": "Computer Science And Engineering (Artificial Intelligence)",
    "CSE(AIML)": "Computer Science And Engineering (Artificial Intelligence And Machine Learning)",
    "CSE(DS)": "Computer Science And Engineering (Data Science)",
    "CSE(CYBER)": "Computer Science And Engineering (Cyber Security)",
    "CSE(IOT)": "Computer Science And Engineering (Internet Of Things)",
    "CSE": "Computer Science And Engineering",
    "ECE": "Electronics And Communication Engineering",
    "EEE": "Electrical And Electronics Engineering",
    "EE": "Electrical Engineering",
    "IT": "Information Technology",
    "ME": "Mechanical Engineering",
    "CE": "Civil Engineering"
}


def normalize_question(question):

    q = question

    for short_name, full_name in BRANCH_MAPPING.items():
        q = q.replace(short_name, full_name)

    return q


@app.get("/tables")
def tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]

    cursor.close()
    conn.close()

    return {
        "tables": tables
    }


def get_schema():

    conn = get_connection()
    cursor = conn.cursor()

    schema = ""

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for table in tables:

        table_name = table[0]

        schema += f"\nTable: {table_name}\nColumns:\n"

        cursor.execute(f"DESCRIBE {table_name}")

        columns = cursor.fetchall()

        for column in columns:
            schema += f"{column[0]}\n"

        schema += "\n"

    cursor.close()
    conn.close()

    return schema


class Question(BaseModel):
    question: str


@app.post("/chat")
def chat(data: Question):

    try:

        question = normalize_question(
            data.question
        )

        # Special handling for hostel bed questions
        if (
            "hostel bed" in question.lower()
            or "hostel beds" in question.lower()
        ):

            sql_query = """
            SELECT
            SUM(bed_capacity_of_boys_hostel_in_number)
            +
            SUM(bed_capacity_of_girls_hostel_in_number)
            AS total_beds
            FROM number_of_available_hostel_and_beds_district_wise
            """

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(sql_query)

            result = cursor.fetchall()

            cursor.close()
            conn.close()

            total_beds = (
                result[0][0]
                if result and result[0][0] is not None
                else 0
            )

            return {
                "question": data.question,
                "answer": f"The total number of hostel beds in Bihar is {total_beds}.",
                "sql_query": sql_query
            }

        # Gemini SQL Generation
        schema = get_schema()

        sql_query = generate_sql(
            question,
            schema
        )

        sql_query = sql_query.replace(
            "```sql",
            ""
        )

        sql_query = sql_query.replace(
            "```",
            ""
        )

        sql_query = sql_query.strip()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql_query)

        result = cursor.fetchall()

        cursor.close()
        conn.close()

        answer = format_answer(
            question,
            result
        )

        return {
            "question": data.question,
            "answer": answer,
            "sql_query": sql_query
        }

    except Exception as e:

        return {
            "error": str(e)
        }