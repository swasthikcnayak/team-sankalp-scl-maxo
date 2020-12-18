from django.contrib.auth.decorators import login_required


@login_required
def view_list(request):
    if request.user.role == 'STD':
        return None
    elif request.user.role == 'THR' or request.user.role == 'ADM':
        return None


@login_required
def view_notes(request):
    return None
