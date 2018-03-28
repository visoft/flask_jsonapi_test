"""create person table

Revision ID: 3b409572f654
Revises:
Create Date: 2018-03-27 16:55:15.857288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b409572f654'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('person')
