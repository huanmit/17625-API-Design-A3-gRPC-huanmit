class SampleData:
    posts = [
        {
            "id": "post_id_1",
            "title": "Title 1",
            "text": "Text 1",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "author": "Author 1",
            "score": 10,
            "state": "NORMAL",
            "sub_id": "sub_id_1",
            "tag": "Tag 1",
            "publication_date": "2023-12-01T12:00:00Z"
        },
        {
            "id": "post_id_2",
            "title": "Title 2",
            "text": "Text 2",
            "image_url": "https://i.imgur.com/2Yw2WvO.jpeg",
            "score": 20,
            "state": "LOCKED",
            "sub_id": "sub_id_2",
            "tag": "Tag 2",
            "publication_date": "2023-12-02T12:00:00Z"
        },
        {
            "id": "post_id_3",
            "title": "Title 3",
            "text": "Text 3",
            "score": 30,
            "state": "HIDDEN",
            "sub_id": "sub_id_3",
            "tag": "Tag 3",
            "publication_date": "2023-12-03T12:00:00Z"
        },
        {
            "id": "post_id_4",
            "title": "Title 4",
            "text": "Text 4",
            "image_url": "https://i.imgur.com/2Yw2WvO.jpeg",
            "author": "Author 4",
            "score": 40,
            "state": "NORMAL",
            "sub_id": "sub_id_4",
            "tag": "Tag 4",
            "publication_date": "2023-12-04T12:00:00Z"
        },
        {
            "id": "post_id_5",
            "title": "Title 5",
            "text": "Text 5",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "author": "Author 5",
            "score": 50,
            "state": "LOCKED",
            "sub_id": "sub_id_5",
            "tag": "Tag 5",
            "publication_date": "2023-12-05T12:00:00Z"
        },
        {
            "id": "post_id_6",
            "title": "Title 6",
            "text": "Text 6",
            "author": "Author 6",
            "score": 60,
            "state": "HIDDEN",
            "sub_id": "sub_id_6",
            "tag": "Tag 6",
            "publication_date": "2023-12-06T12:00:00Z"
        },
        {
            "id": "post_id_7",
            "title": "Title 7",
            "text": "Text 7",
            "author": "Author 7",
            "score": 70,
            "state": "NORMAL",
            "sub_id": "sub_id_7",
            "tag": "Tag 7",
            "publication_date": "2023-12-07T12:00:00Z"
        },
        {
            "id": "post_id_8",
            "title": "Title 8",
            "text": "Text 8",
            "author": "Author 8",
            "score": 80,
            "state": "LOCKED",
            "sub_id": "sub_id_8",
            "tag": "Tag 8",
            "publication_date": "2023-12-08T12:00:00Z"
        },
        {
            "id": "post_id_9",
            "title": "Title 9",
            "text": "Text 9",
            "author": "Author 9",
            "score": 90,
            "state": "HIDDEN",
            "sub_id": "sub_id_9",
            "tag": "Tag 9",
            "publication_date": "2023-12-09T12:00:00Z"
        },
        {
            "id": "post_id_10",
            "title": "Title 10",
            "text": "Text 10",
            "author": "Author 10",
            "score": 100,
            "state": "NORMAL",
            "sub_id": "sub_id_10",
            "tag": "Tag 10",
            "publication_date": "2023-12-10T12:00:00Z"
        }
    ]

    
    users = [
        {"id": "user1"}, {"id": "user2"}, {"id": "user3"},
        {"id": "user4"}, {"id": "user5"}, {"id": "user6"},
    ]

    subs = [
        {"id": "sub1"}, {"id": "sub2"}, {"id": "sub3"},
        {"id": "sub4"}, {"id": "sub5"}, {"id": "sub6"},
    ]

    comments = [
        {
            "id": "comment_id_1",
            "host_id" : "post_id_1",
            "text": "This is a comment",
            "author": "Huanmi",
            "score": 10,
            "state": "NORMAL",
            "publication_date": "2023-12-01T12:00:00Z"
        },
        {
            "id": "comment_id_2",
            "host_id" : "comment_id_1",
            "text": "This is a comment",
            "author": "Huanmi",
            "score": 20,
            "state": "NORMAL",
            "publication_date": "2023-12-02T12:00:00Z"
        },
        {
            "id": "comment_id_3",
            "host_id" : "comment_id_1",
            "text": "This is a comment",
            "author": "Huanmi",
            "score": 30,
            "state": "NORMAL",
            "publication_date": "2023-12-03T12:00:00Z"
        },
        {
            "id": "comment_id_4",
            "host_id" : "comment_id_2",
            "text": "This is a comment",
            "author": "Huanmi",
            "score": 40,
            "state": "NORMAL",
            "publication_date": "2023-12-04T12:00:00Z"
        }
    ]