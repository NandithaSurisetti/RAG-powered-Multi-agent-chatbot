from langchain_openai import ChatOpenAI

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langchain_experimental.tools.python.tool import PythonAstREPLTool

from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper

from langchain import hub
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
from langchain.callbacks.manager import get_openai_callback

import streamlit as st
import os
#from dotenv import load_dotenv
#load_dotenv()
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")




st.title("RAG-Powered Multi-Agent Q&A Assistant")
api_key=st.text_input("Give your OpenAI API key")
query=st.text_input('Type your query here')

if query:
    #wikipedia tool
    api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)
    
    #our personal tool
    loader=WebBaseLoader("https://docs.smith.langchain.com/")                    
    docs=loader.load()
    documents=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200 ).split_documents(docs)

    vector_db=Chroma.from_documents(documents, OpenAIEmbeddings())
    retriever=vector_db.as_retriever()
    
    #top_docs=retriever.get_relevant_documents(query=input)
    retriever_tool=create_retriever_tool(retriever, "Langsmith_search" ,
                        "Search for information about Langsmith.For any questions about Langsmith you must use this tool")

    #tools ready 
    #combining these tools
    calculator_tool = PythonAstREPLTool(name="Calculator", 
                                     description="A tool for performing mathematical calculations.")
    
    tools=[wiki_tool,calculator_tool,retriever_tool]
    llm=ChatOpenAI(model="gpt-3.5-turbo-0125" , temperature=0, api_key=api_key)

    prompt=hub.pull("hwchase17/openai-functions-agent")

    agent=create_openai_tools_agent(llm,tools,prompt)

    agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)

    response=agent_executor.invoke({"input": query})
    
    top_docs = None

    if "langsmith" in query.lower():
        top_docs = retriever.get_relevant_documents(query=query)
        st.header("The Final answer")
        st.write(response['output'].strip())
        
        st.subheader("Tool Used")
        st.write("Langsmith_search")
        st.subheader("Retrieved Documents")
        st.write(top_docs)
        
    elif "calculate" or "+" or "-" or "/" or "=" in query.lower():
        
        st.header("The Final answer")
        st.write(response['output'].strip())
        
        st.subheader("Tool Used")
        st.write("Calculator")
    
    else :
        st.header("The Final answer")
        st.write(response['output'].strip())
        st.subheader("Tool Used")
        st.write("Wikipedia")
        
    
    

    




