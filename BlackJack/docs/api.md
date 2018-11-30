# API Overview

|                       |        |                        |                                       |
|:--------------------- | ------:|:---------------------- |:------------------------------------- |
| [generate](#generate) | `POST` | `/generate`            | Generate data `uid`.                  |
| [register](#register) | `POST` | `/register`            | Register new player and obtain `uid`. |
| [begin](#begin)       | `POST` | `/player/<uid>/begin`  | Begin new deal with specified `bid`.  |
| [action](#action)     | `POST` | `/player/<uid>/action` | Perform `action`.                     |
| [finish](#finish)     | `POST` | `/player/<uid>/finish` | Finish game                           |

# API
Blackjack API is failry simple. Using only three endpoints we are able to play game continously.
To play we first have to [register](#register) our player as return obtaining unique id.
To [begin](#begin) new card deal we have to privide amount of money for bid.
It's now possible to perform one of [actions](#action) in main game loop.

## <a id="register"></a> `POST`  `/generate` 
If you want only generate data.
### Request JSON
```javascript
Generate
{
    "numberof": number
}
```
### Response JSON
```javascript
{
    "header": "data was generate in C: Users Public"
}
```

## <a id="register"></a> `POST`  `/register` 
First you need to register player and obtain `uid` that will allow to perform further actions.
### Request JSON
```javascript
Register
{
    "cash": number
}
```
### Response JSON
```javascript
{
    "header": "confirm_register",
    "uid": number
}
```

## <a id="begin"></a> `POST` `/player/<uid>/begin`
Beginning new game (deal) is only possible if table is in `awaiting` or `end_game` state.
### Request JSON
```javascript
Begin
{
    "bid": number
}
```
### Response JSON
[`Table`](#table)

## <a id="action"></a> `POST` `/player/<uid>/action`
Perform one of available actions.
### Request JSON
```javascript
Action
{
    "action": string  # split, double_down, stand1, stand2, hit1, hit2, insure, surrender, end_game
}
```
### Response JSON
[`Table`](#table)

## <a id="action"></a> `POST` `/player/<uid>/finish`
Finish game.
### Request JSON
```javascript
Action
{
    "uid": number
}
```
### Response JSON
[`Score`](#score)

## Structures

### Error
If some operation was not allowed of caused error that should be handled by client then this error message is returned with `400` return code.
```javascript
{
    "header": "error",
    "message": string
}
```

### Table
```javascript
Table
{
    "header": "success"
    "state": State,
    "player": Player,
    "croupier": Croupier
}
```

```javascript
State
{
    "phase": string,
    "bid": number,
    "winnings": number
}
```

```javascript
Player
{
    "hands": [Hand],
    "current_hand": Hand,
    "account_balance": number
}
```

```javascript
Croupier
{
    "hand": Hand
}
```

```javascript
Hand
{
    "cards": [Card],
    "value": number,
    "playing": boolean
}
```

```javascript
Card
{
    "color": string,
    "rank": string
}
```
### Score
```javascript
Table
{
    "player_score": Player_score,
    "bots_score": Bots_score
}
```

```javascript
Player_score
{
    "winning": number,
    "draw": number,
    "loosing": number
}
```

```javascript
Bots_score
{
    "name": string,
    "score": Bot_result
}
```

```javascript
bot_result
{
    "winning": number,
    "draw": number,
    "loosing": number
}
```