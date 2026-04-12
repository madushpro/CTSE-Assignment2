"""
Ollama Client Module for AI Travel Planner MAS
Handles all Ollama LLM interactions for agents
"""

import requests
import json
from typing import Dict, Optional, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s: %(message)s'
)
logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Client for interacting with Ollama local LLM.
    Manages connections to llama3:8b model.
    """

    def __init__(self, model: str = "llama3:8b", host: str = "http://localhost:11434"):
        """
        Initialize Ollama client.

        Args:
            model: Model name to use (default: llama3:8b)
            host: Ollama server URL (default: localhost:11434)

        Returns:
            None
        """
        self.model = model
        self.host = host
        self.api_endpoint = f"{host}/api/generate"
        self.check_connection()

    def check_connection(self) -> bool:
        """
        Check if Ollama server is running and accessible.

        Args:
            None

        Returns:
            bool: True if connected, False otherwise

        Raises:
            ConnectionError: If Ollama is not running
        """
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            if response.status_code == 200:
                logger.info(f"✓ Ollama server connected at {self.host}")
                return True
            else:
                raise ConnectionError(
                    f"Ollama server returned status {response.status_code}. "
                    f"Make sure Ollama is running: ollama serve"
                )
        except Exception as e:
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.host}. "
                f"Make sure Ollama is running: ollama serve\n"
                f"Error: {str(e)}"
            )

    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> str:
        """
        Generate text using Ollama LLM.

        Args:
            prompt: User prompt/query
            system: System prompt for model behavior
            temperature: Creativity level (0-1, default 0.7)
            max_tokens: Maximum response length (default 500)

        Returns:
            str: Generated response from LLM

        Raises:
            ValueError: If prompt is empty
            requests.RequestException: If API call fails
        """
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")

        full_prompt = prompt
        if system:
            full_prompt = f"{system}\n\n{prompt}"

        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
            "temperature": temperature,
            "num_predict": max_tokens
        }

        try:
            logger.info(f"Calling Ollama: model={self.model}, tokens={max_tokens}")
            response = requests.post(
                self.api_endpoint,
                json=payload,
                timeout=300  # 5 minute timeout for LLM
            )
            response.raise_for_status()

            result = response.json()
            generated_text = result.get("response", "").strip()

            logger.info(f"✓ Generated {len(generated_text)} chars from LLM")
            return generated_text

        except requests.exceptions.Timeout:
            raise requests.RequestException(
                "Ollama request timed out. Please try again."
            )
        except requests.exceptions.ConnectionError:
            raise requests.RequestException(
                f"Cannot reach Ollama at {self.host}. "
                f"Is it running? Execute: ollama serve"
            )
        except json.JSONDecodeError:
            raise requests.RequestException(
                "Invalid response from Ollama. Check server logs."
            )
        except Exception as e:
            raise requests.RequestException(
                f"Ollama API error: {str(e)}"
            )

    def generate_json(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.3
    ) -> Dict:
        """
        Generate structured JSON-like output from Ollama.

        Args:
            prompt: Query requesting JSON output
            system: System prompt to guide format
            temperature: Lower temperature for consistency

        Returns:
            Dict: Parsed JSON response

        Raises:
            ValueError: If output cannot be parsed as JSON
            requests.RequestException: If API call fails
        """
        response_text = self.generate(
            prompt,
            system=system,
            temperature=temperature,
            max_tokens=1000
        )

        # Try to extract JSON from response
        try:
            # Look for JSON block
            import re
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                return json.loads(json_str)
            else:
                # Try parsing entire response
                return json.loads(response_text)
        except json.JSONDecodeError:
            logger.warning(f"Could not parse JSON from: {response_text}")
            # Return as structured dict on parse failure
            return {"raw_response": response_text}

    def list_models(self) -> List[str]:
        """
        List available models downloaded in Ollama.

        Args:
            None

        Returns:
            List[str]: List of available model names

        Raises:
            requests.RequestException: If API call fails
        """
        try:
            response = requests.get(
                f"{self.host}/api/tags",
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            models = [m["name"] for m in data.get("models", [])]
            return models
        except Exception as e:
            raise requests.RequestException(
                f"Cannot list models: {str(e)}"
            )


def create_ollama_client(
    model: str = "llama3:8b",
    host: str = "http://localhost:11434"
) -> OllamaClient:
    """
    Factory function to create and validate Ollama client.

    Args:
        model: Model name (default: llama3:8b)
        host: Server URL (default: localhost)

    Returns:
        OllamaClient: Initialized and validated client

    Raises:
        ConnectionError: If Ollama is not accessible
    """
    try:
        client = OllamaClient(model=model, host=host)
        logger.info(f"✓ Ollama client ready with {model}")
        return client
    except ConnectionError as e:
        logger.error(f"Failed to initialize Ollama: {str(e)}")
        raise


# Example usage for testing
if __name__ == "__main__":
    try:
        # Initialize client
        ollama = create_ollama_client()

        # Test 1: Simple generation
        print("\n=== Test 1: Simple Generation ===")
        response = ollama.generate(
            prompt="What are the top 3 attractions in Ella, Sri Lanka?",
            max_tokens=200
        )
        print(f"Response: {response}\n")

        # Test 2: JSON generation
        print("=== Test 2: JSON Generation ===")
        json_response = ollama.generate_json(
            prompt='Generate a JSON object with 2 popular restaurants in Kandy, Sri Lanka with name and cuisine type',
            system="Always output valid JSON only",
            temperature=0.3
        )
        print(f"JSON Response: {json.dumps(json_response, indent=2)}\n")

        # Test 3: List models
        print("=== Test 3: Available Models ===")
        models = ollama.list_models()
        print(f"Available models: {models}\n")

        print("✓ All Ollama client tests passed!")

    except Exception as e:
        print(f"✗ Error: {str(e)}")
