from flask_restful import Resource
from clusters.service import StoryService


class Stories(Resource):
    def __init__(self, service: StoryService):
        self.service = service

    def get(self):
        stories = self.service.get_top_stories()
        return stories  # TODO json stuff
