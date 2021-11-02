""" Swagger documentation. """
REVERSE_FAST_GET = {
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

REVERSE_FAST_POST = {
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

REVERSE_SLOW_GET = {
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
            "description": "Task details including the task id."
        }
    },
}
