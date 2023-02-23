class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        used = set()
        used2 = set()
        dist = [x for x in deck if x not in used and (used.add(x) or True)]
        count = [deck.count(x) for x in dist if deck.count(x)>1 ]
        if len(count)==len(dist) and len(set(count)) ==1 or len(set([x%gcd(*count) for x in count if gcd(*count)>1]))==1 and len(count) == len(dist):
            return True
        else:
            return False