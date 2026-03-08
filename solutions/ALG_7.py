# Task: Merge overlapping intervals
# Write a Python function merge_intervals(intervals: list[list[int]]) -> list[list[int]]
#
# Each interval is represented as [start, end].
# If intervals overlap, they should be merged.
#
# Example:
# [[1,3],[2,6],[8,10],[15,18]]
#
# Output:
# [[1,6],[8,10],[15,18]]

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Check if there is an overlap
        if current[0] <= last_merged[1]:  # Overlap exists
            # Merge the intervals by updating the end time
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add the current interval to merged list
            merged.append(current)

    return merged