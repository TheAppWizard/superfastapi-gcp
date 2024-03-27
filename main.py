from fastapi import FastAPI

app = FastAPI()

# Simple rule-based chatbot logic
def chatbot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Endpoint to handle chatbot messages
@app.get("/chatbot")
async def chatbot(message: str):
    response = chatbot_response(message)
    return {"response": response}
