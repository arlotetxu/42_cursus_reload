'''
Write a function that counts the number of valid consecutive digits pair in a
string. A valid pair consist of two adjacent digits where the second digit is
exactly one greater than the first digit. A 9 followed by a 0 is NOT a valid
pair and only consider consecutive characters that are both digits (0-9).

def pattern_tracker(text: str) -> int:


Input: “123”
Expected: 2

Input: “12a34”
Expected: 2

Input: “987654321”
Expected: 0

Input: “01234567”
Expected: 7

Input: “abc”
Expected: 0

Input: “1a2b3c4”
Expected: 0

Input: “112233”
Expected: 2

Input: “12”
Expected: 1

Input: “23”
Expected: 1

Input: “123456”
Expected: 5
'''

def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(1, int(len(text))):
        try:
            current = int(text[i])
            prev = int(text[i - 1])
        except Exception:
            continue
        if current - 1 == prev:
            count += 1
    print(count)
    return count


pattern_tracker("123")
pattern_tracker("12a34")
pattern_tracker("987654321")
pattern_tracker("01234567")
pattern_tracker("1a2b3c4")
pattern_tracker("112233")
pattern_tracker("12")
pattern_tracker("23")
pattern_tracker("123456")
