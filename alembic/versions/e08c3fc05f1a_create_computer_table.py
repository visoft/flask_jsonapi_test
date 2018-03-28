"""create computer table

Revision ID: e08c3fc05f1a
Revises: 3b409572f654
Create Date: 2018-03-28 09:23:02.545128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e08c3fc05f1a'
down_revision = '3b409572f654'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'computer',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('serial', sa.String(50), nullable=False),
        sa.Column('person_id', sa.Integer, sa.ForeignKey('person.id'))
    )


def downgrade():
    op.drop_table('computer')
