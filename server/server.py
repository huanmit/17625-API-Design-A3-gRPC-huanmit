"""The Python implementation of the gRPC Reddit server by Huanmi."""

import datetime
import logging
from concurrent import futures
import random
import argparse
import grpc
import sys
import os


# Add the 'generated' directory to sys.path
generated_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated'))
sys.path.insert(0, generated_path)
import reddit_pb2
import reddit_pb2_grpc

from sample_data import *


# now from the dir ""../generated" import reddit_pb2
# from ..generated import reddit_pb2
#from generated import reddit_pb2_grpc


class RedditService(reddit_pb2_grpc.RedditServicer):
    """Provides methods that implement functionality of reddit server."""
    sample_data = SampleData()

    def GetPost(self, request, context):
        print(f"GetPost called with id {request.post_id}")
        posts = self.sample_data.posts
        
        for post in posts:
            if post["id"] == request.post_id:
                # transform post into reddit_pb2.Post
                res_post = reddit_pb2.Post(id=post["id"], title=post["title"], text=post["text"], 
                                           video_url=post["video_url"] if "video_url" in post else None,
                                           image_url=post["image_url"] if "image_url" in post else None,
                                           author=post["author"] if "author" in post else None, 
                                           score=post["score"], state=post["state"], sub_id=post["sub_id"], 
                                           tag=post["tag"], publication_date=post["publication_date"])

                return reddit_pb2.GetPostResponse(post=res_post)
            
        # raise error if post not found and in the message says "Post not found"
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f"Post with ID {request.post_id} not found")
        return reddit_pb2.GetPostResponse()  # Return an empty response
    
    def CreatePost(self, request, context):
        print(f"CreatePost called with title {request.title}")
        post = {
            "title": request.title,
            "text": request.text,
            "sub_id": request.sub_id,
            "tag": request.tag,
        }
        try:
            post["author"] = request.author
            post["video_url"] = request.video_url
            post["image_url"] = request.image_url
        except:
            pass

        post["id"] = f"post_id_{random.randint(1, 9999)}"
        post["score"] = 0
        post["state"] = "NORMAL"
        # get current time
        post["publication_date"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

        self.sample_data.posts.append(post)
        res_post = reddit_pb2.Post(id=post["id"], title=post["title"], text=post["text"], 
                                           video_url=post["video_url"] if "video_url" in post else None,
                                           image_url=post["image_url"] if "image_url" in post else None,
                                           author=post["author"] if "author" in post else None, 
                                           score=post["score"], state=post["state"], sub_id=post["sub_id"], 
                                           tag=post["tag"], publication_date=post["publication_date"])
        
        return reddit_pb2.CreatePostResponse(post=res_post)

    def VotePost(self, request, context):
        print(f"VotePost called with id {request.post_id}")
        posts = self.sample_data.posts
        
        for post in posts:
            if post["id"] == request.post_id:
                # transform post into reddit_pb2.Post
                if request.if_upvote == True:
                    post["score"] += 1
                else:
                    post["score"] -= 1
            
                res_post = reddit_pb2.Post(id=post["id"], title=post["title"], text=post["text"], 
                                           video_url=post["video_url"] if "video_url" in post else None,
                                           image_url=post["image_url"] if "image_url" in post else None,
                                           author=post["author"] if "author" in post else None, 
                                           score=post["score"], state=post["state"], sub_id=post["sub_id"], 
                                           tag=post["tag"], publication_date=post["publication_date"])

                return reddit_pb2.VotePostResponse(post=res_post)
        
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f"Post with ID {request.post_id} not found")
        return reddit_pb2.VotePostResponse()

    def CreateComment(self, request, context):
        print(f"CreateComment called with text {request.text}")
        comment = {
            "host_id": request.host_id,
            "text": request.text,
            "author": request.author,
        }

        comment["id"] = f"comment_id_{random.randint(1, 9999)}"
        comment["score"] = 0
        comment["state"] = "NORMAL"
        comment["publication_date"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

        self.sample_data.comments.append(comment)
        res_comment = reddit_pb2.Comment(id=comment["id"], host_id=comment["host_id"], text=comment["text"], 
                                         author=comment["author"], score=comment["score"], state=comment["state"],
                                         publication_date=comment["publication_date"])
        
        return reddit_pb2.CreateCommentResponse(comment=res_comment)
    
    def VoteComment(self, request, context):
        print(f"VoteComment called with id {request.comment_id}")
        comments = self.sample_data.comments
        
        for comment in comments:
            if comment["id"] == request.comment_id:
                # transform comment into reddit_pb2.Comment
                if request.if_upvote == True:
                    comment["score"] += 1
                else:
                    comment["score"] -= 1
            
                res_comment = reddit_pb2.Comment(id=comment["id"], host_id=comment["host_id"], text=comment["text"], 
                                                 author=comment["author"], score=comment["score"], state=comment["state"],
                                                 publication_date=comment["publication_date"])

                return reddit_pb2.VoteCommentResponse(comment=res_comment)
        
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f"Comment with ID {request.comment_id} not found")
        return reddit_pb2.VoteCommentResponse()

    def GetNComments(self, request, context):
        print(f"GetNComments called with post_id {request.post_id}")
        comments = self.sample_data.comments
        comments_under_this_post = []
        res_comments = []
        for comment in comments:
            if comment["host_id"] == request.post_id:
                comments_under_this_post.append(comment)

        # sort the comments by score, descending
        comments_under_this_post.sort(key=lambda x: x["score"], reverse=True)
        # get top n comments
        try:
            res_comments = comments_under_this_post[:request.n]
        # if n is greater than the number of comments, return all comments
        except:
            res_comments = comments_under_this_post
        
        list_comment_with_replies = []

        for comment in res_comments:
            # see if the comment has any replies
            if_has_replies = False
            for reply in comments:
                if reply["host_id"] == comment["id"]:
                    if_has_replies = True
                    break
            comment_with_replies = reddit_pb2.GetNCommentsResponse.CommentWithReplies(
                comment=reddit_pb2.Comment(id=comment["id"], host_id=comment["host_id"], text=comment["text"], 
                                                 author=comment["author"], score=comment["score"], state=comment["state"],
                                                 publication_date=comment["publication_date"]),
                if_has_replies=if_has_replies
            )
            list_comment_with_replies.append(comment_with_replies)
        
        return reddit_pb2.GetNCommentsResponse(comments=list_comment_with_replies)

    def ExpandCommentBranch(self, request, context):
        print(f"ExpandCommentBranch called with comment_id {request.comment_id}")
        comments = self.sample_data.comments
        comments_under_host_comment_l1 = []

        for comment in comments:
            if comment["host_id"] == request.comment_id:
                comments_under_host_comment_l1.append(comment)

        # sort the comments by score, descending
        comments_under_host_comment_l1.sort(key=lambda x: x["score"], reverse=True)
        # get top n comments
        try:
            top_n_comments_l1 = comments_under_host_comment_l1[:request.n]
        # if n is greater than the number of comments, return all comments
        except:
            top_n_comments_l1 = comments_under_host_comment_l1

        list_comment_with_replies = []
        for comment in top_n_comments_l1:
            replies_under_a_comment_l2 = []
            
            for reply in comments:
                # fetch replies to this comment
                if reply["host_id"] == comment["id"]:
                    reply = reddit_pb2.Comment(id=reply["id"], host_id=reply["host_id"], text=reply["text"],
                                                  author=reply["author"], score=reply["score"], state=reply["state"],
                                                    publication_date=reply["publication_date"])
                    replies_under_a_comment_l2.append(reply)
            
            # store the comment(l1) with its replies (l2)
            comment_with_replies = reddit_pb2.ExpandCommentBranchResponse.CommentWithReplies(
                comment=reddit_pb2.Comment(id=comment["id"], host_id=comment["host_id"], text=comment["text"], 
                                                author=comment["author"], score=comment["score"], state=comment["state"],
                                                publication_date=comment["publication_date"]),
                replies=replies_under_a_comment_l2,
            )
            list_comment_with_replies.append(comment_with_replies)

        return reddit_pb2.ExpandCommentBranchResponse(comments=list_comment_with_replies)

    def MonitorUpdates(self, request_iterator, context):
        # deal with each request from the stream
        for request in request_iterator:
            print(f"MonitorUpdates called with post_id: {request.post_id} and comment_ids: {request.comment_id}")
            posts = self.sample_data.posts
            comments = self.sample_data.comments

            post_score = 0
            comment_score = []
            for post in posts:
                if post["id"] == request.post_id:
                    post_score = post["score"]
                    break
            
            for comment in comments:
                if comment["id"] in request.comment_id:
                    comment_score.append(comment["score"])
            
            yield reddit_pb2.MonitorUpdatesResponse(post_score=post_score, comment_score=comment_score)

def serve():
    # get port from command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="localhost", help="Host address to run the server")
    parser.add_argument("--port", type=str, default="50051", help="Port number to run the server")

    args = parser.parse_args()
    host = args.host
    port = args.port

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServicer_to_server(RedditService(), server)
    server.add_insecure_port(f'{host}:{port}')
    server.start()
    print(f"Reddit server started, listening on {host}:{port}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()