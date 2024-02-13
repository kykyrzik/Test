"""empty message

Revision ID: dd14453415c8
Revises: dd83e29a9755
Create Date: 2024-02-13 09:34:53.195240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd14453415c8'
down_revision: Union[str, None] = 'dd83e29a9755'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
