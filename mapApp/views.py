from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from django.contrib.gis.geos import GEOSGeometry
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth.models import User, Group
from mapApp.models.incident import Incident
from mapApp.models.route import Route
from mapApp.models.alert_area import AlertArea
from mapApp.models.alert_notification import AlertNotification
from mapApp.models.hazard import Hazard
from mapApp.models.theft import Theft

from mapApp.forms.incident import IncidentForm
from mapApp.forms.route import RouteForm
from mapApp.forms.contact import EmailForm
from mapApp.forms.geofences import GeofenceForm
from mapApp.forms.edit_geom import EditForm
from mapApp.forms.hazard import HazardForm
from mapApp.forms.theft import TheftForm

# Used for downloading data
from spirit.utils.decorators import administrator_required
from django.contrib.auth.decorators import login_required
from djgeojson.serializers import Serializer as GeoJSONSerializer

import time

def index(request, lat=None, lng=None, zoom=None):
	context = indexContext(request)

	# Add zoom and center data if present
	if not None in [lat, lng, zoom]:
		context['lat']= float(lat)
		context['lng']= float(lng)
		context['zoom']= int(zoom)
	
	return render(request, 'mapApp/index.html', context)


# Define default context data for the index view. Forms can be overridden to display errors (used by other views)
def indexContext(request, incidentForm=IncidentForm(), routeForm=RouteForm(), geofenceForm=GeofenceForm(), hazardForm=HazardForm(), theftForm=TheftForm()):
	return {
		# Model data used by map
		'incidents': Incident.objects.all(),
		'hazards': Hazard.objects.all(),
		'thefts': Theft.objects.all(),
		"routes": Route.objects.all(),
		"geofences": AlertArea.objects.filter(user=request.user.id),

		# Form data used by map
		"incidentForm": incidentForm,
		"routeForm": routeForm,
		"geofenceForm": geofenceForm,
		"hazardForm": hazardForm,
		"theftForm": theftForm,
		
		"editForm": EditForm()
	}


def about(request):
	return render(request, 'mapApp/about.html', {"emailForm": EmailForm()})


def contact(request):
	if request.method == 'POST':
		emailForm = EmailForm(request.POST)

		if emailForm.is_valid():
			subject = emailForm.cleaned_data['subject']
			message = emailForm.cleaned_data['message']
			sender = emailForm.cleaned_data['sender']
			cc_myself = emailForm.cleaned_data['cc_myself']

			adminContacts = Group.objects.get(name="admin contact").user_set.all()
			recipients = []
			
			for contact in adminContacts:
				recipients.append(contact.email) 
			if cc_myself:
				recipients.append(sender)

			try:
				send_mail(subject, message, sender, recipients)
			except BadHeaderError:
				messages.error(request, '<strong>Invalid Header.</strong> Illegal characters found.')

			messages.success(request, '<strong>Thank you!</strong><br>We\'ll do our best to get back to you.')
			emailForm = EmailForm() # Clear the form

	return render(request, 'mapApp/about.html', {"emailForm": emailForm})


def postRoute(request):
	if request.method == 'POST':
		routeForm = RouteForm(request.POST)

		# Convert string coords to valid geometry object
		routeForm.data = routeForm.data.copy()
		routeForm.data['line'] = GEOSGeometry(routeForm.data['line'])

		if routeForm.is_valid():
			routeForm.save()
			routeForm = RouteForm() # Clear the form
			messages.success(request, '<strong>Thank you!</strong><br>Your route was successfully added.')

	return render(request, 'mapApp/index.html', indexContext(request, routeForm=routeForm))


def postIncident(request):
	if request.method == 'POST':
		incidentForm = IncidentForm(request.POST)
		
		# Convert coords to valid geometry
		incidentForm.data = incidentForm.data.copy()
		incidentForm.data['geom'] = GEOSGeometry(incidentForm.data['geom'])

		if incidentForm.is_valid():
			incident = incidentForm.save()
			alertUsers(request, incident)
			
			messages.success(request, '<strong>Thank you!</strong><br>Your incident marker was successfully added.')			
			return HttpResponseRedirect(reverse('mapApp:index', \
				kwargs=({										\
					"lat":str(incident.latlngList()[0]),		\
					"lng":str(incident.latlngList()[1]),		\
					"zoom":str(18)								\
				})												\
			)) 

		else: # Show form errors 
			return render(request, 'mapApp/index.html', indexContext(request, incidentForm=incidentForm))
	
	else: # Redirect to index if not a post request
		return HttpResponseRedirect(reverse('mapApp:index')) 


def postHazard(request):
	if request.method == 'POST':
		hazardForm = HazardForm(request.POST)
		
		# Convert coords to valid geometry
		hazardForm.data = hazardForm.data.copy()
		hazardForm.data['geom'] = GEOSGeometry(hazardForm.data['geom'])

		if hazardForm.is_valid():
			hazard = hazardForm.save()
			# alertUsers(request, hazard) #alertUsers view needs to be edited to accomodate hazards
			
			messages.success(request, '<strong>Thank you!</strong><br>Your hazard marker was successfully added.')			
			return HttpResponseRedirect(reverse('mapApp:index', \
				kwargs=({										\
					"lat":str(hazard.latlngList()[0]),		\
					"lng":str(hazard.latlngList()[1]),		\
					"zoom":str(18)								\
				})												\
			)) 

		else: # Show form errors 
			return render(request, 'mapApp/index.html', indexContext(request, hazardForm=hazardForm))
	
	else: # Redirect to index if not a post request
		return HttpResponseRedirect(reverse('mapApp:index')) 


def postTheft(request):
	if request.method == 'POST':
		theftForm = TheftForm(request.POST)
		
		# Convert coords to valid geometry
		theftForm.data = theftForm.data.copy()
		theftForm.data['geom'] = GEOSGeometry(theftForm.data['geom'])

		if theftForm.is_valid():
			theft = theftForm.save()
			# alertUsers(request, theft) #alertUsers view needs to be edited to accomodate thefts
			
			messages.success(request, '<strong>Thank you!</strong><br>Your theft marker was successfully added.')			
			return HttpResponseRedirect(reverse('mapApp:index', \
				kwargs=({										\
					"lat":str(theft.latlngList()[0]),		\
					"lng":str(theft.latlngList()[1]),		\
					"zoom":str(18)								\
				})												\
			)) 

		else: # Show form errors 
			return render(request, 'mapApp/index.html', indexContext(request, hazardForm=hazardForm))
	
	else: # Redirect to index if not a post request
		return HttpResponseRedirect(reverse('mapApp:index')) 


def alertUsers(request, incident):
	intersectingPolys = AlertArea.objects.filter(geom__intersects=incident.geom) #list of AlertArea objects
	usersToAlert = set([poly.user for poly in intersectingPolys if poly.emailWeekly]) # get list of distinct users to alert
	usersToNotEmail = list(set([poly.user for poly in intersectingPolys if not poly.emailWeekly]) - usersToAlert) # Email if conflict between two polygons receive email
	usersToAlert = list(usersToAlert)

	# TODO FIX THIS MAGIC
	if (incident.incident_type() == "Collision"):
		action = 0
	elif (incident.incident_type() == "Near miss"):
		action = 1
	else:
		action = 2

	for user in usersToAlert:
		AlertNotification(user=user, point=incident, action=action).save()

	for user in usersToNotEmail:
		AlertNotification(user=user, point=incident, action=action, emailed=True).save()


@login_required
def postAlertPolygon(request):
	if request.method == 'POST':
		geofenceForm = GeofenceForm(request.POST)

		# Create valid attributes for user and geom fields 
		geofenceForm.data = geofenceForm.data.copy()
		geofenceForm.data['user'] = request.user.id
		geofenceForm.data['geom'] = GEOSGeometry(geofenceForm.data['geom'])

		if geofenceForm.is_valid():
			# Save new model object, send success message to the user
			geofenceForm.save()
			messages.success(request, 'You will now receive alerts for the area was traced.')

	return HttpResponseRedirect(reverse('mapApp:index'))


@administrator_required
def getIncidents(request):
	data = GeoJSONSerializer().serialize(Incident.objects.all(), indent=2, use_natural_keys=True)

	response = HttpResponse(data, content_type="application/json")
	response['Content-Disposition'] = 'attachment; filename="bikemaps_incidents_%s.json' % time.strftime("%x_%H-%M")
	return response

@administrator_required
def getHazards(request):
	data = GeoJSONSerializer().serialize(Hazard.objects.all(), indent=2, use_natural_keys=True)

	response = HttpResponse(data, content_type="application/json")
	response['Content-Disposition'] = 'attachment; filename="bikemaps_hazards_%s.json' % time.strftime("%x_%H-%M")
	return response

@administrator_required
def getThefts(request):
	data = GeoJSONSerializer().serialize(Theft.objects.all(), indent=2, use_natural_keys=True)

	response = HttpResponse(data, content_type="application/json")
	response['Content-Disposition'] = 'attachment; filename="bikemaps_thefts_%s.json' % time.strftime("%x_%H-%M")
	return response

@login_required
def readAlertPoint(request, alertID):
	alert = get_object_or_404(AlertNotification.objects.filter(user=request.user), pk=alertID)
	if (alert):
		alert.is_read=True
		alert.save()
		return HttpResponseRedirect(reverse('mapApp:index', \
			kwargs=({										\
				"lat":str(alert.point.latlngList()[0]), 	\
				"lng":str(alert.point.latlngList()[1]), 	\
				"zoom":str(18)								\
			})												\
		))
	
	else:
		return HttpResponseRedirect(reverse('mapApp:index')) 


@login_required
def editShape(request):
	if(request.method == 'POST'):
		editForm = EditForm(request.POST)
		if editForm.is_valid():

			pks = editForm.cleaned_data['editPk'].split(';')[:-1]
			newGeoms = editForm.cleaned_data['editGeom'].split(';')[:-1]
			editType = editForm.cleaned_data['editType']
			objType = editForm.cleaned_data['objType']

			if objType == 'point' and request.user.is_superuser:
				objectSet = Incident.objects.all()
			elif objType == 'polygon':
				objectSet = AlertArea.objects.filter(user=request.user)
			else:
				return HttpResponseRedirect(reverse('mapApp:index'))

			for pk, newGeom in zip(pks, newGeoms):
				if(editType == 'edit'):
					shapeEdited = get_object_or_404(objectSet, pk=pk)
					shapeEdited.geom = GEOSGeometry(newGeom)	# edit the object geometry
					shapeEdited.save()
			
				elif (editType == 'delete'):
					shapeEdited = get_object_or_404(objectSet, pk=pk)
					shapeEdited.delete() 	# delete the object

			message = str(len(pks)) + ' ' + editType + ('s' if len(pks)>1 else '') + ' successful'
			messages.success(request, message)
	return HttpResponseRedirect(reverse('mapApp:index'))