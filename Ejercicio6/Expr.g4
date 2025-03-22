grammar Expr;

root : expr EOF;

expr : expr '+' expr
     | INT
     ;

INT : [0-9]+;
WS  : [ \t\r\n]+ -> skip;