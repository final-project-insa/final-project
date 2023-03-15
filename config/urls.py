from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from users.views import SendEmailView, CustomLoginView, CustomLogoutView, send_email
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("propos/", TemplateView.as_view(template_name="pages/propos.html"), name="propos"),
    path("equipe/", TemplateView.as_view(template_name="pages/equipe.html"), name="equipe"),
    path("competences/", TemplateView.as_view(template_name="pages/competences.html"), name="competences"),
    # path("services/", include("ticket.urls"), namespace="services"),
    # path("services/", include("ticket.urls", namespace="ticket")),
    path("portfolio/", TemplateView.as_view(template_name="pages/portfolio-details.html"), name="portfolio-details"),
    path("services/plan_developer/", TemplateView.as_view(template_name="services/plan_developer.html"), name="plan_developer"),
    path("services/plan_entreprise/", TemplateView.as_view(template_name="services/plan_entreprise.html"), name="plan_entreprise"),
    path("services/plan_base/", TemplateView.as_view(template_name="services/plan_base.html"), name="plan_base"),
    path("payment/", TemplateView.as_view(template_name="services/payment_form.html"), name="payment"),
    path("cinema/", TemplateView.as_view(template_name="loisirs/Movies Website/index.html"), name="cinema"),
    path("ungine_gaming/", TemplateView.as_view(template_name="loisirs/Unigine/index.html"), name="ungine_gaming"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("knl2.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("send_email/", SendEmailView, name="send_email"),
    path("send_contact/", send_email, name="send_contact"),
    # path("accounts/email/", account_email, name="account_email")
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
