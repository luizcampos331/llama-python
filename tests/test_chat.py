import unittest
from unittest.mock import MagicMock, patch
from src.chat import LlamaChat

class TestLlamaChat(unittest.TestCase):
  @patch("src.chat.chat")
  def test_get_response(self, mock_chat_response):
    mock_response = MagicMock()
    mock_response.message = MagicMock(content="I'm fine, thank you!")
    mock_chat_response.return_value = mock_response


    llama_chat = LlamaChat()
    messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
    response = llama_chat.get_response(messages)

    self.assertEqual(response, "I'm fine, thank you!")

    mock_chat_response.assert_called_once_with(
      model="llama3.2",
      messages=messages,
    )

if __name__ == "__main__":
  unittest.main()