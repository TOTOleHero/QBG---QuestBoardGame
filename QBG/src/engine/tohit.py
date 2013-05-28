# inspired from https://code.google.com/p/dquest/source/browse/trunk/ToHit.d


class ToHit: 
      def __init__(self):  
        
          self._uba_chart  = [
                    [4, 4, 5, 6, 6, 6, 6, 6, 6, 6],
                    [3, 4, 4, 4, 5, 5, 6, 6, 6, 6],
                    [2, 3, 4, 4, 4, 4, 5, 5, 5, 6],
                    [2, 3, 3, 4, 4, 4, 4, 4, 5, 5],
                    [2, 3, 3, 3, 4, 4, 4, 4, 4, 4],
                    [2, 3, 3, 3, 3, 4, 4, 4, 4, 4],
                    [2, 3, 3, 3, 3, 3, 4, 4, 4, 4],
                    [2, 2, 3, 3, 3, 3, 3, 4, 4, 4],
                    [2, 2, 2, 3, 3, 3, 3, 3, 4, 4],
                    [2, 2, 2, 2, 3, 3, 3, 3, 3, 4]]
        
      def get(self,attacker,defender) :
                return self._uba_chart[attacker-1][defender-1]
        
if __name__ == "__main__":
        
  toHit = ToHit()
	print toHit.get(5,6)
