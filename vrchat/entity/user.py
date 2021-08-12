from __future__ import annotations

import enum
from typing import List, Optional

from pydantic import BaseModel, Field


class CurrentUser(BaseModel):
    accepted_tos_version: str = Field(alias="acceptedTOSVersion")
    account_deletion_data: Optional[str] = Field(
        None, alias="accountDeletionData"
    )  # datetime
    active_friend_ids: List[str] = Field(alias="activeFriends")
    allow_avater_copying: bool = Field(alias="allowAvatarCopying")
    bio: str = Field(alias="bio")
    bio_links: List[str] = Field(alias="bioLinks")
    current_avater: str = Field(alias="currentAvatar")
    current_avater_asset_url: str = Field(alias="currentAvatarAssetURL")
    current_avater_image_url: str = Field(alias="currentAvatarImageURL")
    current_avater_thumbnail_image_url: str = Field(
        alias="currentAvatarThumbnailImageURL"
    )
    date_joined: str = Field(alias="dateJoined")  # datetime
    developer_type: DeveloperType = Field(alias="developerType")
    display_name: str = Field(alias="displayName")
    email: str = Field(alias="email")
    email_verified: bool = Field(alias="emailVerified")
    fallback_avater: str = Field(alias="fallbackAvatar")
    friends_group_names: List[str] = Field(alias="friendsGroupNames")
    friend_key: str = Field(alias="friendKey")
    friend_ids: List[str] = Field(alias="friends")
    has_birthday: bool = Field(alias="hasBirthday")
    has_email: bool = Field(alias="hasEmail")
    has_logged_in_from_client: bool = Field(alias="hasLoggedInFromClient")
    has_pending_email: bool = Field(alias="hasPendingEmail")
    home_location: str = Field(alias="homeLocation")
    id: str = Field(alias="id")
    is_friend: bool = Field(alias="isFriend")
    last_login: str = Field(alias="lastLogin")  # datetime
    last_platform: str = Field(alias="lastPlatform")
    obfuscated_email: str = Field(alias="obfuscatedEmail")
    obfuscated_pending_email: str = Field(alias="obfuscatedPendingEmail")
    oculus_id: str = Field(alias="oculusId")
    offline_friend_ids: List[str] = Field(alias="offlineFriends")
    online_friend_ids: List[str] = Field(alias="onlineFriends")
    past_display_names: List[PastDisplayName] = Field(alias="pastDisplayNames")
    state: State = Field(alias="state")
    status: str = Field(alias="status")
    status_description: str = Field(alias="statusDescription")
    status_history: str = Field(alias="statusHistory")
    steam_details: str = Field(alias="steamDetails")
    steam_id: str = Field(alias="steamId")
    tags: List[str] = Field(alias="tags")
    two_factor_auth_enabled: bool = Field(alias="twoFactorAuthEnabled")
    unsubscribe: bool = Field(alias="unsubscribe")
    user_icon: str = Field(alias="userIcon")
    username: str = Field(alias="username")


class DeveloperType(str, enum.Enum):
    NONE = "none"
    TRUSTED = "trusted"
    INTERNAL = "internal"
    MODERATOR = "moderator"


class State(str, enum.Enum):
    ONLINE = "online"
    ACTIVE = "active"
    OFFLINE = "offline"


class Status(str, enum.Enum):
    ACTIVE = "active"
    JOIN_ME = "join me"
    ASK_ME = "ask me"
    BUSY = "busy"
    OFFLINE = "offline"


class PastDisplayName(BaseModel):
    display_name: str = Field(alias="displayName")
    updated_at: str = Field(alias="updatedAt")  # datetime
