---
title: "Alembic: Data Migrations"
date: "2016-09-06"
permalink: "/blog/2016/09/06/AlembicDataMigrations.html"
tags: [python, sql, til]
---



We use Alembic__ to perform schema migrations
whenever we add (or drop) tables or columns
from our databases.
It's less well known that Alembic can also perform data migrations,
updating existing data in tables.

Here's an example adapted from a migration I put together this afternoon.
I added a non-NULL Boolean ``stooge`` column to the ``old_timers`` table,
with a default value of ``FALSE``.
I wanted to update certain rows to have ``stooge=TRUE`` as part of the migration.
The following works with PostgreSQL.

Note the ``server_default=sa.false()`` in the declaration of the ``stooge`` column,
which is needed to initially set all instances of ``stooge=FALSE``.
I then declare a ``table`` which has only the two columns needed for the migration.
Finally, I execute an ``update`` on the table.

__ http://alembic.zzzcomputing.com/en/latest/

.. sourcecode:: python

    from alembic import op
    import sqlalchemy as sa
    from sqlalchemy.sql import table

    StoogeNames = (
        "Larry - Production",
        "Moe - Production",
        "Curly - Production",
    )

    def upgrade():
        op.add_column(
            'old_timers',
            sa.Column('stooge',
                      sa.Boolean(),
                      nullable=False,
                      server_default=sa.false()))

        old_timers = table(
            'old_timers',
            sa.Column('name', sa.VARCHAR(length=40)),
            sa.Column('stooge', sa.Boolean())
            # Other columns not needed for the data migration
        )

        op.execute(
            old_timers
                .update()
                .where(old_timers.c.name.in_(StoogeNames))
                .values({'stooge': True})
        )

    def downgrade():
        op.drop_column('old_timers', 'stooge')

.. _permalink:
    /blog/2016/09/06/AlembicDataMigrations.html
