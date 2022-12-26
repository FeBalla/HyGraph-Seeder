from utils import get_template_query, make_query
from dotenv import dotenv_values

if __name__ == "__main__":
  config = dotenv_values(".env")

  query = """
  mutation CreateGame(
    $name: String!,
    $description: String!,
    $objectives: String!,
    $imgUrl: String!,
  ) {
    createGame(data: {
      name: $name,
      description: $description,
      objectives: $objectives,
      imgUrl: $imgUrl
    }) {
      id
      name
      description
      objectives
      imgUrl
    }
  }
  """

  endpoint_url = config["CONTENT_API_URL"]
  headers = { 
    "Content-Type": "application/json",
    "Authorization" : f"Bearer {config['PERMANENT_AUTH_TOKEN']}" 
  }

  variables = {
    "name": "name 1",
    "description": "description 1",
    "objectives": "objective 1",
    "imgUrl": "https://bitacoras-ljyr.s3.amazonaws.com/imagenes/30.png"
  }

  make_query(endpoint_url, query, variables, headers)
