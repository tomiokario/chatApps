import streamlit as st
st.set_page_config(page_title="ChatWebUi")

st.markdown("""
### Home
Streamlitを使用したシンプルなChatアプリケーション

#### Applications
##### 1. Chat
- OpenAI API経由でGPT-3.5と対話します．

##### 2. SearchChat
- DuckDuckGo APIで検索するAIエージェントと対話します．

##### 3. ProgressChatWithSearch
- DuckDuckGo APIで検索するAIエージェントと対話します．
- エージェントの思考過程を表示します．
            
            
            
#### 参考
 
Chat & SearchChat
- https://github.com/streamlit/llm-examples/blob/main/Chatbot.py

ProgressChatWithSearch
- https://github.com/KitaharaMugiro/genai-poc/blob/main/search/pages/duckduckgo.py
""")