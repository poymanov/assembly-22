"""004 make location code unique

Revision ID: 6d8dac873e40
Revises: 5cfc9dd9c1cf
Create Date: 2020-03-16 19:36:57.568264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d8dac873e40'
down_revision = '5cfc9dd9c1cf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint('locations_code_key', 'locations', ['code'])


def downgrade():
    op.drop_constraint('locations_code_key', 'locations')
