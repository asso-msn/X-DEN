"""Add asso member

Revision ID: 15811884a1cb
Revises: b48d07c691aa
Create Date: 2021-04-03 19:30:55.528830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15811884a1cb'
down_revision = 'b48d07c691aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('alias', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('avatar_override', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('socials', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'socials')
    op.drop_table('member')
    # ### end Alembic commands ###
