from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    """
    This class adds support for lazy translation texts to Flask's
    JSON encoder. This is necessary when flashing translated texts.
    """
    
    def default(self, obj):
        from speaklater import is_lazy_string
        if is_lazy_string(obj):
            try:
                return unicode(obj)  # python 2
            except NameError:
                return str(obj)  # python 3
        return super(CustomJSONEncoder, self).default(obj)

