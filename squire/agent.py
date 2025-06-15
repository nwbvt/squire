from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

def create_agent(cfg: dict) -> Agent:
    acfg = cfg['agent']
    agent = Agent(name=acfg['name'],
                  tools=[DuckDuckGoTools()],
                  model=Ollama(acfg['model']),
                  instructions=acfg['instructions'])
    return agent
                  

