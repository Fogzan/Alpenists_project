"""initial

Revision ID: 09da06eeaf43
Revises: 
Create Date: 2023-11-04 07:21:25.150858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09da06eeaf43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('climbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_climbers'))
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_groups'))
    )
    op.create_table('mountains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('coutry', sa.String(length=100), nullable=False),
    sa.Column('district', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mountains'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login'))
    )
    op.create_table('climbers_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climbers_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['climbers_id'], ['climbers.id'], name=op.f('fk_climbers_groups_climbers_id_climbers')),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name=op.f('fk_climbers_groups_group_id_groups')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_climbers_groups'))
    )
    op.create_table('climbings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_start', sa.DateTime(), nullable=False),
    sa.Column('date_end', sa.DateTime(), nullable=False),
    sa.Column('mountains_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name=op.f('fk_climbings_group_id_groups')),
    sa.ForeignKeyConstraint(['mountains_id'], ['mountains.id'], name=op.f('fk_climbings_mountains_id_mountains')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_climbings'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('climbings')
    op.drop_table('climbers_groups')
    op.drop_table('users')
    op.drop_table('mountains')
    op.drop_table('groups')
    op.drop_table('climbers')
    # ### end Alembic commands ###
