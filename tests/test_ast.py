from ast import AST, Call, ClassDef, FunctionDef, Module, Return

from hvorfra import SELF, get_ast_path, get_caller_location


def test_get_ast_path() -> None:
    class A:
        def f(self) -> tuple[AST, ...]:
            return get_ast_path(get_caller_location(SELF))

    a = A()
    types = [type(n) for n in a.f()]
    assert types == [
        Module,
        FunctionDef,
        ClassDef,
        FunctionDef,
        Return,
        Call,
        Call,
    ]
