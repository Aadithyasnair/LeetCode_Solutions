"""
Problem ID : 3921
Title      : Score Validator
Language   : Python
Solved Date: 2026-08-08
"""
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in events:
            if counter<10:
                if i.isdigit():
                    score+=int(i)
                else:
                    if i=='W':
                        counter+=1
                    elif i=='WD':
                        score+=1
                    elif i=='NB':
                        score+=1
        return ([score,counter])