# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRecommendationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The feature- generated recommendation shown to the reviewer."""

    APPROVE = "Approve"
    DENY = "Deny"
    NO_INFO_AVAILABLE = "NoInfoAvailable"


class AccessReviewActorIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type : user/servicePrincipal."""

    USER = "user"
    SERVICE_PRINCIPAL = "servicePrincipal"


class AccessReviewApplyResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The outcome of applying the decision."""

    NEW = "New"
    APPLYING = "Applying"
    APPLIED_SUCCESSFULLY = "AppliedSuccessfully"
    APPLIED_WITH_UNKNOWN_FAILURE = "AppliedWithUnknownFailure"
    APPLIED_SUCCESSFULLY_BUT_OBJECT_NOT_FOUND = "AppliedSuccessfullyButObjectNotFound"
    APPLY_NOT_SUPPORTED = "ApplyNotSupported"


class AccessReviewDecisionInsightType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of insight."""

    USER_SIGN_IN_INSIGHT = "userSignInInsight"


class AccessReviewDecisionPrincipalResourceMembershipType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessReviewDecisionPrincipalResourceMembershipType."""

    DIRECT = "direct"
    INDIRECT = "indirect"


class AccessReviewHistoryDefinitionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This read-only field specifies the of the requested review history data. This is either
    requested, in-progress, done or error.
    """

    REQUESTED = "Requested"
    IN_PROGRESS = "InProgress"
    DONE = "Done"
    ERROR = "Error"


class AccessReviewInstanceReviewersType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field specifies the type of reviewers for a review. Usually for a review, reviewers are
    explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be
    chosen dynamically. For example managers review or self review.
    """

    ASSIGNED = "Assigned"
    SELF = "Self"
    MANAGERS = "Managers"


class AccessReviewInstanceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This read-only field specifies the status of an access review instance."""

    NOT_STARTED = "NotStarted"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    APPLIED = "Applied"
    INITIALIZING = "Initializing"
    APPLYING = "Applying"
    COMPLETING = "Completing"
    SCHEDULED = "Scheduled"
    AUTO_REVIEWING = "AutoReviewing"
    AUTO_REVIEWED = "AutoReviewed"
    STARTING = "Starting"


class AccessReviewRecurrencePatternType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The recurrence type : weekly, monthly, etc."""

    WEEKLY = "weekly"
    ABSOLUTE_MONTHLY = "absoluteMonthly"


class AccessReviewRecurrenceRangeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The recurrence range type. The possible values are: endDate, noEnd, numbered."""

    END_DATE = "endDate"
    NO_END = "noEnd"
    NUMBERED = "numbered"


class AccessReviewResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents a reviewer's decision for a given review."""

    APPROVE = "Approve"
    DENY = "Deny"
    NOT_REVIEWED = "NotReviewed"
    DONT_KNOW = "DontKnow"
    NOT_NOTIFIED = "NotNotified"


class AccessReviewReviewerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type : user/servicePrincipal."""

    USER = "user"
    SERVICE_PRINCIPAL = "servicePrincipal"


class AccessReviewScheduleDefinitionReviewersType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field specifies the type of reviewers for a review. Usually for a review, reviewers are
    explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be
    chosen dynamically. For example managers review or self review.
    """

    ASSIGNED = "Assigned"
    SELF = "Self"
    MANAGERS = "Managers"


class AccessReviewScheduleDefinitionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This read-only field specifies the status of an accessReview."""

    NOT_STARTED = "NotStarted"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    APPLIED = "Applied"
    INITIALIZING = "Initializing"
    APPLYING = "Applying"
    COMPLETING = "Completing"
    SCHEDULED = "Scheduled"
    AUTO_REVIEWING = "AutoReviewing"
    AUTO_REVIEWED = "AutoReviewed"
    STARTING = "Starting"


class AccessReviewScopeAssignmentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The role assignment state eligible/active to review."""

    ELIGIBLE = "eligible"
    ACTIVE = "active"


class AccessReviewScopePrincipalType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type user/servicePrincipal to review."""

    USER = "user"
    GUEST_USER = "guestUser"
    SERVICE_PRINCIPAL = "servicePrincipal"
    USER_GROUP = "user,group"
    REDEEMED_GUEST_USER = "redeemedGuestUser"


class DecisionResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of resource."""

    AZURE_ROLE = "azureRole"


class DecisionTargetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of decision target : User/ServicePrincipal."""

    USER = "user"
    SERVICE_PRINCIPAL = "servicePrincipal"


class DefaultDecisionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This specifies the behavior for the autoReview feature when an access review completes."""

    APPROVE = "Approve"
    DENY = "Deny"
    RECOMMENDATION = "Recommendation"


class RecordAllDecisionsResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The decision to make. Approvers can take action of Approve/Deny."""

    APPROVE = "Approve"
    DENY = "Deny"


class SeverityLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity level of the alert."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"