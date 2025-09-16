from logger_setup import logger, process_order

# Теперь просто используешь готовый логгер!
logger.info("Программа запущена")

def main():
    try:
        process_order(123, 456, 100)
        process_order(124, 457, -50)  # Это вызовет ошибку
    except Exception as e:
        logger.critical("Критическая ошибка в основном потоке")

if __name__ == "__main__":
    main()
