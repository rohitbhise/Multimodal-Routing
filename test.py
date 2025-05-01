import os

#add key

from routellm.controller import Controller


client = Controller(
    routers=["mf"],
    strong_model="gpt-4o",
    weak_model="gpt-4o-mini"
)

response = client.chat.completions.create(
    model="router-mf-0.1",
    messages=[{"role": "user", "content": "Explain black holes simply."}]
)

print(response.model)
# print(response.choices[0].message.content)