"""
This test checks the business logic of high_level_api_utils, even when the API is not accessible 
This is achieved by using a Mock object to mimic API client object interfaces.
"""
import unittest
from unittest.mock import Mock

from api_utils import high_level_api_utils

class TestHighLevelApiUtils(unittest.TestCase):
    
    def setUp(self):
        self.mock_client = Mock()

    def test_no_post_found(self):
        # Scenario where no post is found
        self.mock_client.get_post.return_value = {"err_message": "Post not found"}
        result = high_level_api_utils(self.mock_client, "non_existent_post_id", 1)
        self.assertIsNone(result)

    def test_no_comments_found(self):
        # Scenario where post is found but no comments are present
        self.mock_client.get_post.return_value = {}  # Return an empty dictionary to simulate a found post
        self.mock_client.get_n_comments.return_value = {"err_message": "No comments found"}

        result = high_level_api_utils(self.mock_client, "post_id_with_no_comments", 1)
        self.assertIsNone(result)

    
    def test_no_replies_found(self):
        # Scenario where comments are found but no replies are present
        self.mock_client.get_post.return_value = {}
        self.mock_client.get_n_comments.return_value = [{"comment": {"id": "some_comment_id"}, "if_has_replies": False}]
        self.mock_client.expand_comment_branch.return_value = {"replies": []}

        result = high_level_api_utils(self.mock_client, "post_id", 1)

        self.assertIsNone(result)

    def test_successful_retrieval(self):
        # Scenario where everything is successfully retrieved
        self.mock_client.get_post.return_value = {
            "id": "post_id",
            "title": "Title",
            "text": "Text",
            "author": "Author",
            "score": 100,
            "state": "NORMAL",
            "sub_id": "sub_id",
            "tag": "Tag",
            "publication_date": "2023-12-01T12:00:00Z"
        }

        # Simulating getting the most upvoted comment
        self.mock_client.get_n_comments.return_value = [
            {
            "comment": {"id": "comment_id", "text": "comment_text", "score": 10},
            "if_has_replies": True
            },
            {
            "comment": {"id": "comment_id_2", "text": "comment_text_2", "score": 5},
            "if_has_replies": False
            }
        ]

        self.mock_client.expand_comment_branch.return_value = [{
            "comment": {"id": "comment_id", "text": "comment_text", "score": 10},
            "replies": [{"id": "reply_id", "text": "reply_text", "score": 5}]
        }]

        # Call the high-level function
        result = high_level_api_utils(self.mock_client, 'post_id', 1)

        # Assert that the result is not None and check if the most upvoted reply is correct
        self.assertIsNotNone(result)
        self.assertEqual(result["one_most_upvoted_reply"]["id"], 'reply_id')
        self.assertEqual(result["one_most_upvoted_reply"]["text"], 'reply_text')


if __name__ == '__main__':
    unittest.main()