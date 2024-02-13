"""empty message

Revision ID: 45ecf599f9dc
Revises: 46078f4fd8c7
Create Date: 2024-02-13 09:27:47.154179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45ecf599f9dc'
down_revision: Union[str, None] = '46078f4fd8c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
