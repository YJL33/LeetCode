class Solution:
    def minimumBuckets(self, street: str) -> int:
        if 'H' not in street: return 0
        if '.' not in street: return -1
        if street[:2] == 'HH' or street[-2:] == 'HH' or 'HHH' in street: return -1
        cnt = 0
        lastBucket = None
        lastUncollected = None
        for i in range(len(street)):
            c = street[i]
            # when there's a house, check it's collected or not
            # if yes, either:
            #    a. see if there's an uncollected earlier
            #    b. continue
            # if not, mark it as uncollected
            # when there's a empty space, check there's an uncollected or not
            # if yes, mark it as bucket
            # if not, continue
            if c == 'H':
                if lastUncollected:
                    if street[lastUncollected-1] == '.':
                        lastUncollected, cnt = None, cnt+1
                    else:
                        return -1
                if lastBucket == i-1:
                    lastBucket, lastUncollected = None, None
                    continue
                else:
                    lastUncollected = i
            else:
                if lastUncollected == i-1:
                    lastBucket, lastUncollected = i, None
                    cnt += 1
                # elif lastBucket == i-2 and street[i+1] == 'H':
                #     lastBucket = i
                else:
                    continue
        
        if lastUncollected:
            return cnt+1 if street[-2] == '.' else -1
        
        return cnt