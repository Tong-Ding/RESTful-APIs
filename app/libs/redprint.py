class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):   # f是装饰器作用的方法
            self.mound.append((f, rule, options))   # rule是参数内的url
            return f

        return decorator

    def register(self, bp, url_prefix=None):    # bp是blueprint
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
