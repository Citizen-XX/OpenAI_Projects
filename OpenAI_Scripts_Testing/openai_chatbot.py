from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatBot:
    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        self.model = model
        self.conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

    def send_message(self, message: str) -> str:
        assistant_response = ""
        self.conversation_history.append({"role": "user", "content": message})
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0
            )
            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
        except Exception as error:
            print(f"An error occurred: {error}")
        return assistant_response

def main():
    print("Welcome to ChatBot! Type 'quit' to exit.")
    chatbot = ChatBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.send_message(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()