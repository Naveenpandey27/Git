import logging

try:
    raise ValueError
except ValueError:
    logging.info('This is an info message')