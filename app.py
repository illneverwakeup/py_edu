import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# использовать ключи для форматера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        return 'secret' not in record.getMessage().lower()

if not logger.handlers:  # защита от дублирования
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    # Ротация именно файла orders.log и нужный размер
    file_handler = RotatingFileHandler(
        "orders.log", maxBytes=1000000, backupCount=3, encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.addFilter(SensitiveDataFilter())

def process_order(order_id, user_id, amount):
    logger.info(f"Start processing order {order_id} for user {user_id}")
    logger.debug(f"Amount: {amount}")
    if amount <= 0:
        try:
            raise ValueError(f"Non-positive amount: {amount}")
        except Exception:
            logger.error(f"Order {order_id} failed for user {user_id}", exc_info=True)
            raise
    logger.info(f"Order {order_id} completed for user {user_id}")


process_order(1, 42, 100)
process_order(2, 43, -50)