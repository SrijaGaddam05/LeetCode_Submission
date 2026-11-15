class Solution:
    def compress(self, chars: list[str]) -> int:
        write =0
        read=0
        while read<len(chars):
            character=chars[read]
            count=0
            while read< len(chars) and chars[read]==character:
                read +=1
                count +=1
            chars[write]=character
            write +=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit 
                    write +=1
        return write      