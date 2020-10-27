"""change column name

Revision ID: fc446cb8e823
Revises: 9edfbe885a7d
Create Date: 2020-10-26 20:49:44.239310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc446cb8e823'
down_revision = '9edfbe885a7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###