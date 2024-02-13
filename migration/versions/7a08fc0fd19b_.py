"""empty message

Revision ID: 7a08fc0fd19b
Revises: dd14453415c8
Create Date: 2024-02-13 09:36:27.566609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a08fc0fd19b'
down_revision: Union[str, None] = 'dd14453415c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
