from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("id", "title", "text", "video_url", "image_url", "author", "score", "state", "sub_id", "tag", "publication_date")
    class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Post.PostState]
        LOCKED: _ClassVar[Post.PostState]
        HIDDEN: _ClassVar[Post.PostState]
    NORMAL: Post.PostState
    LOCKED: Post.PostState
    HIDDEN: Post.PostState
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUB_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    text: str
    video_url: str
    image_url: str
    author: str
    score: int
    state: Post.PostState
    sub_id: str
    tag: str
    publication_date: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Post.PostState, str]] = ..., sub_id: _Optional[str] = ..., tag: _Optional[str] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("id", "host_id", "text", "author", "score", "state", "publication_date")
    class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Comment.CommentState]
        HIDDEN: _ClassVar[Comment.CommentState]
    NORMAL: Comment.CommentState
    HIDDEN: Comment.CommentState
    ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    host_id: str
    text: str
    author: str
    score: int
    state: Comment.CommentState
    publication_date: str
    def __init__(self, id: _Optional[str] = ..., host_id: _Optional[str] = ..., text: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Comment.CommentState, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ("id", "sub_name", "state", "tags")
    class SubState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUBLIC: _ClassVar[Subreddit.SubState]
        PRIVATE: _ClassVar[Subreddit.SubState]
        HIDDEN: _ClassVar[Subreddit.SubState]
    PUBLIC: Subreddit.SubState
    PRIVATE: Subreddit.SubState
    HIDDEN: Subreddit.SubState
    ID_FIELD_NUMBER: _ClassVar[int]
    SUB_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    sub_name: str
    state: Subreddit.SubState
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., sub_name: _Optional[str] = ..., state: _Optional[_Union[Subreddit.SubState, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url", "author", "sub_id", "tag")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SUB_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: str
    sub_id: str
    tag: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[str] = ..., sub_id: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ("post_id", "user_id", "if_upvote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IF_UPVOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    user_id: str
    if_upvote: bool
    def __init__(self, post_id: _Optional[str] = ..., user_id: _Optional[str] = ..., if_upvote: bool = ...) -> None: ...

class VotePostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class GetPostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("host_id", "text", "author")
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    host_id: str
    text: str
    author: str
    def __init__(self, host_id: _Optional[str] = ..., text: _Optional[str] = ..., author: _Optional[str] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ("comment_id", "user_id", "if_upvote")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IF_UPVOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    user_id: str
    if_upvote: bool
    def __init__(self, comment_id: _Optional[str] = ..., user_id: _Optional[str] = ..., if_upvote: bool = ...) -> None: ...

class VoteCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class GetNCommentsRequest(_message.Message):
    __slots__ = ("post_id", "n")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    n: int
    def __init__(self, post_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class GetNCommentsResponse(_message.Message):
    __slots__ = ("comments",)
    class CommentWithReplies(_message.Message):
        __slots__ = ("comment", "if_has_replies")
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        IF_HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
        comment: Comment
        if_has_replies: bool
        def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ..., if_has_replies: bool = ...) -> None: ...
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[GetNCommentsResponse.CommentWithReplies]
    def __init__(self, comments: _Optional[_Iterable[_Union[GetNCommentsResponse.CommentWithReplies, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("comment_id", "n")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    n: int
    def __init__(self, comment_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class ExpandCommentBranchResponse(_message.Message):
    __slots__ = ("comments",)
    class CommentWithReplies(_message.Message):
        __slots__ = ("comment", "replies")
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        REPLIES_FIELD_NUMBER: _ClassVar[int]
        comment: Comment
        replies: _containers.RepeatedCompositeFieldContainer[Comment]
        def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ..., replies: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[ExpandCommentBranchResponse.CommentWithReplies]
    def __init__(self, comments: _Optional[_Iterable[_Union[ExpandCommentBranchResponse.CommentWithReplies, _Mapping]]] = ...) -> None: ...

class MonitorUpdatesRequest(_message.Message):
    __slots__ = ("post_id", "comment_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    comment_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, post_id: _Optional[str] = ..., comment_id: _Optional[_Iterable[str]] = ...) -> None: ...

class MonitorUpdatesResponse(_message.Message):
    __slots__ = ("post_score", "comment_score")
    POST_SCORE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
    post_score: int
    comment_score: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, post_score: _Optional[int] = ..., comment_score: _Optional[_Iterable[int]] = ...) -> None: ...
