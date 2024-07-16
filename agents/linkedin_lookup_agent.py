import sys
import os 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv(), override=True) 

from langchain_openai import ChatOpenAI 
from langchain.prompts.prompt import PromptTemplate 
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub # Used to download pre-made prompts from the langchain team and the community

sys.path.append(os.getcwd()) # THIS LINE IS NECESSARY FOR IMPORTING (from tools_folder.tools_file import get_profile_url_tavily) https://stackoverflow.com/questions/60593604/importerror-attempted-relative-import-with-no-known-parent-package

from tools_folder.tools_file import get_profile_url_tavily

def lookup(name: str) -> str: # The arrow here (->) is a return annotation for the function lookup(); more information about return annotations: https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    template=""" 
    Given the full name {name_of_person}, I want you to get me a link to their Linkedin profile page. 
    Your answer should contain ONLY a URL.
    """

    prompt_template=PromptTemplate(
        template=template, 
        input_variables=["name_of_person"]
        )
    
    tools_for_agent=[
        Tool(
            name="Crawl Google for Linkedin Profile Page", 
            func=get_profile_url_tavily,
            description="Useful for when you need to get a Linkedin Page URL"
        )
    ]

    react_prompt=hub.pull("hwchase17/react")

    agent=create_react_agent(
        llm=llm, 
        tools=tools_for_agent, 
        prompt=react_prompt
    )

    agent_executor=AgentExecutor(
        agent=agent, 
        tools=tools_for_agent, 
        verbose=True
    )

    result=agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)}) # MUST USE (input={"input": prompt_template.format_prompt(name_of_person=name)})

    linked_profile_url=result["output"]

    return linked_profile_url

print(lookup("Eden Marco"))