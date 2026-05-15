class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each string:
        # Store sorted in other var
        # If sort_str in hashmap, then append actual to value (list of strs)
            # Need to check and explain why appending is O(1) time
        # Iterate thru hashmap, return array of arrays :)
        # Only problem is I don't know the time compelxity with sorting
        
        groups = {}
        sorted_string = ""
        
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in groups:
                groups[sorted_string].append(string)
                continue
            groups[sorted_string] = [string]
            
        return list(groups.values())
