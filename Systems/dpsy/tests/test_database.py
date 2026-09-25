import unittest
import sqlite3
import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import connect_db, execute_query


class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a test database"""
        cls.test_db = ":memory:"
        cls.conn = connect_db(cls.test_db)
        
        # Create a test table
        execute_query(cls.conn, """
            CREATE TABLE IF NOT EXISTS test_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                value INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up the test database"""
        if cls.conn:
            cls.conn.close()
    
    def test_insert_operation(self):
        """Test INSERT operation"""
        # Insert a record
        execute_query(self.conn, """
            INSERT INTO test_items (name, value)
            VALUES (?, ?)
        """, ("test_item_1", 100))
        
        # Verify the insertion
        result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("test_item_1",), fetch=True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "test_item_1")
        self.assertEqual(result[0][2], 100)
    
    def test_select_operation(self):
        """Test SELECT operation"""
        # Insert test data
        execute_query(self.conn, "INSERT INTO test_items (name, value) VALUES (?, ?)", ("select_test", 200))
        
        # Test SELECT with WHERE clause
        result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("select_test",), fetch=True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "select_test")
        
        # Test SELECT all
        result = execute_query(self.conn, "SELECT * FROM test_items", fetch=True)
        self.assertGreater(len(result), 0)
    
    def test_update_operation(self):
        """Test UPDATE operation"""
        # Insert a record to update
        execute_query(self.conn, "INSERT INTO test_items (name, value) VALUES (?, ?)", ("update_test", 300))
        
        # Update the record
        execute_query(self.conn, "UPDATE test_items SET value = ? WHERE name = ?", (400, "update_test"))
        
        # Verify the update
        result = execute_query(self.conn, "SELECT value FROM test_items WHERE name = ?", ("update_test",), fetch=True)
        self.assertEqual(result[0][0], 400)
    
    def test_delete_operation(self):
        """Test DELETE operation"""
        # Insert a record to delete
        execute_query(self.conn, "INSERT INTO test_items (name, value) VALUES (?, ?)", ("delete_test", 500))
        
        # Verify it exists
        result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("delete_test",), fetch=True)
        self.assertEqual(len(result), 1)
        
        # Delete the record
        execute_query(self.conn, "DELETE FROM test_items WHERE name = ?", ("delete_test",))
        
        # Verify it's gone
        result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("delete_test",), fetch=True)
        self.assertEqual(len(result), 0)
    
    def test_transaction_rollback(self):
        """Test transaction rollback"""
        try:
            # Start a transaction
            self.conn.execute("BEGIN TRANSACTION")
            
            # Insert a record
            execute_query(self.conn, "INSERT INTO test_items (name, value) VALUES (?, ?)", ("transaction_test", 600))
            
            # Verify it's there
            result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("transaction_test",), fetch=True)
            self.assertEqual(len(result), 1)
            
            # Rollback
            self.conn.rollback()
            
            # Verify it's gone
            result = execute_query(self.conn, "SELECT * FROM test_items WHERE name = ?", ("transaction_test",), fetch=True)
            self.assertEqual(len(result), 0)
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == '__main__':
    unittest.main()