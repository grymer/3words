import json, math, random, re

MAXLEN = 3 # Number of words to combine (if "len" not supplied)
DEFSEP = '-' # Default separator to use (if "sep" not supplied)
WORDLIST = '/var/task/3of6game.txt' # File path to a word list

# Function to load words from a file and return as a list object
def ldwords():
    l = []
    with open(WORDLIST) as f:
        l = f.read().splitlines()
    return l
    
# Function to create a password using list object l, with length n, and using separator s 
def mkpasswd(l, n, s):
    passwd = ""
    chosen_words = []
    for x in range(n):
        random_word = random.choice(l)
        chosen_words.append(random_word)
        l.remove(random_word) # No repeated words
    return s.join(chosen_words)

# Function to calculate entropy of password (assumes no repeated words)
def get_entropy(l, n):
    # x = math.pow(len(l), n)
    x = math.comb(len(l), n)
    return math.log2(x)
    
def lambda_handler(event, context):
    n = MAXLEN
    s = DEFSEP
    ent = False
    if (('queryStringParameters' in event.keys()) and (json.dumps(event['queryStringParameters']) != 'null')):
        if ('len' in event['queryStringParameters'].keys()):
            try:
                n = int(event['queryStringParameters']['len'], 10)
            except ValueError:
                n = MAXLEN
        if ('sep' in event['queryStringParameters'].keys()):
            try:
                s = event['queryStringParameters']['sep'][0]
            except IndexError:
                s = DEFSEP
        if ('ent' in event['queryStringParameters'].keys()):
            ent = True
    l = ldwords()
    d = {}
    d['Password'] = mkpasswd(l, n, s)
    if ent:
        d['Entropy'] = str(get_entropy(l, n))
    return {
        'isBase64Encoded': 0,
        'statusCode': 200,
        'headers': {'Content-Type': 'text/json; charset=utf-8', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(d)
    }
