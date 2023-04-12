def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message == 'hi':
        return 'hi!'
    if p_message == 'ping':
        return 'pong'
    return "Please give a valid input"
    
