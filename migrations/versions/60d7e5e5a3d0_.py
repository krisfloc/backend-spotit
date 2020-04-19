"""empty message

Revision ID: 60d7e5e5a3d0
Revises: 82025de14996
Create Date: 2020-04-19 14:16:00.315219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d7e5e5a3d0'
down_revision = '82025de14996'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('VeiwPoint', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('VeiwPoint', 'title')
    # ### end Alembic commands ###
