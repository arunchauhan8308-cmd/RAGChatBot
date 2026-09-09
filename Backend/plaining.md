## Load the data
- Load the data using the Directory Loader
- Load all file in the Directory and return the file 

## Create the Chunks 
- get the files location and then create the chunk in the chunk_size = 500, with the chunk_overlap = 50 
- Then Return the Chunks.

## Load the EMbedding Model 
- Load the Gemini Model
- EMbedded the model in the vetor database 

## Store the chunks in the vector store (mongoDB VectorDB)
- Store the data in the vector Database in the mongoDB
- After that save the data online and store locally on the laptop for performance


## Create te Routes
- Create the route for the user query.
- create the routes for the 
    - Login
    - Signup
    - query