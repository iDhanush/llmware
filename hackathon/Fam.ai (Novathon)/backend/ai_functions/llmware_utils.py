import requests

from global_vars import Var


def get_llmware_response(prompt, context):
    url = Var.kaggle_url+'chat'
    print(context)
    print(url)
    res = requests.post(url,
                        json={'prompt': str(prompt), 'context': str(context)})
    print(res)
    res = res.json()
    if not res:
        return False
    print(res)
    llm_response = res['llm_response']
    return llm_response
