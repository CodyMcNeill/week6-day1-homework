"""test migration

Revision ID: d41cf0570277
Revises: 2f12ede66881
Create Date: 2023-02-06 14:21:58.807908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd41cf0570277'
down_revision = '2f12ede66881'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('poke_name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['poke_name'], ['pokemon.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('poke_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    # ### end Alembic commands ###
