import fdb

# The server is named 'bison'; the database file is at '/temp/test.db'.
con  = fdb.connect (dsn ="d:\\1\2.fdb", user ='sysdba', password ='masterkey')

# Or, equivalently:
con = fdb.connect(
    host ='bison', database="d:\\1\2.fdb",
    user ='sysdba', password ='masterkey'
  )