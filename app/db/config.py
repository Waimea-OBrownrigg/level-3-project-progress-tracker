#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class UserTable:

    NAME = "users"

    SCHEMA = """
        CREATE TABLE users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            username    TEXT NOT NULL,
            pass_hash   INT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO users (username, pass_hash)
        VALUES
            ("PlaceMcholder","1")
    """

class TrackerTable:

    NAME = "projects"

    SCHEMA = """
        CREATE TABLE projects (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            desc   TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO projects (name)
        VALUES
            ("Really Cool Project")
    """

class TargetTable:

    NAME = "milestones"

    SCHEMA = """
        CREATE TABLE milestones (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT NOT NULL,
            status       BOOLEAN NOT NULL,
            project_id   INT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO milestones (name, status, project_id)
        VALUES
            ("Really Cool Project", "TRUE", "1")
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    UserTable,
    TrackerTable
]

