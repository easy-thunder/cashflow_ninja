import random
from datetime import datetime

from faker import Faker
from flask_bcrypt import Bcrypt
from models import ChatMessage, UserAuth

from app import app, db

# Instantiate Faker
fake = Faker()

# Setup bcrypt
bcrypt = Bcrypt(app)


def seed_database():
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()

        # Create fake data for UserAuth
        for _ in range(10):  # Adjust the number of users as needed
            username = fake.user_name()
            email = fake.email()
            # Password is set to '123456' for all users
            password_hash = bcrypt.generate_password_hash("123456").decode("utf-8")

            user = UserAuth(username=username, email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()

            # Create fake chat messages for the user
            for _ in range(5):  # Adjust the number of messages as needed
                message = fake.sentence()
                response = fake.sentence()
                timestamp = fake.date_time_this_year()

                chat_message = ChatMessage(
                    user_id=user.id,
                    message=message,
                    response=response,
                    timestamp=timestamp,
                )
                db.session.add(chat_message)

            db.session.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
