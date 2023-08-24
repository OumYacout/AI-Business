# Business toolkit powered by langchain and openai by Belghini - version August 2023


import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import openai
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType


#enter the api key here
#openai_api_key = ""



github_token = st.secrets.github_token
repo_owner = st.secrets.repo_owner
repo_name = st.secrets.repo_name
file_path = st.secrets.file_path


# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="AI Business Toolkit", page_icon="My_logo.png",)
# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)
welcome_title = '<center style="font-family:Courier; color:Orange; font-size: 25px;">Business Toolkit - Powered by AI</>'
st.markdown(welcome_title, unsafe_allow_html=True)
st.write('\n')  # add spacing


# Set the width of the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


if openai_api_key=="":
    st.sidebar.write("You do not provide an API key. Please enter your openai key")
    
st.sidebar.write("<a href='https://platform.openai.com/account/api-keys' id='api_link'>Generate you own API key by clicking here</a>", unsafe_allow_html=True)

st.sidebar.write('\n')


bmc_button_html = """
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js"
        data-name="bmc-button" data-slug="naouarbelgx" data-color="#FFDD00" data-emoji=""
        data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000"
        data-font-color="#000000" data-coffee-color="#ffffff">
    </script>
</div>
"""

# Display the Buy Me a Coffee button HTML in the sidebar

with st.sidebar:
    st.components.v1.html(bmc_button_html, height=70)
    #st.markdown(bmc_button_html, unsafe_allow_html=True)

st.sidebar.image("bmc_qr.png")

st.sidebar.subheader("Visit our other generative apps:")
st.sidebar.write("<a href='https://aitravelagent.streamlit.app' id='app1_link'>AI travel planner</a>", unsafe_allow_html=True)



def generate_emails(language, category, name, company, subject):
  llm = OpenAI(model_name='gpt-3.5-turbo-16k',temperature=0.7, openai_api_key=openai_api_key)
  # Prompt
  template = 'Please ignore all previous instructions. Please respond only in the {language} language. Do not explain what you are doing. Do not self reference. As a professional email marketer. You have a Creative tone of voice. your name is {name} and you are from {company}. Write a not personalized {category} email promoting this product or service: {subject}.'
  prompt = PromptTemplate(input_variables=["language","category","name","company", "subject"], template=template)
  prompt_query = prompt.format(language=language, category= category, name=name, company= company, subject=subject)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return (response)


def generate_SocialMediaContent(language, category, subject):
  llm = OpenAI(model_name='gpt-3.5-turbo-16k',temperature=0.7, openai_api_key=openai_api_key)
  # Prompt
  template = 'Please ignore all previous instructions. Please respond only in the {language} language. Do not explain what you are doing. Do not self reference. You are an expert {category} marketer. You have a Creative tone of voice. create one post up to 120 caracters based on product/service {subject} for {category}.the post should have a catchy headline and description. Add emojis to the content when appropriate. Do not self reference. Do not explain what you are doing.'

  prompt = PromptTemplate(input_variables=["language","category","subject"], template=template)
  prompt_query = prompt.format(language=language, category= category, subject=subject)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return (response)

def generate_SocialMediaImage(subject):
    openai.api_key = openai_api_key
    response = openai.Image.create(
        prompt="post that include this {subject}",
        n=1,
        size="512x512"
        )
    image_url = response['data'][0]['url']
    return (image_url)

def generate_BusinessAdvisory(language, category, subject):
  llm = OpenAI(model_name='gpt-3.5-turbo-16k',temperature=0.7, openai_api_key=openai_api_key)
  # Prompt
  template = 'Please ignore all previous instructions. Please respond only in the {language} language. Do not explain what you are doing. Do not self reference. As a business consultant. please advise to perform {category} to improve the efficiency of the business based on the following product or service: {subject}. Please present the results in a markdown table'
  prompt = PromptTemplate(input_variables=["language","category","subject"], template=template)
  prompt_query = prompt.format(language=language, category= category, subject=subject)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return (response)



def update_github_file(data):


    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        "Authorization": f"token {github_token}"
    }

    response = requests.get(url, headers=headers)
    file_data = response.json()

    if "content" in file_data:
        decoded_content = base64.b64decode(file_data["content"]).decode("utf-8")
    else:
        decoded_content = ""

    form_data = f"{decoded_content}\n\n{data}"
    encoded_form_data = base64.b64encode(form_data.encode("utf-8")).decode("utf-8")


    if "sha" in file_data:
        payload = {
            "message": "Update contact form data",
            "content": encoded_form_data,
            "sha": file_data["sha"]
        }
    else:
        payload = {
            "message": "Update contact form data",
            "content": encoded_form_data
        }

    update_response = requests.put(url, json=payload, headers=headers)
    return update_response.status_code

def main_send_message():
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.subheader("Contact me for any personalized request")
    message = st.text_area("")
    
    if st.button("Submit"):
        form_data = f"Message: {message}"
        status_code = update_github_file(form_data)

        if status_code == 200:
            st.success("Form submitted successfully!")
        else:
            st.error("An error occurred while updating the file.")
    

def main_gpt_emails_generator():


    st.subheader('\n What is your email is about ?\n')

    post_text = ""  # initialize columns variables

    input_language1 = st.selectbox('Choose a language', ('English', 'Espagnol', 'Francais', 'arabic'),key="1", index=0)
    input_type1 = st.selectbox('Email category ', ('Sales', 'Newsletter'),key="type",index=0)
    input_name1 = st.text_input('What is your name', 'Maria')
    input_company1 = st.text_input('What is your company name', 'Mari bags')
    input_subject1 = st.text_input('What is your products / services', 'for example: bags')

    col1, col2, col3 = st.columns([10, 10, 10])

    with col1:
        pass
    with col3:
        pass
    with col2 :
        if st.button('Generate email'):
            if openai_api_key=="":
                st.warning("You do not provide an API key. Please enter your openai key")

            else:
                with st.spinner():
                    post_text = generate_emails(input_language1, input_type1, input_name1, input_company1, input_subject1)
                    
    if post_text != "":
        st.write('\n')  # add spacing
        with st.expander("Creating email...", expanded=True):
            st.markdown(post_text)  #output the results

        col1, col2, col3 = st.columns([10, 10, 10])
        with col1:
            pass
        with col3:
            pass
        with col2 :
            if st.download_button("Download results?", post_text):
                st.dialog("download with success( see download folder)")

def main_gpt_SocialMedia_generator():


    st.subheader('\n What is your social media is about ?\n')

    post_text = ""  # initialize columns variables

    input_language2 = st.selectbox('Choose a language', ('English', 'Espagnol', 'Francais', 'arabic'),key="2", index=0)
    input_type2 = st.selectbox('Choose a social media', ('Facebook', 'Instagram', 'Linkedin', 'Tiktok', 'Twitter'),key="SM", index=0)
    input_topic = st.text_input('What is your topic is about')

    col1, col2, col3 = st.columns([10, 10, 10])

    with col1:
        pass
    with col3:
        pass
    with col2 :
        if st.button('Generate Social Media Content'):
            if openai_api_key=="":
                st.warning("You do not provide an API key. Please enter your openai key")

            else:
                with st.spinner():
                    post_text = generate_SocialMediaContent(input_language2, input_type2, input_topic)
                    url= generate_SocialMediaImage(input_topic)
                    
    if post_text != "":
        st.write('\n')  # add spacing
        with st.expander("Creating Social Media Content...", expanded=True):
            st.markdown(post_text)#output the results
            st.image(url)


                

            
def main_gpt_BusinessAdvisory_generator():


    st.subheader('\n What is your email is about ?\n')

    post_text = ""  # initialize columns variables

    input_language3 = st.selectbox('Choose a language', ('English', 'Espagnol', 'Francais', 'arabic'),key="3", index=0)
    input_type3 = st.selectbox('Choose category ', ('SWOT analysis', 'generate business idea', 'strategic business advisory'),index=0)
    input_subject3 = st.text_input('What is your business about')

    col1, col2, col3 = st.columns([10, 10, 10])

    with col1:
        pass
    with col3:
        pass
    with col2 :
        if st.button('Business advisoring'):
            if openai_api_key=="":
                st.warning("You do not provide an API key. Please enter your openai key")

            else:
                with st.spinner():
                    post_text = generate_BusinessAdvisory(input_language3, input_type3, input_subject3)
                    
    if post_text != "":
        st.write('\n')  # add spacing
        with st.expander("Here my consulting report..", expanded=True):
            st.markdown(post_text)  #output the results

            
def main_gpt_chat_generator():
  st.subheader('\n Please select a CSV file ?\n')
    # Upload File
  file =  st.file_uploader("",type=["csv"])
  if not file: st.stop()

  if openai_api_key=="":
    st.warning("You do not provide an API key. Please enter your openai key")

  else:

        query = st.text_input("Enter a question to ask your file:") 
        # Read Data as Pandas
        data = pd.read_csv(file)

        # Define pandas df agent - 0 ~ no creativity vs 1 ~ very creative
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0.1, openai_api_key=openai_api_key),data,verbose=True) 
            
        # Define Generated and Past Chat Arrays
        if 'generated' not in st.session_state: 
            st.session_state['generated'] = []

        if 'past' not in st.session_state: 
            st.session_state['past'] = []

        # CSS for chat 
        chat_text_style = \
        """
            .user-text {
                color: blue;
                text-align: right;
                
            }
            
            .ai-text {
                color: gray;
                text-align: left;
            }
        """

        # Apply CSS style
        st.write(f'<style>{chat_text_style}</style>', unsafe_allow_html=True)


        # Execute Button
        if st.button("send") and query and openai_api_key:
            with st.spinner('Generating response...'):
                try:
                    answer = agent.run(query)

                    # Store conversation
                    st.session_state.generated.append(answer)
                    st.session_state.past.append(query)
                    
                    for i in range(len(st.session_state.past)):
                        st.write(f'<div class="user-text">{st.session_state.past[i]}</div>', unsafe_allow_html=True)
                        st.write(f'<div class="ai-text">{st.session_state.generated[i]}</div>', unsafe_allow_html=True)
                        
                        st.write("")

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")   
            

def main():
    
    tab1, tab2, tab3, tab4 = st.tabs(["Mail Generator", "Social Media Content Generator", "Business Advisory", "Ask your data"])

    with tab1:
       main_gpt_emails_generator()

    with tab2:
        main_gpt_SocialMedia_generator()

    with tab3:
        main_gpt_BusinessAdvisory_generator()
        
    with tab4:
        main_gpt_chat_generator()



    
if __name__ == '__main__':
    main()
    main_send_message()
