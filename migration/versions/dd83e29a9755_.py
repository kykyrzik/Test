"""empty message

Revision ID: dd83e29a9755
Revises: 45ecf599f9dc
Create Date: 2024-02-13 09:30:10.948817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd83e29a9755'
down_revision: Union[str, None] = '45ecf599f9dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
