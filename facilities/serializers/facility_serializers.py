from rest_framework import serializers

from common.serializers import AbstractFieldsMixin

from ..models import (
    OwnerType,
    Owner,
    JobTitle,
    Officer,
    OfficerContact,
    FacilityStatus,
    FacilityType,
    RegulatingBody,
    RegulationStatus,
    Facility,
    FacilityRegulationStatus,
    FacilityContact,
    FacilityUnit,
    ServiceCategory,
    Option,
    Service,
    FacilityService,
    FacilityServiceRating,
    ServiceOption,
    FacilityApproval,
    FacilityOperationState,
    FacilityUpgrade,
    RegulatingBodyContact,
    FacilityOfficer,
    RegulatoryBodyUser,
    FacilityUnitRegulation
)


class RegulatoryBodyUserSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    user_name = serializers.ReadOnlyField(source='user.get_full_name')
    regulatory_body_name = serializers.ReadOnlyField(
        source='regulatory_body.name')

    class Meta:
        model = RegulatoryBodyUser


class FacilityOfficerSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    facility_name = serializers.ReadOnlyField(source='facility.name')
    officer_name = serializers.ReadOnlyField(source='officer.name')
    id_number = serializers.ReadOnlyField(source='officer.id_number')
    registration_number = serializers.ReadOnlyField(
        source='officer.registration_number')
    job_title = serializers.ReadOnlyField(source='officer.job_title.name')

    class Meta(object):
        model = FacilityOfficer


class RegulatingBodyContactSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    contact_text = serializers.ReadOnlyField(source='contact.contact')
    contact_type = serializers.ReadOnlyField(
        source='contact.contact_type.name'

    )

    class Meta(object):
        model = RegulatingBodyContact


class FacilityUpgradeSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityUpgrade


class FacilityOperationStateSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityOperationState


class FacilityApprovalSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityApproval


class ServiceCategorySerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = ServiceCategory


class OptionSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Option


class ServiceOptionSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    option_name = serializers.ReadOnlyField(source="option.display_text")
    service_name = serializers.ReadOnlyField(source="service.name")

    class Meta(object):
        model = ServiceOption


class ServiceSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)

    class Meta(object):
        model = Service
        read_only_fields = ('code',)


class FacilityServiceSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    service_name = serializers.CharField(read_only=True)
    option_display_value = serializers.CharField(read_only=True)
    average_rating = serializers.ReadOnlyField()
    number_of_ratings = serializers.ReadOnlyField()

    class Meta(object):
        model = FacilityService


class FacilityStatusSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityStatus


class RegulatingBodySerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = RegulatingBody


class OwnerTypeSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = OwnerType


class FacilityRegulationStatusSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityRegulationStatus


class FacilityTypeSerializer(serializers.ModelSerializer):
    owner_type_name = serializers.ReadOnlyField(source='owner_type.name')

    class Meta(object):
        model = FacilityType


class OfficerContactSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = OfficerContact


class JobTitleSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = JobTitle


class RegulationStatusSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    next_state_name = serializers.CharField(read_only=True)
    previous_state_name = serializers.CharField(read_only=True)

    class Meta(object):
        model = RegulationStatus


class OfficerSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Officer


class OwnerSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = Owner
        read_only_fields = ('code',)


class FacilitySerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    regulatory_status_name = serializers.CharField(read_only=True)
    facility_type_name = serializers.CharField(read_only=True)
    owner_name = serializers.CharField(read_only=True)
    owner_type_name = serializers.CharField(read_only=True)
    operation_status_name = serializers.CharField(read_only=True)
    county = serializers.CharField(read_only=True)
    constituency = serializers.CharField(read_only=True)
    ward_name = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    facility_services = serializers.ReadOnlyField(
        source="get_facility_services")

    class Meta(object):
        model = Facility
        fields = [
            "name", "owner_name", "operation_status", "code", "id",
            "county", "constituency", "ward", "facility_type_name",
            "operation_status_name", "regulatory_status_name",
            "facility_type_name", "number_of_beds",
            "number_of_cots", "is_classified", "is_published",
            "open_weekends", "open_whole_day",
            "open_public_holidays", "owner_type_name",
            "ward_name", "average_rating", "facility_services",
            "created", "updated", "deleted", "active", "search",
            "abbreviation", "description", "location_desc",
            "created_by", "updated_by", "facility_type",
            "owner", "officer_in_charge", "physical_address",
            "parent", "contacts",
        ]


class FacilityDetailSerializer(FacilitySerializer):
    facility_services = serializers.ReadOnlyField(
        source="get_facility_services")
    facility_contacts = serializers.ReadOnlyField(
        read_only=True, source="get_facility_contacts")
    facility_physical_address = serializers.DictField(
        read_only=True, required=False)
    officer_name = serializers.ReadOnlyField(source='officer_in_charge.name')

    class Meta(object):
        model = Facility
        exclude = ('attributes', )


class FacilityListSerializer(FacilitySerializer):
    class Meta(object):
        model = Facility
        fields = [
            'code', 'name', 'id', 'county', 'constituency',
            'facility_type_name', 'owner_type_name',
            'regulatory_status_name', 'ward', 'operation_status_name',
            'ward_name']


class FacilityContactSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    contact_type = serializers.ReadOnlyField(
        source="contact.contact_type.name")
    actual_contact = serializers.ReadOnlyField(source="contact.contact")

    class Meta(object):
        model = FacilityContact


class FacilityUnitSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    regulation_status = serializers.ReadOnlyField()

    class Meta(object):
        model = FacilityUnit


class FacilityServiceRatingSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta(object):
        model = FacilityServiceRating


class FacilityUnitRegulationSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta(object):
        model = FacilityUnitRegulation
