"""Providers Configuration File."""

from masonite.providers import (
    AppProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,
    HelpersProvider,
    MailProvider,
    QueueProvider,
    RouteProvider,
    SassProvider,
    SessionProvider,
    StatusCodeProvider,
    UploadProvider,
    ViewProvider,
    WhitenoiseProvider,
)
from masonite.validation.providers.ValidationProvider import ValidationProvider

from app.inertia.InertiaProvider import InertiaProvider
from app.providers.ModelObserverProvider import ModelObserverProvider
from app.providers.AppStateProvider import AppStateProvider
from app.providers.CommandsProvider import CommandsProvider
from app.providers.CustomHelpersProvider import CustomHelpersProvider
from app.providers.RuleProvider import RuleProvider

"""Providers List
Providers are a simple way to remove or add functionality for Masonite
The providers in this list are either ran on server start or when a
request is made depending on the provider. Take some time to can
learn more more about Service Providers in our documentation
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    SessionProvider,
    # Get App State
    AppStateProvider,
    # More Framework Providers
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    # Optional Framework Providers
    SassProvider,
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CsrfProvider,
    HelpersProvider,
    ValidationProvider,
    # Third Party Providers
    # Application Providers
    CommandsProvider,
    ModelObserverProvider,
    CustomHelpersProvider,
    InertiaProvider,
    RuleProvider,
]
