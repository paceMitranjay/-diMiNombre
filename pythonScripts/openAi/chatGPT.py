from openai import OpenAI

# Set your OpenAI API key
client = OpenAI(
  organization= "org-mykjS3htlUHbQXDf20l65FuG",
  api_key= "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",
)

def functionOpen(data):

    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are my transaction analyser"},
        {"role": "user", "content": f'find all swiggy detail in this{data}'}
    ],
    )
    return completion.choices[0].message.content
    # return type(data)

# print(functionOpen("hey"))
# chatGPTFun("hey")
