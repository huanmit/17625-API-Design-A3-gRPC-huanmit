"""Implement a high level function:
● Retrieve a post
● Retrieve most upvoted comments under the post
● Expand the most upvoted comment
● Return the most upvoted reply under the most upvoted comment, or None if there are no comments or
no replies under the most upvoted one.

The function should accept an instance of the API client to 
perform make these calls. This way, the function doesn’t need 
to maintain awareness of any technical details of the API - such 
as whether it uses REST, graphQL or gRPC under the hood, what server 
(if any) it talks to, etc.
"""

def high_level_api_utils(client, post_id, n):
    """
    Implement the high level function.
    """
    # retrieve the post
    post = client.get_post(post_id)
    if not post or "err_message" in post:
        return None
    
    # retrieve most upvoted comments
    most_upvoted_comments = client.get_n_comments(post_id, n)
    if not most_upvoted_comments or any("err_message" in comment for comment in most_upvoted_comments):
        return None
    
    # expand the most upvoted comment
    one_most_upvoted_comment = client.expand_comment_branch(most_upvoted_comments[0]["comment"]["id"], n)
    if not one_most_upvoted_comment or "err_message" in one_most_upvoted_comment:
        return None

    # Return the most upvoted reply under the most upvoted comment
    one_most_upvoted_reply = one_most_upvoted_comment[0]["replies"][0] if one_most_upvoted_comment[0]["replies"] else None

    return {
        "post": post,
        "most_upvoted_comments": most_upvoted_comments,
        "one_most_upvoted_comment": one_most_upvoted_comment,
        "one_most_upvoted_reply": one_most_upvoted_reply
    }
