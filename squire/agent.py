from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.tools.duckduckgo import DuckDuckGoTools

def create_agent(cfg: dict) -> Agent:
    acfg = cfg['agent']
    agent = Agent(name=acfg['name'],
                  tools=[DuckDuckGoTools()],
                  model=Ollama(acfg['model']),
                  instructions=acfg['instructions'],
                  memory=create_memory(cfg),
                  enable_agentic_memory=True
                  )
    return agent

def db_url(cfg: dict) -> str:
    db_cfg = cfg['db']
    auth = f"{db_cfg['creds']['user']}:{db_cfg['creds']['password']}@" if 'creds' in db_cfg else ""
    return f"postgresql+psycopg://{auth}{db_cfg['host']}:{db_cfg['port']}/{db_cfg['schema']}"

def create_memory(cfg: dict) -> Memory:
    url = db_url(cfg)
    return Memory(db=PostgresMemoryDb(table_name="memories", db_url=url))


