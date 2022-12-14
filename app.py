import streamlit as st
import requests
import time

API_KEY = st.secrets.HugApiKey.key
API_URL = "https://api-inference.huggingface.co/models/huranokuma/es2"
headers = {"Authorization": "Bearer "+API_KEY}

st.set_page_config(
     page_title="ESใๆธใAI ver2.0",
     page_icon="๐ค",
     initial_sidebar_state="expanded",
 )

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def main():
  st.title("AIใซใใ่ชๅESไฝๆ ver2.0")  

  min_length = st.slider(label='ๆๅฐๆๅญๆฐ(ๆๅคงใใผใฏใณๆฐ)',
                  min_value=50,
                  max_value= 500,
                  value=100,
                  )
  
  top_p = st.number_input(label='top p : (ไธไฝ P %ใฎๅ่ชใใ้ธใใงใใพใ)',
                  min_value=0.00,
                  max_value=1.00,
                  value=0.95
  )

  top_k = st.slider(label='top k : (ไธไฝkๅใฎๆ็ซ ใไฟๆใใพใ)',
                min_value=1,
                max_value=1000,
                value=500
)
  temperature = st.number_input(label='temperature : (้ซใใปใฉใฉใณใใ ๆงใไธใใใไฝใใปใฉๅใ็ตๆใๅบๅใใใพใ)',
                min_value=0.01,
                max_value=100.0,
                value=1.00
)
  

  prompt_text = st.text_area(
        label='ESใฎๆธใๅบใใฎๆ็ซ ', 
        value='็งใ'
  )

  progress_num = 0
  status_text = st.empty()
  progress_bar = st.progress(progress_num)
  process_text = st.empty()

  process_text.text("ESใฎๆธใๅบใใใไผ็คพใฎ่ณชๅใๅฅๅใใฆใใ ใใใใใใซ็ถใๆ็ซ ใ็ๆใใพใใ")

  if st.button('ๆ็ซ ็ๆ'):

    progress_num = 40 
    progress_bar.progress(progress_num)
    status_text.text(f'Progress: {progress_num}%')
    process_text.text("ๆ็ซ ใ็ๆใใฆใใพใ...ใใใซใฏๆ้ใใใใใใใใใพใใใ")
    start = time.time()

    # APIใไฝฟใฃใฆHuggingfaceใใๆ็ซ ใๅใฃใฆใใใ
    output = query({"inputs": prompt_text,
                "parameters": {
                               "max_length":500,
                               "min_length":min_length,
                               "top_p":top_p,
                               "top_k":top_k,
                               "temperature":temperature,
                               },
                "options":{
                    "wait_for_model": True,
                }
                })

    process_text.text("ESใฎ็ๆใ็ตไบใใพใใใ")
    elapsed_time =round(time.time()-start,2)
    st.info(f'็ๆ็ตๆ : ็ต้ๆ้{elapsed_time}็ง')
    progress_num = 100
    status_text.text(f'Progress: {progress_num}%')
    st.write(output[0]['generated_text'])
    progress_bar.progress(progress_num)

if __name__ == '__main__':
  main()
