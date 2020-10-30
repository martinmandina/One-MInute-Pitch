"""category

Revision ID: db2e36f7abaf
Revises: c8673706c753
Create Date: 2020-10-27 21:24:58.842104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db2e36f7abaf'
down_revision = 'c8673706c753'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=False))
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###