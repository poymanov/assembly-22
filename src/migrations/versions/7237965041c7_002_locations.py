"""002 locations

Revision ID: 7237965041c7
Revises: 6535b4392f17
Create Date: 2020-03-16 17:42:24.542180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7237965041c7'
down_revision = '6535b4392f17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locations')
    # ### end Alembic commands ###