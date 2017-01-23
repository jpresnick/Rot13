import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)
def rot13(content):
	rot13 = ""
	for x in content:
		x = ord(x)
		if (x < 91 and x > 64):
			x += 13
			if x > 90:
				x = x - 26
		elif (x < 123 and x > 96):
			x += 13
			if x > 122:
				x = x - 26
		rot13 += chr(x)
	return rot13

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, tempalte, **kw):
		self.write(self.render_str(tempalte, **kw))

class MainPage(Handler):
	def get(self):
		content = self.request.get("content")
		self.render("main.html", content = content)

	def post(self):
		content = self.request.get("text")
		self.render('main.html', content = rot13(content))

app = webapp2.WSGIApplication([('/', MainPage),
								],
    							debug=True)