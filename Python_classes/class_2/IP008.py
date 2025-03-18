# SB - start baking
# B - baking time
# CF - cake off

SB_H = int(input()) 
SB_M = int(input())
SB_S = int(input())

B_H = int(input())
B_M = int(input())
B_S = int(input())

# Calculate the total seconds
total_seconds = SB_H * 3600 + SB_M * 60 + SB_S + B_H * 3600 + B_M * 60 + B_S

# Calculate the removal time
CF_hour = total_seconds // 3600 % 24
CF_minute = (total_seconds // 60) % 60
CF_second = total_seconds % 60


print(f"Take the cake out at {CF_hour:02d}:{CF_minute:02d}:{CF_second:02d}.")