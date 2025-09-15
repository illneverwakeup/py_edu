import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def process_order(order_id, user_id, amount):
    logger.info(f"Start processing order {order_id}", exc_info=False)
    logger.debug(f"Amount: {amount}")
    if amount > 0:
        logger.info(f"Order {order_id} completed")
    else:
        logger.error(f"Order {order_id} failed", exc_info=True)


process_order(1, 2, -5)