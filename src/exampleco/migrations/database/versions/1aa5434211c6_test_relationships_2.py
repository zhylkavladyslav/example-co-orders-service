"""test relationships 2

Revision ID: 1aa5434211c6
Revises: b8fff6fe9421
Create Date: 2022-09-07 20:22:36.400238

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1aa5434211c6'
down_revision = 'b8fff6fe9421'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_items', 'order_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('order_items', 'service_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.create_foreign_key(None, 'order_items', 'services', ['service_id'], ['id'])
    op.create_foreign_key(None, 'order_items', 'order', ['order_id'], ['id'])
    op.drop_column('order_items', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_items', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'order_items', type_='foreignkey')
    op.drop_constraint(None, 'order_items', type_='foreignkey')
    op.alter_column('order_items', 'service_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('order_items', 'order_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
