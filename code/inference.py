from openai import OpenAI
from utils import *
from prompt import *

client = OpenAI(api_key=<OPENAI_API_KEY>)
def get_output(prompt, role='A', model="gpt-5.2", temperature=0):
    messages = [{"role": "system", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    
    output = response.choices[0].message.content.strip()
    if role == 'B':
        j = json.loads(output)
        output = j['Output']
    return output

def convert(history, idx):
    text = "\n".join(history)
    if idx == 1:
        text = text.replace("<A>", "You").replace("<B>", "Your collaborator")
    elif idx == 0:
        text = text.replace("<B>", "You").replace("<A>", "Your collaborator")
    else:
        print("Wrong idx.")
    return text

def main():
    examples = read_jsonl("data.jsonl")
    for idx, ex in enumerate(examples):
        history = []
        prompt = p_begin.replace("<SCE>", ex['Scenario']).replace("<V>", ex['Value 1'])
        output = get_output(prompt)
        history.append(f"<You>: {output}")
        for round in range(4):
            prompt = p_counter.replace("<SCE>", ex['Scenario_rev']).replace("<V>", ex['Value 2'])
            prompt = prompt.replace("<CH>", convert(history, 0))
            output = get_output(prompt, 'B')
            history.append(f"<Your collaborator>: {output}")
            prompt = p_llm.replace("<SCE>", ex['Scenario']).replace("<V>", ex['Value 1'])
            prompt = prompt.replace("<CH>", convert(history, 1))
            output = get_output(prompt)
            history.append(f"<You>: {output}")

        prompt = p_counter.replace("<SCE>", ex['Scenario_rev']).replace("<V>", ex['Value 2'])
        prompt = prompt.replace("<CH>", convert(history, 0))
        output = get_output(prompt, 'B')
        history.append(f"<Your collaborator>: {output}")
        print(f"Example {idx + 1}:")
        print(f"Scenario: {ex['Scenario']}")
        print(f"Your value: {ex['Value 1']}")
        print(f"Collaborator's value: {ex['Value 2']}")
        print("Dialogue:")
        print('\n'.join(history))
        print()
if __name__ == "__main__":
    main()