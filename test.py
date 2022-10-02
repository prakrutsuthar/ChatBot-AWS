import requests
import json
import time


url = "https://runtime.lex.us-east-1.amazonaws.com/bot/NewsBotOne/alias/TestBotOP/user/user2027430/text"

payload = json.dumps({
  "inputText": "hi"
})
headers = {
  'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
  'X-Amz-Security-Token': '=FwoGZXIvYXdzEEEaDOGLh9QhKCNjjSrs+iLAAb7I8DJgaDgljCekHl5VL/mPMllMzA2/2tcWg2OY9OjMt4ThN86FzI5Nj8Wfu+NVWVKRj/EBi7qDMkkSkHowT5tROoqkCPnmmd2iGJbm7C77g4cGFZN7g1A9Nvr3VsQfMnk3ZpZ+7mp2A6MdUYUyNDXX6p+PUDgXlgilxsLZKzGFMEMr//IcuP3UDPkUGkvsCzYqAmqIHWjc68JUWxeopdHJ8w4Xltd3wuqd+Ja9iKzBu89p68ZeeAPUKyxyLqVywSjlkbiWBjIt3XP6GkRm3BAzWKvGml6NSgarlXLnIj/a/ynzNsBHMB1mlJfBzLBxMDEdc7cp',
  'X-Amz-Date': '20220712T235255Z',
  'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAX5UJGMCWZWTQKO4K/20220712/us-east-1/lex/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=db307aaf83a3adf50cee02c7f6c7da51972e89e2fde52b6802219555df41d16a',
  'Content-Type': 'application/json'
}
start_time = time.time()
while True:
    print("Hitting..")
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        time.sleep(1)
        print(response.text)
        print("\n"*5)
    else:
        print("Ended in {0} seconds".format(time.time() - start_time))
        break