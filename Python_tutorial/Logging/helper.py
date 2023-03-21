import logging
logger = logging.getLogger(__name__)
logger.propagate = False #Turn this off if we need need main program logger and disable this custom logger
logger.info("hello from helper")