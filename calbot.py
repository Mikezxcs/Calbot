import json
import random
from difflib import get_close_matches

#Queen
#helooooo
#hi
#hello
#blablablabh
#pullreqnadis
#nagtry lang ako maggithub AHAHAH
#nagtatry kung gagana 
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, conversation: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, conversation, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for entry in knowledge_base["conversation"]:
        if entry["user"].lower() == question.lower():
            responses = entry.get("responses", [])
            return random.choice(responses) if responses else None

def calbot():
    user_name = input('CalBot: Kumusta! Ako si CalBot. Ano ang iyong pangalan?\n\nYou: ')
    print(f'\nCalBot: Magandang Araw, {user_name}! Ano ang iyong katanungan?\n')

    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input(f'{user_name}: ').lower()

        if user_input == 'quit':
            response = input('\nCalBot: Sigurado ka na bang gusto mong tapusin? (Oo/Hindi): ')
            if response.lower() == 'oo':
                print('\nCalBot: Paalam! Salamat sa pag-usap. Hanggang sa muli!')
                break
            else:
                continue

        best_match: str | None = find_best_match(user_input, [q["user"] for q in knowledge_base["conversation"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'\nCalBot: {answer}\n')
        else:
            print('\nCalBot: Hindi ko alam ang iyong sinabi o itinanong. Maaari mo ba itong ituro sa akin?\n')
            new_answer: str = input('I-tayp ang sagot o ligtangan na lang: ')

            if new_answer.lower() != 'skip':
                knowledge_base["conversation"].append({"user": user_input, "responses": [new_answer]})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('\nCalBot: Salamat! May bago akong natutunan!\n')

if __name__ == '__main__':
    calbot()
