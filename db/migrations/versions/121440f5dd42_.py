"""empty message

Revision ID: 121440f5dd42
Revises: c85a14ed5561
Create Date: 2023-11-09 15:08:36.738254

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '121440f5dd42'
down_revision = 'c85a14ed5561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('username')

    op.drop_table('user')
    with op.batch_alter_table('refactoring_statistics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('refactoring_date', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('reduction_amount', sa.Float(), nullable=False))
        batch_op.drop_column('total_reduction')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('refactoring_statistics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_reduction', mysql.FLOAT(), nullable=False))
        batch_op.drop_column('reduction_amount')
        batch_op.drop_column('refactoring_date')

    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('username', ['username'], unique=False)
        batch_op.create_index('email', ['email'], unique=False)

    # ### end Alembic commands ###
