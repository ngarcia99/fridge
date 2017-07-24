import webapp2
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class HomeHandler(webapp2.RequestHandler):
    def get (self):
        print('hi')
        template = env.get_template('homepage.html')
        self.response.out.write(template.render())

class NewFoodHandler(webapp2.RequestHandler):
    def get (self):
        newfood_template = env.get_template('newfood.html')
        self.response.out.write(newfood_template.render())

    def post(self):
        submit_template = env.get_template('submit.html')
        submitted_variables = {
            'foodname':self.request.get("foodname"),
            'category':self.request.get("category"),
            'expire_date':self.request.get("expire_date"),
        }
        self.response.out.write(submit_template.render(submitted_variables))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/newfood', NewFoodHandler)
], debug=True)
