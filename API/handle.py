from flask import Response, json

class Handle:

    def success(self, output, status=200, mimetype='application/json'):
        return Response(output, status=status, mimetype=mimetype)

    def error(self, error_message, status=500, mimetype='application/json'):
        return Response(json.dumps({"error": {"message": error_message}}), status=status, mimetype=mimetype)