import wolframalpha
import pickle
import logging as l

logfile = 'wolf.log'
apiFile = 'wolframAPIKey'
l.basicConfig(
    filename=logfile,
    level=l.DEBUG,
)

l.debug("WOLF TEX-WolframAlpha Interface V0")
l.debug("Getting API key from "+apiFile+"...")

try:
    with open(apiFile, "r") as file:
        apiKey = file.readlines()[0].replace("\n","") #read first line and strip \n
except FileNotFoundError:
    l.critical("Cannot find API key file "+apiFile+" - quitting!")
    exit(1)

client = wolframalpha.Client(apiKey)
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
    res = client.query(prompt)
    return res

def lprint(x):
    print(x+"%")

def askW(unFormattedPrompt):
    prompt = get(unFormattedPrompt)
    if not prompt in wolfHistory:
        l.info("Querying WolframAlpha for "+prompt)
        result = askWolfram(prompt)
        try:
            res = next(result.results).text
        except(AttributeError) as e:
            l.critical("Issue in responce from {0} which became {1}, error: {2}\n Quitting!".format(unFormatedPrompt, prompt, e))
            raise Exception("Ahh! issue with result from {0} which became {1}, {2}".format(unFormatedPrompt, prompt, e))
        wolfHistory[prompt] = res.split(" (")[0].replace(" ","")
        pickle.dump(wolfHistory, open("wolfHistory.pickle", "wb"))
    else:
        l.debug("Found \""+prompt+"\" in history: \""+wolfHistory[prompt]+"\".")
    return wolfHistory[prompt]

try:
    l.debug("Opening pickle ....")
    wolfHistory = pickle.load(open("wolfHistory.pickle", "rb"))
except FileNotFoundError:
    l.info("Pickle not found")
    wolfHistory = {}
