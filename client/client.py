import grpc
import sys
import os

# Adjust the import path to match your project structure
generated_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated'))
sys.path.insert(0, generated_path)
import reddit_pb2
import reddit_pb2_grpc

class RedditClient:
    def __init__(self, host='localhost', port='50051'):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = reddit_pb2_grpc.RedditStub(self.channel)
        print(f"Connected to server on {host}:{port}")

    def get_post(self, post_id):
        try:
            response = self.stub.GetPost(reddit_pb2.GetPostRequest(post_id=post_id))
            # transform the response to a dict
            post = {
                "id": response.post.id,
                "title": response.post.title,
                "text": response.post.text,
                "video_url": response.post.video_url if response.post.video_url else None,
                "image_url": response.post.image_url if response.post.image_url else None,
                "author": response.post.author if response.post.author else None,
                "score": response.post.score,
                "state": response.post.state,
                "sub_id": response.post.sub_id,
                "tag": response.post.tag,
                "publication_date": response.post.publication_date
            }
            return post
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}

    def create_post(self, title, text, subreddit, tag, video_url=None, image_url=None, author=None):
        try:
            response = self.stub.CreatePost(
                reddit_pb2.CreatePostRequest(title=title, text=text, sub_id=subreddit, 
                                             tag=tag, video_url=video_url, image_url=image_url, 
                                             author=author))
            post = {
                "id": response.post.id,
                "title": response.post.title,
                "text": response.post.text,
                "video_url": response.post.video_url if response.post.video_url else None,
                "image_url": response.post.image_url if response.post.image_url else None,
                "author": response.post.author if response.post.author else None,
                "score": response.post.score,
                "state": response.post.state,
                "sub_id": response.post.sub_id,
                "tag": response.post.tag,
                "publication_date": response.post.publication_date
            }
            return post
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}
    
    def vote_post(self, post_id, user_id, if_upvote):
        try:
            response = self.stub.VotePost(
                reddit_pb2.VotePostRequest(post_id=post_id, user_id=user_id, if_upvote=if_upvote))
            post = {
                "id": response.post.id,
                "title": response.post.title,
                "text": response.post.text,
                "video_url": response.post.video_url if response.post.video_url else None,
                "image_url": response.post.image_url if response.post.image_url else None,
                "author": response.post.author if response.post.author else None,
                "score": response.post.score,
                "state": response.post.state,
                "sub_id": response.post.sub_id,
                "tag": response.post.tag,
                "publication_date": response.post.publication_date
            }
            return post
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}

    def create_comment(self, host_id, text, author):
        try:
            response = self.stub.CreateComment(
                reddit_pb2.CreateCommentRequest(host_id=host_id, text=text, author=author))
            comment = {
                "id": response.comment.id,
                "host_id": response.comment.host_id,
                "text": response.comment.text,
                "author": response.comment.author,
                "score": response.comment.score,
                "state": response.comment.state,
                "publication_date": response.comment.publication_date
            }
            return comment
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}

    def vote_comment(self, comment_id, user_id, if_upvote):
        try:
            response = self.stub.VoteComment(
                reddit_pb2.VoteCommentRequest(comment_id=comment_id, user_id=user_id, 
                                              if_upvote=if_upvote))
            comment = {
                "id": response.comment.id,
                "host_id": response.comment.host_id,
                "text": response.comment.text,
                "author": response.comment.author,
                "score": response.comment.score,
                "state": response.comment.state,
                "publication_date": response.comment.publication_date
            }
            return comment
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}
    
    def get_n_comments(self, post_id, n):
        try:
            response = self.stub.GetNComments(
                reddit_pb2.GetNCommentsRequest(post_id=post_id, n=n))
            list_of_comments_with_replies = []
            for comment_with_replies in response.comments:
                comment = {
                    "id": comment_with_replies.comment.id,
                    "host_id": comment_with_replies.comment.host_id,
                    "text": comment_with_replies.comment.text,
                    "author": comment_with_replies.comment.author,
                    "score": comment_with_replies.comment.score,
                    "state": comment_with_replies.comment.state,
                    "publication_date": comment_with_replies.comment.publication_date
                }
                if_has_replies = comment_with_replies.replies
                list_of_comments_with_replies.append({"comment": comment, "if_has_replies": if_has_replies})
                
            return list_of_comments_with_replies
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}

    def expand_comment_branch(self, comment_id, n):
        try:
            response = self.stub.ExpandCommentBranch(
                reddit_pb2.ExpandCommentBranchRequest(comment_id=comment_id, n=n))
            list_of_comments_with_replies = []
            for comment_with_replies in response.comments:
                comment = {
                    "id": comment_with_replies.comment.id,
                    "host_id": comment_with_replies.comment.host_id,
                    "text": comment_with_replies.comment.text,
                    "author": comment_with_replies.comment.author,
                    "score": comment_with_replies.comment.score,
                    "state": comment_with_replies.comment.state,
                    "publication_date": comment_with_replies.comment.publication_date
                }
                replies = []
                for reply in comment_with_replies.replies:
                    reply = {
                        "id": reply.id,
                        "host_id": reply.host_id,
                        "text": reply.text,
                        "author": reply.author,
                        "score": reply.score,
                        "state": reply.state,
                        "publication_date": reply.publication_date
                    }
                    replies.append(reply)

                list_of_comments_with_replies.append({"comment": comment, "replies": replies})

            return list_of_comments_with_replies
        except grpc.RpcError as e:
            return {"err_message": f"RPC failed: {e.code()}, {e.details()}"}


if __name__ == '__main__':
    client = RedditClient('localhost', '50051')
    # Example usage
    post_response = client.get_post('post_id_11')
    if post_response != None:
        print(post_response)