## How to ADD New Action?

1. Clone your repository

``` 
git clone <repo-name>
```

2. Change your directory and go to `src` directory

```
cd <repo-name>/src/
``` 

3. Copy the echo directory to a directory with name `<function-name>`

```
cp -r echo <function-name>
```

Note: Directory name should match the Function Name provided in the action.

4. Go to `index.py` in the newly created directory and start writing code for your action in the handler function.

### Input and output format

- Handler function receives the input data in event variable as stringified json with 'body' and 'header' field, which contains the request payload as well as request headers respectively. For context enabled lambda function there will be additional field 'context' with the input.
```
{
    "body": {},
    "headers": {},
    "context": {
      "flow_execution_id": "Root=9-999999-9999999", // flow execution id
      "oauth": {} // json data
    }
}
```
- Handler function in output needs to return 'statusCode' and 'body' fields(where body is a stringified json), which contain the HTTP equivalent statusCode as well as response body respectively. 
- Additionally, in case of an error you can return errors by passing ‘errorMessage’ and ‘errorType’ as part of the response body. Which will help your action users debug errors quickly.
```
{
   "statusCode" : 401,
   "body" : json.dumps({
       "errorMessage": "user creds invalid",
       "errorType": "authentication error"
    })
}
```

## Testing the existing actions using DevServer

- Open Devspaces using the Icon in the Github Repo. A screen will open with an Input Box, an Output Box and a tab to select the existing functions.

### Testing echo action

Ensure that the current selected tab is `ECHO`

- Input:

```json
{
  "headers": {},
  "body": {
    "message": "Hello world!"
  },
  "context": {
    "flow_execution_id" : "Root=9-999999-9999999",
    "oauth": {}
  }
}
```

- Output:

```json
{ "statusCode": 200, "body": "{\"message\": \"Hello world!\"}" }
```

### Testing using `curl`

You can also use curl to test your actions in Devspaces.

```
curl --location --request POST 'http://localhost:8000/echo' --header 'Content-Type: application/json' --data-raw '{
  "headers": {},
  "body": {
    "message": "Hello world!"
  },
  "context": {
    "flow_execution_id": "Root=9-999999-9999999", // flow execution id
    "oauth": {} // json data
  }
}'
```
