import google.generativeai as genai
from speaking import engine,speak
from api_key import key


user_input = str(input("Search : "))

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(user_input)
print(response.text)

#
speak(response.text)
