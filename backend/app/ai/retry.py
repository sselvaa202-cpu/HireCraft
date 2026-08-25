# HireCraft - AI Retry Utility

import time

from app.ai.errors import AIConfigurationError, AIRequestError


def retry_ai_request(
    operation,
    max_attempts: int = 3,
    delay: float = 1.0
):
    """
    Retry a temporary AI request failure.

    Configuration errors are not retried because
    changing the number of attempts cannot fix
    missing configuration.
    """

    for attempt in range(1, max_attempts + 1):

        try:
            return operation()

        except AIConfigurationError:
            # Configuration problems should fail immediately.
            raise

        except AIRequestError:

            if attempt == max_attempts:
                raise

            time.sleep(delay)