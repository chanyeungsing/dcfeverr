"""empty message

Revision ID: 886e5d52fe2d
Revises: e3f3903a8983
Create Date: 2023-04-27 06:25:39.232567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886e5d52fe2d'
down_revision = 'e3f3903a8983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TradingItem', schema=None) as batch_op:
        batch_op.drop_constraint('TradingItem_type_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'TradingType', ['type'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('TradingItem', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('TradingItem_type_fkey', 'TradingItem', ['type'], ['id'])

    # ### end Alembic commands ###
