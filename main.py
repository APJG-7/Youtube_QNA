import streamlit as st
import langchain_helper as lch
st.title("YouTube QnA Assistant")

# Just add it after st.sidebar:
url = st.sidebar.text_input("Enter URL",max_chars=70)
query = st.sidebar.text_input("Enter Your Question",max_chars=70)
open_ai_key = st.sidebar.text_input("Enter your OpenAI Key",max_chars=100,type="password")

if not open_ai_key:
    st.write("Please enter your OPENAI_API_KEY")
    
if url and query and open_ai_key:
    db = lch.load_and_vectorize_data(url, open_ai_key)
    res = lch.get_the_answer(db, query, open_ai_key)
    
    # Check if 'answer' key is present in the result dictionary
    if 'answer' in res:
        answer = res['answer']
        
        # Convert the answer to a string for display
        answer_str = str(answer)
        
        # Print each line of the answer
        for line in answer_str.split('\n'):
            st.write(line)
    else:
        st.write("No answer found.")
