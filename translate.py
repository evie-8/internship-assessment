#!/usr/bin/python3

"""
A function that uses SunbirdA1's API
to translate text prompt into a different language
"""

import requests
import time

language_codes = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}


def lower_case(input):
    """convert input to lowecase"""
    return input.lower()


def source_language_prompt() -> str:
    """prompt to ask user to enter source language"""
    # language of text to be translated
    print("\n(🤖):\tWhich language will you write your text in?")

    for index, key in enumerate(language_codes, start=1):
        print(f"\t\t\t{index}: {key}")
    print("\tEnter number corresponding to language or language name")
    print("\t❓To end press 'q'")
    
    source_input = input("\n(🧑):\t")

    if (source_input.lower() == 'q'):
        language = 'quit'

    elif source_input.isdigit():
        source_input = int(source_input)
        if 1 <= source_input <= len(language_codes):
            language = list(language_codes.keys())[source_input - 1]

        else:
            print("\n(🤖):\t❌❌ Invalid input. Please enter a valid number ❌❌")
            time.sleep(5)
            return source_language_prompt()

    elif source_input.title() in language_codes.keys():
        language = source_input.title()

    else:
        print("\n(🤖):\t❌❌ Invalid input. Please enter a valid language ❌❌")
        time.sleep(5)
        return source_language_prompt()

    return language


def target_language_prompt() -> str:
    """prompt to ask user to enter target language"""
    # language to translate to
    print("\n(🤖):\tWhich language do you want to translate to?")

    for index, key in enumerate(language_codes, start=1):
        print(f"\t\t\t{index}: {key}")
    print("\tEnter number corresponding to language or language name")
    print("\t❓To end press 'q'")
    target_input = input("\n(🧑):\t")

    if (target_input.lower() == 'q'):
        language = 'quit'

    elif target_input.isdigit():
        target_input = int(target_input)
        if 1 <= target_input <= len(language_codes):
            language = list(language_codes.keys())[target_input - 1]

        else:
            print("\n(🤖):\t❌❌ Invalid input. Please enter a valid number ❌❌")
            time.sleep(5)
            return target_language_prompt()

    elif target_input.title() in language_codes.keys():
        language = target_input.title()

    else:
        print("\n(🤖):\t❌❌ Invalid input. Please enter a valid language ❌❌")
        time.sleep(5)
        return target_language_prompt()

    return language


def text_prompt(source_language: str) -> str:
    """prompt to ask user to enter text in a specific target language"""
    print("\n(🤖):\t Enter text to translate in {}".format(source_language))
    text_to_translate = input("\n(🧑):\t")

    if (text_to_translate.lower() == 'q'):
        text_to_translate = 'quit'

    return text_to_translate


def get_translation(data: dict) -> str:
    """passes data to url and returns response"""
    url = "https://api.sunbird.ai/tasks/nllb_translate"

    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"

    headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            }

    response = requests.post(url, headers=headers, json=data)

    response = response.json()
    if (response['status'] == 'COMPLETED'):
        return response['output']['data']['translated_text']
    else:
        return "❌ Translation failed ❌"
    


def translator():
    """
    This function translates text prompt into
    (English, Luganda, Runyankole, Ateso, Lugbara or Acholi) languages
    """

    source = source_language_prompt()

    if (source == 'quit'):
        return

    target = target_language_prompt()
    
    if (target == 'quit'):
        return

    if (source == target):
        print("\n(🤖):\t❌❌ Source language can't be "
              "similar to target language ❌❌")
        time.sleep(5)
        return translator()

    text = text_prompt(source)

    if (text == 'quit'):
        return
    data = {
            "source_language": language_codes[source],
            "target_language": language_codes[target],
            "text": text
            }
    response = get_translation(data)
    print("\n(🤖):\t{}".format(response))
    time.sleep(5)
    return translator()


def main():
    """
    This function translates text prompt into
    (English, Luganda, Runyankole, Ateso, Lugbara or Acholi) languages

    """

    print("(🤖):\tHello, I am sunbird, your personal translator.")
    print("\tWould you like to do translations?\n"
          "\tType (yes)/(y) to accept or any character to decline\n")

    user_input = input("(🧑):\t")
    if (lower_case(user_input) == 'yes' or lower_case(user_input) == 'y'):
        translator()
    else:
        return


if __name__ == "__main__":
    main()
