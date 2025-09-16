import logging
import logging.config
import yaml
from pathlib import Path

class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        return 'secret' not in record.getMessage().lower()

Path("logs").mkdir(exist_ok=True)

with open('logging_config.yaml', 'r', encoding='utf-8') as f:
    logging.config.dictConfig(yaml.safe_load(f))

logger = logging.getLogger("my_app")

def process_order(order_id, user_id, amount):
    logger.info(f"Start processing order {order_id} for user {user_id}")
    logger.debug(f"Amount: {amount}")
    if amount <= 0:
        try:
            raise ValueError(f"Non-positive amount: {amount}")
        except Exception:
            logger.error(f"Order {order_id} failed for user {user_id}")
            raise
    logger.info(f"Order {order_id} completed for user {user_id}")


__all__ = ['logger', 'process_order']

