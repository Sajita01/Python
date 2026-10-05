# Turn seconds into hours, minutes and seconds with divmod(). The function returns 3 values, so unpack them.

def convert(seconds):
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, secs

#  ask the user for seconds with int(input())
seconds = int(input("Enter seconds: "))
h, m, s = convert(seconds)
print(f"{h} h {m} m {s} s")

# Convert hours, minutes and seconds back to seconds
def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


"""
Output:
Enter seconds: 56532
15 h 42 m 12 s

"""