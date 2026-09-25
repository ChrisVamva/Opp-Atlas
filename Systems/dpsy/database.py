import sqlite3
from typing import Optional, List, Tuple, Any


def connect_db(db_path: str = "database.db") -> sqlite3.Connection:
    """Connect to the SQLite database.
    
    Args:
        db_path: Path to the SQLite database file.
    
    Returns:
        sqlite3.Connection: Database connection object.
    """
    conn = sqlite3.connect(db_path)
    return conn


def execute_query(
    conn: sqlite3.Connection,
    query: str,
    params: Optional[Tuple[Any, ...]] = None,
    fetch: bool = False
) -> Optional[List[Tuple[Any, ...]]]:
    """Execute a SQL query with optional parameters.
    
    Args:
        conn: Database connection object.
        query: SQL query to execute.
        params: Parameters for the query (prevents SQL injection).
        fetch: Whether to fetch results (for SELECT queries).
    
    Returns:
        Optional[List[Tuple[Any, ...]]]: Fetched rows if fetch=True, else None.
    """
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return None
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()


def create_table(conn: sqlite3.Connection, table_name: str, schema: str) -> None:
    """Create a table with the given schema.
    
    Args:
        conn: Database connection object.
        table_name: Name of the table to create.
        schema: SQL schema for the table (e.g., "id INTEGER PRIMARY KEY, name TEXT").
    """
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
    execute_query(conn, query)


def insert_data(
    conn: sqlite3.Connection,
    table_name: str,
    columns: str,
    values: Tuple[Any, ...]
) -> None:
    """Insert data into a table.
    
    Args:
        conn: Database connection object.
        table_name: Name of the table.
        columns: Comma-separated column names.
        values: Values to insert.
    """
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({','.join(['?'] * len(values))})"
    execute_query(conn, query, values)


def select_data(
    conn: sqlite3.Connection,
    table_name: str,
    columns: str = "*",
    where_clause: str = "",
    params: Optional[Tuple[Any, ...]] = None
) -> List[Tuple[Any, ...]]:
    """Select data from a table.
    
    Args:
        conn: Database connection object.
        table_name: Name of the table.
        columns: Columns to select (default: "*").
        where_clause: WHERE clause (without "WHERE" keyword).
        params: Parameters for the WHERE clause.
    
    Returns:
        List[Tuple[Any, ...]]: Fetched rows.
    """
    query = f"SELECT {columns} FROM {table_name}"
    if where_clause:
        query += f" WHERE {where_clause}"
    return execute_query(conn, query, params, fetch=True)


def update_data(
    conn: sqlite3.Connection,
    table_name: str,
    updates: str,
    where_clause: str,
    params: Tuple[Any, ...]
) -> None:
    """Update data in a table.
    
    Args:
        conn: Database connection object.
        table_name: Name of the table.
        updates: SET clause (e.g., "name = ?, age = ?").
        where_clause: WHERE clause (without "WHERE" keyword).
        params: Parameters for the query.
    """
    query = f"UPDATE {table_name} SET {updates} WHERE {where_clause}"
    execute_query(conn, query, params)


def delete_data(
    conn: sqlite3.Connection,
    table_name: str,
    where_clause: str,
    params: Optional[Tuple[Any, ...]] = None
) -> None:
    """Delete data from a table.
    
    Args:
        conn: Database connection object.
        table_name: Name of the table.
        where_clause: WHERE clause (without "WHERE" keyword).
        params: Parameters for the WHERE clause.
    """
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    execute_query(conn, query, params)
