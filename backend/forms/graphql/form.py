import graphene
from django.conf import settings
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType

from core.graphql.limited_event import LimitedEventType

from ..models.form import Form
from .limited_survey import LimitedSurveyType

DEFAULT_LANGUAGE: str = settings.LANGUAGE_CODE


class FormType(DjangoObjectType):
    @staticmethod
    def resolve_fields(parent: Form, info, enrich: bool = True):
        if enrich:
            return parent.enriched_fields
        else:
            return parent.fields

    fields = graphene.Field(
        GenericScalar,
        enrich=graphene.Boolean(
            description=(
                "Enriched fields have dynamic choices populated for them. This is the default. "
                'Pass enrich: false to get access to "raw" unenriched fields. This is used by the form editor.'
            ),
        ),
    )

    @staticmethod
    def resolve_event(parent: Form, info):
        return parent.event

    event = graphene.Field(graphene.NonNull(LimitedEventType))

    @staticmethod
    def resolve_survey(parent: Form, info):
        return parent.survey

    survey = graphene.Field(LimitedSurveyType)

    class Meta:
        model = Form
        fields = ("slug", "title", "description", "thank_you_message", "layout", "language")
