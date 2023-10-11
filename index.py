from enum import Enum


class InvalidMetaCommandException(Exception):
    "Raised when an invalid meta-command is entered"
    pass


class InvalidStatementException(Exception):
    "Raised when an invalid SQL statement is entered"
    pass


class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = 1
    META_COMMAND_UNRECOGNIZED_COMMAND = 2


class PrepareResult(Enum):
    PREPARE_SUCCESS = 1
    PREPARE_UNRECOGNIZED_STATEMENT = 2


class StatementType(Enum):
    STATEMENT_INSERT = 1
    STATEMENT_SELECT = 2


def do_meta_command(cmd: str) -> MetaCommandResult:
    """Run a meta-command on the DB Server

    Run the specified meta-command beginning with '.'
    Meta-commands are commands that begin with a period '.', and are not part of the regular SQL syntax.
    They signify meta operations on the DB server itself.

    Args:
        cmd (str): The input command

    Returns:
        MetaCommandResult: The status of command execution

    Raises:
        InvalidMetaCommandException: Raised when an unrecognized meta-command is entered
    """
    match cmd:
        case ".exit":
            print("Shutting down...")
            exit()
        case _:
            raise InvalidMetaCommandException


def prepare_statement(stmt: str) -> PrepareResult:
    """Prepare an SQL statement for execution by the VM

    Convert an SQL statement into a structure understandable by the Virtual Machine which processes the request further

    Args:
        stmt (str): The input statement

    Returns:
        PrepareResult: The result of internal structure preparation

    Raises:
        InvalidStatementException: Raised when an unrecognized statement is entered
    """
    ...


def execute_statement(stmt: str) -> None:
    """Execute the input SQL statement

    Prepare the SQL statement as per convention, and execute it.

    Args:
        stmt (str): The input statement

    Returns:
        None

    Raises:
        InvalidStatementException: Raised when an unrecognized statement is entered
    """
    ...


def main():
    while True:
        cmd = input("db > ")
        if cmd[0] == ".":
            try:
                do_meta_command(cmd)
            except InvalidMetaCommandException as e:
                print(e)
                continue
            except Exception as e:
                print("Unrecognized error occurred, please retry.")
        else:
            try:
                match (prepare_statement(cmd)):
                    case PrepareResult.PREPARE_SUCCESS:
                        print("Prepared")
                    case _:
                        print("This command is not known")
            except InvalidMetaCommandException as e:
                print(e)
                continue
            except Exception as e:
                print("Unrecognized error occurred, please retry.")

        execute_statement(cmd)
        print("Executed")


if __name__ == "__main__":
    main()
