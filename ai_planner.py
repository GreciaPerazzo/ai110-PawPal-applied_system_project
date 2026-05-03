import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemma-3-27b-it")

def generate_care_plan(pet_name: str, pet_species: str, pet_breed: str, pet_age: int, tasks: list) -> str:
    """
    Uses Gemini AI to generate a personalized daily care plan for a pet.
    Takes the pet's info and pending tasks, returns an explained plan.
    """
    if not tasks:
        return "No pending tasks found. Add some tasks to get an AI-generated care plan!"

    # Build a task summary to send to Gemini
    task_summary = ""
    for task in tasks:
        task_summary += f"- {task.task_type} at {task.time} (Priority: {task.frequency})\n"

    # Build the prompt
    prompt = f"""
You are a helpful pet care assistant. A pet owner needs help planning their day.

Pet Information:
- Name: {pet_name}
- Species: {pet_species}
- Breed: {pet_breed}
- Age: {pet_age} years old

Today's pending tasks:
{task_summary}

Please do the following:
1. Suggest the best order to complete these tasks and explain WHY
2. Flag any tasks that seem urgent or time-sensitive
3. Give one helpful pet care tip specific to this pet's breed or age
4. End with a motivational message for the pet owner

Be warm, friendly, and concise.
"""

    try:
        logger.info(f"Generating AI care plan for {pet_name}...")
        response = model.generate_content(prompt)
        logger.info("AI care plan generated successfully")
        return response.text
    except Exception as e:
        logger.error(f"Error generating care plan: {e}")
        return f"Sorry, I couldn't generate a care plan right now. Error: {str(e)}"


def check_task_urgency(task_type: str, pet_species: str) -> str:
    """
    Uses Gemini AI to assess how urgent a specific task is.
    Returns a short urgency assessment.
    """
    prompt = f"""
In one short sentence, how urgent is a '{task_type}' task for a {pet_species}? 
Rate it as: LOW, MEDIUM, or HIGH urgency and explain why briefly.
"""
    try:
        logger.info(f"Checking urgency for task: {task_type}")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logger.error(f"Error checking urgency: {e}")
        return "Could not assess urgency at this time."