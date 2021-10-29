""" Swagger documentation. """
REVERSE = {
    "parameters":[
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
