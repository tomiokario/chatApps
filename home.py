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

##### 3. SearchChatWithProgress
- DuckDuckGo APIで検索するAIエージェントと対話します．
- エージェントの思考過程を表示します．
            
##### 4. webExplore
- Webページを検索し，その内容を要約して表示します．
- Google API Key, Google CSE ID, OpenAI API Keyを使用します．
            
##### 5. TextFileQnA
- アップロードしたテキストファイルに関する質問を受け付けて回答します．

#### 参考
 
Chat & SearchChat
- https://github.com/streamlit/llm-examples/blob/main/Chatbot.py

SearchChatWithProgress
- https://github.com/KitaharaMugiro/genai-poc/blob/main/search/pages/duckduckgo.py

webExplore
- https://github.com/langchain-ai/web-explorer

TextFileQnA
- https://github.com/dataprofessor/langchain-ask-the-doc/blob/master/streamlit_app.py
""")