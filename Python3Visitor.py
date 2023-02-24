# Generated from Python3.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from antlr.Python3Parser import Python3Parser

from ast import *

# Bind operator to their classes
operators = {
    'and': And, 
    'or': Or, 
    '+': UAdd, 
    '-': USub, 
    '*': Mult, 
    '@': MatMult, 
    '/': Div, 
    '%': Mod, 
    '**': Pow, 
    '<<': LShift, 
    '>>': RShift, 
    '|': BitOr, 
    '^': BitXor, 
    '&': BitAnd, 
    '//': FloorDiv, 
    '~': Invert, 
    'not': Not, 
    '==': Eq, 
    '!=': NotEq, 
    '<': Lt, 
    '<=': LtE, 
    '>': Gt, 
    '>=': GtE, 
    'is': Is, 
    'is not': IsNot, 
    'in': In, 
    'not in': NotIn,
}

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.

class Python3Visitor(ParseTreeVisitor):

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None: return nextResult
        elif isinstance(aggregate, list): 
            aggregate.append(nextResult)
            return aggregate
        elif nextResult is None: return aggregate
        else: return [aggregate, nextResult]


    # Visit a parse tree produced by Python3Parser#single_input.
    def visitSingle_input(self, ctx:Python3Parser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx:Python3Parser.File_inputContext):
        body = []
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            childResult = c.accept(self)
            body.append(childResult)

        return Module(body)


    # Visit a parse tree produced by Python3Parser#eval_input.
    def visitEval_input(self, ctx:Python3Parser.Eval_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#decorator.
    def visitDecorator(self, ctx:Python3Parser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#decorators.
    def visitDecorators(self, ctx:Python3Parser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#decorated.
    def visitDecorated(self, ctx:Python3Parser.DecoratedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#async_funcdef.
    def visitAsync_funcdef(self, ctx:Python3Parser.Async_funcdefContext):
        funcdef = ctx.funcdef()
        name = funcdef.NAME().accept(self)
        args = funcdef.parameters().accept(self)

        suite = funcdef.suite().accept(self)

        return AsyncFunctionDef(name, args, suite)


    # Visit a parse tree produced by Python3Parser#funcdef.
    def visitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        name = ctx.NAME().accept(self)
        args = ctx.parameters().accept(self)

        suite = ctx.suite().accept(self)

        return FunctionDef(name, args, suite)


    # Visit a parse tree produced by Python3Parser#parameters.
    def visitParameters(self, ctx:Python3Parser.ParametersContext):
        return ctx.typedargslist().accept(self)


    # Visit a parse tree produced by Python3Parser#typedargslist.
    def visitTypedargslist(self, ctx:Python3Parser.TypedargslistContext):
        argsList = []

        args = ctx.tfpdef()
        for i in range(len(args)):
            c = args[i]
            childResult = c.accept(self)
            argsList.append(childResult)

        return arguments(args=argsList)


    # Visit a parse tree produced by Python3Parser#tfpdef.
    def visitTfpdef(self, ctx:Python3Parser.TfpdefContext):
        return arg(ctx.NAME().accept(self))


    # Visit a parse tree produced by Python3Parser#varargslist.
    def visitVarargslist(self, ctx:Python3Parser.VarargslistContext):
        argsList = []

        args = ctx.vfpdef()
        for i in range(len(args)):
            c = args[i]
            childResult = c.accept(self)
            argsList.append(childResult)

        return arguments(vararg=argsList)


    # Visit a parse tree produced by Python3Parser#vfpdef.
    def visitVfpdef(self, ctx:Python3Parser.VfpdefContext):
        return arg(ctx.NAME().accept(self))


    # Visit a parse tree produced by Python3Parser#stmt.
    def visitStmt(self, ctx:Python3Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#small_stmt.
    def visitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#expr_stmt.
    def visitExpr_stmt(self, ctx:Python3Parser.Expr_stmtContext):

        target = ctx.testlist_star_expr()
        if isinstance(target, list):
            if len(target) == 2:
                targets = target[0].accept(self)
                value = target[1].accept(self)
                return Assign(targets, value)

        return None


    # Visit a parse tree produced by Python3Parser#annassign.
    def visitAnnassign(self, ctx:Python3Parser.AnnassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx:Python3Parser.Testlist_star_exprContext):
        values = []

        tests = ctx.test()
        for i in range(len(tests)):
            c = tests[i]
            childResult = c.accept(self)
            values.append(childResult)

        star_exprs = ctx.star_expr()
        for i in range(len(star_exprs)):
            c = star_exprs[i]
            childResult = c.accept(self)
            values.append(childResult)

        if len(values) == 1:
            return values[0]
        else:
            return values


    # Visit a parse tree produced by Python3Parser#augassign.
    def visitAugassign(self, ctx:Python3Parser.AugassignContext):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by Python3Parser#del_stmt.
    def visitDel_stmt(self, ctx:Python3Parser.Del_stmtContext):
        exprs = ctx.exprlist().accept(self)

        return Delete(exprs)


    # Visit a parse tree produced by Python3Parser#pass_stmt.
    def visitPass_stmt(self, ctx:Python3Parser.Pass_stmtContext):
        return Pass()


    # Visit a parse tree produced by Python3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#break_stmt.
    def visitBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by Python3Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by Python3Parser#return_stmt.
    def visitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        value = ctx.testlist().accept(self)
        return Return(value)


    # Visit a parse tree produced by Python3Parser#yield_stmt.
    def visitYield_stmt(self, ctx:Python3Parser.Yield_stmtContext):
        value = ctx.yield_expr().accept(self)
        return Yield(value)


    # Visit a parse tree produced by Python3Parser#raise_stmt.
    def visitRaise_stmt(self, ctx:Python3Parser.Raise_stmtContext):
        tests = ctx.test()
        exc = test[0].accept(self)
        if len(tests) == 2:
            cause = test[1].accept(self)
            return Raise(exc, cause)

        return Raise(exc)


    # Visit a parse tree produced by Python3Parser#import_stmt.
    def visitImport_stmt(self, ctx:Python3Parser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#import_name.
    def visitImport_name(self, ctx:Python3Parser.Import_nameContext):
        names = ctx.dotted_as_names().accept(self)
        return Import(names)


    # Visit a parse tree produced by Python3Parser#import_from.
    def visitImport_from(self, ctx:Python3Parser.Import_fromContext):
        module = ctx.dotted_name().accept(self)
        names = ctx.import_as_name().accept(self)
        return ImportFrom(module, names)


    # Visit a parse tree produced by Python3Parser#import_as_name.
    def visitImport_as_name(self, ctx:Python3Parser.Import_as_nameContext):
        names = ctx.NAME()
        name = names[0].accept(self)
        if len(names) == 2:
            alias = names[1].accept(self)
            return alias(name, alias)
        return alias(name)


    # Visit a parse tree produced by Python3Parser#dotted_as_name.
    def visitDotted_as_name(self, ctx:Python3Parser.Dotted_as_nameContext):
        name = ctx.dotted_name.accept(self)
        asnameNode = ctx.NAME()
        if asnameNode is not None: 
            asname = asnameNode.accept(self)
            return alias(name, asname)
        return alias(name)


    # Visit a parse tree produced by Python3Parser#import_as_names.
    def visitImport_as_names(self, ctx:Python3Parser.Import_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dotted_as_names.
    def visitDotted_as_names(self, ctx:Python3Parser.Dotted_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dotted_name.
    def visitDotted_name(self, ctx:Python3Parser.Dotted_nameContext):
        names = ctx.NAME()
        attr = names.pop()
        while len(names) > 0:
            value = name.pop()
            attr = Attribute(value, attr, Load())
        return attr


    # Visit a parse tree produced by Python3Parser#global_stmt.
    def visitGlobal_stmt(self, ctx:Python3Parser.Global_stmtContext):
        names = []
        name = ctx.NAME()
        for i in range(len(name)):
            c = name[i]
            childResult = c.accept(self)
            names.append(childResult)

        return Global(names)


    # Visit a parse tree produced by Python3Parser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx:Python3Parser.Nonlocal_stmtContext):
        names = []
        name = ctx.NAME()
        for i in range(len(name)):
            c = name[i]
            childResult = c.accept(self)
            names.append(childResult)

        return Nonlocal(names)


    # Visit a parse tree produced by Python3Parser#assert_stmt.
    def visitAssert_stmt(self, ctx:Python3Parser.Assert_stmtContext):
        tests = ctx.test()
        test = tests[0].accept(self)
        if len(tests) == 2:
            msg = tests[1].accept(self)
            return Assert(test, msg)
        return Assert(test)


    # Visit a parse tree produced by Python3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#async_stmt.
    def visitAsync_stmt(self, ctx:Python3Parser.Async_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#if_stmt.
    def visitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        tests = ctx.test()
        suites = ctx.suite()
        if len(suites) > len(tests):
            curSuite = [suites.pop().accept(self)]
        else:
            curSuite = []
        while len(tests) > 0:
            curTest = tests.pop().accept(self)
            body = suites.pop().accept(self)
            ifstmt = If(curTest, body, curSuite)
            curSuite = ifstmt

        return curSuite


    # Visit a parse tree produced by Python3Parser#while_stmt.
    def visitWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        test = ctx.test().accept(self)
        body = []
        suite = ctx.suite(0).accept(self)

        if ctx.ELSE() is None:
            return While(test, body)

        elseBody = []
        suite = ctx.suite(1).accept(self)
        return While(test, body, elseBody)


    # Visit a parse tree produced by Python3Parser#for_stmt.
    def visitFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#try_stmt.
    def visitTry_stmt(self, ctx:Python3Parser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#with_stmt.
    def visitWith_stmt(self, ctx:Python3Parser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#with_item.
    def visitWith_item(self, ctx:Python3Parser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#except_clause.
    def visitExcept_clause(self, ctx:Python3Parser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#suite.
    def visitSuite(self, ctx:Python3Parser.SuiteContext):
        if ctx.simple_stmt() is not None:
            return [ctx.simple_stmt().accept(self)]

        body = []
        stmts = ctx.stmt()
        for i in range(len(stmts)):
            c = stmts[i]
            childResult = c.accept(self)
            if childResult is not None: body.append(childResult)

        return body


    # Visit a parse tree produced by Python3Parser#test.
    def visitTest(self, ctx:Python3Parser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#test_nocond.
    def visitTest_nocond(self, ctx:Python3Parser.Test_nocondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#lambdef.
    def visitLambdef(self, ctx:Python3Parser.LambdefContext):
        args = ctx.varargslist().accept(self)
        body = ctx.test().accept(self)
        return Lambda(args, body)


    # Visit a parse tree produced by Python3Parser#lambdef_nocond.
    def visitLambdef_nocond(self, ctx:Python3Parser.Lambdef_nocondContext):
        args = ctx.varargslist().accept(self)
        body = ctx.test_nocond().accept(self)
        return Lambda(args, body)


    # Visit a parse tree produced by Python3Parser#or_test.
    def visitOr_test(self, ctx:Python3Parser.Or_testContext):
        ors = ctx.and_test()
        n = len(ors)
        if n == 1:
            return self.visitChildren(ctx)
        
        curr = ors.pop().accept(self)
        while len(ors) > 0:
            nextAnd = ors.pop().accept(self)
            curr = BoolOp(Or(), [curr, nextAnd])

        return curr


    # Visit a parse tree produced by Python3Parser#and_test.
    def visitAnd_test(self, ctx:Python3Parser.And_testContext):
        ands = ctx.not_test()
        n = len(ands)
        if n == 1:
            return self.visitChildren(ctx)
        
        curr = ands.pop().accept(self)
        while len(ands) > 0:
            nextAnd = ands.pop().accept(self)
            curr = BoolOp(And(), [curr, nextAnd])

        return curr


    # Visit a parse tree produced by Python3Parser#not_test.
    def visitNot_test(self, ctx:Python3Parser.Not_testContext):
        test = ctx.not_test()
        if test is None:
            return self.visitChildren(ctx)
        return UnaryOp(Not(), test.accept(self))


    # Visit a parse tree produced by Python3Parser#comparison.
    def visitComparison(self, ctx:Python3Parser.ComparisonContext):
        exprs = ctx.expr()
        if len(exprs) == 1:
            return self.visitChildren(ctx)
        
        tests = ctx.comp_op()
        test = []
        expr = []
        n = len(tests)
        for i in range(n):
            c = tests[i]
            childResult = c.accept(self)
            test.append(childResult)

            c = exprs[i+1]
            childResult = c.accept(self)
            expr.append(childResult)

        left = exprs[0].accept(self)

        return Compare(left, test, expr)

    
    # Visit a parse tree produced by Python3Parser#comp_op.
    def visitComp_op(self, ctx:Python3Parser.Comp_opContext):
        op = ctx.getChild(0).accept(self)
        clazz = operators[op]
        
        return clazz()


    # Visit a parse tree produced by Python3Parser#star_expr.
    def visitStar_expr(self, ctx:Python3Parser.Star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#expr.
    def visitExpr(self, ctx:Python3Parser.ExprContext):
        expr = ctx.xor_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        right = expr.pop().accept(self)
        while len(expr) > 0:
            left = expr.pop().accept(self)
            right = BinOp(left, BitOr(), right)

        return right


    # Visit a parse tree produced by Python3Parser#xor_expr.
    def visitXor_expr(self, ctx:Python3Parser.Xor_exprContext):
        expr = ctx.and_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        right = expr.pop().accept(self)
        while len(expr) > 0:
            left = expr.pop().accept(self)
            right = BinOp(left, BitXor(), right)

        return right


    # Visit a parse tree produced by Python3Parser#and_expr.
    def visitAnd_expr(self, ctx:Python3Parser.And_exprContext):
        expr = ctx.shift_expr()
        if len(expr) == 1:
            return self.visitChildren(ctx)

        right = expr.pop().accept(self)
        while len(expr) > 0:
            left = expr.pop().accept(self)
            right = BinOp(left, BitAnd(), right)

        return right


    # Visit a parse tree produced by Python3Parser#shift_expr.
    def visitShift_expr(self, ctx:Python3Parser.Shift_exprContext):
        childs = list(ctx.getChildren())
        right = childs.pop().accept(self)
        while len(childs) > 0:
            opSign = childs.pop().accept(self)
            op = operators.get(opSign)()
            left = childs.pop().accept(self)
            right = BinOp(left, op, right)

        return right


    # Visit a parse tree produced by Python3Parser#arith_expr.
    def visitArith_expr(self, ctx:Python3Parser.Arith_exprContext):
        childs = list(ctx.getChildren())
        right = childs.pop().accept(self)
        while len(childs) > 0:
            opSign = childs.pop().accept(self)
            op = Add() if opSign == "+" else Sub()
            left = childs.pop().accept(self)
            right = BinOp(left, op, right)

        return right


    # Visit a parse tree produced by Python3Parser#term.
    def visitTerm(self, ctx:Python3Parser.TermContext):
        childs = list(ctx.getChildren())
        right = childs.pop().accept(self)
        while len(childs) > 0:
            opSign = childs.pop().accept(self)
            op = operators.get(opSign)()
            left = childs.pop().accept(self)
            right = BinOp(left, op, right)

        return right


    # Visit a parse tree produced by Python3Parser#factor.
    def visitFactor(self, ctx:Python3Parser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        opSign = ctx.getChild(0).accept(self)
        op = operators.get(opSign)()
        expr = ctx.getChild(1).accept(self)

        return UnaryOp(op, expr)


    # Visit a parse tree produced by Python3Parser#power.
    def visitPower(self, ctx:Python3Parser.PowerContext):
        childs = list(ctx.getChildren())
        right = childs.pop().accept(self)
        while len(childs) > 0:
            opSign = childs.pop().accept(self)
            op = operators.get(opSign)()
            left = childs.pop().accept(self)
            right = BinOp(left, op, right)

        return right


    # Visit a parse tree produced by Python3Parser#atom_expr.
    def visitAtom_expr(self, ctx:Python3Parser.Atom_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#atom.
    def visitAtom(self, ctx:Python3Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#testlist_comp.
    def visitTestlist_comp(self, ctx:Python3Parser.Testlist_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#trailer.
    def visitTrailer(self, ctx:Python3Parser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#subscriptlist.
    def visitSubscriptlist(self, ctx:Python3Parser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#subscript.
    def visitSubscript(self, ctx:Python3Parser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#sliceop.
    def visitSliceop(self, ctx:Python3Parser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#exprlist.
    def visitExprlist(self, ctx:Python3Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#testlist.
    def visitTestlist(self, ctx:Python3Parser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx:Python3Parser.DictorsetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#classdef.
    def visitClassdef(self, ctx:Python3Parser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#arglist.
    def visitArglist(self, ctx:Python3Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#argument.
    def visitArgument(self, ctx:Python3Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#comp_iter.
    def visitComp_iter(self, ctx:Python3Parser.Comp_iterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#comp_for.
    def visitComp_for(self, ctx:Python3Parser.Comp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#comp_if.
    def visitComp_if(self, ctx:Python3Parser.Comp_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#encoding_decl.
    def visitEncoding_decl(self, ctx:Python3Parser.Encoding_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#yield_expr.
    def visitYield_expr(self, ctx:Python3Parser.Yield_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#yield_arg.
    def visitYield_arg(self, ctx:Python3Parser.Yield_argContext):
        return self.visitChildren(ctx)

    def visitTerminal(self, node):
        txt = node.getText()
        if txt.isspace():
            return None
        return node.getText()


del Python3Parser