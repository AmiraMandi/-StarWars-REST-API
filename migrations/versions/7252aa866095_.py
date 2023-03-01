"""empty message

Revision ID: 7252aa866095
Revises: 8204ac9d84cc
Create Date: 2023-02-27 19:28:01.164595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7252aa866095'
down_revision = '8204ac9d84cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###
