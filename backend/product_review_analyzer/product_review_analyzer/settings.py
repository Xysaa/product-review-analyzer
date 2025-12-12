from pyramid.response import Response

def cors_tween_factory(handler, registry):
    allowed = registry.settings.get("cors.allowed_origins", "")

    def tween(request):
        origin = request.headers.get("Origin")

        if request.method == "OPTIONS":
            resp = Response()
        else:
            resp = handler(request)

        if origin and origin in allowed:
            resp.headers["Access-Control-Allow-Origin"] = origin
            resp.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        return resp

    return tween
