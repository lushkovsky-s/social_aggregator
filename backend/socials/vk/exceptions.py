class VKParserError(Exception): pass

class VideoParsingError(VKParserError): pass
class APIResponseError(VKParserError): pass