__author__ = 'jlyman'


class ExceptionError(Exception):
    pass


class IsNotInteger(ExceptionError):
    pass


class IsNotText(ExceptionError):
    pass


class NotValidName(ExceptionError):
    pass


class NameContainsInteger(ExceptionError):
    pass


class NameContainsSymbol(ExceptionError):
    pass


class NameLessThanTwoCharacters(ExceptionError):
    pass


class PlayerAlreadyExists(ExceptionError):
    pass


class AddPlayerToDatabaseFailure(ExceptionError):
    pass


class IdIsNotInteger(ExceptionError):
    pass


class IdNotExist(ExceptionError):
    pass


class IdEqualsZero(ExceptionError):
    pass


class PlayerNotFound(ExceptionError):
    pass


class EditPlayerMethodNotSupported(ExceptionError):
    pass


class DeletePlayerMethodNotSupported(ExceptionError):
    pass


class EditPlayerFailure(ExceptionError):
    pass


class DeletePlayerFailure(ExceptionError):
    pass


class ListPlayersFailure(ExceptionError):
    pass


class PlayersDatabaseContainsNoData(ExceptionError):
    pass


class MatchesDatabaseContainsNoData(ExceptionError):
    pass


class AuditLogDatabaseContainsNoData(ExceptionError):
    pass


class GeneralMatchExecutionFailure(ExceptionError):
    pass


class MatchPlayerCountNotSatisfied(ExceptionError):
    pass


class MatchPlayerNotFound(ExceptionError):
    pass


class MatchReportWinFailure(ExceptionError):
    pass


class SwissListPlayersFailure(ExceptionError):
    pass


class SwissMatchesWithMatchesPlayersFailure(ExceptionError):
    pass


class DeleteMatchFailure(ExceptionError):
    pass


class ListMatchFailure(ExceptionError):
    pass


class ListMatchIdNotFound(ExceptionError):
    pass


class DeleteMatchIdNotFound(ExceptionError):
    pass


class LatestMatchFailure(ExceptionError):
    pass


class LookupMatchFailure(ExceptionError):
    pass


class LookupMatchIdNotFound(ExceptionError):
    pass


class ListWinRankingFailure(ExceptionError):
    pass


class MatchNotFound(ExceptionError):
    pass