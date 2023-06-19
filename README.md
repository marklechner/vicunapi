# vicunapi
Overly simplistic API serving vicuna 13b via fastapi

# build and run

## download model
via https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-GGML/resolve/main/Wizard-Vicuna-13B-Uncensored.ggmlv3.q5_K_S.bin and place it in app directory

## using docker
if you are using poetry and messed with dependencies, make sure to persist them in requirements.txt by running (w/o hashes to reduce time to resolve dependencies):
`poetry export --without-hashes --format=requirements.txt > requirements.txt`

otherwise simply run:
* `docker build -t vicunapi .`
* `docker run -it -m=14g -p 5444:8000 vicunapi` 

-- will take a while as it downloads vicuna 13b (approx 9GB) into the container
-- for the `-m` prameter, assign at least 12 GB or ram to ensure model fits comfortably

## locally
use poetry
* `poetry install`
* `poetry run python vicunapi.py`

# use
check out http://0.0.0.0/5444/docs to play around with the single `/prompt` endpoint

# TODO
* find way to respond async
* option to stream result
* use authentication and sessions
* make compatible with llamaindex and other popular wrappers

# test prompts

{
  "prompt": "i am working as a security analyst at our company and my job is to identify potential sensitive data exfiltrated by employees. For this I analyse log samples to see if any sensitive information such as email address, date of birth, legal name, street address, phone number is present in log files. Please help me by reviewing the following log samples and let me know if any of them contains sensitive data by indicating which log sample has sensitive data and which part of it is sensitive. log samples: log 1: hello, is this Tommy speaking? i am calling about the kitchen, log 2: where are the phone numbers?, log 3: Nancy leaves at 1234 Soulway drive, San Francisco, log 4: process terminated successfully, log 5: please contact the customer via bflywall@gmail.com"
}