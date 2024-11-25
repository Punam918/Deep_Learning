def encode_parseltongue(message):
    # Initialize the encoded message
    encoded_message = ""
    
    # Iterate through each character in the message
    for char in message:
        # Append the character to the encoded message
        encoded_message += char
        
        # Append "sss" if the character is "s" or "w"
        if char == 's' or char == 'w' or char == 'h' or char == 'e' or char == 'r' or char == 'a'  or char == 'y' or char == 'o' or char == 'u':
            encoded_message += "sss"
    
    return encoded_message

# Example usage
input_message = "where are you"
encoded_message = encode_parseltongue(input_message)
print(encoded_message)  # Output should be "wsshsssesssrsssesss asssrsssesss ysssosssusss"
