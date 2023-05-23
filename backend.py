import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"  # Replace "YOUR_API_KEY" with your actual API key

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write a joke on banana")
    print(response)
