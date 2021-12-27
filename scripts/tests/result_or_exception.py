class ResultOrException:
  def __init__(self):
    self.result = None
    self.exception = None

  def from_response(response):
    result_or_exception = ResultOrException()
    result_or_exception.result = response
    return result_or_exception
  
  def from_exception(exception):
    result_or_exception = ResultOrException()
    result_or_exception.exception = exception
    return result_or_exception

  def is_exception(self):
    if self.exception is None:
      return False

    if isinstance(self.exception, Exception):
      return True
  
    return False
