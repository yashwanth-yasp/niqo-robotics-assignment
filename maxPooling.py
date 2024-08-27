import collections

def maxSlidingWindow(nums, k):

    d = collections.deque()
    out = []
    nums_len = len(nums)

    for i, n in enumerate(nums):

        while d and nums[d[-1]] < n:
            d.pop()

        d.append(i)

        if d[0] == i - k:
            d.popleft()

        if i>=k-1:
            out.append(nums[d[0]])

    for i in range(len(nums) - len(out)):
      out.append(0)
    return out


def max_pooling(input_matrix, window_size):

  if window_size <= 1:
    return input_matrix

  if window_size >= len(input_matrix):
    return max(map(max, input_matrix))


  m = len(input_matrix)

  output_matrix = []
  for i in range(len(input_matrix)):
    output_matrix.append(maxSlidingWindow(input_matrix[i], window_size))

  output_matrix = list(map(list, zip(*output_matrix)))

  for i in range(len(output_matrix)):
    output_matrix[i] = maxSlidingWindow(output_matrix[i], window_size)


  output_matrix = list(map(list, zip(*output_matrix)))


  return output_matrix


"""
9 2 3 4
8 6 5 7
1 3 2 6
4 5 9 8
"""

matrix = [[9, 2, 3, 4],
          [8, 6, 5, 7],
          [1, 3, 2, 6],
          [4, 5, 9, 8]]
window_size = 2

print(max_pooling(matrix, window_size))


# the result is a 3x3 matrix padded by 0's on the last row and last column
