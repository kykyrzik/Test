"""empty message

Revision ID: e4a5c108a003
Revises: 7a08fc0fd19b
Create Date: 2024-02-13 09:37:36.594365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4a5c108a003'
down_revision: Union[str, None] = '7a08fc0fd19b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
