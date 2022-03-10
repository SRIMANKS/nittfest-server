"""
Points table
Revision ID: 5a408d60055d
Revises: ba11687fdd5a
Create Date: 2022-03-09 14:02:28.762825

"""
# pylint: skip-file

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5a408d60055d"
down_revision = "ba11687fdd5a"
branch_labels = None
depends_on = None


def upgrade():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "points",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("point", sa.Float(), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("department_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["department_id"],
            ["departments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("points")
    # ### end Alembic commands ###
