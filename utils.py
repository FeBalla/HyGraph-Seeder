import requests

def get_template_query(model_name: str, variable_types: str) -> str:
  """
  Get the template query for creating a new model entry using the default mutation query generated 
  by HyGraph. It has the following example format:

  Attributes:
    `model_name`: The name of the HyGraph model, i.e. `Product`

    `variable_types`: Dictionary with the variable GraphQL types, i.e `{"name": "String!"}`
  ```
    mutation CreateModel(
      $name: String!,
      $description: String!,
    ) {
      createModel(data: {
        name: $name,
        description: $description,
      }) {
        id
        name
        description
      }
    }
    ```
  """
  # Adds the first part of the mutation query, naming it as CreateModel (capitalized)
  query = """mutation """
  query += f"Create{model_name.capitalize()}(\n"
  
  # Adds the query types
  for variable_name, variable_type in variable_types.items():
    query += f"  ${variable_name}: {variable_type},\n"

  # Uses the default mutation name for creating entries in HyGraph -> createModel
  query += ") {\n"
  query += f"  create{model_name.capitalize()}(data: {{\n"

  # Adds the query variables
  for variable_name in variable_types.keys():
    query += f"    {variable_name}: ${variable_name},\n"

  query += "  }) {\n"
  query += "    id\n"

  # Adds the query fields that will be returned. In this case, all given fields will be fetched
  for variable_name in variable_types.keys():
    query += f"    {variable_name}\n"

  query += "  }\n"
  query += "}"
  return query


def make_query(url: str, query: str, variables: dict = {}, headers: dict = {}) -> None:
    """
    Makes query to the default GraphQL endpoint from HyGrap with the specified variables
    """
    request = requests.post(url, json={ "query": query, "variables": variables }, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
      raise Exception(f"Query failed to run by returning code of {request.status_code}:\n{query}")
