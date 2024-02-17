from src.service.database.models.user import User
from src.common.dto.user import UserInDB


def convert_user_model_to_dto(user: User) -> UserInDB:
    return UserInDB(id=user.id,
                    email=user.email,
                    password=user.hashed_password,
                    is_active=user.is_active,
                    referrer=user.referrer
                    )
