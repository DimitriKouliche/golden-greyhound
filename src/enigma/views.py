# coding=utf-8
"""
This is our main controller
"""
import logging
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from .models import Contestant
from .models import Enigma


def error404(request):
    template = loader.get_template('404.html')
    return render(request, template)


class Home(View):
    """
    This will display the homepage of our application
    """
    enigma = None

    def get(self, request):
        """
        Handles displaying our template
        """
        if self.enigma.template_name == "end":
            return render(request, 'end.html', {'contestants': Contestant.objects.all()})
        return render(request, self.enigma.template_name + '.html')

    def post(self, request):
        """
        Handles retrieving a user's answer and redirecting him to the right page
        """
        answer = request.POST.get('answer')
        if self.enigma.template_name == "end":
            contestant = Contestant.objects.create(name=answer)
            contestant.save()
            return render(request, 'end.html', {'confirmation': True})
        logging.debug('User entered ' + answer + ', expected answer was ' + self.enigma.expected_answer)
        if self.enigma.expected_answer == answer:
            return redirect(request.path + f"?key={self.enigma.next_key}")
        return render(request, self.enigma.template_name + '.html', {'error': True})

    def dispatch(self, request, *args, **kwargs):
        """
        This happens whenever we try to do a get request to our view
        """
        key = 'Bv9KHeK0HfIF-REsVqvjUw..'
        if 'key' in request.GET:
            key = request.GET.get('key')
        try:
            self.enigma = Enigma.objects.get(secret_key=key)
        except Enigma.DoesNotExist:
            return render(request, '404.html')
        return super().dispatch(request, *args, **kwargs)
