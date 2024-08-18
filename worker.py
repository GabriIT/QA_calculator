import requests
import time

secret = "CLqR9gk4vR4wxtADim9PX8iJFhTFrN7i"
def get_llm_response(prompt: str):
    # time.sleep(10)
    url = f'http://localhost:5001/ai'  # URL of the 'ai' app
   
    print(f"{prompt}")   
    
    
    response = requests.post(url, json={"Prompt": prompt})    
    answer = response.json()
    return answer
    # return answer["Response"]
    # return answer["answer"]
    # return response
    
while True:
    print("Worker beep...")

    response = requests.put("http://app.athenalabo.com:8080/prompt", json={"Auth": "CLqR9gk4vR4wxtADim9PX8iJFhTFrN7i"})

    print(response.status_code)
    message = response.json()
    print(message)
  

    if "QueueId" in message:        
        print(f"Getting answer from LLM with prompt {message['Prompt']}...")
        answer = get_llm_response(message["Prompt"])

        # str_QueueId = str(message["QueueId"])

        print(f"Answer is {answer}")
        response = requests.post(            
            f"http://app.athenalabo.com:8080/prompt/{message['QueueId']}",
            json={"Auth": "CLqR9gk4vR4wxtADim9PX8iJFhTFrN7i", "Response": answer},
        )
        print(response.status_code)
        print(response.json())
               
    time.sleep(3)
    
      # f"http://app.athenalabo.com:8080/prompt/{str_QueueId}",
            # json={"Auth": "CLqR9gk4vR4wxtADim9PX8iJFhTFrN7i", "Response": answer},