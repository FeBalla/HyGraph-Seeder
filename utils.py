import requests

def get_template_query(model_name: str, variables: str) -> str:
  pass

def make_query(url: str, query: str, variables: dict = {}, headers: dict = {}) -> None:
    """Make query to the default GraphQL endpoint from HyGrap with the specified variables"""
    request = requests.post(url, json={ "query": query, "variables": variables }, headers=headers)
    print(request.json())
