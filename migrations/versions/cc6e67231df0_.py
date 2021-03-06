"""empty message

Revision ID: cc6e67231df0
Revises: 
Create Date: 2019-12-01 23:25:13.433085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc6e67231df0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('birth_date', sa.Date(), nullable=True))
    op.add_column('employee', sa.Column('salary', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'salary')
    op.drop_column('employee', 'birth_date')
    # ### end Alembic commands ###
