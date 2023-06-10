from django.shortcuts import redirect, render
from geoservice.features.models import Feature
from utils.logger.Error import ErrorLogger

error_logger = ErrorLogger


def map_view(request):
    """
    Renders the map view.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - response: The HTTP response.

    """
    try:
        return render(request, 'map.html')
    except Exception as err:
        error_logger.log_unexpected_error(err, dict(), 'E500',
                                          request.get_full_path())
        return render(request, 'login.html')


def feature_list_view(request):
    """
    Renders the feature list view.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - response: The HTTP response.

    """
    try:
        features = Feature.objects.all()
        return render(request, 'feature_list.html', {'features': features})
    except Exception as err:
        error_logger.log_unexpected_error(err, dict(), 'E500',
                                          request.get_full_path())
        return render(request, 'login.html')


def feature_edit_view(request, **kwargs):
    """
    Renders the feature edit view.

    Parameters:
    - request: The HTTP request object.
    - kwargs: Additional keyword arguments.

    Returns:
    - response: The HTTP response.

    """
    try:
        return render(request, 'feature_edit.html')
    except Exception as err:
        error_logger.log_unexpected_error(err, dict(), 'E500',
                                          request.get_full_path())
        return render(request, 'login.html')


def login_view(request, **kwargs):
    """
    Renders the login view or redirects to the map view if the user is authenticated.

    Parameters:
    - request: The HTTP request object.
    - kwargs: Additional keyword arguments.

    Returns:
    - response: The HTTP response.

    """
    try:
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('map-view')
    except Exception as err:
        error_logger.log_unexpected_error(err, dict(), 'E500',
                                          request.get_full_path())
        return render(request, 'login.html')
