import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_interaction(user_input, response):
    logging.info(f"User: {user_input}")
    logging.info(f"Agent: {response}")
