import webapp2

form="""
<form method="post">
What is your birthday?
<br>

<label>Month
<input type="text" name="month">
</label>

<label>Day
<input type="text" name="day">
</label>

<label>Year
<input type="text" name="year">
</label>

<div style="color: red">%(error)s</div>

<br>
<br>
<input type="submit">
</form>
"""

months = ['January',
		  'February',
		  'March',
		  'April',
		  'May',
		  'June',
		  'July',
	      'August',
		  'September',
		  'October',
		  'November',
		  'December']
		  
month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
	if month:
		short_month= month[:3].lower()
		return month_abbvs.get(short_month)
			
			
			
def valid_day(day):
	if day and day.isdigit():
		day = int(day)
	if day > 0 and day <= 31:
		return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
	if year > 1900 and year < 2020:
		return year

class MainHandler(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.out.write(form % {"error":error})
	
	
	def get(self):
		self.write_form()
		#self.response.write(form)
		
	def post(self):
		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))
		
		if not(user_month and user_day and user_year):
			self.write_form("That doesnt look right to me")
			#self.response.out.write(form)
		else:
			self.response.out.write("Thanks for using my first web app")
		
app = webapp2.WSGIApplication([
    ('/', MainHandler)], debug=True)

