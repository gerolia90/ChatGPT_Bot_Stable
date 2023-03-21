import openai

def chatgpt_func(prompt):
    openai.api_key = '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'
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text
