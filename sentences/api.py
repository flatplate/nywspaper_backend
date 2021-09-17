from flask import request
from flask_restful import Resource

from sentences.service import SentenceService


class SimilarSentences(Resource):
    def __init__(self, service: SentenceService):
        self.service = service

    def get(self):
        sentence_id = request.args.get('sentence_id', type=int)
        document_id = request.args.get('document_id', type=int)
        sentences = self.service.get_similar_sentences(document_id, sentence_id)

        return sentences  # TODO json stuff
