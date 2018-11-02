# sample.py

import falcon

class GoogleDriveResource:
    def on_get(self, req, resp):
        print(req)
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        print(req)

app = falcon.API()
app.add_route('/google-drive', GoogleDriveResource())
