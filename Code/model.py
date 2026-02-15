import prompt_bank
from openai import OpenAI
from tenacity import (retry, stop_after_attempt, wait_random_exponential,retry_if_exception_type)
  
''' Model class Structure'''
class Model:
    model_name_: str
    api_key_: str
    api_base_: str
    max_tokens: int 
    client: None

    def __init__(self, model_name_:str , api_key_: str, api_base_: str):
        self.model_name_= model_name_
        self.api_key_ = api_key_
        self.api_base_ = api_base_
        self.temp = 0
        self.max_tokens = 1000 #I think this is enough
        self.client = OpenAI(api_key = api_key_, base_url= api_base_)
        self.format = {"type": "json_object"}
        
    def adjust_max_tokes(self, max_tokens_: int):
        self.max_tokens = max_tokens_
    
    @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3),retry=retry_if_exception_type(Exception))
    def qurey_LLM_model(self, user_prompt: str):
        messages = [
        {"role": "user", "content": user_prompt}
        ]
        print('m: ',messages)
        completion = self.client.chat.completions.create(
            model= self.model_name_,
            messages= messages,
            max_tokens = self.max_tokens,
            temperature= self.temp,
            response_format = self.format
        )

        return completion.choices[0].message.content


#{"role": "system", "content": prompt_bank.qurey_prompt('base_prompt')},
