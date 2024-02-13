"""empty message

Revision ID: 46078f4fd8c7
Revises: e9d5411f4b08
Create Date: 2024-02-13 09:27:11.801923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46078f4fd8c7'
down_revision: Union[str, None] = 'e9d5411f4b08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
