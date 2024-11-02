import boto3
import dotenv
import os
import json
from utils import retry
import logging

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BedrockProvider:
    def __init__(self, model_id: str = "anthropic.claude-3-5-sonnet-20241022-v2:0"):
        self.model_id = model_id
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'))

    def converse_with_computer_use(self, prompt: str) -> str:
        """
        Converse with the computer.
        TODO: Make computer use work on Mac Chrome and define the response format
        TODO: Optimize on system prompt
        TODO: Increase max_attempts later after we test the model more, also add timeout
        """
        @retry(max_attempts=1, delay=4.0, exponential_backoff=False, logger=logger.info)
        def _converse_inner() -> str:
            response = self.bedrock.converse(
                modelId=self.model_id,
                messages=[
                    {
                        'role': 'user',
                        'content': [{'text': prompt}]
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
            
            return json.dumps(response, indent=4)

        return _converse_inner()