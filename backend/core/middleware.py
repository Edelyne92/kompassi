from .models import Event, Organization
from .page_wizard import page_wizard_clear

NEVER_BLOW_PAGE_WIZARD_PREFIXES = [
    # we have addresses like /desuprofile/confirm/475712413a0ddc3c7a57c6721652b75449bf3c89
    # that should not blow the page wizard when used within a signup page wizard flow
    "/desuprofile/confirm/",
    "/oauth2/",
    "/oidc/",
]


class PageWizardMiddleware:
    """
    MIDDLEWARE = (
        # ...

        'core.middleware.page_wizard_middleware'
    )

    Clear the page wizard when visiting a non-related page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        related = request.session.get("core.utils.page_wizard.related", None)

        if related is None:
            pass
        elif request.method != "GET":
            pass
        elif request.path in related:
            pass
        elif any(request.path.startswith(prefix) for prefix in NEVER_BLOW_PAGE_WIZARD_PREFIXES):
            pass
        else:
            page_wizard_clear(request)


class EventOrganizationMiddleware:
    """
    Sets request.event and request.organization if they can be deduced from the URL.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        request.event = None
        request.organization = None

        if resolver_match := request.resolver_match:
            if event_slug := resolver_match.kwargs.get("event_slug"):
                if (
                    event := Event.objects.filter(slug=event_slug)
                    .only(
                        "name",
                        "name_genitive",
                        "slug",
                        "homepage_url",
                        "organization__name",
                        "organization__slug",
                        "organization__homepage_url",
                    )
                    .first()
                ):
                    request.event = event
                    request.organization = event.organization
            elif organization_slug := resolver_match.kwargs.get("organization_slug"):
                request.organization = (
                    Organization.objects.filter(slug=organization_slug)
                    .only(
                        "name",
                        "slug",
                        "homepage_url",
                    )
                    .first()
                )
