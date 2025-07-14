import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a set of predefined responses
responses = {
    "greet": ["Hello!", "Hi there!", "Greetings!", "How can I help you today?"],
    "bye": ["Goodbye!", "See you later!", "Take care!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!", "Anytime!"],
    "default": ["I'm sorry, I didn't quite understand that.", "Can you rephrase that?", "Could you elaborate?"]
}

# Define pairs of questions and responses
patterns = [
    (r'hello|hi|hey|greetings', ["greet"]),
    (r'bye|goodbye|see you', ["bye"]),
    (r'thank you|thanks', ["thanks"]),
    (r'.*', ["default"])  # Catch-all pattern
]

# Preprocessing: Tokenization, removing stopwords, and lemmatization
def preprocess_input(user_input):
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

# Respond based on the predefined patterns
def respond(user_input):
    tokens = preprocess_input(user_input)
    for pattern, response_group in patterns:
        if any(word in pattern for word in tokens):
            # Return a random response from the matching group
            return random.choice(responses[response_group[0]])
    return random.choice(responses["default"])

# Chatbot loop
def chat():
    print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond(user_input)
            print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
