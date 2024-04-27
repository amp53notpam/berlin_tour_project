"""add done col to lap

Revision ID: a65344032fa2
Revises: 89632dc4467f
Create Date: 2024-04-22 15:12:12.450352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a65344032fa2'
down_revision = '89632dc4467f'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lap', schema=None) as batch_op:
        batch_op.add_column(sa.Column('done', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lap', schema=None) as batch_op:
        batch_op.drop_column('done')

    # ### end Alembic commands ###


def upgrade_db_sec():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_db_sec():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
