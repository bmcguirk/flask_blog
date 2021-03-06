"""empty message

Revision ID: f37bc05e623e
Revises: d54e919dc630
Create Date: 2016-09-01 14:42:57.425498

"""

# revision identifiers, used by Alembic.
revision = 'f37bc05e623e'
down_revision = 'd54e919dc630'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.drop_column('author', 'is_badass')
    op.alter_column('post', 'live',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'live',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.add_column('author', sa.Column('is_badass', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    ### end Alembic commands ###
