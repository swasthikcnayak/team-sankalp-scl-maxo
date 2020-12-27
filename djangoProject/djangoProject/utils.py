def is_student(request):
    if request.user.role == 'STD':
        return True
    return False


def is_teacher(request):
    if request.user.role == 'THR':
        return True
    return False


def is_admin(request):
    if request.user.role == 'ADM':
        return True
    return False
