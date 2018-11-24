
schemas = {
    "register": {
        "type": "object",
        "properties": {
            "numberof": {
                "type": "number"
            }
        }
        ,
        "required": ["numberof"]
    },
    "generate": {
        "type": "object",
        "properties": {
            "numberof": {
                "type": "number"
            }
        }
        ,
        "required": ["numberof"]
    },
    "begin_game": {
        "type": "object",
        "properties": {
            "bid": {
                "type": "number"
            }
        },
        "required": ["bid"]
    },
    "action_in_game": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["split", "double_down", "hit", "stand"]
            }
        },
        "required": ["action"]
    }
}
