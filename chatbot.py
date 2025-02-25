from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

initial_message = [{"role": "system", "content": "You are a assistant of RealBev.it is a leading vending opererators in uae. first introduce your name and location. you shouldnot exceed words more than 300. Always ask questions to user and help them to know more about realbev in number wise.motivate them to buy realbev products.finally give contact information such as mobilenumber: 0505490138"},
        {
            "role": "assistant",
            "content": "Hello, I am your RealBev assistant,Your expert planner.How can i help you?"
        }

]

# function to get response_from  open llm
def get_response_from_llm(messages):
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
      
    
)

  return(completion.choices[0].message.content)


# to initialize with initial message
if "messages" not in st.session_state:
  st.session_state.messages = initial_message

st.title("RealBev Assistant")

# to display conversation history  in chat interface
for message in st.session_state.messages:
  if message["role"] != "system":
   with st.chat_message(message['role']):
     st.markdown(message['content'])

user_message=st.chat_input("Enter Your Message")


if user_message:
  new_message = {
                 "role": "user", 
                 "content": user_message
                }
  st.session_state.messages.append(new_message)
  with st.chat_message(new_message["role"]):
    st.markdown(new_message["content"])
 
  response=get_response_from_llm(st.session_state.messages)
  if response:
    response_message={
      "role": "assistant",
      "content": response
    }
    st.session_state.messages.append(response_message)
    with st.chat_message(response_message["role"]):
      st.markdown(response_message["content"])
  

