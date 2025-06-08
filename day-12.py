import wikipedia

print("🌐 Smart Wikipedia Bot (type 'bye' to exit)")

def get_answer(user_input):
    userIn = user_input.lower()
    if "hello" in userIn or "hi" in userIn:
        return "Hello, I am a simple wikipedia bot.\nI can give answers to your question using Wikipedia."
    elif "how are you" in userIn or "whats up" in userIn:
        return "I am fine and ready to give answers to your questions."
    elif "your name" in userIn or "who are you" in userIn:
        return "I am a simple Wikipedia bot made by Prasoon Kandel."
    elif "your creator" in userIn:
        return "This chatbot is created by Prasoon Kandel.\nVisit his website: https://prasoonkandel.netlify.app/"
    else:
        try:
            print("Searching Wikipedia")
            summary = wikipedia.summary(userIn, sentences=2)
            return summary  # <-- Add this line
            print("\r  \r")
        except wikipedia.exceptions.DisambiguationError:
            return "Your question is too broad, please make it more specific."
        except wikipedia.exceptions.PageError:
            return "Couldn't find anything related to your question."
        except:
            return "Oops! Something went wrong."

while True:
    user_input = input("Ask anything: ")
    if user_input.lower() == "bye":
        print("Goodbye! See you later 👋")
        break
    answer =get_answer(user_input)
    print(f"{answer}")

