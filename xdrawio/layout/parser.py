import pyparsing as pp

from .stack import *

def ParseSpec(layoutspec):
    return eval(layoutspec)

def cvtH(toks):
    s = HStack()
    s.items = toks.asList()
    return s

def cvtV(toks):
    s = VStack()
    s.items = toks.asList()
    return s

def cvtIdentity(toks):
    return FixLayout(toks[0])

def parseLayoutSpec(spec):
    # define punctuation as suppressed literals
    lparen, rparen, lbrack, rbrack, lbrace, rbrace, colon, comma = map(
        pp.Suppress, "()[]{}:,"
    )
    HFunc = pp.Suppress(pp.Keyword("H", caseless=True))
    VFunc = pp.Suppress(pp.Keyword("V", caseless=True))

    ident = pp.Word(pp.alphas, pp.alphanums + "_").setName("identifier").setParseAction(cvtIdentity)
    pp.quotedString.setParseAction(lambda t: t[0][1:-1], cvtIdentity)
    hStr = pp.Forward()
    vStr = pp.Forward()

    layoutItem = hStr | vStr | ident | pp.quotedString

    hStr <<= (
        HFunc + lparen + pp.Optional(pp.delimitedList(layoutItem)) + rparen
    )

    vStr <<= (
        VFunc + lparen + pp.Optional(pp.delimitedList(layoutItem)) + rparen
    )

    hStr.setParseAction(cvtH)
    vStr.setParseAction(cvtV)

    result = layoutItem.parseString(spec)
    return result[0]
