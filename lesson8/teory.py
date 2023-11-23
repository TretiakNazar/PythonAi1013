import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
logging.basicConfig(level=logging.DEBUG, filename="Logs.Log", filemode="w", format="We have next logging massage:%(asctime)s%(levelname)s - %(message)s")
# logging.debug("debug")
# logging.info("info")


try:
    print(10/0)
except Exception:
    logging.exception("Помилка діління на 0")