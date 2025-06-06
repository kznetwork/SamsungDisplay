import openai

openai.api_key = "proj-3n8TNE_rqiosOfKRsc_piZXDcFYq_RiDoKxVVQoMiOl7dVYJKwKqUbacavWtx2uNSNCDgokPRBT3BlbkFJkFPfkDexGj5Y_NFt2nz8mS6W6vpCL3CZ7ylCqPTyzeon7NnEoVuzi-Rs52gIDnn7F__pLFeA4A"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role":"system","content": "너는 친절하게 답변해주는 비서야"},
      {"role":"user","content": "2020년 월드시리즈에서는 누가 우승했어?"}
  ]
)
#print(response)
print(response['choices'][0]['message']['content'])