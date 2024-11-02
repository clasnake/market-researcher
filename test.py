# Experimental code to play with the Bedrock API, to remove later

import boto3
import dotenv
import os
import json


dotenv.load_dotenv()

aws_session_token = os.getenv('AWS_SESSION_TOKEN')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')


bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# response = bedrock.list_foundation_models(byProvider="anthropic")

# for summary in response["modelSummaries"]:
#     print(summary["modelId"])

model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

# Start a conversation with the user message.
user_message = "Tell me something about the weather in Tokyo"
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    # response = bedrock.converse(
    #     modelId=model_id,
    #     messages=conversation,
    #     inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    # )

    # # Extract and print the response text.
    # response_text = response["output"]["message"]["content"][0]["text"]
    # print(response_text)

    response = bedrock.converse(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'text': 'Search the web for the top 3 companies involved in RFP Automation leverating AI, using the Chrome browser opened'
                    }
                ]
            }
        ],
        additionalModelRequestFields={
            "tools": [
                {
                    "type": "computer_20241022",
                    "name": "computer",
                    "display_height_px": 768,
                    "display_width_px": 1024,
                    "display_number": 0
                },
                {
                    "type": "bash_20241022",
                    "name": "bash",

                },
                {
                    "type": "text_editor_20241022",
                    "name": "str_replace_editor",
                }
            ],
            "anthropic_beta": ["computer-use-2024-10-22"]
        })

    print(json.dumps(response, indent=4))

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
