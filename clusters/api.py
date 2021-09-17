from flask_restful import Resource
from clusters.service import StoryService
from flask import request


class Stories(Resource):
    def __init__(self, service: StoryService):
        self.service = service

    def get(self):
        offset = request.args.get('offset')
        if offset:
            offset = int(offset)
        else:
            offset = 0
        stories = self.service.get_top_stories(offset=offset)
        return stories  # TODO json stuff
