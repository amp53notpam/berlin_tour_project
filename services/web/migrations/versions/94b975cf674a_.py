"""empty message

Revision ID: 94b975cf674a
Revises: 517f15a7a7cf
Create Date: 2024-10-10 23:27:55.260930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94b975cf674a'
down_revision = '517f15a7a7cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trip_images', schema=None) as batch_op:
        batch_op.alter_column('img_src',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=96),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trip_images', schema=None) as batch_op:
        batch_op.alter_column('img_src',
               existing_type=sa.String(length=96),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)

    # ### end Alembic commands ###
