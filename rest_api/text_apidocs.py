""" Swagger documentation. """
REVERSE_GET = {
    "parameters": [
        {
            "in": "path",
            "name": "string_to_reverse",
            "description": "The string you want to reverse.",
            "required": True,
            "type": "string"
        }
    ],
    "responses": {
        "200": {
            "description": "Your string but reversed."
        }
    },
}

REVERSE_POST = {
    "parameters": [
        {
            "in": "path",
            "name": "string_to_reverse",
            "description": "The string you want to reverse.",
            "required": True,
            "type": "string"
        }
    ],
    "responses": {
        "200": {
            "description": "Your string but reversed."
        }
    },
}
