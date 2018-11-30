
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
                "enum": ["split", "double_down", "hit1", "hit2", "stand1", "stand2", "end_game", "insure", "surrender"]
            }
        },
        "required": ["action"]
    },
    "finish_game": {
        "type": "object",
        "properties": {
            "uid": {
                "type": "number"
            }
        }
    },
}
