# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_post_with_valid_details_returns_post_details post_details'] = {
    'comments': [
        {
            'comment_content': 'comment_content_0',
            'comment_id': 1,
            'commented_at': '2020-04-18 00:00:00',
            'commenter': {
                'name': 'user0',
                'profile_pic': 'profile_pic0',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'type': [
                    'HAHA'
                ]
            },
            'replies': [
                {
                    'comment_content': 'comment_content_3',
                    'comment_id': 4,
                    'commented_at': '2020-04-18 00:00:00',
                    'commenter': {
                        'name': 'user0',
                        'profile_pic': 'profile_pic0',
                        'user_id': 1
                    },
                    'reactions': {
                        'count': 1,
                        'type': [
                            'THUMBS-DOWN'
                        ]
                    }
                }
            ],
            'replies_count': 1
        }
    ],
    'comments_count': 1,
    'post_content': 'post_content_0',
    'post_id': 1,
    'posted_at': '2020-04-18 00:00:00',
    'posted_by': {
        'name': 'user0',
        'profile_pic': 'profile_pic0',
        'user_id': 1
    },
    'reactions': {
        'count': 2,
        'type': [
            'LIKE',
            'THUMBS-UP'
        ]
    }
}
