import fire

def hello(name="World"):
    return "Hello $s!" % name

#hope will work

print("hello")

def calculate(num1=0,num2=1):
    return f"answer:  {num1 + num2}"

fire.Fire(calculate)