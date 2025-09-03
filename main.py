from cli import runCLI
from database import getConnection

def main() -> None:
    connection, cursor = getConnection()
    runCLI(cursor)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
