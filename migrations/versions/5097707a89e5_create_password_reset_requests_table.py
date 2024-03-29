"""Create password reset requests table

Revision ID: 5097707a89e5
Revises: 1d1422eca2ba
Create Date: 2016-02-24 17:42:34.569000

"""

# revision identifiers, used by Alembic.
revision = '5097707a89e5'
down_revision = '1d1422eca2ba'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('password_reset_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('used', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('password_reset_request')
    ### end Alembic commands ###
