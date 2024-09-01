#pylint:disable=W0613
from queue import deque

""" Charles Truscott Watters, developing my own algorithm to solve the Rubik's cube 2 x 2 Byron Bay NSW 2481. Thank you John Flynn Hospital and Byron Bay Hospital. Thank you MITx, MIT OCW and Harvard CCE """

""" Thank you Byron Central Hospital Tuckeroo. Thank you Eric Grimson, John Guttag and Ana Bell and all at MITx """



# August 30, International Day of the Disappeared


""" Update: Today (Sep 1 2024) is one of the greatest days of my life..My father is surviving strong, my brother is very capable and my treatment at Tuckeroo is going great, now prescribed clozapine, fluvoxamine. It took me all night to get the invariant correctly posed in syntax. Now the symbolic computation loop invariant has been made, with dynamic programming, I just have to put meaning to the mnemonic of matrix algebra of cubits, e.g six sides or 8 cubits with 3 colors per cubit """

""" LOOP INVARIANT. On another note going to proudly docstring the matrix cubit computation class methods for coherent explanation 

[]
<__main__.RubiksState object at 0x7b4b907150> ['L', 'L']
<__main__.RubiksState object at 0x7b4b907210> ['L', 'L2']
<__main__.RubiksState object at 0x7b4b907290> ['L', 'L inverse']
<__main__.RubiksState object at 0x7b4b907310> ['L', 'R']
<__main__.RubiksState object at 0x7b4b907390> ['L', 'R2']
<__main__.RubiksState object at 0x7b4b907410> ['L', 'R inverse']
<__main__.RubiksState object at 0x7b4b907490> ['L', 'U']
<__main__.RubiksState object at 0x7b4b907510> ['L', 'U2']
<__main__.RubiksState object at 0x7b4b907590> ['L', 'Up inverse']
<__main__.RubiksState object at 0x7b4b907610> ['L', 'D']
<__main__.RubiksState object at 0x7b4b907690> ['L', 'D2']
<__main__.RubiksState object at 0x7b4b907710> ['L', 'Down inverse']
<__main__.RubiksState object at 0x7b4b907790> ['L', 'F']
<__main__.RubiksState object at 0x7b4b907810> ['L', 'F2']
<__main__.RubiksState object at 0x7b4b907890> ['L', 'F inverse']
<__main__.RubiksState object at 0x7b4b907910> ['L', 'B']
<__main__.RubiksState object at 0x7b4b907990> ['L', 'B2']
<__main__.RubiksState object at 0x7b4b907a10> ['L', 'B inverse']
<__main__.RubiksState object at 0x7b4b907110> ['L2', 'L']
<__main__.RubiksState object at 0x7b4b907ad0> ['L2', 'L2']
<__main__.RubiksState object at 0x7b4b907b50> ['L2', 'L inverse']
<__main__.RubiksState object at 0x7b4b907bd0> ['L2', 'R']
<__main__.RubiksState object at 0x7b4b907c50> ['L2', 'R2']
<__main__.RubiksState object at 0x7b4b907cd0> ['L2', 'R inverse']
<__main__.RubiksState object at 0x7b4b907d90> ['L2', 'U']
<__main__.RubiksState object at 0x7b4b907e50> ['L2', 'U2']
<__main__.RubiksState object at 0x7b4b907f10> ['L2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b907fd0> ['L2', 'D']
<__main__.RubiksState object at 0x7b4b91c0d0> ['L2', 'D2']
<__main__.RubiksState object at 0x7b4b91c190> ['L2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b91c250> ['L2', 'F']
<__main__.RubiksState object at 0x7b4b91c310> ['L2', 'F2']
<__main__.RubiksState object at 0x7b4b91c3d0> ['L2', 'F inverse']
<__main__.RubiksState object at 0x7b4b91c490> ['L2', 'B']
<__main__.RubiksState object at 0x7b4b91c550> ['L2', 'B2']
<__main__.RubiksState object at 0x7b4b91c610> ['L2', 'B inverse']
<__main__.RubiksState object at 0x7b4b91c0d0> ['L inverse', 'L']
<__main__.RubiksState object at 0x7b4b91c710> ['L inverse', 'L2']
<__main__.RubiksState object at 0x7b4b91c7d0> ['L inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b91c890> ['L inverse', 'R']
<__main__.RubiksState object at 0x7b4b91c950> ['L inverse', 'R2']
<__main__.RubiksState object at 0x7b4b91ca10> ['L inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b91cad0> ['L inverse', 'U']
<__main__.RubiksState object at 0x7b4b91cb90> ['L inverse', 'U2']
<__main__.RubiksState object at 0x7b4b91cc50> ['L inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b91cd10> ['L inverse', 'D']
<__main__.RubiksState object at 0x7b4b91cdd0> ['L inverse', 'D2']
<__main__.RubiksState object at 0x7b4b91ce90> ['L inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b91cf50> ['L inverse', 'F']
<__main__.RubiksState object at 0x7b4b91d010> ['L inverse', 'F2']
<__main__.RubiksState object at 0x7b4b91d0d0> ['L inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b91d190> ['L inverse', 'B']
<__main__.RubiksState object at 0x7b4b91d250> ['L inverse', 'B2']
<__main__.RubiksState object at 0x7b4b91d310> ['L inverse', 'B inverse']
<__main__.RubiksState object at 0x7b4b91c610> ['R', 'L']
<__main__.RubiksState object at 0x7b4b91d410> ['R', 'L2']
<__main__.RubiksState object at 0x7b4b91d4d0> ['R', 'L inverse']
<__main__.RubiksState object at 0x7b4b91d590> ['R', 'R']
<__main__.RubiksState object at 0x7b4b91d650> ['R', 'R2']
<__main__.RubiksState object at 0x7b4b91d710> ['R', 'R inverse']
<__main__.RubiksState object at 0x7b4b91d7d0> ['R', 'U']
<__main__.RubiksState object at 0x7b4b91d890> ['R', 'U2']
<__main__.RubiksState object at 0x7b4b91d950> ['R', 'Up inverse']
<__main__.RubiksState object at 0x7b4b91da10> ['R', 'D']
<__main__.RubiksState object at 0x7b4b91dad0> ['R', 'D2']
<__main__.RubiksState object at 0x7b4b91db90> ['R', 'Down inverse']
<__main__.RubiksState object at 0x7b4b91dc50> ['R', 'F']
<__main__.RubiksState object at 0x7b4b91dd10> ['R', 'F2']
<__main__.RubiksState object at 0x7b4b91ddd0> ['R', 'F inverse']
<__main__.RubiksState object at 0x7b4b91de90> ['R', 'B']
<__main__.RubiksState object at 0x7b4b91df50> ['R', 'B2']
<__main__.RubiksState object at 0x7b4b91e010> ['R', 'B inverse']
<__main__.RubiksState object at 0x7b4b91d310> ['R2', 'L']
<__main__.RubiksState object at 0x7b4b91e110> ['R2', 'L2']
<__main__.RubiksState object at 0x7b4b91e1d0> ['R2', 'L inverse']
<__main__.RubiksState object at 0x7b4b91e290> ['R2', 'R']
<__main__.RubiksState object at 0x7b4b91e350> ['R2', 'R2']
<__main__.RubiksState object at 0x7b4b91e410> ['R2', 'R inverse']
<__main__.RubiksState object at 0x7b4b91e4d0> ['R2', 'U']
<__main__.RubiksState object at 0x7b4b91e590> ['R2', 'U2']
<__main__.RubiksState object at 0x7b4b91e650> ['R2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b91e710> ['R2', 'D']
<__main__.RubiksState object at 0x7b4b91e7d0> ['R2', 'D2']
<__main__.RubiksState object at 0x7b4b91e890> ['R2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b91e950> ['R2', 'F']
<__main__.RubiksState object at 0x7b4b91ea10> ['R2', 'F2']
<__main__.RubiksState object at 0x7b4b91ead0> ['R2', 'F inverse']
<__main__.RubiksState object at 0x7b4b91eb90> ['R2', 'B']
<__main__.RubiksState object at 0x7b4b91ec50> ['R2', 'B2']
<__main__.RubiksState object at 0x7b4b91ed10> ['R2', 'B inverse']
<__main__.RubiksState object at 0x7b4b91e010> ['R inverse', 'L']
<__main__.RubiksState object at 0x7b4b91ee10> ['R inverse', 'L2']
<__main__.RubiksState object at 0x7b4b91eed0> ['R inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b91ef90> ['R inverse', 'R']
<__main__.RubiksState object at 0x7b4b91f050> ['R inverse', 'R2']
<__main__.RubiksState object at 0x7b4b91f110> ['R inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b91f1d0> ['R inverse', 'U']
<__main__.RubiksState object at 0x7b4b91f290> ['R inverse', 'U2']
<__main__.RubiksState object at 0x7b4b91f350> ['R inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b91f410> ['R inverse', 'D']
<__main__.RubiksState object at 0x7b4b91f4d0> ['R inverse', 'D2']
<__main__.RubiksState object at 0x7b4b91f590> ['R inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b91f650> ['R inverse', 'F']
<__main__.RubiksState object at 0x7b4b91f710> ['R inverse', 'F2']
<__main__.RubiksState object at 0x7b4b91f7d0> ['R inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b91f890> ['R inverse', 'B']
<__main__.RubiksState object at 0x7b4b91f950> ['R inverse', 'B2']
<__main__.RubiksState object at 0x7b4b91fa10> ['R inverse', 'B inverse']
<__main__.RubiksState object at 0x7b4b91ed10> ['U', 'L']
<__main__.RubiksState object at 0x7b4b91fb10> ['U', 'L2']
<__main__.RubiksState object at 0x7b4b91fbd0> ['U', 'L inverse']
<__main__.RubiksState object at 0x7b4b91fc90> ['U', 'R']
<__main__.RubiksState object at 0x7b4b8bb090> ['U', 'R2']
<__main__.RubiksState object at 0x7b4b8b9750> ['U', 'R inverse']
<__main__.RubiksState object at 0x7b4b91fa10> ['U', 'U']
<__main__.RubiksState object at 0x7b4b91fd90> ['U', 'U2']
<__main__.RubiksState object at 0x7b4b91fe50> ['U', 'Up inverse']
<__main__.RubiksState object at 0x7b4b91ff10> ['U', 'D']
<__main__.RubiksState object at 0x7b4b91ffd0> ['U', 'D2']
<__main__.RubiksState object at 0x7b4b9200d0> ['U', 'Down inverse']
<__main__.RubiksState object at 0x7b4b920190> ['U', 'F']
<__main__.RubiksState object at 0x7b4b920250> ['U', 'F2']
<__main__.RubiksState object at 0x7b4b920310> ['U', 'F inverse']
<__main__.RubiksState object at 0x7b4b9203d0> ['U', 'B']
<__main__.RubiksState object at 0x7b4b920490> ['U', 'B2']
<__main__.RubiksState object at 0x7b4b920550> ['U', 'B inverse']
<__main__.RubiksState object at 0x7b4b9200d0> ['U2', 'L']
<__main__.RubiksState object at 0x7b4b920650> ['U2', 'L2']
<__main__.RubiksState object at 0x7b4b920710> ['U2', 'L inverse']
<__main__.RubiksState object at 0x7b4b9207d0> ['U2', 'R']
<__main__.RubiksState object at 0x7b4b920890> ['U2', 'R2']
<__main__.RubiksState object at 0x7b4b920950> ['U2', 'R inverse']
<__main__.RubiksState object at 0x7b4b920a10> ['U2', 'U']
<__main__.RubiksState object at 0x7b4b920ad0> ['U2', 'U2']
<__main__.RubiksState object at 0x7b4b920b90> ['U2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b920c50> ['U2', 'D']
<__main__.RubiksState object at 0x7b4b920d10> ['U2', 'D2']
<__main__.RubiksState object at 0x7b4b920dd0> ['U2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b920e90> ['U2', 'F']
<__main__.RubiksState object at 0x7b4b920f50> ['U2', 'F2']
<__main__.RubiksState object at 0x7b4b921010> ['U2', 'F inverse']
<__main__.RubiksState object at 0x7b4b9210d0> ['U2', 'B']
<__main__.RubiksState object at 0x7b4b921190> ['U2', 'B2']
<__main__.RubiksState object at 0x7b4b921250> ['U2', 'B inverse']
<__main__.RubiksState object at 0x7b4b920550> ['Up inverse', 'L']
<__main__.RubiksState object at 0x7b4b921350> ['Up inverse', 'L2']
<__main__.RubiksState object at 0x7b4b921410> ['Up inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b9214d0> ['Up inverse', 'R']
<__main__.RubiksState object at 0x7b4b921590> ['Up inverse', 'R2']
<__main__.RubiksState object at 0x7b4b921650> ['Up inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b921710> ['Up inverse', 'U']
<__main__.RubiksState object at 0x7b4b9217d0> ['Up inverse', 'U2']
<__main__.RubiksState object at 0x7b4b921890> ['Up inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b921950> ['Up inverse', 'D']
<__main__.RubiksState object at 0x7b4b921a10> ['Up inverse', 'D2']
<__main__.RubiksState object at 0x7b4b921ad0> ['Up inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b921b90> ['Up inverse', 'F']
<__main__.RubiksState object at 0x7b4b921c50> ['Up inverse', 'F2']
<__main__.RubiksState object at 0x7b4b921d10> ['Up inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b921dd0> ['Up inverse', 'B']
<__main__.RubiksState object at 0x7b4b921e90> ['Up inverse', 'B2']
<__main__.RubiksState object at 0x7b4b921f50> ['Up inverse', 'B inverse']
<__main__.RubiksState object at 0x7b4b921250> ['D', 'L']
<__main__.RubiksState object at 0x7b4b922050> ['D', 'L2']
<__main__.RubiksState object at 0x7b4b922110> ['D', 'L inverse']
<__main__.RubiksState object at 0x7b4b9221d0> ['D', 'R']
<__main__.RubiksState object at 0x7b4b922290> ['D', 'R2']
<__main__.RubiksState object at 0x7b4b922350> ['D', 'R inverse']
<__main__.RubiksState object at 0x7b4b922410> ['D', 'U']
<__main__.RubiksState object at 0x7b4b9224d0> ['D', 'U2']
<__main__.RubiksState object at 0x7b4b922590> ['D', 'Up inverse']
<__main__.RubiksState object at 0x7b4b922650> ['D', 'D']
<__main__.RubiksState object at 0x7b4b922710> ['D', 'D2']
<__main__.RubiksState object at 0x7b4b9227d0> ['D', 'Down inverse']
<__main__.RubiksState object at 0x7b4b922890> ['D', 'F']
<__main__.RubiksState object at 0x7b4b922950> ['D', 'F2']
<__main__.RubiksState object at 0x7b4b922a10> ['D', 'F inverse']
<__main__.RubiksState object at 0x7b4b922ad0> ['D', 'B']
<__main__.RubiksState object at 0x7b4b922b90> ['D', 'B2']
<__main__.RubiksState object at 0x7b4b922c50> ['D', 'B inverse']
<__main__.RubiksState object at 0x7b4b921f50> ['D2', 'L']
<__main__.RubiksState object at 0x7b4b922d50> ['D2', 'L2']
<__main__.RubiksState object at 0x7b4b922e10> ['D2', 'L inverse']
<__main__.RubiksState object at 0x7b4b922ed0> ['D2', 'R']
<__main__.RubiksState object at 0x7b4b922f90> ['D2', 'R2']
<__main__.RubiksState object at 0x7b4b923050> ['D2', 'R inverse']
<__main__.RubiksState object at 0x7b4b923110> ['D2', 'U']
<__main__.RubiksState object at 0x7b4b9231d0> ['D2', 'U2']
<__main__.RubiksState object at 0x7b4b923290> ['D2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b923350> ['D2', 'D']
<__main__.RubiksState object at 0x7b4b923410> ['D2', 'D2']
<__main__.RubiksState object at 0x7b4b9234d0> ['D2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b923590> ['D2', 'F']
<__main__.RubiksState object at 0x7b4b923650> ['D2', 'F2']
<__main__.RubiksState object at 0x7b4b923710> ['D2', 'F inverse']
<__main__.RubiksState object at 0x7b4b9237d0> ['D2', 'B']
<__main__.RubiksState object at 0x7b4b923890> ['D2', 'B2']
<__main__.RubiksState object at 0x7b4b923950> ['D2', 'B inverse']
<__main__.RubiksState object at 0x7b4b922c50> ['Down inverse', 'L']
<__main__.RubiksState object at 0x7b4b923a50> ['Down inverse', 'L2']
<__main__.RubiksState object at 0x7b4b923b10> ['Down inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b923bd0> ['Down inverse', 'R']
<__main__.RubiksState object at 0x7b4b923c90> ['Down inverse', 'R2']
<__main__.RubiksState object at 0x7b4b923d50> ['Down inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b923e10> ['Down inverse', 'U']
<__main__.RubiksState object at 0x7b4b923ed0> ['Down inverse', 'U2']
<__main__.RubiksState object at 0x7b4b923f90> ['Down inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b924090> ['Down inverse', 'D']
<__main__.RubiksState object at 0x7b4b924150> ['Down inverse', 'D2']
<__main__.RubiksState object at 0x7b4b924210> ['Down inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b9242d0> ['Down inverse', 'F']
<__main__.RubiksState object at 0x7b4b924390> ['Down inverse', 'F2']
<__main__.RubiksState object at 0x7b4b924450> ['Down inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b924510> ['Down inverse', 'B']
<__main__.RubiksState object at 0x7b4b9245d0> ['Down inverse', 'B2']
<__main__.RubiksState object at 0x7b4b924690> ['Down inverse', 'B inverse']
<__main__.RubiksState object at 0x7b4b924090> ['F', 'L']
<__main__.RubiksState object at 0x7b4b924790> ['F', 'L2']
<__main__.RubiksState object at 0x7b4b924850> ['F', 'L inverse']
<__main__.RubiksState object at 0x7b4b924910> ['F', 'R']
<__main__.RubiksState object at 0x7b4b9249d0> ['F', 'R2']
<__main__.RubiksState object at 0x7b4b924a90> ['F', 'R inverse']
<__main__.RubiksState object at 0x7b4b924b50> ['F', 'U']
<__main__.RubiksState object at 0x7b4b924c10> ['F', 'U2']
<__main__.RubiksState object at 0x7b4b924cd0> ['F', 'Up inverse']
<__main__.RubiksState object at 0x7b4b924d90> ['F', 'D']
<__main__.RubiksState object at 0x7b4b924e50> ['F', 'D2']
<__main__.RubiksState object at 0x7b4b924f10> ['F', 'Down inverse']
<__main__.RubiksState object at 0x7b4b924fd0> ['F', 'F']
<__main__.RubiksState object at 0x7b4b925090> ['F', 'F2']
<__main__.RubiksState object at 0x7b4b925150> ['F', 'F inverse']
<__main__.RubiksState object at 0x7b4b925210> ['F', 'B']
<__main__.RubiksState object at 0x7b4b9252d0> ['F', 'B2']
<__main__.RubiksState object at 0x7b4b925390> ['F', 'B inverse']
<__main__.RubiksState object at 0x7b4b924690> ['F2', 'L']
<__main__.RubiksState object at 0x7b4b925490> ['F2', 'L2']
<__main__.RubiksState object at 0x7b4b925550> ['F2', 'L inverse']
<__main__.RubiksState object at 0x7b4b925610> ['F2', 'R']
<__main__.RubiksState object at 0x7b4b9256d0> ['F2', 'R2']
<__main__.RubiksState object at 0x7b4b925790> ['F2', 'R inverse']
<__main__.RubiksState object at 0x7b4b925850> ['F2', 'U']
<__main__.RubiksState object at 0x7b4b925910> ['F2', 'U2']
<__main__.RubiksState object at 0x7b4b9259d0> ['F2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b925a90> ['F2', 'D']
<__main__.RubiksState object at 0x7b4b925b50> ['F2', 'D2']
<__main__.RubiksState object at 0x7b4b925c10> ['F2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b925cd0> ['F2', 'F']
<__main__.RubiksState object at 0x7b4b925d90> ['F2', 'F2']
<__main__.RubiksState object at 0x7b4b925e50> ['F2', 'F inverse']
<__main__.RubiksState object at 0x7b4b925f10> ['F2', 'B']
<__main__.RubiksState object at 0x7b4b925fd0> ['F2', 'B2']
<__main__.RubiksState object at 0x7b4b926090> ['F2', 'B inverse']
<__main__.RubiksState object at 0x7b4b925390> ['F inverse', 'L']
<__main__.RubiksState object at 0x7b4b926190> ['F inverse', 'L2']
<__main__.RubiksState object at 0x7b4b926250> ['F inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b926310> ['F inverse', 'R']
<__main__.RubiksState object at 0x7b4b9263d0> ['F inverse', 'R2']
<__main__.RubiksState object at 0x7b4b926490> ['F inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b926550> ['F inverse', 'U']
<__main__.RubiksState object at 0x7b4b926610> ['F inverse', 'U2']
<__main__.RubiksState object at 0x7b4b9266d0> ['F inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b926790> ['F inverse', 'D']
<__main__.RubiksState object at 0x7b4b926850> ['F inverse', 'D2']
<__main__.RubiksState object at 0x7b4b926910> ['F inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b9269d0> ['F inverse', 'F']
<__main__.RubiksState object at 0x7b4b926a90> ['F inverse', 'F2']
<__main__.RubiksState object at 0x7b4b926b50> ['F inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b926c10> ['F inverse', 'B']
<__main__.RubiksState object at 0x7b4b926cd0> ['F inverse', 'B2']
<__main__.RubiksState object at 0x7b4b926d90> ['F inverse', 'B inverse']
<__main__.RubiksState object at 0x7b4b926090> ['B', 'L']
<__main__.RubiksState object at 0x7b4b926e90> ['B', 'L2']
<__main__.RubiksState object at 0x7b4b926f50> ['B', 'L inverse']
<__main__.RubiksState object at 0x7b4b927010> ['B', 'R']
<__main__.RubiksState object at 0x7b4b9270d0> ['B', 'R2']
<__main__.RubiksState object at 0x7b4b927190> ['B', 'R inverse']
<__main__.RubiksState object at 0x7b4b927250> ['B', 'U']
<__main__.RubiksState object at 0x7b4b927310> ['B', 'U2']
<__main__.RubiksState object at 0x7b4b9273d0> ['B', 'Up inverse']
<__main__.RubiksState object at 0x7b4b927490> ['B', 'D']
<__main__.RubiksState object at 0x7b4b927550> ['B', 'D2']
<__main__.RubiksState object at 0x7b4b927610> ['B', 'Down inverse']
<__main__.RubiksState object at 0x7b4b9276d0> ['B', 'F']
<__main__.RubiksState object at 0x7b4b927790> ['B', 'F2']
<__main__.RubiksState object at 0x7b4b927850> ['B', 'F inverse']
<__main__.RubiksState object at 0x7b4b927910> ['B', 'B']
<__main__.RubiksState object at 0x7b4b9279d0> ['B', 'B2']
<__main__.RubiksState object at 0x7b4b927a90> ['B', 'B inverse']
<__main__.RubiksState object at 0x7b4b926d90> ['B2', 'L']
<__main__.RubiksState object at 0x7b4b927b90> ['B2', 'L2']
<__main__.RubiksState object at 0x7b4b927c50> ['B2', 'L inverse']
<__main__.RubiksState object at 0x7b4b927d10> ['B2', 'R']
<__main__.RubiksState object at 0x7b4b927dd0> ['B2', 'R2']
<__main__.RubiksState object at 0x7b4b927e90> ['B2', 'R inverse']
<__main__.RubiksState object at 0x7b4b927f50> ['B2', 'U']
<__main__.RubiksState object at 0x7b4b927fd0> ['B2', 'U2']
<__main__.RubiksState object at 0x7b4b928110> ['B2', 'Up inverse']
<__main__.RubiksState object at 0x7b4b9281d0> ['B2', 'D']
<__main__.RubiksState object at 0x7b4b928290> ['B2', 'D2']
<__main__.RubiksState object at 0x7b4b928350> ['B2', 'Down inverse']
<__main__.RubiksState object at 0x7b4b928410> ['B2', 'F']
<__main__.RubiksState object at 0x7b4b9284d0> ['B2', 'F2']
<__main__.RubiksState object at 0x7b4b928590> ['B2', 'F inverse']
<__main__.RubiksState object at 0x7b4b928650> ['B2', 'B']
<__main__.RubiksState object at 0x7b4b928710> ['B2', 'B2']
<__main__.RubiksState object at 0x7b4b9287d0> ['B2', 'B inverse']
<__main__.RubiksState object at 0x7b4b928050> ['B inverse', 'L']
<__main__.RubiksState object at 0x7b4b9288d0> ['B inverse', 'L2']
<__main__.RubiksState object at 0x7b4b928990> ['B inverse', 'L inverse']
<__main__.RubiksState object at 0x7b4b928a50> ['B inverse', 'R']
<__main__.RubiksState object at 0x7b4b928b10> ['B inverse', 'R2']
<__main__.RubiksState object at 0x7b4b928bd0> ['B inverse', 'R inverse']
<__main__.RubiksState object at 0x7b4b928c90> ['B inverse', 'U']
<__main__.RubiksState object at 0x7b4b928d50> ['B inverse', 'U2']
<__main__.RubiksState object at 0x7b4b928e10> ['B inverse', 'Up inverse']
<__main__.RubiksState object at 0x7b4b928ed0> ['B inverse', 'D']
<__main__.RubiksState object at 0x7b4b928f90> ['B inverse', 'D2']
<__main__.RubiksState object at 0x7b4b929050> ['B inverse', 'Down inverse']
<__main__.RubiksState object at 0x7b4b929110> ['B inverse', 'F']
<__main__.RubiksState object at 0x7b4b9291d0> ['B inverse', 'F2']
<__main__.RubiksState object at 0x7b4b929290> ['B inverse', 'F inverse']
<__main__.RubiksState object at 0x7b4b929350> ['B inverse', 'B']
<__main__.RubiksState object at 0x7b4b929410> ['B inverse', 'B2']
<__main__.RubiksState object at 0x7b4b9294d0> ['B inverse', 'B inverse']

[Program finished]

"""

class RubiksState(object):
#	def __init__(self, moves):
	def __init__(self, left_face, front_face, right_face, back_face, top_face, down_face, moves):
		self.ulb = [0] * 3
		self.urb = [0] * 3
		self.ulf = [0] * 3
		self.urf = [0] * 3
		self.dlb = [0] * 3
		self.drb = [0] * 3
		self.drf = [0] * 3
		self.dlf = [0] * 3
		
		self.ulb[0] = top_face[0]
		self.ulb[1] = left_face[0]
		self.ulb[2] = back_face[1]
		self.urb[0] = top_face[1]
		self.urb[1] = left_face[1]
		self.urb[2] = back_face[0]
		self.ulf[0] = top_face[2]
		self.ulf[1] = left_face[1]
		self.ulf[2] = front_face[0]
		self.urf[0] = top_face[3]
		self.urf[1] = right_face[1]
		self.urf[2] = front_face[1]
		self.dlb[0] = down_face[2]
		self.dlb[1] = left_face[2]
		self.dlb[2] = back_face[2]
		self.drb[0] = down_face[3]
		self.drb[1] = right_face[3]
		self.drb[2] = back_face[2]
		self.drf[0] = back_face[1]
		self.drf[1] = right_face[2]
		self.drf[2] = front_face[3]
		self.dlf[0] = down_face[0]
		self.dlf[1] = left_face[3]
		self.dlf[2] = front_face[2]
		self.left_face = left_face
		self.front_face = front_face
		self.right_face = right_face
		self.back_face = back_face
		self.top_face = top_face
		self.down_face = down_face
		self.moves = moves

	def L(self):
		""" Down left front becomes up left front. Down left back becomes down left front. Up left back becomes down left back, up left front becomes up left back """
		elcopy = self.moves.copy()
		elcopy.append("L")
		return RubiksState(left_face, front_face, right_face, back_face, top_face, down_face, elcopy)
	def L2(self):
		""" Up left back brcomes down left front, down left back becomes up left front. Down left front becomes up left back. Down left back becomes up left front """
		elcopy = self.moves.copy()
		elcopy.append("L2")
		return RubiksState(elcopy)
		pass
	def Linv(self):
		""" Down left front becomes down left back. Down left back becomes up left back. Up left back becomes up left front. Up left front becomes down left front """
		elcopy = self.moves.copy()
		elcopy.append("L inverse")
		return RubiksState(elcopy)
		pass
	def R(self):
		""" Up right front becomes up right back. Up right back becomes Down right back, Down right back befomes Down Right Front, Down Right Front becomes Up Right Front """
		elcopy = self.moves.copy()
		elcopy.append("R")
		return RubiksState(elcopy)
		pass
	def R2(self):
		elcopy = self.moves.copy()
		elcopy.append("R2")
		return RubiksState(elcopy)
		pass
	def Rinv(self):
		elcopy = self.moves.copy()
		elcopy.append("R inverse")
		return RubiksState(elcopy)
		pass
	def U(self):
		elcopy = self.moves.copy()
		elcopy.append("U")
		return RubiksState(elcopy)
		pass
	def U2(self):
		elcopy = self.moves.copy()
		elcopy.append("U2")
		return RubiksState(elcopy)
		pass
	def Uinv(self):
		elcopy = self.moves.copy()
		elcopy.append("Up inverse")
		return RubiksState(elcopy)
		pass
	def D(self):
		elcopy = self.moves.copy()
		elcopy.append("D")
		return RubiksState(elcopy)
		pass
	def D2(self):
		elcopy = self.moves.copy()
		elcopy.append("D2")
		return RubiksState(elcopy)
		pass
	def Dinv(self):
		elcopy = self.moves.copy()
		elcopy.append("Down inverse")
		return RubiksState(elcopy)
		pass
	def F(self):
		elcopy = self.moves.copy()
		elcopy.append("F")
		return RubiksState(elcopy)
		pass
	def F2(self):
		elcopy = self.moves.copy()
		elcopy.append("F2")
		return RubiksState(elcopy)
		pass
	def Finv(self):
		elcopy = self.moves.copy()
		elcopy.append("F inverse")
		return RubiksState(elcopy)
		pass
	def B(self):
		elcopy = self.moves.copy()
		elcopy.append("B")
		return RubiksState(elcopy)
		pass
	def B2(self):
		elcopy = self.moves.copy()
		elcopy.append("B2")
		return RubiksState(elcopy)
		pass
	def Binv(self):
		elcopy = self.moves.copy()
		elcopy.append("B inverse")
		return RubiksState(elcopy)
		pass
		
	def is_solved(self):
		if self.left_face == [] and self.front_face == [] and self.right_face == [] and self.back_face == [] and self.top_face == [] and self.down_face == []:
				return True
		else:
				return False

#def extL(o):
#	o.moves.append("L")
#	pass
#def extL2(o):
#	o.moves.append("L2")
#	pass
#def extLinv(o):
#	o.moves.append("L inverse")
#	pass
#	def extR(o):
#		o.moves.append("R")
#		return RubiksState(self.moves)
#		pass
#	def extR2(o):
#		o.moves.append("R2")
#		return RubiksState(self.moves)
#		pass
#	def extRinv(o):
#		o.moves.append("R inverse")
#		return RubiksState(self.moves)
#		pass
#	def extU(o):
#		o.moves.append("U")
#		return RubiksState(self.moves)
#		pass
#	def extU2(o):
#		o.moves.append("U2")
#		return RubiksState(self.moves)
#		pass
#	def extUinv(self):
#		o.moves.append("Up inverse")
#		return RubiksState(self.moves)
#		pass
#	def extD(o):
#		o.moves.append("D")
#		return RubiksState(self.moves)
#		pass
#	def extD2(o):
#		o.moves.append("D2")
#		return RubiksState(self.moves)
#		pass
#	def extDinv(o):
#		o.moves.append("Down inverse")
#		return RubiksState(self.moves)
#		pass
#	def extF(o):
#		o.moves.append("F")
#		return RubiksState(self.moves)
#		pass
#	def extF2(o):
#		o.moves.append("F2")
#		return RubiksState(self.moves)
#		pass
#	def extFinv(o):
#		o.moves.append("F inverse")
#		return RubiksState(self.moves)
#		pass
#	def extB(o):
#		o.moves.append("B")
#		return RubiksState(self.moves)
#		pass
#	def extB2(o):
#		o.moves.append("B2")
#		return RubiksState(self.moves)
#		pass
#	def extBinv(o):
#		o.moves.append("B inverse")
#		return RubiksState(self.moves)
#		pass

def CharlesTruscottRubiks():
	item = RubiksState([])
	state = deque([])
	state.append(item)
#	moves = [lambda s: extL(s), lambda s: extL2(s), lambda s: extLinv(s)]
	
#	for move in moves:
#		state.append(move(item))
#	for s in state:
#		print(s, s.moves)
	moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.Dinv(), lambda s: s.F(), lambda s: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]
	print(state[0].moves)
	for move in moves:
		e = move(RubiksState([]))
		state.append(e)
	state.popleft()
	c = 0
#	for move in moves:
#		for s in state:
#			print(s, s.moves, move(s).moves)

	while c < 18:
		elem = state.popleft()
		for move in moves:
			state.append(move(elem))
			print(move(elem), move(elem).moves)
		c += 1
#	c = 1
#	for s in state:
#		print(s, s.moves, moves[c](s))
	
#	n = 0
#	for c in range(len(state)):
#		print("state[c] moves {}, c {}".format(state[c].moves, c))
#		state.append(moves[0](state[c]))
#	#	state.append([])
#		state[c + 18] = moves[0](state[c])
#		state.append([])
#		state[c + 19] = moves[1](state[c])
#		state.append([])
#		state[c + 20] = moves[2](state[c])
#		state.append([])
#		state[c + 21] = moves[3](state[c])
#		state.append([])
#	for s in state:
#		print(s, s.moves)
#	c = 0
#	c2 = 0
#	while c < len(moves):
#		c += 1
#		e = RubiksState(state.popleft().moves)
#		s1 = moves[0]
#		s2 = moves[1]
#		s3 = moves[2]
#		s4 = moves[3]
#		s5 = moves[4]
#		s6 = moves[5]
#		s7 = moves[6]
#		s8 = moves[7]
#		s9 = moves[8]
#		s10 = moves[9]
#		s11 = moves[10]
#		s12 = moves[11]
#		s13 = moves[12]
#		s14 = moves[13]
#		s15 = moves[14]
#		s16 = moves[15]
#		s17 = moves[16]
#		s18 = moves[17]
#		s19 = moves[18]
#		state.append(s1(e))
#		state.append(s2(e))
#		state.append(s3(e))
#		state.append(s4(e))
#		state.append(s5(e))
#		state.append(s6(e))
#		state.append(s7(e))
#		state.append(s8(e))
#		state.append(s9(e))
#		state.append(s10(e))
#		state.append(s11(e))
#		state.append(s12(e))
#		state.append(s13(e))
#		state.append(s14(e))
#		state.append(s15(e))
#		state.append(s16(e))
#		state.append(s17(e))
#		state.append(s18(e))
#		print(e, e.moves)
#	for s in state:
#		print(s, s.moves)
#	for n in range(len(state)):
#		t = state.popleft()
#		e = RubiksState(t.moves)
#		state.append(RubiksState(moves[0](e).moves))
#		state.append(RubiksState(moves[1](e).moves))
#		print(t, t.moves)
#		print(t, t.moves)
#	for s in state:
#		print(s, s.moves)
#	c = 0
#	while state and c < len(moves):
#		e = state.popleft()
#		state.append(RubiksState(moves[c](e).moves))
#		c += 1
#	for s in state:
#		print(s, s.moves)
#			print(moves[l](state[n]).moves)
#	L = deque([0])
#	solved = False
#	while solved  != True:
#		elem  = L.popleft()
#		if elem == 10:
#			solved = True
#			break
#		else:
#			L.append(elem + 1)
#		print (L)
#		

def CharlesTruscottSim():
#	left_face, front_face, right_face, back_face, top_face, down_face, moves
	left = ["G", "R", "B", "O"]
	front = ["B", "G", "G", "G"]
	right = ["R", "B", "R", "B"]
	back = ["O", "O", "O", "R"]
	top =["W", "W", "W", "W"]
	down = ["Y", "Y", "Y", "Y"]
	cube = RubiksState(left, front, right, back, top, down, [])
	print(cube.left_face, cube.front_face, cube.right_face, cube.back_face, cube.top_face, cube.down_face)
#	Needed = True
#	while Needed:
#		s = str(input("Enter a move"))
#		if s == "quit":
#			Needed = False
#			exit()
#		if s == "L":
#			cube = cube.L()
#			print(cube.left_face)
#			print(cube.front_face)
#			print(cube.right_face)
#			print(cube.back_face)
#			print(cube.top_face)
#			print(cube.down_face)
CharlesTruscottSim()
#CharlesTruscottRubiks()