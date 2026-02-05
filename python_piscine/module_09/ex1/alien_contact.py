from datetime import datetime
from enum import Enum
from typing import Optional, Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    """
    Enumeration of possible alien contact methods.
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Represents a recorded alien contact event with validation rules.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_contact_id_start(self) -> Self:
        """
        Validates that the contact_id starts with the prefix 'AC'.
        """
        if not self.contact_id.startswith("AC"):
            """
            ValueError / Assertion error is raised. Pydantic captures it and
            evolves it in a ValidationError exception captured in main()
            """
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode="after")
    def contact_validation(self) -> Self:
        """
        Automatically verifies the contact if the contact_type is valid.
        """
        if self.contact_type.value in [
                contact.value for contact in ContactType]:
            self.is_verified = True
        return self

    @model_validator(mode="after")
    def telepathic_validation(self) -> Self:
        """
        Validates that telepathic contacts have a minimum number of
        witnesses.
        """
        if self.contact_type.value == "telepathic" and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def signal_msg_validation(self) -> Self:
        """
        Validates that a message is provided when signal strength is
        high.
        """
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Signal strength >= 7 requires a message_received")
        return self


def main() -> None:
    """
    Main function to demonstrate AlienContact validation with valid and
    invalid data.
    """
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact_1_data: dict = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": "Atacama Desert, Chile",
        "contact_type": "visual",
        "signal_strength": 9.6,
        "duration_minutes": 99,
        "witness_count": 11,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    }
    try:
        contact_1: AlienContact = AlienContact(**contact_1_data)
        print(f"ID: {contact_1.contact_id}")
        print(f"Type: {contact_1.contact_type.value}")
        print(f"Location: {contact_1.location}")
        print(f"Signal: {contact_1.signal_strength}/10")
        print(f"Duration: {contact_1.duration_minutes} minutes")
        print(f"Witnesses: {contact_1.witness_count}")
        print(f"Message: {contact_1.message_received}")
    except ValidationError as v_e:
        for error in v_e.errors():
            print(error.get("msg").replace("Value error, ", ""))

    print()
    print("======================================")
    print("Expected validation error:")
    contact_2_data: dict = {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": "telepathic",
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": None,
        "is_verified": False,
    }
    try:
        contact_2: AlienContact = AlienContact(**contact_2_data)
        print(contact_2)
    except ValidationError as v_e:
        for error in v_e.errors():
            print(error.get("msg").replace("Value error, ", ""))


if __name__ == "__main__":
    main()
