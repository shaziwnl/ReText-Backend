from openaiapi import chat_completion
import json


def verbose_handler(data):
    
    sentence = data.get("sentence")

    return {
        "statusCode": 200,
        "body": json.dumps({"completion": chat_completion(
            "You are a writing assistant that adds detail to texts. Add details to the following text", 
            sentence
        )})
    }


def concise_handler(data):
    
    sentence = data.get("sentence")

    return {
        "statusCode": 200,
        "body": json.dumps({"completion": chat_completion(
            "You are a writing assistant that helps make texts more concise. Make the following text more short and concise", 
            sentence
        )})
    }


def rectify_handler(data):
    
    sentence = data.get("sentence")

    return {
        "statusCode": 200,
        "body": json.dumps({"completion": chat_completion(
            "You are a writing assistant that helps the user with correcting grammatical mistakes in their text. Correct the mistakes in the following text", 
            sentence
        )})
    }


def formalize_handler(data):
    
    sentence = data.get("sentence")

    return {
        "statusCode": 200,
        "body": json.dumps({"completion": chat_completion(
            "I need to send a message to my boss. Please make the following message more formal", 
            sentence
        )})
    }