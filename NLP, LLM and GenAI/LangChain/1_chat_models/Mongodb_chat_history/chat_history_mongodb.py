from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langchain_huggingface import HuggingFaceEndpoint
from rich.console import Console
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Initialize console and load environment variables
console = Console()
load_dotenv()

# MongoDB Atlas setup
CLUSTER_URI = os.getenv("CLUSTER_URI")
if not CLUSTER_URI:
    raise ValueError("CLUSTER_URI not found in .env file")

DB_NAME = "langchain_test_db"
COLLECTION_NAME = "chat_history"
SESSION_ID = "hDFDuoD0L91zNeSU17sd"

# Initialize MongoDB chat history
try:
    chat_history = MongoDBChatMessageHistory(
        connection_string=CLUSTER_URI,
        database_name=DB_NAME,
        collection_name=COLLECTION_NAME,
        session_id=SESSION_ID
    )
    console.print(
        "[green]MongoDB chat history initialized successfully![/green]")
except Exception as e:
    console.print(f"[red]Error initializing MongoDB chat history: {e}[/red]")
    exit(1)

# HuggingFace LLM setup
hf_api_key = os.getenv("HF_TOKEN")
if not hf_api_key:
    raise ValueError("HF_TOKEN not found in .env file")

Qwen_llm = HuggingFaceEndpoint(
    model="Qwen/QwQ-32B",
    temperature=0.7,
    huggingfacehub_api_token=hf_api_key
)

# Chatbot-like interface
system_message = SystemMessage(content="You're a helpful AI assistant.")

while True:
    user_prompt = console.input("[bold red]\n\nYou 👨🏻‍💻:[/bold red] ")

    # If user wants to quit
    if user_prompt.lower() in ("exit", "quit", "q"):
        console.print("[bold green]Goodbye! 👋[/bold green]")
        break

    # Add user message to chat history
    chat_history.add_user_message(user_prompt)

    # Generate and add AI response
    try:
        ai_response = Qwen_llm.invoke(user_prompt)
        chat_history.add_ai_message(ai_response)
        console.print(f"\n[bold yellow]{ai_response}[/bold yellow]")
    except Exception as e:
        console.print(f"[red]Error generating AI response: {e}[/red]")

# Display chat history
console.print(f"\n[bold green] --- Message History --- [/bold green]")
for message in chat_history.messages:
    if isinstance(message, HumanMessage):
        console.print(f"[cyan]You: {message.content}[/cyan]")
    elif isinstance(message, AIMessage):
        console.print(f"[yellow]AI: {message.content}[/yellow]")
