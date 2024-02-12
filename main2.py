import streamlit as st


st.title("Chatbot")

#chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

#display
for message in st.session_state.messages:
  display_result = st.chat_message(message['role'])
  display_result.write(message['content'])
  

prompt = st.chat_input('Enter a prompt here')

if prompt and prompt != '':

  st.chat_message('user').write(prompt)

  st.session_state.messages.append({'role': 'user', 'content': prompt})


  if prompt == "hi":
    st.chat_message('assistant').write('Hi! How are you doing?')
    st.session_state.messages.append({'role': 'assistant', 'content': 'Hi! How are you doing?'})
  elif prompt == "good":
    st.chat_message('assistant').write("That's good to hear!")
    st.session_state.messages.append({'role': 'assistant', 'content': "That's good to hear!"})
  elif prompt == "bad":
    st.chat_message('assistant').write("Eh? Why?")
    st.session_state.messages.append({'role': 'assistant', 'content': "Eh? Why?"})
  elif prompt in ["what's your name", "who are you"]:
    st.chat_message('assistant').write("I'm Gemini! A Chatbot!")
    st.session_state.messages.append({'role': 'assistant', 'content': "I'm Gemini! A Chatbot!"})
  elif prompt == "bye":
    st.chat_message('assistant').write("See you next time!")
    st.session_state.messages.append({'role': 'assistant', 'content': "See you next time!"})
  else:
    st.chat_message('assistant').write("Can you repeat that again? How can I help you?")
    st.session_state.messages.append({'role': 'assistant', 'content': "Can you repeat that again? How can I help you?"})