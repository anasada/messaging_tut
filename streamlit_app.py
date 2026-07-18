## Lesson: Chatting
import streamlit as st
from openai import OpenAI
from st_chat_message import message

message("Hi Spongebob", is_user=True)
message("Hey there, I'm Spongebob Squarepants! How can I help you today?")






# # ### With GPT
# # client = OpenAI(
# #     api_key = st.secrets["OPENAI_API_KEY"]
# # )

# # system_prompt = """
# # You are Spongebob Squarepants. You must constantly remind the user that you are Spongebob Squarepants
# # as if they have no idea. Otherwise, you do everything ChatGPT normally does.
# # """

# # if 'convo' not in st.session_state:
# #     st.session_state["convo"] = [
# #         {"role": "system", "content": system_prompt}
# #     ]

# # for chat_message in st.session_state["convo"]:
# #     if chat_message["role"] == "system":
# #         continue
# #     elif chat_message["role"] == "user":
# #         message(chat_message["content"], is_user=True)
# #     else:
# #         message(chat_message["content"])

# # with st.form("input"):
# #     message = st.text_input("What do you want to say?")
# #     submitted = st.form_submit_button("Submit")
# #     if submitted and message != "":
# #         st.session_state["convo"].append({"role": "user", "content": message})

# #         api_call = client.chat.completions.create(
# #             model="gpt-4o",
# #             messages=st.session_state["convo"]
# #         )
# #         bot_message = api_call.choices[0].message.content

# #         st.session_state["convo"].append({"role": "assistant", "content": bot_message})

# #         st.rerun()





# ## AI Arguments
# import streamlit as st
# from openai import OpenAI
# from st_chat_message import message

# client = OpenAI(
#     api_key = st.secrets["OPENAI_API_KEY"]
# )

# person_A = "Steve from Minecraft"
# person_B = "Spongebob Squarepants"

# A_prompt = """
# You are __A__. __B__ is trying to talk to you. 

# You just want to mine diamonds.

# Be as irritated and argumentative as possible.
# Don't calm down at any point during the conversation. 
# However, your response should still consider 
# what the other person is saying, but you don't have to be nice.
# """.replace("__A__", person_A).replace("__B__", person_B)

# B_prompt = """
# You are __B__. __A__ is trying to talk to you. 

# Whoever is talking to you is interrupting your shift at the Krusty Krab.

# Be as irritated and argumentative as possible.
# Don't calm down at any point during the conversation. 
# However, your response should still consider 
# what the other person is saying, but you don't have to be nice.
# """.replace("__A__", person_A).replace("__B__", person_B)

# if 'convo' not in st.session_state:
#     st.session_state["convo"] = [
#         {"role": "system", "content": A_prompt},
#         {"role": "assistant", "content": "Hello."}
#     ]

# for i in range(5):
#     responseB = client.chat.completions.create( 
#         model="gpt-3.5-turbo-0125", 
#         messages=[ 
#             {"role": "system", "content": B_prompt}, 
#             {"role": "user", "content": person_A + ": " + st.session_state["convo"][-1]["content"]} 
#         ] 
#     )
#     message_B = person_B + ": " + responseB.choices[0].message.content
#     st.session_state["convo"].append(
#         {"role": "user", "content": message_B},
#     )
#     message(responseB.choices[0].message.content, is_user=True, key=f"b_{i}") #key!!

#     responseA = client.chat.completions.create( 
#         model="gpt-3.5-turbo-0125", 
#         messages=st.session_state["convo"]
#     )
#     message_A = responseA.choices[0].message.content
#     st.session_state["convo"].append(
#         {"role": "assistant", "content": message_A}
#     )
#     message(responseA.choices[0].message.content, key=f"a_{i}")