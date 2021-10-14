from flask import request, make_response
from flask_restful import Resource

from feedback.service import FeedbackService


class Feedback(Resource):
    def __init__(self, service: FeedbackService):
        self.service = service

    def post(self):
        # Get the parameters
        json_data = request.get_json()
        print(json_data)
        article_one_id = json_data["articleOneId"]
        article_two_id = json_data["articleTwoId"]
        sentence_one_id = json_data["sentenceOneId"]
        sentence_two_id = json_data["sentenceTwoId"]
        similarity = json_data["similarity"]
        feedback = json_data["feedback"]

        # Uuid should be defined in the cookies
        uuid = request.cookies.get("nywspaper_deviceId")
        print(request.cookies)
        if not uuid:
            uuid = self.service.get_new_uuid()

        # Add feedback using the service
        self.service.insert_paragraph_feedback(
            article_one_id,
            article_two_id,
            sentence_one_id,
            sentence_two_id,
            similarity,
            feedback,
            uuid
        )

        # Return set-cookie headers either way to make sure the new cookie is set

        response = make_response({})
        response.set_cookie("nywspaper_deviceId", uuid)
        return response
