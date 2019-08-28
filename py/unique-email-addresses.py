'''
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the
domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address,
mail sent there will be forwarded to the same address without dots in the local name.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be
ignored. This allows certain emails to be filtered, for example m.y+name@email.com will
be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list. 

** How many different addresses actually receive mails? 

 

Example 1:
Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2

Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:
1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
'''

# Best runtime approach
# Append all emails after filtering, then return the length of its set()
class Solution1:
    def numUniqueEmails(self, emails: [str]) -> int:
        res = []
        # res = set()
        for email in emails:
            name, domain = email.split('@')
            # name = email.split('@')[0]
            # domain = email.split('@')[1]
            name = name.split('+')[0].replace('.', '')
            res.append(name + '@' + domain)
            # res.add(name + '@' + domain)
        return len(set(res))

# Space efficient approach
class Solution1:
    def numUniqueEmails(self, emails: [str]) -> int:
        res = []
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            # curr = name + '@' + domain
            if name + '@' + domain not in res:
                res.append(name + '@' + domain)
        return len(res)

# Helper function
class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        
        def preprocess(email: str) -> str:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            if '+' in name:
                name = name[:name.find('+')]
            return f'{name}@{domain}'
        
        # Call helper function on every email
        emails = list(map(preprocess, emails))
        seen = []
        count = 0
        for email in emails:
            if email not in seen:
                seen.append(email)
                count += 1
        return count



s1 = Solution()
inp = ["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]
print(s1.numUniqueEmails(inp))
























