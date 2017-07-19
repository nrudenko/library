"""Initial database structure.

Revision ID: 2626ce7c4878
Revises:
Create Date: 2017-07-19 11:14:53.016162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2626ce7c4878'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=13), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('title', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('is_confirmed', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('auth_credential',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], [u'author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], [u'book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], [u'book.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('following',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], [u'user.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('close_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], [u'book.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], [u'role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('transaction_hash', sa.String(length=32), nullable=False),
    sa.Column('is_successful', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], [u'order.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('close_date', sa.Date(), nullable=False),
    sa.Column('book_price_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], [u'book.id'], ),
    sa.ForeignKeyConstraint(['book_price_id'], [u'book_price.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('amount_to_pay', sa.Float(), nullable=False),
    sa.Column('rent_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], [u'order.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['rent_id'], [u'rent.id'], onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('rent')
    op.drop_table('payment_transaction')
    op.drop_table('user_role')
    op.drop_table('review')
    op.drop_table('order')
    op.drop_table('following')
    op.drop_table('book_price')
    op.drop_table('author_book')
    op.drop_table('auth_credential')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###
