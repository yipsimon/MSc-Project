import scriptlibrary as sp
import time, sys, copy, re

string = 'a'*3
'''
#Test 1 - Input Read File
automata = sp.callreadauto('test.txt')
automata.printauto()
sp.autoprocess(automata,string,0)
'''
'''
#Test 2 - Input Read Regex
regex = 'a*,<x:a*>,a*'
automata = sp.regextoauto(regex)
automata.printauto()
sp.autoprocess(automata,string,1)
'''
'''
#Test 3 - Input Insert manally
automata = sp.initauto(0,0,0)
automata.reset()
automata.states = ['0','1','2']
automata.varstates = ['x']
automata.transition['0'] = [('0','a'),('1','x+')]
automata.transition['1'] = [('1','a'),('2','x-')]
automata.transition['2'] = [('2','a')]
automata.start = '0'
automata.end = '2'
automata.printauto()
sp.autoprocess(automata,string,0)
'''

#Test 4 - Spanner Algebra
'''
#Test 4.1 - Union
automata1 = sp.initauto(0,0,0)
automata1.reset()
automata1.states = ['0','1','2']
automata1.varstates = ['x']
automata1.transition['0'] = [('0','a'),('1','x+')]
automata1.transition['1'] = [('1','a'),('2','x-')]
automata1.transition['2'] = [('2','a')]
automata1.start = '0'
automata1.end = '2'


automata2 = sp.initauto(0,0,0)
automata2.reset()
automata2.states = ['0','1','2']
automata2.varstates = ['x']
automata2.transition['0'] = [('0','a'),('1','x+')]
automata2.transition['1'] = [('1','a'),('2','x-')]
automata2.transition['2'] = [('2','a')]
automata2.start = '0'
automata2.end = '2'

sp.initialprocess(automata1)
sp.initialprocess(automata2)
grph1 = sp.callgenAg(automata1,string)
grph2 = sp.callgenAg(automata2,string)


sp.callunion(automata1,automata2)
sp.callprintgraph(automata1,'test')

#Test 4.2 - Projection
automata1 = sp.initauto(0,0,0)
automata1.reset()
automata1.states = ['0','1','2','3','4']
automata1.varstates = ['x','y']
automata1.transition['0'] = [('0','a'),('1','x+')]
automata1.transition['1'] = [('1','a'),('2','y+')]
automata1.transition['2'] = [('2','a'),('3','x-')]
automata1.transition['3'] = [('3','a'),('4','y-')]
automata1.transition['4'] = [('4','a')]
automata1.start = '0'
automata1.end = '4'
sp.initialprocess(automata1)
automata1.printauto()
auto = sp.callprojection(automata1,['x'])
auto.printauto()

#Test 4.3 - Natural Join
automata1 = sp.initauto(0,0,0)
automata1.reset()
automata1.states = ['0','1','2','3','4']
automata1.varstates = ['x','y']
automata1.transition['0'] = [('0','a'),('1','x+')]
automata1.transition['1'] = [('1','a'),('2','y+')]
automata1.transition['2'] = [('2','a'),('3','x-')]
automata1.transition['3'] = [('3','a'),('4','y-')]
automata1.transition['4'] = [('4','a')]
automata1.start = '0'
automata1.end = '4'

automata2 = sp.initauto(0,0,0)
automata2.reset()
automata2.states = ['0','1','2','3','4']
automata2.varstates = ['x','y']
automata2.transition['0'] = [('0','a'),('1','y+')]
automata2.transition['1'] = [('1','a'),('2','x+')]
automata2.transition['2'] = [('2','a'),('3','y-')]
automata2.transition['3'] = [('3','a'),('4','x-')]
automata2.transition['4'] = [('4','a')]
automata2.start = '0'
automata2.end = '4'

sp.initialprocess(automata1)
sp.initialprocess(automata2)
auto = sp.calljoin(automata1,automata2)
sp.callprintgraph(auto,'test')

#Test 4.4 - String Equality
automata1 = sp.initauto(0,0,0)
automata1.reset()
automata1.states = ['0','1','2','3','4']
automata1.varstates = ['x','y']
automata1.transition['0'] = [('0','a'),('1','x+')]
automata1.transition['1'] = [('1','a'),('2','y+')]
automata1.transition['2'] = [('2','a'),('3','x-')]
automata1.transition['3'] = [('3','a'),('4','y-')]
automata1.transition['4'] = [('4','a')]
automata1.start = '0'
automata1.end = '4'
sp.autostringequ(automata1,string,['x','y'],0)
'''

#Example 1

start_prctime = time.time()
start_time = time.time()
'''
automata1 = sp.initauto(0,0,0)
automata1.reset()
automata1.states = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
automata1.varstates = ['x']
automata1.transition['0'] = [('0','(.)'),('1','x+')]
automata1.transition['1'] = [('2','[0-9]')]
automata1.transition['2'] = [('3','[0-9]'),('4','[epsi]')]
automata1.transition['3'] = [('4','[0-9]'),('4','[epsi]')]
automata1.transition['4'] = [('5','.')]
automata1.transition['5'] = [('6','[0-9]')]
automata1.transition['6'] = [('7','[0-9]'),('8','[epsi]')]
automata1.transition['7'] = [('8','[0-9]'),('8','[epsi]')]
automata1.transition['8'] = [('9','.')]
automata1.transition['9'] = [('10','[0-9]')]
automata1.transition['10'] = [('11','[0-9]'),('12','[epsi]')]
automata1.transition['11'] = [('12','[0-9]'),('12','[epsi]')]
automata1.transition['12'] = [('13','.')]
automata1.transition['13'] = [('14','[0-9]')]
automata1.transition['14'] = [('15','[0-9]'),('16','[epsi]')]
automata1.transition['15'] = [('16','[0-9]'),('16','[epsi]')]
automata1.transition['16'] = [('17','x-')]
automata1.transition['17'] = [('17','(.)')]
automata1.start = '0'
automata1.end = '17'
automata1.last = 17
'''
'''
regex = '(.)*,<x:[0-9],[0-9]*,.,[0-9],[0-9]*,.,[0-9],[0-9]*,.,[0-9],[0-9]*>,(.)*'
regex2 = '(.)*,<y:[0-9],[0-9]*,/,[A-za-z],[A-za-z]*,/,[0-9],[0-9]*>,(.)*'
automata1 = sp.regextoauto(regex)
automata2 = sp.regextoauto(regex2)
sp.initialprocess(automata1)
sp.initialprocess(automata2)
#sp.callfunck(automata1)
#sp.callcepsilon(automata1)
#sg.printgraph(automata1,'test00')

f = open('access_log2', 'r')
string = f.read()
f.close() #\d+\.

#condits = [(lambda s,i,j: re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$',s[j-1:j+i-1]))] #,(lambda s,i,j: s[j+i-2:j+i-1] in ['0','1','2','3','4','5','6','7','8','9'], 'true')] #,(lambda i: i % 7 == 0, "seven")]
#,(lambda s,i,j: re.match(r'^(?<=' ')\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=' ')$',s[j-2:j+i-1]))]
#(lambda s,i,j: True if j-1 == 0 else (True if re.match(r'^[^0-9]$',s[j-2]) else False) ),\
			#(lambda s,i,j: True if j+i-1 == len(string) else (True if re.match(r'^[^0-9]$',s[j+i-1]) else False) )]

condits = [(lambda s,i,j: True if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',s[j-1:j+i-1]) )]#,\
string, automata = sp.calstringeq(string,1,29,30)#,condits)

print("stringeq : %s seconds" % (time.time() - start_time))
start_time = time.time()
#sg.printgraphconfig(automata,automata.varconfig,'test2')
#sys.exit(1)
#objgraph.show_most_common_types()
#sc1.funchk(automata)

sp.callcepsilon(automata)
print("toepsilion : %s seconds" % (time.time() - start_time))
start_time = time.time()

automata = sp.calljoin(automata,automata1)
print("Joined : %s seconds" % (time.time() - start_time))
start_time = time.time()

finalgraph = sp.callgenAg(automata,string)
print("Ag graph : %s seconds" % (time.time() - start_time))
start_time = time.time()

#test = sg.finalauto(automata,finalgraph)

outputs = sp.callcalcresults(finalgraph, len(string), automata.varconfig)
print("Calc : %s seconds" % (time.time() - start_time))
start_time = time.time()


sp.callprintresultsv2(outputs,automata,string,0,0,1,1)
print("Total Time: %s seconds" % (time.time() - start_prctime))
#objgraph.show_most_common_types()
'''


automata = sp.initauto(0,0,0)
automata.reset()
automata.states = ['0','1','2','3']
automata.varstates = ['x']
automata.transition['0'] = [('0','a'),('1','x+')]
automata.transition['1'] = [('2','a')]
automata.transition['2'] = [('3','x-')]
automata.transition['3'] = []
automata.start = '0'
automata.end = '3'
automata.printauto()
sp.autoprocess(automata,string,0)





'''
string = 'aaa'
sp.initialprocess(automata1)
automata1.printauto()
'''

#automata1.printauto()
#sp.printgraph(automata1,'test00')
'''
automata1 = sc2.automata(0,0,0)
automata1.reset()
automata1.states = ['0','1','2','3','4']
automata1.varstates = ['x','y']
automata1.transition['0'] = [('0','a'),('1','x+')]
automata1.transition['1'] = [('1','a'),('2','y+')]
automata1.transition['2'] = [('2','a'),('3','x-')]
automata1.transition['3'] = [('3','a'),('4','y-')]
automata1.transition['4'] = [('4','a')]
automata1.start = '0'
automata1.end = '4'
'''