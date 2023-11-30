"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Funções OpenAI
==============

Link de estudo: https://python.langchain.com/docs/modules/agents/agent_types/openai_functions_agent

Neste script realizamos queries.

Execução:

$ python Building_LLM_Connected_To_Our_Database.py 
"""
# from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
# from langchain.agents import initialize_agent, Tool
# from langchain.agents import AgentType
# from langchain.chat_models import ChatOpenAI
# from decouple import config
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper, SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Substitua sua chave de API OpenAI:
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']

# Nosso modelo de linguagem:
llm = ChatOpenAI(model="gpt-3.5-turbo-0613",
                 temperature=0
                )

# Criamos uma Tool de pesquisa:
search = SerpAPIWrapper()

# Criamos uma Tool de Matemática:
llm_math_chain = LLMMathChain.from_llm(llm=llm,
                                       verbose=True
                                      )

# Nós conectamos a nosso DB:
db = SQLDatabase.from_uri("sqlite:///product_db.db")

# Criamos uma Chain database:
db_chain = SQLDatabaseChain.from_llm(llm,
                                     db,
                                     verbose=True
                                    )

tools = [
    Tool(
        name="SearchTool",
        func=search.run,
        description="Útil para quando você precisar responder perguntas sobre eventos atuais. Você deve fazer perguntas direcionadas"
    ),
    Tool(
        name="MathTool",
        func=llm_math_chain.run,
        description="Útil para quando você precisa responder perguntas sobre matemática"
    ),
    Tool(
        name="Product_Database",
        func=db_chain.run,
        description="Útil para quando você precisar responder perguntas sobre produtos."
    )
]

# Criando o agente:
agent = initialize_agent(tools=tools,
                         llm=llm,
                         agent=AgentType.OPENAI_FUNCTIONS,
                         verbose=True
                        )

# Fazemos perguntas ao LLM:
agent.run("Qual é o preço do produto mais caro?")
