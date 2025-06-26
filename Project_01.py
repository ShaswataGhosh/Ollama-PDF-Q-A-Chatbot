#!/usr/bin/env python
# coding: utf-8




from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings





MODEL ="llama3.2"





model = Ollama(model=MODEL)
embeddings=OllamaEmbeddings(model=MODEL)
model.invoke("Tell a joke")





from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = model | parser
chain.invoke("Tell me a joke")




from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/attention.pdf")
pages = loader.load_and_split()
pages





from langchain.prompts import PromptTemplate

template = """

Answer the question based on the context below. If you can't answer the question, reply"I don't know"

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)
print(prompt.format(context="Here is some context", question="Here is a question"))





chain = prompt | model | parser




chain.invoke(
    {
        "context":"The name I was given was Shaswata",
        "question":"What is my name?"
    }
)











from langchain_community.vectorstores import DocArrayInMemorySearch

vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)





retriever = vectorstore.as_retriever()
retriever.invoke("Robust Python")




from operator import itemgetter

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
    }
    | prompt
    | model
    | parser
)









import streamlit as st





def run_streamlit_app():
    question = st.text_input("Write Your Query")


    st.write(f"Question: {question}")
    st.write(f"Answer: {chain.invoke({'question': question})}")








