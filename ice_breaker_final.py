import os
import sys
from dotenv import load_dotenv, find_dotenv

sys.path.append(os.getcwd())

if __name__=="__main__": 
    print("Hello!")
    load_dotenv(find_dotenv(), override=True)

from langchain.prompts.prompt import PromptTemplate 
from langchain_openai import ChatOpenAI 

from third_parties.linkedin import scrape_linkedin_profile

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from agents.twitter_lookup_agent import lookup_2 as twitter_lookup_agent 
from third_parties.twitter import scrape_user_tweets_no_duplicate_code

from Output_Parsers import summary_parser
from Output_Parsers import Summary # Summary is a class from Output_Parsers.py

from typing import Tuple

def ice_break_with_2(name: str) -> Tuple[Summary, str]: 
    linkedin_url=linkedin_lookup_agent(name=name)
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)

    twitter_username=twitter_lookup_agent(name=name)

    tweets=scrape_user_tweets_no_duplicate_code(username=twitter_username, mock=True)

    summary_template_new="""
    Given the Linkedin information: {linkedin_information} about a person, and their latest twitter posts {twitter_posts}, I want you to create: 
    1. a short summary 
    2. two interesting facts about them

    Use both sources of information from Twitter and Linkedin
    \n{format_instructions}
    """

    summary_prompt_template_new=PromptTemplate(
        input_variables=["linkedin_information", "twitter_posts"], 
        template=summary_template_new, 
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm_new=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)   

    chain_2=summary_prompt_template_new | llm_new | summary_parser

    output_new: Summary=chain_2.invoke(input={"linkedin_information": linkedin_data, "twitter_posts": tweets})

    return output_new, linkedin_data.get("profile_pic_url")

load_dotenv(find_dotenv(), override=True)

print("Ice Breaker Enter 2")
output, profile_pic_url=ice_break_with_2(name="Eden Marco") # Runs each AgentExecutor chain twice (even before printing "Ice Breaker Enter 2")
print(output)
print("-"*100)
print(output.summary) 
print("-"*100) 
print(output.facts)
print("-"*100) 
print(profile_pic_url)