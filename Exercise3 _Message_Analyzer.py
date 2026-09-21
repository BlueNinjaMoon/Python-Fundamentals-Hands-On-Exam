#Christian Lehman

mssg = input("Enter a message: ").strip()
mssgfirst3 = mssg[0:3]
mssglast3 = mssg[3:7]
everysecondchr = mssg[::2]
reversed = mssg[::-1]
print(f"Message: {mssg}")
print(f"Length: {len(mssg)}")
print(f"First Character: {mssg[0]}")
print(f"Last Character: {mssg[-1]}")
print(f"First 3: {mssgfirst3}")
print(f"Last 3: {mssglast3}")
print(f"Every Second Character: {everysecondchr}")
print(f"Reversed: {reversed}")