import logging
# Different log levels
logging.debug("This is a debug message!")

logging.info("This is an info message!")

logging.warning("This is a warning message!")

logging.error("This is an error message!")

logging.critical("This is  a critical message!")


# Adjusting the log level
logging.basicConfig(level=logging.INFO)
logging.info("This will get logged!")
logging.debug("This won't get logged!")
logging.basicConfig(level=0)


# Formatting the output
logging.basicConfig(format="%(levelname)s:%(asctime)s:%(name)s:%(message)s")
logging.warning("Hello, Warning!")


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

logging.error("Something went wrong!")


# Logging to a file
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

logging.warning("Save me!")


# Displaying variable data
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG
)

name = "Pouya"
logging.warning(f"{name=}")


# Capturing stack traces 
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

donuts = 5
guests = 0
try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.error("DonutCalculationError", exc_info=True)

try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.exception("DonutCalculationError")


# Creating a custom logger
logger = logging.getLogger(__name__)
logger.warning("Look at my logger!")


# Using handlers
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)
print(logger.handlers)

logger.warning("Watch out!")


# Adding formatters to your handlers
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
logger.addHandler(console_handler)
logger.addHandler(file_handler)
formatter = logging.Formatter(
   "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

console_handler.setFormatter(formatter)
logger.warning("Stay calm!")


# Setting the log levels of custom loggers
logger.setLevel(10)
print(logger)


logger.setLevel("INFO")
print(logger)

formatter = logging.Formatter("{levelname} - {message}", style="{")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.debug("Just checking in!")
logger.info("Just checking in, again!")


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
formatter = logging.Formatter("{levelname} - {message}", style="{")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
file_handler.setLevel("WARNING")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Just checking in!")


logger.warning("Stay curious!")


logger.error("Stay put!")


# Filtering logs
def show_only_debug(record):
    return record.levelname == "DEBUG"


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
formatter = logging.Formatter("{levelname} - {message}", style="{")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
console_handler.setFormatter(formatter)
console_handler.addFilter(show_only_debug)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
file_handler.setLevel("WARNING")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Just checking in!")


logger.warning("Stay curious!")
logger.error("Stay put!")