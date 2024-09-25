import os
import sys
import tempfile
from loguru import logger

logger.remove()

log_level = os.getenv("SCREENVIVID_LOG_LEVEL", "INFO")
logger.add(sys.stderr, level=log_level)

logger.add(
    os.path.join(tempfile.gettempdir(), "screenvivid.log"),
    rotation="5 MB",
    level=log_level
)