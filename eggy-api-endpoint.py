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

class StaticResource:
    STATIC_FILES_PATH = 'static_files'
    file_to_read = 'index.html'

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open("%s/%s" % (self.STATIC_FILES_PATH, self.file_to_read), 'r') as f:
            resp.body = f.read()

class HomePageResource(StaticResource):
   file_to_read = 'home-page.html' 

class TermsOfServiceResource(StaticResource):
   file_to_read = 'terms-of-service.html' 

class ApplicationPrivacyResource(StaticResource):
   file_to_read = 'application-privacy-policy.html' 

app = falcon.API()
app.add_route('/google-drive', GoogleDriveResource())
app.add_route('/home-page', HomePageResource())
app.add_route('/application-privacy-policy', ApplicationPrivacyResource())
app.add_route('/terms-of-service', TermsOfServiceResource())
