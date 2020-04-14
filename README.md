# 3words
A simple passphrase generator

Implemented as an AWS Lambda in Python, this function will return multi-word passphrases. It can be called without parameters, or with optional specifiers for number of words, separator, and whether or not to return the calculated password entropy, e.g:

https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/passwd?len=3&sep=-&ent

I recommended deploying with Alan Beale's [3of6game](http://wordlist.aspell.net/12dicts-readme/#3of6) word list for good results and high entropy.

An example web page, "index.html", illustrates how to parse the returned JSON object.
