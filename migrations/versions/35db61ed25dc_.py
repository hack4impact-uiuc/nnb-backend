"""empty message

Revision ID: 35db61ed25dc
Revises: 8f886fc039b0
Create Date: 2017-11-14 13:55:11.092699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35db61ed25dc'
down_revision = '8f886fc039b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stories', sa.Column('story_names_id', sa.Integer(), nullable=True))
    op.alter_column('stories', 'poi_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('stories_story_uuid_fkey', 'stories', type_='foreignkey')
    op.create_foreign_key(None, 'stories', 'story_names', ['story_names_id'], ['id'])
    op.drop_column('stories', 'story_uuid')
    op.alter_column('story_names', 'story_name',
               existing_type=sa.VARCHAR(),
               nullable=0)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('story_names', 'story_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('stories', sa.Column('story_uuid', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'stories', type_='foreignkey')
    op.create_foreign_key('stories_story_uuid_fkey', 'stories', 'story_names', ['story_uuid'], ['id'])
    op.alter_column('stories', 'poi_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('stories', 'story_names_id')
    # ### end Alembic commands ###
