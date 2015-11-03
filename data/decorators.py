from .models import EventLog, MenuEntry, WorkTimer

def timeout_logging(view_func):
    def _wrapped_view_func(request, menu_id, *args, **kwargs):
        print request.COOKIES
        if request.method == "POST":
            worktimer, created = WorkTimer.objects.get_or_create(user_id=request.user.id, value=request.POST['seconds'], token=request.POST['token'])
            menuentry = MenuEntry.objects.get(user_id=request.user.id, menu_id=menu_id)
            eventlog = EventLog(menuentry_id=menuentry.id, name=request.POST['action'])
            eventlog.save()
        return view_func(request, menu_id, *args, **kwargs)
    return _wrapped_view_func
