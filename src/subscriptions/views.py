from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import send_mail
from models import Subscription
from forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    form = SubscriptionForm()

    ctx = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', ctx)


def create(request):
    form = SubscriptionForm(request.POST)

    print form

    if not form.is_valid():
        ctx = RequestContext(request, {'form': form})
        return render_to_response('subscriptions/new.html', ctx)

    print "send mail"
    # send_mail

    subscription = form.save()
    return HttpResponseRedirect(reverse('subscriptions:success', args=(subscription.pk,)))


def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)

    ctx = RequestContext((request), {'subscription': subscription})
    return render_to_response('subscriptions/success.html', ctx)

