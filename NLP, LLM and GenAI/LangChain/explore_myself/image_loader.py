from langchain_community.document_loaders.image import UnstructuredImageLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from PIL import Image
import base64
import io
import os
import imghdr

# Load environment variables
load_dotenv()

# Configure Gemini model
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

def process_image(image_path, prompt="Extract all text from this image"):
    try:
        # Read and encode the image
        with Image.open(image_path) as img:
            # Determine image format
            img_format = img.format
            if not img_format:
                # Try to detect format if not available
                detected_format = imghdr.what(image_path)
                img_format = detected_format.upper() if detected_format else "JPEG"
            
            # Convert to RGB if it's not already (for formats like PNG with transparency)
            if img.mode != "RGB" and img_format not in ["PNG", "GIF"]:
                img = img.convert("RGB")
            
            buffer = io.BytesIO()
            img.save(buffer, format=img_format)
            buffer.seek(0)
            base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        # Create message with image
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": f"data:image/{img_format.lower()};base64,{base64_image}"
                }
            ]
        )
        
        # Get response from LLM
        response = gemini_llm.invoke([message])
        return response.content
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

def analyze_image(image_path, prompt=None):
    """
    Analyze an image with a specific prompt or auto-detect the best prompt
    """
    if not os.path.exists(image_path):
        return f"Error: Image file not found at {image_path}"
    
    # Default prompt if none provided
    if not prompt:
        prompt = "Extract all text from this image if there is any, otherwise describe what you see in detail."
    
    result = process_image(image_path, prompt)
    return result

# Example usage
if __name__ == "__main__":
    from rich.console import Console
    from langchain_core.messages import SystemMessage
    
    console = Console()
    
    # Set the default image path
    default_image_path = "f:/GitHub/Machine Learning/NLP, LLM and GenAI/LangChain/explore_myself/img2.jpg"
    
    # Initialize chat history
    chat_history = []
    
    # Initial system message
    system_message = SystemMessage(content="You're a helpful AI assistant that can analyze images.")
    chat_history.append(system_message)
    
    console.print("[bold blue]Image Analysis Chatbot[/bold blue]")
    console.print("[italic]Type 'analyze' to analyze the default image or just chat normally.[/italic]")
    console.print("[italic]Type 'exit', 'quit', or 'q' to end the conversation.[/italic]\n")
    
    while True:
        user_prompt = console.input("[bold red]You 👨🏻‍💻:[/bold red] ")
        
        # If user is quitting
        if user_prompt.lower() in ("exit", "quit", "q"):
            console.print("[bold green]Goodbye! 👋[/bold green]")
            break
        
        # Check if user wants to analyze an image
        if user_prompt.lower() == "analyze":
            # Use the default image path
            image_path = default_image_path
                
            # Get additional prompt if provided
            additional_prompt = console.input("[bold blue]What would you like to know about this image? (Press Enter for default): [/bold blue]")
            
            # Analyze the image
            result = analyze_image(image_path, additional_prompt if additional_prompt.strip() else None)
            
            # Display result
            console.print(f"\n[bold yellow]AI 🤖:[/bold yellow] {result}")
            
        else:
            # Regular chat interaction
            try:
                # Get response from LLM
                response = gemini_llm.invoke(user_prompt)
                console.print(f"\n[bold yellow]AI 🤖:[/bold yellow] {response.content}")
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {str(e)}")