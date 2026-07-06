import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url

load_dotenv()

# Model setup
model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")
google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# Initialize LLM (will raise error only when needed)
llm = None

def get_llm():
    global llm
    if llm is None:
        if not google_api_key:
            raise RuntimeError("Set GOOGLE_API_KEY or GEMINI_API_KEY in your environment or .env file for Gemini.")
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.2,
            google_api_key=google_api_key,
        )
    return llm


#1st agent
def build_search_agent():
    return create_agent(
        model = get_llm(),
        tools = [web_search]
    )

#2nd agent

def build_reader_agent():
    return create_agent(
        model=get_llm(),
        tools=[scrape_url]
    )


#writter chain

writer_prompt = ChatPromptTemplate.from_messages([
("system" , "You are an expert research writer. Write clear, structured and insightful reports."),
("human" , """Write a detailed research report on thr topic below.
 
 Topic: {topic}

 Research Gathered: {research}

 structure the report as:
 - Introduction
 - Key` Findings (minimum 3 well-explained points)
 - Conclusion
 - Sources (list all URLs used in the research)

 Be detailed, factual and proffesional"""),

])

def get_writer_chain():
    return writer_prompt | get_llm() | StrOutputParser()

#critic_chain

critic_prompt = ChatPromptTemplate.from_messages([
      ("system", "you are a sharp and constructive research critic. Be honest and specific."),
      ("human", """Review the research report below and evaluate it strictly.
       
       
       Report: {report}
       
       
       Respond in the exact format:
       
        Score: x/10
       
       Strengths:
       - ...
       - ...
       
       Areas to Improve:
       - ...
       - ...
       
       One line verdict:
       ...""") ,
])

def get_critic_chain():
    return critic_prompt | get_llm() | StrOutputParser()