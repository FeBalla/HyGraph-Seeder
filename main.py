from utils import get_template_query, make_query
from dotenv import dotenv_values
import json

# PARAMETERS
model_name = "Game"
variable_types_path = "variableTypes.json"
variables_data_path = "variablesData.json"


if __name__ == "__main__":
  with open(variable_types_path, encoding="utf-8") as f:
    variable_types = json.load(f)
  with open(variables_data_path, encoding="utf-8") as f:
    variables_data = json.load(f)

  config = dotenv_values(".env")
  endpoint_url = config["CONTENT_API_URL"]
  headers = { 
    "Content-Type": "application/json",
    "Authorization" : f"Bearer {config['PERMANENT_AUTH_TOKEN']}" 
  }

  query = get_template_query(model_name, variable_types)
  for entry in variables_data:
    make_query(endpoint_url, query, entry, headers)
