# Utilizes Flask-SQLAlchemy for ORM, Bcrypt for password hashing, and custom validation methods to ensure data integrity.

import re
from datetime import datetime

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import bcrypt, db


class UserAuth(db.Model, SerializerMixin):
    """
    UserAuth Model: Manages user authentication data and relations.

    Fields:
    - id: Primary key.
    - username: Unique username for user identification.
    - email: User's email address.
    - password_hash: Hashed password for secure storage.

    Relations:
    - chat_messages: User's chat history.

    Validations:
    - email and username are validated for length and format.

    Security:
    - Passwords are hashed using bcrypt upon setting to ensure secure storage.
    - Password field is write-only to prevent unauthorized access.
    """

    __tablename__ = "user_auth"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    chat_messages = db.relationship(
        "ChatMessage", back_populates="user", cascade="all, delete-orphan"
    )
    sessions = db.relationship(
        "UserSession", back_populates="user", cascade="all, delete-orphan"
    )

    @validates("email")
    def validate_email(self, key, address):
        """
        Validates the email address to ensure it follows a general email format and length.

        This validation is crucial for maintaining data integrity and ensuring that user notifications,
        password resets, and other communications are sent to a valid email address. The validation
        checks include ensuring the email address is at least 3 characters long and matches a basic
        pattern for email addresses. This is a simplistic check aimed at catching obvious errors, and
        it may be adjusted to use more sophisticated regex patterns or external validation libraries
        for comprehensive email validation in a production environment.
        """
        assert len(address) >= 3, f"{key} must be at least 3 characters long"
        assert re.match(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", address
        ), "Invalid email format"
        return address

    @validates("username")
    def validate_username(self, key, value):
        """
        Validates the username format and length.
        """
        assert len(value) >= 3, f"{key} must be at least 3 characters long"
        return value

    @hybrid_property
    def password(self):
        """
        Ensures password field is write-only for security reasons
        """
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        """
        Hashes the password before storing it in the database.
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """
        Verifies password against the hash stored in the database
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    serialize_rules = (
        "-password_hash",
        "-chat_messages.user",
    )


class UserSession(db.Model, SerializerMixin):
    """
    UserSession Model: Tracks user login sessions.

    Fields:
    - id: Primary key, auto-incremented. Used to identify the session uniquely.
    - user_id: Foreign key linking to the UserAuth model. Identifies the user owning the session.
    - started_at: Timestamp when the user logged in and the session was initiated.
    - ended_at: Timestamp when the user logged out, marking the session's end. Nullable, as sessions might be ongoing.

    Relations:
    - user: Defines the relationship back to the UserAuth model, allowing easy access to the user's data from a session.
    """

    __tablename__ = "user_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_auth.id"), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ended_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("UserAuth", back_populates="sessions")

    def __repr__(self):
        return f"<UserSession {self.id} User ID: {self.user_id}>"


class ChatMessage(db.Model, SerializerMixin):
    """
    Captures messages exchanged between the user and the system, including both user queries and system responses.

    Attributes:
    - id: Unique identifier for each chat message.
    - user_id: Links to the UserAuth model to identify the message's sender.
    - message: The content of the user's message.
    - response: The system's response to the user's message.
    - timestamp: The date and time when the message was exchanged.
    """

    __tablename__ = "chat_messages"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_auth.id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey("user_sessions.id"), nullable=True)
    session = db.relationship("UserSession", backref="chat_messages")

    user = db.relationship("UserAuth", back_populates="chat_messages")

    def __repr__(self):
        return f"<ChatMessage {self.id} User ID: {self.user_id}>"
