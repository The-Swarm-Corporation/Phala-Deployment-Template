import os

from loguru import logger
from swarm_models import OpenAIChat
from swarms.agents.create_agents_from_yaml import create_agents_from_yaml

# Path to your YAML file
yaml_file = "agents.yaml"


# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")
model_name = os.getenv("MODEL_NAME")

# Model
model = OpenAIChat(
    openai_api_base=openai_api_base,
    openai_api_key=api_key,
    model_name=model_name,
    temperature=0.1,
)

try:
    # Create agents and run tasks (using 'both' to return agents and task results)
    task_results = create_agents_from_yaml(
        model=model, yaml_file=yaml_file, return_type="run_swarm"
    )

    logger.info(f"Results from agents: {task_results}")
except Exception as e:
    logger.error(f"An error occurred: {e}")
