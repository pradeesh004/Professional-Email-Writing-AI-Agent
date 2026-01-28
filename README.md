# Professional-Email-Writing-AI-Agent
✉️ Professional Email Writing AI Agent

This project implements a Professional Email Writing Agent using Google ADK, LiteLLM, and Pydantic.
The agent generates polite, concise, and professional emails in a strict JSON format, based on the user’s requirements.

🚀 Features

Generates professional email content

Automatically creates:

A clear and precise subject line

A well-structured email body with greetings and conclusion

Outputs response in a validated JSON format

Uses Pydantic schema to ensure structured output

Powered by OpenRouter Nemotron Nano 12B model

🧠 How It Works

A LiteLLM model is initialized using OpenRouter.

A Pydantic model (EmailContent) defines the expected email structure.

An AI Agent:

Understands the user’s email requirement

Writes a professional email

Ensures the response follows the required JSON schema

Appends the user’s contact details

📂 Code Overview
🔹 Model Initialization
model = LiteLlm(
    model="openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

🔹 Email Output Schema
class EmailContent(BaseModel):
    subject: str = Field(description="a precise simple subject line")
    body: str = Field(description="professional email body with greetings and conclusion")

🔹 Agent Definition
root_agent = Agent(
    name="email_agent",
    model=model,
    description="professional email writing agent",
    instruction="Writes polite, short, precise professional emails",
    output_schema=EmailContent,
    output_key="email",
)

📑 Output Format

The agent always returns valid JSON in the following structure:

{
  "subject": "Precise subject line",
  "body": "Professional email body with greeting and conclusion"
}


User contact details included in the email:

Name: Pradeesh Kumar G

Email: pradeesh004.12@gmail.com

▶️ Usage

Provide the email requirement (purpose, recipient, context).

The agent:

Generates a professional subject

Writes a polite and concise email body

Returns structured JSON output

🛠 Requirements

Python 3.8+

Google ADK

LiteLLM

Pydantic

OpenRouter API key

export OPENROUTER_API_KEY="your_api_key_here"

📌 Example Use Cases

Job application emails

Internship or research inquiry emails

Professional follow-up emails

Corporate or academic communication

📄 Notes

The agent does not add extra text outside the JSON response.

Output is strictly validated using the Pydantic schema.

Ideal for automation pipelines and email-generation systems.

✨ Author

Built as a structured, professional email generation agent using Google ADK and LiteLLM.
