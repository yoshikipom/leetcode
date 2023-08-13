#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local, domain = email.split('@', 1)
            unique_local = local.split('+')[0]
            unique_local = unique_local.replace('.', '')
            s.add(unique_local + '@' + domain)
        return len(s)
        
# @lc code=end
