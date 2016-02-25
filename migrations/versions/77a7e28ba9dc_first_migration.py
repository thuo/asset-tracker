"""First migration

Revision ID: 77a7e28ba9dc
Revises: None
Create Date: 2016-02-19 16:14:47.672000

"""

# revision identifiers, used by Alembic.
revision = '77a7e28ba9dc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    role = op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=66), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('serial_no', sa.String(length=64), nullable=True),
    sa.Column('code', sa.String(length=64), nullable=True),
    sa.Column('purchased', sa.DateTime(), nullable=True),
    sa.Column('added_by_id', sa.Integer(), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('lost', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['added_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('google_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('google_id', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('google_id')
    )
    op.create_table('invitation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=20), nullable=True),
    sa.Column('invitee', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('assignment',
    sa.Column('asset_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], ['asset.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )

    op.bulk_insert(role, [
        {
            'id': 1,
            'short': 'superadmin',
            'title': 'Super Administrator',
            'description': "Can add other admins",
            'level': 0
        },
        {
            'id': 2,
            'short': 'admin',
            'title': 'Administrator',
            'description': "Can assign assets to staff",
            'level': 1
        },
        {
            'id': 3,
            'short': 'staff',
            'title': 'Staff Member',
            'description': "Can report found assets",
            'level': 2
        },
    ])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignment')
    op.drop_table('roles')
    op.drop_table('invitation')
    op.drop_table('google_user')
    op.drop_table('asset')
    op.drop_table('user')
    op.drop_table('role')
    ### end Alembic commands ###