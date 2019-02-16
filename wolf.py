import wolframalpha
client = wolframalpha.Client('829ATX-VJ29Y7PP48')
latexVars = {}

def setVar(name, value):
    latexVars[name] = [value]

def getVar(name):
    return latexVars[name][0]
def getVars():
    return [x for x in latexVars]

def get(prompt):
    for x in range(0,5):
        for var in getVars():
            prompt = prompt.replace(var, getVar(var))
    return prompt

def askWolfram(prompt):
    prompt = get(prompt)
    res = client.query(prompt)
    return res

def lprint(x):
    print(x+"%")

def askW(prompt):
    result = askWolfram(prompt)
    try:
        res = next(result.results).text
    except(AttributeError) as e:
        raise Exception("Ahh! issue with result from {0} which became {1}, {2}".format(prompt, get(prompt), e))
    return res.split(" (")[0].replace(" ","")
