import google.generativeai as genai

genai.configure(api_key="AIzaSyAdDFTc4d_Qs2FDzfHKjHXjMbttmT5TtQs")

for m in genai.list_models():
    print(m.name)