"""Initial migration

Revision ID: 89632dc4467f
Revises:
Create Date: 2024-04-22 15:07:30.050280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89632dc4467f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lap',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date', sa.DATE(), nullable=False),
                    sa.Column('start', sa.String(length=32), nullable=False),
                    sa.Column('destination', sa.String(length=32), nullable=False),
                    sa.Column('distance', sa.Float(), nullable=True),
                    sa.Column('ascent', sa.Integer(), nullable=True),
                    sa.Column('descent', sa.Integer(), nullable=True),
                    sa.Column('duration', sa.Time(), nullable=True),
                    sa.Column('gpx', sa.String(length=48), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('date')
                    )
    op.create_table('hotel',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=48), nullable=False),
                    sa.Column('address', sa.String(length=48), nullable=False),
                    sa.Column('town', sa.String(length=32), nullable=False),
                    sa.Column('check_in', sa.DATE(), nullable=False),
                    sa.Column('check_out', sa.DATE(), nullable=True),
                    sa.Column('reserved', sa.BOOLEAN(), nullable=True),
                    sa.Column('price', sa.Integer(), nullable=True),
                    sa.Column('photo', sa.String(length=48), nullable=True),
                    sa.Column('link', sa.String(), nullable=True),
                    sa.Column('lap_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['lap_id'], ['lap.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotel')
    op.drop_table('lap')
    # ### end Alembic commands ###


def upgrade_db_sec():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=64), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    # ### end Alembic commands ###


def downgrade_db_sec():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###