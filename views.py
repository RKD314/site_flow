from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

class IndexView(generic.TemplateView):
	template_name = 'site_flow/index.html'

class AboutView(generic.TemplateView):
	template_name = 'site_flow/about.html'

class FaqView(generic.TemplateView):
	template_name = 'site_flow/faq.html'

#class ContactView(FormView):
#	template_name = 'site_flow/contact.html'
#	success_url = '/thanks/'

#	def form_valid(self, form):
#        	# This method is called when valid form data has been POSTed.
#        	# It should return an HttpResponse.
#        	form.send_email()
#        	return super(ContactView, self).form_valid(form)
