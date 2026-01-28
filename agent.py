from symtable import Class

from google.adk.agents import Agent
from pydantic import BaseModel,Field
from google.adk.models.lite_llm import LiteLlm
import os

from scripts.regsetup import description

model = LiteLlm(
    model = "openrouter/nvidia/nemotron-nano-12b-v2-vl:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

class EmailContent(BaseModel):
    subject: str = Field(description="a precise simple line subject based on the body of the email")
    body: str = Field(description="the body of the email should be more meaningfull, polite and professional manner with proper greetings,main moto,appropriate conlusion with user details .")

root_agent = Agent(
    name = "email_agent",
    model=model,
    description = "proffesional email writing agent",
    instruction = """
    you are an good email writer .
    you need to writer a email based on the user's requirement in a polite,short,precise,proffesional email.
    the email should have:
    -proper subject
    -proper greetings in proffesional way in the body
    -precise,short and polite manner main content
    -appropriate conlusion.
    IMPORTANT: the response should be a vaild json format like the following one:
    {
    subject:"the precise subject line here",
    body:"the body of the email in a proper format in professional way",
    regads:"add the users details for contact purposes"
    
    }
    the contact details of the user:
    name - pradeesh kumar g
    emailid - pradeesh004.12@gmail.com
    
    more importantly don't add any other content in the response.
    """,
    output_schema = EmailContent,
    output_key = "email",
)