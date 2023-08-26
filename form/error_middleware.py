import logging

logger = logging.getLogger(__name__)

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("called")
        try:
            response = self.get_response(request)
            print("good")
        except Exception as e:
            print("not good")
            logger.error(f"An exception occurred: {str(e)}")
            raise e  # Re-raise the exception
        return response
