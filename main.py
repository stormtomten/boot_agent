import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY2")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for _ in range(20):
        try:
            messages = generate_content(client, messages, verbose)

            if isinstance(messages[-1], str):
                print(f"Last message: {messages[-1]}")
                break
        except Exception as e:
            print(f"Error: {e}")
            break


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print(response.text)

    for candidate in response.candidates:
        messages.append(candidate.content)

    if not response.function_calls:
        messages.append(response.text)
        return messages

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response.response
        ):
            raise Exception("Function call did not return expected response structure")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    tool_message = types.Content(role="tool", parts=function_responses)
    messages.append(tool_message)

    if not function_responses:
        raise Exception("No function responses generated, exiting.")

    return messages


if __name__ == "__main__":
    main()
