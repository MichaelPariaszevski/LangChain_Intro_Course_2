from langchain_community.tools.tavily_search import TavilySearchResults

# from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from dotenv import load_dotenv

load_dotenv()


def get_profile_url_tavily(name: str):
    # from langchain_community.tools.tavily_search import TavilySearchResults

    """Searches for a Linkedin or Twitter Profile Page"""
    # tavily_wrapper=TavilySearchAPIWrapper(tavily_api_key="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")
    search = TavilySearchResults()  # api_wrapper=tavily_wrapper
    res = search.run(f"{name}")
    # print(res)
    return res[0]["url"]


get_profile_url_tavily("Harrison Chase")
