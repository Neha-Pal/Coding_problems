# Given the start time st and end time et of a race in the format hh:mm:ss. You task is to print the time taken to complete the race.

# Example 1:

# Input: st = 13:50:45
# et = 14:55:50
# Output: 01:05:05
# Explaination: The time gap is 1 hour 5 
# minutes and 5 seconds.

class Solution:
    def timeGap(self, st, et):
        st_hours, st_mins, st_seconds = map(int, st.split(':'))
        et_hours, et_mins, et_seconds = map(int, et.split(':'))

        st_seconds = (st_hours * 3600) + (st_mins * 60) + st_seconds
        et_seconds = (et_hours * 3600) + (et_mins * 60) + et_seconds

        time_diff = et_seconds - st_seconds

        if time_diff < 0:
            time_diff += 24 * 3600

        hours = time_diff // 3600
        mins = (time_diff % 60) //60
        secs = time_diff % 60

        return f"{hours:02}:{mins:02}:{secs:02}"
    

st = "13:50:45"
et = "14:55:50"

sol = Solution()
print(sol.timeGap(st, et))