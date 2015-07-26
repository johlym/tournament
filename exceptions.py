__author__ = 'jlyman'


class ExceptionError(Exception):
    pass


class IsNotIntegerError(ExceptionError):
    pass


class IsNotTextError(ExceptionError):
    pass


class NotValidNameError(ExceptionError):
    pass


class NameContainsIntegerError(ExceptionError):
    pass


class NameContainsSymbolError(ExceptionError):
    pass


class NameLessThanTwoCharactersError(ExceptionError):
    pass


class NameNotProvidedError(ExceptionError):
    pass


class PlayerAlreadyExistsError(ExceptionError):
    pass


class AddPlayerToDatabaseFailureError(ExceptionError):
    pass


class IdIsNotIntegerError(ExceptionError):
    pass


class IdNotExistError(ExceptionError):
    pass


class IdEqualsZeroError(ExceptionError):
    pass


class PlayerNotFoundError(ExceptionError):
    pass


class EditPlayerMethodNotSupportedError(ExceptionError):
    pass


class DeletePlayerMethodNotSupportedError(ExceptionError):
    pass


class EditPlayerFailureError(ExceptionError):
    pass


class DeletePlayerFailureError(ExceptionError):
    pass


class ListPlayersFailureError(ExceptionError):
    pass


class PlayersDatabaseContainsNoDataError(ExceptionError):
    pass


class MatchesDatabaseContainsNoDataError(ExceptionError):
    pass


class AuditLogDatabaseContainsNoDataError(ExceptionError):
    pass


class GeneralMatchExecutionFailureError(ExceptionError):
    pass


class MatchPlayerCountNotSatisfiedError(ExceptionError):
    pass


class MatchPlayerNotFoundError(ExceptionError):
    pass


class MatchReportWinFailureError(ExceptionError):
    pass


class SwissListPlayersFailureError(ExceptionError):
    pass


class SwissMatchesWithMatchesPlayersFailureError(ExceptionError):
    pass


class DeleteMatchFailureError(ExceptionError):
    pass


class ListMatchFailureError(ExceptionError):
    pass


class ListMatchIdNotFoundError(ExceptionError):
    pass


class DeleteMatchIdNotFoundError(ExceptionError):
    pass


class LatestMatchFailureError(ExceptionError):
    pass


class LookupMatchFailureError(ExceptionError):
    pass


class LookupMatchIdNotFoundError(ExceptionError):
    pass


class ListWinRankingFailureError(ExceptionError):
    pass


class MatchNotFoundError(ExceptionError):
    pass
