import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="Name of the file to save text document")
args = parser.parse_args()

if os.path.isfile(f"{args.file_name}.txt"):
    file = open(f"{args.file_name}.txt", "a")
else:
    file = open(f"{args.file_name}.txt", "w")

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

while True:
    prompt = input("Enter a prompt (or 'done' to finish): ")
    if prompt.lower() == "done":
        break

    request_data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 4000,
        "temperature": 0.5
    }

    response = requests.post(api_endpoint, headers=request_headers, json=request_data)

    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"]
        print(response_text)
        satisfactory = input("\nWas the response satisfactory? (y/n): ")
        while satisfactory.lower() not in ["y", "n"]:
            satisfactory = input("\nPlease enter 'y' or 'n': ")
        if satisfactory.lower() == "y":
            file.write(f"\nQuestion: {prompt} \n {response_text} \n" )
            file.flush()
            print ("\nResponse saved in document\n")
        else:
            continue
    else:
        response_error = response.json()["error"]["message"]
        print(f"\n\nRequest failed with \nstatus code: {str(response.status_code)} \nmessage: {response_error}")
        break

file.close()
