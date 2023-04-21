
import streamlit as st
from LLM_interaction import *


def load_LLM():
    llm=OpenAI(temperature=0.1)
    return llm


st.set_page_config(page_title="Writer block unblocker", page_icon=":robot:")
st.header("Unblock your writers block")

col1, col2=st.columns(2)

with col1:
    st.markdown("Often creative writers and novelists struggle with writers block and it does not mean that you lost focus or you lost your shit. You just need a little push and I am sure this app will be helpful")

with col2:
    st.image(image='book.jpg', width=500)


st.markdown("Enter your plot")

col1, col2=st.columns(2)


with col1:
    option_genre=st.selectbox('Which genre would you like your story to have?',
    ('crime','romcom','thriller','slice of life','I dont care!'))

st.markdown("### The plot that you want to develop")
def get_text():
    input_text = st.text_area(label="", placeholder="enter your plot (not more than 250 words)", key="plot_input")
    return input_text

plot_input=get_text()

if len(plot_input.split(" "))> 350:
    st.write("Please enter a shorter plot. I only have an OPENAI trial account lol")
    st.stop()



st.write(plot_input)

print(len(plot_input))

st.markdown("### Your generated plot :")

if plot_input:
    #st.write(f"the entered token length is:{num_tokens_from_string(plot_input)}")

    creative_writer(plot_input,option_genre)

    #prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    generated_plot= creative_writer(plot_input,option_genre)

    st.write(generated_plot)

