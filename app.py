import streamlit
from langchain import OpenAI, PromptTemplate
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

def generate_response(txt):
    PRIMARY_MODEL = 'gpt-3.5-turbo'
    MAX_TOKENS = 200
    TEMPERATURE = 0.1

    llm = OpenAI(model_name=PRIMARY_MODEL, temperature=TEMPERATURE, max_tokens=MAX_TOKENS, openai_api_key=openai_api_key)

    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)

    docs = [Document(page_content=t) for t in texts]

    prompt_template = '''TLDR. Summarize the text into 3 bullet points.
    {text}
    3-POINT SUMMARY:
    '''

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)

#Webpage
streamlit.set_page_config(page_title="Generative AI Text Summarization Demo", page_icon=":random:", layout='centered')
streamlit.title('Generative AI Text Summarization Demo')

#Take an input
txt_input = streamlit.text_area('Enter your text to summarize', '', height=200)

#Form to accept input
result = []
with streamlit.form('summarize_form', clear_on_submit=True):
    openai_api_key = streamlit.text_input('OpenAI API Key', type='password', disabled=not txt_input, value=streamlit.secrets['OPENAI_API_KEY'])
    submitted = streamlit.form_submit_button('SUBMIT')

    if submitted and openai_api_key.startswith('sk-'):
        with streamlit.spinner('Summarizing ...'):
            response = generate_response(txt_input)
            result.append(response)
            del openai_api_key

if len(result):
    streamlit.write(response)