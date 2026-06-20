from google import genai

client = genai.Client(
    api_key="GEMINI_API_KEY"
)


def generate_sql(question, schema):

    prompt = f"""
You are a MySQL expert.

Database Schema:
{schema}

User Question:
{question}

Branch Name Mappings:

CSE = Computer Science And Engineering
CS = Computer Science And Engineering

CSE(AI) = Computer Science And Engineering (Artificial Intelligence)
CSE(AIML) = Computer Science And Engineering (Artificial Intelligence And Machine Learning)
CSE(DS) = Computer Science And Engineering (Data Science)
CSE(CYBER) = Computer Science And Engineering (Cyber Security)
CSE(IOT) = Computer Science And Engineering (Internet Of Things)

ECE = Electronics And Communication Engineering
EEE = Electrical And Electronics Engineering
EE = Electrical Engineering
IT = Information Technology
ME = Mechanical Engineering
CE = Civil Engineering

Important Rules:

1. Use exact table names from schema.
2. Use exact column names from schema.
3. Use exact branch names from database.
4. Never use abbreviations in SQL query.
5. Return only SQL query.
6. Do not explain anything.
7. Do not use markdown.

Hostel Data Rules:

Table:
number_of_available_hostel_and_beds_district_wise

Total hostel beds =
SUM(bed_capacity_of_boys_hostel_in_number)
+
SUM(bed_capacity_of_girls_hostel_in_number)

Total boys hostel beds =
SUM(bed_capacity_of_boys_hostel_in_number)

Total girls hostel beds =
SUM(bed_capacity_of_girls_hostel_in_number)

Total boys hostels =
SUM(number_of_boys_hostel)

Total girls hostels =
SUM(number_of_girls_hostel)
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


def format_answer(question, result):

    prompt = f"""
User Question:
{question}

Database Result:
{result}

Instructions:

- Answer in simple English.
- Give direct answer.
- Maximum 2 sentences.
- Do not mention SQL query.
- Do not mention database result.
- Give only final answer.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()