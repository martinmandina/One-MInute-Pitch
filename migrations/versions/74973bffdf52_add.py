"""add

Revision ID: 74973bffdf52
Revises: db2e36f7abaf
Create Date: 2020-10-29 14:53:19.240207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74973bffdf52'
down_revision = 'db2e36f7abaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pitches', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('pitches', 'post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('post', sa.TEXT(), autoincrement=False, nullable=False))
    op.alter_column('pitches', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###