from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize the OpenAI GPT-4.1 model
llm = ChatOpenAI(
    model="gpt-4-1106-preview",  # GPT-4.1 model name
    temperature=0.7,
    openai_api_key="YOUR_OPENAI_API_KEY"  # Replace with your actual API key
)

# Set up conversation memory
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Example interaction
response = conversation.predict(input="Hello, who won the FIFA World Cup in 2018?")
print(response)