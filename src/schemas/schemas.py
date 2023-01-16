POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'title': {'type': 'string'}  # , 'enum': ['Post']
    },
    'required': ['id']
}

# {'id': 1, 'title': 'Post 1'}
