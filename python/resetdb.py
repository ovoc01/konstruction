import logging




def reset_db(connection):
   try:
      # Set up logging
      logging.basicConfig(level=logging.INFO)
      logger = logging.getLogger(__name__)

      cursor = connection.cursor()

      # Retrieve all table names
      cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'"
      )
      tables = [table[0] for table in cursor.fetchall()]

      # Disable all table constraints temporarily
      for table in tables:
            cursor.execute(f"ALTER TABLE {table} DISABLE TRIGGER ALL")
            logger.info(f"Disabled triggers on table: {table}")

      # Truncate all tables
      for table in tables:
         cursor.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE")
         logger.info(f"Truncated table: {table}")

      # Reset all sequences to 1
      cursor.execute(
         "SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = 'public'"
      )
      sequences = [sequence[0] for sequence in cursor.fetchall()]
      
      for sequence in sequences:
         cursor.execute(f"ALTER SEQUENCE {sequence} RESTART WITH 1")
         logger.info(f"Reset sequence: {sequence}")

      # Re-enable all table constraints
      for table in tables:
         cursor.execute(f"ALTER TABLE {table} ENABLE TRIGGER ALL")
         logger.info(f"Enabled triggers on table: {table}")

      connection.commit()
      logger.info("Tables truncated and sequences reset successfully.")

   except Exception as error:
      if connection:
         connection.rollback()
      logger.error("Error:", error)

   finally:
      if cursor:
         cursor.close()



def generate_sequence(connection):
   cursor = connection.cursor()

      # Retrieve all table names
   cursor.execute(
         "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'"
   )
   tables = [table[0] for table in cursor.fetchall()]

      # Disable all table constraints temporarily
   for table in tables:
      seq_name = f"seq_{table}"
      try:
            cursor.execute(f"create sequence  {seq_name}")
            
      except psycopg2.errors.DuplicateTable:
         cursor.execute(f"ALTER SEQUENCE {seq_name} RESTART WITH 1")
   
   connection.commit()
         




##generate_sequence(conn)
#truncate_tables_and_reset_sequences(conn)
