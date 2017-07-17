from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test


def should_be_starosta(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that user is logged in like starosta, redirecting to the log_in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.groups.get().name == 'Starostas',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def should_be_jury(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that user is logged in like jury, redirecting to the log_in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.groups.get().name == 'Jury',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator
