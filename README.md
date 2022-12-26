# HyGraph-Seeder
Is a simple Python script made to quickly upload data from a JSON file to a [HyGraph](https://hygraph.com) model. It **uses the default mutations** created from the generated GraphQL API.

## Considerations
Since it was intended for simple use, data can only be uploaded for one model at a time, although it should not be too difficult to extend it to several at once.

## How to use it?
1. Set the environment variables following the `example.env` file. For this you need to get a *Permanent Auth Token* in the project settings and the *Content API* endpoint url.
2. Change the `model_name` variable in `main.py` for the name of your model in HyGraph.
3. Change the `variable_types_path` variable in `main.py` for the path of your JSON file with the model attribute types. This file needs to follow a format like the `variableTypes.json` file in the example folder:
```json
// Example of variable types
{
  "name": "String!",
  "description": "String!",
  "objectives": "String!",
  "imgUrl": "String!"
}
```
4. The same as in the previous step, but this time with the data you want to upload to the HyGraph model. You can base it on the `variablesData.json` file in the example folder.
```json
// Example of variable data. It needs to be an array
[
  {
    "name": "Autograph",
    "description": "You must complete a 3x3 board with the information of other people, this is achieved by beating them in a duel of cachipu00fan. If they beat you, you must write your data on their board.",
    "objectives": "Social interaction, getting to know a group of people, breaking the ice.",
    "imgUrl": "https://bitacoras-ljyr.s3.amazonaws.com/imagenes/1.png"
  },
  {
    "name": "Lotere of names",
    "description": "After the game 'Autograph', names are drawn at random among the players as in a bingo, and if we have the data of that person on our board, we mark it. Finally, the winner is the one who completes the board first.",
    "objectives": "Meet a group of people, break the ice.",
    "imgUrl": "https://bitacoras-ljyr.s3.amazonaws.com/imagenes/2.png"
  }
]

```
5. Run the `main.py` module.
