from icecream import ic

from llm_sdk.llm_sdk import Small_LLM_Model

ic.configureOutput(includeContext=True)


my_model = Small_LLM_Model()
my_prompt = "Este es mi maravilloso prompt de test"

encoded_prompt = my_model.encode(my_prompt)
ic(encoded_prompt)
