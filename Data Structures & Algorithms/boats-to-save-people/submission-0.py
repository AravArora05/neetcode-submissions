class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #integer array where people[i] is weight of i person
        people.sort()
        r=len(people)-1
        l=0
        count=0
        while l<=r:
            #bc if same that guy should be accounted for
            if people[l]+people[r]<=limit:
                l+=1
            count+=1
            r-=1
        return count
                
        #you want it sorted