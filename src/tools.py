import warnings

# Suppress warnings to keep the output clean for the video
warnings.filterwarnings("ignore")

# Reverting to the stable community import to prevent ImportErrors
from langchain_community.tools.tavily_search import TavilySearchResults

def get_search_tool():
    """
    Returns the search tool instance.
    Configuration for max_results can be tuned here.
    """
    return TavilySearchResults(max_results=2)