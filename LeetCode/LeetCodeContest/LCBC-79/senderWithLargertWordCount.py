# TC = O(N*W) where N is the no. of messages and and W is the individual message length.
# SC = O(N)

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        def word_counter(i):
            words = messages[i].split(' ')
            return len(words)

        sender_map = {}
        for s in range(len(senders)):
            sender_map[senders[s]] = word_counter(s) + sender_map.get(senders[s], 0)

        max_message = float('-inf')
        max_sender = ''
        for sender in sender_map:
            if sender_map[sender] > max_message:
                max_message = sender_map[sender]
                max_sender = sender
            elif sender_map[sender] == max_message:
                max_sender = max(sender, max_sender)

        return max_sender