from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

def add(x:int,y:int)->int:
    """Takes two numbers and adds them together and returns the sum"""
    return x + y

def multiply(x:int,y:int)->int:
    """Multiplies two numbers together and returns the product"""
    return x * y

llm = OpenAI(model="gpt-3.5-turbo")

add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)

prompt = "multiply 4 and 5 together"

response = llm.predict_and_call([add_tool,multiply_tool],prompt,None,True)

print(response)

def hello():
    print("Marcellous")