
from lib2to3.pytree import Base


class BaseAst:
    def __init__(self, ast_type) -> None:
        self.ast_type = ast_type

class FunDef(BaseAst):
    def __init__(self, ident_type: str, ident_name: str, arg_list: list, stmt_list: list) -> None:
        super().__init__("FunDef")
        self.ident_type = ident_type
        self.ident_name = ident_name
        self.arg_list = arg_list
        self.stmt_list = stmt_list

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        print(f"{prefix}Function name: {self.ident_type} {self.ident_name}")
        for arg in self.arg_list:
            if arg is not None:
                arg.show(indt+1)
        for stmt in self.stmt_list:
            if stmt is not None:
                stmt.show(indt+1)

class ItemList(BaseAst):
    def __init__(self) -> None:
        super().__init__("List")
        self.content_list = list()

    def append_item(self, item) -> None:
        self.content_list.append(item)

class Arg(BaseAst):
    def __init__(self, ident_type: str, ident_name: str) -> None:
        super().__init__("Arg")
        self.ident_type = ident_type
        self.ident_name = ident_name

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        print(f"{prefix}Arg: {self.ident_type} {self.ident_name}")

class Decl(BaseAst):
    def __init__(self, ident_type: str, ident_list: list) -> None:
        super().__init__("Decl")
        self.ident_type = ident_type
        self.ident_list = ident_list

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        print(f"{prefix}Arg: {self.ident_type} {', '.join(self.ident_list)}")


class ForAst(BaseAst):
    def __init__(self, expr1, expr2, expr3, stmt) -> None:
        super().__init__("ForAst")
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.stmt = stmt

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        if self.expr1 is not None:
            self.expr1.show(indt+1)
        if self.expr2 is not None:
            self.expr2.show(indt+1)
        if self.expr3 is not None:
            self.expr3.show(indt+1)
        if self.stmt is not None:
            self.stmt.show(indt+1)

class WhileAst(BaseAst):
    def __init__(self, expr, stmt) -> None:
        super().__init__("WhileAst")
        self.expr = expr
        self.stmt = stmt

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        if self.expr is not None:
            self.expr.show(indt+1)
        if self.stmt is not None:
            self.stmt.show(indt+1)

class IfAst(BaseAst):
    def __init__(self, expr, if_stmt, else_stmt) -> None:
        super().__init__("IfAst")
        self.expr = expr
        self.if_stmt = if_stmt
        self.else_stmt = else_stmt

    def show(self, indt: int):
        prefix = '-'*indt*4
        print(f"{prefix}Node type: {self.ast_type}")
        if self.expr is not None:
            self.expr.show(indt+1)
        if self.if_stmt is not None:
            self.if_stmt.show(indt+1)
        if self.else_stmt is not None:
            self.else_stmt.show(indt+1)

class ExprAst(BaseAst):
    def __init__(self, lt, op, rt) -> None:
        super().__init__("ExprAst")
        self.lt = lt
        self.rt = rt
        self.op = op
    
    def show(self, indt: int):
        prefix = '-'*indt*4
        prefix2 = '-'*(indt+1)*4
        print(f"{prefix}Node type: {self.ast_type}")

        if self.lt is not None:
            if isinstance(self.lt, BaseAst):
                self.lt.show(indt+1)
            else:
                 print(f"{prefix2}left operand: {self.lt}")

        if self.op is not None:
            print(f"{prefix2}operator: {self.op}")
        
        if self.rt is not None:
            if isinstance(self.rt, BaseAst):
                self.rt.show(indt+1)
            else:
                 print(f"{prefix2}right operand: {self.rt}")

