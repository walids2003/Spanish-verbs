import pandas as pd
import numpy as np
def table_creator(verb):
    d = {'Present': verb_solver_present_simple_tense(verb), 'Imperfect': verb_solver_imperfect_simple_tense(verb)}
    dataframe = pd.DataFrame(data=d)
    return dataframe
def verb_type(infinitive_verb):
    match infinitive_verb[-2:]:
        case 'ir':return 'ir'
        case 'ar':return 'ar'
        case 'er':return 'er'
        case default:return 'Invalid verb'
def verb_solver_present_simple_tense(verb):
    translation = {'ir':ir_solver_present_simple_tense, 'er':er_solver_present_simple_tense, 'ar':ar_solver_present_simple_tense}
    ending = verb_type(verb)
    return translation[ending](verb)
def ar_solver_present_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'o'   ,
              'Tú '       + verb + 'as'  ,
              'Él '       + verb + 'a'   ,
              'Ella '     + verb + 'a'   ,
              'Nosotros ' + verb + 'amos',
              'Vosotros ' + verb + 'ais' ,
              'Ellos '    + verb + 'an'  ,
              'Ellas '    + verb + 'an']
    return result
def er_solver_present_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'o'   ,
              'Tú '       + verb + 'es'  ,
              'Él '       + verb + 'e'   ,
              'Ella '     + verb + 'e'   ,
              'Nosotros ' + verb + 'emos',
              'Vosotros ' + verb + 'eis' ,
              'Ellos '    + verb + 'en'  ,
              'Ellas '    + verb + 'en']
    return result
def ir_solver_present_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'o'   ,
              'Tú '       + verb + 'es'  ,
              'Él '       + verb + 'e'   ,
              'Ella '     + verb + 'e'   ,
              'Nosotros ' + verb + 'imos',
              'Vosotros ' + verb + 'is'  ,
              'Ellos '    + verb + 'en'  ,
              'Ellas '    + verb + 'en']
    return result
def verb_solver_imperfect_simple_tense(verb):
    translation = {'ir':ir_solver_imperfect_simple_tense, 'er':er_solver_imperfect_simple_tense, 'ar':ar_solver_imperfect_simple_tense}
    ending = verb_type(verb)
    return translation[ending](verb)
def ar_solver_imperfect_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'aba'   ,
              'Tú '       + verb + 'abas'  ,
              'Él '       + verb + 'aba'   ,
              'Ella '     + verb + 'aba'   ,
              'Nosotros ' + verb + 'ábamos',
              'Vosotros ' + verb + 'abais' ,
              'Ellos '    + verb + 'aban'  ,
              'Ellas '    + verb + 'aban']
    return result
def er_solver_imperfect_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'ía'   ,
              'Tú '       + verb + 'ías'  ,
              'Él '       + verb + 'ía'   ,
              'Ella '     + verb + 'ía'   ,
              'Nosotros ' + verb + 'íamos',
              'Vosotros ' + verb + 'íais' ,
              'Ellos '    + verb + 'ían'  ,
              'Ellas '    + verb + 'ían']
    return result
def ir_solver_imperfect_simple_tense(verb):
    verb = verb[:-2]
    result = ['Yo '       + verb + 'ía'   ,
              'Tú '       + verb + 'ías'  ,
              'Él '       + verb + 'ía'   ,
              'Ella '     + verb + 'ía'   ,
              'Nosotros ' + verb + 'íamos',
              'Vosotros ' + verb + 'íais' ,
              'Ellos '    + verb + 'ían'  ,
              'Ellas '    + verb + 'ían']
    return result
#print(verb_solver_imperfect_simple_tense('Amar'))
#print(verb_solver_imperfect_simple_tense('Temer'))
#print(verb_solver_imperfect_simple_tense('Partir'))
print(table_creator('Amar'))