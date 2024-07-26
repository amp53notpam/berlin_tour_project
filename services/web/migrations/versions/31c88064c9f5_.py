"""empty message

Revision ID: 31c88064c9f5
Revises: 3f8dd9f6c383
Create Date: 2024-07-25 22:26:17.075817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31c88064c9f5'
down_revision = '3f8dd9f6c383'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.alter_column('check_in',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.alter_column('check_in',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###