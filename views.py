from django.http import HttpResponse

def mint(request, realemail):
    import random, string, commands
    length=10
    anon=''.join(random.choice(string.ascii_lowercase) for x in range(length)) 
    anon=anon + ("@forwurded.com")
    with open("/etc/postfix/virtual", "a") as aliasesfile:
        aliasesfile.write("\n%s %s" % (anon, realemail,)) 

    commands.getoutput("postmap /etc/postfix/virtual")
    commands.getoutput("service postfix restart")
    jsonp = request.GET.get("callback")
    if jsonp:
      return HttpResponse('%s({ "anon": "%s" });' % (jsonp, anon,), mimetype="application/javascript")
    else:
      return HttpResponse("Now forwarding %s to %s." % (anon, realemail,))

