# OpenAI Summarizer with Streamlit Demo

This is a generative AI boilerplate app that quickly summarizes texts. The app was built using Langchain and Streamlit and invokes OpenAI's API via Langchain.

### Overview of the App

- Accepts a paragraph of text as the input text (to be summarized) using Streamlit's 'text_input()'
- Text is split into chunks via 'CharacterTextSplitter()' along with its 'split_text()' method
- Document is generated via 'Document()'
- Text summarization is achieved using 'load_summarize_chain()' by applying the 'run()' method on the input 'docs'.

### Get an OpenAI API Key

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the '+ Create new secret key' button.
3. Next, enter an identifier name (optional) and click on the 'Create secret key' button.

## Setup

1. Clone this repo
    ```bash
    $ git clone https://github.com/ccmilne/GenAI_Boilerplate_Streamlit
    ```

2. Navigate into the directory
    ```bash
    $ cd GenAI_Boilerplate_Streamlit
    ```

3. Create a new virtual environment
    ```bash
    $ python -m venv venv
    $ . venv/bin/activate
    ```

4. Install the requirements
    ```bash
    $ pip install -r requirements.txt --user
    ```

5. Add your [OPENAI API key](https://platform.openai.com/account/api-keys) to '.streamlit/secrets.toml' file

6. Run the application:
    ```bash
    $ streamlit run app.py #or py -m streamlit run app.y
    ```
