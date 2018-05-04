
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocCOMPARISONleftPLUSMINUSleftMULTIPLYDIVIDErightPOWrightUMINUSCOMPARISON CONST_E CONST_PI DIVIDE FLOAT FUNCTION INT LPAREN MINUS MULTIPLY PLUS POW RPAREN VARIABLE\n\t\tresult : expression\n               | empty\n\t\tresult : expression COMPARISON expression\n        expression : INT\n                   | FLOAT\n        \n        expression : CONST_PI\n                   | CONST_E\n        expression : VARIABLEexpression : MINUS expression %prec UMINUSexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression MULTIPLY expressionexpression : expression DIVIDE expressionexpression : expression POW expressionexpression : LPAREN expression RPARENexpression : FUNCTION LPAREN expression RPARENempty : '
    
_lr_action_items = {'INT':([0,9,10,12,13,14,15,16,17,20,],[4,4,4,4,4,4,4,4,4,4,]),'FLOAT':([0,9,10,12,13,14,15,16,17,20,],[5,5,5,5,5,5,5,5,5,5,]),'CONST_PI':([0,9,10,12,13,14,15,16,17,20,],[6,6,6,6,6,6,6,6,6,6,]),'CONST_E':([0,9,10,12,13,14,15,16,17,20,],[7,7,7,7,7,7,7,7,7,7,]),'VARIABLE':([0,9,10,12,13,14,15,16,17,20,],[8,8,8,8,8,8,8,8,8,8,]),'MINUS':([0,2,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,],[9,14,-4,-5,-6,-7,-8,9,9,9,9,9,9,9,9,-9,14,9,14,-10,-11,-12,-13,-14,-15,14,-16,]),'LPAREN':([0,9,10,11,12,13,14,15,16,17,20,],[10,10,10,20,10,10,10,10,10,10,10,]),'FUNCTION':([0,9,10,12,13,14,15,16,17,20,],[11,11,11,11,11,11,11,11,11,11,]),'$end':([0,1,2,3,4,5,6,7,8,18,21,22,23,24,25,26,27,29,],[-17,0,-1,-2,-4,-5,-6,-7,-8,-9,-3,-10,-11,-12,-13,-14,-15,-16,]),'COMPARISON':([2,4,5,6,7,8,18,22,23,24,25,26,27,29,],[12,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'PLUS':([2,4,5,6,7,8,18,19,21,22,23,24,25,26,27,28,29,],[13,-4,-5,-6,-7,-8,-9,13,13,-10,-11,-12,-13,-14,-15,13,-16,]),'MULTIPLY':([2,4,5,6,7,8,18,19,21,22,23,24,25,26,27,28,29,],[15,-4,-5,-6,-7,-8,-9,15,15,15,15,-12,-13,-14,-15,15,-16,]),'DIVIDE':([2,4,5,6,7,8,18,19,21,22,23,24,25,26,27,28,29,],[16,-4,-5,-6,-7,-8,-9,16,16,16,16,-12,-13,-14,-15,16,-16,]),'POW':([2,4,5,6,7,8,18,19,21,22,23,24,25,26,27,28,29,],[17,-4,-5,-6,-7,-8,-9,17,17,17,17,17,17,17,-15,17,-16,]),'RPAREN':([4,5,6,7,8,18,19,22,23,24,25,26,27,28,29,],[-4,-5,-6,-7,-8,-9,27,-10,-11,-12,-13,-14,-15,29,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'result':([0,],[1,]),'expression':([0,9,10,12,13,14,15,16,17,20,],[2,18,19,21,22,23,24,25,26,28,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> result","S'",1,None,None,None),
  ('result -> expression','result',1,'p_result_calc','parser.py',47),
  ('result -> empty','result',1,'p_result_calc','parser.py',48),
  ('result -> expression COMPARISON expression','result',3,'p_result_comp','parser.py',54),
  ('expression -> INT','expression',1,'p_expression_int_float','parser.py',67),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','parser.py',68),
  ('expression -> CONST_PI','expression',1,'p_expression_constant','parser.py',75),
  ('expression -> CONST_E','expression',1,'p_expression_constant','parser.py',76),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','parser.py',81),
  ('expression -> MINUS expression','expression',2,'p_expression_u_minus','parser.py',85),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',89),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',93),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_multiply','parser.py',97),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','parser.py',101),
  ('expression -> expression POW expression','expression',3,'p_expression_power','parser.py',104),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',110),
  ('expression -> FUNCTION LPAREN expression RPAREN','expression',4,'p_expression_function','parser.py',114),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',126),
]
