import datetime
from django.shortcuts import render_to_response



def currentDate(req):
	now = datetime.datetime.now()

	return render_to_response('currentDate.html', {'now':now})


def futureDate(req, offset):
	try:
		hour_offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now()
	future = now + datetime.timedelta(hours=hour_offset)
#	hour_offset = 5
	return render_to_response('futureDate.html', {'hour_offset':hour_offset, 'future':future})
